# AWSClusterRoleIdentity API

Spec for this AWSClusterRoleIdentity.

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **allowedNamespaces** | `object` | AllowedNamespaces is used to identify which namespaces are allowed to use the identity from. Namespaces can be selected either using an array of namespaces or with label selector. An empty allowedNamespaces object indicates that AWSClusters can use this identity from any namespace. If this object is nil, no namespaces will be allowed (default behaviour, if this field is not provided) A namespace should be either in the NamespaceList or match with Selector to use the identity. | N/A |
| └>&nbsp;&nbsp; **list** | `array` | An nil or empty list indicates that AWSClusters cannot use the identity from any namespace. | N/A |
| └>&nbsp;&nbsp; **selector** | `object` | An empty selector indicates that AWSClusters cannot use this AWSClusterIdentity from any namespace. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
|  **durationSeconds** | `integer` | The duration, in seconds, of the role session before it is renewed. | `Minimum=900`<br>`Maximum=43200` |
|  **externalID** | `string` | A unique identifier that might be required when you assume a role in another account. If the administrator of the account to which the role belongs provided you with an external ID, then provide that value in the ExternalId parameter. This value can be any string, such as a passphrase or account number. A cross-account role is usually set up to trust everyone in an account. Therefore, the administrator of the trusting account might send an external ID to the administrator of the trusted account. That way, only someone with the ID can assume the role, rather than everyone in the account. For more information about the external ID, see How to Use an External ID When Granting Access to Your AWS Resources to a Third Party in the IAM User Guide. | N/A |
|  **inlinePolicy** | `string` | An IAM policy as a JSON-encoded string that you want to use as an inline session policy. | N/A |
|  **policyARNs** | `array` | The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. The policies must exist in the same account as the role. | N/A |
|  **roleARN** | `string` | The Amazon Resource Name (ARN) of the role to assume. | N/A |
|  **sessionName** | `string` | An identifier for the assumed role session | N/A |
|  **sourceIdentityRef** | `object` | SourceIdentityRef is a reference to another identity which will be chained to do role assumption. All identity types are accepted. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the identity. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the identity. | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
