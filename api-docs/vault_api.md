# Vault API

Generator information:
- Generated from: /keyvault/resource-manager/Microsoft.KeyVault/preview/2021-04-01-preview/keyvault.json
- ARM URI: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}

## Spec Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **azureName** | `string` | AzureName: The name of the resource in Azure. This is often the same as the name of the resource in Kubernetes but it doesn't have to be. | `Pattern=^[a-zA-Z0-9-]{3,24}$` |
|  **location** | `string` | Location: The supported Azure location where the key vault should be created. | N/A |
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
|  **properties** | `object` | Properties: Properties of the vault | N/A |
| └>&nbsp;&nbsp; **accessPolicies** | `array` | AccessPolicies: An array of 0 to 1024 identities that have access to the key vault. All identities in the array must use the same tenant ID as the key vault's tenant ID. When `createMode` is set to `recover`, access policies are not required. Otherwise, access policies are required. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **applicationId** | `string` | ApplicationId:  Application ID of the client making request on behalf of a principal | `Pattern=^[0-9a-fA-F]{8}(-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}$` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **applicationIdFromConfig** | `object` | ApplicationIdFromConfig:  Application ID of the client making request on behalf of a principal | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the Kubernetes configmap being referenced | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap being referenced. The configmap must be in the same namespace as the resource | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **objectId** | `string` | ObjectId: The object ID of a user, service principal or security group in the Azure Active Directory tenant for the vault. The object ID must be unique for the list of access policies. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **objectIdFromConfig** | `object` | ObjectIdFromConfig: The object ID of a user, service principal or security group in the Azure Active Directory tenant for the vault. The object ID must be unique for the list of access policies. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the Kubernetes configmap being referenced | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap being referenced. The configmap must be in the same namespace as the resource | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **permissions** | `object` | Permissions: Permissions the identity has for keys, secrets and certificates. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **certificates** | `array` | Certificates: Permissions to certificates | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **keys** | `array` | Keys: Permissions to keys | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **secrets** | `array` | Secrets: Permissions to secrets | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **storage** | `array` | Storage: Permissions to storage accounts | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tenantId** | `string` | TenantId: The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. | `Pattern=^[0-9a-fA-F]{8}(-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}$` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tenantIdFromConfig** | `object` | TenantIdFromConfig: The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the Kubernetes configmap being referenced | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap being referenced. The configmap must be in the same namespace as the resource | N/A |
| └>&nbsp;&nbsp; **createMode** | `string` | CreateMode: The vault's create mode to indicate whether the vault need to be recovered or not. | N/A |
| └>&nbsp;&nbsp; **enablePurgeProtection** | `boolean` | EnablePurgeProtection: Property specifying whether protection against purge is enabled for this vault. Setting this property to true activates protection against purge for this vault and its content - only the Key Vault service may initiate a hard, irrecoverable deletion. The setting is effective only if soft delete is also enabled. Enabling this functionality is irreversible - that is, the property does not accept false as its value. | N/A |
| └>&nbsp;&nbsp; **enableRbacAuthorization** | `boolean` | EnableRbacAuthorization: Property that controls how data actions are authorized. When true, the key vault will use Role Based Access Control (RBAC) for authorization of data actions, and the access policies specified in vault properties will be  ignored. When false, the key vault will use the access policies specified in vault properties, and any policy stored on Azure Resource Manager will be ignored. If null or not specified, the vault is created with the default value of false. Note that management actions are always authorized with RBAC. | N/A |
| └>&nbsp;&nbsp; **enableSoftDelete** | `boolean` | EnableSoftDelete: Property to specify whether the 'soft delete' functionality is enabled for this key vault. If it's not set to any value(true or false) when creating new key vault, it will be set to true by default. Once set to true, it cannot be reverted to false. | N/A |
| └>&nbsp;&nbsp; **enabledForDeployment** | `boolean` | EnabledForDeployment: Property to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault. | N/A |
| └>&nbsp;&nbsp; **enabledForDiskEncryption** | `boolean` | EnabledForDiskEncryption: Property to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys. | N/A |
| └>&nbsp;&nbsp; **enabledForTemplateDeployment** | `boolean` | EnabledForTemplateDeployment: Property to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault. | N/A |
| └>&nbsp;&nbsp; **networkAcls** | `object` | NetworkAcls: Rules governing the accessibility of the key vault from specific network locations. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **bypass** | `string` | Bypass: Tells what traffic can bypass network rules. This can be 'AzureServices' or 'None'.  If not specified the default is 'AzureServices'. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **defaultAction** | `string` | DefaultAction: The default action when no rule from ipRules and from virtualNetworkRules match. This is only used after the bypass property has been evaluated. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipRules** | `array` | IpRules: The list of IP address rules. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value: An IPv4 address range in CIDR notation, such as '124.56.78.91' (simple IP address) or '124.56.78.0/24' (all addresses that start with 124.56.78). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **virtualNetworkRules** | `array` | VirtualNetworkRules: The list of virtual network rules. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ignoreMissingVnetServiceEndpoint** | `boolean` | IgnoreMissingVnetServiceEndpoint: Property to specify whether NRP will ignore the check if parent subnet has serviceEndpoints configured. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **reference** | `object` | Reference: Full resource id of a vnet subnet, such as '/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/test-vnet/subnets/subnet1'. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
| └>&nbsp;&nbsp; **provisioningState** | `string` | ProvisioningState: Provisioning state of the vault. | N/A |
| └>&nbsp;&nbsp; **sku** | `object` | Sku: SKU details | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **family** | `string` | Family: SKU family name | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name: SKU name to specify whether the key vault is a standard vault or a premium vault. | N/A |
| └>&nbsp;&nbsp; **softDeleteRetentionInDays** | `integer` | SoftDeleteRetentionInDays: softDelete data retention days. It accepts >=7 and <=90. | N/A |
| └>&nbsp;&nbsp; **tenantId** | `string` | TenantId: The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. | `Pattern=^[0-9a-fA-F]{8}(-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}$` |
| └>&nbsp;&nbsp; **tenantIdFromConfig** | `object` | TenantIdFromConfig: The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the Kubernetes configmap being referenced | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap being referenced. The configmap must be in the same namespace as the resource | N/A |
| └>&nbsp;&nbsp; **vaultUri** | `string` | VaultUri: The URI of the vault for performing operations on keys and secrets. | N/A |
|  **tags** | `object` | Tags: The tags that will be assigned to the key vault. | N/A |
## Status Fields

