# AzureManagedCluster API

AzureManagedCluster is the Schema for the azuremanagedclusters API.

## Spec Fields

AzureManagedClusterSpec defines the desired state of AzureManagedCluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **controlPlaneEndpoint** | `object` | ControlPlaneEndpoint represents the endpoint used to communicate with the control plane. Immutable, populated by the AKS API at create. Because this field is programmatically set by CAPZ after resource creation, we define it as +optional in the API schema to permit resource admission. | N/A |
| └>&nbsp;&nbsp; **host** | `string` | host is the hostname on which the API server is serving. | N/A |
| └>&nbsp;&nbsp; **port** | `integer` | port is the port on which the API server is serving. | N/A |
## Status Fields

AzureManagedClusterStatus defines the observed state of AzureManagedCluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **ready** | `boolean` | Ready is true when the provider resource is ready. | N/A |
