# AWSManagedClusterTemplate API

AWSManagedClusterTemplate is the Schema for the AWSManagedClusterTemplates API.

## Spec Fields

AWSManagedClusterTemplateSpec defines the desired state of AWSManagedClusterTemplate.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **template** | `object` | AWSManagedClusterTemplateResource describes the data needed to create an AWSManagedCluster from a template. | N/A |
| └>&nbsp;&nbsp; **spec** | `object` | AWSManagedClusterSpec defines the desired state of AWSManagedCluster | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **controlPlaneEndpoint** | `object` | ControlPlaneEndpoint represents the endpoint used to communicate with the control plane. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **host** | `string` | host is the hostname on which the API server is serving. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **port** | `integer` | port is the port on which the API server is serving. | N/A |
## Status Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
