# ClusterRelocate API

ClusterRelocate is the Schema for the ClusterRelocates API

## Spec Fields

ClusterRelocateSpec defines the relocation of clusters from one Hive instance to another.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **clusterDeploymentSelector** | `object` | ClusterDeploymentSelector is a LabelSelector indicating which clusters will be relocated. | N/A |
| └>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| └>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
|  **kubeconfigSecretRef** | `object` | KubeconfigSecretRef is a reference to the secret containing the kubeconfig for the destination Hive instance. The kubeconfig must be in a data field where the key is "kubeconfig". | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the secret. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace is the namespace where the secret lives. | N/A |
## Status Fields

ClusterRelocateStatus defines the observed state of ClusterRelocate.

| Field | Type | Description | Validations |
|:---|---|---|---|
