# AgentClassification API

## Spec Fields

AgentClassificationSpec defines the desired state of AgentClassification

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **labelKey** | `string` | LabelKey specifies the label key to apply to matched Agents | N/A |
|  **labelValue** | `string` | LabelValue specifies the label value to apply to matched Agents | N/A |
|  **query** | `string` | Query is in gojq format (https://github.com/itchyny/gojq#difference-to-jq) and will be invoked on each Agent's inventory. The query should return a boolean. The operator will apply the label to any Agent for which "true" is returned. | N/A |
## Status Fields

AgentClassificationStatus defines the observed state of AgentClassification

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **lastHeartbeatTime** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | ConditionType is the state of the operator's reconciliation functionality. | N/A |
|  **errorCount** | `integer` | ErrorCount shows how many Agents encountered errors when matching the classification | N/A |
|  **matchedCount** | `integer` | MatchedCount shows how many Agents currently match the classification | N/A |
