# VirtualNetworksSubnet API

Generator information:
- Generated from: /network/resource-manager/Microsoft.Network/stable/2020-11-01/virtualNetwork.json
- ARM URI: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}

## Spec Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **addressPrefix** | `string` | AddressPrefix: The address prefix for the subnet. | N/A |
|  **addressPrefixes** | `array` | AddressPrefixes: List of address prefixes for the subnet. | N/A |
|  **applicationGatewayIpConfigurations** | `array` | ApplicationGatewayIpConfigurations: Application gateway IP configurations of virtual network resource. | N/A |
| └>&nbsp;&nbsp; **reference** | `object` | Reference: Resource ID. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
|  **azureName** | `string` | AzureName: The name of the resource in Azure. This is often the same as the name of the resource in Kubernetes but it doesn't have to be. | N/A |
|  **delegations** | `array` | Delegations: An array of references to the delegations on the subnet. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name: The name of the resource that is unique within a subnet. This name can be used to access the resource. | N/A |
| └>&nbsp;&nbsp; **serviceName** | `string` | ServiceName: The name of the service to whom the subnet should be delegated (e.g. Microsoft.Sql/servers). | N/A |
|  **ipAllocations** | `array` | IpAllocations: Array of IpAllocation which reference this subnet. | N/A |
| └>&nbsp;&nbsp; **reference** | `object` | Reference: Resource ID. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
|  **natGateway** | `object` | NatGateway: Nat gateway associated with this subnet. | N/A |
| └>&nbsp;&nbsp; **reference** | `object` | Reference: Resource ID. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
|  **networkSecurityGroup** | `object` | NetworkSecurityGroup: The reference to the NetworkSecurityGroup resource. | N/A |
| └>&nbsp;&nbsp; **reference** | `object` | Reference: Resource ID. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
|  **operatorSpec** | `object` | OperatorSpec: The specification for configuring operator behavior. This field is interpreted by the operator and not passed directly to Azure | N/A |
| └>&nbsp;&nbsp; **configMapExpressions** | `array` | ConfigMapExpressions: configures where to place operator written dynamic ConfigMaps (created with CEL expressions). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the ConfigMap or Secret being written to. If the CEL expression in Value returns a string this is required to identify what key to write to. If the CEL expression in Value returns a map[string]string Key must not be set, instead the keys written will be determined dynamically based on the keys of the resulting map[string]string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap or secret to write to. The configmap or secret will be created in the same namespace as the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is a CEL expression. The CEL expression may return a string or a map[string]string. For more information on CEL in ASO see https://azure.github.io/azure-service-operator/guide/expressions/ | N/A |
| └>&nbsp;&nbsp; **secretExpressions** | `array` | SecretExpressions: configures where to place operator written dynamic secrets (created with CEL expressions). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the ConfigMap or Secret being written to. If the CEL expression in Value returns a string this is required to identify what key to write to. If the CEL expression in Value returns a map[string]string Key must not be set, instead the keys written will be determined dynamically based on the keys of the resulting map[string]string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap or secret to write to. The configmap or secret will be created in the same namespace as the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is a CEL expression. The CEL expression may return a string or a map[string]string. For more information on CEL in ASO see https://azure.github.io/azure-service-operator/guide/expressions/ | N/A |
|  **owner** | `object` | Owner: The owner of the resource. The owner controls where the resource goes when it is deployed. The owner also controls the resources lifecycle. When the owner is deleted the resource will also be deleted. Owner is expected to be a reference to a network.azure.com/VirtualNetwork resource | N/A |
| └>&nbsp;&nbsp; **armId** | `string` | No description provided. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| └>&nbsp;&nbsp; **name** | `string` | This is the name of the Kubernetes resource to reference. | N/A |
|  **privateEndpointNetworkPolicies** | `string` | PrivateEndpointNetworkPolicies: Enable or Disable apply network policies on private end point in the subnet. | N/A |
|  **privateLinkServiceNetworkPolicies** | `string` | PrivateLinkServiceNetworkPolicies: Enable or Disable apply network policies on private link service in the subnet. | N/A |
|  **routeTable** | `object` | RouteTable: The reference to the RouteTable resource. | N/A |
| └>&nbsp;&nbsp; **reference** | `object` | Reference: Resource ID. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
|  **serviceEndpointPolicies** | `array` | ServiceEndpointPolicies: An array of service endpoint policies. | N/A |
| └>&nbsp;&nbsp; **reference** | `object` | Reference: Resource ID. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
|  **serviceEndpoints** | `array` | ServiceEndpoints: An array of service endpoints. | N/A |
| └>&nbsp;&nbsp; **locations** | `array` | Locations: A list of locations. | N/A |
| └>&nbsp;&nbsp; **service** | `string` | Service: The type of the endpoint service. | N/A |
## Status Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **addressPrefix** | `string` | AddressPrefix: The address prefix for the subnet. | N/A |
|  **addressPrefixes** | `array` | AddressPrefixes: List of address prefixes for the subnet. | N/A |
|  **applicationGatewayIpConfigurations** | `array` | ApplicationGatewayIpConfigurations: Application gateway IP configurations of virtual network resource. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **conditions** | `array` | Conditions: The observed state of the resource | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the last time the condition transitioned from one status to another. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | ObservedGeneration is the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.condition[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason for the condition's last transition. Reasons are upper CamelCase (PascalCase) with no spaces. A reason is always provided, this field will not be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | Severity with which to treat failures of this type of condition. For conditions which have positive polarity (Status == True is their normal/healthy state), this will be omitted when Status == True For conditions which have negative polarity (Status == False is their normal/healthy state), this will be omitted when Status == False. This is omitted in all cases when Status == Unknown | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status of the condition, one of True, False, or Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type of condition. | N/A |
|  **delegations** | `array` | Delegations: An array of references to the delegations on the subnet. | N/A |
| └>&nbsp;&nbsp; **actions** | `array` | Actions: The actions permitted to the service upon delegation. | N/A |
| └>&nbsp;&nbsp; **etag** | `string` | Etag: A unique read-only string that changes whenever the resource is updated. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name: The name of the resource that is unique within a subnet. This name can be used to access the resource. | N/A |
| └>&nbsp;&nbsp; **provisioningState** | `string` | ProvisioningState: The provisioning state of the service delegation resource. | N/A |
| └>&nbsp;&nbsp; **serviceName** | `string` | ServiceName: The name of the service to whom the subnet should be delegated (e.g. Microsoft.Sql/servers). | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type: Resource type. | N/A |
|  **etag** | `string` | Etag: A unique read-only string that changes whenever the resource is updated. | N/A |
|  **id** | `string` | Id: Resource ID. | N/A |
|  **ipAllocations** | `array` | IpAllocations: Array of IpAllocation which reference this subnet. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **ipConfigurationProfiles** | `array` | IpConfigurationProfiles: Array of IP configuration profiles which reference this subnet. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **ipConfigurations** | `array` | IpConfigurations: An array of references to the network interface IP configurations using subnet. This field is not included if there are more than 2000 entries. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **name** | `string` | Name: The name of the resource that is unique within a resource group. This name can be used to access the resource. | N/A |
|  **natGateway** | `object` | NatGateway: Nat gateway associated with this subnet. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **networkSecurityGroup** | `object` | NetworkSecurityGroup: The reference to the NetworkSecurityGroup resource. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **privateEndpointNetworkPolicies** | `string` | PrivateEndpointNetworkPolicies: Enable or Disable apply network policies on private end point in the subnet. | N/A |
|  **privateEndpoints** | `array` | PrivateEndpoints: An array of references to private endpoints. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **privateLinkServiceNetworkPolicies** | `string` | PrivateLinkServiceNetworkPolicies: Enable or Disable apply network policies on private link service in the subnet. | N/A |
|  **provisioningState** | `string` | ProvisioningState: The provisioning state of the subnet resource. | N/A |
|  **purpose** | `string` | Purpose: A read-only string identifying the intention of use for this subnet based on delegations and other user-defined properties. | N/A |
|  **resourceNavigationLinks** | `array` | ResourceNavigationLinks: An array of references to the external resources using subnet. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource navigation link identifier. | N/A |
|  **routeTable** | `object` | RouteTable: The reference to the RouteTable resource. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **serviceAssociationLinks** | `array` | ServiceAssociationLinks: An array of references to services injecting into this subnet. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **serviceEndpointPolicies** | `array` | ServiceEndpointPolicies: An array of service endpoint policies. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **serviceEndpoints** | `array` | ServiceEndpoints: An array of service endpoints. | N/A |
| └>&nbsp;&nbsp; **locations** | `array` | Locations: A list of locations. | N/A |
| └>&nbsp;&nbsp; **provisioningState** | `string` | ProvisioningState: The provisioning state of the service endpoint resource. | N/A |
| └>&nbsp;&nbsp; **service** | `string` | Service: The type of the endpoint service. | N/A |
|  **type** | `string` | Type: Resource type. | N/A |
