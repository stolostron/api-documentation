# AzureASOManagedClusterTemplate API

AzureASOManagedClusterTemplate is the Schema for the azureasomanagedclustertemplates API.

## Spec Fields

AzureASOManagedClusterTemplateSpec defines the desired state of AzureASOManagedClusterTemplate.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **template** | `object` | AzureASOManagedClusterTemplateResource defines the templated resource. | N/A |
| └>&nbsp;&nbsp; **spec** | `object` | AzureASOManagedClusterTemplateResourceSpec defines the desired state of the templated resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resources** | `array` | Resources are embedded ASO resources to be managed by this resource. | N/A |
## Status Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
