# AzureManagedControlPlane API

AzureManagedControlPlane is the Schema for the azuremanagedcontrolplanes API.

## Spec Fields

AzureManagedControlPlaneSpec defines the desired state of AzureManagedControlPlane.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **aadProfile** | `object` | AadProfile is Azure Active Directory configuration to integrate with AKS for aad authentication. | N/A |
| └>&nbsp;&nbsp; **adminGroupObjectIDs** | `array` | AdminGroupObjectIDs - AAD group object IDs that will have admin role of the cluster. | N/A |
| └>&nbsp;&nbsp; **managed** | `boolean` | Managed - Whether to enable managed AAD. | N/A |
|  **additionalTags** | `object` | AdditionalTags is an optional set of tags to add to Azure resources managed by the Azure provider, in addition to the ones added by default. | N/A |
|  **addonProfiles** | `array` | AddonProfiles are the profiles of managed cluster add-on. | N/A |
| └>&nbsp;&nbsp; **config** | `object` | Config - Key-value pairs for configuring the add-on. | N/A |
| └>&nbsp;&nbsp; **enabled** | `boolean` | Enabled - Whether the add-on is enabled or not. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name - The name of the managed cluster add-on. | N/A |
|  **apiServerAccessProfile** | `object` | APIServerAccessProfile is the access profile for AKS API server. Immutable except for `authorizedIPRanges`. | N/A |
| └>&nbsp;&nbsp; **authorizedIPRanges** | `array` | AuthorizedIPRanges - Authorized IP Ranges to kubernetes API server. | N/A |
| └>&nbsp;&nbsp; **enablePrivateCluster** | `boolean` | EnablePrivateCluster indicates whether to create the cluster as a private cluster or not. | N/A |
| └>&nbsp;&nbsp; **enablePrivateClusterPublicFQDN** | `boolean` | EnablePrivateClusterPublicFQDN indicates whether to create additional public FQDN for private cluster or not. | N/A |
| └>&nbsp;&nbsp; **privateDNSZone** | `string` | PrivateDNSZone enables private dns zone mode for private cluster. | N/A |
|  **asoManagedClusterPatches** | `array` | ASOManagedClusterPatches defines JSON merge patches to be applied to the generated ASO ManagedCluster resource. WARNING: This is meant to be used sparingly to enable features for development and testing that are not otherwise represented in the CAPZ API. Misconfiguration that conflicts with CAPZ's normal mode of operation is possible. | N/A |
|  **autoUpgradeProfile** | `object` | AutoUpgradeProfile defines the auto upgrade configuration. | N/A |
| └>&nbsp;&nbsp; **upgradeChannel** | `string` | UpgradeChannel determines the type of upgrade channel for automatically upgrading the cluster. | N/A |
|  **autoscalerProfile** | `object` | AutoscalerProfile is the parameters to be applied to the cluster-autoscaler when enabled | N/A |
| └>&nbsp;&nbsp; **balanceSimilarNodeGroups** | `string` | BalanceSimilarNodeGroups - Valid values are 'true' and 'false'. The default is false. | N/A |
| └>&nbsp;&nbsp; **expander** | `string` | Expander - If not specified, the default is 'random'. See [expanders](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-are-expanders) for more information. | N/A |
| └>&nbsp;&nbsp; **maxEmptyBulkDelete** | `string` | MaxEmptyBulkDelete - The default is 10. | N/A |
| └>&nbsp;&nbsp; **maxGracefulTerminationSec** | `string` | MaxGracefulTerminationSec - The default is 600. | `Pattern=^(\d+)$` |
| └>&nbsp;&nbsp; **maxNodeProvisionTime** | `string` | MaxNodeProvisionTime - The default is '15m'. Values must be an integer followed by an 'm'. No unit of time other than minutes (m) is supported. | `Pattern=^(\d+)m$` |
| └>&nbsp;&nbsp; **maxTotalUnreadyPercentage** | `string` | MaxTotalUnreadyPercentage - The default is 45. The maximum is 100 and the minimum is 0. | `Pattern=^(\d+)$` |
| └>&nbsp;&nbsp; **newPodScaleUpDelay** | `string` | NewPodScaleUpDelay - For scenarios like burst/batch scale where you don't want CA to act before the kubernetes scheduler could schedule all the pods, you can tell CA to ignore unscheduled pods before they're a certain age. The default is '0s'. Values must be an integer followed by a unit ('s' for seconds, 'm' for minutes, 'h' for hours, etc). | N/A |
| └>&nbsp;&nbsp; **okTotalUnreadyCount** | `string` | OkTotalUnreadyCount - This must be an integer. The default is 3. | `Pattern=^(\d+)$` |
| └>&nbsp;&nbsp; **scaleDownDelayAfterAdd** | `string` | ScaleDownDelayAfterAdd - The default is '10m'. Values must be an integer followed by an 'm'. No unit of time other than minutes (m) is supported. | `Pattern=^(\d+)m$` |
| └>&nbsp;&nbsp; **scaleDownDelayAfterDelete** | `string` | ScaleDownDelayAfterDelete - The default is the scan-interval. Values must be an integer followed by an 's'. No unit of time other than seconds (s) is supported. | `Pattern=^(\d+)s$` |
| └>&nbsp;&nbsp; **scaleDownDelayAfterFailure** | `string` | ScaleDownDelayAfterFailure - The default is '3m'. Values must be an integer followed by an 'm'. No unit of time other than minutes (m) is supported. | `Pattern=^(\d+)m$` |
| └>&nbsp;&nbsp; **scaleDownUnneededTime** | `string` | ScaleDownUnneededTime - The default is '10m'. Values must be an integer followed by an 'm'. No unit of time other than minutes (m) is supported. | `Pattern=^(\d+)m$` |
| └>&nbsp;&nbsp; **scaleDownUnreadyTime** | `string` | ScaleDownUnreadyTime - The default is '20m'. Values must be an integer followed by an 'm'. No unit of time other than minutes (m) is supported. | `Pattern=^(\d+)m$` |
| └>&nbsp;&nbsp; **scaleDownUtilizationThreshold** | `string` | ScaleDownUtilizationThreshold - The default is '0.5'. | N/A |
| └>&nbsp;&nbsp; **scanInterval** | `string` | ScanInterval - How often cluster is reevaluated for scale up or down. The default is '10s'. | `Pattern=^(\d+)s$` |
| └>&nbsp;&nbsp; **skipNodesWithLocalStorage** | `string` | SkipNodesWithLocalStorage - The default is false. | N/A |
| └>&nbsp;&nbsp; **skipNodesWithSystemPods** | `string` | SkipNodesWithSystemPods - The default is true. | N/A |
|  **azureEnvironment** | `string` | AzureEnvironment is the name of the AzureCloud to be used. The default value that would be used by most users is "AzurePublicCloud", other values are: - ChinaCloud: "AzureChinaCloud" - PublicCloud: "AzurePublicCloud" - USGovernmentCloud: "AzureUSGovernmentCloud" Note that values other than the default must also be accompanied by corresponding changes to the aso-controller-settings Secret to configure ASO to refer to the non-Public cloud. ASO currently does not support referring to multiple different clouds in a single installation. The following fields must be defined in the Secret: - AZURE_AUTHORITY_HOST - AZURE_RESOURCE_MANAGER_ENDPOINT - AZURE_RESOURCE_MANAGER_AUDIENCE See the [ASO docs] for more details. [ASO docs]: https://azure.github.io/azure-service-operator/guide/aso-controller-settings-options/ | N/A |
|  **controlPlaneEndpoint** | `object` | ControlPlaneEndpoint represents the endpoint used to communicate with the control plane. Immutable, populated by the AKS API at create. | N/A |
| └>&nbsp;&nbsp; **host** | `string` | host is the hostname on which the API server is serving. | N/A |
| └>&nbsp;&nbsp; **port** | `integer` | port is the port on which the API server is serving. | N/A |
|  **disableLocalAccounts** | `boolean` | DisableLocalAccounts disables getting static credentials for this cluster when set. Expected to only be used for AAD clusters. | N/A |
|  **dnsPrefix** | `string` | DNSPrefix allows the user to customize dns prefix. Immutable. | N/A |
|  **dnsServiceIP** | `string` | DNSServiceIP is an IP address assigned to the Kubernetes DNS service. It must be within the Kubernetes service address range specified in serviceCidr. Immutable. | N/A |
|  **enablePreviewFeatures** | `boolean` | EnablePreviewFeatures enables preview features for the cluster. | N/A |
|  **extensions** | `array` | Extensions is a list of AKS extensions to be installed on the cluster. | N/A |
| └>&nbsp;&nbsp; **aksAssignedIdentityType** | `string` | AKSAssignedIdentityType is the type of the AKS assigned identity. | N/A |
| └>&nbsp;&nbsp; **autoUpgradeMinorVersion** | `boolean` | AutoUpgradeMinorVersion is a flag to note if this extension participates in auto upgrade of minor version, or not. | N/A |
| └>&nbsp;&nbsp; **configurationSettings** | `object` | ConfigurationSettings are the name-value pairs for configuring this extension. | N/A |
| └>&nbsp;&nbsp; **extensionType** | `string` | ExtensionType is the type of the Extension of which this resource is an instance. It must be one of the Extension Types registered with Microsoft.KubernetesConfiguration by the Extension publisher. | N/A |
| └>&nbsp;&nbsp; **identity** | `string` | Identity is the identity type of the Extension resource in an AKS cluster. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the extension. | N/A |
| └>&nbsp;&nbsp; **plan** | `object` | Plan is the plan of the extension. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the user-defined name of the 3rd Party Artifact that is being procured. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **product** | `string` | Product is the name of the 3rd Party artifact that is being procured. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **promotionCode** | `string` | PromotionCode is a publisher-provided promotion code as provisioned in Data Market for the said product/artifact. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **publisher** | `string` | Publisher is the name of the publisher of the 3rd Party Artifact that is being bought. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | Version is the version of the plan. | N/A |
| └>&nbsp;&nbsp; **releaseTrain** | `string` | ReleaseTrain is the release train this extension participates in for auto-upgrade (e.g. Stable, Preview, etc.) This is only used if autoUpgradeMinorVersion is ‘true’. | N/A |
| └>&nbsp;&nbsp; **scope** | `object` | Scope is the scope at which this extension is enabled. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **releaseNamespace** | `string` | ReleaseNamespace is the namespace where the extension Release must be placed, for a Cluster-scoped extension. Required for Cluster-scoped extensions. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **scopeType** | `string` | ScopeType is the scope of the extension. It can be either Cluster or Namespace, but not both. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **targetNamespace** | `string` | TargetNamespace is the namespace where the extension will be created for a Namespace-scoped extension. Required for Namespace-scoped extensions. | N/A |
| └>&nbsp;&nbsp; **version** | `string` | Version is the version of the extension. | N/A |
|  **fleetsMember** | `object` | FleetsMember is the spec for the fleet this cluster is a member of. See also [AKS doc]. [AKS doc]: https://learn.microsoft.com/en-us/azure/templates/microsoft.containerservice/2023-03-15-preview/fleets/members | N/A |
| └>&nbsp;&nbsp; **group** | `string` | Group is the group this member belongs to for multi-cluster update management. | N/A |
| └>&nbsp;&nbsp; **managerName** | `string` | ManagerName is the name of the fleet manager. | N/A |
| └>&nbsp;&nbsp; **managerResourceGroup** | `string` | ManagerResourceGroup is the resource group of the fleet manager. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the member. | N/A |
|  **httpProxyConfig** | `object` | HTTPProxyConfig is the HTTP proxy configuration for the cluster. Immutable. | N/A |
| └>&nbsp;&nbsp; **httpProxy** | `string` | HTTPProxy is the HTTP proxy server endpoint to use. | N/A |
| └>&nbsp;&nbsp; **httpsProxy** | `string` | HTTPSProxy is the HTTPS proxy server endpoint to use. | N/A |
| └>&nbsp;&nbsp; **noProxy** | `array` | NoProxy indicates the endpoints that should not go through proxy. | N/A |
| └>&nbsp;&nbsp; **trustedCa** | `string` | TrustedCA is the alternative CA cert to use for connecting to proxy servers. | N/A |
|  **identity** | `object` | Identity configuration used by the AKS control plane. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type - The Identity type to use. | N/A |
| └>&nbsp;&nbsp; **userAssignedIdentityResourceID** | `string` | UserAssignedIdentityResourceID - Identity ARM resource ID when using user-assigned identity. | N/A |
|  **identityRef** | `object` | IdentityRef is a reference to a AzureClusterIdentity to be used when reconciling this cluster | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| └>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| └>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
|  **kubeletUserAssignedIdentity** | `string` | KubeletUserAssignedIdentity is the user-assigned identity for kubelet. For authentication with Azure Container Registry. | N/A |
|  **loadBalancerProfile** | `object` | LoadBalancerProfile is the profile of the cluster load balancer. | N/A |
| └>&nbsp;&nbsp; **allocatedOutboundPorts** | `integer` | AllocatedOutboundPorts - Desired number of allocated SNAT ports per VM. Allowed values must be in the range of 0 to 64000 (inclusive). The default value is 0 which results in Azure dynamically allocating ports. | N/A |
| └>&nbsp;&nbsp; **idleTimeoutInMinutes** | `integer` | IdleTimeoutInMinutes - Desired outbound flow idle timeout in minutes. Allowed values must be in the range of 4 to 120 (inclusive). The default value is 30 minutes. | N/A |
| └>&nbsp;&nbsp; **managedOutboundIPs** | `integer` | ManagedOutboundIPs - Desired managed outbound IPs for the cluster load balancer. | N/A |
| └>&nbsp;&nbsp; **outboundIPPrefixes** | `array` | OutboundIPPrefixes - Desired outbound IP Prefix resources for the cluster load balancer. | N/A |
| └>&nbsp;&nbsp; **outboundIPs** | `array` | OutboundIPs - Desired outbound IP resources for the cluster load balancer. | N/A |
|  **loadBalancerSKU** | `string` | LoadBalancerSKU is the SKU of the loadBalancer to be provisioned. Immutable. | N/A |
|  **location** | `string` | Location is a string matching one of the canonical Azure region names. Examples: "westus2", "eastus". | N/A |
|  **machineTemplate** | `object` | MachineTemplate contains information about how machines should be shaped when creating or updating a control plane. For the AzureManagedControlPlaneTemplate, this field is used only to fulfill the CAPI contract. | N/A |
|  **networkDataplane** | `string` | NetworkDataplane is the dataplane used for building the Kubernetes network. | N/A |
|  **networkPlugin** | `string` | NetworkPlugin used for building Kubernetes network. | N/A |
|  **networkPluginMode** | `string` | NetworkPluginMode is the mode the network plugin should use. Allowed value is "overlay". | N/A |
|  **networkPolicy** | `string` | NetworkPolicy used for building Kubernetes network. | N/A |
|  **nodeResourceGroupName** | `string` | NodeResourceGroupName is the name of the resource group containing cluster IaaS resources. Will be populated to default in webhook. Immutable. | N/A |
|  **oidcIssuerProfile** | `object` | OIDCIssuerProfile is the OIDC issuer profile of the Managed Cluster. | N/A |
| └>&nbsp;&nbsp; **enabled** | `boolean` | Enabled is whether the OIDC issuer is enabled. | N/A |
|  **outboundType** | `string` | Outbound configuration used by Nodes. | N/A |
|  **resourceGroupName** | `string` | ResourceGroupName is the name of the Azure resource group for this AKS Cluster. Immutable. | N/A |
|  **securityProfile** | `object` | SecurityProfile defines the security profile for cluster. | N/A |
| └>&nbsp;&nbsp; **azureKeyVaultKms** | `object` | AzureKeyVaultKms defines Azure Key Vault Management Services Profile for the security profile. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **enabled** | `boolean` | Enabled enables the Azure Key Vault key management service. The default is false. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **keyID** | `string` | KeyID defines the Identifier of Azure Key Vault key. When Azure Key Vault key management service is enabled, this field is required and must be a valid key identifier. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **keyVaultNetworkAccess** | `string` | KeyVaultNetworkAccess defines the network access of key vault. The possible values are Public and Private. Public means the key vault allows public access from all networks. Private means the key vault disables public access and enables private link. The default value is Public. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **keyVaultResourceID** | `string` | KeyVaultResourceID is the Resource ID of key vault. When keyVaultNetworkAccess is Private, this field is required and must be a valid resource ID. | N/A |
| └>&nbsp;&nbsp; **defender** | `object` | Defender settings for the security profile. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **logAnalyticsWorkspaceResourceID** | `string` | LogAnalyticsWorkspaceResourceID is the ID of the Log Analytics workspace that has to be associated with Microsoft Defender. When Microsoft Defender is enabled, this field is required and must be a valid workspace resource ID. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **securityMonitoring** | `object` | SecurityMonitoring profile defines the Microsoft Defender threat detection for Cloud settings for the security profile. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **enabled** | `boolean` | Enabled enables Defender threat detection | N/A |
| └>&nbsp;&nbsp; **imageCleaner** | `object` | ImageCleaner settings for the security profile. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **enabled** | `boolean` | Enabled enables the Image Cleaner on AKS cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **intervalHours** | `integer` | IntervalHours defines Image Cleaner scanning interval in hours. Default value is 24 hours. | `Minimum=24`<br>`Maximum=2160` |
| └>&nbsp;&nbsp; **workloadIdentity** | `object` | Workloadidentity enables Kubernetes applications to access Azure cloud resources securely with Azure AD. Ensure to enable OIDC issuer while enabling Workload Identity | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **enabled** | `boolean` | Enabled enables the workload identity. | N/A |
|  **sku** | `object` | SKU is the SKU of the AKS to be provisioned. | N/A |
| └>&nbsp;&nbsp; **tier** | `string` | Tier - Tier of an AKS cluster. | N/A |
|  **sshPublicKey** | `string` | SSHPublicKey is a string literal containing an ssh public key base64 encoded. Use empty string to autogenerate new key. Use null value to not set key. Immutable. | N/A |
|  **subscriptionID** | `string` | SubscriptionID is the GUID of the Azure subscription that owns this cluster. | N/A |
|  **version** | `string` | Version defines the desired Kubernetes version. | N/A |
|  **virtualNetwork** | `object` | VirtualNetwork describes the virtual network for the AKS cluster. It will be created if it does not already exist. | N/A |
| └>&nbsp;&nbsp; **cidrBlock** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the virtual network. | N/A |
| └>&nbsp;&nbsp; **resourceGroup** | `string` | ResourceGroup is the name of the Azure resource group for the VNet and Subnet. | N/A |
| └>&nbsp;&nbsp; **subnet** | `object` | ManagedControlPlaneSubnet describes a subnet for an AKS cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cidrBlock** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **privateEndpoints** | `array` | PrivateEndpoints is a slice of Virtual Network private endpoints to create for the subnets. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **applicationSecurityGroups** | `array` | ApplicationSecurityGroups specifies the Application security group in which the private endpoint IP configuration is included. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **customNetworkInterfaceName** | `string` | CustomNetworkInterfaceName specifies the network interface name associated with the private endpoint. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **location** | `string` | Location specifies the region to create the private endpoint. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **manualApproval** | `boolean` | ManualApproval specifies if the connection approval needs to be done manually or not. Set it true when the network admin does not have access to approve connections to the remote resource. Defaults to false. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name specifies the name of the private endpoint. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **privateIPAddresses** | `array` | PrivateIPAddresses specifies the IP addresses for the network interface associated with the private endpoint. They have to be part of the subnet where the private endpoint is linked. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **privateLinkServiceConnections** | `array` | PrivateLinkServiceConnections specifies Private Link Service Connections of the private endpoint. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **groupIDs** | `array` | GroupIDs specifies the ID(s) of the group(s) obtained from the remote resource that this private endpoint should connect to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name specifies the name of the private link service. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **privateLinkServiceID** | `string` | PrivateLinkServiceID specifies the resource ID of the private link service. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **requestMessage** | `string` | RequestMessage specifies a message passed to the owner of the remote resource with the private endpoint connection request. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serviceEndpoints** | `array` | ServiceEndpoints is a slice of Virtual Network service endpoints to enable for the subnets. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **locations** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **service** | `string` | No description provided. | N/A |
## Status Fields

