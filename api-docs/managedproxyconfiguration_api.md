# ManagedProxyConfiguration API

## Spec Fields

ManagedProxyConfigurationSpec is the prescription of ManagedProxyConfiguration

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **authentication** | `object` | `authentication` defines how the credentials for the authentication between proxy servers and proxy agents are signed and mounted. | N/A |
| └>&nbsp;&nbsp; **dump** | `object` | `dump` is where we store the signed certificates from signers. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **secrets** | `object` | `secrets` is the names of the secrets for saving the signed certificates. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **signingAgentServerSecretName** | `string` | `signingAgentServerSecretName` is the secret name of the proxy servers to receive tunneling handshakes from proxy agents. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **signingProxyClientSecretName** | `string` | `signingProxyClientSecretName` is the secret name for requesting/streaming over the proxy server. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **signingProxyServerSecretName** | `string` | `signingProxyServerSecretName` the secret name of the proxy server's listening certificates for serving proxy requests. | N/A |
| └>&nbsp;&nbsp; **signer** | `object` | `signer` defines how we sign server and client certificates for the proxy servers and agents. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **selfSigned** | `object` | `selfSigned` prescribes the detail of how we self-sign the certificates. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **additionalSANs** | `array` | `additionalSANs` adds a few custom hostnames or IPs to the signing certificates. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | `type` is the supported type of signer. Currently only "SelfSign" supported. | N/A |
|  **deploy** | `object` | `deploy` is where we override miscellaneous details for deploying either proxy servers or agents. | N/A |
| └>&nbsp;&nbsp; **ports** | `object` | `ports` is the ports for proxying and tunneling. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **adminServer** | `integer` | `adminServer` is the port for debugging and operating. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **agentServer** | `integer` | `agentServer` is the listening port of proxy server for serving tunneling handshakes. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **healthServer** | `integer` | `healthServer` is for probing the healthiness. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **proxyServer** | `integer` | `proxyServer` is the listening port of proxy server for serving proxy requests. | N/A |
|  **proxyAgent** | `object` | `proxyServer` structurelized the arguments for running proxy agents. | N/A |
| └>&nbsp;&nbsp; **additionalArgs** | `array` | `additionalArgs` defines args used in proxy-agent. | N/A |
| └>&nbsp;&nbsp; **image** | `string` | `image` is the container image of the proxy agent. | N/A |
| └>&nbsp;&nbsp; **imagePullSecrets** | `array` | `imagePullSecrets` defines the imagePullSecrets used by proxy-agent | N/A |
| └>&nbsp;&nbsp; **replicas** | `integer` | `replicas` is the replicas of the agents. | N/A |
|  **proxyServer** | `object` | `proxyServer` structurelized the arguments for running proxy servers. | N/A |
| └>&nbsp;&nbsp; **additionalArgs** | `array` | `additionalArgs` adds arbitrary additional command line args to the proxy-server. | N/A |
| └>&nbsp;&nbsp; **entrypoint** | `object` | `entrypoint` defines how will the proxy agents connecting the servers. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **hostname** | `object` | `hostname` points to a fixed hostname for serving agents' handshakes. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **loadBalancerService** | `object` | `loadBalancerService` points to a load-balancer typed service in the hub cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **annotations** | `array` | Annotations is the annoations of the load-balancer service. This is for allowing customizing service using vendor-specific extended annotations such as: - service.beta.kubernetes.io/alibaba-cloud-loadbalancer-address-type: "intranet" - service.beta.kubernetes.io/azure-load-balancer-internal: true | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key of annotation | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is the value of annotation | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | `name` is the name of the load-balancer service. And the namespace will align to where the proxy-servers are deployed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **port** | `integer` | `port` is the target port to access proxy servers | `Minimum=1` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | `type` is the type of the entrypoint of the proxy servers. Currently supports "Hostname", "LoadBalancerService" | N/A |
| └>&nbsp;&nbsp; **image** | `string` | `image` is the container image of the proxy servers. | N/A |
| └>&nbsp;&nbsp; **inClusterServiceName** | `string` | `inClusterServiceName` is the name of the in-cluster service for proxying requests inside the hub cluster to the proxy servers. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | `namespace` is the namespace where we will deploy the proxy servers and related resources. | N/A |
| └>&nbsp;&nbsp; **nodePlacement** | `object` | NodePlacement defines which Nodes the proxy server are scheduled on. The default is an empty list. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **nodeSelector** | `object` | NodeSelector defines which Nodes the Pods are scheduled on. The default is an empty list. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tolerations** | `array` | Tolerations is attached by pods to tolerate any taint that matches the triple <key,value,effect> using the matching operator <operator>. The default is an empty list. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **effect** | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tolerationSeconds** | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. | N/A |
| └>&nbsp;&nbsp; **replicas** | `integer` | `replicas` is the expected replicas of the proxy servers. Note that the replicas will also be reflected in the flag `--server-count` so that agents can discover all the server instances. | N/A |
## Status Fields

ManagedProxyConfigurationStatus defines the observed state of ManagedProxyConfiguration

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt) | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **lastObservedGeneration** | `integer` | No description provided. | N/A |
