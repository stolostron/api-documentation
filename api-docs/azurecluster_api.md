# AzureCluster API

AzureCluster is the Schema for the azureclusters API.

## Spec Fields

AzureClusterSpec defines the desired state of AzureCluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **additionalTags** | `object` | AdditionalTags is an optional set of tags to add to Azure resources managed by the Azure provider, in addition to the ones added by default. | N/A |
|  **azureEnvironment** | `string` | AzureEnvironment is the name of the AzureCloud to be used. The default value that would be used by most users is "AzurePublicCloud", other values are: - ChinaCloud: "AzureChinaCloud" - GermanCloud: "AzureGermanCloud" - PublicCloud: "AzurePublicCloud" - USGovernmentCloud: "AzureUSGovernmentCloud" Note that values other than the default must also be accompanied by corresponding changes to the aso-controller-settings Secret to configure ASO to refer to the non-Public cloud. ASO currently does not support referring to multiple different clouds in a single installation. The following fields must be defined in the Secret: - AZURE_AUTHORITY_HOST - AZURE_RESOURCE_MANAGER_ENDPOINT - AZURE_RESOURCE_MANAGER_AUDIENCE See the [ASO docs] for more details. [ASO docs]: https://azure.github.io/azure-service-operator/guide/aso-controller-settings-options/ | N/A |
|  **bastionSpec** | `object` | BastionSpec encapsulates all things related to the Bastions in the cluster. | N/A |
| └>&nbsp;&nbsp; **azureBastion** | `object` | AzureBastion specifies how the Azure Bastion cloud component should be configured. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **enableTunneling** | `boolean` | EnableTunneling enables the native client support feature for the Azure Bastion Host. Defaults to false. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **publicIP** | `object` | PublicIPSpec defines the inputs to create an Azure public IP address. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dnsName** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipTags** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tag** | `string` | Tag specifies the value of the IP tag associated with the public IP. Example: SQL. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type specifies the IP tag type. Example: FirstPartyUsage. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sku** | `string` | BastionHostSkuName configures the tier of the Azure Bastion Host. Can be either Basic or Standard. Defaults to Basic. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **subnet** | `object` | SubnetSpec configures an Azure subnet. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cidrBlocks** | `array` | CIDRBlocks defines the subnet's address space, specified as one or more address prefixes in CIDR notation. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID is the Azure resource ID of the subnet. READ-ONLY | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name defines a name for the subnet resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **natGateway** | `object` | NatGateway associated with this subnet. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID is the Azure resource ID of the NAT gateway. READ-ONLY | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ip** | `object` | PublicIPSpec defines the inputs to create an Azure public IP address. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dnsName** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipTags** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tag** | `string` | Tag specifies the value of the IP tag associated with the public IP. Example: SQL. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type specifies the IP tag type. Example: FirstPartyUsage. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **zones** | `array` | Zones mentions the list of zones the NAT gateway should be a part of. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **privateEndpoints** | `array` | PrivateEndpoints defines a list of private endpoints that should be attached to this subnet. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **applicationSecurityGroups** | `array` | ApplicationSecurityGroups specifies the Application security group in which the private endpoint IP configuration is included. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **customNetworkInterfaceName** | `string` | CustomNetworkInterfaceName specifies the network interface name associated with the private endpoint. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **location** | `string` | Location specifies the region to create the private endpoint. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **manualApproval** | `boolean` | ManualApproval specifies if the connection approval needs to be done manually or not. Set it true when the network admin does not have access to approve connections to the remote resource. Defaults to false. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name specifies the name of the private endpoint. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **privateIPAddresses** | `array` | PrivateIPAddresses specifies the IP addresses for the network interface associated with the private endpoint. They have to be part of the subnet where the private endpoint is linked. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **privateLinkServiceConnections** | `array` | PrivateLinkServiceConnections specifies Private Link Service Connections of the private endpoint. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **groupIDs** | `array` | GroupIDs specifies the ID(s) of the group(s) obtained from the remote resource that this private endpoint should connect to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name specifies the name of the private link service. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **privateLinkServiceID** | `string` | PrivateLinkServiceID specifies the resource ID of the private link service. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **requestMessage** | `string` | RequestMessage specifies a message passed to the owner of the remote resource with the private endpoint connection request. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **role** | `string` | Role defines the subnet role (eg. Node, ControlPlane) | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **routeTable** | `object` | RouteTable defines the route table that should be attached to this subnet. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID is the Azure resource ID of the route table. READ-ONLY | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **securityGroup** | `object` | SecurityGroup defines the NSG (network security group) that should be attached to this subnet. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID is the Azure resource ID of the security group. READ-ONLY | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **securityRules** | `array` | SecurityRules is a slice of Azure security rules for security groups. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **action** | `string` | Action specifies whether network traffic is allowed or denied. Can either be "Allow" or "Deny". Defaults to "Allow". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **description** | `string` | A description for this rule. Restricted to 140 chars. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **destination** | `string` | Destination is the destination address prefix. CIDR or destination IP range. Asterix '*' can also be used to match all source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **destinationPorts** | `string` | DestinationPorts specifies the destination port or range. Integer or range between 0 and 65535. Asterix '*' can also be used to match all ports. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **direction** | `string` | Direction indicates whether the rule applies to inbound, or outbound traffic. "Inbound" or "Outbound". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is a unique name within the network security group. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **priority** | `integer` | Priority is a number between 100 and 4096. Each rule should have a unique value for priority. Rules are processed in priority order, with lower numbers processed before higher numbers. Once traffic matches a rule, processing stops. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **protocol** | `string` | Protocol specifies the protocol type. "Tcp", "Udp", "Icmp", or "*". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **source** | `string` | Source specifies the CIDR or source IP range. Asterix '*' can also be used to match all source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used. If this is an ingress rule, specifies where network traffic originates from. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sourcePorts** | `string` | SourcePorts specifies source port or range. Integer or range between 0 and 65535. Asterix '*' can also be used to match all ports. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sources** | `array` | Sources specifies The CIDR or source IP ranges. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tags** | `object` | Tags defines a map of tags. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serviceEndpoints** | `array` | ServiceEndpoints is a slice of Virtual Network service endpoints to enable for the subnets. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **locations** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **service** | `string` | No description provided. | N/A |
|  **cloudProviderConfigOverrides** | `object` | CloudProviderConfigOverrides is an optional set of configuration values that can be overridden in azure cloud provider config. This is only a subset of options that are available in azure cloud provider config. Some values for the cloud provider config are inferred from other parts of cluster api provider azure spec, and may not be available for overrides. See: https://cloud-provider-azure.sigs.k8s.io/install/configs Note: All cloud provider config values can be customized by creating the secret beforehand. CloudProviderConfigOverrides is only used when the secret is managed by the Azure Provider. | N/A |
| └>&nbsp;&nbsp; **backOffs** | `object` | BackOffConfig indicates the back-off config options. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cloudProviderBackoff** | `boolean` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cloudProviderBackoffDuration** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cloudProviderBackoffExponent** | `N/A` | No description provided. | `Pattern=^(\+\|-)?(([0-9]+(\.[0-9]*)?)\|(\.[0-9]+))(([KMGTPE]i)\|[numkMGTPE]\|([eE](\+\|-)?(([0-9]+(\.[0-9]*)?)\|(\.[0-9]+))))?$` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cloudProviderBackoffJitter** | `N/A` | No description provided. | `Pattern=^(\+\|-)?(([0-9]+(\.[0-9]*)?)\|(\.[0-9]+))(([KMGTPE]i)\|[numkMGTPE]\|([eE](\+\|-)?(([0-9]+(\.[0-9]*)?)\|(\.[0-9]+))))?$` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cloudProviderBackoffRetries** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **rateLimits** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **config** | `object` | RateLimitConfig indicates the rate limit config options. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cloudProviderRateLimit** | `boolean` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cloudProviderRateLimitBucket** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cloudProviderRateLimitBucketWrite** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cloudProviderRateLimitQPS** | `N/A` | No description provided. | `Pattern=^(\+\|-)?(([0-9]+(\.[0-9]*)?)\|(\.[0-9]+))(([KMGTPE]i)\|[numkMGTPE]\|([eE](\+\|-)?(([0-9]+(\.[0-9]*)?)\|(\.[0-9]+))))?$` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cloudProviderRateLimitQPSWrite** | `N/A` | No description provided. | `Pattern=^(\+\|-)?(([0-9]+(\.[0-9]*)?)\|(\.[0-9]+))(([KMGTPE]i)\|[numkMGTPE]\|([eE](\+\|-)?(([0-9]+(\.[0-9]*)?)\|(\.[0-9]+))))?$` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the rate limit spec. | N/A |
|  **controlPlaneEnabled** | `boolean` | ControlPlaneEnabled enables control plane components in the cluster. | N/A |
|  **controlPlaneEndpoint** | `object` | ControlPlaneEndpoint represents the endpoint used to communicate with the control plane. It is not recommended to set this when creating an AzureCluster as CAPZ will set this for you. However, if it is set, CAPZ will not change it. | N/A |
| └>&nbsp;&nbsp; **host** | `string` | host is the hostname on which the API server is serving. | N/A |
| └>&nbsp;&nbsp; **port** | `integer` | port is the port on which the API server is serving. | N/A |
|  **extendedLocation** | `object` | ExtendedLocation is an optional set of ExtendedLocation properties for clusters on Azure public MEC. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name defines the name for the extended location. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type defines the type for the extended location. | N/A |
|  **failureDomains** | `object` | FailureDomains is a list of failure domains in the cluster's region, used to restrict eligibility to host the control plane. A FailureDomain maps to an availability zone, which is a separated group of datacenters within a region. See: https://learn.microsoft.com/azure/reliability/availability-zones-overview | N/A |
|  **identityRef** | `object` | IdentityRef is a reference to an AzureIdentity to be used when reconciling this cluster | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| └>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| └>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
|  **location** | `string` | No description provided. | N/A |
|  **networkSpec** | `object` | NetworkSpec encapsulates all things related to Azure network. | N/A |
| └>&nbsp;&nbsp; **additionalAPIServerLBPorts** | `array` | AdditionalAPIServerLBPorts specifies extra inbound ports for the APIServer load balancer. Each port specified (e.g., 9345) creates an inbound rule where the frontend port and the backend port are the same. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name for the additional port within LB definition | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **port** | `integer` | Port for the LB definition | N/A |
| └>&nbsp;&nbsp; **apiServerLB** | `object` | APIServerLB is the configuration for the control-plane load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **backendPool** | `object` | BackendPool describes the backend pool of the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name specifies the name of backend pool for the load balancer. If not specified, the default name will be set, depending on the load balancer role. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **frontendIPs** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **privateIP** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **publicIP** | `object` | PublicIPSpec defines the inputs to create an Azure public IP address. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dnsName** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipTags** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tag** | `string` | Tag specifies the value of the IP tag associated with the public IP. Example: SQL. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type specifies the IP tag type. Example: FirstPartyUsage. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **frontendIPsCount** | `integer` | FrontendIPsCount specifies the number of frontend IP addresses for the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID is the Azure resource ID of the load balancer. READ-ONLY | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **idleTimeoutInMinutes** | `integer` | IdleTimeoutInMinutes specifies the timeout for the TCP idle connection. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sku** | `string` | SKU defines an Azure load balancer SKU. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | LBType defines an Azure load balancer Type. | N/A |
| └>&nbsp;&nbsp; **controlPlaneOutboundLB** | `object` | ControlPlaneOutboundLB is the configuration for the control-plane outbound load balancer. This is different from APIServerLB, and is used only in private clusters (optionally) for enabling outbound traffic. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **backendPool** | `object` | BackendPool describes the backend pool of the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name specifies the name of backend pool for the load balancer. If not specified, the default name will be set, depending on the load balancer role. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **frontendIPs** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **privateIP** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **publicIP** | `object` | PublicIPSpec defines the inputs to create an Azure public IP address. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dnsName** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipTags** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tag** | `string` | Tag specifies the value of the IP tag associated with the public IP. Example: SQL. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type specifies the IP tag type. Example: FirstPartyUsage. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **frontendIPsCount** | `integer` | FrontendIPsCount specifies the number of frontend IP addresses for the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID is the Azure resource ID of the load balancer. READ-ONLY | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **idleTimeoutInMinutes** | `integer` | IdleTimeoutInMinutes specifies the timeout for the TCP idle connection. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sku** | `string` | SKU defines an Azure load balancer SKU. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | LBType defines an Azure load balancer Type. | N/A |
| └>&nbsp;&nbsp; **nodeOutboundLB** | `object` | NodeOutboundLB is the configuration for the node outbound load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **backendPool** | `object` | BackendPool describes the backend pool of the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name specifies the name of backend pool for the load balancer. If not specified, the default name will be set, depending on the load balancer role. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **frontendIPs** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **privateIP** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **publicIP** | `object` | PublicIPSpec defines the inputs to create an Azure public IP address. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dnsName** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipTags** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tag** | `string` | Tag specifies the value of the IP tag associated with the public IP. Example: SQL. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type specifies the IP tag type. Example: FirstPartyUsage. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **frontendIPsCount** | `integer` | FrontendIPsCount specifies the number of frontend IP addresses for the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID is the Azure resource ID of the load balancer. READ-ONLY | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **idleTimeoutInMinutes** | `integer` | IdleTimeoutInMinutes specifies the timeout for the TCP idle connection. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sku** | `string` | SKU defines an Azure load balancer SKU. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | LBType defines an Azure load balancer Type. | N/A |
| └>&nbsp;&nbsp; **privateDNSZone** | `string` | PrivateDNSZone enables private dns zone creation modes for a private cluster. When unspecified, it defaults to PrivateDNSZoneModeSystem which creates a private DNS zone. | N/A |
| └>&nbsp;&nbsp; **privateDNSZoneName** | `string` | PrivateDNSZoneName defines the zone name for the Azure Private DNS. | N/A |
| └>&nbsp;&nbsp; **privateDNSZoneResourceGroup** | `string` | PrivateDNSZoneResourceGroup defines the resource group to be used for Azure Private DNS Zone. If not specified, the resource group of the cluster will be used to create the Azure Private DNS Zone. | N/A |
| └>&nbsp;&nbsp; **subnets** | `array` | Subnets is the configuration for the control-plane subnet and the node subnet. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cidrBlocks** | `array` | CIDRBlocks defines the subnet's address space, specified as one or more address prefixes in CIDR notation. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID is the Azure resource ID of the subnet. READ-ONLY | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name defines a name for the subnet resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **natGateway** | `object` | NatGateway associated with this subnet. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID is the Azure resource ID of the NAT gateway. READ-ONLY | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ip** | `object` | PublicIPSpec defines the inputs to create an Azure public IP address. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dnsName** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipTags** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tag** | `string` | Tag specifies the value of the IP tag associated with the public IP. Example: SQL. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type specifies the IP tag type. Example: FirstPartyUsage. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **zones** | `array` | Zones mentions the list of zones the NAT gateway should be a part of. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **privateEndpoints** | `array` | PrivateEndpoints defines a list of private endpoints that should be attached to this subnet. | N/A |
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
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **role** | `string` | Role defines the subnet role (eg. Node, ControlPlane) | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **routeTable** | `object` | RouteTable defines the route table that should be attached to this subnet. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID is the Azure resource ID of the route table. READ-ONLY | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **securityGroup** | `object` | SecurityGroup defines the NSG (network security group) that should be attached to this subnet. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID is the Azure resource ID of the security group. READ-ONLY | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **securityRules** | `array` | SecurityRules is a slice of Azure security rules for security groups. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **action** | `string` | Action specifies whether network traffic is allowed or denied. Can either be "Allow" or "Deny". Defaults to "Allow". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **description** | `string` | A description for this rule. Restricted to 140 chars. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **destination** | `string` | Destination is the destination address prefix. CIDR or destination IP range. Asterix '*' can also be used to match all source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **destinationPorts** | `string` | DestinationPorts specifies the destination port or range. Integer or range between 0 and 65535. Asterix '*' can also be used to match all ports. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **direction** | `string` | Direction indicates whether the rule applies to inbound, or outbound traffic. "Inbound" or "Outbound". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is a unique name within the network security group. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **priority** | `integer` | Priority is a number between 100 and 4096. Each rule should have a unique value for priority. Rules are processed in priority order, with lower numbers processed before higher numbers. Once traffic matches a rule, processing stops. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **protocol** | `string` | Protocol specifies the protocol type. "Tcp", "Udp", "Icmp", or "*". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **source** | `string` | Source specifies the CIDR or source IP range. Asterix '*' can also be used to match all source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used. If this is an ingress rule, specifies where network traffic originates from. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sourcePorts** | `string` | SourcePorts specifies source port or range. Integer or range between 0 and 65535. Asterix '*' can also be used to match all ports. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sources** | `array` | Sources specifies The CIDR or source IP ranges. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tags** | `object` | Tags defines a map of tags. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serviceEndpoints** | `array` | ServiceEndpoints is a slice of Virtual Network service endpoints to enable for the subnets. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **locations** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **service** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **vnet** | `object` | Vnet is the configuration for the Azure virtual network. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cidrBlocks** | `array` | CIDRBlocks defines the virtual network's address space, specified as one or more address prefixes in CIDR notation. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID is the Azure resource ID of the virtual network. READ-ONLY | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name defines a name for the virtual network resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **peerings** | `array` | Peerings defines a list of peerings of the newly created virtual network with existing virtual networks. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **forwardPeeringProperties** | `object` | ForwardPeeringProperties specifies VnetPeeringProperties for peering from the cluster's virtual network to the remote virtual network. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **allowForwardedTraffic** | `boolean` | AllowForwardedTraffic specifies whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **allowGatewayTransit** | `boolean` | AllowGatewayTransit specifies if gateway links can be used in remote virtual networking to link to this virtual network. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **allowVirtualNetworkAccess** | `boolean` | AllowVirtualNetworkAccess specifies whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **useRemoteGateways** | `boolean` | UseRemoteGateways specifies if remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also set to true, the virtual network will use the gateways of the remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **remoteVnetName** | `string` | RemoteVnetName defines name of the remote virtual network. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceGroup** | `string` | ResourceGroup is the resource group name of the remote virtual network. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **reversePeeringProperties** | `object` | ReversePeeringProperties specifies VnetPeeringProperties for peering from the remote virtual network to the cluster's virtual network. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **allowForwardedTraffic** | `boolean` | AllowForwardedTraffic specifies whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **allowGatewayTransit** | `boolean` | AllowGatewayTransit specifies if gateway links can be used in remote virtual networking to link to this virtual network. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **allowVirtualNetworkAccess** | `boolean` | AllowVirtualNetworkAccess specifies whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **useRemoteGateways** | `boolean` | UseRemoteGateways specifies if remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also set to true, the virtual network will use the gateways of the remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceGroup** | `string` | ResourceGroup is the name of the resource group of the existing virtual network or the resource group where a managed virtual network should be created. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tags** | `object` | Tags is a collection of tags describing the resource. | N/A |
|  **resourceGroup** | `string` | No description provided. | N/A |
|  **subscriptionID** | `string` | No description provided. | N/A |
## Status Fields

