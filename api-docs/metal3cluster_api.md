# Metal3Cluster API

Metal3ClusterStatus defines the observed state of Metal3Cluster.

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **cloudProviderEnabled** | `boolean` | Determines if the cluster is to be deployed with an external cloud provider. If set to false, CAPM3 will use node labels to set providerID on the kubernetes nodes. If set to true, providerID is set on nodes by other entities and CAPM3 uses the value of the providerID on the m3m resource. Default value is true, it is set in the webhook. | N/A |
|  **controlPlaneEndpoint** | `object` | ControlPlaneEndpoint represents the endpoint used to communicate with the control plane. | N/A |
| └>&nbsp;&nbsp; **host** | `string` | Host is the hostname on which the API server is serving. | N/A |
| └>&nbsp;&nbsp; **port** | `integer` | Port is the port on which the API server is serving. | N/A |
|  **noCloudProvider** | `boolean` | Determines if the cluster is not to be deployed with an external cloud provider. If set to true, CAPM3 will use node labels to set providerID on the kubernetes nodes. If set to false, providerID is set on nodes by other entities and CAPM3 uses the value of the providerID on the m3m resource.  Deprecated: This field is deprecated, use cloudProviderEnabled instead | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions defines current service state of the Metal3Cluster. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | Last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | A human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | The reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **failureMessage** | `string` | FailureMessage indicates that there is a fatal problem reconciling the state, and will be set to a descriptive error message. | N/A |
|  **failureReason** | `string` | FailureReason indicates that there is a fatal problem reconciling the state, and will be set to a token value suitable for programmatic interpretation. | N/A |
|  **lastUpdated** | `string` | LastUpdated identifies when this status was last observed. | N/A |
|  **ready** | `boolean` | Ready denotes that the Metal3 cluster (infrastructure) is ready. In Baremetal case, it does not mean anything for now as no infrastructure steps need to be performed. Required by Cluster API. Set to True by the metal3Cluster controller after creation. | N/A |
