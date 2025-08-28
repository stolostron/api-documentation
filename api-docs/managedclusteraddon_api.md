# ManagedClusterAddOn API

ManagedClusterAddOn is the Custom Resource object which holds the current state
of an add-on. This object is used by add-on operators to convey their state.
This resource should be created in the ManagedCluster namespace.

## Spec Fields

spec holds configuration that could apply to any operator.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **configs** | `array` | configs is a list of add-on configurations. In scenario where the current add-on has its own configurations. An empty list means there are no default configurations for add-on. The default is an empty list | N/A |
| └>&nbsp;&nbsp; **group** | `string` | group of the add-on configuration. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | name of the add-on configuration. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | namespace of the add-on configuration. If this field is not set, the configuration is in the cluster scope. | N/A |
| └>&nbsp;&nbsp; **resource** | `string` | resource of the add-on configuration. | N/A |
|  **installNamespace** | `string` | installNamespace is the namespace on the managed cluster to install the addon agent. If it is not set, open-cluster-management-agent-addon namespace is used to install the addon agent. | `Pattern=^[a-z0-9]([-a-z0-9]*[a-z0-9])?$` |
## Status Fields

status holds the information about the state of an operator.  It is consistent with status information across
the Kubernetes ecosystem.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **addOnConfiguration** | `object` | Deprecated: Use configReferences instead. addOnConfiguration is a reference to configuration information for the add-on. This resource is used to locate the configuration resource for the add-on. | N/A |
| └>&nbsp;&nbsp; **crName** | `string` | crName is the name of the CR used to configure instances of the managed add-on. This field should be configured if add-on CR have a consistent name across the all of the ManagedCluster instaces. | N/A |
| └>&nbsp;&nbsp; **crdName** | `string` | crdName is the name of the CRD used to configure instances of the managed add-on. This field should be configured if the add-on have a CRD that controls the configuration of the add-on. | N/A |
| └>&nbsp;&nbsp; **lastObservedGeneration** | `integer` | lastObservedGeneration is the observed generation of the custom resource for the configuration of the addon. | N/A |
|  **addOnMeta** | `object` | addOnMeta is a reference to the metadata information for the add-on. This should be same as the addOnMeta for the corresponding ClusterManagementAddOn resource. | N/A |
| └>&nbsp;&nbsp; **description** | `string` | description represents the detailed description of the add-on. | N/A |
| └>&nbsp;&nbsp; **displayName** | `string` | displayName represents the name of add-on that will be displayed. | N/A |
|  **conditions** | `array` | conditions describe the state of the managed and monitored components for the operator. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **configReferences** | `array` | configReferences is a list of current add-on configuration references. This will be overridden by the clustermanagementaddon configuration references. | N/A |
| └>&nbsp;&nbsp; **desiredConfig** | `object` | desiredConfig record the desired config spec hash. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | name of the add-on configuration. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | namespace of the add-on configuration. If this field is not set, the configuration is in the cluster scope. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **specHash** | `string` | spec hash for an add-on configuration. | N/A |
| └>&nbsp;&nbsp; **group** | `string` | group of the add-on configuration. | N/A |
| └>&nbsp;&nbsp; **lastAppliedConfig** | `object` | lastAppliedConfig record the config spec hash when the corresponding ManifestWork is applied successfully. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | name of the add-on configuration. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | namespace of the add-on configuration. If this field is not set, the configuration is in the cluster scope. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **specHash** | `string` | spec hash for an add-on configuration. | N/A |
| └>&nbsp;&nbsp; **lastObservedGeneration** | `integer` | Deprecated: Use LastAppliedConfig instead lastObservedGeneration is the observed generation of the add-on configuration. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | name of the add-on configuration. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | namespace of the add-on configuration. If this field is not set, the configuration is in the cluster scope. | N/A |
| └>&nbsp;&nbsp; **resource** | `string` | resource of the add-on configuration. | N/A |
|  **healthCheck** | `object` | healthCheck indicates how to check the healthiness status of the current addon. It should be set by each addon implementation, by default, the lease mode will be used. | N/A |
| └>&nbsp;&nbsp; **mode** | `string` | mode indicates which mode will be used to check the healthiness status of the addon. | N/A |
|  **namespace** | `string` | namespace is the namespace on the managedcluster to put registration secret or lease for the addon. It is required when registration is set or healthcheck mode is Lease. | N/A |
|  **registrations** | `array` | registrations is the configurations for the addon agent to register to hub. It should be set by each addon controller on hub to define how the addon agent on managedcluster is registered. With the registration defined, The addon agent can access to kube apiserver with kube style API or other endpoints on hub cluster with client certificate authentication. A csr will be created per registration configuration. If more than one registrationConfig is defined, a csr will be created for each registration configuration. It is not allowed that multiple registrationConfigs have the same signer name. After the csr is approved on the hub cluster, the klusterlet agent will create a secret in the installNamespace for the registrationConfig. If the signerName is "kubernetes.io/kube-apiserver-client", the secret name will be "{addon name}-hub-kubeconfig" whose contents includes key/cert and kubeconfig. Otherwise, the secret name will be "{addon name}-{signer name}-client-cert" whose contents includes key/cert. | N/A |
| └>&nbsp;&nbsp; **signerName** | `string` | signerName is the name of signer that addon agent will use to create csr. | `Pattern=^([a-z0-9][a-z0-9-]*[a-z0-9]\.)+[a-z]+\/[a-z0-9-\.]+$` |
| └>&nbsp;&nbsp; **subject** | `object` | subject is the user subject of the addon agent to be registered to the hub. If it is not set, the addon agent will have the default subject "subject": {   "user": "system:open-cluster-management:cluster:{clusterName}:addon:{addonName}:agent:{agentName}",   "groups: ["system:open-cluster-management:cluster:{clusterName}:addon:{addonName}",             "system:open-cluster-management:addon:{addonName}", "system:authenticated"] } | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **groups** | `array` | groups is the user group of the addon agent. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **organizationUnit** | `array` | organizationUnit is the ou of the addon agent | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **user** | `string` | user is the user name of the addon agent. | N/A |
|  **relatedObjects** | `array` | relatedObjects is a list of objects that are "interesting" or related to this operator. Common uses are: 1. the detailed resource driving the operator 2. operator namespaces 3. operand namespaces 4. related ClusterManagementAddon resource | N/A |
| └>&nbsp;&nbsp; **group** | `string` | group of the referent. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | name of the referent. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | namespace of the referent. | N/A |
| └>&nbsp;&nbsp; **resource** | `string` | resource of the referent. | N/A |
|  **supportedConfigs** | `array` | SupportedConfigs is a list of configuration types that are allowed to override the add-on configurations defined in ClusterManagementAddOn spec. The default is an empty list, which means the add-on configurations can not be overridden. | N/A |
| └>&nbsp;&nbsp; **group** | `string` | group of the add-on configuration. | N/A |
| └>&nbsp;&nbsp; **resource** | `string` | resource of the add-on configuration. | N/A |
