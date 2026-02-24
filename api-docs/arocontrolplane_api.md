# AROControlPlane API

AROControlPlane is the Schema for the AROControlPlanes API.

## Spec Fields

AROControlPlaneSpec defines the desired state of AROControlPlane.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **azureEnvironment** | `string` | AzureEnvironment is the name of the AzureCloud to be used. The default value that would be used by most users is "AzurePublicCloud", other values are: - ChinaCloud: "AzureChinaCloud" - PublicCloud: "AzurePublicCloud" - USGovernmentCloud: "AzureUSGovernmentCloud" Note that values other than the default must also be accompanied by corresponding changes to the aso-controller-settings Secret to configure ASO to refer to the non-Public cloud. ASO currently does not support referring to multiple different clouds in a single installation. The following fields must be defined in the Secret: - AZURE_AUTHORITY_HOST - AZURE_RESOURCE_MANAGER_ENDPOINT - AZURE_RESOURCE_MANAGER_AUDIENCE See the [ASO docs] for more details. [ASO docs]: https://azure.github.io/azure-service-operator/guide/aso-controller-settings-options/ | N/A |
|  **identityRef** | `object` | IdentityRef is a reference to an identity to be used when reconciling the aro control plane. If no identity is specified, the default identity for this controller will be used. | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| └>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| └>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
|  **resources** | `array` | Resources are embedded ASO resources to be managed by this AROControlPlane. This allows you to define the full infrastructure including HcpOpenShiftCluster and HcpOpenShiftClustersExternalAuth resources directly using ASO types. All cluster configuration (version, domain prefix, channel group, etc.) should be defined in the HcpOpenShiftCluster resource within this field. | N/A |
|  **subscriptionID** | `string` | SubscriptionID is the GUID of the Azure subscription that owns this cluster. Required for Azure API authentication and ARM resource ID construction. | N/A |
## Status Fields

AROControlPlaneStatus defines the observed state of AROControlPlane.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **apiURL** | `string` | APIURL is the url for the ARO-HCP openshift cluster api endPoint. | N/A |
|  **availableUpgrades** | `array` | Available upgrades for the ARO hosted control plane. | N/A |
|  **conditions** | `array` | Conditions specifies the conditions for the managed control plane | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **consoleURL** | `string` | ConsoleURL is the url for the openshift console. | N/A |
|  **failureMessage** | `string` | FailureMessage will be set in the event that there is a terminal problem reconciling the state and will be set to a descriptive error message. This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the spec or the configuration of the controller, and that manual intervention is required. | N/A |
|  **id** | `string` | ID is the cluster ID given by ARO. | N/A |
|  **initialization** | `object` | initialization provides observations of the AROControlPlane initialization process. NOTE: Fields in this struct are part of the Cluster API contract and are used to orchestrate initial Machine provisioning. | N/A |
| └>&nbsp;&nbsp; **controlPlaneInitialized** | `boolean` | controlPlaneInitialized is true when the AROControlPlane provider reports that the Kubernetes control plane is initialized; A control plane is considered initialized when it can accept requests, no matter if this happens before the control plane is fully provisioned or not. NOTE: this field is part of the Cluster API contract, and it is used to orchestrate initial Machine provisioning. | N/A |
|  **longRunningOperationStates** | `array` | LongRunningOperationStates saves the state for ARO long-running operations so they can be continued on the next reconciliation loop. | N/A |
| └>&nbsp;&nbsp; **data** | `string` | Data is the base64 url encoded json Azure AutoRest Future. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the Azure resource. Together with the service name, this forms the unique identifier for the future. | N/A |
| └>&nbsp;&nbsp; **resourceGroup** | `string` | ResourceGroup is the Azure resource group for the resource. | N/A |
| └>&nbsp;&nbsp; **serviceName** | `string` | ServiceName is the name of the Azure service. Together with the name of the resource, this forms the unique identifier for the future. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type describes the type of future, such as update, create, delete, etc. | N/A |
|  **ready** | `boolean` | Ready denotes that the AROControlPlane API Server is ready to receive requests. | N/A |
|  **resources** | `array` | Resources represents the status of ASO resources managed by this AROControlPlane. This is populated when using the Resources field in the spec. | N/A |
| └>&nbsp;&nbsp; **ready** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **resource** | `object` | StatusResource is a handle to a resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | No description provided. | N/A |
|  **version** | `string` | ARO-HCP OpenShift semantic version, for example "4.20.0". | N/A |