AzureClusterStatus defines the observed state of AzureCluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions defines current service state of the AzureCluster. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | reason is the reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **failureDomains** | `object` | FailureDomains specifies the list of unique failure domains for the location/region of the cluster. A FailureDomain maps to Availability Zone with an Azure Region (if the region support them). An Availability Zone is a separate data center within a region and they can be used to ensure the cluster is more resilient to failure. See: https://learn.microsoft.com/azure/reliability/availability-zones-overview This list will be used by Cluster API to try and spread the machines across the failure domains. | N/A |
|  **longRunningOperationStates** | `array` | LongRunningOperationStates saves the states for Azure long-running operations so they can be continued on the next reconciliation loop. | N/A |
| └>&nbsp;&nbsp; **data** | `string` | Data is the base64 url encoded json Azure AutoRest Future. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the Azure resource. Together with the service name, this forms the unique identifier for the future. | N/A |
| └>&nbsp;&nbsp; **resourceGroup** | `string` | ResourceGroup is the Azure resource group for the resource. | N/A |
| └>&nbsp;&nbsp; **serviceName** | `string` | ServiceName is the name of the Azure service. Together with the name of the resource, this forms the unique identifier for the future. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type describes the type of future, such as update, create, delete, etc. | N/A |
|  **ready** | `boolean` | Ready is true when the provider resource is ready. | N/A |
