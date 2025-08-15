# Agent API

## Spec Fields

AgentSpec defines the desired state of Agent

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **approved** | `boolean` | No description provided. | N/A |
|  **clusterDeploymentName** | `object` | ClusterReference represents a Cluster Reference. It has enough information to retrieve cluster in any namespace | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is unique within a namespace to reference a cluster resource. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace defines the space within which the cluster name must be unique. | N/A |
|  **hostname** | `string` | No description provided. | N/A |
|  **ignitionConfigOverrides** | `string` | Json formatted string containing the user overrides for the host's ignition config | N/A |
|  **ignitionEndpointHTTPHeaders** | `object` | IgnitionEndpointHTTPHeaders are the additional HTTP headers used when fetching the ignition. | N/A |
|  **ignitionEndpointTokenReference** | `object` | IgnitionEndpointTokenReference references a secret containing an Authorization Bearer token to fetch the ignition from ignition_endpoint_url. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the secret containing the ignition endpoint token. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace is the namespace of the secret containing the ignition endpoint token. | N/A |
|  **installation_disk_id** | `string` | InstallationDiskID defines the installation destination disk (must be equal to the inventory disk id). | N/A |
|  **installerArgs** | `string` | Json formatted string containing the user overrides for the host's coreos installer args | N/A |
|  **machineConfigPool** | `string` | No description provided. | N/A |
|  **nodeLabels** | `object` | NodeLabels are the labels to be applied on the node associated with this agent | N/A |
|  **role** | `string` | HostRole host role swagger:model host-role | N/A |
## Status Fields

AgentStatus defines the observed state of Agent

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **bootstrap** | `boolean` | No description provided. | N/A |
|  **conditions** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **lastHeartbeatTime** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | ConditionType is the state of the operator's reconciliation functionality. | N/A |
|  **csrStatus** | `object` | CSRStatus tracks the status of CSR approvals for the agent | N/A |
| └>&nbsp;&nbsp; **approvedCSRs** | `array` | CSRs that have been approved for the agent by the assisted-service | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **approvedAt** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | CSRType represents the type of CSR | N/A |
| └>&nbsp;&nbsp; **lastApprovalAttempt** | `string` | Last time we attempted a CSR approval | N/A |
|  **debugInfo** | `object` | DebugInfo includes information for debugging the installation process. | N/A |
| └>&nbsp;&nbsp; **eventsURL** | `string` | EventsURL specifies an HTTP/S URL that contains events which occured during the cluster installation process | N/A |
| └>&nbsp;&nbsp; **logsURL** | `string` | LogsURL specifies a url for download controller logs tar file. | N/A |
| └>&nbsp;&nbsp; **state** | `string` | Current state of the Agent | N/A |
| └>&nbsp;&nbsp; **stateInfo** | `string` | Additional information pertaining to the status of the Agent | N/A |
|  **deprovision_info** | `object` | DeprovisionInfo stores data related to the agent's previous cluster binding in order to clean up when the agent re-registers | N/A |
| └>&nbsp;&nbsp; **cluster_name** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **cluster_namespace** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **node_name** | `string` | No description provided. | N/A |
|  **installation_disk_id** | `string` | InstallationDiskID is the disk that will be used for the installation. | N/A |
|  **inventory** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **bmcAddress** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **bmcV6Address** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **boot** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **currentBootMode** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **deviceType** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **pxeInterface** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **cpu** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **architecture** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **clockMegahertz** | `integer` | Name in REST API: frequency | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **count** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **flags** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **modelName** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **disks** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **bootable** | `boolean` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **byID** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **byPath** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **driveType** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **hctl** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **installationEligibility** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **eligible** | `boolean` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **notEligibleReasons** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ioPerf** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **syncDurationMilliseconds** | `integer` | 99th percentile of fsync duration in milliseconds | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **model** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **path** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serial** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sizeBytes** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **smart** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vendor** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **wwn** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **hostname** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **interfaces** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **biosDevName** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **clientID** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **flags** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **hasCarrier** | `boolean` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipV4Addresses** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ipV6Addresses** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **macAddress** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **mtu** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **product** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **speedMbps** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vendor** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **memory** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **physicalBytes** | `integer` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **usableBytes** | `integer` | No description provided. | N/A |
| └>&nbsp;&nbsp; **reportTime** | `string` | Name in REST API: timestamp | N/A |
| └>&nbsp;&nbsp; **systemVendor** | `object` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **manufacturer** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **productName** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serialNumber** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **virtual** | `boolean` | No description provided. | N/A |
|  **kind** | `string` | Kind corresponds to the same field in the model Host. It indicates the type of cluster the host is being installed to; either an existing cluster (day-2) or a new cluster (day-1). Value is one of: "AddToExistingClusterHost" (day-2) or "Host" (day-1) | N/A |
|  **ntpSources** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **sourceName** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **sourceState** | `string` | SourceState source state swagger:model source_state | N/A |
|  **progress** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **currentStage** | `string` | current installation stage | N/A |
| └>&nbsp;&nbsp; **installationPercentage** | `integer` | Estimate progress (percentage) | N/A |
| └>&nbsp;&nbsp; **progressInfo** | `string` | Additional information for the current installation stage | N/A |
| └>&nbsp;&nbsp; **progressStages** | `array` | All stages (ordered by their appearance) for this agent | N/A |
| └>&nbsp;&nbsp; **stageStartTime** | `string` | host field: progress: stage_started_at | N/A |
| └>&nbsp;&nbsp; **stageUpdateTime** | `string` | host field: progress: stage_updated_at | N/A |
|  **role** | `string` | HostRole host role swagger:model host-role | N/A |
|  **validationsInfo** | `object` | ValidationsInfo is a JSON-formatted string containing the validation results for each validation id grouped by category (network, hosts-data, etc.) | N/A |
