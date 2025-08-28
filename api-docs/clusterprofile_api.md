# ClusterProfile API

ClusterProfile represents a single cluster in a multi-cluster deployment.

## Spec Fields

ClusterProfileSpec defines the desired state of ClusterProfile.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **clusterManager** | `object` | ClusterManager defines which cluster manager owns this ClusterProfile resource | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name defines the name of the cluster manager | N/A |
|  **displayName** | `string` | DisplayName defines a human-readable name of the ClusterProfile | N/A |
## Status Fields

ClusterProfileStatus defines the observed state of ClusterProfile.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions contains the different condition statuses for this cluster. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt) | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **properties** | `array` | Properties defines name/value pairs to represent properties of a cluster. It could be a collection of ClusterProperty (KEP-2149) resources, but could also be info based on other implementations. The names of the properties can be predefined names from ClusterProperty resources and is allowed to be customized by different cluster managers. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of a property resource on cluster. It's a well-known or customized name to identify the property. | N/A |
| └>&nbsp;&nbsp; **value** | `string` | Value is a property-dependent string | N/A |
|  **version** | `object` | Version defines the version information of the cluster. | N/A |
| └>&nbsp;&nbsp; **kubernetes** | `string` | Kubernetes is the kubernetes version of the cluster. | N/A |
