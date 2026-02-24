# AzureASOManagedMachinePool API

AzureASOManagedMachinePool is the Schema for the azureasomanagedmachinepools API.

## Spec Fields

AzureASOManagedMachinePoolSpec defines the desired state of AzureASOManagedMachinePool.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **providerIDList** | `array` | ProviderIDList is the list of cloud provider IDs for the instances. It fulfills Cluster API's machine pool infrastructure provider contract. | N/A |
|  **resources** | `array` | Resources are embedded ASO resources to be managed by this resource. | N/A |
## Status Fields

AzureASOManagedMachinePoolStatus defines the observed state of AzureASOManagedMachinePool.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **ready** | `boolean` | Ready represents whether or not the infrastructure is ready to be used. It fulfills Cluster API's machine pool infrastructure provider contract. | N/A |
|  **replicas** | `integer` | Replicas is the current number of provisioned replicas. It fulfills Cluster API's machine pool infrastructure provider contract. | N/A |
|  **resources** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **ready** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **resource** | `object` | StatusResource is a handle to a resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | No description provided. | N/A |
