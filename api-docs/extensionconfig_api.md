# ExtensionConfig API

ExtensionConfig is the Schema for the ExtensionConfig API.

## Spec Fields

ExtensionConfigSpec is the desired state of the ExtensionConfig

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **clientConfig** | `object` | clientConfig defines how to communicate with the Extension server. | N/A |
| └>&nbsp;&nbsp; **caBundle** | `string` | caBundle is a PEM encoded CA bundle which will be used to validate the Extension server's server certificate. | N/A |
| └>&nbsp;&nbsp; **service** | `object` | service is a reference to the Kubernetes service for the Extension server. Note: Exactly one of `url` or `service` must be specified. If the Extension server is running within a cluster, then you should use `service`. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | name is the name of the service. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | namespace is the namespace of the service. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **path** | `string` | path is an optional URL path and if present may be any string permissible in a URL. If a path is set it will be used as prefix to the hook-specific path. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **port** | `integer` | port is the port on the service that's hosting the Extension server. Defaults to 443. Port should be a valid port number (1-65535, inclusive). | N/A |
| └>&nbsp;&nbsp; **url** | `string` | url gives the location of the Extension server, in standard URL form (`scheme://host:port/path`). Note: Exactly one of `url` or `service` must be specified. The scheme must be "https". The `host` should not refer to a service running in the cluster; use the `service` field instead. A path is optional, and if present may be any string permissible in a URL. If a path is set it will be used as prefix to the hook-specific path. Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#...") and query parameters ("?...") are not allowed either. | N/A |
|  **namespaceSelector** | `object` | namespaceSelector decides whether to call the hook for an object based on whether the namespace for that object matches the selector. Defaults to the empty LabelSelector, which matches all objects. | N/A |
| └>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| └>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
|  **settings** | `object` | settings defines key value pairs to be passed to all calls to all supported RuntimeExtensions. Note: Settings can be overridden on the ClusterClass. | N/A |
## Status Fields

ExtensionConfigStatus is the current state of the ExtensionConfig

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | conditions define the current service state of the ExtensionConfig. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | Last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | A human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | The reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **handlers** | `array` | handlers defines the current ExtensionHandlers supported by an Extension. | N/A |
| └>&nbsp;&nbsp; **failurePolicy** | `string` | failurePolicy defines how failures in calls to the ExtensionHandler should be handled by a client. Defaults to Fail if not set. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | name is the unique name of the ExtensionHandler. | N/A |
| └>&nbsp;&nbsp; **requestHook** | `object` | requestHook defines the versioned runtime hook which this ExtensionHandler serves. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiVersion** | `string` | apiVersion is the group and version of the Hook. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **hook** | `string` | hook is the name of the hook. | N/A |
| └>&nbsp;&nbsp; **timeoutSeconds** | `integer` | timeoutSeconds defines the timeout duration for client calls to the ExtensionHandler. Defaults to 10 is not set. | N/A |
