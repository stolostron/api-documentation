# VirtualNetwork API

Generator information:
- Generated from: /network/resource-manager/Microsoft.Network/stable/2020-11-01/virtualNetwork.json
- ARM URI: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}

## Spec Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **addressSpace** | `object` | AddressSpace: The AddressSpace that contains an array of IP address ranges that can be used by subnets. | N/A |
| └>&nbsp;&nbsp; **addressPrefixes** | `array` | AddressPrefixes: A list of address blocks reserved for this virtual network in CIDR notation. | N/A |
|  **azureName** | `string` | AzureName: The name of the resource in Azure. This is often the same as the name of the resource in Kubernetes but it doesn't have to be. | N/A |
|  **bgpCommunities** | `object` | BgpCommunities: Bgp Communities sent over ExpressRoute with each route corresponding to a prefix in this VNET. | N/A |
| └>&nbsp;&nbsp; **virtualNetworkCommunity** | `string` | VirtualNetworkCommunity: The BGP community associated with the virtual network. | N/A |
|  **ddosProtectionPlan** | `object` | DdosProtectionPlan: The DDoS protection plan associated with the virtual network. | N/A |
| └>&nbsp;&nbsp; **reference** | `object` | Reference: Resource ID. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
|  **dhcpOptions** | `object` | DhcpOptions: The dhcpOptions that contains an array of DNS servers available to VMs deployed in the virtual network. | N/A |
| └>&nbsp;&nbsp; **dnsServers** | `array` | DnsServers: The list of DNS servers IP addresses. | N/A |
|  **enableDdosProtection** | `boolean` | EnableDdosProtection: Indicates if DDoS protection is enabled for all the protected resources in the virtual network. It requires a DDoS protection plan associated with the resource. | N/A |
|  **enableVmProtection** | `boolean` | EnableVmProtection: Indicates if VM protection is enabled for all the subnets in the virtual network. | N/A |
|  **extendedLocation** | `object` | ExtendedLocation: The extended location of the virtual network. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name: The name of the extended location. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type: The type of the extended location. | N/A |
|  **ipAllocations** | `array` | IpAllocations: Array of IpAllocation which reference this VNET. | N/A |
| └>&nbsp;&nbsp; **reference** | `object` | Reference: Resource ID. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
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

Virtual Network resource.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **addressSpace** | `object` | AddressSpace: The AddressSpace that contains an array of IP address ranges that can be used by subnets. | N/A |
| └>&nbsp;&nbsp; **addressPrefixes** | `array` | AddressPrefixes: A list of address blocks reserved for this virtual network in CIDR notation. | N/A |
|  **bgpCommunities** | `object` | BgpCommunities: Bgp Communities sent over ExpressRoute with each route corresponding to a prefix in this VNET. | N/A |
| └>&nbsp;&nbsp; **regionalCommunity** | `string` | RegionalCommunity: The BGP community associated with the region of the virtual network. | N/A |
| └>&nbsp;&nbsp; **virtualNetworkCommunity** | `string` | VirtualNetworkCommunity: The BGP community associated with the virtual network. | N/A |
|  **conditions** | `array` | Conditions: The observed state of the resource | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the last time the condition transitioned from one status to another. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | ObservedGeneration is the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.condition[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason for the condition's last transition. Reasons are upper CamelCase (PascalCase) with no spaces. A reason is always provided, this field will not be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | Severity with which to treat failures of this type of condition. For conditions which have positive polarity (Status == True is their normal/healthy state), this will be omitted when Status == True For conditions which have negative polarity (Status == False is their normal/healthy state), this will be omitted when Status == False. This is omitted in all cases when Status == Unknown | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status of the condition, one of True, False, or Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type of condition. | N/A |
|  **ddosProtectionPlan** | `object` | DdosProtectionPlan: The DDoS protection plan associated with the virtual network. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **dhcpOptions** | `object` | DhcpOptions: The dhcpOptions that contains an array of DNS servers available to VMs deployed in the virtual network. | N/A |
| └>&nbsp;&nbsp; **dnsServers** | `array` | DnsServers: The list of DNS servers IP addresses. | N/A |
|  **enableDdosProtection** | `boolean` | EnableDdosProtection: Indicates if DDoS protection is enabled for all the protected resources in the virtual network. It requires a DDoS protection plan associated with the resource. | N/A |
|  **enableVmProtection** | `boolean` | EnableVmProtection: Indicates if VM protection is enabled for all the subnets in the virtual network. | N/A |
|  **etag** | `string` | Etag: A unique read-only string that changes whenever the resource is updated. | N/A |
|  **extendedLocation** | `object` | ExtendedLocation: The extended location of the virtual network. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name: The name of the extended location. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type: The type of the extended location. | N/A |
|  **id** | `string` | Id: Resource ID. | N/A |
|  **ipAllocations** | `array` | IpAllocations: Array of IpAllocation which reference this VNET. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **location** | `string` | Location: Resource location. | N/A |
|  **name** | `string` | Name: Resource name. | N/A |
|  **provisioningState** | `string` | ProvisioningState: The provisioning state of the virtual network resource. | N/A |
|  **resourceGuid** | `string` | ResourceGuid: The resourceGuid property of the Virtual Network resource. | N/A |
|  **tags** | `object` | Tags: Resource tags. | N/A |
|  **type** | `string` | Type: Resource type. | N/A |
