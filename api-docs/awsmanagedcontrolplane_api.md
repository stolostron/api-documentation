# AWSManagedControlPlane API

AWSManagedControlPlaneStatus defines the observed state of an Amazon EKS Cluster.

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **additionalTags** | `object` | AdditionalTags is an optional set of tags to add to AWS resources managed by the AWS provider, in addition to the ones added by default. | N/A |
|  **addons** | `array` | Addons defines the EKS addons to enable with the EKS cluster. | N/A |
| └>&nbsp;&nbsp; **configuration** | `string` | Configuration of the EKS addon | N/A |
| └>&nbsp;&nbsp; **conflictResolution** | `string` | ConflictResolution is used to declare what should happen if there are parameter conflicts. Defaults to none | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the addon | N/A |
| └>&nbsp;&nbsp; **serviceAccountRoleARN** | `string` | ServiceAccountRoleArn is the ARN of an IAM role to bind to the addons service account | N/A |
| └>&nbsp;&nbsp; **version** | `string` | Version is the version of the addon to use | N/A |
|  **associateOIDCProvider** | `boolean` | AssociateOIDCProvider can be enabled to automatically create an identity provider for the controller for use with IAM roles for service accounts | N/A |
|  **bastion** | `object` | Bastion contains options to configure the bastion host. | N/A |
| └>&nbsp;&nbsp; **allowedCIDRBlocks** | `array` | AllowedCIDRBlocks is a list of CIDR blocks allowed to access the bastion host. They are set as ingress rules for the Bastion host's Security Group (defaults to 0.0.0.0/0). | N/A |
| └>&nbsp;&nbsp; **ami** | `string` | AMI will use the specified AMI to boot the bastion. If not specified, the AMI will default to one picked out in public space. | N/A |
| └>&nbsp;&nbsp; **disableIngressRules** | `boolean` | DisableIngressRules will ensure there are no Ingress rules in the bastion host's security group. Requires AllowedCIDRBlocks to be empty. | N/A |
| └>&nbsp;&nbsp; **enabled** | `boolean` | Enabled allows this provider to create a bastion host instance with a public ip to access the VPC private network. | N/A |
| └>&nbsp;&nbsp; **instanceType** | `string` | InstanceType will use the specified instance type for the bastion. If not specified, Cluster API Provider AWS will use t3.micro for all regions except us-east-1, where t2.micro will be the default. | N/A |
|  **controlPlaneEndpoint** | `object` | ControlPlaneEndpoint represents the endpoint used to communicate with the control plane. | N/A |
| └>&nbsp;&nbsp; **host** | `string` | The hostname on which the API server is serving. | N/A |
| └>&nbsp;&nbsp; **port** | `integer` | The port on which the API server is serving. | N/A |
|  **disableVPCCNI** | `boolean` | DisableVPCCNI indicates that the Amazon VPC CNI should be disabled. With EKS clusters the Amazon VPC CNI is automatically installed into the cluster. For clusters where you want to use an alternate CNI this option provides a way to specify that the Amazon VPC CNI should be deleted. You cannot set this to true if you are using the Amazon VPC CNI addon. | N/A |
|  **eksClusterName** | `string` | EKSClusterName allows you to specify the name of the EKS cluster in AWS. If you don't specify a name then a default name will be created based on the namespace and name of the managed control plane. | N/A |
|  **encryptionConfig** | `object` | EncryptionConfig specifies the encryption configuration for the cluster | N/A |
| └>&nbsp;&nbsp; **provider** | `string` | Provider specifies the ARN or alias of the CMK (in AWS KMS) | N/A |
| └>&nbsp;&nbsp; **resources** | `array` | Resources specifies the resources to be encrypted | N/A |
|  **endpointAccess** | `object` | Endpoints specifies access to this cluster's control plane endpoints | N/A |
| └>&nbsp;&nbsp; **private** | `boolean` | Private points VPC-internal control plane access to the private endpoint | N/A |
| └>&nbsp;&nbsp; **public** | `boolean` | Public controls whether control plane endpoints are publicly accessible | N/A |
| └>&nbsp;&nbsp; **publicCIDRs** | `array` | PublicCIDRs specifies which blocks can access the public endpoint | N/A |
|  **iamAuthenticatorConfig** | `object` | IAMAuthenticatorConfig allows the specification of any additional user or role mappings for use when generating the aws-iam-authenticator configuration. If this is nil the default configuration is still generated for the cluster. | N/A |
| └>&nbsp;&nbsp; **mapRoles** | `array` | RoleMappings is a list of role mappings | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **groups** | `array` | Groups is a list of kubernetes RBAC groups | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **rolearn** | `string` | RoleARN is the AWS ARN for the role to map | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **username** | `string` | UserName is a kubernetes RBAC user subject | N/A |
| └>&nbsp;&nbsp; **mapUsers** | `array` | UserMappings is a list of user mappings | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **groups** | `array` | Groups is a list of kubernetes RBAC groups | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **userarn** | `string` | UserARN is the AWS ARN for the user to map | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **username** | `string` | UserName is a kubernetes RBAC user subject | N/A |
|  **identityRef** | `object` | IdentityRef is a reference to an identity to be used when reconciling the managed control plane. If no identity is specified, the default identity for this controller will be used. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the identity. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the identity. | N/A |
|  **imageLookupBaseOS** | `string` | ImageLookupBaseOS is the name of the base operating system used to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupBaseOS. | N/A |
|  **imageLookupFormat** | `string` | ImageLookupFormat is the AMI naming format to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupOrg. Supports substitutions for {{.BaseOS}} and {{.K8sVersion}} with the base OS and kubernetes version, respectively. The BaseOS will be the value in ImageLookupBaseOS or ubuntu (the default), and the kubernetes version as defined by the packages produced by kubernetes/release without v as a prefix: 1.13.0, 1.12.5-mybuild.1, or 1.17.3. For example, the default image format of capa-ami-{{.BaseOS}}-?{{.K8sVersion}}-* will end up searching for AMIs that match the pattern capa-ami-ubuntu-?1.18.0-* for a Machine that is targeting kubernetes v1.18.0 and the ubuntu base OS. See also: https://golang.org/pkg/text/template/ | N/A |
|  **imageLookupOrg** | `string` | ImageLookupOrg is the AWS Organization ID to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupOrg. | N/A |
|  **kubeProxy** | `object` | KubeProxy defines managed attributes of the kube-proxy daemonset | N/A |
| └>&nbsp;&nbsp; **disable** | `boolean` | Disable set to true indicates that kube-proxy should be disabled. With EKS clusters kube-proxy is automatically installed into the cluster. For clusters where you want to use kube-proxy functionality that is provided with an alternate CNI, this option provides a way to specify that the kube-proxy daemonset should be deleted. You cannot set this to true if you are using the Amazon kube-proxy addon. | N/A |
|  **logging** | `object` | Logging specifies which EKS Cluster logs should be enabled. Entries for each of the enabled logs will be sent to CloudWatch | N/A |
| └>&nbsp;&nbsp; **apiServer** | `boolean` | APIServer indicates if the Kubernetes API Server log (kube-apiserver) shoulkd be enabled | N/A |
| └>&nbsp;&nbsp; **audit** | `boolean` | Audit indicates if the Kubernetes API audit log should be enabled | N/A |
| └>&nbsp;&nbsp; **authenticator** | `boolean` | Authenticator indicates if the iam authenticator log should be enabled | N/A |
| └>&nbsp;&nbsp; **controllerManager** | `boolean` | ControllerManager indicates if the controller manager (kube-controller-manager) log should be enabled | N/A |
| └>&nbsp;&nbsp; **scheduler** | `boolean` | Scheduler indicates if the Kubernetes scheduler (kube-scheduler) log should be enabled | N/A |
|  **network** | `object` | NetworkSpec encapsulates all things related to AWS network. | N/A |
| └>&nbsp;&nbsp; **additionalControlPlaneIngressRules** | `array` | AdditionalControlPlaneIngressRules is an optional set of ingress rules to add to the control plane | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cidrBlocks** | `array` | List of CIDR blocks to allow access from. Cannot be specified with SourceSecurityGroupID. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **description** | `string` | Description provides extended information about the ingress rule. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fromPort** | `integer` | FromPort is the start of port range. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipv6CidrBlocks** | `array` | List of IPv6 CIDR blocks to allow access from. Cannot be specified with SourceSecurityGroupID. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **natGatewaysIPsSource** | `boolean` | NatGatewaysIPsSource use the NAT gateways IPs as the source for the ingress rule. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **protocol** | `string` | Protocol is the protocol for the ingress rule. Accepted values are "-1" (all), "4" (IP in IP),"tcp", "udp", "icmp", and "58" (ICMPv6), "50" (ESP). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sourceSecurityGroupIds** | `array` | The security group id to allow access from. Cannot be specified with CidrBlocks. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sourceSecurityGroupRoles** | `array` | The security group role to allow access from. Cannot be specified with CidrBlocks. The field will be combined with source security group IDs if specified. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **toPort** | `integer` | ToPort is the end of port range. | N/A |
| └>&nbsp;&nbsp; **cni** | `object` | CNI configuration | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cniIngressRules** | `array` | CNIIngressRules specify rules to apply to control plane and worker node security groups. The source for the rule will be set to control plane and worker security group IDs. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **description** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fromPort** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **protocol** | `string` | SecurityGroupProtocol defines the protocol type for a security group rule. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **toPort** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **nodePortIngressRuleCidrBlocks** | `array` | NodePortIngressRuleCidrBlocks is an optional set of CIDR blocks to allow traffic to nodes' NodePort services. If none are specified here, all IPs are allowed to connect. | N/A |
| └>&nbsp;&nbsp; **securityGroupOverrides** | `object` | SecurityGroupOverrides is an optional set of security groups to use for cluster instances This is optional - if not provided new security groups will be created for the cluster | N/A |
| └>&nbsp;&nbsp; **subnets** | `array` | Subnets configuration. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **availabilityZone** | `string` | AvailabilityZone defines the availability zone to use for this subnet in the cluster's region. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cidrBlock** | `string` | CidrBlock is the CIDR block to be used when the provider creates a managed VPC. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID defines a unique identifier to reference this resource. If you're bringing your subnet, set the AWS subnet-id here, it must start with `subnet-`.  When the VPC is managed by CAPA, and you'd like the provider to create a subnet for you, the id can be set to any placeholder value that does not start with `subnet-`; upon creation, the subnet AWS identifier will be populated in the `ResourceID` field and the `id` field is going to be used as the subnet name. If you specify a tag called `Name`, it takes precedence. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipv6CidrBlock** | `string` | IPv6CidrBlock is the IPv6 CIDR block to be used when the provider creates a managed VPC. A subnet can have an IPv4 and an IPv6 address. IPv6 is only supported in managed clusters, this field cannot be set on AWSCluster object. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **isIpv6** | `boolean` | IsIPv6 defines the subnet as an IPv6 subnet. A subnet is IPv6 when it is associated with a VPC that has IPv6 enabled. IPv6 is only supported in managed clusters, this field cannot be set on AWSCluster object. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **isPublic** | `boolean` | IsPublic defines the subnet as a public subnet. A subnet is public when it is associated with a route table that has a route to an internet gateway. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **natGatewayId** | `string` | NatGatewayID is the NAT gateway id associated with the subnet. Ignored unless the subnet is managed by the provider, in which case this is set on the public subnet where the NAT gateway resides. It is then used to determine routes for private subnets in the same AZ as the public subnet. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **parentZoneName** | `string` | ParentZoneName is the zone name where the current subnet's zone is tied when the zone is a Local Zone.  The subnets in Local Zone or Wavelength Zone locations consume the ParentZoneName to select the correct private route table to egress traffic to the internet. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceID** | `string` | ResourceID is the subnet identifier from AWS, READ ONLY. This field is populated when the provider manages the subnet. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **routeTableId** | `string` | RouteTableID is the routing table id associated with the subnet. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tags** | `object` | Tags is a collection of tags describing the resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **zoneType** | `string` | ZoneType defines the type of the zone where the subnet is created.  The valid values are availability-zone, local-zone, and wavelength-zone.  Subnet with zone type availability-zone (regular) is always selected to create cluster resources, like Load Balancers, NAT Gateways, Contol Plane nodes, etc.  Subnet with zone type local-zone or wavelength-zone is not eligible to automatically create regular cluster resources.  The public subnet in availability-zone or local-zone is associated with regular public route table with default route entry to a Internet Gateway.  The public subnet in wavelength-zone is associated with a carrier public route table with default route entry to a Carrier Gateway.  The private subnet in the availability-zone is associated with a private route table with the default route entry to a NAT Gateway created in that zone.  The private subnet in the local-zone or wavelength-zone is associated with a private route table with the default route entry re-using the NAT Gateway in the Region (preferred from the parent zone, the zone type availability-zone in the region, or first table available). | N/A |
| └>&nbsp;&nbsp; **vpc** | `object` | VPC configuration. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **availabilityZoneSelection** | `string` | AvailabilityZoneSelection specifies how AZs should be selected if there are more AZs in a region than specified by AvailabilityZoneUsageLimit. There are 2 selection schemes: Ordered - selects based on alphabetical order Random - selects AZs randomly in a region Defaults to Ordered | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **availabilityZoneUsageLimit** | `integer` | AvailabilityZoneUsageLimit specifies the maximum number of availability zones (AZ) that should be used in a region when automatically creating subnets. If a region has more than this number of AZs then this number of AZs will be picked randomly when creating default subnets. Defaults to 3 | `Minimum=1` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **carrierGatewayId** | `string` | CarrierGatewayID is the id of the internet gateway associated with the VPC, for carrier network (Wavelength Zones). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cidrBlock** | `string` | CidrBlock is the CIDR block to be used when the provider creates a managed VPC. Defaults to 10.0.0.0/16. Mutually exclusive with IPAMPool. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **elasticIpPool** | `object` | ElasticIPPool contains specific configuration to allocate Public IPv4 address (Elastic IP) from user-defined pool brought to AWS for core infrastructure resources, like NAT Gateways and Public Network Load Balancers for the API Server. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **publicIpv4Pool** | `string` | PublicIpv4Pool sets a custom Public IPv4 Pool used to create Elastic IP address for resources created in public IPv4 subnets. Every IPv4 address, Elastic IP, will be allocated from the custom Public IPv4 pool that you brought to AWS, instead of Amazon-provided pool. The public IPv4 pool resource ID starts with 'ipv4pool-ec2'. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **publicIpv4PoolFallbackOrder** | `string` | PublicIpv4PoolFallBackOrder defines the fallback action when the Public IPv4 Pool has been exhausted, no more IPv4 address available in the pool.  When set to 'amazon-pool', the controller check if the pool has available IPv4 address, when pool has reached the IPv4 limit, the address will be claimed from Amazon-pool (default).  When set to 'none', the controller will fail the Elastic IP allocation when the publicIpv4Pool is exhausted. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **emptyRoutesDefaultVPCSecurityGroup** | `boolean` | EmptyRoutesDefaultVPCSecurityGroup specifies whether the default VPC security group ingress and egress rules should be removed.  By default, when creating a VPC, AWS creates a security group called `default` with ingress and egress rules that allow traffic from anywhere. The group could be used as a potential surface attack and it's generally suggested that the group rules are removed or modified appropriately.  NOTE: This only applies when the VPC is managed by the Cluster API AWS controller. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID is the vpc-id of the VPC this provider should use to create resources. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **internetGatewayId** | `string` | InternetGatewayID is the id of the internet gateway associated with the VPC. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipamPool** | `object` | IPAMPool defines the IPAMv4 pool to be used for VPC. Mutually exclusive with CidrBlock. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID is the ID of the IPAM pool this provider should use to create VPC. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the IPAM pool this provider should use to create VPC. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netmaskLength** | `integer` | The netmask length of the IPv4 CIDR you want to allocate to VPC from an Amazon VPC IP Address Manager (IPAM) pool. Defaults to /16 for IPv4 if not specified. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipv6** | `object` | IPv6 contains ipv6 specific settings for the network. Supported only in managed clusters. This field cannot be set on AWSCluster object. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cidrBlock** | `string` | CidrBlock is the CIDR block provided by Amazon when VPC has enabled IPv6. Mutually exclusive with IPAMPool. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **egressOnlyInternetGatewayId** | `string` | EgressOnlyInternetGatewayID is the id of the egress only internet gateway associated with an IPv6 enabled VPC. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipamPool** | `object` | IPAMPool defines the IPAMv6 pool to be used for VPC. Mutually exclusive with CidrBlock. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID is the ID of the IPAM pool this provider should use to create VPC. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the IPAM pool this provider should use to create VPC. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **netmaskLength** | `integer` | The netmask length of the IPv4 CIDR you want to allocate to VPC from an Amazon VPC IP Address Manager (IPAM) pool. Defaults to /16 for IPv4 if not specified. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **poolId** | `string` | PoolID is the IP pool which must be defined in case of BYO IP is defined. Must be specified if CidrBlock is set. Mutually exclusive with IPAMPool. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **privateDnsHostnameTypeOnLaunch** | `string` | PrivateDNSHostnameTypeOnLaunch is the type of hostname to assign to instances in the subnet at launch. For IPv4-only and dual-stack (IPv4 and IPv6) subnets, an instance DNS name can be based on the instance IPv4 address (ip-name) or the instance ID (resource-name). For IPv6 only subnets, an instance DNS name must be based on the instance ID (resource-name). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **secondaryCidrBlocks** | `array` | SecondaryCidrBlocks are additional CIDR blocks to be associated when the provider creates a managed VPC. Defaults to none. Mutually exclusive with IPAMPool. This makes sense to use if, for example, you want to use a separate IP range for pods (e.g. Cilium ENI mode). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipv4CidrBlock** | `string` | IPv4CidrBlock is the IPv4 CIDR block to associate with the managed VPC. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **subnetSchema** | `string` | SubnetSchema specifies how CidrBlock should be divided on subnets in the VPC depending on the number of AZs. PreferPrivate - one private subnet for each AZ plus one other subnet that will be further sub-divided for the public subnets. PreferPublic - have the reverse logic of PreferPrivate, one public subnet for each AZ plus one other subnet that will be further sub-divided for the private subnets. Defaults to PreferPrivate | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tags** | `object` | Tags is a collection of tags describing the resource. | N/A |
|  **oidcIdentityProviderConfig** | `object` | IdentityProviderconfig is used to specify the oidc provider config to be attached with this eks cluster | N/A |
| └>&nbsp;&nbsp; **clientId** | `string` | This is also known as audience. The ID for the client application that makes authentication requests to the OpenID identity provider. | N/A |
| └>&nbsp;&nbsp; **groupsClaim** | `string` | The JWT claim that the provider uses to return your groups. | N/A |
| └>&nbsp;&nbsp; **groupsPrefix** | `string` | The prefix that is prepended to group claims to prevent clashes with existing names (such as system: groups). For example, the valueoidc: will create group names like oidc:engineering and oidc:infra. | N/A |
| └>&nbsp;&nbsp; **identityProviderConfigName** | `string` | The name of the OIDC provider configuration.  IdentityProviderConfigName is a required field | N/A |
| └>&nbsp;&nbsp; **issuerUrl** | `string` | The URL of the OpenID identity provider that allows the API server to discover public signing keys for verifying tokens. The URL must begin with https:// and should correspond to the iss claim in the provider's OIDC ID tokens. Per the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a hostname, like https://server.example.org or https://example.com. This URL should point to the level below .well-known/openid-configuration and must be publicly accessible over the internet. | N/A |
| └>&nbsp;&nbsp; **requiredClaims** | `object` | The key value pairs that describe required claims in the identity token. If set, each claim is verified to be present in the token with a matching value. For the maximum number of claims that you can require, see Amazon EKS service quotas (https://docs.aws.amazon.com/eks/latest/userguide/service-quotas.html) in the Amazon EKS User Guide. | N/A |
| └>&nbsp;&nbsp; **tags** | `object` | tags to apply to oidc identity provider association | N/A |
| └>&nbsp;&nbsp; **usernameClaim** | `string` | The JSON Web Token (JWT) claim to use as the username. The default is sub, which is expected to be a unique identifier of the end user. You can choose other claims, such as email or name, depending on the OpenID identity provider. Claims other than email are prefixed with the issuer URL to prevent naming clashes with other plug-ins. | N/A |
| └>&nbsp;&nbsp; **usernamePrefix** | `string` | The prefix that is prepended to username claims to prevent clashes with existing names. If you do not provide this field, and username is a value other than email, the prefix defaults to issuerurl#. You can use the value - to disable all prefixing. | N/A |
|  **region** | `string` | The AWS Region the cluster lives in. | N/A |
|  **roleAdditionalPolicies** | `array` | RoleAdditionalPolicies allows you to attach additional polices to the control plane role. You must enable the EKSAllowAddRoles feature flag to incorporate these into the created role. | N/A |
|  **roleName** | `string` | RoleName specifies the name of IAM role that gives EKS permission to make API calls. If the role is pre-existing we will treat it as unmanaged and not delete it on deletion. If the EKSEnableIAM feature flag is true and no name is supplied then a role is created. | N/A |
|  **secondaryCidrBlock** | `string` | SecondaryCidrBlock is the additional CIDR range to use for pod IPs. Must be within the 100.64.0.0/10 or 198.19.0.0/16 range. | N/A |
|  **sshKeyName** | `string` | SSHKeyName is the name of the ssh key to attach to the bastion host. Valid values are empty string (do not use SSH keys), a valid SSH key name, or omitted (use the default SSH key name) | N/A |
|  **tokenMethod** | `string` | TokenMethod is used to specify the method for obtaining a client token for communicating with EKS iam-authenticator - obtains a client token using iam-authentictor aws-cli - obtains a client token using the AWS CLI Defaults to iam-authenticator | N/A |
|  **version** | `string` | Version defines the desired Kubernetes version. If no version number is supplied then the latest version of Kubernetes that EKS supports will be used. | `Pattern=^v?(0\|[1-9][0-9]*)\.(0\|[1-9][0-9]*)\.?(\.0\|[1-9][0-9]*)?$` |
|  **vpcCni** | `object` | VpcCni is used to set configuration options for the VPC CNI plugin | N/A |
| └>&nbsp;&nbsp; **env** | `array` | Env defines a list of environment variables to apply to the `aws-node` DaemonSet | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the environment variable. Must be a C_IDENTIFIER. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Variable references $(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **valueFrom** | `object` | Source for the environment variable's value. Cannot be used if value is not empty. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **configMapKeyRef** | `object` | Selects a key of a ConfigMap. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | The key to select. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **optional** | `boolean` | Specify whether the ConfigMap or its key must be defined | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fieldRef** | `object` | Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiVersion** | `string` | Version of the schema the FieldPath is written in terms of, defaults to "v1". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fieldPath** | `string` | Path of the field to select in the specified API version. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceFieldRef** | `object` | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **containerName** | `string` | Container name: required for volumes, optional for env vars | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **divisor** | `N/A` | Specifies the output format of the exposed resources, defaults to "1" | `Pattern=^(\+\|-)?(([0-9]+(\.[0-9]*)?)\|(\.[0-9]+))(([KMGTPE]i)\|[numkMGTPE]\|([eE](\+\|-)?(([0-9]+(\.[0-9]*)?)\|(\.[0-9]+))))?$` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resource** | `string` | Required: resource to select | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **secretKeyRef** | `object` | Selects a key of a secret in the pod's namespace | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | The key of the secret to select from.  Must be a valid secret key. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **optional** | `boolean` | Specify whether the Secret or its key must be defined | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **addons** | `array` | Addons holds the current status of the EKS addons | N/A |
| └>&nbsp;&nbsp; **arn** | `string` | ARN is the AWS ARN of the addon | N/A |
| └>&nbsp;&nbsp; **createdAt** | `string` | CreatedAt is the date and time the addon was created at | N/A |
| └>&nbsp;&nbsp; **issues** | `array` | Issues is a list of issue associated with the addon | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **code** | `string` | Code is the issue code | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **message** | `string` | Message is the textual description of the issue | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceIds** | `array` | ResourceIDs is a list of resource ids for the issue | N/A |
| └>&nbsp;&nbsp; **modifiedAt** | `string` | ModifiedAt is the date and time the addon was last modified | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the addon | N/A |
| └>&nbsp;&nbsp; **serviceAccountRoleARN** | `string` | ServiceAccountRoleArn is the ARN of the IAM role used for the service account | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status is the status of the addon | N/A |
| └>&nbsp;&nbsp; **version** | `string` | Version is the version of the addon to use | N/A |
|  **bastion** | `object` | Bastion holds details of the instance that is used as a bastion jump box | N/A |
| └>&nbsp;&nbsp; **addresses** | `array` | Addresses contains the AWS instance associated addresses. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **address** | `string` | The machine address. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Machine address type, one of Hostname, ExternalIP, InternalIP, ExternalDNS or InternalDNS. | N/A |
| └>&nbsp;&nbsp; **availabilityZone** | `string` | Availability zone of instance | N/A |
| └>&nbsp;&nbsp; **capacityReservationId** | `string` | CapacityReservationID specifies the target Capacity Reservation into which the instance should be launched. | N/A |
| └>&nbsp;&nbsp; **ebsOptimized** | `boolean` | Indicates whether the instance is optimized for Amazon EBS I/O. | N/A |
| └>&nbsp;&nbsp; **enaSupport** | `boolean` | Specifies whether enhanced networking with ENA is enabled. | N/A |
| └>&nbsp;&nbsp; **iamProfile** | `string` | The name of the IAM instance profile associated with the instance, if applicable. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **imageId** | `string` | The ID of the AMI used to launch the instance. | N/A |
| └>&nbsp;&nbsp; **instanceMetadataOptions** | `object` | InstanceMetadataOptions is the metadata options for the EC2 instance. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **httpEndpoint** | `string` | Enables or disables the HTTP metadata endpoint on your instances.  If you specify a value of disabled, you cannot access your instance metadata.  Default: enabled | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **httpPutResponseHopLimit** | `integer` | The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel.  Default: 1 | `Minimum=1`<br>`Maximum=64` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **httpTokens** | `string` | The state of token usage for your instance metadata requests.  If the state is optional, you can choose to retrieve instance metadata with or without a session token on your request. If you retrieve the IAM role credentials without a token, the version 1.0 role credentials are returned. If you retrieve the IAM role credentials using a valid session token, the version 2.0 role credentials are returned.  If the state is required, you must send a session token with any instance metadata retrieval requests. In this state, retrieving the IAM role credentials always returns the version 2.0 credentials; the version 1.0 credentials are not available.  Default: optional | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **instanceMetadataTags** | `string` | Set to enabled to allow access to instance tags from the instance metadata. Set to disabled to turn off access to instance tags from the instance metadata. For more information, see Work with instance tags using the instance metadata (https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#work-with-tags-in-IMDS).  Default: disabled | N/A |
| └>&nbsp;&nbsp; **instanceState** | `string` | The current state of the instance. | N/A |
| └>&nbsp;&nbsp; **marketType** | `string` | MarketType specifies the type of market for the EC2 instance. Valid values include: "OnDemand" (default): The instance runs as a standard OnDemand instance. "Spot": The instance runs as a Spot instance. When SpotMarketOptions is provided, the marketType defaults to "Spot". "CapacityBlock": The instance utilizes pre-purchased compute capacity (capacity blocks) with AWS Capacity Reservations.  If this value is selected, CapacityReservationID must be specified to identify the target reservation. If marketType is not specified and spotMarketOptions is provided, the marketType defaults to "Spot". | N/A |
| └>&nbsp;&nbsp; **networkInterfaceType** | `string` | NetworkInterfaceType is the interface type of the primary network Interface. | N/A |
| └>&nbsp;&nbsp; **networkInterfaces** | `array` | Specifies ENIs attached to instance | N/A |
| └>&nbsp;&nbsp; **nonRootVolumes** | `array` | Configuration options for the non root storage volumes. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **deviceName** | `string` | Device name | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **encrypted** | `boolean` | Encrypted is whether the volume should be encrypted or not. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **encryptionKey** | `string` | EncryptionKey is the KMS key to use to encrypt the volume. Can be either a KMS key ID or ARN. If Encrypted is set and this is omitted, the default AWS key will be used. The key must already exist and be accessible by the controller. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **iops** | `integer` | IOPS is the number of IOPS requested for the disk. Not applicable to all types. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **size** | `integer` | Size specifies size (in Gi) of the storage device. Must be greater than the image snapshot size or 8 (whichever is greater). | `Minimum=8` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **throughput** | `integer` | Throughput to provision in MiB/s supported for the volume type. Not applicable to all types. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type is the type of the volume (e.g. gp2, io1, etc...). | N/A |
| └>&nbsp;&nbsp; **placementGroupName** | `string` | PlacementGroupName specifies the name of the placement group in which to launch the instance. | N/A |
| └>&nbsp;&nbsp; **placementGroupPartition** | `integer` | PlacementGroupPartition is the partition number within the placement group in which to launch the instance. This value is only valid if the placement group, referred in `PlacementGroupName`, was created with strategy set to partition. | `Minimum=1`<br>`Maximum=7` |
| └>&nbsp;&nbsp; **privateDnsName** | `object` | PrivateDNSName is the options for the instance hostname. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **enableResourceNameDnsAAAARecord** | `boolean` | EnableResourceNameDNSAAAARecord indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **enableResourceNameDnsARecord** | `boolean` | EnableResourceNameDNSARecord indicates whether to respond to DNS queries for instance hostnames with DNS A records. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **hostnameType** | `string` | The type of hostname to assign to an instance. | N/A |
| └>&nbsp;&nbsp; **privateIp** | `string` | The private IPv4 address assigned to the instance. | N/A |
| └>&nbsp;&nbsp; **publicIPOnLaunch** | `boolean` | PublicIPOnLaunch is the option to associate a public IP on instance launch | N/A |
| └>&nbsp;&nbsp; **publicIp** | `string` | The public IPv4 address assigned to the instance, if applicable. | N/A |
| └>&nbsp;&nbsp; **rootVolume** | `object` | Configuration options for the root storage volume. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **deviceName** | `string` | Device name | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **encrypted** | `boolean` | Encrypted is whether the volume should be encrypted or not. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **encryptionKey** | `string` | EncryptionKey is the KMS key to use to encrypt the volume. Can be either a KMS key ID or ARN. If Encrypted is set and this is omitted, the default AWS key will be used. The key must already exist and be accessible by the controller. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **iops** | `integer` | IOPS is the number of IOPS requested for the disk. Not applicable to all types. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **size** | `integer` | Size specifies size (in Gi) of the storage device. Must be greater than the image snapshot size or 8 (whichever is greater). | `Minimum=8` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **throughput** | `integer` | Throughput to provision in MiB/s supported for the volume type. Not applicable to all types. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type is the type of the volume (e.g. gp2, io1, etc...). | N/A |
| └>&nbsp;&nbsp; **securityGroupIds** | `array` | SecurityGroupIDs are one or more security group IDs this instance belongs to. | N/A |
| └>&nbsp;&nbsp; **spotMarketOptions** | `object` | SpotMarketOptions option for configuring instances to be run using AWS Spot instances. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **maxPrice** | `string` | MaxPrice defines the maximum price the user is willing to pay for Spot VM instances | N/A |
| └>&nbsp;&nbsp; **sshKeyName** | `string` | The name of the SSH key pair. | N/A |
| └>&nbsp;&nbsp; **subnetId** | `string` | The ID of the subnet of the instance. | N/A |
| └>&nbsp;&nbsp; **tags** | `object` | The tags associated with the instance. | N/A |
| └>&nbsp;&nbsp; **tenancy** | `string` | Tenancy indicates if instance should run on shared or single-tenant hardware. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | The instance type. | N/A |
| └>&nbsp;&nbsp; **userData** | `string` | UserData is the raw data script passed to the instance which is run upon bootstrap. This field must not be base64 encoded and should only be used when running a new instance. | N/A |
| └>&nbsp;&nbsp; **volumeIDs** | `array` | IDs of the instance's volumes | N/A |
|  **conditions** | `array` | Conditions specifies the cpnditions for the managed control plane | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | Last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | A human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | The reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **externalManagedControlPlane** | `boolean` | ExternalManagedControlPlane indicates to cluster-api that the control plane is managed by an external service such as AKS, EKS, GKE, etc. | N/A |
|  **failureDomains** | `object` | FailureDomains specifies a list fo available availability zones that can be used | N/A |
|  **failureMessage** | `string` | ErrorMessage indicates that there is a terminal problem reconciling the state, and will be set to a descriptive error message. | N/A |
|  **identityProviderStatus** | `object` | IdentityProviderStatus holds the status for associated identity provider | N/A |
| └>&nbsp;&nbsp; **arn** | `string` | ARN holds the ARN of associated identity provider | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status holds current status of associated identity provider | N/A |
|  **initialized** | `boolean` | Initialized denotes whether or not the control plane has the uploaded kubernetes config-map. | N/A |
|  **networkStatus** | `object` | Networks holds details about the AWS networking resources used by the control plane | N/A |
| └>&nbsp;&nbsp; **apiServerElb** | `object` | APIServerELB is the Kubernetes api server load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **arn** | `string` | ARN of the load balancer. Unlike the ClassicLB, ARN is used mostly to define and get it. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **attributes** | `object` | ClassicElbAttributes defines extra attributes associated with the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **crossZoneLoadBalancing** | `boolean` | CrossZoneLoadBalancing enables the classic load balancer load balancing. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **idleTimeout** | `integer` | IdleTimeout is time that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **availabilityZones** | `array` | AvailabilityZones is an array of availability zones in the VPC attached to the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dnsName** | `string` | DNSName is the dns name of the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **elbAttributes** | `object` | ELBAttributes defines extra attributes associated with v2 load balancers. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **elbListeners** | `array` | ELBListeners is an array of listeners associated with the load balancer. There must be at least one. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **port** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **protocol** | `string` | ELBProtocol defines listener protocols for a load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **targetGroup** | `object` | TargetGroupSpec specifies target group settings for a given listener. This is created first, and the ARN is then passed to the listener. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the TargetGroup. Must be unique over the same group of listeners. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **port** | `integer` | Port is the exposed port | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **protocol** | `string` | ELBProtocol defines listener protocols for a load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **targetGroupHealthCheck** | `object` | HealthCheck is the elb health check associated with the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **intervalSeconds** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **path** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **port** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **protocol** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **thresholdCount** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **timeoutSeconds** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **unhealthyThresholdCount** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vpcId** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **healthChecks** | `object` | HealthCheck is the classic elb health check associated with the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **healthyThreshold** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **interval** | `integer` | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **target** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **timeout** | `integer` | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **unhealthyThreshold** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **listeners** | `array` | ClassicELBListeners is an array of classic elb listeners associated with the load balancer. There must be at least one. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **instancePort** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **instanceProtocol** | `string` | ELBProtocol defines listener protocols for a load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **port** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **protocol** | `string` | ELBProtocol defines listener protocols for a load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **loadBalancerType** | `string` | LoadBalancerType sets the type for a load balancer. The default type is classic. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | The name of the load balancer. It must be unique within the set of load balancers defined in the region. It also serves as identifier. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **scheme** | `string` | Scheme is the load balancer scheme, either internet-facing or private. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **securityGroupIds** | `array` | SecurityGroupIDs is an array of security groups assigned to the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **subnetIds** | `array` | SubnetIDs is an array of subnets in the VPC attached to the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tags** | `object` | Tags is a map of tags associated with the load balancer. | N/A |
| └>&nbsp;&nbsp; **natGatewaysIPs** | `array` | NatGatewaysIPs contains the public IPs of the NAT Gateways | N/A |
| └>&nbsp;&nbsp; **secondaryAPIServerELB** | `object` | SecondaryAPIServerELB is the secondary Kubernetes api server load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **arn** | `string` | ARN of the load balancer. Unlike the ClassicLB, ARN is used mostly to define and get it. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **attributes** | `object` | ClassicElbAttributes defines extra attributes associated with the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **crossZoneLoadBalancing** | `boolean` | CrossZoneLoadBalancing enables the classic load balancer load balancing. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **idleTimeout** | `integer` | IdleTimeout is time that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **availabilityZones** | `array` | AvailabilityZones is an array of availability zones in the VPC attached to the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dnsName** | `string` | DNSName is the dns name of the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **elbAttributes** | `object` | ELBAttributes defines extra attributes associated with v2 load balancers. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **elbListeners** | `array` | ELBListeners is an array of listeners associated with the load balancer. There must be at least one. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **port** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **protocol** | `string` | ELBProtocol defines listener protocols for a load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **targetGroup** | `object` | TargetGroupSpec specifies target group settings for a given listener. This is created first, and the ARN is then passed to the listener. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the TargetGroup. Must be unique over the same group of listeners. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **port** | `integer` | Port is the exposed port | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **protocol** | `string` | ELBProtocol defines listener protocols for a load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **targetGroupHealthCheck** | `object` | HealthCheck is the elb health check associated with the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **intervalSeconds** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **path** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **port** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **protocol** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **thresholdCount** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **timeoutSeconds** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **unhealthyThresholdCount** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vpcId** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **healthChecks** | `object` | HealthCheck is the classic elb health check associated with the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **healthyThreshold** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **interval** | `integer` | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **target** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **timeout** | `integer` | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **unhealthyThreshold** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **listeners** | `array` | ClassicELBListeners is an array of classic elb listeners associated with the load balancer. There must be at least one. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **instancePort** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **instanceProtocol** | `string` | ELBProtocol defines listener protocols for a load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **port** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **protocol** | `string` | ELBProtocol defines listener protocols for a load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **loadBalancerType** | `string` | LoadBalancerType sets the type for a load balancer. The default type is classic. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | The name of the load balancer. It must be unique within the set of load balancers defined in the region. It also serves as identifier. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **scheme** | `string` | Scheme is the load balancer scheme, either internet-facing or private. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **securityGroupIds** | `array` | SecurityGroupIDs is an array of security groups assigned to the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **subnetIds** | `array` | SubnetIDs is an array of subnets in the VPC attached to the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tags** | `object` | Tags is a map of tags associated with the load balancer. | N/A |
| └>&nbsp;&nbsp; **securityGroups** | `object` | SecurityGroups is a map from the role/kind of the security group to its unique name, if any. | N/A |
|  **oidcProvider** | `object` | OIDCProvider holds the status of the identity provider for this cluster | N/A |
| └>&nbsp;&nbsp; **arn** | `string` | ARN holds the ARN of the provider | N/A |
| └>&nbsp;&nbsp; **trustPolicy** | `string` | TrustPolicy contains the boilerplate IAM trust policy to use for IRSA | N/A |
|  **ready** | `boolean` | Ready denotes that the AWSManagedControlPlane API Server is ready to receive requests and that the VPC infra is ready. | N/A |
