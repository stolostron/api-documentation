# ClusterState API

## Spec Fields

ClusterStateSpec defines the desired state of ClusterState

| Field | Type | Description | Validations |
|:---|---|---|---|
## Status Fields

ClusterStateStatus defines the observed state of ClusterState

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **clusterOperators** | `array` | ClusterOperators contains the state for every cluster operator in the target cluster | N/A |
| └>&nbsp;&nbsp; **conditions** | `array` | Conditions is the set of conditions in the status of the cluster operator on the target cluster | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the time of the last update to the current status property. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **message** | `string` | message provides additional information about the current condition. This is only to be consumed by humans.  It may contain Line Feed characters (U+000A), which should be rendered as new lines. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **reason** | `string` | reason is the CamelCase reason for the condition's current status. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | type specifies the aspect reported by this condition. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the cluster operator | N/A |
|  **lastUpdated** | `string` | LastUpdated is the last time that operator state was updated | N/A |
