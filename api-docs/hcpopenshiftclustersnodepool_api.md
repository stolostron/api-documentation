# HcpOpenShiftClustersNodePool API

Generator information:
- Generated from: /redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/hcpclusters/preview/2024-06-10-preview/openapi.json
- ARM URI: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RedHatOpenShift/hcpOpenShiftClusters/{hcpOpenShiftClusterName}/nodePools/{nodePoolName}

## Spec Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **azureName** | `string` | AzureName: The name of the resource in Azure. This is often the same as the name of the resource in Kubernetes but it doesn't have to be. | `Pattern=^[a-zA-Z][-a-zA-Z0-9]{1,13}[a-zA-Z0-9]$` |
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
|  **owner** | `object` | Owner: The owner of the resource. The owner controls where the resource goes when it is deployed. The owner also controls the resources lifecycle. When the owner is deleted the resource will also be deleted. Owner is expected to be a reference to a redhatopenshift.azure.com/HcpOpenShiftCluster resource | N/A |
| └>&nbsp;&nbsp; **armId** | `string` | No description provided. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| └>&nbsp;&nbsp; **name** | `string` | This is the name of the Kubernetes resource to reference. | N/A |
|  **properties** | `object` | Properties: The resource-specific properties for this resource. | N/A |
| └>&nbsp;&nbsp; **autoRepair** | `boolean` | AutoRepair: Auto-repair | N/A |
| └>&nbsp;&nbsp; **autoScaling** | `object` | AutoScaling: Representation of a autoscaling in a node pool. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **max** | `integer` | Max: The maximum number of nodes in the node pool | `Minimum=0` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **min** | `integer` | Min: The minimum number of nodes in the node pool | `Minimum=0` |
| └>&nbsp;&nbsp; **labels** | `array` | Labels: Kubernetes labels to propagate to the NodePool Nodes Note that when the labels are updated this is only applied to newly create nodes in the Nodepool, existing node labels remain unchanged. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key: The key of the label | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value: The value of the label | N/A |
| └>&nbsp;&nbsp; **nodeDrainTimeoutMinutes** | `integer` | NodeDrainTimeoutMinutes: nodeDrainTimeoutMinutes is the grace period for how long Pod Disruption Budget-protected workloads will be respected during any node draining operation. After this grace period, any workloads protected by Pod Disruption Budgets that have not been successfully drained from a node will be forcibly evicted. This is especially relevant to cluster upgrades. Valid values are from 0 to 10080 minutes (1 week) . 0 means that the NodePool can be drained without any time limitation. If unset the cluster nodeDrainTimeoutMinutes value is used as a default. | N/A |
| └>&nbsp;&nbsp; **platform** | `object` | Platform: Azure node pool platform configuration | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **availabilityZone** | `string` | AvailabilityZone: The availability zone for the node pool. Please read the documentation to see which regions support availability zones - https://learn.microsoft.com/en-us/azure/availability-zones/az-overview | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **enableEncryptionAtHost** | `boolean` | EnableEncryptionAtHost: Whether to enable host based OS and data drive encryption. - https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption#encryption-at-host---end-to-end-encryption-for-your-vm-data | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **osDisk** | `object` | OsDisk: The settings and configuration options for OSDisk | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **diskStorageAccountType** | `string` | DiskStorageAccountType: The type of the disk storage account - https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **encryptionSetReference** | `object` | EncryptionSetReference: The ID of the DiskEncryptionSet resource to use to encrypt the OS disks for the VMs. This needs to exist in the same subscription id listed in the Hosted Cluster, HostedCluster.Spec.Platform.Azure.SubscriptionID. DiskEncryptionSetID should also exist in a resource group under the same subscription id and the same location listed in the Hosted Cluster, HostedCluster.Spec.Platform.Azure.Location. Details on how to create a Disk Encryption Set can be found here: https://learn.microsoft.com/en-us/azure/virtual-machines/disks-enable-customer-managed-keys-portal#set-up-your-disk-encryption-set | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sizeGiB** | `integer` | SizeGiB: The OS disk size in GiB | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **subnetReference** | `object` | SubnetReference: The Azure resource ID of the worker subnet Note that a subnet cannot be reused between ARO-HCP Clusters, however the same subnet can be used for NodePools of the same cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vmSize** | `string` | VmSize: The VM size according to the documentation: - https://learn.microsoft.com/en-us/azure/virtual-machines/sizes | N/A |
| └>&nbsp;&nbsp; **replicas** | `integer` | Replicas: The number of worker nodes, it cannot be used together with autoscaling | N/A |
| └>&nbsp;&nbsp; **taints** | `array` | Taints: Taints for the nodes | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **effect** | `string` | Effect: The effect of the taint | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key: The key of the taint | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value: The value of the taint | N/A |
| └>&nbsp;&nbsp; **version** | `object` | Version: OpenShift version for the nodepool | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **channelGroup** | `string` | ChannelGroup: ChannelGroup is the name of the set to which this version belongs. Each version belongs to only a single set. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | Id: ID is the unique identifier of the version. | N/A |
|  **tags** | `object` | Tags: Resource tags. | N/A |
## Status Fields

