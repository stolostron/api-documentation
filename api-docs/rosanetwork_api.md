# ROSANetwork API

ROSANetwork is the schema for the rosanetworks API

## Spec Fields

ROSANetworkSpec defines the desired state of ROSANetwork

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **availabilityZoneCount** | `integer` | The number of availability zones to be used for creation of the network infrastructure. You can specify anything between one and four, depending on the chosen AWS region. | N/A |
|  **availabilityZones** | `array` | The list of availability zones to be used for creation of the network infrastructure. You can specify anything between one and four valid availability zones from a given region. Should you specify both the availabilityZoneCount and availabilityZones, the list of availability zones takes preference. | N/A |
|  **cidrBlock** | `string` | CIDR block to be used for the VPC | N/A |
|  **identityRef** | `object` | IdentityRef is a reference to an identity to be used when reconciling rosa network. If no identity is specified, the default identity for this controller will be used. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the identity. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the identity. | N/A |
|  **region** | `string` | The AWS region in which the components of ROSA network infrastruture are to be crated | N/A |
|  **stackName** | `string` | The name of the cloudformation stack under which the network infrastructure would be created | N/A |
|  **stackTags** | `object` | StackTags is an optional set of tags to add to the created cloudformation stack. The stack tags will then be automatically applied to the supported AWS resources (VPC, subnets, ...). | N/A |
## Status Fields

ROSANetworkStatus defines the observed state of ROSANetwork

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions specifies the conditions for ROSANetwork | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | reason is the reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **resources** | `array` | Resources created in the cloudformation stack | N/A |
| └>&nbsp;&nbsp; **logicalId** | `string` | LogicalResourceID of the created resource. | N/A |
| └>&nbsp;&nbsp; **physicalId** | `string` | PhysicalResourceID of the created resource. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Message pertaining to the status of the resource | N/A |
| └>&nbsp;&nbsp; **resource** | `string` | Type of the created resource: AWS::EC2::VPC, AWS::EC2::Subnet, ... | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status of the resource: CREATE_IN_PROGRESS, CREATE_COMPLETE, ... | N/A |
|  **subnets** | `array` | Array of created private, public subnets and availability zones, grouped by availability zones | N/A |
| └>&nbsp;&nbsp; **availabilityZone** | `string` | Availability zone of the subnet pair, for example us-west-2a | N/A |
| └>&nbsp;&nbsp; **privateSubnet** | `string` | ID of the private subnet, for example subnet-07a20d6c41af2b725 | N/A |
| └>&nbsp;&nbsp; **publicSubnet** | `string` | ID of the public subnet, for example subnet-0f7e49a3ce68ff338 | N/A |
