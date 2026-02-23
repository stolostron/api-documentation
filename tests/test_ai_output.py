#!/usr/bin/env python3
"""
Tests for AI-consumable output functionality in gen-api-docs.py
"""

import json
import os
import tempfile
import unittest

import yaml
import importlib.util

# Import the module
spec = importlib.util.spec_from_file_location(
    "gen_api_docs",
    os.path.join(os.path.dirname(__file__), '..', 'cmd', 'gen-api-docs.py')
)
gen_api_docs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen_api_docs)


class TestMetadataCapture(unittest.TestCase):
    """Test that parse_crd_file captures CRD metadata."""

    def setUp(self):
        self.crd_data = {
            'apiVersion': 'apiextensions.k8s.io/v1',
            'kind': 'CustomResourceDefinition',
            'metadata': {'name': 'samples.example.com'},
            'spec': {
                'group': 'example.com',
                'names': {
                    'kind': 'Sample',
                    'plural': 'samples',
                    'singular': 'sample',
                },
                'scope': 'Namespaced',
                'versions': [{
                    'name': 'v1alpha1',
                    'served': True,
                    'storage': True,
                    'schema': {
                        'openAPIV3Schema': {
                            'type': 'object',
                            'properties': {
                                'spec': {
                                    'type': 'object',
                                    'description': 'Spec description',
                                    'properties': {
                                        'name': {
                                            'type': 'string',
                                            'description': 'The name',
                                        }
                                    }
                                }
                            }
                        }
                    }
                }]
            }
        }

    def _write_and_parse(self, data):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(data, f)
            temp_file = f.name
        try:
            return gen_api_docs.parse_crd_file(temp_file)
        finally:
            os.unlink(temp_file)

    def test_group_captured(self):
        result = self._write_and_parse(self.crd_data)
        self.assertEqual(result['group'], 'example.com')

    def test_version_captured(self):
        result = self._write_and_parse(self.crd_data)
        self.assertEqual(result['version'], 'v1alpha1')

    def test_plural_captured(self):
        result = self._write_and_parse(self.crd_data)
        self.assertEqual(result['plural'], 'samples')

    def test_singular_captured(self):
        result = self._write_and_parse(self.crd_data)
        self.assertEqual(result['singular'], 'sample')

    def test_scope_captured(self):
        result = self._write_and_parse(self.crd_data)
        self.assertEqual(result['scope'], 'Namespaced')

    def test_cluster_scope(self):
        self.crd_data['spec']['scope'] = 'Cluster'
        result = self._write_and_parse(self.crd_data)
        self.assertEqual(result['scope'], 'Cluster')


class TestFieldAttributes(unittest.TestCase):
    """Test required, enum, and default field extraction."""

    def setUp(self):
        self.crd_data = {
            'apiVersion': 'apiextensions.k8s.io/v1',
            'kind': 'CustomResourceDefinition',
            'metadata': {'name': 'tests.example.com'},
            'spec': {
                'group': 'example.com',
                'names': {'kind': 'TestCRD', 'plural': 'tests', 'singular': 'test'},
                'scope': 'Namespaced',
                'versions': [{
                    'name': 'v1',
                    'served': True,
                    'storage': True,
                    'schema': {
                        'openAPIV3Schema': {
                            'type': 'object',
                            'properties': {
                                'spec': {
                                    'type': 'object',
                                    'required': ['name', 'mode'],
                                    'properties': {
                                        'name': {
                                            'type': 'string',
                                            'description': 'Resource name',
                                        },
                                        'mode': {
                                            'type': 'string',
                                            'description': 'Operating mode',
                                            'enum': ['active', 'passive', 'standby'],
                                            'default': 'active',
                                        },
                                        'optional': {
                                            'type': 'integer',
                                            'description': 'Optional field',
                                        }
                                    }
                                },
                                'status': {
                                    'type': 'object',
                                    'properties': {
                                        'phase': {
                                            'type': 'string',
                                            'enum': ['Pending', 'Running', 'Failed'],
                                        }
                                    }
                                }
                            }
                        }
                    }
                }]
            }
        }

    def _write_and_parse(self, data):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(data, f)
            temp_file = f.name
        try:
            return gen_api_docs.parse_crd_file(temp_file)
        finally:
            os.unlink(temp_file)

    def test_required_fields_marked(self):
        result = self._write_and_parse(self.crd_data)
        spec_fields = result.get('spec', [])
        name_field = next(f for f in spec_fields if f['name'] == 'name')
        mode_field = next(f for f in spec_fields if f['name'] == 'mode')
        optional_field = next(f for f in spec_fields if f['name'] == 'optional')
        self.assertTrue(name_field.get('required'))
        self.assertTrue(mode_field.get('required'))
        self.assertNotIn('required', optional_field)

    def test_enum_captured(self):
        result = self._write_and_parse(self.crd_data)
        spec_fields = result.get('spec', [])
        mode_field = next(f for f in spec_fields if f['name'] == 'mode')
        self.assertEqual(mode_field['enum'], ['active', 'passive', 'standby'])

    def test_default_captured(self):
        result = self._write_and_parse(self.crd_data)
        spec_fields = result.get('spec', [])
        mode_field = next(f for f in spec_fields if f['name'] == 'mode')
        self.assertEqual(mode_field['default'], 'active')

    def test_status_enum(self):
        result = self._write_and_parse(self.crd_data)
        status_fields = result.get('status', [])
        phase_field = next(f for f in status_fields if f['name'] == 'phase')
        self.assertEqual(phase_field['enum'], ['Pending', 'Running', 'Failed'])


