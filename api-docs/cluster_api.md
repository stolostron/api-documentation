# Cluster API

## Spec Fields

spec is the desired state of Cluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **clusterNetwork** | `object` | clusterNetwork is the cluster network configuration. | N/A |
| └>&nbsp;&nbsp; **apiServerPort** | `integer` | apiServerPort specifies the port the API Server should bind to. Defaults to 6443. | N/A |
| └>&nbsp;&nbsp; **pods** | `object` | pods is the network ranges from which Pod networks are allocated. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cidrBlocks** | `array` | cidrBlocks is a list of CIDR blocks. | N/A |
| └>&nbsp;&nbsp; **serviceDomain** | `string` | serviceDomain is the domain name for services. | N/A |
| └>&nbsp;&nbsp; **services** | `object` | services is the network ranges from which service VIPs are allocated. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cidrBlocks** | `array` | cidrBlocks is a list of CIDR blocks. | N/A |
|  **controlPlaneEndpoint** | `object` | controlPlaneEndpoint represents the endpoint used to communicate with the control plane. | N/A |
| └>&nbsp;&nbsp; **host** | `string` | host is the hostname on which the API server is serving. | N/A |
| └>&nbsp;&nbsp; **port** | `integer` | port is the port on which the API server is serving. | N/A |
|  **controlPlaneRef** | `object` | controlPlaneRef is an optional reference to a provider-specific resource that holds the details for provisioning the Control Plane for a Cluster. | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| └>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| └>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
|  **infrastructureRef** | `object` | infrastructureRef is a reference to a provider-specific resource that holds the details for provisioning infrastructure for a cluster in said provider. | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| └>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| └>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
|  **paused** | `boolean` | paused can be used to prevent controllers from processing the Cluster and all its associated objects. | N/A |
## Status Fields

status is the observed state of Cluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | conditions defines current service state of the cluster. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | reason is the reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may not be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **controlPlaneInitialized** | `boolean` | controlPlaneInitialized defines if the control plane has been initialized. | N/A |
|  **controlPlaneReady** | `boolean` | controlPlaneReady defines if the control plane is ready. | N/A |
|  **failureDomains** | `object` | failureDomains is a slice of failure domain objects synced from the infrastructure provider. | N/A |
|  **failureMessage** | `string` | failureMessage indicates that there is a fatal problem reconciling the state, and will be set to a descriptive error message. | N/A |
|  **failureReason** | `string` | failureReason indicates that there is a fatal problem reconciling the state, and will be set to a token value suitable for programmatic interpretation. | N/A |
|  **infrastructureReady** | `boolean` | infrastructureReady is the state of the infrastructure provider. | N/A |
|  **observedGeneration** | `integer` | observedGeneration is the latest generation observed by the controller. | N/A |
|  **phase** | `string` | phase represents the current phase of cluster actuation. E.g. Pending, Running, Terminating, Failed etc. | N/A |
