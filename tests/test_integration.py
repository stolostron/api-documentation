#!/usr/bin/env python3
"""
Integration tests for the complete gen-api-docs workflow
"""

import os
import tempfile
import unittest
import shutil
import importlib.util
from unittest.mock import patch

# Import the module by executing the file
spec = importlib.util.spec_from_file_location("gen_api_docs", os.path.join(os.path.dirname(__file__), '..', 'cmd', 'gen-api-docs.py'))
gen_api_docs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen_api_docs)


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete workflow"""

    def setUp(self):
        """Set up test fixtures"""
        self.test_dir = tempfile.mkdtemp()
        self.original_search_dir = gen_api_docs.search_dir
        gen_api_docs.search_dir = self.test_dir

    def tearDown(self):
        """Clean up test fixtures"""
        gen_api_docs.search_dir = self.original_search_dir
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def create_test_crd_file(self, filename, content):
        """Helper to create a test CRD file"""
        filepath = os.path.join(self.test_dir, filename)
        with open(filepath, 'w') as f:
            f.write(content)
        return filepath

    def create_test_types_file(self, filename, content):
        """Helper to create a test _types.go file"""
        filepath = os.path.join(self.test_dir, filename)
        with open(filepath, 'w') as f:
            f.write(content)
        return filepath

    def test_crd_priority_over_types(self):
        """Test that CRD files take priority over _types.go files"""
        # Create a _types.go file
        types_content = '''
package v1alpha1

// TestResourceSpec defines the desired state of TestResource
type TestResourceSpec struct {
    // Name from types.go
    Name string `json:"name"`

    // Type from types.go
    Type string `json:"type"`
}
'''
        self.create_test_types_file('testresource_types.go', types_content)

        # Create a CRD file with different fields
        crd_content = '''
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: testresources.example.com
spec:
  group: example.com
  names:
    kind: TestResource
    plural: testresources
    singular: testresource
  scope: Namespaced
  versions:
  - name: v1alpha1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            description: Specification for TestResource
            properties:
              name:
                type: string
                description: The name from CRD
              replicas:
                type: integer
                description: Number of replicas from CRD
                minimum: 1
                maximum: 10
          status:
            type: object
            description: Status of TestResource
            properties:
              phase:
                type: string
                description: Current phase
                enum: [Pending, Running, Completed, Failed]
'''
        self.create_test_crd_file('testresource-crd.yaml', crd_content)

        # Run the main function
        with patch('builtins.print'):  # Suppress print output
            gen_api_docs.main()

        # Check that the CRD was used (not the types.go)
        api_docs_dir = os.path.join(self.test_dir, 'api-docs')
        self.assertTrue(os.path.exists(api_docs_dir))

        # Check that the markdown file was generated
        md_file = os.path.join(api_docs_dir, 'testresource_api.md')
        self.assertTrue(os.path.exists(md_file))

        # Read the generated markdown and verify CRD content was used
        with open(md_file, 'r') as f:
            content = f.read()

        # Should contain CRD fields, not types.go fields
        self.assertIn('replicas', content)
        self.assertIn('Number of replicas from CRD', content)
        self.assertIn('phase', content)
        self.assertNotIn('Type from types.go', content)

    def test_types_go_when_no_crd(self):
        """Test that _types.go files are used when no CRD is present"""
        # Create only a _types.go file
        types_content = '''
package v1alpha1

// TestResourceSpec defines the desired state of TestResource
type TestResourceSpec struct {
    // Name is the name of the resource
    // +kubebuilder:validation:Pattern=^[a-z0-9]([-a-z0-9]*[a-z0-9])?$
    Name string `json:"name"`

    // Replicas is the number of replicas
    // +kubebuilder:validation:Minimum=1
    // +kubebuilder:validation:Maximum=10
    Replicas int32 `json:"replicas"`

    // Config contains configuration
    Config TestConfig `json:"config"`
}

// TestConfig defines configuration options
type TestConfig struct {
    // Timeout is the timeout in seconds
    Timeout int32 `json:"timeout"`

    // Retries is the number of retries
    Retries int32 `json:"retries"`
}
'''
        self.create_test_types_file('testresource_types.go', types_content)

        # Run the main function
        with patch('builtins.print'):  # Suppress print output
            gen_api_docs.main()

        # Check that the markdown file was generated
        api_docs_dir = os.path.join(self.test_dir, 'api-docs')
        md_file = os.path.join(api_docs_dir, 'testresource_api.md')
        self.assertTrue(os.path.exists(md_file))

        # Read the generated markdown and verify types.go content was used
        with open(md_file, 'r') as f:
            content = f.read()

        # Should contain types.go fields
        self.assertIn('Name is the name of the resource', content)
        self.assertIn('Replicas is the number of replicas', content)
        self.assertIn('Pattern=^[a-z0-9]([-a-z0-9]*[a-z0-9])?$', content)
        self.assertIn('Minimum=1', content)
        self.assertIn('Maximum=10', content)

    def test_helm_template_removal_integration(self):
        """Test Helm template removal in the complete workflow"""
        # Create a CRD file with Helm templates
        helm_crd_content = '''
{{- if .Values.manageCRDs }}
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: {{ .Values.crdName | default "testresources.example.com" }}
spec:
  group: {{ .Values.group | default "example.com" }}
  names:
    kind: {{ .Values.kind | default "TestResource" }}
    plural: {{ .Values.plural | default "testresources" }}
    singular: {{ .Values.singular | default "testresource" }}
  scope: {{ .Values.scope | default "Namespaced" }}
  versions:
  - name: {{ .Values.version | default "v1alpha1" }}
    served: {{ .Values.served | default true }}
    storage: {{ .Values.storage | default true }}
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            description: Specification for TestResource
            properties:
              name:
                type: string
                description: The name of the resource
                pattern: "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$"
              replicas:
                type: integer
                description: Number of replicas
                minimum: 1
                maximum: 10
{{- end }}
'''
        self.create_test_crd_file('testresource-crd.yaml', helm_crd_content)

        # Run the main function
        with patch('builtins.print'):  # Suppress print output
            gen_api_docs.main()

        # Check that the markdown file was generated
        api_docs_dir = os.path.join(self.test_dir, 'api-docs')
        md_file = os.path.join(api_docs_dir, 'testresource_api.md')
        self.assertTrue(os.path.exists(md_file))

        # Read the generated markdown and verify content
        with open(md_file, 'r') as f:
            content = f.read()

        # Should contain the processed content
        self.assertIn('TestResource API', content)
        self.assertIn('The name of the resource', content)
        self.assertIn('Number of replicas', content)
        self.assertIn('Pattern=^[a-z0-9]([-a-z0-9]*[a-z0-9])?$', content)
        self.assertIn('Minimum=1', content)
        self.assertIn('Maximum=10', content)

    def test_multiple_resources(self):
        """Test processing multiple resources"""
        # Create multiple CRD files
        crd1_content = '''
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: resource1.example.com
spec:
  group: example.com
  names:
    kind: Resource1
    plural: resource1s
    singular: resource1
  scope: Namespaced
  versions:
  - name: v1alpha1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              name:
                type: string
                description: The name of resource1
'''
        self.create_test_crd_file('resource1-crd.yaml', crd1_content)

        crd2_content = '''
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: resource2.example.com
spec:
  group: example.com
  names:
    kind: Resource2
    plural: resource2s
    singular: resource2
  scope: Namespaced
  versions:
  - name: v1alpha1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              name:
                type: string
                description: The name of resource2
'''
        self.create_test_crd_file('resource2-crd.yaml', crd2_content)

        # Create a _types.go file for a third resource
        types_content = '''
package v1alpha1

// Resource3Spec defines the desired state of Resource3
type Resource3Spec struct {
    // Name is the name of resource3
    Name string `json:"name"`
}
'''
        self.create_test_types_file('resource3_types.go', types_content)

        # Run the main function
        with patch('builtins.print'):  # Suppress print output
            gen_api_docs.main()

        # Check that all markdown files were generated
        api_docs_dir = os.path.join(self.test_dir, 'api-docs')
        self.assertTrue(os.path.exists(os.path.join(api_docs_dir, 'resource1_api.md')))
        self.assertTrue(os.path.exists(os.path.join(api_docs_dir, 'resource2_api.md')))
        self.assertTrue(os.path.exists(os.path.join(api_docs_dir, 'resource3_api.md')))

        # Check that README was generated
        readme_file = os.path.join(api_docs_dir, 'README.md')
        self.assertTrue(os.path.exists(readme_file))

        # Read the README and verify all resources are listed
        with open(readme_file, 'r') as f:
            content = f.read()

        self.assertIn('Resource1', content)
        self.assertIn('Resource2', content)
        self.assertIn('Resource3', content)

    def test_ignored_folders(self):
        """Test that ignored folders are properly skipped"""
        # Create ignored folders
        ignored_dirs = ['vendor', '.github', '.git', 'hack']
        for ignored_dir in ignored_dirs:
            os.makedirs(os.path.join(self.test_dir, ignored_dir), exist_ok=True)

            # Create a CRD file in each ignored directory
            crd_content = '''
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: ignored.example.com
spec:
  group: example.com
  names:
    kind: Ignored
    plural: ignoreds
    singular: ignored
  scope: Namespaced
  versions:
  - name: v1alpha1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              name:
                type: string
                description: This should be ignored
'''
            self.create_test_crd_file(os.path.join(ignored_dir, 'ignored-crd.yaml'), crd_content)

        # Create a valid CRD file in the main directory
        valid_crd_content = '''
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: valid.example.com
spec:
  group: example.com
  names:
    kind: Valid
    plural: valids
    singular: valid
  scope: Namespaced
  versions:
  - name: v1alpha1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              name:
                type: string
                description: This should be processed
'''
        self.create_test_crd_file('valid-crd.yaml', valid_crd_content)

        # Run the main function
        with patch('builtins.print'):  # Suppress print output
            gen_api_docs.main()

        # Check that only the valid CRD was processed
        api_docs_dir = os.path.join(self.test_dir, 'api-docs')
        self.assertTrue(os.path.exists(os.path.join(api_docs_dir, 'valid_api.md')))
        self.assertFalse(os.path.exists(os.path.join(api_docs_dir, 'ignored_api.md')))

    def test_markdown_generation_format(self):
        """Test that generated markdown has the correct format"""
        # Create a CRD file
        crd_content = '''
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: test.example.com
spec:
  group: example.com
  names:
    kind: Test
    plural: tests
    singular: test
  scope: Namespaced
  versions:
  - name: v1alpha1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            description: Specification for Test
            properties:
              name:
                type: string
                description: The name of the resource
                pattern: "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$"
              replicas:
                type: integer
                description: Number of replicas
                minimum: 1
                maximum: 10
          status:
            type: object
            description: Status of Test
            properties:
              phase:
                type: string
                description: Current phase
                enum: [Pending, Running, Completed, Failed]
'''
        self.create_test_crd_file('test-crd.yaml', crd_content)

        # Run the main function
        with patch('builtins.print'):  # Suppress print output
            gen_api_docs.main()

        # Check the generated markdown
        api_docs_dir = os.path.join(self.test_dir, 'api-docs')
        md_file = os.path.join(api_docs_dir, 'test_api.md')

        with open(md_file, 'r') as f:
            content = f.read()

        # Check markdown structure
        self.assertIn('# Test API', content)
        self.assertIn('## Spec Fields', content)
        self.assertIn('## Status Fields', content)
        self.assertIn('| Field | Type | Description | Validations |', content)
        self.assertIn('|:---|---|---|---|', content)

        # Check that fields are properly formatted
        self.assertIn('**name**', content)
        self.assertIn('`string`', content)
        self.assertIn('The name of the resource', content)
        self.assertIn('`Pattern=^[a-z0-9]([-a-z0-9]*[a-z0-9])?$`', content)

        self.assertIn('**replicas**', content)
        self.assertIn('`integer`', content)
        self.assertIn('Number of replicas', content)
        self.assertIn('`Minimum=1`', content)
        self.assertIn('`Maximum=10`', content)


if __name__ == '__main__':
    unittest.main()