class TestJsonSchema(unittest.TestCase):
    """Test JSON schema generation."""

    def setUp(self):
        self.crd_info = {
            'kind': 'Widget',
            'group': 'widgets.example.com',
            'version': 'v1beta1',
            'plural': 'widgets',
            'singular': 'widget',
            'scope': 'Namespaced',
            'description': 'A widget resource',
            'descriptionspec': 'Widget spec',
            'descriptionstatus': 'Widget status',
            'spec': [
                {
                    'name': 'size',
                    'type': 'integer',
                    'description': 'Widget size',
                    'required': True,
                    'validations': ['Minimum=1', 'Maximum=100'],
                },
                {
                    'name': 'color',
                    'type': 'string',
                    'description': 'Widget color',
                    'enum': ['red', 'green', 'blue'],
                    'default': 'red',
                    'validations': [],
                },
            ],
            'status': [
                {
                    'name': 'ready',
                    'type': 'boolean',
                    'description': 'Whether the widget is ready',
                    'validations': [],
                }
            ],
        }
        self.output_dir = tempfile.mkdtemp()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.output_dir)

    def test_json_schema_created(self):
        gen_api_docs.generate_json_schema(self.crd_info, self.output_dir)
        path = os.path.join(self.output_dir, 'Widget.json')
        self.assertTrue(os.path.exists(path))

    def test_json_schema_parseable(self):
        gen_api_docs.generate_json_schema(self.crd_info, self.output_dir)
        path = os.path.join(self.output_dir, 'Widget.json')
        with open(path) as f:
            data = json.load(f)
        self.assertEqual(data['kind'], 'Widget')
        self.assertEqual(data['apiVersion'], 'widgets.example.com/v1beta1')

    def test_json_schema_metadata(self):
        gen_api_docs.generate_json_schema(self.crd_info, self.output_dir)
        path = os.path.join(self.output_dir, 'Widget.json')
        with open(path) as f:
            data = json.load(f)
        meta = data['metadata']
        self.assertEqual(meta['group'], 'widgets.example.com')
        self.assertEqual(meta['version'], 'v1beta1')
        self.assertEqual(meta['plural'], 'widgets')
        self.assertEqual(meta['scope'], 'Namespaced')

    def test_json_schema_fields(self):
        gen_api_docs.generate_json_schema(self.crd_info, self.output_dir)
        path = os.path.join(self.output_dir, 'Widget.json')
        with open(path) as f:
            data = json.load(f)
        fields = data['spec']['fields']
        self.assertIn('size', fields)
        self.assertTrue(fields['size']['required'])
        self.assertEqual(fields['size']['validations']['minimum'], 1)
        self.assertIn('color', fields)
        self.assertEqual(fields['color']['enum'], ['red', 'green', 'blue'])
        self.assertEqual(fields['color']['default'], 'red')

    def test_json_schema_has_example_yaml(self):
        gen_api_docs.generate_json_schema(self.crd_info, self.output_dir)
        path = os.path.join(self.output_dir, 'Widget.json')
        with open(path) as f:
            data = json.load(f)
        self.assertIn('exampleYAML', data)
        self.assertIn('apiVersion:', data['exampleYAML'])


