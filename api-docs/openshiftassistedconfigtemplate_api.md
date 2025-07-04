# OpenshiftAssistedConfigTemplate API

## Spec Fields

OpenshiftAssistedConfigTemplateSpec defines the desired state of OpenshiftAssistedConfigTemplate

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **template** | `object` | OpenshiftAssistedConfig template | N/A |
| └>&nbsp;&nbsp; **metadata** | `object` | Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **annotations** | `object` | annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **labels** | `object` | Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels | N/A |
| └>&nbsp;&nbsp; **spec** | `object` | OpenshiftAssistedConfigSpec defines the desired state of OpenshiftAssistedConfig | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **additionalNTPSources** | `array` | AdditionalNTPSources is a list of NTP sources (hostname or IP) to be added to all cluster hosts. They are added to any NTP sources that were configured through other means. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **additionalTrustBundle** | `string` | PEM-encoded X.509 certificate bundle. Hosts discovered by this infra-env will trust the certificates in this bundle. Clusters formed from the hosts discovered by this infra-env will also trust the certificates in this bundle. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cpuArchitecture** | `string` | CpuArchitecture specifies the target CPU architecture. Default is x86_64 | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kernelArguments** | `array` | KernelArguments is the additional kernel arguments to be passed during boot time of the discovery image. Applicable for both iPXE, and ISO streaming from Image Service. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operation** | `string` | Operation is the operation to apply on the kernel argument. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value can have the form <parameter> or <parameter>=<value>. The following examples should be supported: rd.net.timeout.carrier=60 isolcpus=1,2,10-20,100-2000:2/25 quiet | `Pattern=^(?:(?:[^ \t\n\r"]+)\|(?:"[^"]*"))+$` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **nmStateConfigLabelSelector** | `object` | NmstateConfigLabelSelector associates NMStateConfigs for hosts that are considered part of this installation environment. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **nodeRegistration** | `object` | NodeRegistrationOption holds fields related to registering nodes to the cluster | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kubeletExtraLabels** | `array` | KubeletExtraLabels passes extra labels to kubelet. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Defaults to the hostname of the node if not provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **osImageVersion** | `string` | OSImageVersion is the version of OS image to use when generating the InfraEnv. The version should refer to an OSImage specified in the AgentServiceConfig (i.e. OSImageVersion should equal to an OpenshiftVersion in OSImages list). Note: OSImageVersion can't be specified along with ClusterRef. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **proxy** | `object` | Proxy defines the proxy settings for agents and clusters that use the InfraEnv. If unset, the agents and clusters will not be configured to use a proxy. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **httpProxy** | `string` | HTTPProxy is the URL of the proxy for HTTP requests. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **httpsProxy** | `string` | HTTPSProxy is the URL of the proxy for HTTPS requests. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **noProxy** | `string` | NoProxy is a comma-separated list of domains and CIDRs for which the proxy should not be used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **pullSecretRef** | `object` | PullSecretRef is the reference to the secret to use when pulling images. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sshAuthorizedKey** | `string` | SSHAuthorizedKey is a SSH public keys that will be added to all agents for use in debugging. | N/A |
## Status Fields

OpenshiftAssistedConfigTemplateStatus defines the observed state of OpenshiftAssistedConfigTemplate

| Field | Type | Description | Validations |
|:---|---|---|---|
