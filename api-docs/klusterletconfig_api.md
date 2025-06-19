# KlusterletConfig API

Status defines the observed state of KlusterletConfig

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **appliedManifestWorkEvictionGracePeriod** | `string` | AppliedManifestWorkEvictionGracePeriod is the eviction grace period the work agent will wait before evicting the AppliedManifestWorks, whose corresponding ManifestWorks are missing on the hub cluster, from the managed cluster. If not present, the default value of the work agent will be used. If its value is set to "INFINITE", it means the AppliedManifestWorks will never been evicted from the managed cluster. | `Pattern=^([0-9]+(s\|m\|h))+$\|^INFINITE$` |
|  **clusterClaimConfiguration** | `object` | ClusterClaimConfiguration represents the configuration of ClusterClaim Effective only when the `ClusterClaim` feature gate is enabled. | N/A |
| └>&nbsp;&nbsp; **maxCustomClusterClaims** | `integer` | Maximum number of custom ClusterClaims allowed. | N/A |
|  **featureGates** | `array` | FeatureGates is the list of feature gate for the klusterlet agent. If it is set empty, default feature gates will be used. | N/A |
| └>&nbsp;&nbsp; **feature** | `string` | Feature is the key of feature gate. e.g. featuregate/Foo. | N/A |
| └>&nbsp;&nbsp; **mode** | `string` | Mode is either Enable, Disable, "" where "" is Disable by default. In Enable mode, a valid feature gate `featuregate/Foo` will be set to "--featuregate/Foo=true". In Disable mode, a valid feature gate `featuregate/Foo` will be set to "--featuregate/Foo=false". | N/A |
|  **hubKubeAPIServerCABundle** | `string` | HubKubeAPIServerCABundle is the CA bundle to verify the server certificate of the hub kube API against. If not present, CA bundle will be determined with the logic below: 1). Use the certificate of the named certificate configured in APIServer/cluster if FQDN matches; 2). Otherwise use the CA certificates from kube-root-ca.crt ConfigMap in the cluster namespace;  Deprecated and maintained for backward compatibility, use HubKubeAPIServerConfig.ServerVarificationStrategy and HubKubeAPIServerConfig.TrustedCABundles instead | N/A |
|  **hubKubeAPIServerConfig** | `object` | HubKubeAPIServerConfig specifies the settings required for connecting to the hub Kube API server. If this field is present, the below deprecated fields will be ignored: - HubKubeAPIServerProxyConfig - HubKubeAPIServerURL - HubKubeAPIServerCABundle | N/A |
| └>&nbsp;&nbsp; **proxyURL** | `string` | ProxyURL is the URL to the proxy to be used for all requests made by client If an HTTPS proxy server is configured, you may also need to add the necessary CA certificates to TrustedCABundles. | N/A |
| └>&nbsp;&nbsp; **serverVerificationStrategy** | `string` | ServerVerificationStrategy is the strategy used for verifying the server certification; The value could be "UseSystemTruststore", "UseAutoDetectedCABundle", "UseCustomCABundles", empty.  When this strategy is not set or value is empty; if there is only one klusterletConfig configured for a cluster, the strategy is eaual to "UseAutoDetectedCABundle", if there are more than one klusterletConfigs, the empty strategy will be overrided by other non-empty strategies. | N/A |
| └>&nbsp;&nbsp; **trustedCABundles** | `array` | TrustedCABundles refers to a collection of user-provided CA bundles used for verifying the server certificate of the hub Kubernetes API If the ServerVerificationStrategy is set to "UseSystemTruststore", this field will be ignored. Otherwise, the CA certificates from the configured bundles will be appended to the klusterlet CA bundle. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **caBundle** | `object` | CABundle refers to a ConfigMap with label "import.open-cluster-management.io/ca-bundle" containing the user-provided CA bundle The key of the CA data could be "ca-bundle.crt", "ca.crt", or "tls.crt". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | name is the metadata.name of the referenced config map | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | name is the metadata.namespace of the referenced config map | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the identifier used to reference the CA bundle; Do not use "auto-detected" as the name since it is the reserved name for the auto-detected CA bundle. | N/A |
| └>&nbsp;&nbsp; **url** | `string` | URL is the endpoint of the hub Kube API server. If not present, the .status.apiServerURL of Infrastructure/cluster will be used as the default value. e.g. `oc get infrastructure cluster -o jsonpath='{.status.apiServerURL}'` | N/A |
|  **hubKubeAPIServerProxyConfig** | `object` | HubKubeAPIServerProxyConfig holds proxy settings for connections between klusterlet/add-on agents on the managed cluster and the kube-apiserver on the hub cluster. Empty means no proxy settings is available.  Deprecated and maintained for backward compatibility, use HubKubeAPIServerConfig.ProxyURL instead | N/A |
| └>&nbsp;&nbsp; **caBundle** | `string` | CABundle is a CA certificate bundle to verify the proxy server. It will be ignored if only HTTPProxy is set; And it is required when HTTPSProxy is set and self signed CA certificate is used by the proxy server. | N/A |
| └>&nbsp;&nbsp; **httpProxy** | `string` | HTTPProxy is the URL of the proxy for HTTP requests | N/A |
| └>&nbsp;&nbsp; **httpsProxy** | `string` | HTTPSProxy is the URL of the proxy for HTTPS requests HTTPSProxy will be chosen if both HTTPProxy and HTTPSProxy are set. | N/A |
|  **hubKubeAPIServerURL** | `string` | HubKubeAPIServerURL is the URL of the hub Kube API server. If not present, the .status.apiServerURL of Infrastructure/cluster will be used as the default value. e.g. `oc get infrastructure cluster -o jsonpath='{.status.apiServerURL}'`  Deprecated and maintained for backward compatibility, use HubKubeAPIServerConfig.URL instead | N/A |
|  **installMode** | `object` | InstallMode is the mode to install the klusterlet | N/A |
| └>&nbsp;&nbsp; **noOperator** | `object` | NoOperator is the setting of klusterlet installation when install type is noOperator. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **postfix** | `string` | Postfix is the postfix of the klusterlet name. The name of the klusterlet is "klusterlet" if it is not set, and "klusterlet-{Postfix}". The install namespace is "open-cluster-management-agent" if it is not set, and "open-cluster-management-{Postfix}". | `Pattern=^[-a-z0-9]*[a-z0-9]$` |
| └>&nbsp;&nbsp; **type** | `string` | InstallModeType is the type of install mode. | N/A |
|  **multipleHubsConfig** | `object` | MultipleHubsConfig contains configuration specific to multiple hub scenarios | N/A |
| └>&nbsp;&nbsp; **bootstrapKubeConfigs** | `object` | BootstrapKubeConfigs is the list of bootstrap kubeconfigs for multiple hubs | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **localSecretsConfig** | `object` | LocalSecretsConfig include a list of secrets that contains the kubeconfigs for ordered bootstrap kubeconifigs. The secrets must be in the same namespace where the agent controller runs. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **hubConnectionTimeoutSeconds** | `integer` | HubConnectionTimeoutSeconds is used to set the timeout of connecting to the hub cluster. When agent loses the connection to the hub over the timeout seconds, the agent do a rebootstrap. By default is 10 mins. | `Minimum=180` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kubeConfigSecrets** | `array` | KubeConfigSecrets is a list of secret names. The secrets are in the same namespace where the agent controller runs. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the secret. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type specifies the type of priority bootstrap kubeconfigs. By default, it is set to None, representing no priority bootstrap kubeconfigs are set. | N/A |
| └>&nbsp;&nbsp; **genBootstrapKubeConfigStrategy** | `string` | GenBootstrapKubeConfigStrategy controls the strategy for generating bootstrap kubeconfig files. Default - Generate bootstrap kubeconfigs only with the BootstrapKubeConfigs configured in KlusterletConfig. IncludeCurrentHub - When generating bootstrap kubeconfigs, automatically include the current hub's kubeconfig. | N/A |
|  **nodePlacement** | `object` | NodePlacement enables explicit control over the scheduling of the agent components. If the placement is nil, the placement is not specified, it will be omitted. If the placement is an empty object, the placement will match all nodes and tolerate nothing. | N/A |
| └>&nbsp;&nbsp; **nodeSelector** | `object` | NodeSelector defines which Nodes the Pods are scheduled on. The default is an empty list. | N/A |
| └>&nbsp;&nbsp; **tolerations** | `array` | Tolerations are attached by pods to tolerate any taint that matches the triple <key,value,effect> using the matching operator <operator>. The default is an empty list. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **effect** | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tolerationSeconds** | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. | N/A |
|  **pullSecret** | `object` | PullSecret is the name of image pull secret. | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| └>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| └>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
|  **registries** | `array` | Registries includes the mirror and source registries. The source registry will be replaced by the Mirror. | N/A |
| └>&nbsp;&nbsp; **mirror** | `string` | Mirror is the mirrored registry of the Source. Will be ignored if Mirror is empty. | N/A |
| └>&nbsp;&nbsp; **source** | `string` | Source is the source registry. All image registries will be replaced by Mirror if Source is empty. | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