class TestExampleYaml(unittest.TestCase):
    """Test example YAML generation."""

    def test_example_yaml_parseable(self):
        crd_info = {
            'kind': 'Sample',
            'group': 'example.com',
            'version': 'v1alpha1',
            'scope': 'Namespaced',
            'spec': [
                {'name': 'name', 'type': 'string', 'description': 'Name',
                 'validations': []},
                {'name': 'replicas', 'type': 'integer', 'description': 'Replicas',
                 'validations': ['Minimum=1']},
            ],
        }
        result = gen_api_docs.generate_example_yaml(crd_info)
        parsed = yaml.safe_load(result)
        self.assertEqual(parsed['kind'], 'Sample')
        self.assertEqual(parsed['apiVersion'], 'example.com/v1alpha1')
        self.assertIn('namespace', parsed['metadata'])

    def test_cluster_scope_no_namespace(self):
        crd_info = {
            'kind': 'ClusterWidget',
            'group': 'example.com',
            'version': 'v1',
            'scope': 'Cluster',
            'spec': [
                {'name': 'enabled', 'type': 'boolean', 'description': 'Enabled',
                 'validations': []},
            ],
        }
        result = gen_api_docs.generate_example_yaml(crd_info)
        parsed = yaml.safe_load(result)
        self.assertNotIn('namespace', parsed.get('metadata', {}))

    def test_required_fields_preferred(self):
        crd_info = {
            'kind': 'Pref',
            'group': 'example.com',
            'version': 'v1',
            'scope': 'Namespaced',
            'spec': [
                {'name': 'optional1', 'type': 'string', 'description': '',
                 'validations': []},
                {'name': 'optional2', 'type': 'string', 'description': '',
                 'validations': []},
                {'name': 'required1', 'type': 'string', 'description': '',
                 'required': True, 'validations': []},
            ],
        }
        result = gen_api_docs.generate_example_yaml(crd_info)
        parsed = yaml.safe_load(result)
        self.assertIn('required1', parsed.get('spec', {}))
        # optional fields should not appear since required fields exist
        self.assertNotIn('optional1', parsed.get('spec', {}))

    def test_enum_default_used(self):
        crd_info = {
            'kind': 'EnumTest',
            'group': 'example.com',
            'version': 'v1',
            'scope': 'Namespaced',
            'spec': [
                {'name': 'mode', 'type': 'string', 'description': '',
                 'enum': ['fast', 'slow'], 'default': 'fast',
                 'required': True, 'validations': []},
            ],
        }
        result = gen_api_docs.generate_example_yaml(crd_info)
        parsed = yaml.safe_load(result)
        self.assertEqual(parsed['spec']['mode'], 'fast')


class TestIndex(unittest.TestCase):
    """Test index.json generation."""

    def setUp(self):
        self.output_dir = tempfile.mkdtemp()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.output_dir)

    def test_index_created(self):
        crds = [
            {'kind': 'Alpha', 'group': 'g.io', 'version': 'v1',
             'plural': 'alphas', 'scope': 'Namespaced', 'description': 'A'},
            {'kind': 'Beta', 'group': 'g.io', 'version': 'v2',
             'plural': 'betas', 'scope': 'Cluster', 'description': 'B'},
        ]
        gen_api_docs.generate_index(crds, self.output_dir)
        path = os.path.join(self.output_dir, 'index.json')
        self.assertTrue(os.path.exists(path))

    def test_index_content(self):
        crds = [
            {'kind': 'Alpha', 'group': 'g.io', 'version': 'v1',
             'plural': 'alphas', 'scope': 'Namespaced', 'description': 'A'},
            {'kind': 'Beta', 'group': 'g.io', 'version': 'v2',
             'plural': 'betas', 'scope': 'Cluster', 'description': 'B'},
        ]
        gen_api_docs.generate_index(crds, self.output_dir)
        path = os.path.join(self.output_dir, 'index.json')
        with open(path) as f:
            data = json.load(f)
        self.assertEqual(len(data['crds']), 2)
        self.assertEqual(data['crds'][0]['kind'], 'Alpha')
        self.assertEqual(data['crds'][0]['apiVersion'], 'g.io/v1')
        self.assertEqual(data['crds'][1]['kind'], 'Beta')
        self.assertEqual(data['crds'][1]['scope'], 'Cluster')
        self.assertEqual(data['crds'][0]['schemaFile'], 'Alpha.json')


class TestPrompt(unittest.TestCase):
    """Test PROMPT.md generation."""

    def setUp(self):
        self.output_dir = tempfile.mkdtemp()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.output_dir)

    def test_prompt_created(self):
        gen_api_docs.generate_prompt(self.output_dir)
        path = os.path.join(self.output_dir, 'PROMPT.md')
        self.assertTrue(os.path.exists(path))

    def test_prompt_content(self):
        gen_api_docs.generate_prompt(self.output_dir)
        path = os.path.join(self.output_dir, 'PROMPT.md')
        with open(path) as f:
            content = f.read()
        self.assertIn('index.json', content)
        self.assertIn('apiVersion', content)
        self.assertIn('kubectl', content)


class TestMarkdownUnchanged(unittest.TestCase):
    """Regression: markdown output should be unchanged by new metadata."""

    def test_markdown_ignores_new_keys(self):
        crd_info = {
            'kind': 'Regression',
            'group': 'example.com',
            'version': 'v1',
            'plural': 'regressions',
            'singular': 'regression',
            'scope': 'Namespaced',
            'description': 'Regression test',
            'descriptionspec': 'Spec desc',
            'descriptionstatus': 'Status desc',
            'spec': [
                {'name': 'field1', 'type': 'string',
                 'description': 'A field', 'validations': [],
                 'required': True, 'enum': ['a', 'b']},
            ],
            'status': [],
        }
        output_dir = tempfile.mkdtemp()
        try:
            gen_api_docs.generate_markdown(crd_info, output_dir, [])
            path = os.path.join(output_dir, 'regression_api.md')
            with open(path) as f:
                content = f.read()
            self.assertIn('# Regression API', content)
            self.assertIn('field1', content)
            # New metadata keys should not appear in markdown
            self.assertNotIn('"group"', content)
            self.assertNotIn('"plural"', content)
        finally:
            import shutil
            shutil.rmtree(output_dir)


if __name__ == '__main__':
    unittest.main()
