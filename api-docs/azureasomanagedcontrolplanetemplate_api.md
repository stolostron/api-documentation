# AzureASOManagedControlPlaneTemplate API

AzureASOManagedControlPlaneTemplate is the Schema for the azureasomanagedcontrolplanetemplates API.

## Spec Fields

AzureASOManagedControlPlaneTemplateSpec defines the desired state of AzureASOManagedControlPlane.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **template** | `object` | AzureASOManagedControlPlaneResource defines the templated resource. | N/A |
| └>&nbsp;&nbsp; **spec** | `object` | AzureASOManagedControlPlaneTemplateResourceSpec defines the desired state of the templated resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resources** | `array` | Resources are embedded ASO resources to be managed by this resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | Version is the Kubernetes version of the control plane. It fulfills Cluster API's control plane provider contract. | N/A |
## Status Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
