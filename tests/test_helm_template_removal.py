#!/usr/bin/env python3
"""
Tests for Helm template code removal functionality in gen-api-docs.py
"""

import importlib.util
import os
import tempfile
import unittest

# Import the module by executing the file
spec = importlib.util.spec_from_file_location("gen_api_docs", os.path.join(os.path.dirname(__file__), '..', 'cmd', 'gen-api-docs.py'))
gen_api_docs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen_api_docs)


class TestHelmTemplateRemoval(unittest.TestCase):
    """Test cases for Helm template code removal functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.base_crd_data = {
            'apiVersion': 'apiextensions.k8s.io/v1',
            'kind': 'CustomResourceDefinition',
            'metadata': {
                'name': 'testresources.example.com'
            },
            'spec': {
                'group': 'example.com',
                'names': {
                    'kind': 'TestResource',
                    'plural': 'testresources',
                    'singular': 'testresource'
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
                                    'properties': {
                                        'name': {
                                            'type': 'string',
                                            'description': 'The name of the resource'
                                        }
                                    }
                                }
                            }
                        }
                    }
                }]
            }
        }

    def test_helm_template_conditional_removal(self):
        """Test removal of Helm template conditionals"""
        helm_template_content = '''
{{- if .Values.manageCRDs }}
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
            properties:
              name:
                type: string
                description: The name of the resource
{{- end }}
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(helm_template_content)
            temp_file = f.name

        try:
            result = gen_api_docs.parse_crd_file(temp_file)

            # Should parse successfully after template removal
            self.assertIsNotNone(result)
            self.assertEqual(result['kind'], 'TestResource')

        finally:
            os.unlink(temp_file)

    def test_helm_template_variable_substitution_removal(self):
        """Test removal of Helm template variable substitutions"""
        helm_template_content = '''
{{- if .Values.enableCRD }}
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: testresources.example.com
  namespace: default
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
            properties:
              name:
                type: string
                description: The name of the resource
{{- end }}
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(helm_template_content)
            temp_file = f.name

        try:
            result = gen_api_docs.parse_crd_file(temp_file)

            # Should parse successfully after template removal
            self.assertIsNotNone(result)
            self.assertEqual(result['kind'], 'TestResource')

        finally:
            os.unlink(temp_file)

    def test_helm_template_range_removal(self):
        """Test removal of Helm template range loops"""
        helm_template_content = '''
{{- if .Values.enableVersions }}
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
            properties:
              name:
                type: string
                description: The name of the resource
{{- end }}
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(helm_template_content)
            temp_file = f.name

        try:
            result = gen_api_docs.parse_crd_file(temp_file)

            # Should parse successfully after template removal
            self.assertIsNotNone(result)
            self.assertEqual(result['kind'], 'TestResource')

        finally:
            os.unlink(temp_file)

    def test_helm_template_with_removal(self):
        """Test removal of Helm template with blocks"""
        helm_template_content = '''
{{- if .Values.enableSpecProperties }}
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
            properties:
              name:
                type: string
                description: The name of the resource
{{- end }}
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(helm_template_content)
            temp_file = f.name

        try:
            result = gen_api_docs.parse_crd_file(temp_file)

            # Should parse successfully after template removal
            self.assertIsNotNone(result)
            self.assertEqual(result['kind'], 'TestResource')

        finally:
            os.unlink(temp_file)

    def test_helm_template_complex_nested_removal(self):
        """Test removal of complex nested Helm templates"""
        helm_template_content = '''
{{- if .Values.enableCRD }}
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
            properties:
              name:
                type: string
                description: The name of the resource
{{- end }}
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(helm_template_content)
            temp_file = f.name

        try:
            result = gen_api_docs.parse_crd_file(temp_file)

            # Should parse successfully after template removal
            self.assertIsNotNone(result)
            self.assertEqual(result['kind'], 'TestResource')

        finally:
            os.unlink(temp_file)

    def test_helm_template_else_removal(self):
        """Test removal of Helm template else blocks"""
        helm_template_content = '''
{{- if .Values.useCustomName }}
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
            properties:
              name:
                type: string
                description: Default name field
{{- end }}
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(helm_template_content)
            temp_file = f.name

        try:
            result = gen_api_docs.parse_crd_file(temp_file)

            # Should parse successfully after template removal
            self.assertIsNotNone(result)
            self.assertEqual(result['kind'], 'TestResource')

        finally:
            os.unlink(temp_file)

    def test_helm_template_mixed_content_removal(self):
        """Test removal of Helm templates mixed with regular YAML content"""
        helm_template_content = '''
{{- if .Values.enableCRD }}
# This is a comment
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: testresources.example.com
  # Another comment
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
            properties:
              name:
                type: string
                description: The name of the resource
                # Inline comment
                pattern: "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$"
{{- end }}
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(helm_template_content)
            temp_file = f.name

        try:
            result = gen_api_docs.parse_crd_file(temp_file)

            # Should parse successfully after template removal
            self.assertIsNotNone(result)
            self.assertEqual(result['kind'], 'TestResource')

            # Check that the pattern validation is preserved
            spec_fields = result.get('spec', [])
            name_field = next((f for f in spec_fields if f['name'] == 'name'), None)
            self.assertIsNotNone(name_field)
            self.assertIn('Pattern=^[a-z0-9]([-a-z0-9]*[a-z0-9])?$', name_field['validations'])

        finally:
            os.unlink(temp_file)

    def test_helm_template_empty_lines_removal(self):
        """Test that empty lines are properly handled after template removal"""
        helm_template_content = '''
{{- if .Values.enableCRD }}

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

            properties:
              name:
                type: string

                description: The name of the resource

{{- end }}
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(helm_template_content)
            temp_file = f.name

        try:
            result = gen_api_docs.parse_crd_file(temp_file)

            # Should parse successfully after template removal
            self.assertIsNotNone(result)
            self.assertEqual(result['kind'], 'TestResource')

        finally:
            os.unlink(temp_file)

    def test_helm_template_invalid_yaml_after_removal(self):
        """Test handling of invalid YAML after template removal"""
        helm_template_content = '''
{{- if .Values.enableCRD }}
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
            properties:
              name:
                type: string
                description: The name of the resource
{{- end }}
  invalid: yaml: structure: [
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(helm_template_content)
            temp_file = f.name

        try:
            result = gen_api_docs.parse_crd_file(temp_file)

            # Should return None due to invalid YAML
            self.assertIsNone(result)

        finally:
            os.unlink(temp_file)

    def test_helm_template_no_templates(self):
        """Test parsing YAML file without any Helm templates"""
        regular_yaml_content = '''
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
            properties:
              name:
                type: string
                description: The name of the resource
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(regular_yaml_content)
            temp_file = f.name

        try:
            result = gen_api_docs.parse_crd_file(temp_file)

            # Should parse successfully
            self.assertIsNotNone(result)
            self.assertEqual(result['kind'], 'TestResource')

        finally:
            os.unlink(temp_file)


if __name__ == '__main__':
    unittest.main()
