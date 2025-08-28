# MultiClusterObservability API

MultiClusterObservability defines the configuration for the Observability installation on
Hub and Managed Clusters all through this one custom resource.

## Spec Fields

MultiClusterObservabilitySpec defines the desired state of MultiClusterObservability.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **availabilityConfig** | `string` | ReplicaCount for HA support. Does not affect data stores. Enabled will toggle HA support. This will provide better support in cases of failover but consumes more resources. Options are: Basic and High (default). | N/A |
|  **enableDownSampling** | `boolean` | Enable or disable the downsample. The default value is false. This is not recommended as querying long time ranges without non-downsampled data is not efficient and useful. | N/A |
|  **imagePullPolicy** | `string` | Pull policy of the MultiClusterObservability images | N/A |
|  **imagePullSecret** | `string` | Pull secret of the MultiClusterObservability images | N/A |
|  **nodeSelector** | `object` | Spec of NodeSelector | N/A |
|  **observabilityAddonSpec** | `object` | The ObservabilityAddonSpec defines the global settings for all managed clusters which have observability add-on enabled. | N/A |
| └>&nbsp;&nbsp; **enableMetrics** | `boolean` | EnableMetrics indicates the observability addon push metrics to hub server. | N/A |
| └>&nbsp;&nbsp; **interval** | `integer` | Interval for the observability addon push metrics to hub server. | `Minimum=15`<br>`Maximum=3600` |
| └>&nbsp;&nbsp; **resources** | `object` | Resource requirement for metrics-collector | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **claims** | `array` | Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container. This is an alpha field and requires enabling the DynamicResourceAllocation feature gate. This field is immutable. It can only be set for containers. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **limits** | `object` | Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **requests** | `object` | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | N/A |
| └>&nbsp;&nbsp; **scrapeSizeLimitBytes** | `integer` | ScrapeSizeLimitBytes is the max size in bytes for a single metrics scrape from in-cluster Prometheus. Default is 1 GiB. | N/A |
| └>&nbsp;&nbsp; **workers** | `integer` | Workers is the number of workers in metrics-collector that work in parallel to push metrics to hub server. If set to > 1, metrics-collector will shard /federate calls to Prometheus, based on matcher rules provided by allowlist. Ensure that number of matchers exceeds number of workers. | `Minimum=1` |
|  **retentionResolution1h** | `string` | How long to retain samples of resolution 2 (1 hour) in bucket. | N/A |
|  **retentionResolution5m** | `string` | How long to retain samples of resolution 1 (5 minutes) in bucket. | N/A |
|  **retentionResolutionRaw** | `string` | How long to retain raw samples in a bucket. | N/A |
|  **storageConfigObject** | `object` | Specifies the storage to be used by Observability | N/A |
| └>&nbsp;&nbsp; **metricObjectStorage** | `object` | Object store config secret for metrics | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | The key of the secret to select from. Must be a valid secret key. Refer to https://thanos.io/tip/thanos/storage.md/#configuring-access-to-object-storage for a valid content of key. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serviceAccountProjection** | `boolean` | serviceAccountProjection indicates whether mount service account token to thanos pods. Default is false. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tlsSecretMountPath** | `string` | TLS secret mount path for the custom certificate for the object store | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tlsSecretName** | `string` | TLS secret contains the custom certificate for the object store | N/A |
| └>&nbsp;&nbsp; **statefulSetSize** | `string` | The amount of storage applied to the Observability stateful sets, i.e. Thanos store, Rule, compact and receiver. | N/A |
| └>&nbsp;&nbsp; **statefulSetStorageClass** | `string` | 	Specify the storageClass Stateful Sets. This storage class will also be used for Object Storage if MetricObjectStorage was configured for the system to create the storage. | N/A |
|  **tolerations** | `array` | Tolerations causes all components to tolerate any taints. | N/A |
| └>&nbsp;&nbsp; **effect** | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute. | N/A |
| └>&nbsp;&nbsp; **key** | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. | N/A |
| └>&nbsp;&nbsp; **operator** | `string` | Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. | N/A |
| └>&nbsp;&nbsp; **tolerationSeconds** | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. | N/A |
| └>&nbsp;&nbsp; **value** | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. | N/A |
## Status Fields

MultiClusterObservabilityStatus defines the observed state of MultiClusterObservability.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Represents the status of each deployment | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt) | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
