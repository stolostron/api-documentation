# ManagedServiceAccount API

ManagedServiceAccount is the Schema for the managedserviceaccounts API

## Spec Fields

ManagedServiceAccountSpec defines the desired state of ManagedServiceAccount

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **rotation** | `object` | Rotation is the policy for rotation the credentials. | N/A |
| └>&nbsp;&nbsp; **enabled** | `boolean` | Enabled prescribes whether the ServiceAccount token will be rotated from the upstream | N/A |
| └>&nbsp;&nbsp; **validity** | `string` | Validity is the duration for which the signed ServiceAccount token is valid. | N/A |
|  **ttlSecondsAfterCreation** | `integer` | ttlSecondsAfterCreation limits the lifetime of a ManagedServiceAccount. If the ttlSecondsAfterCreation field is set, the ManagedServiceAccount will be automatically deleted regardless of the ManagedServiceAccount's status. When the ManagedServiceAccount is deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is unset, the ManagedServiceAccount won't be automatically deleted. If this field is set to zero, the ManagedServiceAccount becomes eligible for deletion immediately after its creation. In order to use ttlSecondsAfterCreation, the EphemeralIdentity feature gate must be enabled. | `Minimum=0` |
## Status Fields

ManagedServiceAccountStatus defines the observed state of ManagedServiceAccount

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions is the condition list. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt) | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **expirationTimestamp** | `string` | ExpirationTimestamp is the time when the token will expire. | N/A |
|  **tokenSecretRef** | `object` | TokenSecretRef is a reference to the corresponding ServiceAccount's Secret, which stores the CA certficate and token from the managed cluster. | N/A |
| └>&nbsp;&nbsp; **lastRefreshTimestamp** | `string` | LastRefreshTimestamp is the timestamp indicating when the token in the Secret is refreshed. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the referenced secret. | N/A |
