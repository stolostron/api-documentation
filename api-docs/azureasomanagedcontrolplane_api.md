# AzureASOManagedControlPlane API

AzureASOManagedControlPlane is the Schema for the azureasomanagedcontrolplanes API.

## Spec Fields

AzureASOManagedControlPlaneSpec defines the desired state of AzureASOManagedControlPlane.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **resources** | `array` | Resources are embedded ASO resources to be managed by this resource. | N/A |
|  **version** | `string` | Version is the Kubernetes version of the control plane. It fulfills Cluster API's control plane provider contract. | N/A |
## Status Fields

AzureASOManagedControlPlaneStatus defines the observed state of AzureASOManagedControlPlane.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **controlPlaneEndpoint** | `object` | ControlPlaneEndpoint represents the endpoint for the cluster's API server. | N/A |
| └>&nbsp;&nbsp; **host** | `string` | host is the hostname on which the API server is serving. | N/A |
| └>&nbsp;&nbsp; **port** | `integer` | port is the port on which the API server is serving. | N/A |
|  **initialized** | `boolean` | Initialized represents whether or not the API server has been provisioned. It fulfills Cluster API's control plane provider contract. For AKS, this is equivalent to `ready`. | N/A |
|  **ready** | `boolean` | Ready represents whether or not the API server is ready to receive requests. It fulfills Cluster API's control plane provider contract. For AKS, this is equivalent to `initialized`. | N/A |
|  **resources** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **ready** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **resource** | `object` | StatusResource is a handle to a resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | No description provided. | N/A |
|  **version** | `string` | Version is the observed Kubernetes version of the control plane. It fulfills Cluster API's control plane provider contract. | N/A |
