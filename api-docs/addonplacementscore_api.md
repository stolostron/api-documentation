# AddOnPlacementScore API

AddOnPlacementScore represents a bundle of scores of one managed cluster, which could be used by placement.
AddOnPlacementScore is a namespace scoped resource. The namespace of the resource is the cluster namespace.

## Spec Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
## Status Fields

Status represents the status of the AddOnPlacementScore.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions contain the different condition statuses for this AddOnPlacementScore. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **scores** | `array` | Scores contain a list of score name and value of this managed cluster. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the score | N/A |
| └>&nbsp;&nbsp; **value** | `integer` | Value is the value of the score. The score range is from -100 to 100. | `Minimum=-100`<br>`Maximum=100` |
|  **validUntil** | `string` | ValidUntil defines the valid time of the scores. After this time, the scores are considered to be invalid by placement. nil means never expire. The controller owning this resource should keep the scores up-to-date. | N/A |
