# AWSMachinePool API

AWSMachinePool is the Schema for the awsmachinepools API.

## Spec Fields

AWSMachinePoolSpec defines the desired state of AWSMachinePool.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **additionalTags** | `object` | AdditionalTags is an optional set of tags to add to an instance, in addition to the ones added by default by the AWS provider. | N/A |
|  **availabilityZones** | `array` | AvailabilityZones is an array of availability zones instances can run in | N/A |
|  **awsLaunchTemplate** | `object` | AWSLaunchTemplate specifies the launch template and version to use when an instance is launched. | N/A |
| └>&nbsp;&nbsp; **additionalSecurityGroups** | `array` | AdditionalSecurityGroups is an array of references to security groups that should be applied to the instances. These security groups would be set in addition to any security groups defined at the cluster level or in the actuator. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **filters** | `array` | Filters is a set of key/value pairs used to identify a resource They are applied according to the rules defined by the AWS API: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the filter. Filter names are case-sensitive. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | Values includes one or more filter values. Filter values are case-sensitive. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID of resource | N/A |
| └>&nbsp;&nbsp; **ami** | `object` | AMI is the reference to the AMI from which to create the machine instance. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **eksLookupType** | `string` | EKSOptimizedLookupType If specified, will look up an EKS Optimized image in SSM Parameter store | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID of resource | N/A |
| └>&nbsp;&nbsp; **iamInstanceProfile** | `string` | The name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance. The instance profile contains the IAM role. | N/A |
| └>&nbsp;&nbsp; **imageLookupBaseOS** | `string` | ImageLookupBaseOS is the name of the base operating system to use for image lookup the AMI is not set. | N/A |
| └>&nbsp;&nbsp; **imageLookupFormat** | `string` | ImageLookupFormat is the AMI naming format to look up the image for this machine It will be ignored if an explicit AMI is set. Supports substitutions for  and  with the base OS and kubernetes version, respectively. The BaseOS will be the value in ImageLookupBaseOS or ubuntu (the default), and the kubernetes version as defined by the packages produced by kubernetes/release without v as a prefix: 1.13.0, 1.12.5-mybuild.1, or 1.17.3. For example, the default image format of capa-ami--?-* will end up searching for AMIs that match the pattern capa-ami-ubuntu-?1.18.0-* for a Machine that is targeting kubernetes v1.18.0 and the ubuntu base OS. See also: https://golang.org/pkg/text/template/ | N/A |
| └>&nbsp;&nbsp; **imageLookupOrg** | `string` | ImageLookupOrg is the AWS Organization ID to use for image lookup if AMI is not set. | N/A |
| └>&nbsp;&nbsp; **instanceType** | `string` | InstanceType is the type of instance to create. Example: m4.xlarge | N/A |
| └>&nbsp;&nbsp; **name** | `string` | The name of the launch template. | N/A |
| └>&nbsp;&nbsp; **rootVolume** | `object` | RootVolume encapsulates the configuration options for the root volume | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **deviceName** | `string` | Device name | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **encrypted** | `boolean` | Encrypted is whether the volume should be encrypted or not. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **encryptionKey** | `string` | EncryptionKey is the KMS key to use to encrypt the volume. Can be either a KMS key ID or ARN. If Encrypted is set and this is omitted, the default AWS key will be used. The key must already exist and be accessible by the controller. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **iops** | `integer` | IOPS is the number of IOPS requested for the disk. Not applicable to all types. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **size** | `integer` | Size specifies size (in Gi) of the storage device. Must be greater than the image snapshot size or 8 (whichever is greater). | `Minimum=8` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **throughput** | `integer` | Throughput to provision in MiB/s supported for the volume type. Not applicable to all types. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type is the type of the volume (e.g. gp2, io1, etc...). | N/A |
| └>&nbsp;&nbsp; **spotMarketOptions** | `object` | SpotMarketOptions are options for configuring AWSMachinePool instances to be run using AWS Spot instances. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **maxPrice** | `string` | MaxPrice defines the maximum price the user is willing to pay for Spot VM instances | N/A |
| └>&nbsp;&nbsp; **sshKeyName** | `string` | SSHKeyName is the name of the ssh key to attach to the instance. Valid values are empty string (do not use SSH keys), a valid SSH key name, or omitted (use the default SSH key name) | N/A |
| └>&nbsp;&nbsp; **versionNumber** | `integer` | VersionNumber is the version of the launch template that is applied. Typically a new version is created when at least one of the following happens: 1) A new launch template spec is applied. 2) One or more parameters in an existing template is changed. 3) A new AMI is discovered. | N/A |
|  **capacityRebalance** | `boolean` | Enable or disable the capacity rebalance autoscaling group feature | N/A |
|  **defaultCoolDown** | `string` | The amount of time, in seconds, after a scaling activity completes before another scaling activity can start. If no value is supplied by user a default value of 300 seconds is set | N/A |
|  **maxSize** | `integer` | MaxSize defines the maximum size of the group. | `Minimum=1` |
|  **minSize** | `integer` | MinSize defines the minimum size of the group. | `Minimum=0` |
|  **mixedInstancesPolicy** | `object` | MixedInstancesPolicy describes how multiple instance types will be used by the ASG. | N/A |
| └>&nbsp;&nbsp; **instancesDistribution** | `object` | InstancesDistribution to configure distribution of On-Demand Instances and Spot Instances. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **onDemandAllocationStrategy** | `string` | OnDemandAllocationStrategy indicates how to allocate instance types to fulfill On-Demand capacity. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **onDemandBaseCapacity** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **onDemandPercentageAboveBaseCapacity** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **spotAllocationStrategy** | `string` | SpotAllocationStrategy indicates how to allocate instances across Spot Instance pools. | N/A |
| └>&nbsp;&nbsp; **overrides** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **instanceType** | `string` | No description provided. | N/A |
|  **providerID** | `string` | ProviderID is the ARN of the associated ASG | N/A |
|  **providerIDList** | `array` | ProviderIDList are the identification IDs of machine instances provided by the provider. This field must match the provider IDs as seen on the node objects corresponding to a machine pool's machine instances. | N/A |
|  **refreshPreferences** | `object` | RefreshPreferences describes set of preferences associated with the instance refresh request. | N/A |
| └>&nbsp;&nbsp; **instanceWarmup** | `integer` | The number of seconds until a newly launched instance is configured and ready to use. During this time, the next replacement will not be initiated. The default is to use the value for the health check grace period defined for the group. | N/A |
| └>&nbsp;&nbsp; **minHealthyPercentage** | `integer` | The amount of capacity as a percentage in ASG that must remain healthy during an instance refresh. The default is 90. | N/A |
| └>&nbsp;&nbsp; **strategy** | `string` | The strategy to use for the instance refresh. The only valid value is Rolling. A rolling update is an update that is applied to all instances in an Auto Scaling group until all instances have been updated. | N/A |
|  **subnets** | `array` | Subnets is an array of subnet configurations | N/A |
| └>&nbsp;&nbsp; **filters** | `array` | Filters is a set of key/value pairs used to identify a resource They are applied according to the rules defined by the AWS API: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the filter. Filter names are case-sensitive. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | Values includes one or more filter values. Filter values are case-sensitive. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | ID of resource | N/A |
## Status Fields

