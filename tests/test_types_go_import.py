#!/usr/bin/env python3
"""
Tests for _types.go import functionality in gen-api-docs.py
"""

import os
import tempfile
import unittest
import importlib.util
from unittest.mock import patch

# Import the module by executing the file
spec = importlib.util.spec_from_file_location("gen_api_docs", os.path.join(os.path.dirname(__file__), '..', 'cmd', 'gen-api-docs.py'))
gen_api_docs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen_api_docs)


class TestTypesGoImport(unittest.TestCase):
    """Test cases for _types.go import functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.sample_types_go = '''
// TestResourceSpec defines the desired state of TestResource
type TestResourceSpec struct {
    // Name is the name of the resource
    // +kubebuilder:validation:Pattern=^[a-z0-9]([-a-z0-9]*[a-z0-9])?$
    Name string `json:"name"`

    // Replicas is the number of replicas to run
    // +kubebuilder:validation:Minimum=1
    // +kubebuilder:validation:Maximum=10
    Replicas int32 `json:"replicas"`

    // Config contains configuration options
    Config TestConfig `json:"config"`

    // Enabled determines if the resource is enabled
    Enabled bool `json:"enabled"`

    // EmbeddedStruct is an embedded struct
    EmbeddedStruct `json:"embedded"`
}

// TestConfig defines configuration options
type TestConfig struct {
    // Timeout is the timeout in seconds
    // +kubebuilder:validation:Minimum=1
    Timeout int32 `json:"timeout"`

    // Retries is the number of retries
    Retries int32 `json:"retries"`
}

// EmbeddedStruct is an embedded struct
type EmbeddedStruct struct {
    // EmbeddedField is a field in the embedded struct
    EmbeddedField string `json:"embeddedField"`
}

// TestResourceStatus defines the observed state of TestResource
type TestResourceStatus struct {
    // Phase represents the current phase
    // +kubebuilder:validation:Enum=Pending;Running;Completed;Failed
    Phase string `json:"phase"`

    // ReadyReplicas is the number of ready replicas
    ReadyReplicas int32 `json:"readyReplicas"`

    // Conditions represents the latest available observations
    Conditions []TestCondition `json:"conditions"`
}

// TestCondition represents a condition
type TestCondition struct {
    // Type is the type of condition
    Type string `json:"type"`

    // Status is the status of the condition
    Status string `json:"status"`

    // Message is the message describing the condition
    Message string `json:"message"`
}
'''

    def test_parse_go_file_valid(self):
        """Test parsing a valid _types.go file"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='_types.go', delete=False) as f:
            f.write(self.sample_types_go)
            temp_file = f.name

        try:
            # Mock the collect_go_type_files function to return our test file
            with patch.object(gen_api_docs, 'collect_go_type_files', return_value=[temp_file]):
                result = gen_api_docs.parse_go_file(temp_file, [temp_file])

                self.assertIsNotNone(result)
                self.assertEqual(result['kind'], 'TestResource')
                self.assertEqual(result['description'], 'TestResourceSpec defines the desired state of TestResource')

                # Check fields
                fields = result.get('fields', [])
                self.assertEqual(len(fields), 5)

                # Check name field
                name_field = next((f for f in fields if f['name'] == 'name'), None)
                self.assertIsNotNone(name_field)
                self.assertEqual(name_field['type'], 'string')
                self.assertEqual(name_field['description'], 'Name is the name of the resource')
                self.assertIn('Pattern=^[a-z0-9]([-a-z0-9]*[a-z0-9])?$', name_field['validations'])

                # Check replicas field
                replicas_field = next((f for f in fields if f['name'] == 'replicas'), None)
                self.assertIsNotNone(replicas_field)
                self.assertEqual(replicas_field['type'], 'int32')
                self.assertIn('Minimum=1', replicas_field['validations'])
                self.assertIn('Maximum=10', replicas_field['validations'])

                # Check config field (nested struct)
                config_field = next((f for f in fields if f['name'] == 'config'), None)
                self.assertIsNotNone(config_field)
                self.assertEqual(config_field['type'], 'TestConfig')
                self.assertIn('inline', config_field)

                # Check embedded struct fields are inlined
                embedded_field = next((f for f in fields if f['name'] == 'embeddedField'), None)
                self.assertIsNotNone(embedded_field)
                self.assertEqual(embedded_field['type'], 'string')

        finally:
            os.unlink(temp_file)

    def test_parse_go_file_no_struct(self):
        """Test parsing a Go file without struct definitions"""
        no_struct_content = '''
package v1alpha1

import (
    "metav1"
)

// Some other type definitions
type SomeType string

const (
    TypeA SomeType = "A"
    TypeB SomeType = "B"
)
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='_types.go', delete=False) as f:
            f.write(no_struct_content)
            temp_file = f.name

        try:
            with patch.object(gen_api_docs, 'collect_go_type_files', return_value=[temp_file]):
                result = gen_api_docs.parse_go_file(temp_file, [temp_file])
                self.assertIsNone(result)
        finally:
            os.unlink(temp_file)

    def test_parse_go_struct_with_comments(self):
        """Test parsing Go struct with various comment styles"""
        struct_with_comments = '''
