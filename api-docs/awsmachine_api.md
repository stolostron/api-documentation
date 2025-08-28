# AWSMachine API

AWSMachine is the schema for Amazon EC2 machines.

## Spec Fields

AWSMachineSpec defines the desired state of an Amazon EC2 instance.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **additionalSecurityGroups** | `array` | AdditionalSecurityGroups is an array of references to security groups that should be applied to the instance. These security groups would be set in addition to any security groups defined at the cluster level or in the actuator. It is possible to specify either IDs of Filters. Using Filters will cause additional requests to AWS API and if tags change the attached security groups might change too. | N/A |
| └>&nbsp;&nbsp; **arn** | `string` | ARN of resource. Deprecated: This field has no function and is going to be removed in the next release. | N/A |
| └>&nbsp;&nbsp; **filters** | `array` | Filters is a set of key/value pairs used to identify a resource They are applied according to the rules defined by the AWS API: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the filter. Filter names are case-sensitive. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | Values includes one or more filter values. Filter values are case-sensitive. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | ID of resource | N/A |
|  **additionalTags** | `object` | AdditionalTags is an optional set of tags to add to an instance, in addition to the ones added by default by the AWS provider. If both the AWSCluster and the AWSMachine specify the same tag name with different values, the AWSMachine's value takes precedence. | N/A |
|  **ami** | `object` | AMI is the reference to the AMI from which to create the machine instance. | N/A |
| └>&nbsp;&nbsp; **eksLookupType** | `string` | EKSOptimizedLookupType If specified, will look up an EKS Optimized image in SSM Parameter store | N/A |
| └>&nbsp;&nbsp; **id** | `string` | ID of resource | N/A |
|  **cloudInit** | `object` | CloudInit defines options related to the bootstrapping systems where CloudInit is used. | N/A |
| └>&nbsp;&nbsp; **insecureSkipSecretsManager** | `boolean` | InsecureSkipSecretsManager, when set to true will not use AWS Secrets Manager or AWS Systems Manager Parameter Store to ensure privacy of userdata. By default, a cloud-init boothook shell script is prepended to download the userdata from Secrets Manager and additionally delete the secret. | N/A |
| └>&nbsp;&nbsp; **secretCount** | `integer` | SecretCount is the number of secrets used to form the complete secret | N/A |
| └>&nbsp;&nbsp; **secretPrefix** | `string` | SecretPrefix is the prefix for the secret name. This is stored temporarily, and deleted when the machine registers as a node against the workload cluster. | N/A |
| └>&nbsp;&nbsp; **secureSecretsBackend** | `string` | SecureSecretsBackend, when set to parameter-store will utilize the AWS Systems Manager Parameter Storage to distribute secrets. By default or with the value of secrets-manager, will use AWS Secrets Manager instead. | N/A |
|  **failureDomain** | `string` | FailureDomain is the failure domain unique identifier this Machine should be attached to, as defined in Cluster API. For this infrastructure provider, the ID is equivalent to an AWS Availability Zone. If multiple subnets are matched for the availability zone, the first one returned is picked. | N/A |
|  **iamInstanceProfile** | `string` | IAMInstanceProfile is a name of an IAM instance profile to assign to the instance | N/A |
|  **ignition** | `object` | Ignition defined options related to the bootstrapping systems where Ignition is used. | N/A |
| └>&nbsp;&nbsp; **version** | `string` | Version defines which version of Ignition will be used to generate bootstrap data. | N/A |
|  **imageLookupBaseOS** | `string` | ImageLookupBaseOS is the name of the base operating system to use for image lookup the AMI is not set. | N/A |
|  **imageLookupFormat** | `string` | ImageLookupFormat is the AMI naming format to look up the image for this machine It will be ignored if an explicit AMI is set. Supports substitutions for  and  with the base OS and kubernetes version, respectively. The BaseOS will be the value in ImageLookupBaseOS or ubuntu (the default), and the kubernetes version as defined by the packages produced by kubernetes/release without v as a prefix: 1.13.0, 1.12.5-mybuild.1, or 1.17.3. For example, the default image format of capa-ami--?-* will end up searching for AMIs that match the pattern capa-ami-ubuntu-?1.18.0-* for a Machine that is targeting kubernetes v1.18.0 and the ubuntu base OS. See also: https://golang.org/pkg/text/template/ | N/A |
|  **imageLookupOrg** | `string` | ImageLookupOrg is the AWS Organization ID to use for image lookup if AMI is not set. | N/A |
|  **instanceID** | `string` | InstanceID is the EC2 instance ID for this machine. | N/A |
|  **instanceType** | `string` | InstanceType is the type of instance to create. Example: m4.xlarge | N/A |
|  **networkInterfaces** | `array` | NetworkInterfaces is a list of ENIs to associate with the instance. A maximum of 2 may be specified. | N/A |
|  **nonRootVolumes** | `array` | Configuration options for the non root storage volumes. | N/A |
| └>&nbsp;&nbsp; **deviceName** | `string` | Device name | N/A |
| └>&nbsp;&nbsp; **encrypted** | `boolean` | Encrypted is whether the volume should be encrypted or not. | N/A |
| └>&nbsp;&nbsp; **encryptionKey** | `string` | EncryptionKey is the KMS key to use to encrypt the volume. Can be either a KMS key ID or ARN. If Encrypted is set and this is omitted, the default AWS key will be used. The key must already exist and be accessible by the controller. | N/A |
| └>&nbsp;&nbsp; **iops** | `integer` | IOPS is the number of IOPS requested for the disk. Not applicable to all types. | N/A |
| └>&nbsp;&nbsp; **size** | `integer` | Size specifies size (in Gi) of the storage device. Must be greater than the image snapshot size or 8 (whichever is greater). | `Minimum=8` |
| └>&nbsp;&nbsp; **throughput** | `integer` | Throughput to provision in MiB/s supported for the volume type. Not applicable to all types. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type is the type of the volume (e.g. gp2, io1, etc...). | N/A |
|  **providerID** | `string` | ProviderID is the unique identifier as specified by the cloud provider. | N/A |
|  **publicIP** | `boolean` | PublicIP specifies whether the instance should get a public IP. Precedence for this setting is as follows: 1. This field if set 2. Cluster/flavor setting 3. Subnet default | N/A |
|  **rootVolume** | `object` | RootVolume encapsulates the configuration options for the root volume | N/A |
| └>&nbsp;&nbsp; **deviceName** | `string` | Device name | N/A |
| └>&nbsp;&nbsp; **encrypted** | `boolean` | Encrypted is whether the volume should be encrypted or not. | N/A |
| └>&nbsp;&nbsp; **encryptionKey** | `string` | EncryptionKey is the KMS key to use to encrypt the volume. Can be either a KMS key ID or ARN. If Encrypted is set and this is omitted, the default AWS key will be used. The key must already exist and be accessible by the controller. | N/A |
| └>&nbsp;&nbsp; **iops** | `integer` | IOPS is the number of IOPS requested for the disk. Not applicable to all types. | N/A |
| └>&nbsp;&nbsp; **size** | `integer` | Size specifies size (in Gi) of the storage device. Must be greater than the image snapshot size or 8 (whichever is greater). | `Minimum=8` |
| └>&nbsp;&nbsp; **throughput** | `integer` | Throughput to provision in MiB/s supported for the volume type. Not applicable to all types. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type is the type of the volume (e.g. gp2, io1, etc...). | N/A |
|  **spotMarketOptions** | `object` | SpotMarketOptions allows users to configure instances to be run using AWS Spot instances. | N/A |
| └>&nbsp;&nbsp; **maxPrice** | `string` | MaxPrice defines the maximum price the user is willing to pay for Spot VM instances | N/A |
|  **sshKeyName** | `string` | SSHKeyName is the name of the ssh key to attach to the instance. Valid values are empty string (do not use SSH keys), a valid SSH key name, or omitted (use the default SSH key name) | N/A |
|  **subnet** | `object` | Subnet is a reference to the subnet to use for this instance. If not specified, the cluster subnet will be used. | N/A |
| └>&nbsp;&nbsp; **arn** | `string` | ARN of resource. Deprecated: This field has no function and is going to be removed in the next release. | N/A |
| └>&nbsp;&nbsp; **filters** | `array` | Filters is a set of key/value pairs used to identify a resource They are applied according to the rules defined by the AWS API: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the filter. Filter names are case-sensitive. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | Values includes one or more filter values. Filter values are case-sensitive. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | ID of resource | N/A |
|  **tenancy** | `string` | Tenancy indicates if instance should run on shared or single-tenant hardware. | N/A |
|  **uncompressedUserData** | `boolean` | UncompressedUserData specify whether the user data is gzip-compressed before it is sent to ec2 instance. cloud-init has built-in support for gzip-compressed user data user data stored in aws secret manager is always gzip-compressed. | N/A |
## Status Fields

