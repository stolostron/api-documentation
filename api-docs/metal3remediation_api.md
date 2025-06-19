# Metal3Remediation API

Metal3RemediationStatus defines the observed state of Metal3Remediation.

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **strategy** | `object` | Strategy field defines remediation strategy. | N/A |
| └>&nbsp;&nbsp; **retryLimit** | `integer` | Sets maximum number of remediation retries. | N/A |
| └>&nbsp;&nbsp; **timeout** | `string` | Sets the timeout between remediation retries. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type of remediation. | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **lastRemediated** | `string` | LastRemediated identifies when the host was last remediated | N/A |
|  **phase** | `string` | Phase represents the current phase of machine remediation. E.g. Pending, Running, Done etc. | N/A |
|  **retryCount** | `integer` | RetryCount can be used as a counter during the remediation. Field can hold number of reboots etc. | N/A |
