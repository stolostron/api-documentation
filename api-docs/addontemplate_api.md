# AddOnTemplate API

AddOnTemplate is the Custom Resource object, it is used to describe
how to deploy the addon agent and how to register the addon.
AddOnTemplate is a cluster-scoped resource, and will only be used
on the hub cluster.

## Spec Fields

spec holds the registration configuration for the addon and the
addon agent resources yaml description.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **addonName** | `string` | AddonName represents the name of the addon which the template belongs to | N/A |
|  **agentSpec** | `object` | AgentSpec describes what/how the kubernetes resources of the addon agent to be deployed on a managed cluster. | N/A |
| └>&nbsp;&nbsp; **deleteOption** | `object` | DeleteOption represents deletion strategy when the manifestwork is deleted. Foreground deletion strategy is applied to all the resource in this manifestwork if it is not set. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **propagationPolicy** | `string` | propagationPolicy can be Foreground, Orphan or SelectivelyOrphan SelectivelyOrphan should be rarely used.  It is provided for cases where particular resources is transfering ownership from one ManifestWork to another or another management unit. Setting this value will allow a flow like 1. create manifestwork/2 to manage foo 2. update manifestwork/1 to selectively orphan foo 3. remove foo from manifestwork/1 without impacting continuity because manifestwork/2 adopts it. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **selectivelyOrphans** | `object` | selectivelyOrphan represents a list of resources following orphan deletion stratecy | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **orphaningRules** | `array` | orphaningRules defines a slice of orphaningrule. Each orphaningrule identifies a single resource included in this manifestwork | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the API Group of the Kubernetes resource, empty string indicates it is in core group. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Name is the namespace of the Kubernetes resource, empty string indicates it is a cluster scoped resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resource** | `string` | Resource is the resource name of the Kubernetes resource. | N/A |
| └>&nbsp;&nbsp; **executor** | `object` | Executor is the configuration that makes the work agent to perform some pre-request processing/checking. e.g. the executor identity tells the work agent to check the executor has sufficient permission to write the workloads to the local managed cluster. Note that nil executor is still supported for backward-compatibility which indicates that the work agent will not perform any additional actions before applying resources. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **subject** | `object` | Subject is the subject identity which the work agent uses to talk to the local cluster when applying the resources. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serviceAccount** | `object` | ServiceAccount is for identifying which service account to use by the work agent. Only required if the type is "ServiceAccount". | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the service account. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*)$` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace is the namespace of the service account. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*)$` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type is the type of the subject identity. Supported types are: "ServiceAccount". | N/A |
| └>&nbsp;&nbsp; **manifestConfigs** | `array` | ManifestConfigs represents the configurations of manifests defined in workload field. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **feedbackRules** | `array` | FeedbackRules defines what resource status field should be returned. If it is not set or empty, no feedback rules will be honored. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **jsonPaths** | `array` | JsonPaths defines the json path under status field to be synced. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name represents the alias name for this field | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **path** | `string` | Path represents the json path of the field under status. The path must point to a field with single value in the type of integer, bool or string. If the path points to a non-existing field, no value will be returned. If the path points to a structure, map or slice, no value will be returned and the status conddition of StatusFeedBackSynced will be set as false. Ref to https://kubernetes.io/docs/reference/kubectl/jsonpath/ on how to write a jsonPath. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | Version is the version of the Kubernetes resource. If it is not specified, the resource with the semantically latest version is used to resolve the path. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type defines the option of how status can be returned. It can be jsonPaths or wellKnownStatus. If the type is JSONPaths, user should specify the jsonPaths field If the type is WellKnownStatus, certain common fields of status defined by a rule only for types in in k8s.io/api and open-cluster-management/api will be reported, If these status fields do not exist, no values will be reported. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceIdentifier** | `object` | ResourceIdentifier represents the group, resource, name and namespace of a resoure. iff this refers to a resource not created by this manifest work, the related rules will not be executed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **group** | `string` | Group is the API Group of the Kubernetes resource, empty string indicates it is in core group. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Name is the namespace of the Kubernetes resource, empty string indicates it is a cluster scoped resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resource** | `string` | Resource is the resource name of the Kubernetes resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **updateStrategy** | `object` | UpdateStrategy defines the strategy to update this manifest. UpdateStrategy is Update if it is not set. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serverSideApply** | `object` | serverSideApply defines the configuration for server side apply. It is honored only when the type of the updateStrategy is ServerSideApply | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fieldManager** | `string` | FieldManager is the manager to apply the resource. It is work-agent by default, but can be other name with work-agent as the prefix. | `Pattern=^work-agent` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **force** | `boolean` | Force represents to force apply the manifest. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **ignoreFields** | `array` | IgnoreFields defines a list of json paths in the resource that will not be updated on the spoke. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **condition** | `string` | Condition defines the condition that the fields should be ignored when apply the resource. Fields in JSONPaths are all ignored when condition is met, otherwise no fields is ignored in the apply operation. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **jsonPaths** | `array` | JSONPaths defines the list of json path in the resource to be ignored | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | type defines the strategy to update this manifest, default value is Update. Update type means to update resource by an update call. CreateOnly type means do not update resource based on current manifest. ServerSideApply type means to update resource using server side apply with work-controller as the field manager. If there is conflict, the related Applied condition of manifest will be in the status of False with the reason of ApplyConflict. ReadOnly type means the agent will only check the existence of the resource based on its metadata, statusFeedBackRules can still be used to get feedbackResults. | N/A |
| └>&nbsp;&nbsp; **workload** | `object` | Workload represents the manifest workload to be deployed on a managed cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **manifests** | `array` | Manifests represents a list of kuberenetes resources to be deployed on a managed cluster. | N/A |
|  **registration** | `array` | Registration holds the registration configuration for the addon | N/A |
| └>&nbsp;&nbsp; **customSigner** | `object` | CustomSigner holds the configuration of the CustomSigner type registration required when the Type is CustomSigner | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **signerName** | `string` | signerName is the name of signer that addon agent will use to create csr. | `Pattern=^([a-z0-9][a-z0-9-]*[a-z0-9]\.)+[a-z]+\/[a-z0-9-\.]+$` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **signingCA** | `object` | SigningCA represents the reference of the secret on the hub cluster to sign the CSR the secret type must be "kubernetes.io/tls" Note: The addon manager will not have permission to access the secret by default, so the user must grant the permission to the addon manager(by creating rolebinding/clusterrolebinding for the addon-manager serviceaccount "addon-manager-controller-sa"). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the signing CA secret | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace of the signing CA secret, the namespace of the addon-manager will be used if it is not set. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **subject** | `object` | Subject is the user subject of the addon agent to be registered to the hub. If it is not set, the addon agent will have the default subject "subject": {   "user": "system:open-cluster-management:cluster:{clusterName}:addon:{addonName}:agent:{agentName}",   "groups: ["system:open-cluster-management:cluster:{clusterName}:addon:{addonName}",             "system:open-cluster-management:addon:{addonName}", "system:authenticated"] } | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **groups** | `array` | groups is the user group of the addon agent. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **organizationUnit** | `array` | organizationUnit is the ou of the addon agent | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **user** | `string` | user is the user name of the addon agent. | N/A |
| └>&nbsp;&nbsp; **kubeClient** | `object` | KubeClient holds the configuration of the KubeClient type registration | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **hubPermissions** | `array` | HubPermissions represent the permission configurations of the addon agent to access the hub cluster | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **currentCluster** | `object` | CurrentCluster contains the configuration of CurrentCluster type binding. It is required when the type is CurrentCluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **clusterRoleName** | `string` | ClusterRoleName is the name of the clusterrole the addon agent is bound. A rolebinding will be created referring to this cluster role in each cluster namespace. The user must make sure the clusterrole exists on the hub cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **singleNamespace** | `object` | SingleNamespace contains the configuration of SingleNamespace type binding. It is required when the type is SingleNamespace | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace is the namespace the addon agent has permissions to bind to. A rolebinding will be created in this namespace referring to the RoleRef. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **roleRef** | `object` | RoleRef is an reference to the permission resource. it could be a role or a cluster role, the user must make sure it exist on the hub cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiGroup** | `string` | APIGroup is the group for the resource being referenced | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the type of resource being referenced | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of resource being referenced | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type of the permissions setting. It defines how to bind the roleRef on the hub cluster. It can be: - CurrentCluster: Bind the roleRef to the namespace with the same name as the managedCluster. - SingleNamespace: Bind the roleRef to the namespace specified by SingleNamespaceBindingConfig. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type of the registration configuration, it supports: - KubeClient: the addon agent can access the hub kube apiserver with kube style API.   the signer name should be "kubernetes.io/kube-apiserver-client". When this type is   used, the KubeClientRegistrationConfig can be used to define the permission of the   addon agent to access the hub cluster - CustomSigner: the addon agent can access the hub cluster through user-defined endpoints.   When this type is used, the CustomSignerRegistrationConfig can be used to define how   to issue the client certificate for the addon agent. | N/A |
## Status Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
