# AROCluster API

AROCluster is the Schema for the AROClusters API.

## Spec Fields

AROClusterSpec defines the desired state of AROCluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **controlPlaneEndpoint** | `object` | ControlPlaneEndpoint represents the endpoint used to communicate with the control plane. | N/A |
| └>&nbsp;&nbsp; **host** | `string` | host is the hostname on which the API server is serving. | N/A |
| └>&nbsp;&nbsp; **port** | `integer` | port is the port on which the API server is serving. | `Minimum=1`<br>`Maximum=65535` |
|  **resources** | `array` | Resources are embedded ASO resources to be managed by this AROCluster. These typically include ResourceGroup, VirtualNetwork, NetworkSecurityGroup, VirtualNetworksSubnet, Vault (Key Vault), UserAssignedIdentities, and RoleAssignments. | N/A |
## Status Fields

AROClusterStatus defines the observed state of AROCluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions define the current service state of the AROCluster. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **failureDomains** | `array` | FailureDomains specifies a list fo available availability zones that can be used | N/A |
| └>&nbsp;&nbsp; **attributes** | `object` | attributes is a free form map of attributes an infrastructure provider might use or require. | N/A |
| └>&nbsp;&nbsp; **controlPlane** | `boolean` | controlPlane determines if this failure domain is suitable for use by control plane machines. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | name is the name of the failure domain. | N/A |
|  **initialization** | `object` | initialization provides observations of the AROCluster initialization process. NOTE: Fields in this struct are part of the Cluster API contract and are used to orchestrate initial Machine provisioning. | N/A |
| └>&nbsp;&nbsp; **provisioned** | `boolean` | provision is true when the AROCluster provider reports that the infra cluster is provisioned; A infra cluster is considered provisioned when it has valid endpoint. NOTE: this field is part of the Cluster API contract, and it is used to orchestrate initial Machine provisioning. | N/A |
|  **ready** | `boolean` | Ready is when the AROControlPlane has a API server URL. | N/A |
|  **resources** | `array` | Resources represents the status of ASO resources managed by this AROCluster. This is populated when using the Resources field in the spec. | N/A |
| └>&nbsp;&nbsp; **ready** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **resource** | `object` | StatusResource is a handle to a resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | No description provided. | N/A |
