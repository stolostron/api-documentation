# ClusterPermission API

ClusterPermissionStatus defines the observed state of ClusterPermission

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **clusterRole** | `object` | ClusterRole represents the ClusterRole that is being created on the managed cluster | N/A |
| └>&nbsp;&nbsp; **rules** | `array` | Rules holds all the PolicyRules for this ClusterRole | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiGroups** | `array` | APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. "" represents the core API group and "*" represents all API groups. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **nonResourceURLs** | `array` | NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"),  but not both. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceNames** | `array` | ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resources** | `array` | Resources is a list of resources this rule applies to. '*' represents all resources. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **verbs** | `array` | Verbs is a list of Verbs that apply to ALL the ResourceKinds contained in this rule. '*' represents all verbs. | N/A |
|  **clusterRoleBinding** | `object` | ClusterRoleBinding represents the ClusterRoleBinding that is being created on the managed cluster | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the ClusterRoleBinding if a name different than the ClusterPermission name is used | N/A |
| └>&nbsp;&nbsp; **roleRef** | `object` | RoleRef contains information that points to the ClusterRole being used | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiGroup** | `string` | APIGroup is the group for the resource being referenced | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the type of resource being referenced | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of resource being referenced | N/A |
| └>&nbsp;&nbsp; **subject** | `object` | Subject contains a reference to the object or user identities a ClusterPermission binding applies to. Besides the typical subject for a binding, a ManagedServiceAccount can be used as a subject as well. If both subject and subjects exist then only subjects will be used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiGroup** | `string` | APIGroup holds the API group of the referenced subject. Defaults to "" for ServiceAccount subjects. Defaults to "rbac.authorization.k8s.io" for User and Group subjects. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind of object being referenced. Values defined by this API group are "User", "Group", and "ServiceAccount". If the Authorizer does not recognized the kind value, the Authorizer should report an error. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the object being referenced. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referenced object.  If the object kind is non-namespace, such as "User" or "Group", and this value is not empty the Authorizer should report an error. | N/A |
| └>&nbsp;&nbsp; **subjects** | `array` | Subjects contains an array of references to objects or user identities a ClusterPermission binding applies to. Besides the typical subject for a binding, a ManagedServiceAccount can be used as a subject as well. If both subject and subjects exist then only subjects will be used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiGroup** | `string` | APIGroup holds the API group of the referenced subject. Defaults to "" for ServiceAccount subjects. Defaults to "rbac.authorization.k8s.io" for User and Group subjects. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind of object being referenced. Values defined by this API group are "User", "Group", and "ServiceAccount". If the Authorizer does not recognized the kind value, the Authorizer should report an error. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the object being referenced. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referenced object.  If the object kind is non-namespace, such as "User" or "Group", and this value is not empty the Authorizer should report an error. | N/A |
|  **roleBindings** | `array` | RoleBindings represents RoleBindings that are being created on the managed cluster | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the RoleBinding if a name different than the ClusterPermission name is used | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the Role for that is being created on the managed cluster | N/A |
| └>&nbsp;&nbsp; **namespaceSelector** | `object` | NamespaceSelector define the general labelSelector which namespace to apply the rules to Note: the namespace must exists on the hub cluster | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
| └>&nbsp;&nbsp; **roleRef** | `object` | RoleRef contains information that points to the role being used | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiGroup** | `string` | APIGroup is the group for the resource being referenced | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the type of resource being referenced | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of resource being referenced | N/A |
| └>&nbsp;&nbsp; **subject** | `object` | Subject contains a reference to the object or user identities a ClusterPermission binding applies to. Besides the typical subject for a binding, a ManagedServiceAccount can be used as a subject as well. If both subject and subjects exist then only subjects will be used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiGroup** | `string` | APIGroup holds the API group of the referenced subject. Defaults to "" for ServiceAccount subjects. Defaults to "rbac.authorization.k8s.io" for User and Group subjects. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind of object being referenced. Values defined by this API group are "User", "Group", and "ServiceAccount". If the Authorizer does not recognized the kind value, the Authorizer should report an error. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the object being referenced. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referenced object.  If the object kind is non-namespace, such as "User" or "Group", and this value is not empty the Authorizer should report an error. | N/A |
| └>&nbsp;&nbsp; **subjects** | `array` | Subjects contains an array of references to objects or user identities a ClusterPermission binding applies to. Besides the typical subject for a binding, a ManagedServiceAccount can be used as a subject as well. If both subject and subjects exist then only subjects will be used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiGroup** | `string` | APIGroup holds the API group of the referenced subject. Defaults to "" for ServiceAccount subjects. Defaults to "rbac.authorization.k8s.io" for User and Group subjects. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind of object being referenced. Values defined by this API group are "User", "Group", and "ServiceAccount". If the Authorizer does not recognized the kind value, the Authorizer should report an error. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the object being referenced. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referenced object.  If the object kind is non-namespace, such as "User" or "Group", and this value is not empty the Authorizer should report an error. | N/A |
|  **roles** | `array` | Roles represents roles that are being created on the managed cluster | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the Role for that is being created on the managed cluster | N/A |
| └>&nbsp;&nbsp; **namespaceSelector** | `object` | NamespaceSelector define the general labelSelector which namespace to apply the rules to Note: the namespace must exists on the hub cluster | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
| └>&nbsp;&nbsp; **rules** | `array` | Rules holds all the PolicyRules for this Role | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiGroups** | `array` | APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. "" represents the core API group and "*" represents all API groups. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **nonResourceURLs** | `array` | NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"),  but not both. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceNames** | `array` | ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resources** | `array` | Resources is a list of resources this rule applies to. '*' represents all resources. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **verbs** | `array` | Verbs is a list of Verbs that apply to ALL the ResourceKinds contained in this rule. '*' represents all verbs. | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions is the condition list. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
