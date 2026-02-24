# ObservabilityAddon API

ObservabilityAddon is the Schema for the observabilityaddon API

## Spec Fields

ObservabilityAddonSpec is the spec of observability addon.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **enableMetrics** | `boolean` | EnableMetrics indicates the observability addon push metrics to hub server. | N/A |
|  **interval** | `integer` | Interval for the observability addon push metrics to hub server. | `Minimum=15`<br>`Maximum=3600` |
|  **resources** | `object` | Resource requirement for metrics-collector | N/A |
| └>&nbsp;&nbsp; **claims** | `array` | Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container. This is an alpha field and requires enabling the DynamicResourceAllocation feature gate. This field is immutable. It can only be set for containers. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **request** | `string` | Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request. | N/A |
| └>&nbsp;&nbsp; **limits** | `object` | Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | N/A |
| └>&nbsp;&nbsp; **requests** | `object` | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | N/A |
|  **scrapeSizeLimitBytes** | `integer` | ScrapeSizeLimitBytes is the max size in bytes for a single metrics scrape from in-cluster Prometheus. Default is 1 GiB. | N/A |
|  **workers** | `integer` | Workers is the number of workers in metrics-collector that work in parallel to push metrics to hub server. If set to > 1, metrics-collector will shard /federate calls to Prometheus, based on matcher rules provided by allowlist. Ensure that number of matchers exceeds number of workers. | `Minimum=1` |
## Status Fields

ObservabilityAddonStatus defines the observed state of ObservabilityAddon

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | No description provided. | N/A |
