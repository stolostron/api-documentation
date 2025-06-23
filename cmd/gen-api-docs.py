# Copyright (c) 2025 Red Hat, Inc.
# Copyright Contributors to the Open Cluster Management project


import os
import re
import yaml
from collections import defaultdict

# List of folder names to ignore during file search
IGNORED_FOLDERS = ['vendor', '.github', '.git', 'hack']

# Global search directory
search_dir = '.'

def is_primitive(go_type):
    primitives = {'string', 'int', 'int32', 'int64', 'float32', 'float64', 'bool', 'byte', 'rune', 'uint', 'uint32', 'uint64', 'map', '[]byte', 'interface{}'}
    # Also treat slices and maps of primitives as primitives
    if go_type.startswith('[]'):
        return is_primitive(go_type[2:])
    if go_type.startswith('map['):
        return True
    if go_type in primitives:
        return True
    # Well-known k8s types
    if go_type.startswith('metav1.') or go_type.startswith('corev1.'):
        return True
    return False

def find_go_struct(type_name, go_files):
    # Look for a struct definition with the exact type name
    struct_regex = re.compile(r'type ' + re.escape(type_name) + r' struct {([^}]*)}', re.MULTILINE | re.DOTALL)
    for file_path in go_files:
        with open(file_path, 'r') as f:
            content = f.read()
            match = struct_regex.search(content)
            if match:
                return match.group(1), file_path, content
    # If not found, look for an embedded struct (i.e., a struct field without a name)
    embedded_regex = re.compile(r'type \w+ struct {([^}]*)}', re.MULTILINE | re.DOTALL)
    for file_path in go_files:
        with open(file_path, 'r') as f:
            content = f.read()
            for match in embedded_regex.finditer(content):
                struct_body = match.group(1)
                for line in struct_body.split('\n'):
                    line = line.strip()
                    if not line or line.startswith('//'):
                        continue
                    parts = line.split()
                    if len(parts) == 1 and parts[0] == type_name:
                        return struct_body, file_path, content
    return None, None, None

def parse_go_struct(type_name, go_files, parsed_types):
    if type_name in parsed_types:
        return {'kind': type_name, 'fields': [{'name': '...', 'type': '', 'description': 'Recursive reference to ' + type_name, 'validations': []}]}
    parsed_types.add(type_name)
    struct_body, file_path, content = find_go_struct(type_name, go_files)
    if not struct_body:
        return {'kind': type_name, 'fields': [{'name': '...', 'type': '', 'description': f'Definition for {type_name} not found', 'validations': []}]}
    struct_comment = ''
    struct_comment_match = re.search(r'// ([^\n]+)\n(.*\n)*?type ' + re.escape(type_name), content)
    if struct_comment_match:
        struct_comment = struct_comment_match.group(1).strip()
    fields = []
    for line in struct_body.split('\n'):
        line = line.strip()
        if not line or line.startswith('//'):
            continue
        parts = line.split()
        # Embedded field: only a type, no name
        if len(parts) == 1:
            embedded_type = parts[0]
            if not is_primitive(embedded_type):
                embedded_struct = parse_go_struct(embedded_type, go_files, parsed_types)
                # Inline the embedded struct's fields into the parent
                fields.extend(embedded_struct['fields'])
            continue
        if len(parts) < 2:
            continue
        field_name = parts[0]
        field_type = parts[1]
        json_tag = ""
        if '`json:"' in line:
            json_tag_match = re.search(r'`json:"([^"]+)"`', line)
            if json_tag_match:
                json_tag = json_tag_match.group(1).split(',')[0]
        field_comment_regex = re.compile(r"// ([^\n]+)\n\s*" + re.escape(field_name) + r"\s")
        comment_match = field_comment_regex.search(content)
        description = comment_match.group(1).strip() if comment_match else "No description provided."
        field_info = {
            'name': json_tag or field_name,
            'type': field_type,
            'description': description,
            'validations': []
        }
        tag_regex = re.compile(r"// \\+kubebuilder:validation:([^\n]+)\n\s*" + re.escape(field_name))
        tag_matches = tag_regex.findall(content)
        for tag in tag_matches:
            field_info['validations'].append(tag.strip())
        if not is_primitive(field_type):
            field_info['inline'] = parse_go_struct(field_type, go_files, parsed_types)
        fields.append(field_info)
    return {'kind': type_name, 'description': struct_comment, 'fields': fields}