AzureManagedControlPlaneStatus defines the observed state of AzureManagedControlPlane.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **autoUpgradeVersion** | `string` | AutoUpgradeVersion is the Kubernetes version populated after auto-upgrade based on the upgrade channel. | N/A |
|  **conditions** | `array` | Conditions defines current service state of the AzureManagedControlPlane. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | reason is the reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **initialized** | `boolean` | Initialized is true when the control plane is available for initial contact. This may occur before the control plane is fully ready. In the AzureManagedControlPlane implementation, these are identical. | N/A |
|  **longRunningOperationStates** | `array` | LongRunningOperationStates saves the states for Azure long-running operations so they can be continued on the next reconciliation loop. | N/A |
| └>&nbsp;&nbsp; **data** | `string` | Data is the base64 url encoded json Azure AutoRest Future. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the Azure resource. Together with the service name, this forms the unique identifier for the future. | N/A |
| └>&nbsp;&nbsp; **resourceGroup** | `string` | ResourceGroup is the Azure resource group for the resource. | N/A |
| └>&nbsp;&nbsp; **serviceName** | `string` | ServiceName is the name of the Azure service. Together with the name of the resource, this forms the unique identifier for the future. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type describes the type of future, such as update, create, delete, etc. | N/A |
|  **oidcIssuerProfile** | `object` | OIDCIssuerProfile is the OIDC issuer profile of the Managed Cluster. | N/A |
| └>&nbsp;&nbsp; **issuerURL** | `string` | IssuerURL is the OIDC issuer url of the Managed Cluster. | N/A |
|  **ready** | `boolean` | Ready is true when the provider resource is ready. | N/A |
|  **version** | `string` | Version defines the Kubernetes version for the control plane instance. | N/A |
