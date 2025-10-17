# MulticlusterRoleAssignment API

MulticlusterRoleAssignment is the Schema for the multiclusterroleassignments API.

## Spec Fields

spec defines the desired state of MulticlusterRoleAssignment

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **roleAssignments** | `array` | RoleAssignments defines the list of role assignments for different roles, namespaces, and cluster sets. | N/A |
| └>&nbsp;&nbsp; **clusterRole** | `string` | ClusterRole defines the cluster role name to be assigned. | N/A |
| └>&nbsp;&nbsp; **clusterSelection** | `object` | ClusterSelection defines the type of cluster selection and the clusters to be selected. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **clusterNames** | `array` | ClusterNames defines the clusters where the role should be applied. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type defines the type of cluster selection. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name defines the name of the role assignment. | N/A |
| └>&nbsp;&nbsp; **targetNamespaces** | `array` | TargetNamespaces defines what namespaces the role should be applied in for all selected clusters in the role assignment. If TargetNamespaces is not present, the role will be applied to all clusters' namespaces. | N/A |
|  **subject** | `object` | Subject defines the user, group, or service account for all role assignments. | N/A |
| └>&nbsp;&nbsp; **apiGroup** | `string` | APIGroup holds the API group of the referenced subject. Defaults to "" for ServiceAccount subjects. Defaults to "rbac.authorization.k8s.io" for User and Group subjects. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of object being referenced. Values defined by this API group are "User", "Group", and "ServiceAccount". If the Authorizer does not recognized the kind value, the Authorizer should report an error. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the object being referenced. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referenced object.  If the object kind is non-namespace, such as "User" or "Group", and this value is not empty the Authorizer should report an error. | N/A |
## Status Fields

status defines the observed state of MulticlusterRoleAssignment

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions is the condition list. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **roleAssignments** | `array` | RoleAssignments provides the status of each role assignment. | N/A |
| └>&nbsp;&nbsp; **createdAt** | `string` | CreatedAt defines the creation time of the roleAssignment. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message provides additional human readable details about the role assignment status. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name defines the name of the role assignment. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason provides a programmatic identifier for the role assignment status. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status defines the current status of the role assignment. | N/A |
