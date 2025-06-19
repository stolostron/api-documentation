# Application API

ApplicationStatus defines controller's the observed state of Application

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **addOwnerRef** | `boolean` | AddOwnerRef objects - flag to indicate if we need to add OwnerRefs to matching objects Matching is done by using Selector to query all ComponentGroupKinds | N/A |
|  **assemblyPhase** | `string` | AssemblyPhase represents the current phase of the application's assembly. An empty value is equivalent to "Succeeded". | N/A |
|  **componentKinds** | `array` | ComponentGroupKinds is a list of Kinds for Application's components (e.g. Deployments, Pods, Services, CRDs). It can be used in conjunction with the Application's Selector to list or watch the Applications components. | N/A |
| └>&nbsp;&nbsp; **group** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | No description provided. | N/A |
|  **descriptor** | `object` | Descriptor regroups information and metadata about an application. | N/A |
| └>&nbsp;&nbsp; **description** | `string` | Description is a brief string description of the Application. | N/A |
| └>&nbsp;&nbsp; **icons** | `array` | Icons is an optional list of icons for an application. Icon information includes the source, size, and mime type. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **size** | `string` | (optional) The size of the image in pixels (e.g., 25x25). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **src** | `string` | The source for image represented as either an absolute URL to the image or a Data URL containing the image. Data URLs are defined in RFC 2397. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | (optional) The mine type of the image (e.g., "image/png"). | N/A |
| └>&nbsp;&nbsp; **keywords** | `array` | Keywords is an optional list of key words associated with the application (e.g. MySQL, RDBMS, database). | N/A |
| └>&nbsp;&nbsp; **links** | `array` | Links are a list of descriptive URLs intended to be used to surface additional documentation, dashboards, etc. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **description** | `string` | Description is human readable content explaining the purpose of the link. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **url** | `string` | Url typically points at a website address. | N/A |
| └>&nbsp;&nbsp; **maintainers** | `array` | Maintainers is an optional list of maintainers of the application. The maintainers in this list maintain the the source code, images, and package for the application. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **email** | `string` | Email is the email address. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the descriptive name. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **url** | `string` | Url could typically be a website address. | N/A |
| └>&nbsp;&nbsp; **notes** | `string` | Notes contain a human readable snippets intended as a quick start for the users of the Application. CommonMark markdown syntax may be used for rich text representation. | N/A |
| └>&nbsp;&nbsp; **owners** | `array` | Owners is an optional list of the owners of the installed application. The owners of the application should be contacted in the event of a planned or unplanned disruption affecting the application. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **email** | `string` | Email is the email address. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the descriptive name. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **url** | `string` | Url could typically be a website address. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type is the type of the application (e.g. WordPress, MySQL, Cassandra). | N/A |
| └>&nbsp;&nbsp; **version** | `string` | Version is an optional version indicator for the Application. | N/A |
|  **info** | `array` | Info contains human readable key,value pairs for the Application. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is a human readable title for this piece of information. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type of the value for this InfoItem. | N/A |
| └>&nbsp;&nbsp; **value** | `string` | Value is human readable content. | N/A |
| └>&nbsp;&nbsp; **valueFrom** | `object` | ValueFrom defines a reference to derive the value from another source. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **configMapKeyRef** | `object` | Selects a key of a ConfigMap. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. TODO: this design is not final and this field is subject to change in the future. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | The key to select. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ingressRef** | `object` | Select an Ingress. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. TODO: this design is not final and this field is subject to change in the future. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **host** | `string` | The optional host to select. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **path** | `string` | The optional HTTP path. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **protocol** | `string` | Protocol for the ingress | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **secretKeyRef** | `object` | Selects a key of a Secret. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. TODO: this design is not final and this field is subject to change in the future. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | The key to select. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serviceRef** | `object` | Select a Service. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. TODO: this design is not final and this field is subject to change in the future. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **path** | `string` | The optional HTTP path. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **port** | `integer` | The optional port to select. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **protocol** | `string` | Protocol for the service | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type of source. | N/A |
|  **selector** | `object` | Selector is a label query over kinds that created by the application. It must match the component objects' labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors | N/A |
| └>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| └>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **components** | `array` | Object status array for all matching objects | N/A |
| └>&nbsp;&nbsp; **group** | `string` | Object group | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of object | N/A |
| └>&nbsp;&nbsp; **link** | `string` | Link to object | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of object | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status. Values: InProgress, Ready, Unknown | N/A |
|  **componentsReady** | `string` | ComponentsReady: status of the components in the format ready/total | N/A |
|  **conditions** | `array` | Conditions represents the latest state of the object | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | Last time the condition transitioned from one status to another. | N/A |
| └>&nbsp;&nbsp; **lastUpdateTime** | `string` | Last time the condition was probed | N/A |
| └>&nbsp;&nbsp; **message** | `string` | A human readable message indicating details about the transition. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | The reason for the condition's last transition. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type of condition. | N/A |
|  **observedGeneration** | `integer` | ObservedGeneration is the most recent generation observed. It corresponds to the Object's generation, which is updated on mutation by the API Server. | N/A |
