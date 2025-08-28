# MachinePool API

MachinePool is the Schema for the machinepools API

## Spec Fields

MachinePoolSpec defines the desired state of MachinePool

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **autoscaling** | `object` | Autoscaling is the details for auto-scaling the machine pool. Replicas and autoscaling cannot be used together. | N/A |
| └>&nbsp;&nbsp; **maxReplicas** | `integer` | MaxReplicas is the maximum number of replicas for the machine pool. | N/A |
| └>&nbsp;&nbsp; **minReplicas** | `integer` | MinReplicas is the minimum number of replicas for the machine pool. | N/A |
|  **clusterDeploymentRef** | `object` | ClusterDeploymentRef references the cluster deployment to which this machine pool belongs. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
|  **labels** | `object` | Map of label string keys and values that will be applied to the created MachineSet's MachineSpec. This affects the labels that will end up on the *Nodes* (in contrast with the MachineLabels field). This list will overwrite any modifications made to Node labels on an ongoing basis. | N/A |
|  **machineLabels** | `object` | Map of label string keys and values that will be applied to the created MachineSet's MachineTemplateSpec. This affects the labels that will end up on the *Machines* (in contrast with the Labels field). This list will overwrite any modifications made to Machine labels on an ongoing basis. Note: We ignore entries that conflict with generated labels. | N/A |
|  **name** | `string` | Name is the name of the machine pool. | N/A |
|  **platform** | `object` | Platform is configuration for machine pool specific to the platform. When using a MachinePool to control the default worker machines created by installer, these must match the values provided in the install-config. | N/A |
| └>&nbsp;&nbsp; **aws** | `object` | AWS is the configuration used when installing on AWS. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **additionalSecurityGroupIDs** | `array` | AdditionalSecurityGroupIDs contains IDs of additional security groups for machines, where each ID is presented in the format sg-xxxx. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **metadataService** | `object` | EC2MetadataOptions defines metadata service interaction options for EC2 instances in the machine pool. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **authentication** | `string` | Authentication determines whether or not the host requires the use of authentication when interacting with the metadata service. When using authentication, this enforces v2 interaction method (IMDSv2) with the metadata service. When omitted, this means the user has no opinion and the value is left to the platform to choose a good default, which is subject to change over time. The current default is optional. At this point this field represents `HttpTokens` parameter from `InstanceMetadataOptionsRequest` structure in AWS EC2 API https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceMetadataOptionsRequest.html | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **rootVolume** | `object` | EC2RootVolume defines the storage for ec2 instance. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **iops** | `integer` | IOPS defines the iops for the storage. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kmsKeyARN** | `string` | The KMS key that will be used to encrypt the EBS volume. If no key is provided the default KMS key for the account will be used. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetEbsDefaultKmsKeyId.html | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **size** | `integer` | Size defines the size of the storage. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type defines the type of the storage. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **spotMarketOptions** | `object` | SpotMarketOptions allows users to configure instances to be run using AWS Spot instances. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **maxPrice** | `string` | The maximum price the user is willing to pay for their instances Default: On-Demand price | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **subnets** | `array` | Subnets is the list of IDs of subnets to which to attach the machines. There must be exactly one subnet for each availability zone used. These subnets may be public or private. As a special case, for consistency with install-config, you may specify exactly one private and one public subnet for each availability zone. In this case, the public subnets will be filtered out and only the private subnets will be used. If empty/omitted, we will look for subnets in each availability zone tagged with Name=<clusterID>-private-<az> (legacy terraform) or <clusterID>-subnet-private-<az> (CAPA). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | InstanceType defines the ec2 instance type. eg. m4-large | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **userTags** | `object` | UserTags contains the user defined tags to be supplied for the ec2 instance. Note that these will be merged with ClusterDeployment.Spec.Platform.AWS.UserTags, with this field taking precedence when keys collide. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **zones** | `array` | Zones is list of availability zones that can be used. | N/A |
| └>&nbsp;&nbsp; **azure** | `object` | Azure is the configuration used when installing on Azure. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **computeSubnet** | `string` | ComputeSubnet specifies an existing subnet for use by compute nodes. If omitted, the default (${infraID}-worker-subnet) will be used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **networkResourceGroupName** | `string` | NetworkResourceGroupName specifies the network resource group that contains an existing VNet. Ignored unless VirtualNetwork is also specified. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **osDisk** | `object` | OSDisk defines the storage for instance. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **diskEncryptionSet** | `object` | DiskEncryptionSet defines a disk encryption set. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the disk encryption set. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceGroup** | `string` | ResourceGroup defines the Azure resource group used by the disk encryption set. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **subscriptionId** | `string` | SubscriptionID defines the Azure subscription the disk encryption set is in. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **diskSizeGB** | `integer` | DiskSizeGB defines the size of disk in GB. | `Minimum=0` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **diskType** | `string` | DiskType defines the type of disk. For control plane nodes, the valid values are Premium_LRS and StandardSSD_LRS. Default is Premium_LRS. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **osImage** | `object` | OSImage defines the image to use for the OS. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **offer** | `string` | Offer is the offer of the image. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **publisher** | `string` | Publisher is the publisher of the image. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sku** | `string` | SKU is the SKU of the image. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | Version is the version of the image. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **outboundType** | `string` | OutboundType is a strategy for how egress from cluster is achieved. When not specified default is "Loadbalancer". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | InstanceType defines the azure instance type. eg. Standard_DS_V2 | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **virtualNetwork** | `string` | VirtualNetwork specifies the name of an existing VNet for the Machines to use If omitted, the default (${infraID}-vnet) will be used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vmNetworkingType** | `string` | VMNetworkingType specifies whether to enable accelerated networking. Accelerated networking enables single root I/O virtualization (SR-IOV) to a VM, greatly improving its networking performance. eg. values: "Accelerated", "Basic" | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **zones** | `array` | Zones is list of availability zones that can be used. eg. ["1", "2", "3"] | N/A |
| └>&nbsp;&nbsp; **gcp** | `object` | GCP is the configuration used when installing on GCP. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **networkProjectID** | `string` | NetworkProjectID specifies which project the network and subnets exist in when they are not in the main ProjectID. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **onHostMaintenance** | `string` | OnHostMaintenance determines the behavior when a maintenance event occurs that might cause the instance to reboot. This is required to be set to "Terminate" if you want to provision machine with attached GPUs. Otherwise, allowed values are "Migrate" and "Terminate". If omitted, the platform chooses a default, which is subject to change over time, currently that default is "Migrate". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **osDisk** | `object` | OSDisk defines the storage for instances. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **diskSizeGB** | `integer` | DiskSizeGB defines the size of disk in GB. Defaulted internally to 128. | `Minimum=16`<br>`Maximum=65536` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **diskType** | `string` | DiskType defines the type of disk. The valid values at this time are: pd-standard, pd-ssd, local-ssd, pd-balanced, hyperdisk-balanced. Defaulted internally to pd-ssd. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **encryptionKey** | `object` | EncryptionKey defines the KMS key to be used to encrypt the disk. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kmsKey** | `object` | KMSKey is a reference to a KMS Key to use for the encryption. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **keyRing** | `string` | KeyRing is the name of the KMS Key Ring which the KMS Key belongs to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **location** | `string` | Location is the GCP location in which the Key Ring exists. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the customer managed encryption key to be used for the disk encryption. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **projectID** | `string` | ProjectID is the ID of the Project in which the KMS Key Ring exists. Defaults to the VM ProjectID if not set. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kmsKeyServiceAccount** | `string` | KMSKeyServiceAccount is the service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used. See https://cloud.google.com/compute/docs/access/service-accounts#compute_engine_service_account for details on the default service account. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **secureBoot** | `string` | SecureBoot Defines whether the instance should have secure boot enabled. Verifies the digital signature of all boot components, and halts the boot process if signature verification fails. If omitted, the platform chooses a default, which is subject to change over time. Currently that default is "Disabled". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serviceAccount** | `string` | ServiceAccount is the email of a gcp service account to be attached to worker nodes in order to provide the permissions required by the cloud provider. For the default worker MachinePool, it is the user's responsibility to match this to the value provided in the install-config. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | InstanceType defines the GCP instance type. eg. n1-standard-4 | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **userTags** | `array` | userTags has additional keys and values that we will add as tags to the providerSpec of MachineSets that we creates on GCP. Tag key and tag value should be the shortnames of the tag key and tag value resource. Consumer is responsible for using this only for spokes where custom tags are supported. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the key part of the tag. A tag key can have a maximum of 63 characters and cannot be empty. Tag key must begin and end with an alphanumeric character, and must contain only uppercase, lowercase alphanumeric characters, and the following special characters `._-`. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **parentID** | `string` | parentID is the ID of the hierarchical resource where the tags are defined, e.g. at the Organization or the Project level. To find the Organization ID or Project ID refer to the following pages: https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id, https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects. An OrganizationID must consist of decimal numbers, and cannot have leading zeroes. A ProjectID must be 6 to 30 characters in length, can only contain lowercase letters, numbers, and hyphens, and must start with a letter, and cannot end with a hyphen. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | value is the value part of the tag. A tag value can have a maximum of 63 characters and cannot be empty. Tag value must begin and end with an alphanumeric character, and must contain only uppercase, lowercase alphanumeric characters, and the following special characters `_-.@%=+:,*#&(){}[]` and spaces. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **zones** | `array` | Zones is list of availability zones that can be used. | N/A |
| └>&nbsp;&nbsp; **ibmcloud** | `object` | IBMCloud is the configuration used when installing on IBM Cloud. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **bootVolume** | `object` | BootVolume is the configuration for the machine's boot volume. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **encryptionKey** | `string` | EncryptionKey is the CRN referencing a Key Protect or Hyper Protect Crypto Services key to use for volume encryption. If not specified, a provider managed encryption key will be used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dedicatedHosts** | `array` | DedicatedHosts is the configuration for the machine's dedicated host and profile. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the dedicated host to provision the machine on. If specified, machines will be created on pre-existing dedicated host. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **profile** | `string` | Profile is the profile ID for the dedicated host. If specified, new dedicated host will be created for machines. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | InstanceType is the VSI machine profile. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **zones** | `array` | Zones is the list of availability zones used for machines in the pool. | N/A |
| └>&nbsp;&nbsp; **nutanix** | `object` | Nutanix is the configuration used when installing on Nutanix prism central. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **bootType** | `string` | BootType indicates the boot type (Legacy, UEFI or SecureBoot) the Machine's VM uses to boot. If this field is empty or omitted, the VM will use the default boot type "Legacy" to boot. "SecureBoot" depends on "UEFI" boot, i.e., enabling "SecureBoot" means that "UEFI" boot is also enabled. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **categories** | `array` | Categories optionally adds one or more prism categories (each with key and value) for the Machine's VM to associate with. All the category key and value pairs specified must already exist in the prism central. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the prism category key name | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | value is the prism category value associated with the key | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **coresPerSocket** | `integer` | NumCoresPerSocket is the number of cores per socket in a vm. The number of vCPUs on the vm will be NumCPUs times NumCoresPerSocket. For example: 4 CPUs and 4 Cores per socket will result in 16 VPUs. The AHV scheduler treats socket and core allocation exactly the same so there is no benefit to configuring cores over CPUs. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cpus** | `integer` | NumCPUs is the total number of virtual processor cores to assign a vm. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dataDisks** | `array` | DataDisks holds information of the data disks to attach to the Machine's VM | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dataSource** | `object` | dataSource refers to a data source image for the VM disk. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | name is the resource name in the PC | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | type is the identifier type to use for this resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **uuid** | `string` | uuid is the UUID of the resource in the PC. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **deviceProperties** | `object` | deviceProperties are the properties of the disk device. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **adapterType** | `string` | adapterType is the adapter type of the disk address. If the deviceType is "Disk", the valid adapterType can be "SCSI", "IDE", "PCI", "SATA" or "SPAPR". If the deviceType is "CDRom", the valid adapterType can be "IDE" or "SATA". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **deviceIndex** | `integer` | deviceIndex is the index of the disk address. The valid values are non-negative integers, with the default value 0. For a Machine VM, the deviceIndex for the disks with the same deviceType.adapterType combination should start from 0 and increase consecutively afterwards. Note that for each Machine VM, the Disk.SCSI.0 and CDRom.IDE.0 are reserved to be used by the VM's system. So for dataDisks of Disk.SCSI and CDRom.IDE, the deviceIndex should start from 1. | `Minimum=0` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **deviceType** | `string` | deviceType specifies the disk device type. The valid values are "Disk" and "CDRom", and the default is "Disk". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **diskSize** | `N/A` | diskSize is size (in Quantity format) of the disk attached to the VM. See https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Format for the Quantity format and example documentation. The minimum diskSize is 1GB. | `Pattern=^(\+\|-)?(([0-9]+(\.[0-9]*)?)\|(\.[0-9]+))(([KMGTPE]i)\|[numkMGTPE]\|([eE](\+\|-)?(([0-9]+(\.[0-9]*)?)\|(\.[0-9]+))))?$` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **storageConfig** | `object` | storageConfig are the storage configuration parameters of the VM disks. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **diskMode** | `string` | diskMode specifies the disk mode. The valid values are Standard and Flash, and the default is Standard. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **storageContainer** | `object` | storageContainer refers to the storage_container used by the VM disk. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | type is the identifier type to use for this resource. The valid value is "uuid". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **uuid** | `string` | uuid is the UUID of the storage resource in the PC. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **failureDomains** | `array` | FailureDomains optionally configures a list of failure domain names that will be applied to the MachinePool. These names must correspond to failure domains configured in `CD.Spec.Platform.Nutanix`. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **gpus** | `array` | GPUs is a list of GPU devices to attach to the machine's VM. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **deviceID** | `integer` | deviceID is the GPU device ID with the integer value. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | name is the GPU device name | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | type is the identifier type of the GPU device. Valid values are Name and DeviceID. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **memoryMiB** | `integer` | Memory is the size of a VM's memory in MiB. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **osDisk** | `object` | OSDisk defines the storage for instance. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **diskSizeGiB** | `integer` | DiskSizeGiB defines the size of disk in GiB. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **project** | `object` | Project optionally identifies a Prism project for the Machine's VM to associate with. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | name is the resource name in the PC | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | type is the identifier type to use for this resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **uuid** | `string` | uuid is the UUID of the resource in the PC. | N/A |
| └>&nbsp;&nbsp; **openstack** | `object` | OpenStack is the configuration used when installing on OpenStack. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **additionalSecurityGroupIDs** | `array` | AdditionalSecurityGroupIDs contains IDs of additional security groups for machines, where each ID is presented in the UUID format. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **flavor** | `string` | Flavor defines the OpenStack Nova flavor. eg. m1.large The json key here differs from the installer which uses both "computeFlavor" and type "type" depending on which type you're looking at, and the resulting field on the MachineSet is "flavor". We are opting to stay consistent with the end result. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **rootVolume** | `object` | RootVolume defines the root volume for instances in the machine pool. The instances use ephemeral disks if not set. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **size** | `integer` | Size defines the size of the volume in gibibytes (GiB). Required | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type defines the type of the volume. Required | N/A |
| └>&nbsp;&nbsp; **ovirt** | `object` | Ovirt is the configuration used when installing on oVirt. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cpu** | `object` | CPU defines the VM CPU. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cores** | `integer` | Cores is the number of cores per socket. Total CPUs is (Sockets * Cores) | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sockets** | `integer` | Sockets is the number of sockets for a VM. Total CPUs is (Sockets * Cores) | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **memoryMB** | `integer` | MemoryMB is the size of a VM's memory in MiBs. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **osDisk** | `object` | OSDisk is the the root disk of the node. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sizeGB** | `integer` | SizeGB size of the bootable disk in GiB. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vmType** | `string` | VMType defines the workload type of the VM. | N/A |
| └>&nbsp;&nbsp; **vsphere** | `object` | VSphere is the configuration used when installing on vSphere | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **coresPerSocket** | `integer` | NumCoresPerSocket is the number of cores per socket in a vm. The number of vCPUs on the vm will be NumCPUs/NumCoresPerSocket. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cpus** | `integer` | NumCPUs is the total number of virtual processor cores to assign a vm. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **memoryMB** | `integer` | Memory is the size of a VM's memory in MB. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **osDisk** | `object` | OSDisk defines the storage for instance. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **diskSizeGB** | `integer` | DiskSizeGB defines the size of disk in GB. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourcePool** | `string` | ResourcePool is the name of the resource pool that will be used for virtual machines. If it is not present, a default value will be used. | N/A |
|  **replicas** | `integer` | Replicas is the count of machines for this machine pool. Replicas and autoscaling cannot be used together. Default is 1, if autoscaling is not used. | N/A |
|  **taints** | `array` | List of taints that will be applied to the created MachineSet's MachineSpec. This list will overwrite any modifications made to Node taints on an ongoing basis. In case of duplicate entries, first encountered taint Value will be preserved, and the rest collapsed on the corresponding MachineSets. Note that taints are uniquely identified based on key+effect, not just key. | N/A |
| └>&nbsp;&nbsp; **effect** | `string` | Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute. | N/A |
| └>&nbsp;&nbsp; **key** | `string` | Required. The taint key to be applied to a node. | N/A |
| └>&nbsp;&nbsp; **timeAdded** | `string` | TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints. | N/A |
| └>&nbsp;&nbsp; **value** | `string` | The taint value corresponding to the taint key. | N/A |
## Status Fields

