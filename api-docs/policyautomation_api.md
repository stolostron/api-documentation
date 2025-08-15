# PolicyAutomation API

## Spec Fields

PolicyAutomationSpec defines how and when automation is initiated for the referenced policy.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **automationDef** | `object` | AutomationDef defines the automation to invoke. | N/A |
| └>&nbsp;&nbsp; **extra_vars** | `object` | ExtraVars is passed to the Ansible job at execution time and is a known Ansible entity. | N/A |
| └>&nbsp;&nbsp; **jobTtl** | `integer` | JobTTL sets the time to live for the Kubernetes Job object after the Ansible job playbook run has finished. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the Ansible Template to run in Ansible Automation Platform as a job. | N/A |
| └>&nbsp;&nbsp; **policyViolationsLimit** | `integer` | The maximum number of violating cluster contexts that are provided to the Ansible job as extra variables. When policyViolationsLimit is set to "0", it means no limit. The default value is "1000". | `Minimum=0` |
| └>&nbsp;&nbsp; **secret** | `string` | TowerSecret is the name of the secret that contains the Ansible Automation Platform credential. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type of the automation to invoke | N/A |
|  **delayAfterRunSeconds** | `integer` | DelayAfterRunSeconds sets the minimum number of seconds before an automation can run again due to a new violation on the same managed cluster. This only applies to the EveryEvent mode. The default value is "0". | `Minimum=0` |
|  **eventHook** | `string` | EventHook specifies the compliance state that initiates automation. This must be set to "noncompliant". | N/A |
|  **mode** | `string` | Mode specifies how often automation is initiated. The supported values are "once", "everyEvent", and "disabled". | N/A |
|  **policyRef** | `string` | PolicyRef is the name of the policy that this automation resource is bound to. | N/A |
|  **rescanAfter** | `string` | RescanAfter is reserved for future use and should not be set. | N/A |
## Status Fields

PolicyAutomationStatus defines the observed state of the PolicyAutomation resource.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **clustersWithEvent** | `object` | Cluster name as the key of ClustersWithEvent | N/A |
