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

3. **Helm Template Removal Validation**:
   - All Helm template syntax patterns
   - Conditional blocks (`{{- if }}`, `{{- else }}`, `{{- end }}`)
   - Mixed template and YAML content
   - Empty line cleanup after template removal

4. **Integration Testing**:
   - Complete workflow validation
   - CRD vs `_types.go` priority handling
   - Multiple resource processing
   - Ignored folder functionality
   - Markdown generation format validation

## Expected Test Results

All tests should pass and validate that:
- CRD files are properly parsed and their schemas extracted
- Helm templates are completely removed while preserving valid YAML
- The integration workflow works correctly end-to-end
- Generated markdown has the correct format and content

## Troubleshooting

If tests fail:
1. Check that the `cmd/gen-api-docs.py` file is accessible
2. Ensure all required Python packages are installed (`yaml`, `unittest`)
3. Verify that test data files are present in `test_data/`
4. Check that the test directory structure matches the expected layout 