// TestResourceSpec defines the desired state of TestResource
// This is a multi-line comment
type TestResourceSpec struct {
    // Name is the name of the resource
    // This is also a multi-line comment
    // +kubebuilder:validation:Pattern=^[a-z0-9]([-a-z0-9]*[a-z0-9])?$
    Name string `json:"name"`

    // Description with special characters: < > & " '
    Description string `json:"description"`

    // Field with no comment
    NoComment string `json:"noComment"`
}
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='_types.go', delete=False) as f:
            f.write(struct_with_comments)
            temp_file = f.name

        try:
            with patch.object(gen_api_docs, 'collect_go_type_files', return_value=[temp_file]):
                result = gen_api_docs.parse_go_file(temp_file, [temp_file])

                self.assertIsNotNone(result)
                fields = result.get('fields', [])

                # Check name field with validation
                name_field = next((f for f in fields if f['name'] == 'name'), None)
                self.assertIsNotNone(name_field)
                self.assertEqual(name_field['description'], 'Name is the name of the resource')
                self.assertIn('Pattern=^[a-z0-9]([-a-z0-9]*[a-z0-9])?$', name_field['validations'])

                # Check description field with special characters
                desc_field = next((f for f in fields if f['name'] == 'description'), None)
                self.assertIsNotNone(desc_field)
                self.assertEqual(desc_field['description'], 'Description with special characters: < > & " \'')

                # Check field with no comment
                no_comment_field = next((f for f in fields if f['name'] == 'noComment'), None)
                self.assertIsNotNone(no_comment_field)
                self.assertEqual(no_comment_field['description'], 'No description provided.')

        finally:
            os.unlink(temp_file)

    def test_parse_go_struct_with_json_tags(self):
        """Test parsing Go struct with various JSON tag formats"""
        struct_with_json_tags = '''
type TestResourceSpec struct {
    // Field with simple JSON tag
    Name string `json:"name"`

    // Field with JSON tag and omitempty
    Optional string `json:"optional,omitempty"`

    // Field with JSON tag and other options
    Complex string `json:"complex,omitempty,string"`

    // Field with no JSON tag
    NoTag string

    // Field with empty JSON tag
    EmptyTag string `json:""`
}
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='_types.go', delete=False) as f:
            f.write(struct_with_json_tags)
            temp_file = f.name

        try:
            with patch.object(gen_api_docs, 'collect_go_type_files', return_value=[temp_file]):
                result = gen_api_docs.parse_go_file(temp_file, [temp_file])

                self.assertIsNotNone(result)
                fields = result.get('fields', [])

                # Check field with simple JSON tag
                name_field = next((f for f in fields if f['name'] == 'name'), None)
                self.assertIsNotNone(name_field)

                # Check field with omitempty
                optional_field = next((f for f in fields if f['name'] == 'optional'), None)
                self.assertIsNotNone(optional_field)

                # Check field with complex JSON tag
                complex_field = next((f for f in fields if f['name'] == 'complex'), None)
                self.assertIsNotNone(complex_field)

                # Check field with no JSON tag (should use field name)
                no_tag_field = next((f for f in fields if f['name'] == 'NoTag'), None)
                self.assertIsNotNone(no_tag_field)

                # Check field with empty JSON tag (should use field name)
                empty_tag_field = next((f for f in fields if f['name'] == 'EmptyTag'), None)
                self.assertIsNotNone(empty_tag_field)

        finally:
            os.unlink(temp_file)

    def test_parse_go_struct_with_embedded_types(self):
        """Test parsing Go struct with embedded types"""
        struct_with_embedded = '''
