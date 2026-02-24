# BastionHost API

Generator information:
- Generated from: /network/resource-manager/Microsoft.Network/stable/2022-07-01/bastionHost.json
- ARM URI: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/bastionHosts/{bastionHostName}

## Spec Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **azureName** | `string` | AzureName: The name of the resource in Azure. This is often the same as the name of the resource in Kubernetes but it doesn't have to be. | N/A |
|  **disableCopyPaste** | `boolean` | DisableCopyPaste: Enable/Disable Copy/Paste feature of the Bastion Host resource. | N/A |
|  **dnsName** | `string` | DnsName: FQDN for the endpoint on which bastion host is accessible. | N/A |
|  **enableFileCopy** | `boolean` | EnableFileCopy: Enable/Disable File Copy feature of the Bastion Host resource. | N/A |
|  **enableIpConnect** | `boolean` | EnableIpConnect: Enable/Disable IP Connect feature of the Bastion Host resource. | N/A |
|  **enableShareableLink** | `boolean` | EnableShareableLink: Enable/Disable Shareable Link of the Bastion Host resource. | N/A |
|  **enableTunneling** | `boolean` | EnableTunneling: Enable/Disable Tunneling feature of the Bastion Host resource. | N/A |
|  **ipConfigurations** | `array` | IpConfigurations: IP configuration of the Bastion Host resource. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name: Name of the resource that is unique within a resource group. This name can be used to access the resource. | N/A |
| └>&nbsp;&nbsp; **privateIPAllocationMethod** | `string` | PrivateIPAllocationMethod: Private IP allocation method. | N/A |
| └>&nbsp;&nbsp; **publicIPAddress** | `object` | PublicIPAddress: Reference of the PublicIP resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **reference** | `object` | Reference: Resource ID. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
| └>&nbsp;&nbsp; **subnet** | `object` | Subnet: Reference of the subnet resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **reference** | `object` | Reference: Resource ID. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
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
|  **scaleUnits** | `integer` | ScaleUnits: The scale units for the Bastion Host resource. | `Minimum=2`<br>`Maximum=50` |
|  **sku** | `object` | Sku: The sku of this Bastion Host. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name: The name of this Bastion Host. | N/A |
|  **tags** | `object` | Tags: Resource tags. | N/A |
## Status Fields

Bastion Host resource.

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
|  **disableCopyPaste** | `boolean` | DisableCopyPaste: Enable/Disable Copy/Paste feature of the Bastion Host resource. | N/A |
|  **dnsName** | `string` | DnsName: FQDN for the endpoint on which bastion host is accessible. | N/A |
|  **enableFileCopy** | `boolean` | EnableFileCopy: Enable/Disable File Copy feature of the Bastion Host resource. | N/A |
|  **enableIpConnect** | `boolean` | EnableIpConnect: Enable/Disable IP Connect feature of the Bastion Host resource. | N/A |
|  **enableShareableLink** | `boolean` | EnableShareableLink: Enable/Disable Shareable Link of the Bastion Host resource. | N/A |
|  **enableTunneling** | `boolean` | EnableTunneling: Enable/Disable Tunneling feature of the Bastion Host resource. | N/A |
|  **etag** | `string` | Etag: A unique read-only string that changes whenever the resource is updated. | N/A |
|  **id** | `string` | Id: Resource ID. | N/A |
|  **ipConfigurations** | `array` | IpConfigurations: IP configuration of the Bastion Host resource. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **location** | `string` | Location: Resource location. | N/A |
|  **name** | `string` | Name: Resource name. | N/A |
|  **provisioningState** | `string` | ProvisioningState: The provisioning state of the bastion host resource. | N/A |
|  **scaleUnits** | `integer` | ScaleUnits: The scale units for the Bastion Host resource. | N/A |
|  **sku** | `object` | Sku: The sku of this Bastion Host. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name: The name of this Bastion Host. | N/A |
|  **tags** | `object` | Tags: Resource tags. | N/A |
|  **type** | `string` | Type: Resource type. | N/A |
