# HcpOpenShiftCluster API

Generator information:
- Generated from: /redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/hcpclusters/preview/2024-06-10-preview/openapi.json
- ARM URI: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RedHatOpenShift/hcpOpenShiftClusters/{hcpOpenShiftClusterName}

## Spec Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **azureName** | `string` | AzureName: The name of the resource in Azure. This is often the same as the name of the resource in Kubernetes but it doesn't have to be. | `Pattern=^[a-zA-Z][-a-zA-Z0-9]{1,52}[a-zA-Z0-9]$` |
|  **identity** | `object` | Identity: The managed service identities assigned to this resource. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type: Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed). | N/A |
| └>&nbsp;&nbsp; **userAssignedIdentities** | `array` | UserAssignedIdentities: The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **reference** | `object` | ResourceReference represents a resource reference, either to a Kubernetes resource or directly to an Azure resource via ARMID | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
|  **location** | `string` | Location: The geo-location where the resource lives | N/A |
|  **operatorSpec** | `object` | OperatorSpec: The specification for configuring operator behavior. This field is interpreted by the operator and not passed directly to Azure | N/A |
| └>&nbsp;&nbsp; **configMapExpressions** | `array` | ConfigMapExpressions: configures where to place operator written dynamic ConfigMaps (created with CEL expressions). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the ConfigMap or Secret being written to. If the CEL expression in Value returns a string this is required to identify what key to write to. If the CEL expression in Value returns a map[string]string Key must not be set, instead the keys written will be determined dynamically based on the keys of the resulting map[string]string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap or secret to write to. The configmap or secret will be created in the same namespace as the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is a CEL expression. The CEL expression may return a string or a map[string]string. For more information on CEL in ASO see https://azure.github.io/azure-service-operator/guide/expressions/ | N/A |
| └>&nbsp;&nbsp; **secretExpressions** | `array` | SecretExpressions: configures where to place operator written dynamic secrets (created with CEL expressions). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the ConfigMap or Secret being written to. If the CEL expression in Value returns a string this is required to identify what key to write to. If the CEL expression in Value returns a map[string]string Key must not be set, instead the keys written will be determined dynamically based on the keys of the resulting map[string]string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap or secret to write to. The configmap or secret will be created in the same namespace as the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is a CEL expression. The CEL expression may return a string or a map[string]string. For more information on CEL in ASO see https://azure.github.io/azure-service-operator/guide/expressions/ | N/A |
| └>&nbsp;&nbsp; **secrets** | `object` | Secrets: configures where to place Azure generated secrets. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **adminCredentials** | `object` | AdminCredentials: indicates where the AdminCredentials secret should be placed. If omitted, the secret will not be retrieved from Azure. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the Kubernetes secret being referenced. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes secret to write to. The secret will be created in the same namespace as the resource. | N/A |
|  **owner** | `object` | Owner: The owner of the resource. The owner controls where the resource goes when it is deployed. The owner also controls the resources lifecycle. When the owner is deleted the resource will also be deleted. Owner is expected to be a reference to a resources.azure.com/ResourceGroup resource | N/A |
| └>&nbsp;&nbsp; **armId** | `string` | No description provided. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| └>&nbsp;&nbsp; **name** | `string` | This is the name of the Kubernetes resource to reference. | N/A |
|  **properties** | `object` | Properties: The resource-specific properties for this resource. | N/A |
| └>&nbsp;&nbsp; **api** | `object` | Api: Shows the cluster API server profile | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **authorizedCidrs** | `array` | AuthorizedCidrs: The list of authorized IPv4 CIDR blocks allowed to access the API server. Maximum 500 entries. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **visibility** | `string` | Visibility: The internet visibility of the OpenShift API server | N/A |
| └>&nbsp;&nbsp; **autoscaling** | `object` | Autoscaling: Configure ClusterAutoscaling . | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **maxNodeProvisionTimeSeconds** | `integer` | MaxNodeProvisionTimeSeconds: maxNodeProvisionTimeSeconds is the maximum time to wait for node provisioning before considering the provisioning to be unsuccessful. The default is 900 seconds, or 15 minutes. | `Minimum=0` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **maxNodesTotal** | `integer` | MaxNodesTotal: maxNodesTotal is the maximum allowable number of nodes for the Autoscaler scale out to be operational. The autoscaler will not grow the cluster beyond this number. If omitted, the autoscaler will not have a maximum limit. | `Minimum=0` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **maxPodGracePeriodSeconds** | `integer` | MaxPodGracePeriodSeconds: maxPodGracePeriod is the maximum seconds to wait for graceful pod termination before scaling down a NodePool. The default is 600 seconds. | `Minimum=0` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **podPriorityThreshold** | `integer` | PodPriorityThreshold: podPriorityThreshold enables users to schedule “best-effort” pods, which shouldn’t trigger autoscaler actions, but only run when there are spare resources available. The default is -10. See the following for more details: https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-does-cluster-autoscaler-work-with-pod-priority-and-preemption | N/A |
| └>&nbsp;&nbsp; **clusterImageRegistry** | `object` | ClusterImageRegistry: OpenShift internal image registry | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **state** | `string` | State: state indicates the desired ImageStream-backed cluster image registry installation mode. This can only be set during cluster creation and cannot be changed after cluster creation. Enabled means the ImageStream-backed image registry will be run as pods on worker nodes in the cluster. Disabled means the ImageStream-backed image registry will not be present in the cluster. The default is Enabled. | N/A |
| └>&nbsp;&nbsp; **dns** | `object` | Dns: Cluster DNS configuration | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **baseDomainPrefix** | `string` | BaseDomainPrefix: BaseDomainPrefix is the unique name of the cluster representing the OpenShift's cluster name. BaseDomainPrefix is the name that will appear in the cluster's DNS, provisioned cloud providers resources | `Pattern=^[a-z]([-a-z0-9]*[a-z0-9])?$` |
| └>&nbsp;&nbsp; **etcd** | `object` | Etcd: Configure ETCD. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dataEncryption** | `object` | DataEncryption: ETCD Data Encryption settings. If not specified platform managed keys are used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **customerManaged** | `object` | CustomerManaged: Specify customer managed encryption key details. Required when keyManagementMode is "CustomerManaged". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **encryptionType** | `string` | EncryptionType: The encryption type used. By default, "KMS" is used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kms** | `object` | Kms: The Key Management Service (KMS) encryption key details. Required when encryptionType is "KMS". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **activeKey** | `object` | ActiveKey: The details of the active key. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name: name is the name of the keyvault key used for encryption/decryption. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vaultName** | `string` | VaultName: vaultName is the name of the keyvault that contains the secret. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | Version: version contains the version of the key to use. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **keyManagementMode** | `string` | KeyManagementMode: Specify the key management strategy used for the encryption key that encrypts the ETCD data. By default, "PlatformManaged" is used. | N/A |
| └>&nbsp;&nbsp; **network** | `object` | Network: Cluster network configuration | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **hostPrefix** | `integer` | HostPrefix: Network host prefix | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **machineCidr** | `string` | MachineCidr: The CIDR block from which to assign machine IP addresses | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **networkType** | `string` | NetworkType: The main controller responsible for rendering the core networking components | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **podCidr** | `string` | PodCidr: The CIDR of the pod IP addresses | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serviceCidr** | `string` | ServiceCidr: The CIDR block for assigned service IPs | N/A |
| └>&nbsp;&nbsp; **nodeDrainTimeoutMinutes** | `integer` | NodeDrainTimeoutMinutes: nodeDrainTimeoutMinutes is the grace period for how long Pod Disruption Budget-protected workloads will be respected during any node draining operation. After this grace period, any workloads protected by Pod Disruption Budgets that have not been successfully drained from a node will be forcibly evicted. This is especially relevant to cluster upgrades. Valid values are in minutes and from 0 to 10080 minutes (1 week). 0 means that the MachinePool can be drained without any time limitation. This is the value is used a default for all NodePools. It can be overridden by specifying nodeDrainTimeoutMinutes for a given NodePool | `Minimum=0`<br>`Maximum=10080` |
| └>&nbsp;&nbsp; **platform** | `object` | Platform: Azure platform configuration | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **managedResourceGroup** | `string` | ManagedResourceGroup: Resource group to put cluster resources | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **networkSecurityGroupReference** | `object` | NetworkSecurityGroupReference: ResourceId for the NSG (network security group) attached to the cluster subnet Note that NSGs cannot be reused for other ARO-HCP clusters. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operatorsAuthentication** | `object` | OperatorsAuthentication: The configuration that the operators of the cluster have to authenticate to Azure | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **userAssignedIdentities** | `object` | UserAssignedIdentities: Represents the information related to Azure User-Assigned managed identities needed to perform Operators authentication based on Azure User-Assigned Managed Identities | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **controlPlaneOperatorsReferences** | `object` | ControlPlaneOperatorsReferences: The set of Azure User-Assigned Managed Identities leveraged for the Control Plane operators of the cluster. The set of required managed identities is dependent on the Cluster's OpenShift version. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dataPlaneOperatorsReferences** | `object` | DataPlaneOperatorsReferences: The set of Azure User-Assigned Managed Identities leveraged for the Data Plane operators of the cluster. The set of required managed identities is dependent on the Cluster's OpenShift version. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serviceManagedIdentityReference** | `object` | ServiceManagedIdentityReference: Represents the information associated to an Azure User-Assigned Managed Identity whose purpose is to perform service level actions. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **outboundType** | `string` | OutboundType: The core outgoing configuration | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **subnetReference** | `object` | SubnetReference: The Azure resource ID of the worker subnet Note that a subnet cannot be reused between ARO-HCP Clusters. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
| └>&nbsp;&nbsp; **version** | `object` | Version: Version of the control plane components | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **channelGroup** | `string` | ChannelGroup: ChannelGroup is the name of the set to which this version belongs. Each version belongs to only a single set. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | Id: ID is the unique identifier of the version. | N/A |
|  **tags** | `object` | Tags: Resource tags. | N/A |
## Status Fields