AWSMachineStatus defines the observed state of AWSMachine.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **addresses** | `array` | Addresses contains the AWS instance associated addresses. | N/A |
| └>&nbsp;&nbsp; **address** | `string` | The machine address. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Machine address type, one of Hostname, ExternalIP, InternalIP, ExternalDNS or InternalDNS. | N/A |
|  **conditions** | `array` | Conditions defines current service state of the AWSMachine. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | Last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | A human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | The reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **failureMessage** | `string` | FailureMessage will be set in the event that there is a terminal problem reconciling the Machine and will contain a more verbose string suitable for logging and human consumption. This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the Machine's spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured. Any transient errors that occur during the reconciliation of Machines can be added as events to the Machine object and/or logged in the controller's output. | N/A |
|  **failureReason** | `string` | FailureReason will be set in the event that there is a terminal problem reconciling the Machine and will contain a succinct value suitable for machine interpretation. This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the Machine's spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured. Any transient errors that occur during the reconciliation of Machines can be added as events to the Machine object and/or logged in the controller's output. | N/A |
|  **instanceState** | `string` | InstanceState is the state of the AWS instance for this machine. | N/A |
|  **interruptible** | `boolean` | Interruptible reports that this machine is using spot instances and can therefore be interrupted by CAPI when it receives a notice that the spot instance is to be terminated by AWS. This will be set to true when SpotMarketOptions is not nil (i.e. this machine is using a spot instance). | N/A |
|  **ready** | `boolean` | Ready is true when the provider resource is ready. | N/A |
