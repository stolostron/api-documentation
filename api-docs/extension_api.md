# Extension API

Generator information:
- Generated from: /kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/stable/2023-05-01/extensions.json
- ARM URI: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/extensions/{extensionName}

## Spec Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **aksAssignedIdentity** | `object` | AksAssignedIdentity: Identity of the Extension resource in an AKS cluster | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type: The identity type. | N/A |
|  **autoUpgradeMinorVersion** | `boolean` | AutoUpgradeMinorVersion: Flag to note if this extension participates in auto upgrade of minor version, or not. | N/A |
|  **azureName** | `string` | AzureName: The name of the resource in Azure. This is often the same as the name of the resource in Kubernetes but it doesn't have to be. | N/A |
|  **configurationProtectedSettings** | `object` | ConfigurationProtectedSettings: Configuration settings that are sensitive, as name-value pairs for configuring this extension. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes secret being referenced. The secret must be in the same namespace as the resource | N/A |
|  **configurationSettings** | `object` | ConfigurationSettings: Configuration settings, as name-value pairs for configuring this extension. | N/A |
|  **extensionType** | `string` | ExtensionType: Type of the Extension, of which this resource is an instance of.  It must be one of the Extension Types registered with Microsoft.KubernetesConfiguration by the Extension publisher. | N/A |
|  **identity** | `object` | Identity: Identity of the Extension resource | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type: The identity type. | N/A |
|  **operatorSpec** | `object` | OperatorSpec: The specification for configuring operator behavior. This field is interpreted by the operator and not passed directly to Azure | N/A |
| └>&nbsp;&nbsp; **configMapExpressions** | `array` | ConfigMapExpressions: configures where to place operator written dynamic ConfigMaps (created with CEL expressions). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the ConfigMap or Secret being written to. If the CEL expression in Value returns a string this is required to identify what key to write to. If the CEL expression in Value returns a map[string]string Key must not be set, instead the keys written will be determined dynamically based on the keys of the resulting map[string]string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap or secret to write to. The configmap or secret will be created in the same namespace as the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is a CEL expression. The CEL expression may return a string or a map[string]string. For more information on CEL in ASO see https://azure.github.io/azure-service-operator/guide/expressions/ | N/A |
| └>&nbsp;&nbsp; **configMaps** | `object` | ConfigMaps: configures where to place operator written ConfigMaps. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **principalId** | `object` | PrincipalId: indicates where the PrincipalId config map should be placed. If omitted, no config map will be created. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the ConfigMap being referenced | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes ConfigMap to write to. The ConfigMap will be created in the same namespace as the resource. | N/A |
| └>&nbsp;&nbsp; **secretExpressions** | `array` | SecretExpressions: configures where to place operator written dynamic secrets (created with CEL expressions). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the ConfigMap or Secret being written to. If the CEL expression in Value returns a string this is required to identify what key to write to. If the CEL expression in Value returns a map[string]string Key must not be set, instead the keys written will be determined dynamically based on the keys of the resulting map[string]string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap or secret to write to. The configmap or secret will be created in the same namespace as the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is a CEL expression. The CEL expression may return a string or a map[string]string. For more information on CEL in ASO see https://azure.github.io/azure-service-operator/guide/expressions/ | N/A |
|  **owner** | `object` | Owner: The owner of the resource. The owner controls where the resource goes when it is deployed. The owner also controls the resources lifecycle. When the owner is deleted the resource will also be deleted. This resource is an extension resource, which means that any other Azure resource can be its owner. | N/A |
| └>&nbsp;&nbsp; **armId** | `string` | Ownership across namespaces is not supported. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| └>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | This is the name of the Kubernetes resource to reference. | N/A |
|  **plan** | `object` | Plan: The plan information. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name: A user defined name of the 3rd Party Artifact that is being procured. | N/A |
| └>&nbsp;&nbsp; **product** | `string` | Product: The 3rd Party artifact that is being procured. E.g. NewRelic. Product maps to the OfferID specified for the artifact at the time of Data Market onboarding. | N/A |
| └>&nbsp;&nbsp; **promotionCode** | `string` | PromotionCode: A publisher provided promotion code as provisioned in Data Market for the said product/artifact. | N/A |
| └>&nbsp;&nbsp; **publisher** | `string` | Publisher: The publisher of the 3rd Party Artifact that is being bought. E.g. NewRelic | N/A |
| └>&nbsp;&nbsp; **version** | `string` | Version: The version of the desired product/artifact. | N/A |
|  **releaseTrain** | `string` | ReleaseTrain: ReleaseTrain this extension participates in for auto-upgrade (e.g. Stable, Preview, etc.) - only if autoUpgradeMinorVersion is 'true'. | N/A |
|  **scope** | `object` | Scope: Scope at which the extension is installed. | N/A |
| └>&nbsp;&nbsp; **cluster** | `object` | Cluster: Specifies that the scope of the extension is Cluster | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **releaseNamespace** | `string` | ReleaseNamespace: Namespace where the extension Release must be placed, for a Cluster scoped extension.  If this namespace does not exist, it will be created | N/A |
| └>&nbsp;&nbsp; **namespace** | `object` | Namespace: Specifies that the scope of the extension is Namespace | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **targetNamespace** | `string` | TargetNamespace: Namespace where the extension will be created for an Namespace scoped extension.  If this namespace does not exist, it will be created | N/A |
|  **systemData** | `object` | SystemData: Top level metadata https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources | N/A |
| └>&nbsp;&nbsp; **createdAt** | `string` | CreatedAt: The timestamp of resource creation (UTC). | N/A |
| └>&nbsp;&nbsp; **createdBy** | `string` | CreatedBy: The identity that created the resource. | N/A |
| └>&nbsp;&nbsp; **createdByType** | `string` | CreatedByType: The type of identity that created the resource. | N/A |
| └>&nbsp;&nbsp; **lastModifiedAt** | `string` | LastModifiedAt: The timestamp of resource last modification (UTC) | N/A |
| └>&nbsp;&nbsp; **lastModifiedBy** | `string` | LastModifiedBy: The identity that last modified the resource. | N/A |
| └>&nbsp;&nbsp; **lastModifiedByType** | `string` | LastModifiedByType: The type of identity that last modified the resource. | N/A |
|  **version** | `string` | Version: User-specified version of the extension for this extension to 'pin'. To use 'version', autoUpgradeMinorVersion must be 'false'. | N/A |
## Status Fields

