# AWSFargateProfile API

## Spec Fields

FargateProfileSpec defines the desired state of FargateProfile.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **additionalTags** | `object` | AdditionalTags is an optional set of tags to add to AWS resources managed by the AWS provider, in addition to the ones added by default. | N/A |
|  **clusterName** | `string` | ClusterName is the name of the Cluster this object belongs to. | N/A |
|  **profileName** | `string` | ProfileName specifies the profile name. | N/A |
|  **roleName** | `string` | RoleName specifies the name of IAM role for this fargate pool If the role is pre-existing we will treat it as unmanaged and not delete it on deletion. If the EKSEnableIAM feature flag is true and no name is supplied then a role is created. | N/A |
|  **selectors** | `array` | Selectors specify fargate pod selectors. | N/A |
| └>&nbsp;&nbsp; **labels** | `object` | Labels specifies which pod labels this selector should match. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace specifies which namespace this selector should match. | N/A |
|  **subnetIDs** | `array` | SubnetIDs specifies which subnets are used for the auto scaling group of this nodegroup. | N/A |
## Status Fields

FargateProfileStatus defines the observed state of FargateProfile.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions defines current state of the Fargate profile. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | Last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | A human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | The reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **failureMessage** | `string` | FailureMessage will be set in the event that there is a terminal problem reconciling the FargateProfile and will contain a more verbose string suitable for logging and human consumption. This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the FargateProfile's spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured. Any transient errors that occur during the reconciliation of FargateProfiles can be added as events to the FargateProfile object and/or logged in the controller's output. | N/A |
|  **failureReason** | `string` | FailureReason will be set in the event that there is a terminal problem reconciling the FargateProfile and will contain a succinct value suitable for machine interpretation. This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the FargateProfile's spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured. Any transient errors that occur during the reconciliation of FargateProfiles can be added as events to the FargateProfile object and/or logged in the controller's output. | N/A |
|  **ready** | `boolean` | Ready denotes that the FargateProfile is available. | N/A |
