# AzureASOManagedCluster API

AzureASOManagedCluster is the Schema for the azureasomanagedclusters API.

## Spec Fields

AzureASOManagedClusterSpec defines the desired state of AzureASOManagedCluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **controlPlaneEndpoint** | `object` | ControlPlaneEndpoint is the location of the API server within the control plane. CAPZ manages this field and it should not be set by the user. It fulfills Cluster API's cluster infrastructure provider contract. Because this field is programmatically set by CAPZ after resource creation, we define it as +optional in the API schema to permit resource admission. | N/A |
| └>&nbsp;&nbsp; **host** | `string` | host is the hostname on which the API server is serving. | N/A |
| └>&nbsp;&nbsp; **port** | `integer` | port is the port on which the API server is serving. | N/A |
|  **resources** | `array` | Resources are embedded ASO resources to be managed by this resource. | N/A |
## Status Fields

AzureASOManagedClusterStatus defines the observed state of AzureASOManagedCluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **ready** | `boolean` | Ready represents whether or not the cluster has been provisioned and is ready. It fulfills Cluster API's cluster infrastructure provider contract. | N/A |
|  **resources** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **ready** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **resource** | `object` | StatusResource is a handle to a resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | No description provided. | N/A |
