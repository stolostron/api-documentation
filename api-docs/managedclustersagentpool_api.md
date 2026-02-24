# ManagedClustersAgentPool API

Generator information:
- Generated from: /containerservice/resource-manager/Microsoft.ContainerService/aks/stable/2021-05-01/managedClusters.json
- ARM URI: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/agentPools/{agentPoolName}

## Spec Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **availabilityZones** | `array` | AvailabilityZones: The list of Availability zones to use for nodes. This can only be specified if the AgentPoolType property is 'VirtualMachineScaleSets'. | N/A |
|  **azureName** | `string` | AzureName: The name of the resource in Azure. This is often the same as the name of the resource in Kubernetes but it doesn't have to be. | N/A |
|  **count** | `integer` | Count: Number of agents (VMs) to host docker containers. Allowed values must be in the range of 0 to 1000 (inclusive) for user pools and in the range of 1 to 1000 (inclusive) for system pools. The default value is 1. | N/A |
|  **enableAutoScaling** | `boolean` | EnableAutoScaling: Whether to enable auto-scaler | N/A |
|  **enableEncryptionAtHost** | `boolean` | EnableEncryptionAtHost: This is only supported on certain VM sizes and in certain Azure regions. For more information, see: https://docs.microsoft.com/azure/aks/enable-host-encryption | N/A |
|  **enableFIPS** | `boolean` | EnableFIPS: See [Add a FIPS-enabled node pool](https://docs.microsoft.com/azure/aks/use-multiple-node-pools#add-a-fips-enabled-node-pool-preview) for more details. | N/A |
|  **enableNodePublicIP** | `boolean` | EnableNodePublicIP: Some scenarios may require nodes in a node pool to receive their own dedicated public IP addresses. A common scenario is for gaming workloads, where a console needs to make a direct connection to a cloud virtual machine to minimize hops. For more information see [assigning a public IP per node](https://docs.microsoft.com/azure/aks/use-multiple-node-pools#assign-a-public-ip-per-node-for-your-node-pools). The default is false. | N/A |
|  **enableUltraSSD** | `boolean` | EnableUltraSSD: Whether to enable UltraSSD | N/A |
|  **gpuInstanceProfile** | `string` | GpuInstanceProfile: GPUInstanceProfile to be used to specify GPU MIG instance profile for supported GPU VM SKU. | N/A |
|  **kubeletConfig** | `object` | KubeletConfig: The Kubelet configuration on the agent pool nodes. | N/A |
| └>&nbsp;&nbsp; **allowedUnsafeSysctls** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **containerLogMaxFiles** | `integer` | No description provided. | `Minimum=2` |
| └>&nbsp;&nbsp; **containerLogMaxSizeMB** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **cpuCfsQuota** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **cpuCfsQuotaPeriod** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **cpuManagerPolicy** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **failSwapOn** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **imageGcHighThreshold** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **imageGcLowThreshold** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **podMaxPids** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **topologyManagerPolicy** | `string` | No description provided. | N/A |
|  **kubeletDiskType** | `string` | KubeletDiskType: Determines the placement of emptyDir volumes, container runtime data root, and Kubelet ephemeral storage. | N/A |
|  **linuxOSConfig** | `object` | LinuxOSConfig: The OS configuration of Linux agent nodes. | N/A |
| └>&nbsp;&nbsp; **swapFileSizeMB** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **sysctls** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fsAioMaxNr** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fsFileMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fsInotifyMaxUserWatches** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fsNrOpen** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kernelThreadsMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreNetdevMaxBacklog** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreOptmemMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreRmemDefault** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreRmemMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreSomaxconn** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreWmemDefault** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreWmemMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4IpLocalPortRange** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4NeighDefaultGcThresh1** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4NeighDefaultGcThresh2** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4NeighDefaultGcThresh3** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpFinTimeout** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpKeepaliveProbes** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpKeepaliveTime** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpMaxSynBacklog** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpMaxTwBuckets** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpTwReuse** | `boolean` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpkeepaliveIntvl** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netNetfilterNfConntrackBuckets** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netNetfilterNfConntrackMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vmMaxMapCount** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vmSwappiness** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vmVfsCachePressure** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **transparentHugePageDefrag** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **transparentHugePageEnabled** | `string` | No description provided. | N/A |
|  **maxCount** | `integer` | MaxCount: The maximum number of nodes for auto-scaling | N/A |
|  **maxPods** | `integer` | MaxPods: The maximum number of pods that can run on a node. | N/A |
|  **minCount** | `integer` | MinCount: The minimum number of nodes for auto-scaling | N/A |
|  **mode** | `string` | Mode: A cluster must have at least one 'System' Agent Pool at all times. For additional information on agent pool restrictions  and best practices, see: https://docs.microsoft.com/azure/aks/use-system-pools | N/A |
|  **nodeLabels** | `object` | NodeLabels: The node labels to be persisted across all nodes in agent pool. | N/A |
|  **nodePublicIPPrefixIDReference** | `object` | NodePublicIPPrefixIDReference: This is of the form: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes/{publicIPPrefixName} | N/A |
| └>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| └>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
|  **nodeTaints** | `array` | NodeTaints: The taints added to new nodes during node pool create and scale. For example, key=value:NoSchedule. | N/A |
|  **operatorSpec** | `object` | OperatorSpec: The specification for configuring operator behavior. This field is interpreted by the operator and not passed directly to Azure | N/A |
| └>&nbsp;&nbsp; **configMapExpressions** | `array` | ConfigMapExpressions: configures where to place operator written dynamic ConfigMaps (created with CEL expressions). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the ConfigMap or Secret being written to. If the CEL expression in Value returns a string this is required to identify what key to write to. If the CEL expression in Value returns a map[string]string Key must not be set, instead the keys written will be determined dynamically based on the keys of the resulting map[string]string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap or secret to write to. The configmap or secret will be created in the same namespace as the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is a CEL expression. The CEL expression may return a string or a map[string]string. For more information on CEL in ASO see https://azure.github.io/azure-service-operator/guide/expressions/ | N/A |
| └>&nbsp;&nbsp; **secretExpressions** | `array` | SecretExpressions: configures where to place operator written dynamic secrets (created with CEL expressions). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the ConfigMap or Secret being written to. If the CEL expression in Value returns a string this is required to identify what key to write to. If the CEL expression in Value returns a map[string]string Key must not be set, instead the keys written will be determined dynamically based on the keys of the resulting map[string]string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes configmap or secret to write to. The configmap or secret will be created in the same namespace as the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is a CEL expression. The CEL expression may return a string or a map[string]string. For more information on CEL in ASO see https://azure.github.io/azure-service-operator/guide/expressions/ | N/A |
|  **orchestratorVersion** | `string` | OrchestratorVersion: As a best practice, you should upgrade all node pools in an AKS cluster to the same Kubernetes version. The node pool version must have the same major version as the control plane. The node pool minor version must be within two minor versions of the control plane version. The node pool version cannot be greater than the control plane version. For more information see [upgrading a node pool](https://docs.microsoft.com/azure/aks/use-multiple-node-pools#upgrade-a-node-pool). | N/A |
|  **osDiskSizeGB** | `integer` | No description provided. | `Minimum=0`<br>`Maximum=2048` |
|  **osDiskType** | `string` | OsDiskType: The default is 'Ephemeral' if the VM supports it and has a cache disk larger than the requested OSDiskSizeGB. Otherwise,  defaults to 'Managed'. May not be changed after creation. For more information see [Ephemeral OS](https://docs.microsoft.com/azure/aks/cluster-configuration#ephemeral-os). | N/A |
|  **osSKU** | `string` | OsSKU: Specifies an OS SKU. This value must not be specified if OSType is Windows. | N/A |
|  **osType** | `string` | OsType: The operating system type. The default is Linux. | N/A |
|  **owner** | `object` | Owner: The owner of the resource. The owner controls where the resource goes when it is deployed. The owner also controls the resources lifecycle. When the owner is deleted the resource will also be deleted. Owner is expected to be a reference to a containerservice.azure.com/ManagedCluster resource | N/A |
| └>&nbsp;&nbsp; **armId** | `string` | No description provided. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| └>&nbsp;&nbsp; **name** | `string` | This is the name of the Kubernetes resource to reference. | N/A |
|  **podSubnetIDReference** | `object` | PodSubnetIDReference: If omitted, pod IPs are statically assigned on the node subnet (see vnetSubnetID for more details). This is of the form: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName} | N/A |
| └>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| └>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
|  **proximityPlacementGroupID** | `string` | ProximityPlacementGroupID: The ID for Proximity Placement Group. | N/A |
|  **scaleSetEvictionPolicy** | `string` | ScaleSetEvictionPolicy: This cannot be specified unless the scaleSetPriority is 'Spot'. If not specified, the default is 'Delete'. | N/A |
|  **scaleSetPriority** | `string` | ScaleSetPriority: The Virtual Machine Scale Set priority. If not specified, the default is 'Regular'. | N/A |
|  **spotMaxPrice** | `number` | SpotMaxPrice: Possible values are any decimal value greater than zero or -1 which indicates the willingness to pay any on-demand price. For more details on spot pricing, see [spot VMs pricing](https://docs.microsoft.com/azure/virtual-machines/spot-vms#pricing) | N/A |
|  **tags** | `object` | Tags: The tags to be persisted on the agent pool virtual machine scale set. | N/A |
|  **type** | `string` | Type: The type of Agent Pool. | N/A |
|  **upgradeSettings** | `object` | UpgradeSettings: Settings for upgrading the agentpool | N/A |
| └>&nbsp;&nbsp; **maxSurge** | `string` | No description provided. | N/A |
|  **vmSize** | `string` | VmSize: VM size availability varies by region. If a node contains insufficient compute resources (memory, cpu, etc) pods might fail to run correctly. For more details on restricted VM sizes, see: https://docs.microsoft.com/azure/aks/quotas-skus-regions | N/A |
|  **vnetSubnetIDReference** | `object` | VnetSubnetIDReference: If this is not specified, a VNET and subnet will be generated and used. If no podSubnetID is specified, this applies to nodes and pods, otherwise it applies to just nodes. This is of the form: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName} | N/A |
| └>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| └>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
## Status Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **availabilityZones** | `array` | AvailabilityZones: The list of Availability zones to use for nodes. This can only be specified if the AgentPoolType property is 'VirtualMachineScaleSets'. | N/A |
|  **conditions** | `array` | Conditions: The observed state of the resource | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the last time the condition transitioned from one status to another. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | ObservedGeneration is the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.condition[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason for the condition's last transition. Reasons are upper CamelCase (PascalCase) with no spaces. A reason is always provided, this field will not be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | Severity with which to treat failures of this type of condition. For conditions which have positive polarity (Status == True is their normal/healthy state), this will be omitted when Status == True For conditions which have negative polarity (Status == False is their normal/healthy state), this will be omitted when Status == False. This is omitted in all cases when Status == Unknown | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status of the condition, one of True, False, or Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type of condition. | N/A |
|  **count** | `integer` | Count: Number of agents (VMs) to host docker containers. Allowed values must be in the range of 0 to 1000 (inclusive) for user pools and in the range of 1 to 1000 (inclusive) for system pools. The default value is 1. | N/A |
|  **enableAutoScaling** | `boolean` | EnableAutoScaling: Whether to enable auto-scaler | N/A |
|  **enableEncryptionAtHost** | `boolean` | EnableEncryptionAtHost: This is only supported on certain VM sizes and in certain Azure regions. For more information, see: https://docs.microsoft.com/azure/aks/enable-host-encryption | N/A |
|  **enableFIPS** | `boolean` | EnableFIPS: See [Add a FIPS-enabled node pool](https://docs.microsoft.com/azure/aks/use-multiple-node-pools#add-a-fips-enabled-node-pool-preview) for more details. | N/A |
|  **enableNodePublicIP** | `boolean` | EnableNodePublicIP: Some scenarios may require nodes in a node pool to receive their own dedicated public IP addresses. A common scenario is for gaming workloads, where a console needs to make a direct connection to a cloud virtual machine to minimize hops. For more information see [assigning a public IP per node](https://docs.microsoft.com/azure/aks/use-multiple-node-pools#assign-a-public-ip-per-node-for-your-node-pools). The default is false. | N/A |
|  **enableUltraSSD** | `boolean` | EnableUltraSSD: Whether to enable UltraSSD | N/A |
|  **gpuInstanceProfile** | `string` | GpuInstanceProfile: GPUInstanceProfile to be used to specify GPU MIG instance profile for supported GPU VM SKU. | N/A |
|  **id** | `string` | Id: Resource ID. | N/A |
|  **kubeletConfig** | `object` | KubeletConfig: The Kubelet configuration on the agent pool nodes. | N/A |
| └>&nbsp;&nbsp; **allowedUnsafeSysctls** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **containerLogMaxFiles** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **containerLogMaxSizeMB** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **cpuCfsQuota** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **cpuCfsQuotaPeriod** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **cpuManagerPolicy** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **failSwapOn** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **imageGcHighThreshold** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **imageGcLowThreshold** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **podMaxPids** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **topologyManagerPolicy** | `string` | No description provided. | N/A |
|  **kubeletDiskType** | `string` | KubeletDiskType: Determines the placement of emptyDir volumes, container runtime data root, and Kubelet ephemeral storage. | N/A |
|  **linuxOSConfig** | `object` | LinuxOSConfig: The OS configuration of Linux agent nodes. | N/A |
| └>&nbsp;&nbsp; **swapFileSizeMB** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **sysctls** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fsAioMaxNr** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fsFileMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fsInotifyMaxUserWatches** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fsNrOpen** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kernelThreadsMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreNetdevMaxBacklog** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreOptmemMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreRmemDefault** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreRmemMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreSomaxconn** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreWmemDefault** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreWmemMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4IpLocalPortRange** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4NeighDefaultGcThresh1** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4NeighDefaultGcThresh2** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4NeighDefaultGcThresh3** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpFinTimeout** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpKeepaliveProbes** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpKeepaliveTime** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpMaxSynBacklog** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpMaxTwBuckets** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpTwReuse** | `boolean` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpkeepaliveIntvl** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netNetfilterNfConntrackBuckets** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netNetfilterNfConntrackMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vmMaxMapCount** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vmSwappiness** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vmVfsCachePressure** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **transparentHugePageDefrag** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **transparentHugePageEnabled** | `string` | No description provided. | N/A |
|  **maxCount** | `integer` | MaxCount: The maximum number of nodes for auto-scaling | N/A |
|  **maxPods** | `integer` | MaxPods: The maximum number of pods that can run on a node. | N/A |
|  **minCount** | `integer` | MinCount: The minimum number of nodes for auto-scaling | N/A |
|  **mode** | `string` | Mode: A cluster must have at least one 'System' Agent Pool at all times. For additional information on agent pool restrictions  and best practices, see: https://docs.microsoft.com/azure/aks/use-system-pools | N/A |
|  **name** | `string` | Name: The name of the resource that is unique within a resource group. This name can be used to access the resource. | N/A |
|  **nodeImageVersion** | `string` | NodeImageVersion: The version of node image | N/A |
|  **nodeLabels** | `object` | NodeLabels: The node labels to be persisted across all nodes in agent pool. | N/A |
|  **nodePublicIPPrefixID** | `string` | NodePublicIPPrefixID: This is of the form: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes/{publicIPPrefixName} | N/A |
|  **nodeTaints** | `array` | NodeTaints: The taints added to new nodes during node pool create and scale. For example, key=value:NoSchedule. | N/A |
|  **orchestratorVersion** | `string` | OrchestratorVersion: As a best practice, you should upgrade all node pools in an AKS cluster to the same Kubernetes version. The node pool version must have the same major version as the control plane. The node pool minor version must be within two minor versions of the control plane version. The node pool version cannot be greater than the control plane version. For more information see [upgrading a node pool](https://docs.microsoft.com/azure/aks/use-multiple-node-pools#upgrade-a-node-pool). | N/A |
|  **osDiskSizeGB** | `integer` | No description provided. | N/A |
|  **osDiskType** | `string` | OsDiskType: The default is 'Ephemeral' if the VM supports it and has a cache disk larger than the requested OSDiskSizeGB. Otherwise,  defaults to 'Managed'. May not be changed after creation. For more information see [Ephemeral OS](https://docs.microsoft.com/azure/aks/cluster-configuration#ephemeral-os). | N/A |
|  **osSKU** | `string` | OsSKU: Specifies an OS SKU. This value must not be specified if OSType is Windows. | N/A |
|  **osType** | `string` | OsType: The operating system type. The default is Linux. | N/A |
|  **podSubnetID** | `string` | PodSubnetID: If omitted, pod IPs are statically assigned on the node subnet (see vnetSubnetID for more details). This is of the form: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName} | N/A |
|  **powerState** | `object` | PowerState: Describes whether the Agent Pool is Running or Stopped | N/A |
| └>&nbsp;&nbsp; **code** | `string` | No description provided. | N/A |
|  **properties_type** | `string` | PropertiesType: The type of Agent Pool. | N/A |
|  **provisioningState** | `string` | ProvisioningState: The current deployment or provisioning state. | N/A |
|  **proximityPlacementGroupID** | `string` | ProximityPlacementGroupID: The ID for Proximity Placement Group. | N/A |
|  **scaleSetEvictionPolicy** | `string` | ScaleSetEvictionPolicy: This cannot be specified unless the scaleSetPriority is 'Spot'. If not specified, the default is 'Delete'. | N/A |
|  **scaleSetPriority** | `string` | ScaleSetPriority: The Virtual Machine Scale Set priority. If not specified, the default is 'Regular'. | N/A |
|  **spotMaxPrice** | `number` | SpotMaxPrice: Possible values are any decimal value greater than zero or -1 which indicates the willingness to pay any on-demand price. For more details on spot pricing, see [spot VMs pricing](https://docs.microsoft.com/azure/virtual-machines/spot-vms#pricing) | N/A |
|  **tags** | `object` | Tags: The tags to be persisted on the agent pool virtual machine scale set. | N/A |
|  **type** | `string` | Type: Resource type | N/A |
|  **upgradeSettings** | `object` | UpgradeSettings: Settings for upgrading the agentpool | N/A |
| └>&nbsp;&nbsp; **maxSurge** | `string` | No description provided. | N/A |
|  **vmSize** | `string` | VmSize: VM size availability varies by region. If a node contains insufficient compute resources (memory, cpu, etc) pods might fail to run correctly. For more details on restricted VM sizes, see: https://docs.microsoft.com/azure/aks/quotas-skus-regions | N/A |
|  **vnetSubnetID** | `string` | VnetSubnetID: If this is not specified, a VNET and subnet will be generated and used. If no podSubnetID is specified, this applies to nodes and pods, otherwise it applies to just nodes. This is of the form: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName} | N/A |
