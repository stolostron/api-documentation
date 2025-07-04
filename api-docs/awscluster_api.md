# AWSCluster API

## Spec Fields

AWSClusterSpec defines the desired state of an EC2-based Kubernetes cluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **additionalTags** | `object` | AdditionalTags is an optional set of tags to add to AWS resources managed by the AWS provider, in addition to the ones added by default. | N/A |
|  **bastion** | `object` | Bastion contains options to configure the bastion host. | N/A |
| └>&nbsp;&nbsp; **allowedCIDRBlocks** | `array` | AllowedCIDRBlocks is a list of CIDR blocks allowed to access the bastion host. They are set as ingress rules for the Bastion host's Security Group (defaults to 0.0.0.0/0). | N/A |
| └>&nbsp;&nbsp; **ami** | `string` | AMI will use the specified AMI to boot the bastion. If not specified, the AMI will default to one picked out in public space. | N/A |
| └>&nbsp;&nbsp; **disableIngressRules** | `boolean` | DisableIngressRules will ensure there are no Ingress rules in the bastion host's security group. Requires AllowedCIDRBlocks to be empty. | N/A |
| └>&nbsp;&nbsp; **enabled** | `boolean` | Enabled allows this provider to create a bastion host instance with a public ip to access the VPC private network. | N/A |
| └>&nbsp;&nbsp; **instanceType** | `string` | InstanceType will use the specified instance type for the bastion. If not specified, Cluster API Provider AWS will use t3.micro for all regions except us-east-1, where t2.micro will be the default. | N/A |
|  **controlPlaneEndpoint** | `object` | ControlPlaneEndpoint represents the endpoint used to communicate with the control plane. | N/A |
| └>&nbsp;&nbsp; **host** | `string` | The hostname on which the API server is serving. | N/A |
| └>&nbsp;&nbsp; **port** | `integer` | The port on which the API server is serving. | N/A |
|  **controlPlaneLoadBalancer** | `object` | ControlPlaneLoadBalancer is optional configuration for customizing control plane behavior. | N/A |
| └>&nbsp;&nbsp; **additionalSecurityGroups** | `array` | AdditionalSecurityGroups sets the security groups used by the load balancer. Expected to be security group IDs This is optional - if not provided new security groups will be created for the load balancer | N/A |
| └>&nbsp;&nbsp; **crossZoneLoadBalancing** | `boolean` | CrossZoneLoadBalancing enables the classic ELB cross availability zone balancing. With cross-zone load balancing, each load balancer node for your Classic Load Balancer distributes requests evenly across the registered instances in all enabled Availability Zones. If cross-zone load balancing is disabled, each load balancer node distributes requests evenly across the registered instances in its Availability Zone only. Defaults to false. | N/A |
| └>&nbsp;&nbsp; **healthCheckProtocol** | `string` | HealthCheckProtocol sets the protocol type for classic ELB health check target default value is ClassicELBProtocolSSL | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name sets the name of the classic ELB load balancer. As per AWS, the name must be unique within your set of load balancers for the region, must have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and cannot begin or end with a hyphen. Once set, the value cannot be changed. | `Pattern=^[A-Za-z0-9]([A-Za-z0-9]{0,31}\|[-A-Za-z0-9]{0,30}[A-Za-z0-9])$` |
| └>&nbsp;&nbsp; **scheme** | `string` | Scheme sets the scheme of the load balancer (defaults to internet-facing) | N/A |
| └>&nbsp;&nbsp; **subnets** | `array` | Subnets sets the subnets that should be applied to the control plane load balancer (defaults to discovered subnets for managed VPCs or an empty set for unmanaged VPCs) | N/A |
|  **identityRef** | `object` | IdentityRef is a reference to an identity to be used when reconciling the managed control plane. If no identity is specified, the default identity for this controller will be used. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the identity. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the identity. | N/A |
|  **imageLookupBaseOS** | `string` | ImageLookupBaseOS is the name of the base operating system used to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupBaseOS. | N/A |
|  **imageLookupFormat** | `string` | ImageLookupFormat is the AMI naming format to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupOrg. Supports substitutions for  and  with the base OS and kubernetes version, respectively. The BaseOS will be the value in ImageLookupBaseOS or ubuntu (the default), and the kubernetes version as defined by the packages produced by kubernetes/release without v as a prefix: 1.13.0, 1.12.5-mybuild.1, or 1.17.3. For example, the default image format of capa-ami--?-* will end up searching for AMIs that match the pattern capa-ami-ubuntu-?1.18.0-* for a Machine that is targeting kubernetes v1.18.0 and the ubuntu base OS. See also: https://golang.org/pkg/text/template/ | N/A |
|  **imageLookupOrg** | `string` | ImageLookupOrg is the AWS Organization ID to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupOrg. | N/A |
|  **network** | `object` | NetworkSpec encapsulates all things related to AWS network. | N/A |
| └>&nbsp;&nbsp; **cni** | `object` | CNI configuration | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cniIngressRules** | `array` | CNIIngressRules specify rules to apply to control plane and worker node security groups. The source for the rule will be set to control plane and worker security group IDs. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **description** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fromPort** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **protocol** | `string` | SecurityGroupProtocol defines the protocol type for a security group rule. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **toPort** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **securityGroupOverrides** | `object` | SecurityGroupOverrides is an optional set of security groups to use for cluster instances This is optional - if not provided new security groups will be created for the cluster | N/A |
| └>&nbsp;&nbsp; **subnets** | `array` | Subnets configuration. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **availabilityZone** | `string` | AvailabilityZone defines the availability zone to use for this subnet in the cluster's region. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cidrBlock** | `string` | CidrBlock is the CIDR block to be used when the provider creates a managed VPC. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID defines a unique identifier to reference this resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipv6CidrBlock** | `string` | IPv6CidrBlock is the IPv6 CIDR block to be used when the provider creates a managed VPC. A subnet can have an IPv4 and an IPv6 address. IPv6 is only supported in managed clusters, this field cannot be set on AWSCluster object. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **isIpv6** | `boolean` | IsIPv6 defines the subnet as an IPv6 subnet. A subnet is IPv6 when it is associated with a VPC that has IPv6 enabled. IPv6 is only supported in managed clusters, this field cannot be set on AWSCluster object. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **isPublic** | `boolean` | IsPublic defines the subnet as a public subnet. A subnet is public when it is associated with a route table that has a route to an internet gateway. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **natGatewayId** | `string` | NatGatewayID is the NAT gateway id associated with the subnet. Ignored unless the subnet is managed by the provider, in which case this is set on the public subnet where the NAT gateway resides. It is then used to determine routes for private subnets in the same AZ as the public subnet. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **routeTableId** | `string` | RouteTableID is the routing table id associated with the subnet. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tags** | `object` | Tags is a collection of tags describing the resource. | N/A |
| └>&nbsp;&nbsp; **vpc** | `object` | VPC configuration. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **availabilityZoneSelection** | `string` | AvailabilityZoneSelection specifies how AZs should be selected if there are more AZs in a region than specified by AvailabilityZoneUsageLimit. There are 2 selection schemes: Ordered - selects based on alphabetical order Random - selects AZs randomly in a region Defaults to Ordered | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **availabilityZoneUsageLimit** | `integer` | AvailabilityZoneUsageLimit specifies the maximum number of availability zones (AZ) that should be used in a region when automatically creating subnets. If a region has more than this number of AZs then this number of AZs will be picked randomly when creating default subnets. Defaults to 3 | `Minimum=1` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cidrBlock** | `string` | CidrBlock is the CIDR block to be used when the provider creates a managed VPC. Defaults to 10.0.0.0/16. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID is the vpc-id of the VPC this provider should use to create resources. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **internetGatewayId** | `string` | InternetGatewayID is the id of the internet gateway associated with the VPC. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipv6** | `object` | IPv6 contains ipv6 specific settings for the network. Supported only in managed clusters. This field cannot be set on AWSCluster object. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cidrBlock** | `string` | CidrBlock is the CIDR block provided by Amazon when VPC has enabled IPv6. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **egressOnlyInternetGatewayId** | `string` | EgressOnlyInternetGatewayID is the id of the egress only internet gateway associated with an IPv6 enabled VPC. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **poolId** | `string` | PoolID is the IP pool which must be defined in case of BYO IP is defined. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tags** | `object` | Tags is a collection of tags describing the resource. | N/A |
|  **region** | `string` | The AWS Region the cluster lives in. | N/A |
|  **s3Bucket** | `object` | S3Bucket contains options to configure a supporting S3 bucket for this cluster - currently used for nodes requiring Ignition (https://coreos.github.io/ignition/) for bootstrapping (requires BootstrapFormatIgnition feature flag to be enabled). | N/A |
| └>&nbsp;&nbsp; **controlPlaneIAMInstanceProfile** | `string` | ControlPlaneIAMInstanceProfile is a name of the IAMInstanceProfile, which will be allowed to read control-plane node bootstrap data from S3 Bucket. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name defines name of S3 Bucket to be created. | `Pattern=^[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]$` |
| └>&nbsp;&nbsp; **nodesIAMInstanceProfiles** | `array` | NodesIAMInstanceProfiles is a list of IAM instance profiles, which will be allowed to read worker nodes bootstrap data from S3 Bucket. | N/A |
|  **sshKeyName** | `string` | SSHKeyName is the name of the ssh key to attach to the bastion host. Valid values are empty string (do not use SSH keys), a valid SSH key name, or omitted (use the default SSH key name) | N/A |
## Status Fields

AWSClusterStatus defines the observed state of AWSCluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **bastion** | `object` | Instance describes an AWS instance. | N/A |
| └>&nbsp;&nbsp; **addresses** | `array` | Addresses contains the AWS instance associated addresses. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **address** | `string` | The machine address. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Machine address type, one of Hostname, ExternalIP, InternalIP, ExternalDNS or InternalDNS. | N/A |
| └>&nbsp;&nbsp; **availabilityZone** | `string` | Availability zone of instance | N/A |
| └>&nbsp;&nbsp; **ebsOptimized** | `boolean` | Indicates whether the instance is optimized for Amazon EBS I/O. | N/A |
| └>&nbsp;&nbsp; **enaSupport** | `boolean` | Specifies whether enhanced networking with ENA is enabled. | N/A |
| └>&nbsp;&nbsp; **iamProfile** | `string` | The name of the IAM instance profile associated with the instance, if applicable. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **imageId** | `string` | The ID of the AMI used to launch the instance. | N/A |
| └>&nbsp;&nbsp; **instanceState** | `string` | The current state of the instance. | N/A |
| └>&nbsp;&nbsp; **networkInterfaces** | `array` | Specifies ENIs attached to instance | N/A |
| └>&nbsp;&nbsp; **nonRootVolumes** | `array` | Configuration options for the non root storage volumes. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **deviceName** | `string` | Device name | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **encrypted** | `boolean` | Encrypted is whether the volume should be encrypted or not. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **encryptionKey** | `string` | EncryptionKey is the KMS key to use to encrypt the volume. Can be either a KMS key ID or ARN. If Encrypted is set and this is omitted, the default AWS key will be used. The key must already exist and be accessible by the controller. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **iops** | `integer` | IOPS is the number of IOPS requested for the disk. Not applicable to all types. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **size** | `integer` | Size specifies size (in Gi) of the storage device. Must be greater than the image snapshot size or 8 (whichever is greater). | `Minimum=8` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **throughput** | `integer` | Throughput to provision in MiB/s supported for the volume type. Not applicable to all types. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type is the type of the volume (e.g. gp2, io1, etc...). | N/A |
| └>&nbsp;&nbsp; **privateIp** | `string` | The private IPv4 address assigned to the instance. | N/A |
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
|  **conditions** | `array` | Conditions provide observations of the operational state of a Cluster API resource. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | Last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | A human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | The reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **failureDomains** | `object` | FailureDomains is a slice of FailureDomains. | N/A |
|  **networkStatus** | `object` | NetworkStatus encapsulates AWS networking resources. | N/A |
| └>&nbsp;&nbsp; **apiServerElb** | `object` | APIServerELB is the Kubernetes api server classic load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **attributes** | `object` | Attributes defines extra attributes associated with the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **crossZoneLoadBalancing** | `boolean` | CrossZoneLoadBalancing enables the classic load balancer load balancing. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **idleTimeout** | `integer` | IdleTimeout is time that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **availabilityZones** | `array` | AvailabilityZones is an array of availability zones in the VPC attached to the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dnsName** | `string` | DNSName is the dns name of the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **healthChecks** | `object` | HealthCheck is the classic elb health check associated with the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **healthyThreshold** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **interval** | `integer` | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **target** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **timeout** | `integer` | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **unhealthyThreshold** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **listeners** | `array` | Listeners is an array of classic elb listeners associated with the load balancer. There must be at least one. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **instancePort** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **instanceProtocol** | `string` | ClassicELBProtocol defines listener protocols for a classic load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **port** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **protocol** | `string` | ClassicELBProtocol defines listener protocols for a classic load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | The name of the load balancer. It must be unique within the set of load balancers defined in the region. It also serves as identifier. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **scheme** | `string` | Scheme is the load balancer scheme, either internet-facing or private. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **securityGroupIds** | `array` | SecurityGroupIDs is an array of security groups assigned to the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **subnetIds** | `array` | SubnetIDs is an array of subnets in the VPC attached to the load balancer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tags** | `object` | Tags is a map of tags associated with the load balancer. | N/A |
| └>&nbsp;&nbsp; **securityGroups** | `object` | SecurityGroups is a map from the role/kind of the security group to its unique name, if any. | N/A |
|  **ready** | `boolean` | No description provided. | N/A |
