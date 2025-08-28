# MachineHealthCheck API

MachineHealthCheck is the Schema for the machinehealthchecks API.
Deprecated: This type will be removed in one of the next releases.

## Spec Fields

spec is the specification of machine health check policy

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **clusterName** | `string` | clusterName is the name of the Cluster this object belongs to. | N/A |
|  **maxUnhealthy** | `N/A` | maxUnhealthy specifies the maximum number of unhealthy machines allowed. Any further remediation is only allowed if at most "maxUnhealthy" machines selected by "selector" are not healthy. | N/A |
|  **nodeStartupTimeout** | `string` | nodeStartupTimeout is the duration after which machines without a node will be considered to have failed and will be remediated. | N/A |
|  **remediationTemplate** | `object` | remediationTemplate is a reference to a remediation template provided by an infrastructure provider. This field is completely optional, when filled, the MachineHealthCheck controller creates a new object from the template referenced and hands off remediation of the machine to a controller that lives outside of Cluster API. | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| └>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| └>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
|  **selector** | `object` | selector is the label selector to match machines whose health will be exercised | N/A |
| └>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| └>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
|  **unhealthyConditions** | `array` | unhealthyConditions contains a list of the conditions that determine whether a node is considered unhealthy.  The conditions are combined in a logical OR, i.e. if any of the conditions is met, the node is unhealthy. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **timeout** | `string` | timeout is the duration that a node must be in a given status for, after which the node is considered unhealthy. For example, with a value of "1h", the node must match the status for at least 1 hour before being considered unhealthy. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of Node condition | N/A |
## Status Fields

status is the most recently observed status of MachineHealthCheck resource

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | conditions defines current service state of the MachineHealthCheck. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | reason is the reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may not be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **currentHealthy** | `integer` | currentHealthy is the total number of healthy machines counted by this machine health check | `Minimum=0` |
|  **expectedMachines** | `integer` | expectedMachines is the total number of machines counted by this machine health check | `Minimum=0` |
|  **observedGeneration** | `integer` | observedGeneration is the latest generation observed by the controller. | N/A |
|  **remediationsAllowed** | `integer` | remediationsAllowed is the number of further remediations allowed by this machine health check before maxUnhealthy short circuiting will be applied | `Minimum=0` |
|  **targets** | `array` | targets shows the current list of machines the machine health check is watching | N/A |
