#!/usr/bin/env python3
"""
Tests for CRD import functionality in gen-api-docs.py
"""

import os
import tempfile
import unittest
import yaml
import importlib.util

# Import the module by executing the file
spec = importlib.util.spec_from_file_location("gen_api_docs", os.path.join(os.path.dirname(__file__), '..', 'cmd', 'gen-api-docs.py'))
gen_api_docs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen_api_docs)


class TestCRDImport(unittest.TestCase):
    """Test cases for CRD import functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.test_crd_data = {
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
                                    'description': 'Specification for TestResource',
                                    'properties': {
                                        'name': {
                                            'type': 'string',
                                            'description': 'The name of the resource',
                                            'pattern': '^[a-z0-9]([-a-z0-9]*[a-z0-9])?$'
                                        },
                                        'replicas': {
                                            'type': 'integer',
                                            'description': 'Number of replicas',
                                            'minimum': 1,
                                            'maximum': 10
                                        },
                                        'config': {
                                            'type': 'object',
                                            'description': 'Configuration object',
                                            'properties': {
                                                'enabled': {
                                                    'type': 'boolean',
                                                    'description': 'Whether the feature is enabled'
                                                },
                                                'timeout': {
                                                    'type': 'integer',
                                                    'description': 'Timeout in seconds',
                                                    'minimum': 1
                                                }
                                            }
                                        }
                                    }
                                },
                                'status': {
                                    'type': 'object',
                                    'description': 'Status of TestResource',
                                    'properties': {
                                        'phase': {
                                            'type': 'string',
                                            'description': 'Current phase of the resource',
                                            'enum': ['Pending', 'Running', 'Completed', 'Failed']
                                        },
                                        'readyReplicas': {
                                            'type': 'integer',
                                            'description': 'Number of ready replicas'
                                        }
                                    }
                                }
                            }
                        }
                    }
                }]
            }
        }

    def test_parse_crd_file_valid(self):
        """Test parsing a valid CRD file"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(self.test_crd_data, f)
            temp_file = f.name

        try:
            result = gen_api_docs.parse_crd_file(temp_file)

            self.assertIsNotNone(result)
            self.assertEqual(result['kind'], 'TestResource')
            self.assertEqual(result['description'], 'Description not found in CRD.')

            # Check spec fields
            spec_fields = result.get('spec', [])
            self.assertEqual(len(spec_fields), 3)

            # Check name field
            name_field = next((f for f in spec_fields if f['name'] == 'name'), None)
            self.assertIsNotNone(name_field)
            self.assertEqual(name_field['type'], 'string')
            self.assertEqual(name_field['description'], 'The name of the resource')
            self.assertIn('Pattern=^[a-z0-9]([-a-z0-9]*[a-z0-9])?$', name_field['validations'])

            # Check replicas field
            replicas_field = next((f for f in spec_fields if f['name'] == 'replicas'), None)
            self.assertIsNotNone(replicas_field)
            self.assertEqual(replicas_field['type'], 'integer')
            self.assertIn('Minimum=1', replicas_field['validations'])
            self.assertIn('Maximum=10', replicas_field['validations'])

            # Check config field (nested object)
            config_field = next((f for f in spec_fields if f['name'] == 'config'), None)
            self.assertIsNotNone(config_field)
            self.assertEqual(config_field['type'], 'object')
            self.assertIn('inline', config_field)

            # Check status fields
            status_fields = result.get('status', [])
            self.assertEqual(len(status_fields), 2)

            phase_field = next((f for f in status_fields if f['name'] == 'phase'), None)
            self.assertIsNotNone(phase_field)
            self.assertEqual(phase_field['type'], 'string')

        finally:
            os.unlink(temp_file)

    def test_parse_crd_file_invalid_yaml(self):
        """Test parsing an invalid YAML file"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write("invalid: yaml: content: [")
            temp_file = f.name

        try:
            result = gen_api_docs.parse_crd_file(temp_file)
            self.assertIsNone(result)
        finally:
            os.unlink(temp_file)

    def test_parse_crd_file_not_crd(self):
        """Test parsing a YAML file that is not a CRD"""
        non_crd_data = {
            'apiVersion': 'v1',
            'kind': 'Pod',
            'metadata': {'name': 'test-pod'},
            'spec': {'containers': []}
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(non_crd_data, f)
            temp_file = f.name

        try:
            result = gen_api_docs.parse_crd_file(temp_file)
            self.assertIsNone(result)
        finally:
            os.unlink(temp_file)

    def test_parse_crd_file_empty_schema(self):
        """Test parsing a CRD file with empty schema"""
        empty_schema_crd = {
            'apiVersion': 'apiextensions.k8s.io/v1',
            'kind': 'CustomResourceDefinition',
            'metadata': {'name': 'test.example.com'},
            'spec': {
                'group': 'example.com',
                'names': {'kind': 'Test'},
                'scope': 'Namespaced',
                'versions': [{
                    'name': 'v1alpha1',
                    'served': True,
                    'storage': True,
                    'schema': {
                        'openAPIV3Schema': {
                            'type': 'object',
                            'properties': {}
                        }
                    }
                }]
            }
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(empty_schema_crd, f)
            temp_file = f.name

        try:
            result = gen_api_docs.parse_crd_file(temp_file)
            self.assertIsNotNone(result)
            self.assertEqual(result['kind'], 'Test')
            self.assertEqual(len(result.get('spec', [])), 0)
            self.assertEqual(len(result.get('status', [])), 0)
        finally:
            os.unlink(temp_file)

    def test_parse_crd_file_with_array_properties(self):
        """Test parsing a CRD file with array properties"""
        array_crd_data = {
            'apiVersion': 'apiextensions.k8s.io/v1',
            'kind': 'CustomResourceDefinition',
            'metadata': {'name': 'test.example.com'},
            'spec': {
                'group': 'example.com',
                'names': {'kind': 'TestArray'},
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
                                        'items': {
                                            'type': 'array',
                                            'description': 'List of items',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'name': {
                                                        'type': 'string',
                                                        'description': 'Item name'
                                                    },
                                                    'value': {
                                                        'type': 'integer',
                                                        'description': 'Item value'
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }]
            }
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(array_crd_data, f)
            temp_file = f.name

        try:
            result = gen_api_docs.parse_crd_file(temp_file)
            self.assertIsNotNone(result)
            self.assertEqual(result['kind'], 'TestArray')

            spec_fields = result.get('spec', [])
            self.assertEqual(len(spec_fields), 1)

            items_field = spec_fields[0]
            self.assertEqual(items_field['name'], 'items')
            self.assertEqual(items_field['type'], 'array')
            self.assertIn('inline', items_field)
        finally:
            os.unlink(temp_file)


if __name__ == '__main__':
    unittest.main()