Resource information with extended details.

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
|  **id** | `string` | Id: Fully qualified identifier of the key vault resource. | N/A |
|  **location** | `string` | Location: Azure location of the key vault resource. | N/A |
|  **name** | `string` | Name: Name of the key vault resource. | N/A |
|  **properties** | `object` | Properties: Properties of the vault | N/A |
| └>&nbsp;&nbsp; **accessPolicies** | `array` | AccessPolicies: An array of 0 to 1024 identities that have access to the key vault. All identities in the array must use the same tenant ID as the key vault's tenant ID. When `createMode` is set to `recover`, access policies are not required. Otherwise, access policies are required. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **applicationId** | `string` | ApplicationId:  Application ID of the client making request on behalf of a principal | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **objectId** | `string` | ObjectId: The object ID of a user, service principal or security group in the Azure Active Directory tenant for the vault. The object ID must be unique for the list of access policies. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **permissions** | `object` | Permissions: Permissions the identity has for keys, secrets and certificates. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **certificates** | `array` | Certificates: Permissions to certificates | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **keys** | `array` | Keys: Permissions to keys | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **secrets** | `array` | Secrets: Permissions to secrets | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **storage** | `array` | Storage: Permissions to storage accounts | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tenantId** | `string` | TenantId: The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. | N/A |
| └>&nbsp;&nbsp; **createMode** | `string` | CreateMode: The vault's create mode to indicate whether the vault need to be recovered or not. | N/A |
| └>&nbsp;&nbsp; **enablePurgeProtection** | `boolean` | EnablePurgeProtection: Property specifying whether protection against purge is enabled for this vault. Setting this property to true activates protection against purge for this vault and its content - only the Key Vault service may initiate a hard, irrecoverable deletion. The setting is effective only if soft delete is also enabled. Enabling this functionality is irreversible - that is, the property does not accept false as its value. | N/A |
| └>&nbsp;&nbsp; **enableRbacAuthorization** | `boolean` | EnableRbacAuthorization: Property that controls how data actions are authorized. When true, the key vault will use Role Based Access Control (RBAC) for authorization of data actions, and the access policies specified in vault properties will be  ignored. When false, the key vault will use the access policies specified in vault properties, and any policy stored on Azure Resource Manager will be ignored. If null or not specified, the vault is created with the default value of false. Note that management actions are always authorized with RBAC. | N/A |
| └>&nbsp;&nbsp; **enableSoftDelete** | `boolean` | EnableSoftDelete: Property to specify whether the 'soft delete' functionality is enabled for this key vault. If it's not set to any value(true or false) when creating new key vault, it will be set to true by default. Once set to true, it cannot be reverted to false. | N/A |
| └>&nbsp;&nbsp; **enabledForDeployment** | `boolean` | EnabledForDeployment: Property to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault. | N/A |
| └>&nbsp;&nbsp; **enabledForDiskEncryption** | `boolean` | EnabledForDiskEncryption: Property to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys. | N/A |
| └>&nbsp;&nbsp; **enabledForTemplateDeployment** | `boolean` | EnabledForTemplateDeployment: Property to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault. | N/A |
| └>&nbsp;&nbsp; **hsmPoolResourceId** | `string` | HsmPoolResourceId: The resource id of HSM Pool. | N/A |
| └>&nbsp;&nbsp; **networkAcls** | `object` | NetworkAcls: Rules governing the accessibility of the key vault from specific network locations. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **bypass** | `string` | Bypass: Tells what traffic can bypass network rules. This can be 'AzureServices' or 'None'.  If not specified the default is 'AzureServices'. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **defaultAction** | `string` | DefaultAction: The default action when no rule from ipRules and from virtualNetworkRules match. This is only used after the bypass property has been evaluated. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipRules** | `array` | IpRules: The list of IP address rules. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value: An IPv4 address range in CIDR notation, such as '124.56.78.91' (simple IP address) or '124.56.78.0/24' (all addresses that start with 124.56.78). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **virtualNetworkRules** | `array` | VirtualNetworkRules: The list of virtual network rules. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | Id: Full resource id of a vnet subnet, such as '/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/test-vnet/subnets/subnet1'. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ignoreMissingVnetServiceEndpoint** | `boolean` | IgnoreMissingVnetServiceEndpoint: Property to specify whether NRP will ignore the check if parent subnet has serviceEndpoints configured. | N/A |
| └>&nbsp;&nbsp; **privateEndpointConnections** | `array` | PrivateEndpointConnections: List of private endpoint connections associated with the key vault. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **etag** | `string` | Etag: Modified whenever there is a change in the state of private endpoint connection. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | Id: Id of private endpoint connection. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **privateEndpoint** | `object` | PrivateEndpoint: Properties of the private endpoint object. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | Id: Full identifier of the private endpoint resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **privateLinkServiceConnectionState** | `object` | PrivateLinkServiceConnectionState: Approval state of the private link connection. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **actionsRequired** | `string` | ActionsRequired: A message indicating if changes on the service provider require any updates on the consumer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **description** | `string` | Description: The reason for approval or rejection. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **status** | `string` | Status: Indicates whether the connection has been approved, rejected or removed by the key vault owner. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **provisioningState** | `string` | ProvisioningState: Provisioning state of the private endpoint connection. | N/A |
| └>&nbsp;&nbsp; **provisioningState** | `string` | ProvisioningState: Provisioning state of the vault. | N/A |
| └>&nbsp;&nbsp; **sku** | `object` | Sku: SKU details | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **family** | `string` | Family: SKU family name | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name: SKU name to specify whether the key vault is a standard vault or a premium vault. | N/A |
| └>&nbsp;&nbsp; **softDeleteRetentionInDays** | `integer` | SoftDeleteRetentionInDays: softDelete data retention days. It accepts >=7 and <=90. | N/A |
| └>&nbsp;&nbsp; **tenantId** | `string` | TenantId: The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. | N/A |
| └>&nbsp;&nbsp; **vaultUri** | `string` | VaultUri: The URI of the vault for performing operations on keys and secrets. | N/A |
|  **systemData** | `object` | SystemData: System metadata for the key vault. | N/A |
| └>&nbsp;&nbsp; **createdAt** | `string` | CreatedAt: The timestamp of the key vault resource creation (UTC). | N/A |
| └>&nbsp;&nbsp; **createdBy** | `string` | CreatedBy: The identity that created the key vault resource. | N/A |
| └>&nbsp;&nbsp; **createdByType** | `string` | CreatedByType: The type of identity that created the key vault resource. | N/A |
| └>&nbsp;&nbsp; **lastModifiedAt** | `string` | LastModifiedAt: The timestamp of the key vault resource last modification (UTC). | N/A |
| └>&nbsp;&nbsp; **lastModifiedBy** | `string` | LastModifiedBy: The identity that last modified the key vault resource. | N/A |
| └>&nbsp;&nbsp; **lastModifiedByType** | `string` | LastModifiedByType: The type of identity that last modified the key vault resource. | N/A |
|  **tags** | `object` | Tags: Tags assigned to the key vault resource. | N/A |
|  **type** | `string` | Type: Resource type of the key vault resource. | N/A |
