# AzureMachinePoolMachine API

AzureMachinePoolMachine is the Schema for the azuremachinepoolmachines API.

## Spec Fields

AzureMachinePoolMachineSpec defines the desired state of AzureMachinePoolMachine.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **instanceID** | `string` | InstanceID is the identification of the Machine Instance within the VMSS | N/A |
|  **providerID** | `string` | ProviderID is the identification ID of the Virtual Machine Scale Set | N/A |
## Status Fields

AzureMachinePoolMachineStatus defines the observed state of AzureMachinePoolMachine.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions defines current service state of the AzureMachinePool. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | reason is the reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **failureMessage** | `string` | FailureMessage will be set in the event that there is a terminal problem reconciling the MachinePool and will contain a more verbose string suitable for logging and human consumption. Any transient errors that occur during the reconciliation of MachinePools can be added as events to the MachinePool object and/or logged in the controller's output. | N/A |
|  **failureReason** | `string` | FailureReason will be set in the event that there is a terminal problem reconciling the MachinePool machine and will contain a succinct value suitable for machine interpretation. Any transient errors that occur during the reconciliation of MachinePools can be added as events to the MachinePool object and/or logged in the controller's output. | N/A |
|  **instanceName** | `string` | InstanceName is the name of the Machine Instance within the VMSS | N/A |
|  **latestModelApplied** | `boolean` | LatestModelApplied indicates the instance is running the most up-to-date VMSS model. A VMSS model describes the image version the VM is running. If the instance is not running the latest model, it means the instance may not be running the version of Kubernetes the Machine Pool has specified and needs to be updated. | N/A |
|  **longRunningOperationStates** | `array` | LongRunningOperationStates saves the state for Azure long running operations so they can be continued on the next reconciliation loop. | N/A |
| └>&nbsp;&nbsp; **data** | `string` | Data is the base64 url encoded json Azure AutoRest Future. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the Azure resource. Together with the service name, this forms the unique identifier for the future. | N/A |
| └>&nbsp;&nbsp; **resourceGroup** | `string` | ResourceGroup is the Azure resource group for the resource. | N/A |
| └>&nbsp;&nbsp; **serviceName** | `string` | ServiceName is the name of the Azure service. Together with the name of the resource, this forms the unique identifier for the future. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type describes the type of future, such as update, create, delete, etc. | N/A |
|  **nodeRef** | `object` | NodeRef will point to the corresponding Node if it exists. | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| └>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| └>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
|  **provisioningState** | `string` | ProvisioningState is the provisioning state of the Azure virtual machine instance. | N/A |
|  **ready** | `boolean` | Ready is true when the provider resource is ready. | N/A |
|  **version** | `string` | Version defines the Kubernetes version for the VM Instance | N/A |
