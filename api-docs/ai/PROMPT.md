# AI Instructions for CRD Usage

This directory contains machine-readable schemas for Kubernetes Custom Resource
Definitions (CRDs) used in Advanced Cluster Management (ACM) and Multicluster
Engine (MCE).

## Quick Start

1. Read `index.json` to discover available CRDs.
2. Load the `{Kind}.json` file for the CRD you need.
3. Use the `exampleYAML` field as a starting template.
4. Refer to `spec.fields` for available fields, types, and constraints.

## Generating Valid YAML

- Always set `apiVersion` and `kind` exactly as shown in the schema.
- Use the `metadata.scope` field to determine whether to include `namespace`.
- For `Namespaced` resources, always include `metadata.namespace`.
- For `Cluster` scoped resources, omit `metadata.namespace`.
- Check `required: true` fields — these must be present.
- Respect `enum` values — only use listed values.
- Respect `validations` (minimum, maximum, pattern) constraints.

## Field Structure

Each field in the schema has:
- `type`: The data type (string, integer, boolean, object, array)
- `description`: What the field does
- `required`: Whether the field must be present (when true)
- `enum`: Allowed values (when present)
- `default`: Default value if not specified (when present)
- `validations`: Constraints like minimum, maximum, pattern (when present)
- `fields`: Nested fields for object types (when present)

## Kubernetes MCP Tools (Preferred)

If you have Kubernetes MCP tools installed (e.g., `mcp-server-kubernetes`),
prefer using them over generating shell commands. MCP tools provide direct
API access with structured input/output and better error handling.

- **Use MCP tools to apply resources** by passing the generated YAML directly.
- **Use MCP tools to list/get resources** using the `plural` name and `group`
  from the schema metadata.
- **Use MCP tools to watch or describe resources** for status monitoring.

MCP tools eliminate the need to shell out to `kubectl` and give you structured
responses you can parse programmatically. Fall back to `kubectl` only when MCP
tools are unavailable.

## Using with kubectl

When MCP tools are not available, use `kubectl` directly:

```bash
# Apply a resource
kubectl apply -f resource.yaml

# Get resources (use plural name from schema)
kubectl get <plural> -n <namespace>

# Describe a resource
kubectl describe <singular>/<name> -n <namespace>
```
