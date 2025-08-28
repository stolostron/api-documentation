# DiscoveredCluster API

DiscoveredCluster is the Schema for the discoveredclusters API

## Spec Fields

DiscoveredClusterSpec defines the desired state of DiscoveredCluster

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **activityTimestamp** | `string` | ActivityTimestamp records the last observed activity of the cluster. | N/A |
|  **apiUrl** | `string` | APIURL is the endpoint used to access the cluster's API server. | N/A |
|  **cloudProvider** | `string` | CloudProvider specifies the cloud provider where the cluster is hosted (e.g., AWS, Azure, GCP). | N/A |
|  **console** | `string` | Console provides the URL of the cluster's web-based console. | N/A |
|  **creationTimestamp** | `string` | CreationTimestamp marks when the cluster was initially discovered. | N/A |
|  **credential** | `object` | Credential references the Kubernetes secret containing authentication details for the cluster. | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| └>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. TODO: this design is not final and this field is subject to change in the future. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| └>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
|  **displayName** | `string` | DisplayName is a human-readable name assigned to the cluster. | N/A |
|  **importAsManagedCluster** | `boolean` | ImportAsManagedCluster determines whether the discovered cluster should be automatically imported as a managed cluster. | N/A |
|  **isManagedCluster** | `boolean` | IsManagedCluster indicates whether the cluster is currently managed. | N/A |
|  **name** | `string` | Name represents the unique identifier of the discovered cluster. | N/A |
|  **ocpClusterId** | `string` | OCPClusterID contains the unique identifier assigned by OpenShift to the cluster. | N/A |
|  **openshiftVersion** | `string` | OpenshiftVersion specifies the OpenShift version running on the cluster. | N/A |
|  **owner** | `string` | Owner identifies the owner or organization responsible for the cluster. | N/A |
|  **region** | `string` | Region specifies the geographical region where the cluster is deployed. | N/A |
|  **rhocmClusterId** | `string` | RHOCMClusterID contains the cluster ID from Red Hat OpenShift Cluster Manager. | N/A |
|  **status** | `string` | Status represents the current state of the discovered cluster (e.g Active, Stale). | N/A |
|  **type** | `string` | Type defines the type of cluster, such as OpenShift, Kubernetes, or a specific managed service type. | N/A |
## Status Fields

DiscoveredClusterStatus defines the observed state of DiscoveredCluster

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | INSERT ADDITIONAL STATUS FIELD - define observed state of cluster Important: Run "make" to regenerate code after modifying this file | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the last time the condition changed from one status to another. | N/A |
| └>&nbsp;&nbsp; **lastUpdateTime** | `string` | The last time this condition was updated. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status is the status of the condition. One of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type is the type of the discovered cluster condition. | N/A |
