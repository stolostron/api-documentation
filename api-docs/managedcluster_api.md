# ManagedCluster API

Description not found in CRD.

## Spec Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **aadProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **adminGroupObjectIDs** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **clientAppID** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enableAzureRBAC** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **managed** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **serverAppID** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **serverAppSecret** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **tenantID** | `string` | No description provided. | N/A |
|  **addonProfiles** | `object` | No description provided. | N/A |
|  **agentPoolProfiles** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **availabilityZones** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **count** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enableAutoScaling** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enableEncryptionAtHost** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enableFIPS** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enableNodePublicIP** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enableUltraSSD** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **gpuInstanceProfile** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **kubeletConfig** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **allowedUnsafeSysctls** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **containerLogMaxFiles** | `integer` | No description provided. | `Minimum=2` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **containerLogMaxSizeMB** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cpuCfsQuota** | `boolean` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cpuCfsQuotaPeriod** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cpuManagerPolicy** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **failSwapOn** | `boolean` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **imageGcHighThreshold** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **imageGcLowThreshold** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **podMaxPids** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **topologyManagerPolicy** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **kubeletDiskType** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **linuxOSConfig** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **swapFileSizeMB** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sysctls** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fsAioMaxNr** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fsFileMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fsInotifyMaxUserWatches** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fsNrOpen** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kernelThreadsMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreNetdevMaxBacklog** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreOptmemMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreRmemDefault** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreRmemMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreSomaxconn** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreWmemDefault** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreWmemMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4IpLocalPortRange** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4NeighDefaultGcThresh1** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4NeighDefaultGcThresh2** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4NeighDefaultGcThresh3** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpFinTimeout** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpKeepaliveProbes** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpKeepaliveTime** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpMaxSynBacklog** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpMaxTwBuckets** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpTwReuse** | `boolean` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpkeepaliveIntvl** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netNetfilterNfConntrackBuckets** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netNetfilterNfConntrackMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vmMaxMapCount** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vmSwappiness** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vmVfsCachePressure** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **transparentHugePageDefrag** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **transparentHugePageEnabled** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **maxCount** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **maxPods** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **minCount** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **mode** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | No description provided. | `Pattern=^[a-z][a-z0-9]{0,11}$` |
| └>&nbsp;&nbsp; **nodeLabels** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **nodePublicIPPrefixIDReference** | `object` | ResourceReference represents a resource reference, either to a Kubernetes resource or directly to an Azure resource via ARMID | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
| └>&nbsp;&nbsp; **nodeTaints** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **orchestratorVersion** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **osDiskSizeGB** | `integer` | No description provided. | `Minimum=0`<br>`Maximum=2048` |
| └>&nbsp;&nbsp; **osDiskType** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **osSKU** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **osType** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **podSubnetIDReference** | `object` | ResourceReference represents a resource reference, either to a Kubernetes resource or directly to an Azure resource via ARMID | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
| └>&nbsp;&nbsp; **proximityPlacementGroupID** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scaleSetEvictionPolicy** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scaleSetPriority** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **spotMaxPrice** | `number` | No description provided. | N/A |
| └>&nbsp;&nbsp; **tags** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **upgradeSettings** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **maxSurge** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **vmSize** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **vnetSubnetIDReference** | `object` | ResourceReference represents a resource reference, either to a Kubernetes resource or directly to an Azure resource via ARMID | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
|  **apiServerAccessProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **authorizedIPRanges** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enablePrivateCluster** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enablePrivateClusterPublicFQDN** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **privateDNSZone** | `string` | No description provided. | N/A |
|  **autoScalerProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **balance-similar-node-groups** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **expander** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **max-empty-bulk-delete** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **max-graceful-termination-sec** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **max-node-provision-time** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **max-total-unready-percentage** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **new-pod-scale-up-delay** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **ok-total-unready-count** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scale-down-delay-after-add** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scale-down-delay-after-delete** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scale-down-delay-after-failure** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scale-down-unneeded-time** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scale-down-unready-time** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scale-down-utilization-threshold** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scan-interval** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **skip-nodes-with-local-storage** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **skip-nodes-with-system-pods** | `string` | No description provided. | N/A |
|  **autoUpgradeProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **upgradeChannel** | `string` | No description provided. | N/A |
|  **azureName** | `string` | AzureName: The name of the resource in Azure. This is often the same as the name of the resource in Kubernetes but it doesn't have to be. | `Pattern=^[a-zA-Z0-9]$\|^[a-zA-Z0-9][-_a-zA-Z0-9]{0,61}[a-zA-Z0-9]$` |
|  **disableLocalAccounts** | `boolean` | No description provided. | N/A |
|  **diskEncryptionSetIDReference** | `object` | ResourceReference represents a resource reference, either to a Kubernetes resource or directly to an Azure resource via ARMID | N/A |
| └>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| └>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
|  **dnsPrefix** | `string` | No description provided. | N/A |
|  **enablePodSecurityPolicy** | `boolean` | No description provided. | N/A |
|  **enableRBAC** | `boolean` | No description provided. | N/A |
|  **extendedLocation** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | No description provided. | N/A |
|  **fqdnSubdomain** | `string` | No description provided. | N/A |
|  **httpProxyConfig** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **httpProxy** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **httpsProxy** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **noProxy** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **trustedCa** | `string` | No description provided. | N/A |
|  **identity** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **userAssignedIdentities** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **reference** | `object` | ResourceReference represents a resource reference, either to a Kubernetes resource or directly to an Azure resource via ARMID | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
|  **identityProfile** | `object` | No description provided. | N/A |
|  **kubernetesVersion** | `string` | No description provided. | N/A |
|  **linuxProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **adminUsername** | `string` | No description provided. | `Pattern=^[A-Za-z][-A-Za-z0-9_]*$` |
| └>&nbsp;&nbsp; **ssh** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **publicKeys** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **keyData** | `string` | No description provided. | N/A |
|  **location** | `string` | No description provided. | N/A |
|  **networkProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **dnsServiceIP** | `string` | No description provided. | `Pattern=^(?:(?:25[0-5]\|2[0-4][0-9]\|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]\|2[0-4][0-9]\|[01]?[0-9][0-9]?)$` |
| └>&nbsp;&nbsp; **dockerBridgeCidr** | `string` | No description provided. | `Pattern=^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]\|[1-2][0-9]\|3[0-2]))?$` |
| └>&nbsp;&nbsp; **loadBalancerProfile** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **allocatedOutboundPorts** | `integer` | No description provided. | `Minimum=0`<br>`Maximum=64000` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **effectiveOutboundIPs** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **reference** | `object` | ResourceReference represents a resource reference, either to a Kubernetes resource or directly to an Azure resource via ARMID | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **idleTimeoutInMinutes** | `integer` | No description provided. | `Minimum=4`<br>`Maximum=120` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **managedOutboundIPs** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **count** | `integer` | No description provided. | `Minimum=1`<br>`Maximum=100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **outboundIPPrefixes** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **publicIPPrefixes** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **reference** | `object` | ResourceReference represents a resource reference, either to a Kubernetes resource or directly to an Azure resource via ARMID | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **outboundIPs** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **publicIPs** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **reference** | `object` | ResourceReference represents a resource reference, either to a Kubernetes resource or directly to an Azure resource via ARMID | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
| └>&nbsp;&nbsp; **loadBalancerSku** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **networkMode** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **networkPlugin** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **networkPolicy** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **outboundType** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **podCidr** | `string` | No description provided. | `Pattern=^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]\|[1-2][0-9]\|3[0-2]))?$` |
| └>&nbsp;&nbsp; **serviceCidr** | `string` | No description provided. | `Pattern=^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]\|[1-2][0-9]\|3[0-2]))?$` |
|  **nodeResourceGroup** | `string` | No description provided. | N/A |
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
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **userCredentials** | `object` | UserCredentials: indicates where the UserCredentials secret should be placed. If omitted, the secret will not be retrieved from Azure. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the Kubernetes secret being referenced. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes secret to write to. The secret will be created in the same namespace as the resource. | N/A |
|  **owner** | `object` | Owner: The owner of the resource. The owner controls where the resource goes when it is deployed. The owner also controls the resources lifecycle. When the owner is deleted the resource will also be deleted. Owner is expected to be a reference to a resources.azure.com/ResourceGroup resource | N/A |
| └>&nbsp;&nbsp; **armId** | `string` | No description provided. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| └>&nbsp;&nbsp; **name** | `string` | This is the name of the Kubernetes resource to reference. | N/A |
|  **podIdentityProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **allowNetworkPluginKubenet** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enabled** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **userAssignedIdentities** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **bindingSelector** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **identity** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **clientId** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **objectId** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceReference** | `object` | ResourceReference represents a resource reference, either to a Kubernetes resource or directly to an Azure resource via ARMID | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **userAssignedIdentityExceptions** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **podLabels** | `object` | No description provided. | N/A |
|  **privateLinkResources** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **groupId** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **reference** | `object` | ResourceReference represents a resource reference, either to a Kubernetes resource or directly to an Azure resource via ARMID | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **armId** | `string` | ARMID is a string of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}. The /resourcegroups/{resourceGroupName} bit is optional as some resources are scoped at the subscription level ARMID is mutually exclusive with Group, Kind, Namespace and Name. | `Pattern=(?i)(^(/subscriptions/([^/]+)(/resourcegroups/([^/]+))?)?/providers/([^/]+)/([^/]+/[^/]+)(/([^/]+/[^/]+))*$\|^/subscriptions/([^/]+)(/resourcegroups/([^/]+))?$)` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the Kubernetes group of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the Kubernetes kind of the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the Kubernetes name of the resource. | N/A |
| └>&nbsp;&nbsp; **requiredMembers** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | No description provided. | N/A |
|  **servicePrincipalProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **clientId** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **secret** | `object` | SecretReference is a reference to a Kubernetes secret and key in the same namespace as the resource it is on. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the Kubernetes secret being referenced | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes secret being referenced. The secret must be in the same namespace as the resource | N/A |
|  **sku** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **tier** | `string` | No description provided. | N/A |
|  **tags** | `object` | No description provided. | N/A |
|  **windowsProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **adminPassword** | `object` | SecretReference is a reference to a Kubernetes secret and key in the same namespace as the resource it is on. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the key in the Kubernetes secret being referenced | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes secret being referenced. The secret must be in the same namespace as the resource | N/A |
| └>&nbsp;&nbsp; **adminUsername** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enableCSIProxy** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **licenseType** | `string` | No description provided. | N/A |
## Status Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **aadProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **adminGroupObjectIDs** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **clientAppID** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enableAzureRBAC** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **managed** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **serverAppID** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **serverAppSecret** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **tenantID** | `string` | No description provided. | N/A |
|  **addonProfiles** | `object` | No description provided. | N/A |
|  **agentPoolProfiles** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **availabilityZones** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **count** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enableAutoScaling** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enableEncryptionAtHost** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enableFIPS** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enableNodePublicIP** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enableUltraSSD** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **gpuInstanceProfile** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **kubeletConfig** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **allowedUnsafeSysctls** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **containerLogMaxFiles** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **containerLogMaxSizeMB** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cpuCfsQuota** | `boolean` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cpuCfsQuotaPeriod** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cpuManagerPolicy** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **failSwapOn** | `boolean` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **imageGcHighThreshold** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **imageGcLowThreshold** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **podMaxPids** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **topologyManagerPolicy** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **kubeletDiskType** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **linuxOSConfig** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **swapFileSizeMB** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sysctls** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fsAioMaxNr** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fsFileMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fsInotifyMaxUserWatches** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fsNrOpen** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kernelThreadsMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreNetdevMaxBacklog** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreOptmemMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreRmemDefault** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreRmemMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreSomaxconn** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreWmemDefault** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netCoreWmemMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4IpLocalPortRange** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4NeighDefaultGcThresh1** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4NeighDefaultGcThresh2** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4NeighDefaultGcThresh3** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpFinTimeout** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpKeepaliveProbes** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpKeepaliveTime** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpMaxSynBacklog** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpMaxTwBuckets** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpTwReuse** | `boolean` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netIpv4TcpkeepaliveIntvl** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netNetfilterNfConntrackBuckets** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netNetfilterNfConntrackMax** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vmMaxMapCount** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vmSwappiness** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vmVfsCachePressure** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **transparentHugePageDefrag** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **transparentHugePageEnabled** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **maxCount** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **maxPods** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **minCount** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **mode** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **nodeImageVersion** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **nodeLabels** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **nodePublicIPPrefixID** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **nodeTaints** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **orchestratorVersion** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **osDiskSizeGB** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **osDiskType** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **osSKU** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **osType** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **podSubnetID** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **powerState** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **code** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **provisioningState** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **proximityPlacementGroupID** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scaleSetEvictionPolicy** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scaleSetPriority** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **spotMaxPrice** | `number` | No description provided. | N/A |
| └>&nbsp;&nbsp; **tags** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **upgradeSettings** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **maxSurge** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **vmSize** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **vnetSubnetID** | `string` | No description provided. | N/A |
|  **apiServerAccessProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **authorizedIPRanges** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enablePrivateCluster** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enablePrivateClusterPublicFQDN** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **privateDNSZone** | `string` | No description provided. | N/A |
|  **autoScalerProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **balance-similar-node-groups** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **expander** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **max-empty-bulk-delete** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **max-graceful-termination-sec** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **max-node-provision-time** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **max-total-unready-percentage** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **new-pod-scale-up-delay** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **ok-total-unready-count** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scale-down-delay-after-add** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scale-down-delay-after-delete** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scale-down-delay-after-failure** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scale-down-unneeded-time** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scale-down-unready-time** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scale-down-utilization-threshold** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **scan-interval** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **skip-nodes-with-local-storage** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **skip-nodes-with-system-pods** | `string` | No description provided. | N/A |
|  **autoUpgradeProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **upgradeChannel** | `string` | No description provided. | N/A |
|  **azurePortalFQDN** | `string` | No description provided. | N/A |
|  **conditions** | `array` | Conditions: The observed state of the resource | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the last time the condition transitioned from one status to another. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | ObservedGeneration is the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.condition[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason for the condition's last transition. Reasons are upper CamelCase (PascalCase) with no spaces. A reason is always provided, this field will not be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | Severity with which to treat failures of this type of condition. For conditions which have positive polarity (Status == True is their normal/healthy state), this will be omitted when Status == True For conditions which have negative polarity (Status == False is their normal/healthy state), this will be omitted when Status == False. This is omitted in all cases when Status == Unknown | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status of the condition, one of True, False, or Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type of condition. | N/A |
|  **disableLocalAccounts** | `boolean` | No description provided. | N/A |
|  **diskEncryptionSetID** | `string` | No description provided. | N/A |
|  **dnsPrefix** | `string` | No description provided. | N/A |
|  **enablePodSecurityPolicy** | `boolean` | No description provided. | N/A |
|  **enableRBAC** | `boolean` | No description provided. | N/A |
|  **extendedLocation** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | No description provided. | N/A |
|  **fqdn** | `string` | No description provided. | N/A |
|  **fqdnSubdomain** | `string` | No description provided. | N/A |
|  **httpProxyConfig** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **httpProxy** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **httpsProxy** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **noProxy** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **trustedCa** | `string` | No description provided. | N/A |
|  **id** | `string` | No description provided. | N/A |
|  **identity** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **principalId** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **tenantId** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **userAssignedIdentities** | `object` | No description provided. | N/A |
|  **identityProfile** | `object` | No description provided. | N/A |
|  **kubernetesVersion** | `string` | No description provided. | N/A |
|  **linuxProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **adminUsername** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **ssh** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **publicKeys** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **keyData** | `string` | No description provided. | N/A |
|  **location** | `string` | No description provided. | N/A |
|  **maxAgentPools** | `integer` | No description provided. | N/A |
|  **name** | `string` | No description provided. | N/A |
|  **networkProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **dnsServiceIP** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **dockerBridgeCidr** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **loadBalancerProfile** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **allocatedOutboundPorts** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **effectiveOutboundIPs** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **idleTimeoutInMinutes** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **managedOutboundIPs** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **count** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **outboundIPPrefixes** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **publicIPPrefixes** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **outboundIPs** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **publicIPs** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **loadBalancerSku** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **networkMode** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **networkPlugin** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **networkPolicy** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **outboundType** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **podCidr** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **serviceCidr** | `string` | No description provided. | N/A |
|  **nodeResourceGroup** | `string` | No description provided. | N/A |
|  **podIdentityProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **allowNetworkPluginKubenet** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enabled** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **userAssignedIdentities** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **bindingSelector** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **identity** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **clientId** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **objectId** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceId** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **provisioningInfo** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **error** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **error** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **code** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **details** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **code** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **message** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **target** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **message** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **target** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **provisioningState** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **userAssignedIdentityExceptions** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **podLabels** | `object` | No description provided. | N/A |
|  **powerState** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **code** | `string` | No description provided. | N/A |
|  **privateFQDN** | `string` | No description provided. | N/A |
|  **privateLinkResources** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **groupId** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **privateLinkServiceID** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **requiredMembers** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | No description provided. | N/A |
|  **provisioningState** | `string` | No description provided. | N/A |
|  **servicePrincipalProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **clientId** | `string` | No description provided. | N/A |
|  **sku** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **tier** | `string` | No description provided. | N/A |
|  **tags** | `object` | No description provided. | N/A |
|  **type** | `string` | No description provided. | N/A |
|  **windowsProfile** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **adminUsername** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **enableCSIProxy** | `boolean` | No description provided. | N/A |
| └>&nbsp;&nbsp; **licenseType** | `string` | No description provided. | N/A |