The Extension object.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **aksAssignedIdentity** | `object` | AksAssignedIdentity: Identity of the Extension resource in an AKS cluster | N/A |
| └>&nbsp;&nbsp; **principalId** | `string` | PrincipalId: The principal ID of resource identity. | N/A |
| └>&nbsp;&nbsp; **tenantId** | `string` | TenantId: The tenant ID of resource. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type: The identity type. | N/A |
|  **autoUpgradeMinorVersion** | `boolean` | AutoUpgradeMinorVersion: Flag to note if this extension participates in auto upgrade of minor version, or not. | N/A |
|  **conditions** | `array` | Conditions: The observed state of the resource | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the last time the condition transitioned from one status to another. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | ObservedGeneration is the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.condition[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason for the condition's last transition. Reasons are upper CamelCase (PascalCase) with no spaces. A reason is always provided, this field will not be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | Severity with which to treat failures of this type of condition. For conditions which have positive polarity (Status == True is their normal/healthy state), this will be omitted when Status == True For conditions which have negative polarity (Status == False is their normal/healthy state), this will be omitted when Status == False. This is omitted in all cases when Status == Unknown | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status of the condition, one of True, False, or Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type of condition. | N/A |
|  **configurationProtectedSettings** | `object` | ConfigurationProtectedSettings: Configuration settings that are sensitive, as name-value pairs for configuring this extension. | N/A |
|  **configurationSettings** | `object` | ConfigurationSettings: Configuration settings, as name-value pairs for configuring this extension. | N/A |
|  **currentVersion** | `string` | CurrentVersion: Currently installed version of the extension. | N/A |
|  **customLocationSettings** | `object` | CustomLocationSettings: Custom Location settings properties. | N/A |
|  **errorInfo** | `object` | ErrorInfo: Error information from the Agent - e.g. errors during installation. | N/A |
| └>&nbsp;&nbsp; **additionalInfo** | `array` | AdditionalInfo: The error additional info. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **info** | `object` | Info: The additional info. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type: The additional info type. | N/A |
| └>&nbsp;&nbsp; **code** | `string` | Code: The error code. | N/A |
| └>&nbsp;&nbsp; **details** | `array` | Details: The error details. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **additionalInfo** | `array` | AdditionalInfo: The error additional info. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **info** | `object` | Info: The additional info. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type: The additional info type. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **code** | `string` | Code: The error code. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **message** | `string` | Message: The error message. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **target** | `string` | Target: The error target. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message: The error message. | N/A |
| └>&nbsp;&nbsp; **target** | `string` | Target: The error target. | N/A |
|  **extensionType** | `string` | ExtensionType: Type of the Extension, of which this resource is an instance of.  It must be one of the Extension Types registered with Microsoft.KubernetesConfiguration by the Extension publisher. | N/A |
|  **id** | `string` | Id: Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} | N/A |
|  **identity** | `object` | Identity: Identity of the Extension resource | N/A |
| └>&nbsp;&nbsp; **principalId** | `string` | PrincipalId: The principal ID of resource identity. | N/A |
| └>&nbsp;&nbsp; **tenantId** | `string` | TenantId: The tenant ID of resource. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type: The identity type. | N/A |
|  **isSystemExtension** | `boolean` | IsSystemExtension: Flag to note if this extension is a system extension | N/A |
|  **name** | `string` | Name: The name of the resource | N/A |
|  **packageUri** | `string` | PackageUri: Uri of the Helm package | N/A |
|  **plan** | `object` | Plan: The plan information. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name: A user defined name of the 3rd Party Artifact that is being procured. | N/A |
| └>&nbsp;&nbsp; **product** | `string` | Product: The 3rd Party artifact that is being procured. E.g. NewRelic. Product maps to the OfferID specified for the artifact at the time of Data Market onboarding. | N/A |
| └>&nbsp;&nbsp; **promotionCode** | `string` | PromotionCode: A publisher provided promotion code as provisioned in Data Market for the said product/artifact. | N/A |
| └>&nbsp;&nbsp; **publisher** | `string` | Publisher: The publisher of the 3rd Party Artifact that is being bought. E.g. NewRelic | N/A |
| └>&nbsp;&nbsp; **version** | `string` | Version: The version of the desired product/artifact. | N/A |
|  **provisioningState** | `string` | ProvisioningState: Status of installation of this extension. | N/A |
|  **releaseTrain** | `string` | ReleaseTrain: ReleaseTrain this extension participates in for auto-upgrade (e.g. Stable, Preview, etc.) - only if autoUpgradeMinorVersion is 'true'. | N/A |
|  **scope** | `object` | Scope: Scope at which the extension is installed. | N/A |
| └>&nbsp;&nbsp; **cluster** | `object` | Cluster: Specifies that the scope of the extension is Cluster | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **releaseNamespace** | `string` | ReleaseNamespace: Namespace where the extension Release must be placed, for a Cluster scoped extension.  If this namespace does not exist, it will be created | N/A |
| └>&nbsp;&nbsp; **namespace** | `object` | Namespace: Specifies that the scope of the extension is Namespace | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **targetNamespace** | `string` | TargetNamespace: Namespace where the extension will be created for an Namespace scoped extension.  If this namespace does not exist, it will be created | N/A |
|  **statuses** | `array` | Statuses: Status from this extension. | N/A |
| └>&nbsp;&nbsp; **code** | `string` | Code: Status code provided by the Extension | N/A |
| └>&nbsp;&nbsp; **displayStatus** | `string` | DisplayStatus: Short description of status of the extension. | N/A |
| └>&nbsp;&nbsp; **level** | `string` | Level: Level of the status. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message: Detailed message of the status from the Extension. | N/A |
| └>&nbsp;&nbsp; **time** | `string` | Time: DateLiteral (per ISO8601) noting the time of installation status. | N/A |
|  **systemData** | `object` | SystemData: Top level metadata https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources | N/A |
| └>&nbsp;&nbsp; **createdAt** | `string` | CreatedAt: The timestamp of resource creation (UTC). | N/A |
| └>&nbsp;&nbsp; **createdBy** | `string` | CreatedBy: The identity that created the resource. | N/A |
| └>&nbsp;&nbsp; **createdByType** | `string` | CreatedByType: The type of identity that created the resource. | N/A |
| └>&nbsp;&nbsp; **lastModifiedAt** | `string` | LastModifiedAt: The timestamp of resource last modification (UTC) | N/A |
| └>&nbsp;&nbsp; **lastModifiedBy** | `string` | LastModifiedBy: The identity that last modified the resource. | N/A |
| └>&nbsp;&nbsp; **lastModifiedByType** | `string` | LastModifiedByType: The type of identity that last modified the resource. | N/A |
|  **type** | `string` | Type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" | N/A |
|  **version** | `string` | Version: User-specified version of the extension for this extension to 'pin'. To use 'version', autoUpgradeMinorVersion must be 'false'. | N/A |
