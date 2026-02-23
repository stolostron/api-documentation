# gen-api-docs Tests

This directory contains comprehensive tests for the `gen-api-docs.py` script.

## Test Files

### `test_crd_import.py`
Tests for CRD (Custom Resource Definition) import functionality:
- Valid CRD parsing
- Invalid YAML handling
- Missing CRD fields
- Array properties
- Validation rules extraction
- Schema parsing

### `test_helm_template_removal.py`
Tests for Helm template code removal:
- Conditional template removal (`{{- if }}`)
- Mixed content handling
- Empty line cleanup

### `test_types_go_import.py`
Tests for Go struct (`_types.go`) parsing:
- Struct field extraction
- JSON tag parsing
- Kubebuilder validation tags
- Embedded struct handling

### `test_ai_output.py`
Tests for AI-consumable output generation:
- CRD metadata capture (group, version, plural, singular, scope)
- Required, enum, and default field extraction
- JSON schema structure and parseability
- Example YAML generation and parseability
- Index generation with multiple CRDs
- PROMPT.md content validation
- Regression: existing markdown output unchanged

### `test_integration.py`
Integration tests for the complete workflow:
- CRD priority over `_types.go`
- Multiple resource processing
- Ignored folder handling
- Markdown generation format
- Complete end-to-end workflows

## Test Data

### `test_data/sample_crd.yaml`
A sample CRD file with various field types and validations for testing.

### `test_data/sample_types.go`
A sample `_types.go` file with various struct definitions, validations, and embedded types.

### `test_data/sample_helm_crd.yaml`
A sample CRD file with Helm templates for testing template removal functionality.

## Running Tests

### Run all tests:
```bash
make test
```

### Run individual tests:
```bash
make test-crd-import
make test-helm-template-removal
make test-ai-output
make test-integration
```

### Run with verbose output:
```bash
make test-verbose
```

## Test Coverage

The tests cover:

1. **CRD Import Validation**:
   - Valid CRD parsing with all field types
   - Invalid YAML handling
   - Missing or malformed CRD structures
   - Array and object property handling
   - Validation rule extraction (minimum, maximum, pattern, enum)

2. **Go Types Import Validation**:
   - Struct field extraction and JSON tag parsing
   - Kubebuilder validation tag extraction
   - Embedded struct inlining

3. **Helm Template Removal Validation**:
   - All Helm template syntax patterns
   - Conditional blocks (`{{- if }}`, `{{- else }}`, `{{- end }}`)
   - Mixed template and YAML content
   - Empty line cleanup after template removal

4. **AI Output Validation**:
   - CRD metadata (group, version, plural, scope) captured correctly
   - Required, enum, and default field attributes extracted
   - Per-CRD JSON schema is valid and complete
   - Example YAML is parseable and uses correct apiVersion/kind
   - Index lists all CRDs with schema file references
   - Existing markdown output unchanged by new metadata

5. **Integration Testing**:
   - Complete workflow validation
   - CRD vs `_types.go` priority handling
   - Multiple resource processing
   - Ignored folder functionality
   - Markdown generation format validation

## Expected Test Results

All tests should pass and validate that:
- CRD files are properly parsed and their schemas extracted
- Go type files are properly parsed with validations and embedded structs
- Helm templates are completely removed while preserving valid YAML
- AI-consumable JSON schemas, example YAML, and index are correctly generated
- The integration workflow works correctly end-to-end
- Generated markdown has the correct format and content

## Troubleshooting

If tests fail:
1. Check that the `cmd/gen-api-docs.py` file is accessible
2. Ensure all required Python packages are installed (`yaml`, `unittest`)
3. Verify that test data files are present in `test_data/`
4. Check that the test directory structure matches the expected layout 