AWSMachinePoolStatus defines the observed state of AWSMachinePool.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **asgStatus** | `string` | ASGStatus is a status string returned by the autoscaling API. | N/A |
|  **conditions** | `array` | Conditions defines current service state of the AWSMachinePool. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | Last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | A human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | The reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **failureMessage** | `string` | FailureMessage will be set in the event that there is a terminal problem reconciling the Machine and will contain a more verbose string suitable for logging and human consumption. This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the Machine's spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured. Any transient errors that occur during the reconciliation of Machines can be added as events to the Machine object and/or logged in the controller's output. | N/A |
|  **failureReason** | `string` | FailureReason will be set in the event that there is a terminal problem reconciling the Machine and will contain a succinct value suitable for machine interpretation. This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the Machine's spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured. Any transient errors that occur during the reconciliation of Machines can be added as events to the Machine object and/or logged in the controller's output. | N/A |
|  **instances** | `array` | Instances contains the status for each instance in the pool | N/A |
| └>&nbsp;&nbsp; **instanceID** | `string` | InstanceID is the identification of the Machine Instance within ASG | N/A |
| └>&nbsp;&nbsp; **version** | `string` | Version defines the Kubernetes version for the Machine Instance | N/A |
|  **launchTemplateID** | `string` | The ID of the launch template | N/A |
|  **launchTemplateVersion** | `string` | The version of the launch template | N/A |
|  **ready** | `boolean` | Ready is true when the provider resource is ready. | N/A |
|  **replicas** | `integer` | Replicas is the most recently observed number of replicas | N/A |