def parse_go_file(file_path, go_files, parsed_types=None):
    if parsed_types is None:
        parsed_types = set()
    # Find the main Kind in the file
    with open(file_path, 'r') as f:
        content = f.read()
    kind_match = re.search(r'type (\w+) struct', content)
    if not kind_match:
        return None
    kind = kind_match.group(1)
    # Find the Spec struct for this Kind
    spec_struct_name = kind + 'Spec'
    return parse_go_struct(spec_struct_name, go_files, parsed_types)

def parse_crd_file(file_path):
    with open(file_path, 'r') as f:
        try:
            crd = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file {file_path}: {e}")
            return None
    if not crd or crd.get('kind') != 'CustomResourceDefinition':
        return None

    def parse_schema_fields(schema):
        fields = []
        for field, properties in schema.items():
            field_info = {
                'name': field,
                'type': properties.get('type', 'N/A'),
                'description': properties.get('description', 'No description provided.'),
                'validations': []
            }
            if field != '':
                if 'minimum' in properties:
                    field_info['validations'].append(f"Minimum={properties['minimum']}")
                if 'maximum' in properties:
                    field_info['validations'].append(f"Maximum={properties['maximum']}")
                if 'pattern' in properties:
                    field_info['validations'].append(f"Pattern={properties['pattern']}")
            if 'properties' in properties and properties.get('type').lower() == 'object':
                field_info['inline'] = {'fields': parse_schema_fields(properties['properties'])}
            if 'items' in properties:
                inline = parse_schema_fields({'': properties['items']})
                if inline and 'inline' in inline[0]:
                    field_info['inline'] = inline[0]['inline']
            if field_info != {}:
                fields.append(field_info)
        return fields

    try:
        # Check for 'spec' and 'status' fields in the CRD schema
        spec = crd.get('spec', {})
        names = spec.get('names', {})
        kind = names.get('kind')
        if not kind:
            return None
        crd_info = {
            'kind': kind,
            'description': "Description not found in CRD.",
            'fields': []
        }
        openapi_schema = spec['versions'][0]['schema']['openAPIV3Schema']
        properties = openapi_schema.get('properties', {})

        for field_name in properties:
            if field_name in ['spec', 'status']:
                field_schema = properties[field_name]
                schema = field_schema.get('properties', {})
                if 'description' in field_schema:
                    crd_info['description'+field_name] = field_schema['description']
                crd_info[field_name] = parse_schema_fields(schema)
    except (KeyError, IndexError) as e:
        print(f"Exception details: {e}")
        import traceback
        traceback.print_exc()
        pass
    return crd_info

def render_fields(fields, go_files, depth=0):
    md = ''
    indent = ''

    if depth > 0:
        indent = "&nbsp;" * ((depth - 1) * 4) +"└>" + "&nbsp;" * 2

    for field in fields:
        if isinstance(field, str):
            print(f"[DEBUG] Skipping string field: {field}")
            continue
        if not isinstance(field, dict):
            print(f"[DEBUG] Skipping non-dict field of type {type(field)}")
            continue
        validations = "<br>".join(f"`{v}`" for v in field.get('validations', [])) if field.get('validations') else "N/A"
        validations = validations.replace('|', '\\|')
        description = field.get('description', 'No description provided.').replace('\n', ' ')
        md += f"| {indent} **{field.get('name', 'N/A')}** | `{field.get('type', 'N/A')}` | {description} | {validations} |\n"
        if 'inline' in field and len(field['inline']) > 0:
            md += render_fields(field['inline']['fields'], go_files, depth+1)

    return md

