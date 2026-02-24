# HcpOpenShiftClustersExternalAuth API

Generator information:
- Generated from: /redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/hcpclusters/preview/2024-06-10-preview/openapi.json
- ARM URI: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RedHatOpenShift/hcpOpenShiftClusters/{hcpOpenShiftClusterName}/externalAuths/{externalAuthName}

## Spec Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **azureName** | `string` | AzureName: The name of the resource in Azure. This is often the same as the name of the resource in Kubernetes but it doesn't have to be. | `Pattern=^[a-zA-Z][-a-zA-Z0-9]{1,15}$` |
|  **operatorSpec** | `object` | OperatorSpec: The specification for configuring operator behavior. This field is interpreted by the operator and not passed directly to Azure | N/A |
| └>&nbsp;&nbsp; **configMapExpressions** | `array` | ConfigMapExpressions: configures where to place operator written dynamic ConfigMaps (created with CEL expressions). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the ConfigMap or Secret being written to. If the CEL expression in Value returns a string this is required to identify what key to write to. If the CEL expression in Value returns a map[string]string Key must not be set, instead the keys written will be determined dynamically based on the keys of the resulting map[string]string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap or secret to write to. The configmap or secret will be created in the same namespace as the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is a CEL expression. The CEL expression may return a string or a map[string]string. For more information on CEL in ASO see https://azure.github.io/azure-service-operator/guide/expressions/ | N/A |
| └>&nbsp;&nbsp; **secretExpressions** | `array` | SecretExpressions: configures where to place operator written dynamic secrets (created with CEL expressions). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the ConfigMap or Secret being written to. If the CEL expression in Value returns a string this is required to identify what key to write to. If the CEL expression in Value returns a map[string]string Key must not be set, instead the keys written will be determined dynamically based on the keys of the resulting map[string]string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap or secret to write to. The configmap or secret will be created in the same namespace as the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is a CEL expression. The CEL expression may return a string or a map[string]string. For more information on CEL in ASO see https://azure.github.io/azure-service-operator/guide/expressions/ | N/A |
|  **owner** | `object` | Owner: The owner of the resource. The owner controls where the resource goes when it is deployed. The owner also controls the resources lifecycle. When the owner is deleted the resource will also be deleted. Owner is expected to be a reference to a redhatopenshift.azure.com/HcpOpenShiftCluster resource | N/A |
| └>&nbsp;&nbsp; **armId** | `string` | No description provided. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| └>&nbsp;&nbsp; **name** | `string` | This is the name of the Kubernetes resource to reference. | N/A |
|  **properties** | `object` | Properties: The resource-specific properties for this resource. | N/A |
| └>&nbsp;&nbsp; **claim** | `object` | Claim: External Auth claim This configures how claims are validated and applied. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **mappings** | `object` | Mappings: The claim mappings | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **groups** | `object` | Groups: The claim mappings groups. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **claim** | `string` | Claim: Claim name of the external profile | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **prefix** | `string` | Prefix: Prefix for the claim external profile If this is specified prefixPolicy will be set to "Prefix" by default | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **username** | `object` | Username: The claim mappings username. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **claim** | `string` | Claim: Claim name of the external profile | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **prefix** | `string` | Prefix: Prefix for the claim external profile Must be set when the prefixPolicy field is set to 'Prefix' and must be unset otherwise. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **prefixPolicy** | `string` | PrefixPolicy: Prefix policy is an optional field that configures how a prefix should be applied to the value of the JWT claim specified in the 'claim' field. Allowed values are 'Prefix', 'NoPrefix', and 'None'. When set to 'Prefix', the value specified in the prefix field will be prepended to the value of the JWT claim. The prefix field must be set when prefixPolicy is 'Prefix'. When set to 'NoPrefix', no prefix will be prepended to the value of the JWT claim. When set to 'None', this means no opinion and the platform is left to choose any prefixes that are applied which is subject to change over time. Currently, the platform prepends `{issuerURL}#` to the value of the JWT claim when the claim is not 'email'. As an example, consider the following scenario: `prefix` is unset, `issuerURL` is set to `https://myoidc.tld`, the JWT claims include "username":"userA" and "email":"userA | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **validationRules** | `array` | ValidationRules: The claim validation rules | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **requiredClaim** | `object` | RequiredClaim: The required claim rule to be applied. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **claim** | `string` | Claim: Claim name for the validation profile claim is a required field that configures the name of the required claim. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **requiredValue** | `string` | RequiredValue: Required value requiredValue is a required field that configures the value that 'claim' must have when taken from the incoming JWT claims. If the value in the JWT claims does not match, the token will be rejected for authentication. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type: This configures the type of the validation rule. It defaults to "RequiredClaim" | N/A |
| └>&nbsp;&nbsp; **clients** | `array` | Clients: External Auth OIDC clients There must not be more than 20 entries and entries must have unique namespace/name pairs. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **clientId** | `string` | ClientId: External Auth client id The clientId must appear in the audience field of the TokenIssuerProfile. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **component** | `object` | Component: External Auth client component | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **authClientNamespace** | `string` | AuthClientNamespace: The namespace of the external Auth client This specifies the namespace in which the platform component being configured to use the identity provider as an authentication mode is running. It is used in combination with name as a unique identifier. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name: The name of the external auth client This specifies the name of the platform component being configured to use the identity provider as an authentication mode. It is used in combination with namespace as a unique identifier. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **extraScopes** | `array` | ExtraScopes: external auth client scopes This is useful if you have configured claim mappings that requires specific scopes to be requested beyond the standard OIDC scopes. When omitted, no additional scopes are requested. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type: Determines the OIDC provider client type. | N/A |
| └>&nbsp;&nbsp; **issuer** | `object` | Issuer: Token Issuer profile | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **audiences** | `array` | Audiences: This configures the acceptable audiences the JWT token, issued by the identity provider, must be issued to. At least one of the entries must match the 'aud' claim in the JWT token. audiences must contain at least one entry and must not exceed ten entries. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ca** | `string` | Ca: The issuer of the token Certificate bundle to use to validate server certificates for the configured URL. It must be PEM encoded and when not specified, the system trust is used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **url** | `string` | Url: This configures the URL used to issue tokens by the identity provider. The Kubernetes API server determines how authentication tokens should be handled by matching the 'iss' claim in the JWT to the issuerURL of configured identity providers. issuerURL must use the 'https' scheme. | N/A |
## Status Fields

