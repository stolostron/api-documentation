# ManifestWork API

ManifestWork represents a manifests workload that hub wants to deploy on the managed cluster.
A manifest workload is defined as a set of Kubernetes resources.
ManifestWork must be created in the cluster namespace on the hub, so that agent on the
corresponding managed cluster can access this resource and deploy on the managed
cluster.

## Spec Fields

Spec represents a desired configuration of work to be deployed on the managed cluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **deleteOption** | `object` | DeleteOption represents deletion strategy when the manifestwork is deleted. Foreground deletion strategy is applied to all the resource in this manifestwork if it is not set. | N/A |
| └>&nbsp;&nbsp; **propagationPolicy** | `string` | propagationPolicy can be Foreground, Orphan or SelectivelyOrphan SelectivelyOrphan should be rarely used.  It is provided for cases where particular resources is transfering ownership from one ManifestWork to another or another management unit. Setting this value will allow a flow like 1. create manifestwork/2 to manage foo 2. update manifestwork/1 to selectively orphan foo 3. remove foo from manifestwork/1 without impacting continuity because manifestwork/2 adopts it. | N/A |
| └>&nbsp;&nbsp; **selectivelyOrphans** | `object` | selectivelyOrphan represents a list of resources following orphan deletion stratecy | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **orphaningRules** | `array` | orphaningRules defines a slice of orphaningrule. Each orphaningrule identifies a single resource included in this manifestwork | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the API Group of the Kubernetes resource, empty string indicates it is in core group. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Name is the namespace of the Kubernetes resource, empty string indicates it is a cluster scoped resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resource** | `string` | Resource is the resource name of the Kubernetes resource. | N/A |
| └>&nbsp;&nbsp; **ttlSecondsAfterFinished** | `integer` | TTLSecondsAfterFinished limits the lifetime of a ManifestWork that has been marked Complete by one or more conditionRules set for its manifests. If this field is set, and the manifestwork has completed, then it is elligible to be automatically deleted. If this field is unset, the manifestwork won't be automatically deleted even afer completion. If this field is set to zero, the manfiestwork becomes elligible to be deleted immediately after completion. | N/A |
|  **executor** | `object` | Executor is the configuration that makes the work agent to perform some pre-request processing/checking. e.g. the executor identity tells the work agent to check the executor has sufficient permission to write the workloads to the local managed cluster. Note that nil executor is still supported for backward-compatibility which indicates that the work agent will not perform any additional actions before applying resources. | N/A |
| └>&nbsp;&nbsp; **subject** | `object` | Subject is the subject identity which the work agent uses to talk to the local cluster when applying the resources. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serviceAccount** | `object` | ServiceAccount is for identifying which service account to use by the work agent. Only required if the type is "ServiceAccount". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the service account. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*)$` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace is the namespace of the service account. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*)$` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type is the type of the subject identity. Supported types are: "ServiceAccount". | N/A |
|  **manifestConfigs** | `array` | ManifestConfigs represents the configurations of manifests defined in workload field. | N/A |
| └>&nbsp;&nbsp; **conditionRules** | `array` | ConditionRules defines how to set manifestwork conditions for a specific manifest. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **celExpressions** | `array` | CelExpressions defines the CEL expressions to be evaluated for the condition. Final result is the logical AND of all expressions. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **condition** | `string` | Condition is the type of condition that is set based on this rule. Any condition is supported, but certain special conditions can be used to to control higher level behaviors of the manifestwork. If the condition is Complete, the manifest will no longer be updated once completed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **message** | `string` | Message is set on the condition created for this rule | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **messageExpression** | `string` | MessageExpression uses a CEL expression to generate a message for the condition Will override message if both are set and messageExpression returns a non-empty string. Variables: - object: The current instance of the manifest - result: Boolean result of the CEL expressions | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type defines how a manifest should be evaluated for a condition. It can be CEL, or WellKnownConditions. If the type is CEL, user should specify the celExpressions field If the type is WellKnownConditions, certain common types in k8s.io/api will be considered completed as defined by hardcoded rules. | N/A |
| └>&nbsp;&nbsp; **feedbackRules** | `array` | FeedbackRules defines what resource status field should be returned. If it is not set or empty, no feedback rules will be honored. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **jsonPaths** | `array` | JsonPaths defines the json path under status field to be synced. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name represents the alias name for this field | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **path** | `string` | Path represents the json path of the field under status. The path must point to a field with single value in the type of integer, bool or string. If the path points to a non-existing field, no value will be returned. If the path points to a structure, map or slice, no value will be returned and the status conddition of StatusFeedBackSynced will be set as false. Ref to https://kubernetes.io/docs/reference/kubectl/jsonpath/ on how to write a jsonPath. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | Version is the version of the Kubernetes resource. If it is not specified, the resource with the semantically latest version is used to resolve the path. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type defines the option of how status can be returned. It can be jsonPaths or wellKnownStatus. If the type is JSONPaths, user should specify the jsonPaths field If the type is WellKnownStatus, certain common fields of status defined by a rule only for types in in k8s.io/api and open-cluster-management/api will be reported, If these status fields do not exist, no values will be reported. | N/A |
| └>&nbsp;&nbsp; **resourceIdentifier** | `object` | ResourceIdentifier represents the group, resource, name and namespace of a resoure. iff this refers to a resource not created by this manifest work, the related rules will not be executed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the API Group of the Kubernetes resource, empty string indicates it is in core group. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Name is the namespace of the Kubernetes resource, empty string indicates it is a cluster scoped resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resource** | `string` | Resource is the resource name of the Kubernetes resource. | N/A |
| └>&nbsp;&nbsp; **updateStrategy** | `object` | UpdateStrategy defines the strategy to update this manifest. UpdateStrategy is Update if it is not set. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serverSideApply** | `object` | serverSideApply defines the configuration for server side apply. It is honored only when the type of the updateStrategy is ServerSideApply | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fieldManager** | `string` | FieldManager is the manager to apply the resource. It is work-agent by default, but can be other name with work-agent as the prefix. | `Pattern=^work-agent` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **force** | `boolean` | Force represents to force apply the manifest. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ignoreFields** | `array` | IgnoreFields defines a list of json paths in the resource that will not be updated on the spoke. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **condition** | `string` | Condition defines the condition that the fields should be ignored when apply the resource. Fields in JSONPaths are all ignored when condition is met, otherwise no fields is ignored in the apply operation. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **jsonPaths** | `array` | JSONPaths defines the list of json path in the resource to be ignored | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | type defines the strategy to update this manifest, default value is Update. Update type means to update resource by an update call. CreateOnly type means do not update resource based on current manifest. ServerSideApply type means to update resource using server side apply with work-controller as the field manager. If there is conflict, the related Applied condition of manifest will be in the status of False with the reason of ApplyConflict. ReadOnly type means the agent will only check the existence of the resource based on its metadata, statusFeedBackRules can still be used to get feedbackResults. | N/A |
|  **workload** | `object` | Workload represents the manifest workload to be deployed on a managed cluster. | N/A |
| └>&nbsp;&nbsp; **manifests** | `array` | Manifests represents a list of kuberenetes resources to be deployed on a managed cluster. | N/A |
## Status Fields

