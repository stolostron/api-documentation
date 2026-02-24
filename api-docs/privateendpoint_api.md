# PrivateEndpoint API

Generator information:
- Generated from: /network/resource-manager/Microsoft.Network/stable/2022-07-01/privateEndpoint.json
- ARM URI: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}

## Spec Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **applicationSecurityGroups** | `array` | ApplicationSecurityGroups: Application security groups in which the private endpoint IP configuration is included. | N/A |
| └>&nbsp;&nbsp; **reference** | `object` | Reference: Resource ID. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
|  **azureName** | `string` | AzureName: The name of the resource in Azure. This is often the same as the name of the resource in Kubernetes but it doesn't have to be. | N/A |
|  **customNetworkInterfaceName** | `string` | CustomNetworkInterfaceName: The custom name of the network interface attached to the private endpoint. | N/A |
|  **extendedLocation** | `object` | ExtendedLocation: The extended location of the load balancer. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name: The name of the extended location. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type: The type of the extended location. | N/A |
|  **ipConfigurations** | `array` | IpConfigurations: A list of IP configurations of the private endpoint. This will be used to map to the First Party Service's endpoints. | N/A |
| └>&nbsp;&nbsp; **groupId** | `string` | GroupId: The ID of a group obtained from the remote resource that this private endpoint should connect to. | N/A |
| └>&nbsp;&nbsp; **memberName** | `string` | MemberName: The member name of a group obtained from the remote resource that this private endpoint should connect to. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name: The name of the resource that is unique within a resource group. | N/A |
| └>&nbsp;&nbsp; **privateIPAddress** | `string` | PrivateIPAddress: A private ip address obtained from the private endpoint's subnet. | N/A |
|  **location** | `string` | Location: Resource location. | N/A |
|  **manualPrivateLinkServiceConnections** | `array` | ManualPrivateLinkServiceConnections: A grouping of information about the connection to the remote resource. Used when the network admin does not have access to approve connections to the remote resource. | N/A |
| └>&nbsp;&nbsp; **groupIds** | `array` | GroupIds: The ID(s) of the group(s) obtained from the remote resource that this private endpoint should connect to. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name: The name of the resource that is unique within a resource group. This name can be used to access the resource. | N/A |
| └>&nbsp;&nbsp; **privateLinkServiceConnectionState** | `object` | PrivateLinkServiceConnectionState: A collection of read-only information about the state of the connection to the remote resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **actionsRequired** | `string` | ActionsRequired: A message indicating if changes on the service provider require any updates on the consumer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **description** | `string` | Description: The reason for approval/rejection of the connection. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **status** | `string` | Status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service. | N/A |
| └>&nbsp;&nbsp; **privateLinkServiceReference** | `object` | PrivateLinkServiceReference: The resource id of private link service. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
| └>&nbsp;&nbsp; **requestMessage** | `string` | RequestMessage: A message passed to the owner of the remote resource with this connection request. Restricted to 140 chars. | N/A |
|  **operatorSpec** | `object` | OperatorSpec: The specification for configuring operator behavior. This field is interpreted by the operator and not passed directly to Azure | N/A |
| └>&nbsp;&nbsp; **configMapExpressions** | `array` | ConfigMapExpressions: configures where to place operator written dynamic ConfigMaps (created with CEL expressions). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the ConfigMap or Secret being written to. If the CEL expression in Value returns a string this is required to identify what key to write to. If the CEL expression in Value returns a map[string]string Key must not be set, instead the keys written will be determined dynamically based on the keys of the resulting map[string]string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap or secret to write to. The configmap or secret will be created in the same namespace as the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is a CEL expression. The CEL expression may return a string or a map[string]string. For more information on CEL in ASO see https://azure.github.io/azure-service-operator/guide/expressions/ | N/A |
| └>&nbsp;&nbsp; **configMaps** | `object` | ConfigMaps: configures where to place operator written ConfigMaps. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **primaryNicPrivateIpAddress** | `object` | PrimaryNicPrivateIpAddress: indicates where the PrimaryNicPrivateIpAddress config map should be placed. If omitted, no config map will be created. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the ConfigMap being referenced | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes ConfigMap to write to. The ConfigMap will be created in the same namespace as the resource. | N/A |
| └>&nbsp;&nbsp; **secretExpressions** | `array` | SecretExpressions: configures where to place operator written dynamic secrets (created with CEL expressions). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the ConfigMap or Secret being written to. If the CEL expression in Value returns a string this is required to identify what key to write to. If the CEL expression in Value returns a map[string]string Key must not be set, instead the keys written will be determined dynamically based on the keys of the resulting map[string]string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap or secret to write to. The configmap or secret will be created in the same namespace as the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is a CEL expression. The CEL expression may return a string or a map[string]string. For more information on CEL in ASO see https://azure.github.io/azure-service-operator/guide/expressions/ | N/A |
|  **owner** | `object` | Owner: The owner of the resource. The owner controls where the resource goes when it is deployed. The owner also controls the resources lifecycle. When the owner is deleted the resource will also be deleted. Owner is expected to be a reference to a resources.azure.com/ResourceGroup resource | N/A |
| └>&nbsp;&nbsp; **armId** | `string` | No description provided. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| └>&nbsp;&nbsp; **name** | `string` | This is the name of the Kubernetes resource to reference. | N/A |
|  **privateLinkServiceConnections** | `array` | PrivateLinkServiceConnections: A grouping of information about the connection to the remote resource. | N/A |
| └>&nbsp;&nbsp; **groupIds** | `array` | GroupIds: The ID(s) of the group(s) obtained from the remote resource that this private endpoint should connect to. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name: The name of the resource that is unique within a resource group. This name can be used to access the resource. | N/A |
| └>&nbsp;&nbsp; **privateLinkServiceConnectionState** | `object` | PrivateLinkServiceConnectionState: A collection of read-only information about the state of the connection to the remote resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **actionsRequired** | `string` | ActionsRequired: A message indicating if changes on the service provider require any updates on the consumer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **description** | `string` | Description: The reason for approval/rejection of the connection. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **status** | `string` | Status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service. | N/A |
| └>&nbsp;&nbsp; **privateLinkServiceReference** | `object` | PrivateLinkServiceReference: The resource id of private link service. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
| └>&nbsp;&nbsp; **requestMessage** | `string` | RequestMessage: A message passed to the owner of the remote resource with this connection request. Restricted to 140 chars. | N/A |
|  **subnet** | `object` | Subnet: The ID of the subnet from which the private IP will be allocated. | N/A |
| └>&nbsp;&nbsp; **reference** | `object` | Reference: Resource ID. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
|  **tags** | `object` | Tags: Resource tags. | N/A |
## Status Fields

