# GitOpsCluster API

The GitOpsCluster uses placement to import selected managed clusters into the Argo CD.

## Spec Fields

GitOpsClusterSpec defines the desired state of GitOpsCluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **argoServer** | `object` | ArgoServerSpec specifies the location of the Argo CD server. | N/A |
| └>&nbsp;&nbsp; **argoNamespace** | `string` | ArgoNamespace is the namespace in which the Argo CD server is installed. | N/A |
| └>&nbsp;&nbsp; **cluster** | `string` | Not used and reserved for defining a managed cluster name. | N/A |
|  **createBlankClusterSecrets** | `boolean` | Internally used. | N/A |
|  **createPolicyTemplate** | `boolean` | Create default policy template if it is true. | N/A |
|  **gitopsAddon** | `object` | GitOpsAddon defines the configuration for the GitOps addon. | N/A |
| └>&nbsp;&nbsp; **argoCDAgent** | `object` | ArgoCDAgent defines the configuration for the ArgoCD agent. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **enabled** | `boolean` | Enabled indicates whether the ArgoCD agent is enabled. Default is false. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **image** | `string` | Image specifies the ArgoCD agent container image. Default is empty. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **mode** | `string` | Mode specifies the ArgoCD agent mode. Default is empty. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **propagateHubCA** | `boolean` | PropagateHubCA indicates whether to propagate the hub CA certificate to managed clusters via ManifestWork. Default is true. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serverAddress** | `string` | ServerAddress specifies the ArgoCD server address for the agent. Default is empty. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serverPort** | `string` | ServerPort specifies the ArgoCD server port for the agent. Default is empty. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **uninstall** | `boolean` | Uninstall indicates whether to uninstall only the ArgoCD agent component. Default is false. When set to true, only the agent component is uninstalled while keeping the gitopsAddon. This is different from GitOpsAddonSpec.Uninstall which removes everything. | N/A |
| └>&nbsp;&nbsp; **enabled** | `boolean` | Enabled indicates whether the GitOps addon is enabled. Default is false. When enabled, creates AddonDeploymentConfigs/ManagedClusterAddon resources. | N/A |
| └>&nbsp;&nbsp; **gitOpsImage** | `string` | GitOpsImage specifies the GitOps (ArgoCD) container image. Default is empty. | N/A |
| └>&nbsp;&nbsp; **gitOpsNamespace** | `string` | GitOpsNamespace specifies the GitOps namespace. Default is empty. | N/A |
| └>&nbsp;&nbsp; **gitOpsOperatorImage** | `string` | GitOpsOperatorImage specifies the GitOps operator container image. Default is empty. | N/A |
| └>&nbsp;&nbsp; **gitOpsOperatorNamespace** | `string` | GitOpsOperatorNamespace specifies the GitOps operator namespace. Default is empty. | N/A |
| └>&nbsp;&nbsp; **overrideExistingConfigs** | `boolean` | OverrideExistingConfigs indicates whether to override existing configuration values in AddOnDeploymentConfig. When false (default), existing config values are preserved and only new ones are added. When true, config values from GitOpsCluster spec will override existing values. | N/A |
| └>&nbsp;&nbsp; **reconcileScope** | `string` | ReconcileScope specifies the reconcile scope for the GitOps operator. Default is empty. | N/A |
| └>&nbsp;&nbsp; **redisImage** | `string` | RedisImage specifies the Redis container image. Default is empty. | N/A |
| └>&nbsp;&nbsp; **uninstall** | `boolean` | Uninstall indicates whether to uninstall the gitopsaddon. Default is false. When set to true, performs uninstall operations instead of install. When uninstall is true, OverrideExistingConfigs is automatically set to true. | N/A |
|  **managedServiceAccountRef** | `string` | ManagedServiceAccountRef defines managed service account in the managed cluster namespace used to create the ArgoCD cluster secret. | N/A |
|  **placementRef** | `object` | ObjectReference contains enough information to let you inspect or modify the referred object. | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| └>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| └>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
## Status Fields

GitOpsClusterStatus defines the observed state of GitOpsCluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions represent the latest available observations of the GitOpsCluster's current state. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **lastUpdateTime** | `string` | LastUpdateTime provides the last updated timestamp of the gitOpsCluster status | N/A |
|  **message** | `string` | Message provides the detailed message of the GitOpsCluster status. | N/A |
|  **phase** | `string` | Phase provides the overall phase of the GitOpsCluster status. Valid values include failed or successful. This field is kept for backward compatibility. For detailed status information, use the Conditions field. | N/A |
