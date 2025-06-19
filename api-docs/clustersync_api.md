# ClusterSync API

ClusterSyncStatus defines the observed state of ClusterSync

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions is a list of conditions associated with syncing to the cluster. | N/A |
| └>&nbsp;&nbsp; **lastProbeTime** | `string` | LastProbeTime is the last time we probed the condition. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the last time the condition transitioned from one status to another. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message is a human-readable message indicating details about the last transition. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason is a unique, one-word, CamelCase reason for the condition's last transition. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status is the status of the condition. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type is the type of the condition. | N/A |
|  **controlledByReplica** | `integer` | ControlledByReplica indicates which replica of the hive-clustersync StatefulSet is responsible for (the CD related to) this clustersync. Note that this value indicates the replica that most recently handled the ClusterSync. If the hive-clustersync statefulset is scaled up or down, the controlling replica can change, potentially causing logs to be spread across multiple pods. | N/A |
|  **firstSuccessTime** | `string` | FirstSuccessTime is the time we first successfully applied all (selector)syncsets to a cluster. | N/A |
|  **selectorSyncSets** | `array` | SelectorSyncSets is the sync status of all of the SelectorSyncSets for the cluster. | N/A |
| └>&nbsp;&nbsp; **failureMessage** | `string` | FailureMessage is a message describing why the SyncSet or SelectorSyncSet could not be applied. This is only set when Result is Failure. | N/A |
| └>&nbsp;&nbsp; **firstSuccessTime** | `string` | FirstSuccessTime is the time when the SyncSet or SelectorSyncSet was first successfully applied to the cluster. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the time when this status last changed. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the SyncSet or SelectorSyncSet. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | ObservedGeneration is the generation of the SyncSet or SelectorSyncSet that was last observed. | N/A |
| └>&nbsp;&nbsp; **resourcesToDelete** | `array` | ResourcesToDelete is the list of resources in the cluster that should be deleted when the SyncSet or SelectorSyncSet is deleted or is no longer matched to the cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiVersion** | `string` | APIVersion is the Group and Version of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace is the namespace of the resource. | N/A |
| └>&nbsp;&nbsp; **result** | `string` | Result is the result of the last attempt to apply the SyncSet or SelectorSyncSet to the cluster. | N/A |
|  **syncSets** | `array` | SyncSets is the sync status of all of the SyncSets for the cluster. | N/A |
| └>&nbsp;&nbsp; **failureMessage** | `string` | FailureMessage is a message describing why the SyncSet or SelectorSyncSet could not be applied. This is only set when Result is Failure. | N/A |
| └>&nbsp;&nbsp; **firstSuccessTime** | `string` | FirstSuccessTime is the time when the SyncSet or SelectorSyncSet was first successfully applied to the cluster. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the time when this status last changed. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the SyncSet or SelectorSyncSet. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | ObservedGeneration is the generation of the SyncSet or SelectorSyncSet that was last observed. | N/A |
| └>&nbsp;&nbsp; **resourcesToDelete** | `array` | ResourcesToDelete is the list of resources in the cluster that should be deleted when the SyncSet or SelectorSyncSet is deleted or is no longer matched to the cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiVersion** | `string` | APIVersion is the Group and Version of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace is the namespace of the resource. | N/A |
| └>&nbsp;&nbsp; **result** | `string` | Result is the result of the last attempt to apply the SyncSet or SelectorSyncSet to the cluster. | N/A |