MachinePoolStatus defines the observed state of MachinePool

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions includes more detailed status for the cluster deployment | N/A |
| └>&nbsp;&nbsp; **lastProbeTime** | `string` | LastProbeTime is the last time we probed the condition. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the last time the condition transitioned from one status to another. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message is a human-readable message indicating details about last transition. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason is a unique, one-word, CamelCase reason for the condition's last transition. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status is the status of the condition. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type is the type of the condition. | N/A |
|  **controlledByReplica** | `integer` | ControlledByReplica indicates which replica of the hive-machinepool StatefulSet is responsible for this MachinePool. Note that this value indicates the replica that most recently handled the MachinePool. If the hive-machinepool statefulset is scaled up or down, the controlling replica can change, potentially causing logs to be spread across multiple pods. | N/A |
|  **machineSets** | `array` | MachineSets is the status of the machine sets for the machine pool on the remote cluster. | N/A |
| └>&nbsp;&nbsp; **errorMessage** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **errorReason** | `string` | In the event that there is a terminal problem reconciling the replicas, both ErrorReason and ErrorMessage will be set. ErrorReason will be populated with a succinct value suitable for machine interpretation, while ErrorMessage will contain a more verbose string suitable for logging and human consumption. | N/A |
| └>&nbsp;&nbsp; **maxReplicas** | `integer` | MaxReplicas is the maximum number of replicas for the machine set. | N/A |
| └>&nbsp;&nbsp; **minReplicas** | `integer` | MinReplicas is the minimum number of replicas for the machine set. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the machine set. | N/A |
| └>&nbsp;&nbsp; **readyReplicas** | `integer` | The number of ready replicas for this MachineSet. A machine is considered ready when the node has been created and is "Ready". It is transferred as-is from the MachineSet from remote cluster. | N/A |
| └>&nbsp;&nbsp; **replicas** | `integer` | Replicas is the current number of replicas for the machine set. | N/A |
|  **ownedLabels** | `array` | OwnedLabels lists the keys of labels this MachinePool created on the remote MachineSet's MachineSpec. (In contrast with OwnedMachineLabels.) Used to identify labels to remove from the remote MachineSet when they are absent from the MachinePool's spec.labels. | N/A |
|  **ownedMachineLabels** | `array` | OwnedMachineLabels lists the keys of labels this MachinePool created on the remote MachineSet's MachineTemplateSpec. (In contrast with OwnedLabels.) Used to identify labels to remove from the remote MachineSet when they are absent from the MachinePool's spec.machineLabels. | N/A |
|  **ownedTaints** | `array` | OwnedTaints lists identifiers of taints this MachinePool created on the remote MachineSet. Used to identify taints to remove from the remote MachineSet when they are absent from the MachinePool's spec.taints. | N/A |
| └>&nbsp;&nbsp; **effect** | `string` | Effect matches corev1.Taint.Effect. | N/A |
| └>&nbsp;&nbsp; **key** | `string` | Key matches corev1.Taint.Key. | N/A |
|  **replicas** | `integer` | Replicas is the current number of replicas for the machine pool. | N/A |