No description available.

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
| └>&nbsp;&nbsp; **autoRepair** | `boolean` | AutoRepair: Auto-repair | N/A |
| └>&nbsp;&nbsp; **autoScaling** | `object` | AutoScaling: Representation of a autoscaling in a node pool. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **max** | `integer` | Max: The maximum number of nodes in the node pool | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **min** | `integer` | Min: The minimum number of nodes in the node pool | N/A |
| └>&nbsp;&nbsp; **labels** | `array` | Labels: Kubernetes labels to propagate to the NodePool Nodes Note that when the labels are updated this is only applied to newly create nodes in the Nodepool, existing node labels remain unchanged. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key: The key of the label | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value: The value of the label | N/A |
| └>&nbsp;&nbsp; **nodeDrainTimeoutMinutes** | `integer` | NodeDrainTimeoutMinutes: nodeDrainTimeoutMinutes is the grace period for how long Pod Disruption Budget-protected workloads will be respected during any node draining operation. After this grace period, any workloads protected by Pod Disruption Budgets that have not been successfully drained from a node will be forcibly evicted. This is especially relevant to cluster upgrades. Valid values are from 0 to 10080 minutes (1 week) . 0 means that the NodePool can be drained without any time limitation. If unset the cluster nodeDrainTimeoutMinutes value is used as a default. | N/A |
| └>&nbsp;&nbsp; **platform** | `object` | Platform: Azure node pool platform configuration | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **availabilityZone** | `string` | AvailabilityZone: The availability zone for the node pool. Please read the documentation to see which regions support availability zones - https://learn.microsoft.com/en-us/azure/availability-zones/az-overview | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **enableEncryptionAtHost** | `boolean` | EnableEncryptionAtHost: Whether to enable host based OS and data drive encryption. - https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption#encryption-at-host---end-to-end-encryption-for-your-vm-data | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **osDisk** | `object` | OsDisk: The settings and configuration options for OSDisk | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **diskStorageAccountType** | `string` | DiskStorageAccountType: The type of the disk storage account - https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **encryptionSetId** | `string` | EncryptionSetId: The ID of the DiskEncryptionSet resource to use to encrypt the OS disks for the VMs. This needs to exist in the same subscription id listed in the Hosted Cluster, HostedCluster.Spec.Platform.Azure.SubscriptionID. DiskEncryptionSetID should also exist in a resource group under the same subscription id and the same location listed in the Hosted Cluster, HostedCluster.Spec.Platform.Azure.Location. Details on how to create a Disk Encryption Set can be found here: https://learn.microsoft.com/en-us/azure/virtual-machines/disks-enable-customer-managed-keys-portal#set-up-your-disk-encryption-set | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sizeGiB** | `integer` | SizeGiB: The OS disk size in GiB | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **subnetId** | `string` | SubnetId: The Azure resource ID of the worker subnet Note that a subnet cannot be reused between ARO-HCP Clusters, however the same subnet can be used for NodePools of the same cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vmSize** | `string` | VmSize: The VM size according to the documentation: - https://learn.microsoft.com/en-us/azure/virtual-machines/sizes | N/A |
| └>&nbsp;&nbsp; **provisioningState** | `string` | ProvisioningState: Provisioning state | N/A |
| └>&nbsp;&nbsp; **replicas** | `integer` | Replicas: The number of worker nodes, it cannot be used together with autoscaling | N/A |
| └>&nbsp;&nbsp; **taints** | `array` | Taints: Taints for the nodes | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **effect** | `string` | Effect: The effect of the taint | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key: The key of the taint | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value: The value of the taint | N/A |
| └>&nbsp;&nbsp; **version** | `object` | Version: OpenShift version for the nodepool | N/A |
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
