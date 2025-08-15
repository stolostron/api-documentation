# ClusterClaim API

## Spec Fields

ClusterClaimSpec defines the desired state of the ClusterClaim.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **clusterPoolName** | `string` | ClusterPoolName is the name of the cluster pool from which to claim a cluster. | N/A |
|  **lifetime** | `string` | Lifetime is the maximum lifetime of the claim after it is assigned a cluster. If the claim still exists when the lifetime has elapsed, the claim will be deleted by Hive. This is a Duration value; see https://pkg.go.dev/time#ParseDuration for accepted formats. Note: due to discrepancies in validation vs parsing, we use a Pattern instead of `Format=duration`. See https://bugzilla.redhat.com/show_bug.cgi?id=2050332 https://github.com/kubernetes/apimachinery/issues/131 https://github.com/kubernetes/apiextensions-apiserver/issues/56 | `Pattern=^([0-9]+(\.[0-9]+)?(ns\|us\|µs\|ms\|s\|m\|h))+$` |
|  **namespace** | `string` | Namespace is the namespace containing the ClusterDeployment (name will match the namespace) of the claimed cluster. This field will be set as soon as a suitable cluster can be found, however that cluster may still be resuming and not yet ready for use. Wait for the ClusterRunning condition to be true to avoid this issue. | N/A |
|  **subjects** | `array` | Subjects hold references to which to authorize access to the claimed cluster. | N/A |
| └>&nbsp;&nbsp; **apiGroup** | `string` | APIGroup holds the API group of the referenced subject. Defaults to "" for ServiceAccount subjects. Defaults to "rbac.authorization.k8s.io" for User and Group subjects. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of object being referenced. Values defined by this API group are "User", "Group", and "ServiceAccount". If the Authorizer does not recognized the kind value, the Authorizer should report an error. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the object being referenced. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referenced object.  If the object kind is non-namespace, such as "User" or "Group", and this value is not empty the Authorizer should report an error. | N/A |
## Status Fields

ClusterClaimStatus defines the observed state of ClusterClaim.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions includes more detailed status for the cluster pool. | N/A |
| └>&nbsp;&nbsp; **lastProbeTime** | `string` | LastProbeTime is the last time we probed the condition. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the last time the condition transitioned from one status to another. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message is a human-readable message indicating details about last transition. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason is a unique, one-word, CamelCase reason for the condition's last transition. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status is the status of the condition. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type is the type of the condition. | N/A |
|  **lifetime** | `string` | Lifetime is the maximum lifetime of the claim after it is assigned a cluster. If the claim still exists when the lifetime has elapsed, the claim will be deleted by Hive. | N/A |
