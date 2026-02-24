# ClusterResourceSet API

ClusterResourceSet is the Schema for the clusterresourcesets API.
Deprecated: This type will be removed in one of the next releases.

## Spec Fields

spec is the desired state of ClusterResourceSet.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **clusterSelector** | `object` | clusterSelector is the label selector for Clusters. The Clusters that are selected by this will be the ones affected by this ClusterResourceSet. It must match the Cluster labels. This field is immutable. | N/A |
| └>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| └>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
|  **resources** | `array` | resources is a list of Secrets/ConfigMaps where each contains 1 or more resources to be applied to remote clusters. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | kind of the resource. Supported kinds are: Secrets and ConfigMaps. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | name of the resource that is in the same namespace with ClusterResourceSet object. | N/A |
|  **strategy** | `string` | strategy is the strategy to be used during applying resources. Defaults to ApplyOnce. This field is immutable. | N/A |
## Status Fields

status is the observed state of ClusterResourceSet.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | conditions defines current state of the ClusterResourceSet. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | reason is the reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may not be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **observedGeneration** | `integer` | observedGeneration reflects the generation of the most recently observed ClusterResourceSet. | N/A |