No description available.

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
|  **id** | `string` | Id: Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" | N/A |
|  **name** | `string` | Name: The name of the resource | N/A |
|  **properties** | `object` | Properties: The resource-specific properties for this resource. | N/A |
| └>&nbsp;&nbsp; **claim** | `object` | Claim: External Auth claim This configures how claims are validated and applied. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **mappings** | `object` | Mappings: The claim mappings | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **groups** | `object` | Groups: The claim mappings groups. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **claim** | `string` | Claim: Claim name of the external profile | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **prefix** | `string` | Prefix: Prefix for the claim external profile If this is specified prefixPolicy will be set to "Prefix" by default | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **username** | `object` | Username: The claim mappings username. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **claim** | `string` | Claim: Claim name of the external profile | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **prefix** | `string` | Prefix: Prefix for the claim external profile Must be set when the prefixPolicy field is set to 'Prefix' and must be unset otherwise. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **prefixPolicy** | `string` | PrefixPolicy: Prefix policy is an optional field that configures how a prefix should be applied to the value of the JWT claim specified in the 'claim' field. Allowed values are 'Prefix', 'NoPrefix', and 'None'. When set to 'Prefix', the value specified in the prefix field will be prepended to the value of the JWT claim. The prefix field must be set when prefixPolicy is 'Prefix'. When set to 'NoPrefix', no prefix will be prepended to the value of the JWT claim. When set to 'None', this means no opinion and the platform is left to choose any prefixes that are applied which is subject to change over time. Currently, the platform prepends `{issuerURL}#` to the value of the JWT claim when the claim is not 'email'. As an example, consider the following scenario: `prefix` is unset, `issuerURL` is set to `https://myoidc.tld`, the JWT claims include "username":"userA" and "email":"userA | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **validationRules** | `array` | ValidationRules: The claim validation rules | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **requiredClaim** | `object` | RequiredClaim: The required claim rule to be applied. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **claim** | `string` | Claim: Claim name for the validation profile claim is a required field that configures the name of the required claim. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **requiredValue** | `string` | RequiredValue: Required value requiredValue is a required field that configures the value that 'claim' must have when taken from the incoming JWT claims. If the value in the JWT claims does not match, the token will be rejected for authentication. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type: This configures the type of the validation rule. It defaults to "RequiredClaim" | N/A |
| └>&nbsp;&nbsp; **clients** | `array` | Clients: External Auth OIDC clients There must not be more than 20 entries and entries must have unique namespace/name pairs. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **clientId** | `string` | ClientId: External Auth client id The clientId must appear in the audience field of the TokenIssuerProfile. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **component** | `object` | Component: External Auth client component | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **authClientNamespace** | `string` | AuthClientNamespace: The namespace of the external Auth client This specifies the namespace in which the platform component being configured to use the identity provider as an authentication mode is running. It is used in combination with name as a unique identifier. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name: The name of the external auth client This specifies the name of the platform component being configured to use the identity provider as an authentication mode. It is used in combination with namespace as a unique identifier. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **extraScopes** | `array` | ExtraScopes: external auth client scopes This is useful if you have configured claim mappings that requires specific scopes to be requested beyond the standard OIDC scopes. When omitted, no additional scopes are requested. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type: Determines the OIDC provider client type. | N/A |
| └>&nbsp;&nbsp; **condition** | `object` | Condition: An observation of the current state with additional information. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime: The last time the condition transitioned from one status to another. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **message** | `string` | Message: This is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **reason** | `string` | Reason: This contains a programmatic identifier indicating the reason for the condition's last transition. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **status** | `string` | Status: The status of the condition. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type: This is a PascalCase (or in foo.example.com/PascalCase) code to represent the type of condition. | N/A |
| └>&nbsp;&nbsp; **issuer** | `object` | Issuer: Token Issuer profile | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **audiences** | `array` | Audiences: This configures the acceptable audiences the JWT token, issued by the identity provider, must be issued to. At least one of the entries must match the 'aud' claim in the JWT token. audiences must contain at least one entry and must not exceed ten entries. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ca** | `string` | Ca: The issuer of the token Certificate bundle to use to validate server certificates for the configured URL. It must be PEM encoded and when not specified, the system trust is used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **url** | `string` | Url: This configures the URL used to issue tokens by the identity provider. The Kubernetes API server determines how authentication tokens should be handled by matching the 'iss' claim in the JWT to the issuerURL of configured identity providers. issuerURL must use the 'https' scheme. | N/A |
| └>&nbsp;&nbsp; **provisioningState** | `string` | ProvisioningState: Provisioning state | N/A |
|  **systemData** | `object` | SystemData: Azure Resource Manager metadata containing createdBy and modifiedBy information. | N/A |
| └>&nbsp;&nbsp; **createdAt** | `string` | CreatedAt: The timestamp of resource creation (UTC). | N/A |
| └>&nbsp;&nbsp; **createdBy** | `string` | CreatedBy: The identity that created the resource. | N/A |
| └>&nbsp;&nbsp; **createdByType** | `string` | CreatedByType: The type of identity that created the resource. | N/A |
| └>&nbsp;&nbsp; **lastModifiedAt** | `string` | LastModifiedAt: The timestamp of resource last modification (UTC) | N/A |
| └>&nbsp;&nbsp; **lastModifiedBy** | `string` | LastModifiedBy: The identity that last modified the resource. | N/A |
| └>&nbsp;&nbsp; **lastModifiedByType** | `string` | LastModifiedByType: The type of identity that last modified the resource. | N/A |
|  **type** | `string` | Type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" | N/A |
