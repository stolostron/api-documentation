# Restore API

Restore is an ACM resource that you can use to restore resources from a cluster backup to a target cluster.
The restore resource has properties that you can use to restore only passive data or to restore managed cluster
activation resources.
Additionally, it has a property that you can use to periodically check for new backups and automatically restore
them on the target cluster.

## Spec Fields

RestoreSpec defines the desired state of Restore

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **cleanupBeforeRestore** | `string` | 1. Use CleanupRestored if you want to delete all resources created by a previous restore operation, before restoring the new data 2. Use None if you don't want to clean up any resources before restoring the new data. | N/A |
|  **excludedNamespaces** | `array` | velero option - ExcludedNamespaces contains a list of namespaces that are not included in the restore. | N/A |
|  **excludedResources** | `array` | velero option - ExcludedResources is a slice of resource names that are not included in the restore. | N/A |
|  **hooks** | `object` | velero option -  Hooks represent custom behaviors that should be executed during or post restore. | N/A |
| └>&nbsp;&nbsp; **resources** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **excludedNamespaces** | `array` | ExcludedNamespaces specifies the namespaces to which this hook spec does not apply. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **excludedResources** | `array` | ExcludedResources specifies the resources to which this hook spec does not apply. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **includedNamespaces** | `array` | IncludedNamespaces specifies the namespaces to which this hook spec applies. If empty, it applies to all namespaces. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **includedResources** | `array` | IncludedResources specifies the resources to which this hook spec applies. If empty, it applies to all resources. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **labelSelector** | `object` | LabelSelector, if specified, filters the resources to which this hook spec applies. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of this hook. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **postHooks** | `array` | PostHooks is a list of RestoreResourceHooks to execute during and after restoring a resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **exec** | `object` | Exec defines an exec restore hook. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **command** | `array` | Command is the command and arguments to execute from within a container after a pod has been restored. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **container** | `string` | Container is the container in the pod where the command should be executed. If not specified, the pod's first container is used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **execTimeout** | `string` | ExecTimeout defines the maximum amount of time Velero should wait for the hook to complete before considering the execution a failure. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **onError** | `string` | OnError specifies how Velero should behave if it encounters an error executing this hook. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **waitForReady** | `boolean` | WaitForReady ensures command will be launched when container is Ready instead of Running. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **waitTimeout** | `string` | WaitTimeout defines the maximum amount of time Velero should wait for the container to be Ready before attempting to run the command. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **init** | `object` | Init defines an init restore hook. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **initContainers** | `array` | InitContainers is list of init containers to be added to a pod during its restore. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **timeout** | `string` | Timeout defines the maximum amount of time Velero should wait for the initContainers to complete. | N/A |
|  **includedNamespaces** | `array` | velero option - IncludedNamespaces is a slice of namespace names to include objects from. If empty, all namespaces are included. | N/A |
|  **includedResources** | `array` | velero option - IncludedResources is a slice of resource names to include in the restore. If empty, all resources in the backup are included. | N/A |
|  **labelSelector** | `object` | velero option - LabelSelector is a metav1.LabelSelector to filter with when restoring individual objects from the backup. If empty or nil, all objects are included. Optional. | N/A |
| └>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| └>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
|  **namespaceMapping** | `object` | velero option - NamespaceMapping is a map of source namespace names to target namespace names to restore into. Any source namespaces not included in the map will be restored into namespaces of the same name. | N/A |
|  **orLabelSelectors** | `array` | velero option - OrLabelSelectors is list of metav1.LabelSelector to filter with when restoring individual objects from the backup. If multiple provided they will be joined by the OR operator. LabelSelector as well as OrLabelSelectors cannot co-exist in restore request, only one of them can be used | N/A |
| └>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| └>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
|  **preserveNodePorts** | `boolean` | velero option - PreserveNodePorts specifies whether to restore old nodePorts from backup. | N/A |
|  **restorePVs** | `boolean` | velero option -  RestorePVs specifies whether to restore all included PVs from snapshot (via the cloudprovider). | N/A |
|  **restoreStatus** | `object` | velero option -  RestoreStatus specifies which resources we should restore the status field. If nil, no objects are included. Optional. | N/A |
| └>&nbsp;&nbsp; **excludedResources** | `array` | ExcludedResources specifies the resources to which will not restore the status. | N/A |
| └>&nbsp;&nbsp; **includedResources** | `array` | IncludedResources specifies the resources to which will restore the status. If empty, it applies to all resources. | N/A |
|  **restoreSyncInterval** | `string` | Used in combination with the SyncRestoreWithNewBackups property When SyncRestoreWithNewBackups is set to true, defines the duration for checking on new backups If not defined and SyncRestoreWithNewBackups is set to true, it defaults to 30minutes | N/A |
|  **syncRestoreWithNewBackups** | `boolean` | Set this to true if you want to keep checking for new backups and restore if updates are available. If not defined, the value is set to false. For this option to work, you need to set VeleroResourcesBackupName and VeleroCredentialsBackupName to latest and VeleroManagedClustersBackupName to skip | N/A |
|  **veleroCredentialsBackupName** | `string` | VeleroCredentialsBackupName is the name of the velero back-up used to restore credentials. Is required, valid values are latest, skip or backup_name If value is set to latest, the latest backup is used, skip will not restore this type of backup backup_name points to the name of the backup to be restored | N/A |
|  **veleroManagedClustersBackupName** | `string` | VeleroManagedClustersBackupName is the name of the velero back-up used to restore managed clusters. Is required, valid values are latest, skip or backup_name If value is set to latest, the latest backup is used, skip will not restore this type of backup backup_name points to the name of the backup to be restored | N/A |
|  **veleroResourcesBackupName** | `string` | VeleroResourcesBackupName is the name of the velero back-up used to restore resources. Is required, valid values are latest, skip or backup_name If value is set to latest, the latest backup is used, skip will not restore this type of backup backup_name points to the name of the backup to be restored | N/A |
## Status Fields

RestoreStatus defines the observed state of Restore

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **completionTimestamp** | `string` | CompletionTimestamp records the time the restore operation was completed. | N/A |
|  **lastMessage** | `string` | Message on the last operation | N/A |
|  **messages** | `array` | Messages contains any messages that were encountered during the restore process. | N/A |
|  **phase** | `string` | Phase is the current phase of the restore | N/A |
|  **veleroCredentialsRestoreName** | `string` | No description provided. | N/A |
|  **veleroGenericResourcesRestoreName** | `string` | No description provided. | N/A |
|  **veleroManagedClustersRestoreName** | `string` | No description provided. | N/A |
|  **veleroResourcesRestoreName** | `string` | No description provided. | N/A |
