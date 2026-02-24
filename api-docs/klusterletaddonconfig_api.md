# KlusterletAddonConfig API

KlusterletAddonConfig is the Schema for the klusterletaddonconfigs API

## Spec Fields

KlusterletAddonConfigSpec defines the desired state of KlusterletAddonConfig

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **applicationManager** | `object` | ApplicationManagerConfig defines the configurations of ApplicationManager addon agent. | N/A |
| └>&nbsp;&nbsp; **enabled** | `boolean` | Enabled is the flag to enable/disable the addon. default is false. | N/A |
| └>&nbsp;&nbsp; **proxyPolicy** | `string` | ProxyPolicy defines the policy to set proxy for each addon agent. default is Disabled. Disabled means that the addon agent pods do not configure the proxy env variables. OCPGlobalProxy means that the addon agent pods use the cluster-wide proxy config of OCP cluster provisioned by ACM. CustomProxy means that the addon agent pods use the ProxyConfig specified in KlusterletAddonConfig. | N/A |
|  **certPolicyController** | `object` | CertPolicyControllerConfig defines the configurations of CertPolicyController addon agent. | N/A |
| └>&nbsp;&nbsp; **enabled** | `boolean` | Enabled is the flag to enable/disable the addon. default is false. | N/A |
| └>&nbsp;&nbsp; **proxyPolicy** | `string` | ProxyPolicy defines the policy to set proxy for each addon agent. default is Disabled. Disabled means that the addon agent pods do not configure the proxy env variables. OCPGlobalProxy means that the addon agent pods use the cluster-wide proxy config of OCP cluster provisioned by ACM. CustomProxy means that the addon agent pods use the ProxyConfig specified in KlusterletAddonConfig. | N/A |
|  **clusterLabels** | `object` | DEPRECATED in release 2.4 and will be removed in the future since not used anymore. | N/A |
|  **clusterName** | `string` | DEPRECATED in release 2.4 and will be removed in the future since not used anymore. | N/A |
|  **clusterNamespace** | `string` | DEPRECATED in release 2.4 and will be removed in the future since not used anymore. | N/A |
|  **iamPolicyController** | `object` | DEPRECATED in release 2.11 and will be removed in the future since not used anymore. | N/A |
| └>&nbsp;&nbsp; **enabled** | `boolean` | Enabled is the flag to enable/disable the addon. default is false. | N/A |
| └>&nbsp;&nbsp; **proxyPolicy** | `string` | ProxyPolicy defines the policy to set proxy for each addon agent. default is Disabled. Disabled means that the addon agent pods do not configure the proxy env variables. OCPGlobalProxy means that the addon agent pods use the cluster-wide proxy config of OCP cluster provisioned by ACM. CustomProxy means that the addon agent pods use the ProxyConfig specified in KlusterletAddonConfig. | N/A |
|  **policyController** | `object` | PolicyController defines the configurations of PolicyController addon agent. | N/A |
| └>&nbsp;&nbsp; **enabled** | `boolean` | Enabled is the flag to enable/disable the addon. default is false. | N/A |
| └>&nbsp;&nbsp; **proxyPolicy** | `string` | ProxyPolicy defines the policy to set proxy for each addon agent. default is Disabled. Disabled means that the addon agent pods do not configure the proxy env variables. OCPGlobalProxy means that the addon agent pods use the cluster-wide proxy config of OCP cluster provisioned by ACM. CustomProxy means that the addon agent pods use the ProxyConfig specified in KlusterletAddonConfig. | N/A |
|  **proxyConfig** | `object` | ProxyConfig defines the cluster-wide proxy configuration of the OCP managed cluster. | N/A |
| └>&nbsp;&nbsp; **httpProxy** | `string` | HTTPProxy is the URL of the proxy for HTTP requests.  Empty means unset and will not result in an env var. | N/A |
| └>&nbsp;&nbsp; **httpsProxy** | `string` | HTTPSProxy is the URL of the proxy for HTTPS requests.  Empty means unset and will not result in an env var. | N/A |
| └>&nbsp;&nbsp; **noProxy** | `string` | NoProxy is a comma-separated list of hostnames and/or CIDRs for which the proxy should not be used. Empty means unset and will not result in an env var. The API Server of Hub cluster should be added here. And If you scale up workers that are not included in the network defined by the networking.machineNetwork[].cidr field from the installation configuration, you must add them to this list to prevent connection issues. | N/A |
|  **searchCollector** | `object` | SearchCollectorConfig defines the configurations of SearchCollector addon agent. | N/A |
| └>&nbsp;&nbsp; **enabled** | `boolean` | Enabled is the flag to enable/disable the addon. default is false. | N/A |
| └>&nbsp;&nbsp; **proxyPolicy** | `string` | ProxyPolicy defines the policy to set proxy for each addon agent. default is Disabled. Disabled means that the addon agent pods do not configure the proxy env variables. OCPGlobalProxy means that the addon agent pods use the cluster-wide proxy config of OCP cluster provisioned by ACM. CustomProxy means that the addon agent pods use the ProxyConfig specified in KlusterletAddonConfig. | N/A |
|  **version** | `string` | DEPRECATED in release 2.4 and will be removed in the future since not used anymore. | N/A |
## Status Fields

KlusterletAddonConfigStatus defines the observed state of KlusterletAddonConfig

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions contains condition information for the klusterletAddonConfig | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt) | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **ocpGlobalProxy** | `object` | OCPGlobalProxy is the cluster-wide proxy config of the OCP cluster provisioned by ACM | N/A |
| └>&nbsp;&nbsp; **httpProxy** | `string` | HTTPProxy is the URL of the proxy for HTTP requests.  Empty means unset and will not result in an env var. | N/A |
| └>&nbsp;&nbsp; **httpsProxy** | `string` | HTTPSProxy is the URL of the proxy for HTTPS requests.  Empty means unset and will not result in an env var. | N/A |
| └>&nbsp;&nbsp; **noProxy** | `string` | NoProxy is a comma-separated list of hostnames and/or CIDRs for which the proxy should not be used. Empty means unset and will not result in an env var. The API Server of Hub cluster should be added here. And If you scale up workers that are not included in the network defined by the networking.machineNetwork[].cidr field from the installation configuration, you must add them to this list to prevent connection issues. | N/A |
