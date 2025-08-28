# ClusterCurator API

ClusterCurator is the custom resource for the clustercurators API. This kind allows you to run Ansible prehook and posthook jobs before provisioning Hive or HyperShift and importing a cluster. Additionally, cluster upgrade and destroy operations are supported as well.

## Spec Fields

ClusterCuratorSpec defines the desired state of ClusterCurator

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **curatorJob** | `string` | Kubernetes job resource created for curation of a cluster | N/A |
|  **desiredCuration** | `string` | This is the desired curation that will occur | N/A |
|  **destroy** | `object` | During an destroy curation run these **Pre hook ONLY** | N/A |
| └>&nbsp;&nbsp; **jobMonitorTimeout** | `integer` | JobMonitorTimeout defines the timeout for finding a job, the unit of this is minute. If job is found, the curator controller waits until the job becomes active. By default, it is 5 minutes If its value is less than or equal to zero, the default value will be used. | N/A |
| └>&nbsp;&nbsp; **overrideJob** | `object` | When provided, this is a Job specification and overrides the default flow | N/A |
| └>&nbsp;&nbsp; **posthook** | `array` | Jobs to run after the cluster import | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **extra_vars** | `object` | Ansible job extra_vars is passed to the Ansible job at execution time and is a known Ansible entity. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **job_tags** | `string` | A comma-separated list of tags to specify which sets of ansible tasks in a job should be run. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the Ansible Template to run in Tower as a job | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **skip_tags** | `string` | A comma-separated list of tags to specify which sets of ansible tasks in a job should not be run. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type of the Hook. For Job type, Ansible job template will be used. For Workflow type, Ansible workflow template will be used. If omitted, default to Job type. | N/A |
| └>&nbsp;&nbsp; **prehook** | `array` | Jobs to run before the cluster deployment | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **extra_vars** | `object` | Ansible job extra_vars is passed to the Ansible job at execution time and is a known Ansible entity. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **job_tags** | `string` | A comma-separated list of tags to specify which sets of ansible tasks in a job should be run. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the Ansible Template to run in Tower as a job | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **skip_tags** | `string` | A comma-separated list of tags to specify which sets of ansible tasks in a job should not be run. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type of the Hook. For Job type, Ansible job template will be used. For Workflow type, Ansible workflow template will be used. If omitted, default to Job type. | N/A |
| └>&nbsp;&nbsp; **towerAuthSecret** | `string` | TowerAuthSecret is ansible secret used in template to run in tower | N/A |
|  **install** | `object` | During an install curation run these Pre/Post hooks | N/A |
| └>&nbsp;&nbsp; **jobMonitorTimeout** | `integer` | JobMonitorTimeout defines the timeout for finding a job, the unit of this is minute. If job is found, the curator controller waits until the job becomes active. By default, it is 5 minutes If its value is less than or equal to zero, the default value will be used. | N/A |
| └>&nbsp;&nbsp; **overrideJob** | `object` | When provided, this is a Job specification and overrides the default flow | N/A |
| └>&nbsp;&nbsp; **posthook** | `array` | Jobs to run after the cluster import | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **extra_vars** | `object` | Ansible job extra_vars is passed to the Ansible job at execution time and is a known Ansible entity. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **job_tags** | `string` | A comma-separated list of tags to specify which sets of ansible tasks in a job should be run. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the Ansible Template to run in Tower as a job | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **skip_tags** | `string` | A comma-separated list of tags to specify which sets of ansible tasks in a job should not be run. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type of the Hook. For Job type, Ansible job template will be used. For Workflow type, Ansible workflow template will be used. If omitted, default to Job type. | N/A |
| └>&nbsp;&nbsp; **prehook** | `array` | Jobs to run before the cluster deployment | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **extra_vars** | `object` | Ansible job extra_vars is passed to the Ansible job at execution time and is a known Ansible entity. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **job_tags** | `string` | A comma-separated list of tags to specify which sets of ansible tasks in a job should be run. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the Ansible Template to run in Tower as a job | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **skip_tags** | `string` | A comma-separated list of tags to specify which sets of ansible tasks in a job should not be run. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type of the Hook. For Job type, Ansible job template will be used. For Workflow type, Ansible workflow template will be used. If omitted, default to Job type. | N/A |
| └>&nbsp;&nbsp; **towerAuthSecret** | `string` | TowerAuthSecret is ansible secret used in template to run in tower | N/A |
|  **inventory** | `string` | Inventory values are supplied for use with the pre/post jobs. | N/A |
|  **providerCredentialPath** | `string` | Points to the Cloud Provider or Ansible Provider secret, format: namespace/secretName | N/A |
|  **scale** | `object` | During an scale curation run these Pre/Post hooks | N/A |
| └>&nbsp;&nbsp; **jobMonitorTimeout** | `integer` | JobMonitorTimeout defines the timeout for finding a job, the unit of this is minute. If job is found, the curator controller waits until the job becomes active. By default, it is 5 minutes If its value is less than or equal to zero, the default value will be used. | N/A |
| └>&nbsp;&nbsp; **overrideJob** | `object` | When provided, this is a Job specification and overrides the default flow | N/A |
| └>&nbsp;&nbsp; **posthook** | `array` | Jobs to run after the cluster import | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **extra_vars** | `object` | Ansible job extra_vars is passed to the Ansible job at execution time and is a known Ansible entity. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **job_tags** | `string` | A comma-separated list of tags to specify which sets of ansible tasks in a job should be run. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the Ansible Template to run in Tower as a job | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **skip_tags** | `string` | A comma-separated list of tags to specify which sets of ansible tasks in a job should not be run. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type of the Hook. For Job type, Ansible job template will be used. For Workflow type, Ansible workflow template will be used. If omitted, default to Job type. | N/A |
| └>&nbsp;&nbsp; **prehook** | `array` | Jobs to run before the cluster deployment | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **extra_vars** | `object` | Ansible job extra_vars is passed to the Ansible job at execution time and is a known Ansible entity. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **job_tags** | `string` | A comma-separated list of tags to specify which sets of ansible tasks in a job should be run. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the Ansible Template to run in Tower as a job | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **skip_tags** | `string` | A comma-separated list of tags to specify which sets of ansible tasks in a job should not be run. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type of the Hook. For Job type, Ansible job template will be used. For Workflow type, Ansible workflow template will be used. If omitted, default to Job type. | N/A |
| └>&nbsp;&nbsp; **towerAuthSecret** | `string` | TowerAuthSecret is ansible secret used in template to run in tower | N/A |
|  **upgrade** | `object` | During an upgrade curation run these | N/A |
| └>&nbsp;&nbsp; **channel** | `string` | Channel is an identifier for explicitly requesting that a non-default set of updates be applied to this cluster. The default channel will be contain stable updates that are appropriate for production clusters. | N/A |
| └>&nbsp;&nbsp; **desiredUpdate** | `string` | DesiredUpdate indicates the desired value of the cluster version. Setting this value will trigger an upgrade (if the current version does not match the desired version). During an EUS to EUS upgrade, this value becomes the final cluster version (the target version that ClusterCurator will upgrade the cluster to). | N/A |
| └>&nbsp;&nbsp; **intermediateUpdate** | `string` | IntermediateUpdate indicates the desired value of the intermediate cluster version when performing EUS to EUS upgrades. Setting both this value and DesiredUpdate will trigger an EUS to EUS upgrade. | N/A |
| └>&nbsp;&nbsp; **monitorTimeout** | `integer` | MonitorTimeout defines the monitor process timeout, the unit of this is minute. By default, it is 120 minutes If its value is less than or equal to zero, the default value will be used. | N/A |
| └>&nbsp;&nbsp; **overrideJob** | `object` | When provided, this is a Job specification and overrides the default flow | N/A |
| └>&nbsp;&nbsp; **posthook** | `array` | Jobs to run after the cluster upgrade | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **extra_vars** | `object` | Ansible job extra_vars is passed to the Ansible job at execution time and is a known Ansible entity. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **job_tags** | `string` | A comma-separated list of tags to specify which sets of ansible tasks in a job should be run. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the Ansible Template to run in Tower as a job | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **skip_tags** | `string` | A comma-separated list of tags to specify which sets of ansible tasks in a job should not be run. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type of the Hook. For Job type, Ansible job template will be used. For Workflow type, Ansible workflow template will be used. If omitted, default to Job type. | N/A |
| └>&nbsp;&nbsp; **prehook** | `array` | Jobs to run before the cluster upgrade | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **extra_vars** | `object` | Ansible job extra_vars is passed to the Ansible job at execution time and is a known Ansible entity. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **job_tags** | `string` | A comma-separated list of tags to specify which sets of ansible tasks in a job should be run. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the Ansible Template to run in Tower as a job | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **skip_tags** | `string` | A comma-separated list of tags to specify which sets of ansible tasks in a job should not be run. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type of the Hook. For Job type, Ansible job template will be used. For Workflow type, Ansible workflow template will be used. If omitted, default to Job type. | N/A |
| └>&nbsp;&nbsp; **towerAuthSecret** | `string` | TowerAuthSecret is ansible secret used in template to run in tower | N/A |
| └>&nbsp;&nbsp; **upstream** | `string` | Upstream may be used to specify the preferred update server. By default it will use the appropriate update server for the cluster and region. | N/A |
## Status Fields

ClusterCuratorStatus defines the observed state of ClusterCurator work

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Track the conditions for each step in the desired curation that is being executed as a job | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt) | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
