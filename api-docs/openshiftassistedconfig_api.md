# OpenshiftAssistedConfig API

## Spec Fields

OpenshiftAssistedConfigSpec defines the desired state of OpenshiftAssistedConfig

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **additionalNTPSources** | `array` | AdditionalNTPSources is a list of NTP sources (hostname or IP) to be added to all cluster hosts. They are added to any NTP sources that were configured through other means. | N/A |
|  **additionalTrustBundle** | `string` | PEM-encoded X.509 certificate bundle. Hosts discovered by this infra-env will trust the certificates in this bundle. Clusters formed from the hosts discovered by this infra-env will also trust the certificates in this bundle. | N/A |
|  **cpuArchitecture** | `string` | CpuArchitecture specifies the target CPU architecture. Default is x86_64 | N/A |
|  **kernelArguments** | `array` | KernelArguments is the additional kernel arguments to be passed during boot time of the discovery image. Applicable for both iPXE, and ISO streaming from Image Service. | N/A |
| └>&nbsp;&nbsp; **operation** | `string` | Operation is the operation to apply on the kernel argument. | N/A |
| └>&nbsp;&nbsp; **value** | `string` | Value can have the form <parameter> or <parameter>=<value>. The following examples should be supported: rd.net.timeout.carrier=60 isolcpus=1,2,10-20,100-2000:2/25 quiet | `Pattern=^(?:(?:[^ \t\n\r"]+)\|(?:"[^"]*"))+$` |
|  **nmStateConfigLabelSelector** | `object` | NmstateConfigLabelSelector associates NMStateConfigs for hosts that are considered part of this installation environment. | N/A |
| └>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| └>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
|  **nodeRegistration** | `object` | NodeRegistrationOption holds fields related to registering nodes to the cluster | N/A |
| └>&nbsp;&nbsp; **kubeletExtraLabels** | `array` | KubeletExtraLabels passes extra labels to kubelet. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Defaults to the hostname of the node if not provided. | N/A |
|  **osImageVersion** | `string` | OSImageVersion is the version of OS image to use when generating the InfraEnv. The version should refer to an OSImage specified in the AgentServiceConfig (i.e. OSImageVersion should equal to an OpenshiftVersion in OSImages list). Note: OSImageVersion can't be specified along with ClusterRef. | N/A |
|  **proxy** | `object` | Proxy defines the proxy settings for agents and clusters that use the InfraEnv. If unset, the agents and clusters will not be configured to use a proxy. | N/A |
| └>&nbsp;&nbsp; **httpProxy** | `string` | HTTPProxy is the URL of the proxy for HTTP requests. | N/A |
| └>&nbsp;&nbsp; **httpsProxy** | `string` | HTTPSProxy is the URL of the proxy for HTTPS requests. | N/A |
| └>&nbsp;&nbsp; **noProxy** | `string` | NoProxy is a comma-separated list of domains and CIDRs for which the proxy should not be used. | N/A |
|  **pullSecretRef** | `object` | PullSecretRef is the reference to the secret to use when pulling images. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
|  **sshAuthorizedKey** | `string` | SSHAuthorizedKey is a SSH public keys that will be added to all agents for use in debugging. | N/A |
## Status Fields

OpenshiftAssistedConfigStatus defines the observed state of OpenshiftAssistedConfig

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **agentRef** | `object` | AgentRef references the agent this agent bootstrap config has booted | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
|  **conditions** | `array` | Conditions defines current service state of the OpenshiftAssistedConfig. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | Last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | A human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | The reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **dataSecretName** | `string` | DataSecretName is the name of the secret that stores the bootstrap data script. | N/A |
|  **failureMessage** | `string` | FailureMessage will be set on non-retryable errors | N/A |
|  **failureReason** | `string` | FailureReason will be set on non-retryable errors | N/A |
|  **infraEnvRef** | `object` | INSERT ADDITIONAL STATUS FIELD - define observed state of cluster Important: Run "make" to regenerate code after modifying this file InfraEnvRef references the infra env to generate the ISO | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| └>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| └>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
|  **observedGeneration** | `integer` | ObservedGeneration is the latest generation observed by the controller. | N/A |
|  **ready** | `boolean` | Ready indicates the BootstrapData field is ready to be consumed | N/A |
