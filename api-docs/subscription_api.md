# Subscription API

## Spec Fields

SubscriptionSpec defines the desired state of Subscription

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **allow** | `array` | Specify a list of resources allowed for deployment | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | APIVersion specifies the API version for the group of resources | N/A |
| └>&nbsp;&nbsp; **kinds** | `array` | Kinds specifies a list of kinds under the same API version for the group of resources | N/A |
|  **channel** | `string` | The primary channel namespaced name used by the subscription. Its format is "<channel NameSpace>/<channel Name>" | N/A |
|  **deny** | `array` | Specify a list of resources denied for deployment | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | APIVersion specifies the API version for the group of resources | N/A |
| └>&nbsp;&nbsp; **kinds** | `array` | Kinds specifies a list of kinds under the same API version for the group of resources | N/A |
|  **hooksecretref** | `object` | Specify a secret reference used in Ansible job integration authentication | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| └>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. TODO: this design is not final and this field is subject to change in the future. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| └>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
|  **name** | `string` | Subscribe a package by its package name | N/A |
|  **overrides** | `array` | Specify overrides when applied to clusters. Hub use only | N/A |
| └>&nbsp;&nbsp; **clusterName** | `string` | Cluster name | N/A |
| └>&nbsp;&nbsp; **clusterOverrides** | `array` | ClusterOverrides defines a list of content for override | N/A |
|  **packageFilter** | `object` | Subscribe packages by a package filter | N/A |
| └>&nbsp;&nbsp; **annotations** | `object` | Annotations defines a type of filter for selecting resources by annotations | N/A |
| └>&nbsp;&nbsp; **filterRef** | `object` | FilterRef defines a type of filter for selecting resources by another resource reference | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid? | N/A |
| └>&nbsp;&nbsp; **labelSelector** | `object` | LabelSelector defines a type of filter for selecting resources by label selector | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
| └>&nbsp;&nbsp; **version** | `string` | Version defines a type of filter for selecting resources by version | N/A |
|  **packageOverrides** | `array` | Override packages | N/A |
| └>&nbsp;&nbsp; **packageAlias** | `string` | PackageAlias defines the alias of the package name that will be onverriden | N/A |
| └>&nbsp;&nbsp; **packageName** | `string` | PackageName defines the package name that will be onverriden | N/A |
| └>&nbsp;&nbsp; **packageOverrides** | `array` | PackageOverrides defines a list of content for override | N/A |
|  **placement** | `object` | Specify a placement reference for selecting clusters. Hub use only | N/A |
| └>&nbsp;&nbsp; **clusterSelector** | `object` | A label selector is a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. An empty label selector matches all objects. A null label selector matches no objects. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
| └>&nbsp;&nbsp; **clusters** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **local** | `boolean` | It indicates a standalone subscription if the Local pointer is set to be true | N/A |
| └>&nbsp;&nbsp; **placementRef** | `object` | Specify a placement reference for selecting clusters | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. TODO: this design is not final and this field is subject to change in the future. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
|  **secondaryChannel** | `string` | The secondary channel will be applied if the primary channel fails to connect | N/A |
|  **timewindow** | `object` | Specify a time window to indicate when the subscription is handled | N/A |
| └>&nbsp;&nbsp; **daysofweek** | `array` | A list of days of a week, valid values include: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday | N/A |
| └>&nbsp;&nbsp; **hours** | `array` | A list of hour ranges | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **end** | `string` | End time of the hour range | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **start** | `string` | Start time of the hour range | N/A |
| └>&nbsp;&nbsp; **location** | `string` | time zone location, refer to TZ identifier in https://en.wikipedia.org/wiki/List_of_tz_database_time_zones | N/A |
| └>&nbsp;&nbsp; **windowtype** | `string` | Activiate time window or not. The subscription deployment will only be handled during these active windows Valid values include: active,blocked,Active,Blocked | N/A |
|  **watchHelmNamespaceScopedResources** | `boolean` | WatchHelmNamespaceScopedResources is used to enable watching namespace scope Helm chart resources | N/A |
## Status Fields

SubscriptionStatus defines the observed status of a subscription

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **ansiblejobs** | `object` | AnsibleJobsStatus defines status of ansible jobs propagated by the subscription | N/A |
| └>&nbsp;&nbsp; **lastposthookjob** | `string` | The lastly propagated posthook job | N/A |
| └>&nbsp;&nbsp; **lastprehookjob** | `string` | The lastly propagated prehook job | N/A |
| └>&nbsp;&nbsp; **posthookjobshistory** | `array` | reserved for backward compatibility | N/A |
| └>&nbsp;&nbsp; **prehookjobshistory** | `array` | reserved for backward compatibility | N/A |
|  **appstatusReference** | `string` | The CLI reference for getting the subscription status output | N/A |
|  **lastUpdateTime** | `string` | Timestamp of when the subscription status was last updated. | N/A |
|  **message** | `string` | Informational message of the subscription deployment | N/A |
|  **phase** | `string` | Phase of the subscription deployment | N/A |
|  **reason** | `string` | additional error output of the subscription deployment | N/A |
|  **statuses** | `object` | SubscriptionClusterStatusMap defines status of each subscription per cluster, key is cluster name | N/A |
