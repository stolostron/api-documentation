# NetworkSecurityGroup API

Generator information:
- Generated from: /network/resource-manager/Microsoft.Network/stable/2020-11-01/networkSecurityGroup.json
- ARM URI: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityGroups/{networkSecurityGroupName}

## Spec Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **azureName** | `string` | AzureName: The name of the resource in Azure. This is often the same as the name of the resource in Kubernetes but it doesn't have to be. | N/A |
|  **location** | `string` | Location: Resource location. | N/A |
|  **operatorSpec** | `object` | OperatorSpec: The specification for configuring operator behavior. This field is interpreted by the operator and not passed directly to Azure | N/A |
| └>&nbsp;&nbsp; **configMapExpressions** | `array` | ConfigMapExpressions: configures where to place operator written dynamic ConfigMaps (created with CEL expressions). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the ConfigMap or Secret being written to. If the CEL expression in Value returns a string this is required to identify what key to write to. If the CEL expression in Value returns a map[string]string Key must not be set, instead the keys written will be determined dynamically based on the keys of the resulting map[string]string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap or secret to write to. The configmap or secret will be created in the same namespace as the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is a CEL expression. The CEL expression may return a string or a map[string]string. For more information on CEL in ASO see https://azure.github.io/azure-service-operator/guide/expressions/ | N/A |
| └>&nbsp;&nbsp; **secretExpressions** | `array` | SecretExpressions: configures where to place operator written dynamic secrets (created with CEL expressions). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the ConfigMap or Secret being written to. If the CEL expression in Value returns a string this is required to identify what key to write to. If the CEL expression in Value returns a map[string]string Key must not be set, instead the keys written will be determined dynamically based on the keys of the resulting map[string]string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap or secret to write to. The configmap or secret will be created in the same namespace as the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is a CEL expression. The CEL expression may return a string or a map[string]string. For more information on CEL in ASO see https://azure.github.io/azure-service-operator/guide/expressions/ | N/A |
|  **owner** | `object` | Owner: The owner of the resource. The owner controls where the resource goes when it is deployed. The owner also controls the resources lifecycle. When the owner is deleted the resource will also be deleted. Owner is expected to be a reference to a resources.azure.com/ResourceGroup resource | N/A |
| └>&nbsp;&nbsp; **armId** | `string` | No description provided. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| └>&nbsp;&nbsp; **name** | `string` | This is the name of the Kubernetes resource to reference. | N/A |
|  **tags** | `object` | Tags: Resource tags. | N/A |
## Status Fields

NetworkSecurityGroup resource.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions: The observed state of the resource | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the last time the condition transitioned from one status to another. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | ObservedGeneration is the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.condition[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason for the condition's last transition. Reasons are upper CamelCase (PascalCase) with no spaces. A reason is always provided, this field will not be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | Severity with which to treat failures of this type of condition. For conditions which have positive polarity (Status == True is their normal/healthy state), this will be omitted when Status == True For conditions which have negative polarity (Status == False is their normal/healthy state), this will be omitted when Status == False. This is omitted in all cases when Status == Unknown | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status of the condition, one of True, False, or Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type of condition. | N/A |
|  **defaultSecurityRules** | `array` | DefaultSecurityRules: The default security rules of network security group. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **etag** | `string` | Etag: A unique read-only string that changes whenever the resource is updated. | N/A |
|  **flowLogs** | `array` | FlowLogs: A collection of references to flow log resources. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **id** | `string` | Id: Resource ID. | N/A |
|  **location** | `string` | Location: Resource location. | N/A |
|  **name** | `string` | Name: Resource name. | N/A |
|  **networkInterfaces** | `array` | NetworkInterfaces: A collection of references to network interfaces. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **provisioningState** | `string` | ProvisioningState: The provisioning state of the network security group resource. | N/A |
|  **resourceGuid** | `string` | ResourceGuid: The resource GUID property of the network security group resource. | N/A |
|  **subnets** | `array` | Subnets: A collection of references to subnets. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **tags** | `object` | Tags: Resource tags. | N/A |
|  **type** | `string` | Type: Resource type. | N/A |
