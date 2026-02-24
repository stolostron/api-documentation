# AROMachinePool API

AROMachinePool is the Schema for the aromachinepools API.

## Spec Fields

AROMachinePoolSpec defines the desired state of AROMachinePool.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **providerIDList** | `array` | ProviderIDList are the identification IDs of machine instances provided by the provider. This field must match the provider IDs as seen on the node objects corresponding to a machine pool's machine instances. | N/A |
|  **resources** | `array` | Resources are embedded ASO resources to be managed by this AROMachinePool. This allows you to define the HcpOpenShiftNodePool resource directly using ASO types. Required. Must include HcpOpenShiftClustersNodePool resource. | N/A |
## Status Fields

AROMachinePoolStatus defines the observed state of AROMachinePool.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **availableUpgrades** | `array` | Available upgrades for the ARO MachinePool. | N/A |
|  **conditions** | `array` | Conditions defines current service state of the managed machine pool | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **failureMessage** | `string` | FailureMessage will be set in the event that there is a terminal problem reconciling the state and will be set to a descriptive error message. This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the spec or the configuration of the controller, and that manual intervention is required. | N/A |
|  **id** | `string` | ID is the ID given by ARO. | N/A |
|  **initialization** | `object` | initialization provides observations of the AROMachinePool initialization process. NOTE: Fields in this struct are part of the Cluster API contract and are used to orchestrate initial Machine provisioning. | N/A |
| └>&nbsp;&nbsp; **provisioned** | `boolean` | provision is true when the AROMachinePoolInitializationStatus provider reports that the infra machine pool is provisioned; NOTE: this field is part of the Cluster API contract, and it is used to orchestrate initial Machine provisioning. | N/A |
|  **longRunningOperationStates** | `array` | LongRunningOperationStates saves the state for ARO long-running operations so they can be continued on the next reconciliation loop. | N/A |
| └>&nbsp;&nbsp; **data** | `string` | Data is the base64 url encoded json Azure AutoRest Future. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the Azure resource. Together with the service name, this forms the unique identifier for the future. | N/A |
| └>&nbsp;&nbsp; **resourceGroup** | `string` | ResourceGroup is the Azure resource group for the resource. | N/A |
| └>&nbsp;&nbsp; **serviceName** | `string` | ServiceName is the name of the Azure service. Together with the name of the resource, this forms the unique identifier for the future. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type describes the type of future, such as update, create, delete, etc. | N/A |
|  **provisioningState** | `string` | ProvisioningState represents the asynchronous provisioning state of an ARM resource. Allowed values are: Succeeded, Failed, Canceled, Accepted, Deleting, Provisioning, and Updating. | N/A |
|  **ready** | `boolean` | Ready denotes that the AROMachinePool nodepool has joined the cluster | N/A |
|  **replicas** | `integer` | Replicas is the most recently observed number of replicas. | N/A |
|  **resources** | `array` | Resources represents the status of ASO resources managed by this AROMachinePool. This is populated when using the Resources field in the spec. | N/A |
| └>&nbsp;&nbsp; **ready** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **resource** | `object` | StatusResource is a handle to a resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | No description provided. | N/A |
|  **version** | `string` | ARO-HCP OpenShift version X.Y (without Z-stream), for example "4.20". | N/A |