HCP cluster resource

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions: The observed state of the resource | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the last time the condition transitioned from one status to another. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | ObservedGeneration is the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.condition[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason for the condition's last transition. Reasons are upper CamelCase (PascalCase) with no spaces. A reason is always provided, this field will not be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | Severity with which to treat failures of this type of condition. For conditions which have positive polarity (Status == True is their normal/healthy state), this will be omitted when Status == True For conditions which have negative polarity (Status == False is their normal/healthy state), this will be omitted when Status == False. This is omitted in all cases when Status == Unknown | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status of the condition, one of True, False, or Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type of condition. | N/A |
|  **id** | `string` | Id: Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" | N/A |
|  **identity** | `object` | Identity: The managed service identities assigned to this resource. | N/A |
| └>&nbsp;&nbsp; **principalId** | `string` | PrincipalId: The service principal ID of the system assigned identity. This property will only be provided for a system assigned identity. | N/A |
| └>&nbsp;&nbsp; **tenantId** | `string` | TenantId: The tenant ID of the system assigned identity. This property will only be provided for a system assigned identity. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type: Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed). | N/A |
| └>&nbsp;&nbsp; **userAssignedIdentities** | `object` | UserAssignedIdentities: The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests. | N/A |
|  **location** | `string` | Location: The geo-location where the resource lives | N/A |
|  **name** | `string` | Name: The name of the resource | N/A |
|  **properties** | `object` | Properties: The resource-specific properties for this resource. | N/A |
| └>&nbsp;&nbsp; **api** | `object` | Api: Shows the cluster API server profile | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **authorizedCidrs** | `array` | AuthorizedCidrs: The list of authorized IPv4 CIDR blocks allowed to access the API server. Maximum 500 entries. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **url** | `string` | Url: URL endpoint for the API server | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **visibility** | `string` | Visibility: The internet visibility of the OpenShift API server | N/A |
| └>&nbsp;&nbsp; **autoscaling** | `object` | Autoscaling: Configure ClusterAutoscaling . | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **maxNodeProvisionTimeSeconds** | `integer` | MaxNodeProvisionTimeSeconds: maxNodeProvisionTimeSeconds is the maximum time to wait for node provisioning before considering the provisioning to be unsuccessful. The default is 900 seconds, or 15 minutes. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **maxNodesTotal** | `integer` | MaxNodesTotal: maxNodesTotal is the maximum allowable number of nodes for the Autoscaler scale out to be operational. The autoscaler will not grow the cluster beyond this number. If omitted, the autoscaler will not have a maximum limit. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **maxPodGracePeriodSeconds** | `integer` | MaxPodGracePeriodSeconds: maxPodGracePeriod is the maximum seconds to wait for graceful pod termination before scaling down a NodePool. The default is 600 seconds. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **podPriorityThreshold** | `integer` | PodPriorityThreshold: podPriorityThreshold enables users to schedule “best-effort” pods, which shouldn’t trigger autoscaler actions, but only run when there are spare resources available. The default is -10. See the following for more details: https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-does-cluster-autoscaler-work-with-pod-priority-and-preemption | N/A |
| └>&nbsp;&nbsp; **clusterImageRegistry** | `object` | ClusterImageRegistry: OpenShift internal image registry | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **state** | `string` | State: state indicates the desired ImageStream-backed cluster image registry installation mode. This can only be set during cluster creation and cannot be changed after cluster creation. Enabled means the ImageStream-backed image registry will be run as pods on worker nodes in the cluster. Disabled means the ImageStream-backed image registry will not be present in the cluster. The default is Enabled. | N/A |
| └>&nbsp;&nbsp; **console** | `object` | Console: Shows the cluster web console information | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **url** | `string` | Url: The cluster web console URL endpoint | N/A |
| └>&nbsp;&nbsp; **dns** | `object` | Dns: Cluster DNS configuration | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **baseDomain** | `string` | BaseDomain: BaseDomain is the base DNS domain of the cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **baseDomainPrefix** | `string` | BaseDomainPrefix: BaseDomainPrefix is the unique name of the cluster representing the OpenShift's cluster name. BaseDomainPrefix is the name that will appear in the cluster's DNS, provisioned cloud providers resources | N/A |
| └>&nbsp;&nbsp; **etcd** | `object` | Etcd: Configure ETCD. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dataEncryption** | `object` | DataEncryption: ETCD Data Encryption settings. If not specified platform managed keys are used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **customerManaged** | `object` | CustomerManaged: Specify customer managed encryption key details. Required when keyManagementMode is "CustomerManaged". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **encryptionType** | `string` | EncryptionType: The encryption type used. By default, "KMS" is used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kms** | `object` | Kms: The Key Management Service (KMS) encryption key details. Required when encryptionType is "KMS". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **activeKey** | `object` | ActiveKey: The details of the active key. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name: name is the name of the keyvault key used for encryption/decryption. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vaultName** | `string` | VaultName: vaultName is the name of the keyvault that contains the secret. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | Version: version contains the version of the key to use. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **keyManagementMode** | `string` | KeyManagementMode: Specify the key management strategy used for the encryption key that encrypts the ETCD data. By default, "PlatformManaged" is used. | N/A |
| └>&nbsp;&nbsp; **network** | `object` | Network: Cluster network configuration | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **hostPrefix** | `integer` | HostPrefix: Network host prefix | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **machineCidr** | `string` | MachineCidr: The CIDR block from which to assign machine IP addresses | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **networkType** | `string` | NetworkType: The main controller responsible for rendering the core networking components | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **podCidr** | `string` | PodCidr: The CIDR of the pod IP addresses | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serviceCidr** | `string` | ServiceCidr: The CIDR block for assigned service IPs | N/A |
| └>&nbsp;&nbsp; **nodeDrainTimeoutMinutes** | `integer` | NodeDrainTimeoutMinutes: nodeDrainTimeoutMinutes is the grace period for how long Pod Disruption Budget-protected workloads will be respected during any node draining operation. After this grace period, any workloads protected by Pod Disruption Budgets that have not been successfully drained from a node will be forcibly evicted. This is especially relevant to cluster upgrades. Valid values are in minutes and from 0 to 10080 minutes (1 week). 0 means that the MachinePool can be drained without any time limitation. This is the value is used a default for all NodePools. It can be overridden by specifying nodeDrainTimeoutMinutes for a given NodePool | N/A |
| └>&nbsp;&nbsp; **platform** | `object` | Platform: Azure platform configuration | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **issuerUrl** | `string` | IssuerUrl: URL for the OIDC provider to be used for authentication to authenticate against user Azure cloud account | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **managedResourceGroup** | `string` | ManagedResourceGroup: Resource group to put cluster resources | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **networkSecurityGroupId** | `string` | NetworkSecurityGroupId: ResourceId for the NSG (network security group) attached to the cluster subnet Note that NSGs cannot be reused for other ARO-HCP clusters. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operatorsAuthentication** | `object` | OperatorsAuthentication: The configuration that the operators of the cluster have to authenticate to Azure | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **userAssignedIdentities** | `object` | UserAssignedIdentities: Represents the information related to Azure User-Assigned managed identities needed to perform Operators authentication based on Azure User-Assigned Managed Identities | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **controlPlaneOperators** | `object` | ControlPlaneOperators: The set of Azure User-Assigned Managed Identities leveraged for the Control Plane operators of the cluster. The set of required managed identities is dependent on the Cluster's OpenShift version. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dataPlaneOperators** | `object` | DataPlaneOperators: The set of Azure User-Assigned Managed Identities leveraged for the Data Plane operators of the cluster. The set of required managed identities is dependent on the Cluster's OpenShift version. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serviceManagedIdentity** | `string` | ServiceManagedIdentity: Represents the information associated to an Azure User-Assigned Managed Identity whose purpose is to perform service level actions. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **outboundType** | `string` | OutboundType: The core outgoing configuration | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **subnetId** | `string` | SubnetId: The Azure resource ID of the worker subnet Note that a subnet cannot be reused between ARO-HCP Clusters. | N/A |
| └>&nbsp;&nbsp; **provisioningState** | `string` | ProvisioningState: The status of the last operation. | N/A |
| └>&nbsp;&nbsp; **version** | `object` | Version: Version of the control plane components | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **channelGroup** | `string` | ChannelGroup: ChannelGroup is the name of the set to which this version belongs. Each version belongs to only a single set. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | Id: ID is the unique identifier of the version. | N/A |
|  **systemData** | `object` | SystemData: Azure Resource Manager metadata containing createdBy and modifiedBy information. | N/A |
| └>&nbsp;&nbsp; **createdAt** | `string` | CreatedAt: The timestamp of resource creation (UTC). | N/A |
| └>&nbsp;&nbsp; **createdBy** | `string` | CreatedBy: The identity that created the resource. | N/A |
| └>&nbsp;&nbsp; **createdByType** | `string` | CreatedByType: The type of identity that created the resource. | N/A |
| └>&nbsp;&nbsp; **lastModifiedAt** | `string` | LastModifiedAt: The timestamp of resource last modification (UTC) | N/A |
| └>&nbsp;&nbsp; **lastModifiedBy** | `string` | LastModifiedBy: The identity that last modified the resource. | N/A |
| └>&nbsp;&nbsp; **lastModifiedByType** | `string` | LastModifiedByType: The type of identity that last modified the resource. | N/A |
|  **tags** | `object` | Tags: Resource tags. | N/A |
|  **type** | `string` | Type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" | N/A |
