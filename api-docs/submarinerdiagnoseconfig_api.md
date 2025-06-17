# SubmarinerDiagnoseConfig API

Status represents the current status of SubmarinerDiagnose

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **CNI** | `boolean` | No description provided. | N/A |
|  **all** | `boolean` | No description provided. | N/A |
|  **connections** | `boolean` | No description provided. | N/A |
|  **deployment** | `boolean` | No description provided. | N/A |
|  **firewall** | `boolean` | No description provided. | N/A |
|  **firewallOptions** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **interCluster** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **intraCluster** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **metrics** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **remoteCluster** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **remoteK8sAPIServer** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **remoteK8sAPIServerToken** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **remoteK8sCA** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **remoteK8sRemoteNamespace** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **remoteK8sSecret** | `string` | No description provided. | N/A |
|  **gatherLogs** | `boolean` | No description provided. | N/A |
|  **k8sVersion** | `boolean` | No description provided. | N/A |
|  **kubeProxyMode** | `boolean` | No description provided. | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **cniType** | `string` | No description provided. | N/A |
|  **conditions** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **firewallStatus** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **IPSecTunnel** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **metricsStatus** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **vxlanTunnel** | `string` | No description provided. | N/A |
|  **k8sVersion** | `string` | No description provided. | N/A |
|  **kubeProxyMode** | `boolean` | No description provided. | N/A |