def generate_markdown(crd_info, output_dir, go_files):
    kind = crd_info['kind']
    file_path = os.path.join(output_dir, f"{kind.lower()}_api.md")
    with open(file_path, 'w') as f:
        f.write(f"# {kind} API\n\n")
        f.write("## Spec Fields\n\n")
        f.write(f"{crd_info.get('descriptionspec', 'No description available.')}\n\n")
        f.write("| Field | Type | Description | Validations |\n")
        f.write("|:---|---|---|---|\n")
        f.write(render_fields(crd_info.get('spec', []), go_files))
        f.write("## Status Fields\n\n")
        f.write(f"{crd_info.get('descriptionstatus', 'No description available.')}\n\n")
        f.write("| Field | Type | Description | Validations |\n")
        f.write("|:---|---|---|---|\n")
        f.write(render_fields(crd_info.get('status', []), go_files))
    return f"{kind.lower()}_api.md"

def collect_go_type_files():
    go_type_files = []
    for root, _, files in os.walk(search_dir):
        if any(ignored in root.split(os.sep) for ignored in IGNORED_FOLDERS):
            continue
        for file in files:
            if file.endswith('.go') and not file.startswith('zz_generated') and not file.startswith('doc.go'):
                go_type_files.append(os.path.join(root, file))
    return go_type_files

def main():
    import sys
    global search_dir
    if len(sys.argv) > 1:
        search_dir = sys.argv[1]
    api_docs_dir = './api-docs'
    if not os.path.exists(api_docs_dir):
        os.makedirs(api_docs_dir)
    go_type_files = collect_go_type_files()
    crd_definitions = []
    kind_to_source = {}
    for root, _, files in os.walk(search_dir):
        if api_docs_dir.lstrip('./') in root:
            continue
        if any(ignored in root.split(os.sep) for ignored in IGNORED_FOLDERS):
            continue
        for file in files:
            crd_info = None
            file_path = os.path.join(root, file)
            if file.endswith('_types.go'):
                print(f"[DEBUG] Processing Go type file: {file_path}")
                crd_info = parse_go_file(file_path, go_type_files)
                source_type = 'go'
            elif file.endswith('.yaml') or file.endswith('.yml'):
                print(f"[DEBUG] Processing CRD file: {file_path}")
                crd_info = parse_crd_file(file_path)
                source_type = 'crd'
            if crd_info:
                kind = crd_info['kind']
                if kind in kind_to_source:
                    prev_source, prev_file = kind_to_source[kind]
                    if source_type == 'crd':
                        print(f"[DEBUG] Duplicate kind '{kind}' found in {file_path} (CRD) and {prev_file} ({prev_source}). Using CRD.")
                        # Replace previous entry with CRD
                        crd_definitions = [c for c in crd_definitions if c['kind'] != kind]
                        crd_definitions.append(crd_info)
                        kind_to_source[kind] = (source_type, file_path)
                    else:
                        print(f"[DEBUG] Duplicate kind '{kind}' found in {file_path} (Go) and {prev_file} ({prev_source}). Keeping previous (CRD if present).")
                        # Keep the previous (CRD) entry
                        continue
                else:
                    crd_definitions.append(crd_info)
                    kind_to_source[kind] = (source_type, file_path)
    if not crd_definitions:
        print("No CRD or type definitions with API documentation comments found.")
        return
    index_entries = []
    for crd_info in crd_definitions:
        md_file = generate_markdown(crd_info, api_docs_dir, go_type_files)
        index_entries.append({
            'kind': crd_info['kind'],
            'description': crd_info.get('description', 'No description available.'),
            'link': md_file
        })
    with open(os.path.join(api_docs_dir, 'README.md'), 'w') as f:
        f.write("# Advanced Cluster Management Custom Resource API Documentation\n\n")
        f.write("This document provides an overview of the Custom Resource Definitions (CRDs) used in this project.\n\n")
        for entry in index_entries:
            f.write(f"## {entry['kind']}\n\n")
            f.write(f"{entry['description']}\n\n")
            f.write(f"[View a detailed API Reference for {entry['kind']}]({entry['link']}).\n\n")
            f.write("---\n\n")
    print(f"API documentation generated successfully in the '{api_docs_dir}' directory.")

if __name__ == "__main__":
    main()