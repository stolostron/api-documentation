# AzureClusterIdentity API

AzureClusterIdentity is the Schema for the azureclustersidentities API.

## Spec Fields

AzureClusterIdentitySpec defines the parameters that are used to create an AzureIdentity.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **allowedNamespaces** | `object` | AllowedNamespaces is used to identify the namespaces the clusters are allowed to use the identity from. Namespaces can be selected either using an array of namespaces or with label selector. An empty allowedNamespaces object indicates that AzureClusters can use this identity from any namespace. If this object is nil, no namespaces will be allowed (default behaviour, if this field is not provided) A namespace should be either in the NamespaceList or match with Selector to use the identity. | N/A |
| └>&nbsp;&nbsp; **list** | `array` | A nil or empty list indicates that AzureCluster cannot use the identity from any namespace. | N/A |
| └>&nbsp;&nbsp; **selector** | `object` | Selector is a selector of namespaces that AzureCluster can use this Identity from. This is a standard Kubernetes LabelSelector, a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. A nil or empty selector indicates that AzureCluster cannot use this AzureClusterIdentity from any namespace. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
|  **certPath** | `string` | CertPath is the path where certificates exist. When set, it takes precedence over ClientSecret for types that use certs like ServicePrincipalCertificate. | N/A |
|  **clientID** | `string` | ClientID is the service principal client ID. Both User Assigned MSI and SP can use this field. | N/A |
|  **clientSecret** | `object` | ClientSecret is a secret reference which should contain either a Service Principal password or certificate secret. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | name is unique within a namespace to reference a secret resource. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | namespace defines the space within which the secret name must be unique. | N/A |
|  **resourceID** | `string` | ResourceID is the Azure resource ID for the User Assigned MSI resource. Only applicable when type is UserAssignedMSI. Deprecated: This field no longer has any effect. | N/A |
|  **tenantID** | `string` | TenantID is the service principal primary tenant id. | N/A |
|  **type** | `string` | Type is the type of Azure Identity used. ServicePrincipal, ServicePrincipalCertificate, UserAssignedMSI, ManualServicePrincipal, UserAssignedIdentityCredential, or WorkloadIdentity. | N/A |
|  **userAssignedIdentityCredentialsCloudType** | `string` | UserAssignedIdentityCredentialsCloudType is used with UserAssignedIdentityCredentialsPath to specify the Cloud type. Can only be one of the following values: public, china, or usgovernment If a value is not specified, defaults to public | N/A |
|  **userAssignedIdentityCredentialsPath** | `string` | UserAssignedIdentityCredentialsPath is the path where an existing JSON file exists containing the JSON format of a UserAssignedIdentityCredentials struct. See the msi-dataplane for more details on UserAssignedIdentityCredentials - https://github.com/Azure/msi-dataplane/blob/main/pkg/dataplane/internal/client/models.go#L125 | N/A |
## Status Fields

AzureClusterIdentityStatus defines the observed state of AzureClusterIdentity.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions defines current service state of the AzureClusterIdentity. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | reason is the reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
