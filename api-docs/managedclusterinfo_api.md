# ManagedClusterInfo API

## Spec Fields

Spec defines the information of the Cluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **loggingCA** | `string` | LoggingCA is the ca data for logging server to authorize apiserver | N/A |
|  **masterEndpoint** | `string` | MasterEndpoint shows the apiserver endpoint of managed cluster | N/A |
## Status Fields

Status represents the desired status of the Cluster

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **cloudVendor** | `string` | CloudVendor describes the cloud provider for the managed cluster. Deprecated in release 2.3 and will be removed in the future. Use clusterClaim product.open-cluster-management.io instead. | N/A |
|  **clusterID** | `string` | ClusterID is the identifier of managed cluster. Deprecated in release 2.3 and will be removed in the future. Use clusterClaim id.openshift.io instead. | N/A |
|  **conditions** | `array` | Conditions contains condition information for a managed cluster | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt) | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **consoleURL** | `string` | ConsoleURL shows the url of console in managed cluster. Deprecated in release 2.3 and will be removed in the future. Use clusterClaim consoleurl.cluster.open-cluster-management.io instead. | N/A |
|  **distributionInfo** | `object` | DistributionInfo is the information about distribution of managed cluster | N/A |
| └>&nbsp;&nbsp; **ocp** | `object` | OCP is the distribution information of OCP managed cluster, is matched when the Type is OCP. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **availableUpdates** | `array` | AvailableUpdates contains the list of update versions that are appropriate for the manage cluster. Deprecated in release 2.3 and will be removed in the future. Use VersionAvailableUpdates instead. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **channel** | `string` | Channel is an identifier for explicitly requesting that a non-default set of updates be applied to this cluster. The default channel will be contain stable updates that are appropriate for production clusters. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **desired** | `object` | desired is the version that the cluster is reconciling towards. If the cluster is not yet fully initialized desired will be set with the information available, which may be an image or a tag. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **channels** | `array` | channels is the set of Cincinnati channels to which the release currently belongs. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **image** | `string` | image is a container image location that contains the update. When this field is part of spec, image is optional if version is specified and the availableUpdates field contains a matching version. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **url** | `string` | url contains information about this release. This URL is set by the 'url' metadata property on a release or the metadata returned by the update API and should be displayed as a link in user interfaces. The URL field may not be set for test or nightly releases. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | version is a semantic versioning identifying the update version. When this field is part of spec, version is optional if image is specified. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **desiredVersion** | `string` | DesiredVersion is the version that the cluster is reconciling towards. Deprecated in release 2.3 and will be removed in the future. User Desired instead. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **lastAppliedAPIServerURL** | `string` | LastAppliedAPIServerURL is a valid URI with scheme 'https', address and optionally a port (defaulting to 443). it can be used by components like the web console to tell users where to find the Kubernetes API. This is the api server url that has been applied to the managedcluster resource successfully | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **managedClusterClientConfig** | `object` | Controller will sync this field to managedcluster's ManagedClusterClientConfigs | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **caBundle** | `string` | CABundle is the ca bundle to connect to apiserver of the managed cluster. System certs are used if it is not set. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **url** | `string` | URL is the URL of apiserver endpoint of the managed cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **upgradeFailed** | `boolean` | UpgradeFailed indicates whether upgrade of the manage cluster is failed. This is true if the status of Failing condition is True and the version is different with desiredVersion in clusterVersion | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | Version is the current version of the OCP cluster. Deprecated in release 2.3 and will be removed in the future. Use clusterClaim version.openshift.io instead. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **versionAvailableUpdates** | `array` | VersionAvailableUpdates contains the list of updates that are appropriate for this cluster. This list may be empty if no updates are recommended, if the update service is unavailable, or if an invalid channel has been specified. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **channels** | `array` | channels is the set of Cincinnati channels to which the release currently belongs. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **image** | `string` | image is a container image location that contains the update. When this field is part of spec, image is optional if version is specified and the availableUpdates field contains a matching version. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **url** | `string` | url contains information about this release. This URL is set by the 'url' metadata property on a release or the metadata returned by the update API and should be displayed as a link in user interfaces. The URL field may not be set for test or nightly releases. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | version is a semantic versioning identifying the update version. When this field is part of spec, version is optional if image is specified. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **versionHistory** | `array` | VersionHistory contains a list of the most recent versions applied to the cluster. This value may be empty during cluster startup, and then will be updated when a new update is being applied. The newest update is first in the list and it is ordered by recency. Updates in the history have state Completed if the rollout completed - if an update was failing or halfway applied the state will be Partial. Only a limited amount of update history is preserved. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **image** | `string` | image is a container image location that contains the update. This value is always populated. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **state** | `string` | state reflects whether the update was fully applied. The Partial state indicates the update is not fully applied, while the Completed state indicates the update was successfully rolled out at least once (all parts of the update successfully applied). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **verified** | `boolean` | verified indicates whether the provided update was properly verified before it was installed. If this is false the cluster may not be trusted. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | version is a semantic versioning identifying the update version. If the requested image does not define a version, or if a failure occurs retrieving the image, this value may be empty. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type is the distribution type of managed cluster, is OCP currently | N/A |
|  **kubeVendor** | `string` | KubeVendor describes the kubernetes provider of the managed cluster. Deprecated in release 2.3 and will be removed in the future. Use clusterClaim platform.open-cluster-management.io instead. | N/A |
|  **loggingEndpoint** | `object` | LoggingEndpoint shows the endpoint to connect to logging server of managed cluster | N/A |
| └>&nbsp;&nbsp; **hostname** | `string` | The Hostname of this endpoint | N/A |
| └>&nbsp;&nbsp; **ip** | `string` | The IP of this endpoint. May not be loopback (127.0.0.0/8), link-local (169.254.0.0/16), or link-local multicast ((224.0.0.0/24). IPv6 is also accepted but not fully supported on all platforms. Also, certain kubernetes components, like kube-proxy, are not IPv6 ready. TODO: This should allow hostname or IP, See #4447. | N/A |
| └>&nbsp;&nbsp; **nodeName** | `string` | Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node. | N/A |
| └>&nbsp;&nbsp; **targetRef** | `object` | Reference to object providing the endpoint. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. TODO: this design is not final and this field is subject to change in the future. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
|  **loggingPort** | `object` | LoggingPort shows the port to connect to logging server of managed cluster | N/A |
| └>&nbsp;&nbsp; **appProtocol** | `string` | The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and http://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | The name of this port.  This must match the 'name' field in the corresponding ServicePort. Must be a DNS_LABEL. Optional only if one port is defined. | N/A |
| └>&nbsp;&nbsp; **port** | `integer` | The port number of the endpoint. | N/A |
| └>&nbsp;&nbsp; **protocol** | `string` | The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP. | N/A |
|  **nodeList** | `array` | NodeList shows a list of the status of nodes | N/A |
| └>&nbsp;&nbsp; **capacity** | `object` | Capacity represents the total resources of a node. only includes CPU and memory. | N/A |
| └>&nbsp;&nbsp; **conditions** | `array` | Conditions is an array of current node conditions. only includes NodeReady. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **status** | `string` | Status of the condition, one of True, False, Unknown. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type of node condition. | N/A |
| └>&nbsp;&nbsp; **labels** | `object` | Labels of node. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of node | N/A |
|  **version** | `string` | Version is the kube version of managed cluster. | N/A |
