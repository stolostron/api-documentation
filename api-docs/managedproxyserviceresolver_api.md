# ManagedProxyServiceResolver API

ManagedProxyServiceResolverStatus defines the observed state of ManagedProxyServiceResolver.

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **managedClusterSelector** | `object` | ManagedClusterSelector selects a set of managed clusters. | N/A |
| └>&nbsp;&nbsp; **managedClusterSet** | `object` | ManagedClusterSet defines a set of managed clusters that need to expose the service. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the managed cluster set. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type represents the type of the selector. Now only ManagedClusterSet is supported. | N/A |
|  **serviceSelector** | `object` | ServiceSelector selects a service. | N/A |
| └>&nbsp;&nbsp; **serviceRef** | `object` | ServiceRef defines a service in a namespace. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name represents the name of the service. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace represents the namespace of the service. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type represents the type of the selector. Now only ServiceRef type is supported. | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions contains the different condition statuses for this ManagedProxyServiceResolver. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt) | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