Status represents the current status of work.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions contains the different condition statuses for this work. Valid condition types are: 1. Applied represents workload in ManifestWork is applied successfully on managed cluster. 2. Progressing represents workload in ManifestWork is being applied on managed cluster. 3. Available represents workload in ManifestWork exists on the managed cluster. 4. Degraded represents the current state of workload does not match the desired state for a certain period. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **resourceStatus** | `object` | ResourceStatus represents the status of each resource in manifestwork deployed on a managed cluster. The Klusterlet agent on managed cluster syncs the condition from the managed cluster to the hub. | N/A |
| └>&nbsp;&nbsp; **manifests** | `array` | Manifests represents the condition of manifests deployed on managed cluster. Valid condition types are: 1. Progressing represents the resource is being applied on managed cluster. 2. Applied represents the resource is applied successfully on managed cluster. 3. Available represents the resource exists on the managed cluster. 4. Degraded represents the current state of resource does not match the desired state for a certain period. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **conditions** | `array` | Conditions represents the conditions of this resource on a managed cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceMeta** | `object` | ResourceMeta represents the group, version, kind, name and namespace of a resoure. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the API Group of the Kubernetes resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the kind of the Kubernetes resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Name is the namespace of the Kubernetes resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ordinal** | `integer` | Ordinal represents the index of the manifest on spec. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resource** | `string` | Resource is the resource name of the Kubernetes resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | Version is the version of the Kubernetes resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **statusFeedback** | `object` | StatusFeedback represents the values of the feild synced back defined in statusFeedbacks | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | Values represents the synced value of the interested field. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fieldValue** | `object` | Value is the value of the status field. The value of the status field can only be integer, string or boolean. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **boolean** | `boolean` | Boolean is bool value when type is boolean. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **integer** | `integer` | Integer is the integer value when type is integer. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **jsonRaw** | `string` | JsonRaw is a json string when type is a list or object | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **string** | `string` | String is the string value when type is string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type represents the type of the value, it can be integer, string or boolean. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name represents the alias name for this field. It is the same as what is specified in StatuFeedbackRule in the spec. | N/A |
