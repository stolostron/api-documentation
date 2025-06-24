# ManagedClusterImageRegistry API

## Spec Fields

Spec defines the information of the ManagedClusterImageRegistry.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **placementRef** | `object` | PlacementRef is the referred Placement name. | N/A |
| └>&nbsp;&nbsp; **group** | `string` | Group is the api group of the placement. Current group is cluster.open-cluster-management.io. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the Placement. | N/A |
| └>&nbsp;&nbsp; **resource** | `string` | Resource is the resource type of the Placement. Current resource is placement or placements. | N/A |
|  **pullSecret** | `object` | PullSecret is the name of image pull secret which should be in the same namespace with the managedClusterImageRegistry. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid? | N/A |
|  **registries** | `array` | Registries includes the mirror and source registries. The source registry will be replaced by the Mirror. The larger index will work if the Sources are the same. | N/A |
| └>&nbsp;&nbsp; **mirror** | `string` | Mirror is the mirrored registry of the Source. Will be ignored if Mirror is empty. | N/A |
| └>&nbsp;&nbsp; **source** | `string` | Source is the source registry. All image registries will be replaced by Mirror if Source is empty. | N/A |
|  **registry** | `string` | Registry is the Mirror registry which will replace all images registries. will be ignored if Registries is not empty. | N/A |
## Status Fields

Status represents the desired status of the managedClusterImageRegistry.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions contains condition information for a managedClusterImageRegistry | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt) | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
