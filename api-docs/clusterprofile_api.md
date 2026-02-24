# ClusterProfile API

ClusterProfile represents a single cluster in a multi-cluster deployment.

## Spec Fields

ClusterProfileSpec defines the desired state of ClusterProfile.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **clusterManager** | `object` | ClusterManager defines which cluster manager owns this ClusterProfile resource | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name defines the name of the cluster manager | N/A |
|  **displayName** | `string` | DisplayName defines a human-readable name of the ClusterProfile | N/A |
## Status Fields

ClusterProfileStatus defines the observed state of ClusterProfile.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **accessProviders** | `array` | AccessProviders is a list of cluster access providers that can provide access information for clusters. | N/A |
| └>&nbsp;&nbsp; **cluster** | `object` | Cluster contains information about how to communicate with a kubernetes cluster | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **certificate-authority** | `string` | CertificateAuthority is the path to a cert file for the certificate authority. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **certificate-authority-data** | `string` | CertificateAuthorityData contains PEM-encoded certificate authority certificates. Overrides CertificateAuthority | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **disable-compression** | `boolean` | DisableCompression allows client to opt-out of response compression for all requests to the server. This is useful to speed up requests (specifically lists) when client-server network bandwidth is ample, by saving time on compression (server-side) and decompression (client-side): https://github.com/kubernetes/kubernetes/issues/112296. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **extensions** | `array` | Extensions holds additional information. This is useful for extenders so that reads and writes don't clobber unknown fields | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **extension** | `object` | Extension holds the extension information | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the nickname for this Extension | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **insecure-skip-tls-verify** | `boolean` | InsecureSkipTLSVerify skips the validity check for the server's certificate. This will make your HTTPS connections insecure. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **proxy-url** | `string` | ProxyURL is the URL to the proxy to be used for all requests made by this client. URLs with "http", "https", and "socks5" schemes are supported.  If this configuration is not provided or the empty string, the client attempts to construct a proxy configuration from http_proxy and https_proxy environment variables. If these environment variables are not set, the client does not attempt to proxy requests. socks5 proxying does not currently support spdy streaming endpoints (exec, attach, port forward). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **server** | `string` | Server is the address of the kubernetes cluster (https://hostname:port). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tls-server-name** | `string` | TLSServerName is used to check server certificate. If TLSServerName is empty, the hostname used to contact the server is used. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
|  **conditions** | `array` | Conditions contains the different condition statuses for this cluster. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **credentialProviders** | `array` | CredentialProviders is a list of cluster access providers that can provide access information for clusters. Deprecated: Use AccessProviders instead. If both AccessProviders and CredentialProviders are provided, both are used. In case they specify a provider with the same name, the one in AccessProviders is preferred. | N/A |
| └>&nbsp;&nbsp; **cluster** | `object` | Cluster contains information about how to communicate with a kubernetes cluster | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **certificate-authority** | `string` | CertificateAuthority is the path to a cert file for the certificate authority. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **certificate-authority-data** | `string` | CertificateAuthorityData contains PEM-encoded certificate authority certificates. Overrides CertificateAuthority | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **disable-compression** | `boolean` | DisableCompression allows client to opt-out of response compression for all requests to the server. This is useful to speed up requests (specifically lists) when client-server network bandwidth is ample, by saving time on compression (server-side) and decompression (client-side): https://github.com/kubernetes/kubernetes/issues/112296. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **extensions** | `array` | Extensions holds additional information. This is useful for extenders so that reads and writes don't clobber unknown fields | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **extension** | `object` | Extension holds the extension information | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the nickname for this Extension | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **insecure-skip-tls-verify** | `boolean` | InsecureSkipTLSVerify skips the validity check for the server's certificate. This will make your HTTPS connections insecure. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **proxy-url** | `string` | ProxyURL is the URL to the proxy to be used for all requests made by this client. URLs with "http", "https", and "socks5" schemes are supported.  If this configuration is not provided or the empty string, the client attempts to construct a proxy configuration from http_proxy and https_proxy environment variables. If these environment variables are not set, the client does not attempt to proxy requests. socks5 proxying does not currently support spdy streaming endpoints (exec, attach, port forward). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **server** | `string` | Server is the address of the kubernetes cluster (https://hostname:port). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tls-server-name** | `string` | TLSServerName is used to check server certificate. If TLSServerName is empty, the hostname used to contact the server is used. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
|  **properties** | `array` | Properties defines cluster characteristics through a list of Property objects. Each Property can be one of: 1. A ClusterProperty resource (as defined in KEP-2149) 2. Custom information from cluster manager implementations Property names support both: - Standard names from ClusterProperty resources - Custom names defined by cluster managers | N/A |
| └>&nbsp;&nbsp; **lastObservedTime** | `string` | LastObservedTime is the last time the property was observed on the corresponding cluster. The value is the timestamp when the property was observed not the time when the property was updated in the cluster-profile. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of a property resource on cluster. It's a well-known or customized name to identify the property. | N/A |
| └>&nbsp;&nbsp; **value** | `string` | Value is a property-dependent string | N/A |
|  **version** | `object` | Version defines the version information of the cluster. | N/A |
| └>&nbsp;&nbsp; **kubernetes** | `string` | Kubernetes is the kubernetes version of the cluster. | N/A |
