# PolicySet API

PolicySetStatus reports the observed status of the policy set resulting from its policies.

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **description** | `string` | Description is the description of this policy set. | N/A |
|  **policies** | `array` | Policies is a list of policy names that are contained within the policy set. | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **compliant** | `string` | Compliant reports the observed status resulting from the compliance of the policies within. | N/A |
|  **placement** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **placement** | `string` | Placement is the name of the Placement resource, from the cluster.open-cluster-management.io API group, that is bound to the policy. | N/A |
| └>&nbsp;&nbsp; **placementBinding** | `string` | PlacementBinding is the name of the PlacementBinding resource, from the policies.open-cluster-management.io API group, that binds the placement resource to the policy set. | N/A |
| └>&nbsp;&nbsp; **placementRule** | `string` | PlacementRule (deprecated) is the name of the PlacementRule resource, from the apps.open-cluster-management.io API group, that is bound to the policy. | N/A |
|  **statusMessage** | `string` | StatusMessge reports the current state while determining the compliance of the policy set. | N/A |
