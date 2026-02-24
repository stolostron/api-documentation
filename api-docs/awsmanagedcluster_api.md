# AWSManagedCluster API

AWSManagedCluster is the Schema for the awsmanagedclusters API

## Spec Fields

AWSManagedClusterSpec defines the desired state of AWSManagedCluster

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **controlPlaneEndpoint** | `object` | ControlPlaneEndpoint represents the endpoint used to communicate with the control plane. | N/A |
| └>&nbsp;&nbsp; **host** | `string` | host is the hostname on which the API server is serving. | N/A |
| └>&nbsp;&nbsp; **port** | `integer` | port is the port on which the API server is serving. | N/A |
## Status Fields

AWSManagedClusterStatus defines the observed state of AWSManagedCluster

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions defines current service state of the AWSManagedCluster. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | reason is the reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **failureDomains** | `object` | FailureDomains specifies a list fo available availability zones that can be used | N/A |
|  **ready** | `boolean` | Ready is when the AWSManagedControlPlane has a API server URL. | N/A |