Private endpoint resource.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **applicationSecurityGroups** | `array` | ApplicationSecurityGroups: Application security groups in which the private endpoint IP configuration is included. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **conditions** | `array` | Conditions: The observed state of the resource | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the last time the condition transitioned from one status to another. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | ObservedGeneration is the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.condition[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason for the condition's last transition. Reasons are upper CamelCase (PascalCase) with no spaces. A reason is always provided, this field will not be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | Severity with which to treat failures of this type of condition. For conditions which have positive polarity (Status == True is their normal/healthy state), this will be omitted when Status == True For conditions which have negative polarity (Status == False is their normal/healthy state), this will be omitted when Status == False. This is omitted in all cases when Status == Unknown | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status of the condition, one of True, False, or Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type of condition. | N/A |
|  **customDnsConfigs** | `array` | CustomDnsConfigs: An array of custom dns configurations. | N/A |
| └>&nbsp;&nbsp; **fqdn** | `string` | Fqdn: Fqdn that resolves to private endpoint ip address. | N/A |
| └>&nbsp;&nbsp; **ipAddresses** | `array` | IpAddresses: A list of private ip addresses of the private endpoint. | N/A |
|  **customNetworkInterfaceName** | `string` | CustomNetworkInterfaceName: The custom name of the network interface attached to the private endpoint. | N/A |
|  **etag** | `string` | Etag: A unique read-only string that changes whenever the resource is updated. | N/A |
|  **extendedLocation** | `object` | ExtendedLocation: The extended location of the load balancer. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name: The name of the extended location. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type: The type of the extended location. | N/A |
|  **id** | `string` | Id: Resource ID. | N/A |
|  **ipConfigurations** | `array` | IpConfigurations: A list of IP configurations of the private endpoint. This will be used to map to the First Party Service's endpoints. | N/A |
| └>&nbsp;&nbsp; **etag** | `string` | Etag: A unique read-only string that changes whenever the resource is updated. | N/A |
| └>&nbsp;&nbsp; **groupId** | `string` | GroupId: The ID of a group obtained from the remote resource that this private endpoint should connect to. | N/A |
| └>&nbsp;&nbsp; **memberName** | `string` | MemberName: The member name of a group obtained from the remote resource that this private endpoint should connect to. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name: The name of the resource that is unique within a resource group. | N/A |
| └>&nbsp;&nbsp; **privateIPAddress** | `string` | PrivateIPAddress: A private ip address obtained from the private endpoint's subnet. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type: The resource type. | N/A |
|  **location** | `string` | Location: Resource location. | N/A |
|  **manualPrivateLinkServiceConnections** | `array` | ManualPrivateLinkServiceConnections: A grouping of information about the connection to the remote resource. Used when the network admin does not have access to approve connections to the remote resource. | N/A |
| └>&nbsp;&nbsp; **etag** | `string` | Etag: A unique read-only string that changes whenever the resource is updated. | N/A |
| └>&nbsp;&nbsp; **groupIds** | `array` | GroupIds: The ID(s) of the group(s) obtained from the remote resource that this private endpoint should connect to. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name: The name of the resource that is unique within a resource group. This name can be used to access the resource. | N/A |
| └>&nbsp;&nbsp; **privateLinkServiceConnectionState** | `object` | PrivateLinkServiceConnectionState: A collection of read-only information about the state of the connection to the remote resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **actionsRequired** | `string` | ActionsRequired: A message indicating if changes on the service provider require any updates on the consumer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **description** | `string` | Description: The reason for approval/rejection of the connection. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **status** | `string` | Status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service. | N/A |
| └>&nbsp;&nbsp; **privateLinkServiceId** | `string` | PrivateLinkServiceId: The resource id of private link service. | N/A |
| └>&nbsp;&nbsp; **provisioningState** | `string` | ProvisioningState: The provisioning state of the private link service connection resource. | N/A |
| └>&nbsp;&nbsp; **requestMessage** | `string` | RequestMessage: A message passed to the owner of the remote resource with this connection request. Restricted to 140 chars. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type: The resource type. | N/A |
|  **name** | `string` | Name: Resource name. | N/A |
|  **networkInterfaces** | `array` | NetworkInterfaces: An array of references to the network interfaces created for this private endpoint. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **privateLinkServiceConnections** | `array` | PrivateLinkServiceConnections: A grouping of information about the connection to the remote resource. | N/A |
| └>&nbsp;&nbsp; **etag** | `string` | Etag: A unique read-only string that changes whenever the resource is updated. | N/A |
| └>&nbsp;&nbsp; **groupIds** | `array` | GroupIds: The ID(s) of the group(s) obtained from the remote resource that this private endpoint should connect to. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name: The name of the resource that is unique within a resource group. This name can be used to access the resource. | N/A |
| └>&nbsp;&nbsp; **privateLinkServiceConnectionState** | `object` | PrivateLinkServiceConnectionState: A collection of read-only information about the state of the connection to the remote resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **actionsRequired** | `string` | ActionsRequired: A message indicating if changes on the service provider require any updates on the consumer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **description** | `string` | Description: The reason for approval/rejection of the connection. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **status** | `string` | Status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service. | N/A |
| └>&nbsp;&nbsp; **privateLinkServiceId** | `string` | PrivateLinkServiceId: The resource id of private link service. | N/A |
| └>&nbsp;&nbsp; **provisioningState** | `string` | ProvisioningState: The provisioning state of the private link service connection resource. | N/A |
| └>&nbsp;&nbsp; **requestMessage** | `string` | RequestMessage: A message passed to the owner of the remote resource with this connection request. Restricted to 140 chars. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type: The resource type. | N/A |
|  **provisioningState** | `string` | ProvisioningState: The provisioning state of the private endpoint resource. | N/A |
|  **subnet** | `object` | Subnet: The ID of the subnet from which the private IP will be allocated. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | Id: Resource ID. | N/A |
|  **tags** | `object` | Tags: Resource tags. | N/A |
|  **type** | `string` | Type: Resource type. | N/A |