type TestResourceSpec struct {
    // Embedded metav1.TypeMeta
    metav1.TypeMeta `json:",inline"`

    // Embedded metav1.ObjectMeta
    metav1.ObjectMeta `json:"metadata,omitempty"`

    // Custom embedded struct
    EmbeddedStruct `json:",inline"`

    // Regular field
    Name string `json:"name"`
}

type EmbeddedStruct struct {
    // Field in embedded struct
    EmbeddedField string `json:"embeddedField"`
}
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='_types.go', delete=False) as f:
            f.write(struct_with_embedded)
            temp_file = f.name

        try:
            with patch.object(gen_api_docs, 'collect_go_type_files', return_value=[temp_file]):
                result = gen_api_docs.parse_go_file(temp_file, [temp_file])

                self.assertIsNotNone(result)
                fields = result.get('fields', [])

                # Should have the embedded field inlined
                embedded_field = next((f for f in fields if f['name'] == 'embeddedField'), None)
                self.assertIsNotNone(embedded_field)

                # Should have the regular field
                name_field = next((f for f in fields if f['name'] == 'name'), None)
                self.assertIsNotNone(name_field)

        finally:
            os.unlink(temp_file)

    def test_parse_go_struct_recursive_reference(self):
        """Test parsing Go struct with recursive references"""
        recursive_struct = '''
type TestResourceSpec struct {
    // Self-referencing field
    Parent *TestResourceSpec `json:"parent"`

    // Field with nested struct that references parent
    Config TestConfig `json:"config"`
}

type TestConfig struct {
    // Reference back to parent
    Resource *TestResourceSpec `json:"resource"`
}
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='_types.go', delete=False) as f:
            f.write(recursive_struct)
            temp_file = f.name

        try:
            with patch.object(gen_api_docs, 'collect_go_type_files', return_value=[temp_file]):
                result = gen_api_docs.parse_go_file(temp_file, [temp_file])

                self.assertIsNotNone(result)
                fields = result.get('fields', [])

                # Check that recursive reference is handled
                parent_field = next((f for f in fields if f['name'] == 'parent'), None)
                self.assertIsNotNone(parent_field)
                self.assertEqual(parent_field['type'], '*TestResourceSpec')

        finally:
            os.unlink(temp_file)

    def test_is_primitive(self):
        """Test the is_primitive function"""
        # Test basic primitives
        self.assertTrue(gen_api_docs.is_primitive('string'))
        self.assertTrue(gen_api_docs.is_primitive('int'))
        self.assertTrue(gen_api_docs.is_primitive('bool'))
        self.assertTrue(gen_api_docs.is_primitive('float64'))

        # Test slices of primitives
        self.assertTrue(gen_api_docs.is_primitive('[]string'))
        self.assertTrue(gen_api_docs.is_primitive('[]int'))

        # Test maps
        self.assertTrue(gen_api_docs.is_primitive('map[string]string'))
        self.assertTrue(gen_api_docs.is_primitive('map[string]int'))

        # Test k8s types
        self.assertTrue(gen_api_docs.is_primitive('metav1.Time'))
        self.assertTrue(gen_api_docs.is_primitive('corev1.PodSpec'))

        # Test non-primitives
        self.assertFalse(gen_api_docs.is_primitive('TestResourceSpec'))
        self.assertFalse(gen_api_docs.is_primitive('CustomType'))
        self.assertFalse(gen_api_docs.is_primitive('[]CustomType'))


if __name__ == '__main__':
    unittest.main()
