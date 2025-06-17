# Metal3RemediationTemplate API

Metal3RemediationTemplateStatus defines the observed state of Metal3RemediationTemplate.

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **template** | `object` | Metal3RemediationTemplateResource describes the data needed to create a Metal3Remediation from a template. | N/A |
| └>&nbsp;&nbsp; **spec** | `object` | Spec is the specification of the desired behavior of the Metal3Remediation. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **strategy** | `object` | Strategy field defines remediation strategy. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **retryLimit** | `integer` | Sets maximum number of remediation retries. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **timeout** | `string` | Sets the timeout between remediation retries. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type of remediation. | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **status** | `object` | Metal3RemediationStatus defines the observed state of Metal3Remediation | N/A |
| └>&nbsp;&nbsp; **lastRemediated** | `string` | LastRemediated identifies when the host was last remediated | N/A |
| └>&nbsp;&nbsp; **phase** | `string` | Phase represents the current phase of machine remediation. E.g. Pending, Running, Done etc. | N/A |
| └>&nbsp;&nbsp; **retryCount** | `integer` | RetryCount can be used as a counter during the remediation. Field can hold number of reboots etc. | N/A |
