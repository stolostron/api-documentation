# SelectorSyncSet API

SelectorSyncSet is the Schema for the SelectorSyncSet API

## Spec Fields

SelectorSyncSetSpec defines the SyncSetCommonSpec resources and patches to sync along
with a ClusterDeploymentSelector indicating which clusters the SelectorSyncSet applies
to in any namespace.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **applyBehavior** | `string` | ApplyBehavior indicates how resources in this syncset will be applied to the target cluster. The default value of "Apply" indicates that resources should be applied using the 'oc apply' command. If no value is set, "Apply" is assumed. A value of "CreateOnly" indicates that the resource will only be created if it does not already exist in the target cluster. Otherwise, it will be left alone. A value of "CreateOrUpdate" indicates that the resource will be created/updated without the use of the 'oc apply' command, allowing larger resources to be synced, but losing some functionality of the 'oc apply' command such as the ability to remove annotations, labels, and other map entries in general. | N/A |
|  **clusterDeploymentSelector** | `object` | ClusterDeploymentSelector is a LabelSelector indicating which clusters the SelectorSyncSet applies to in any namespace. | N/A |
| └>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| └>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
|  **enablePatchTemplates** | `boolean` | EnablePatchTemplates, if True, causes hive to honor golang text/templates in Patches[].Patch strings. While the standard syntax is supported, it won't do you a whole lot of good as the parser does not pass a data object (i.e. there is no "dot" for you to use). This currently exists to expose a single function:  will be substituted with the string value of ClusterDeployment.Labels["some.label/key"]. The empty string is interpolated if there are no labels, or if the indicated key does not exist. Note that the patch string must be valid JSON after interpolation. This may make for odd-looking quoting in the uninterpolated string. | N/A |
|  **enableResourceTemplates** | `boolean` | EnableResourceTemplates, if True, causes hive to honor golang text/templates in Resources. While the standard syntax is supported, it won't do you a whole lot of good as the parser does not pass a data object (i.e. there is no "dot" for you to use). This currently exists to expose a single function:  will be substituted with the string value of ClusterDeployment.Labels["some.label/key"]. The empty string is interpolated if there are no labels, or if the indicated key does not exist. Note that this only works in values (not e.g. map keys) that are of type string. | N/A |
|  **patches** | `array` | Patches is the list of patches to apply. | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | APIVersion is the Group and Version of the object to be patched. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind is the Kind of the object to be patched. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the object to be patched. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace is the Namespace in which the object to patch exists. Defaults to the SyncSet's Namespace. | N/A |
| └>&nbsp;&nbsp; **patch** | `string` | Patch is the patch to apply. | N/A |
| └>&nbsp;&nbsp; **patchType** | `string` | PatchType indicates the PatchType as "strategic" (default), "json", or "merge". | N/A |
|  **resourceApplyMode** | `string` | ResourceApplyMode indicates if the Resource apply mode is "Upsert" (default) or "Sync". ApplyMode "Upsert" indicates create and update. ApplyMode "Sync" indicates create, update and delete. | N/A |
|  **resources** | `array` | Resources is the list of objects to sync from RawExtension definitions. | N/A |
|  **secretMappings** | `array` | Secrets is the list of secrets to sync along with their respective destinations. | N/A |
| └>&nbsp;&nbsp; **sourceRef** | `object` | SourceRef specifies the name and namespace of a secret on the management cluster | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the secret | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace is the namespace where the secret lives. If not present for the source secret reference, it is assumed to be the same namespace as the syncset with the reference. | N/A |
| └>&nbsp;&nbsp; **targetRef** | `object` | TargetRef specifies the target name and namespace of the secret on the target cluster | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the secret | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace is the namespace where the secret lives. If not present for the source secret reference, it is assumed to be the same namespace as the syncset with the reference. | N/A |
## Status Fields

SelectorSyncSetStatus defines the observed state of a SelectorSyncSet

| Field | Type | Description | Validations |
|:---|---|---|---|
