# ROSAMachinePool API

ROSAMachinePool is the Schema for the rosamachinepools API.

## Spec Fields

RosaMachinePoolSpec defines the desired state of RosaMachinePool.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **additionalSecurityGroups** | `array` | AdditionalSecurityGroups is an optional set of security groups to associate with all node instances of the machine pool. | N/A |
|  **additionalTags** | `object` | AdditionalTags are user-defined tags to be added on the underlying EC2 instances associated with this machine pool. | N/A |
|  **autoRepair** | `boolean` | AutoRepair specifies whether health checks should be enabled for machines in the NodePool. The default is true. | N/A |
|  **autoscaling** | `object` | Autoscaling specifies auto scaling behaviour for this MachinePool. required if Replicas is not configured | N/A |
| └>&nbsp;&nbsp; **maxReplicas** | `integer` | No description provided. | `Minimum=1` |
| └>&nbsp;&nbsp; **minReplicas** | `integer` | No description provided. | `Minimum=1` |
|  **availabilityZone** | `string` | AvailabilityZone is an optinal field specifying the availability zone where instances of this machine pool should run For Multi-AZ clusters, you can create a machine pool in a Single-AZ of your choice. | N/A |
|  **instanceType** | `string` | InstanceType specifies the AWS instance type | N/A |
|  **labels** | `object` | Labels specifies labels for the Kubernetes node objects | N/A |
|  **nodeDrainGracePeriod** | `string` | NodeDrainGracePeriod is grace period for how long Pod Disruption Budget-protected workloads will be respected during upgrades. After this grace period, any workloads protected by Pod Disruption Budgets that have not been successfully drained from a node will be forcibly evicted. Valid values are from 0 to 1 week(10080m|168h) . 0 or empty value means that the MachinePool can be drained without any time limitation. | N/A |
|  **nodePoolName** | `string` | NodePoolName specifies the name of the nodepool in Rosa must be a valid DNS-1035 label, so it must consist of lower case alphanumeric and have a max length of 15 characters. | `Pattern=^[a-z]([-a-z0-9]*[a-z0-9])?$` |
|  **providerIDList** | `array` | ProviderIDList contain a ProviderID for each machine instance that's currently managed by this machine pool. | N/A |
|  **subnet** | `string` | No description provided. | N/A |
|  **taints** | `array` | Taints specifies the taints to apply to the nodes of the machine pool | N/A |
| └>&nbsp;&nbsp; **effect** | `string` | The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute. | N/A |
| └>&nbsp;&nbsp; **key** | `string` | The taint key to be applied to a node. | N/A |
| └>&nbsp;&nbsp; **value** | `string` | The taint value corresponding to the taint key. | `Pattern=^(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])?$` |
|  **tuningConfigs** | `array` | TuningConfigs specifies the names of the tuning configs to be applied to this MachinePool. Tuning configs must already exist. | N/A |
|  **updateConfig** | `object` | UpdateConfig specifies update configurations. | N/A |
| └>&nbsp;&nbsp; **rollingUpdate** | `object` | RollingUpdate specifies MaxUnavailable & MaxSurge number of nodes during update. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **maxSurge** | `N/A` | MaxSurge is the maximum number of nodes that can be provisioned above the desired number of nodes. Value can be an absolute number (ex: 5) or a percentage of desired nodes (ex: 10%). Absolute number is calculated from percentage by rounding up. MaxSurge can not be 0 if MaxUnavailable is 0, default is 1. Both MaxSurge & MaxUnavailable must use the same units (absolute value or percentage). Example: when MaxSurge is set to 30%, new nodes can be provisioned immediately when the rolling update starts, such that the total number of old and new nodes do not exceed 130% of desired nodes. Once old nodes have been deleted, new nodes can be provisioned, ensuring that total number of nodes running at any time during the update is at most 130% of desired nodes. | `Pattern=^((100\|[0-9]{1,2})%\|[0-9]+)$` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **maxUnavailable** | `N/A` | MaxUnavailable is the maximum number of nodes that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired nodes (ex: 10%). Absolute number is calculated from percentage by rounding down. MaxUnavailable can not be 0 if MaxSurge is 0, default is 0. Both MaxUnavailable & MaxSurge must use the same units (absolute value or percentage). Example: when MaxUnavailable is set to 30%, old nodes can be deleted down to 70% of desired nodes immediately when the rolling update starts. Once new nodes are ready, more old nodes be deleted, followed by provisioning new nodes, ensuring that the total number of nodes available at all times during the update is at least 70% of desired nodes. | `Pattern=^((100\|[0-9]{1,2})%\|[0-9]+)$` |
|  **version** | `string` | Version specifies the OpenShift version of the nodes associated with this machinepool. ROSAControlPlane version is used if not set. | N/A |
|  **volumeSize** | `integer` | VolumeSize set the disk volume size for the machine pool, in Gib. The default is 300 GiB. | `Minimum=75`<br>`Maximum=16384` |
## Status Fields

RosaMachinePoolStatus defines the observed state of RosaMachinePool.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **availableUpgrades** | `array` | Available upgrades for the ROSA MachinePool. | N/A |
|  **conditions** | `array` | Conditions defines current service state of the managed machine pool | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | reason is the reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **failureMessage** | `string` | FailureMessage will be set in the event that there is a terminal problem reconciling the state and will be set to a descriptive error message. This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the spec or the configuration of the controller, and that manual intervention is required. | N/A |
|  **id** | `string` | ID is the ID given by ROSA. | N/A |
|  **ready** | `boolean` | Ready denotes that the RosaMachinePool nodepool has joined the cluster | N/A |
|  **replicas** | `integer` | Replicas is the most recently observed number of replicas. | N/A |
