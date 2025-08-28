# ManagedClusterSetBinding API

ManagedClusterSetBinding projects a ManagedClusterSet into a certain namespace.
You can create a ManagedClusterSetBinding in a namespace and bind it to a
ManagedClusterSet if both have a RBAC rules to CREATE on the virtual subresource of managedclustersets/bind.
Workloads that you create in the same namespace can only be distributed to ManagedClusters
in ManagedClusterSets that are bound in this namespace by higher-level controllers.

## Spec Fields

Spec defines the attributes of ManagedClusterSetBinding.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **clusterSet** | `string` | ClusterSet is the name of the ManagedClusterSet to bind. It must match the instance name of the ManagedClusterSetBinding and cannot change once created. User is allowed to set this field if they have an RBAC rule to CREATE on the virtual subresource of managedclustersets/bind. | N/A |
## Status Fields

Status represents the current status of the ManagedClusterSetBinding

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions contains the different condition statuses for this ManagedClusterSetBinding. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
