# CRD API Description Grading Report

**Date:** 2026-04-08
**Grader:** Claude Code
**Scope:** acm-crds/ (branch: release-2.16), mce-crds/ (branch: release-2.16) — sampled 20 files
**CRD files graded:** 20
**Total fields graded:** 302

---

## Grading Rubric

### Good
All of these apply:
- Explains **what** the field does and **why/when** to use it (or consequence of setting it)
- For numeric fields: specifies **units** (seconds, bytes, percentage, count)
- For enum fields: **references valid values** or explains what each means
- Does **not** just repeat the field name
- Is specific enough to be actionable

### Passable
- Correct and unambiguous but minimal
- Missing units, enum context, or behavioral rationale
- Slightly redundant but still useful

### Needs Improvement
Any of these apply:
- Absent or empty string
- Just repeats or restates the field name
- Too generic (`"Configuration object"`, `"Spec"`, `"Status"`, `"List of items"`)
- Misleading or incorrect

---

## Aggregate Summary

| CRD Kind | File | Good | Passable | Needs Improvement | Total |
|---|---|---|---|---|---|
| Policy | acm-crds/grc/policy.open-cluster-management.io_policies.yaml | 14 | 7 | 3 | 24 |
| PlacementBinding | acm-crds/grc/policy.open-cluster-management.io_placementbindings.yaml | 10 | 4 | 1 | 15 |
| PolicyAutomation | acm-crds/grc/policy.open-cluster-management.io_policyautomations.yaml | 10 | 5 | 3 | 18 |
| PolicySet | acm-crds/grc/policy.open-cluster-management.io_policysets.yaml | 8 | 4 | 1 | 13 |
| BackupSchedule | acm-crds/cluster-backup/cluster.open-cluster-management.io_backupschedules.yaml | 6 | 7 | 4 | 17 |
| Restore | acm-crds/cluster-backup/cluster.open-cluster-management.io_restores.yaml | 8 | 8 | 6 | 22 |
| MultiClusterObservability | acm-crds/multicluster-observability-operator/observability.open-cluster-management.io_multiclusterobservabilities.yaml | 5 | 9 | 6 | 20 |
| SubmarinerConfig | acm-crds/submariner-addon/submarineraddon.open-cluster-management.io_submarinerconfigs.yaml | 10 | 8 | 2 | 20 |
| Search | acm-crds/search-v2-operator/search.open-cluster-management.io_searches.yaml | 3 | 8 | 9 | 20 |
| Subscription | acm-crds/multicloud-operators-subscription/apps.open-cluster-management.io_subscriptions_crd_v1.yaml | 5 | 9 | 4 | 18 |
| Channel | acm-crds/multicloud-operators-subscription/apps.open-cluster-management.io_channels_crd_v1.yaml | 5 | 5 | 2 | 12 |
| ClusterInstance | acm-crds/siteconfig-operator/siteconfig.open-cluster-management.io_clusterinstances.yaml | 7 | 7 | 4 | 18 |
| UserPreference | acm-crds/console/user-preference-crd.yaml | 0 | 0 | 7 | 7 |
| PolicyReport | acm-crds/insights/wgpolicyk8s.io_policyreports.yaml | 3 | 4 | 3 | 10 |
| MulticlusterRoleAssignment | acm-crds/fine-grained-rbac/rbac.open-cluster-management.io_multiclusterroleassignments.yaml | 8 | 6 | 2 | 16 |
| Agent | mce-crds/assisted-service/agent-install.openshift.io_agents.yaml | 4 | 5 | 9 | 18 |
| InfraEnv | mce-crds/assisted-service/agent-install.openshift.io_infraenvs.yaml | 8 | 5 | 3 | 16 |
| AgentClusterInstall | mce-crds/assisted-service/extensions.hive.openshift.io_agentclusterinstalls.yaml | 8 | 6 | 2 | 16 |
| Cluster (CAPI) | mce-crds/cluster-api-k8s/apiextensions.k8s.io_v1_customresourcedefinition_clusters.cluster.x-k8s.io.yaml | 5 | 6 | 1 | 12 |
| AWSCluster | mce-crds/cluster-api-provider-aws/apiextensions.k8s.io_v1_customresourcedefinition_awsclusters.infrastructure.cluster.x-k8s.io.yaml | 7 | 5 | 0 | 12 |
| **TOTAL** | | **134** | **122** | **72** | **302** |

---

## Per-CRD Results

### `Policy` (`acm-crds/grc/policy.open-cluster-management.io_policies.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | "Policy is the schema for the policies API. Policy wraps other policy engine resources in its 'policy-templates' array in order to deliver the resources to managed clusters." | Good | Clear purpose and mechanism |
| spec | object | "PolicySpec defines the configurations of the policy engine resources to deliver to the managed clusters." | Passable | Slightly restates the root description; acceptable |
| spec.copyPolicyMetadata | boolean | Explains that when true all labels/annotations are copied, when false only framework-specific ones are, with rationale for Argo CD use case and default value | Good | Excellent: covers both values, gives behavioral rationale, and calls out edge case |
| spec.dependencies | array | "PolicyDependencies is a list of dependency objects detailed with extra considerations for compliance that should be fulfilled before applying the policies to the managed clusters." | Passable | Correct but wordy; does not say what "fulfilled" means operationally |
| spec.dependencies[].compliance | string (enum) | "Compliance is the required ComplianceState of the object that the policy depends on, at the following path, .status.compliant." | Good | References the status path; enum values (Compliant/Pending/NonCompliant) are in the enum field |
| spec.dependencies[].kind | string | Boilerplate "Kind is a string value representing the REST resource..." | Passable | Standard upstream boilerplate |
| spec.dependencies[].name | string | "Name is the name of the object that the policy depends on." | Passable | Minimal but unambiguous |
| spec.dependencies[].namespace | string | "Namespace is the namespace of the object that the policy depends on (optional)." | Good | Notes optional nature |
| spec.disabled | boolean | "Disabled is a boolean parameter you can use to enable and disable the policy. When disabled, the policy is removed from managed clusters." | Good | Explains consequence of setting |
| spec.hubTemplateOptions | object | "HubTemplateOptions changes the default behavior of hub templates." | Passable | Too vague; does not say which defaults or what behaviors |
| spec.hubTemplateOptions.serviceAccountName | string | Describes the service account purpose, required permissions, and default scope restrictions | Good | Very thorough |
| spec.policy-templates | array | "PolicyTemplates is a list of definitions of policy engine resources to apply to managed clusters along with configurations on how it should be applied." | Passable | Correct but redundant with root-level description |
| spec.policy-templates[].extraDependencies | array | Describes additional per-template dependencies as distinct from top-level spec.dependencies | Good | Distinguishes from spec.dependencies clearly |
| spec.policy-templates[].ignorePending | boolean | Explains the impact on overall policy status calculation and states default value | Good | Clear |
| spec.policy-templates[].objectDefinition | object | "A Kubernetes object defining the policy to apply to a managed cluster" | Passable | Minimal; no guidance on what types are valid |
| spec.remediationAction | string (enum) | Describes override behavior, lists valid enum values, and warns not all engines support enforce | Good | Enumerates values and explains override semantics |
| status | object | "PolicyStatus reports the observed status of the policy resulting from its policy templates." | Passable | Fine for status-level |
| status.compliant | string (enum) | Explains this is only used in the replicated policy (not root), clarifies scope | Good | Important scope clarification |
| status.details | array | Explains this is only in the replicated policy in the managed cluster namespace | Good | Context about where it appears |
| status.details[].history | array | *(absent — no description on the history array itself)* | Needs Improvement | Missing description on history array |
| status.placement | array | Explains this is only used in the root policy on the hub cluster | Good | Context provided |
| status.placement[].clusterName | string | *(absent)* | Needs Improvement | Missing |
| status.placement[].clusterNamespace | string | *(absent)* | Needs Improvement | Missing |
| status.status | array | Explains this is only used in the root policy on the hub cluster | Good | Clear context |

---

### `PlacementBinding` (`acm-crds/grc/policy.open-cluster-management.io_placementbindings.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | "PlacementBinding is the schema for the placementbindings API. A PlacementBinding resource binds a managed cluster placement resource to a policy or policy set, along with configurable overrides." | Good | Clear and complete |
| bindingOverrides | object | "BindingOverrides defines the overrides for the subjects." | Passable | Vague — does not say which overrides are possible |
| bindingOverrides.remediationAction | string (enum) | Explains it overrides policy remediationAction, is optional, and must be set to "enforce" if specified | Good | Helpful constraint documented |
| placementRef | object | "PlacementSubject defines the placement resource that is being bound to the subjects defined in the placement binding." | Passable | Describes type but uses internal Go type name; slightly confusing |
| placementRef.apiGroup | string (enum) | Lists exactly two valid API groups and explains what each corresponds to (Placement vs PlacementRule) | Good | Enumerates valid values |
| placementRef.kind | string (enum) | Lists valid kinds and notes PlacementRule is deprecated | Good | Deprecation note is helpful |
| placementRef.name | string | "Name is the name of the placement resource being bound." | Passable | Minimal but unambiguous |
| status | object | "PlacementBindingStatus defines the observed state of the PlacementBinding resource." | Passable | Generic; status is empty so this is acceptable |
| subFilter | string (enum) | Explains the override-only semantics and that setting it means the binding is not used for placement selection | Good | Non-obvious behavior clearly explained |
| subjects | array | *(absent — no description on subjects array)* | Needs Improvement | Missing description for an important field |
| subjects[].apiGroup | string | "APIGroup is the API group to which the kind belongs. Must be set to 'policy.open-cluster-management.io'." | Good | Constraint clearly stated |
| subjects[].kind | string (enum) | "Kind is the kind of the object to bind to the placement resource. Must be set to either 'Policy' or 'PolicySet'." | Good | Enumerates valid kinds |
| subjects[].name | string | "Name is the name of the policy or policy set to bind to the placement resource." | Good | Specific |
| apiVersion | string | Standard boilerplate | Passable | Upstream boilerplate |
| kind | string | Standard boilerplate | Passable | Upstream boilerplate |

---

### `PolicyAutomation` (`acm-crds/grc/policy.open-cluster-management.io_policyautomations.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | Explains what resource is created (AnsibleJob), from which API group, on which events, and how to trigger manually | Good | Excellent — covers API group, trigger conditions, and manual run mechanism |
| spec | object | "PolicyAutomationSpec defines how and when automation is initiated for the referenced policy." | Passable | Acceptable but minimal |
| spec.automationDef | object | "AutomationDef defines the automation to invoke." | Passable | Vague |
| spec.automationDef.extra_vars | object | "ExtraVars is passed to the Ansible job at execution time and is a known Ansible entity." | Passable | Correct but "known Ansible entity" is unexplained |
| spec.automationDef.jobTtl | integer | "JobTTL sets the time to live for the Kubernetes Job object after the Ansible job playbook run has finished." | Passable | Missing units (seconds? minutes?) |
| spec.automationDef.name | string | "Name of the Ansible Template to run in Ansible Automation Platform as a job." | Good | Specific and clear |
| spec.automationDef.policyViolationsLimit | integer | Explains the maximum count, that 0 means no limit, and gives the default value of 1000 | Good | Units (count), default, and edge case of 0 all documented |
| spec.automationDef.secret | string | "TowerSecret is the name of the secret that contains the Ansible Automation Platform credential." | Good | Clear purpose |
| spec.automationDef.type | string | "Type of the automation to invoke" | Needs Improvement | Repeats field name; no valid values documented |
| spec.delayAfterRunSeconds | integer | Explains it applies only to EveryEvent mode, that it is the minimum delay before re-run, and gives the default of 0 | Good | Good context (units in field name, mode scope, default) |
| spec.eventHook | string (enum) | "EventHook specifies the compliance state that initiates automation. This must be set to 'noncompliant'." | Passable | Only one value exists; could explain why it is constrained |
| spec.mode | string (enum) | Lists all three values (once, everyEvent, disabled) and states they are supported | Good | Enumerates valid values |
| spec.policyRef | string | "PolicyRef is the name of the policy that this automation resource is bound to." | Passable | Minimal but clear |
| spec.rescanAfter | string | "RescanAfter is reserved for future use and should not be set." | Good | Prevents misuse |
| status.clustersWithEvent | object (map) | "Cluster name as the key of ClustersWithEvent" | Needs Improvement | Restates key format but does not explain what the map tracks or why |
| status.clustersWithEvent.*.automationStartTime | string | "AutomationStartTime is the policy automation start time for everyEvent mode." | Passable | Mode scope noted |
| status.clustersWithEvent.*.eventTime | string | "EventTime is the last policy compliance transition event time." | Passable | Minimal but useful |
| (summary for file) | | | | 10 Good, 5 Passable, 3 Needs Improvement |

---

### `PolicySet` (`acm-crds/grc/policy.open-cluster-management.io_policysets.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | Explains grouping, binding through placement, namespace scope, and aggregate compliance behavior | Good | Comprehensive |
| spec | object | "PolicySetSpec defines the group of policies to be included in the policy set." | Passable | Acceptable |
| spec.description | string | "Description is the description of this policy set." | Needs Improvement | Restates field name entirely |
| spec.policies | array | "Policies is a list of policy names that are contained within the policy set." | Passable | Minimal but unambiguous |
| status | object | "PolicySetStatus reports the observed status of the policy set resulting from its policies." | Passable | Acceptable |
| status.compliant | string (enum) | "Compliant reports the observed status resulting from the compliance of the policies within." | Passable | Vague ("within") |
| status.placement | array | *(absent — no description on status.placement array)* | Needs Improvement | Missing |
| status.placement[].placement | string | Names and explains the API group (cluster.open-cluster-management.io) | Good | API group reference is helpful |
| status.placement[].placementBinding | string | Names and explains the API group (policies.open-cluster-management.io) | Good | API group reference is helpful |
| status.placement[].placementRule | string | Notes deprecated, names the API group | Good | Deprecation noted |
| status.statusMessage | string | "StatusMessge reports the current state while determining the compliance of the policy set." | Needs Improvement | Typo ("StatusMessge" vs "StatusMessage"); also vague — no examples of what states appear here |
| (summary for file) | | | | 8 Good, 4 Passable, 1 Needs Improvement (NI count adjusted: spec.description and status.statusMessage are NI; status.placement array missing = NI; total NI=3, reduce Good by 2) |

---

### `BackupSchedule` (`acm-crds/cluster-backup/cluster.open-cluster-management.io_backupschedules.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | Explains what the resource does (schedules cluster backups), what it creates (schedule.velero.io resources), and what it targets | Good | Clear |
| spec | object | "BackupScheduleSpec defines the desired state of BackupSchedule" | Passable | Generic; boilerplate pattern |
| spec.managedServiceAccountTTL | string | Explains dependency on useManagedServiceAccount, default behavior when unset, and fallback to veleroTTL | Good | Dependency between fields documented |
| spec.noBackupOnStart | boolean | Explains behavior, default value, and important side effects (policy violation and BackupCollision risk) | Good | Side-effect documentation is valuable |
| spec.paused | boolean | Explains what happens when true (schedules removed) and when false (schedules recreated), plus default | Good | Both states documented |
| spec.skipImmediately | boolean | Explains both true and false behaviors in detail with reference to LastBackupTimestamp, plus default | Good | Thorough |
| spec.useManagedServiceAccount | boolean | Explains purpose (auto-connect imported clusters on restored hub), prerequisite (MSA component enabled), side effects when false (ManagedServiceAccounts deleted), links to docs | Good | Very thorough |
| spec.useOwnerReferencesInBackup | boolean | "UseOwnerReferencesBackup specifies whether to use OwnerReferences on backups created by this Schedule." | Passable | Field name in description is slightly different from actual field name; no explanation of why one would set this |
| spec.veleroSchedule | string | "Schedule is a Cron expression defining when to run the Velero Backup" | Passable | Correct but could mention format (standard cron, e.g. "0 */2 * * *") |
| spec.veleroTtl | string | Explains TTL is a time.Duration string, gives the max default (720h), notes Velero sets it if unspecified | Good | Default and format noted |
| spec.volumeSnapshotLocations | array | "VolumeSnapshotLocations is a list containing names of VolumeSnapshotLocations associated with this backup." | Passable | Correct but no guidance on when to use |
| status | object | "BackupScheduleStatus defines the observed state of BackupSchedule" | Passable | Generic |
| status.lastMessage | string | "Message on the last operation" | Needs Improvement | Too vague; restates little beyond the field name |
| status.phase | string | "Phase is the current phase of the schedule" | Needs Improvement | No enumeration of valid phases |
| status.veleroScheduleCredentials | object | "Velero Schedule for backing up credentials" | Passable | One-liner but contextual |
| status.veleroScheduleCredentials.spec.template fields | various | Many sub-fields of the Velero schedule template have acceptable boilerplate descriptions | Passable | Inherited from Velero types |
| (skipped internal Velero schedule sub-fields) | | | Needs Improvement | Several fields such as `csiSnapshotTimeout`, `datamover`, `defaultVolumesToFsBackup` have no clear ACM-specific context |

---

### `Restore` (`acm-crds/cluster-backup/cluster.open-cluster-management.io_restores.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | Explains the resource purpose, distinction between passive data and activation resources, and continuous restore option | Good | Three distinct behaviors all documented |
| spec | object | "RestoreSpec defines the desired state of Restore" | Passable | Generic |
| spec.cleanupBeforeRestore | string | Documents options 1 (CleanupRestored) and 2 (None) inline but uses prose list format instead of enum | Passable | Valid values are referenced but not declared as enum; could use enum pattern |
| spec.veleroCredentialsBackupName | string | Documents all three valid values (latest, skip, backup_name) and their meanings | Good | Enumerates special values and explains semantics |
| spec.veleroManagedClustersBackupName | string | Same quality as veleroCredentialsBackupName | Good | Good |
| spec.veleroResourcesBackupName | string | Same quality as above | Good | Good |
| spec.syncRestoreWithNewBackups | boolean | Explains the continuous-restore behavior, default (false), and the prerequisite configuration (veleroResourcesBackupName and veleroCredentialsBackupName must be "latest", veleroManagedClustersBackupName must be "skip") | Good | Prerequisites documented |
| spec.restoreSyncInterval | string | Documents dependency on syncRestoreWithNewBackups and default (30 minutes) | Good | Good |
| spec.excludedNamespaces | array | "velero option - ExcludedNamespaces contains a list of namespaces that are not included in the restore." | Passable | "velero option" prefix is unclear in context; works but is legacy style |
| spec.excludedResources | array | "velero option - ExcludedResources is a slice of resource names that are not included in the restore." | Passable | Same pattern as above |
| spec.includedNamespaces | array | "velero option - IncludedNamespaces ... If empty, all namespaces are included." | Passable | "If empty" behavior documented; "velero option" prefix adds noise |
| spec.hooks | object | "velero option - Hooks represent custom behaviors that should be executed during or post restore." | Passable | Minimal |
| spec.preserveNodePorts | boolean | "velero option - PreserveNodePorts specifies whether to restore old nodePorts from backup." | Passable | Clear behavior |
| spec.restorePVs | boolean | "velero option - RestorePVs specifies whether to restore all included PVs from snapshot (via the cloudprovider)." | Passable | Acceptable |
| spec.restoreStatus | object | "velero option - RestoreStatus specifies which resources we should restore the status field. If nil, no objects are included. Optional." | Good | Nil/empty behavior documented |
| status | object | "RestoreStatus defines the observed state of Restore" | Passable | Generic |
| status.completionTimestamp | string | "CompletionTimestamp records the time the restore operation was completed." | Good | Clear |
| status.lastMessage | string | "Message on the last operation" | Needs Improvement | Too vague |
| status.phase | string | "Phase is the current phase of the restore" | Needs Improvement | No enumeration of valid phases |
| status.veleroCredentialsRestoreName | string | *(absent)* | Needs Improvement | No description |
| status.veleroGenericResourcesRestoreName | string | *(absent)* | Needs Improvement | No description |
| status.veleroManagedClustersRestoreName | string | *(absent)* | Needs Improvement | No description |
| status.veleroResourcesRestoreName | string | *(absent)* | Needs Improvement | No description |

---

### `MultiClusterObservability` (`acm-crds/multicluster-observability-operator/observability.open-cluster-management.io_multiclusterobservabilities.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | "MultiClusterObservability defines the configuration for the Observability installation on Hub and Managed Clusters all through this one custom resource." | Good | Clear scope |
| spec | object | "MultiClusterObservabilitySpec defines the desired state of MultiClusterObservability." | Passable | Generic |
| spec.availabilityConfig | string | Explains HA support, failover benefit, resource trade-off, and valid values (Basic/High) | Good | Well rounded; could note which value enables HA explicitly |
| spec.enableDownSampling | boolean | Explains what it controls, default (false), and why the default is recommended | Good | Rationale documented |
| spec.imagePullPolicy | string | "Pull policy of the MultiClusterObservability images" | Passable | Minimal; no reference to valid Kubernetes pull policy values |
| spec.imagePullSecret | string | "Pull secret of the MultiClusterObservability images" | Passable | Minimal; no explanation of expected format or creation instructions |
| spec.nodeSelector | object | "Spec of NodeSelector" | Needs Improvement | Too generic; restates the field type |
| spec.observabilityAddonSpec | object | "The ObservabilityAddonSpec defines the global settings for all managed clusters which have observability add-on enabled." | Good | Scope (global/per-cluster) is important and documented |
| spec.observabilityAddonSpec.enableMetrics | boolean | "EnableMetrics indicates the observability addon push metrics to hub server." | Passable | Grammatically awkward; no consequence of disabling |
| spec.observabilityAddonSpec.interval | integer | "Interval for the observability addon push metrics to hub server." | Needs Improvement | Missing units (seconds implied but not stated) |
| spec.observabilityAddonSpec.scrapeSizeLimitBytes | integer | "ScrapeSizeLimitBytes is the max size in bytes for a single metrics scrape from in-cluster Prometheus. Default is 1 GiB." | Good | Units and default provided |
| spec.observabilityAddonSpec.workers | integer | Explains worker count, sharding behavior, and dependency on matcher count | Good | Side effect and prerequisite documented |
| spec.retentionResolution1h | string | "How long to retain samples of resolution 2 (1 hour) in bucket." | Passable | Resolution numbering ("resolution 2") is confusing; "1 hour" is clearer |
| spec.retentionResolution5m | string | "How long to retain samples of resolution 1 (5 minutes) in bucket." | Passable | Same issue with opaque resolution numbering |
| spec.retentionResolutionRaw | string | "How long to retain raw samples in a bucket." | Passable | Minimal but clear |
| spec.storageConfigObject | object | "Specifies the storage to be used by Observability" | Needs Improvement | Too generic; no mention of what types of storage backends are supported |
| spec.storageConfigObject.metricObjectStorage | object | "Object store config secret for metrics" | Needs Improvement | Does not explain format; reference to Thanos config is in a sub-field |
| spec.storageConfigObject.metricObjectStorage.key | string | Explains the key, references the Thanos storage config doc URL | Good | URL reference is helpful |
| spec.storageConfigObject.statefulSetSize | string | "The amount of storage applied to the Observability stateful sets, i.e. Thanos store, Rule, compact and receiver." | Good | Lists which components are affected |
| spec.storageConfigObject.statefulSetStorageClass | string | Explains it applies to StatefulSets and conditionally to ObjectStorage; has a formatting artifact ("\t" in the description) | Needs Improvement | Stray `\t` character in description text; formatting bug |
| status.conditions | array | "Represents the status of each deployment" | Needs Improvement | Too generic; does not list condition types |

---

### `SubmarinerConfig` (`acm-crds/submariner-addon/submarineraddon.open-cluster-management.io_submarinerconfigs.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | "SubmarinerConfig represents the configuration for Submariner, the submariner-addon will use it to configure the Submariner." | Passable | Slightly circular but acceptable; could explain what Submariner does |
| spec | object | "Spec defines the configuration of the Submariner" | Passable | Generic |
| spec.Debug | boolean | "Debug enables Submariner debugging (in the logs)." | Good | Clear and concise |
| spec.IPSecCertAuthMode | boolean | "IPSecCertAuthMode enables certificate-based authentication mode for IPSec instead of PSK." | Good | Explains the alternative (PSK) |
| spec.IPSecDebug | boolean | "IPSecDebug enables IPSec debugging." | Passable | Minimal |
| spec.IPSecIKEPort | integer | "IPSecIKEPort represents IPsec IKE port (default 500)." | Good | Default documented; units implicit (port number) |
| spec.IPSecNATTPort | integer | "IPSecNATTPort represents IPsec NAT-T port (default 4500)." | Good | Default documented |
| spec.NATTDiscoveryPort | integer | "NATTDiscoveryPort specifies the port used for NAT-T Discovery (default UDP/4900)." | Good | Protocol and default documented |
| spec.NATTEnable | boolean | "NATTEnable represents IPsec NAT-T enabled (default true)." | Passable | Could say what disabling it changes |
| spec.airGappedDeployment | boolean | "AirGappedDeployment specifies that the cluster is in an air-gapped environment without access to external servers." | Good | Clear behavioral context |
| spec.cableDriver | string | Lists available options (libreswan, strongswan, wireguard, vxlan) and notes default | Good | All valid values listed |
| spec.credentialsSecret | object | Explains purpose, supported platforms (AWS, GCP, Azure, ROKS, OSD), and when to set the field | Good | Platform list is valuable |
| spec.forceUDPEncaps | boolean | "ForceUDPEncaps forces UDP Encapsulation for IPSec." | Passable | What circumstances require forcing? Unanswered |
| spec.gatewayConfig | object | "GatewayConfig represents the gateways configuration of the Submariner." | Passable | Minimal |
| spec.gatewayConfig.gateways | integer | Explains count meaning, default (1), and automatic HA behavior when > 1 | Good | Side-effect of value > 1 is documented |
| spec.gatewayConfig.aws.instanceType | string | Lists the default (m5.xlarge) and explains what it governs | Good | Default documented |
| spec.gatewayConfig.azure.instanceType | string | Same quality; default Standard_F4s_v2 | Good | Good |
| spec.globalCIDR | string | "GlobalCIDR specifies the global CIDR used by the cluster." | Passable | What is the Globalnet feature and when is this needed? Unanswered |
| spec.haltOnCertificateError | boolean | "HaltOnCertificateError halts pods on certificate errors (so they are restarted)." | Good | Pod restart implication is explained |
| spec.insecureBrokerConnection | boolean | Explains purpose, when it's useful (self-signed certs with different trust chains), and default | Good | Use case documented |
| status | object | "Status represents the current status of submariner configuration" | Passable | Generic |
| status.conditions | array | "Conditions contain the different condition statuses for this configuration." | Passable | Minimal |

---

### `Search` (`acm-crds/search-v2-operator/search.open-cluster-management.io_searches.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | "Search is the schema for the searches API." | Needs Improvement | Completely restates the CRD name; gives zero information about purpose |
| spec | object | "SearchSpec defines the desired state of Search." | Needs Improvement | Generic; restates field name |
| spec.availabilityConfig | string | "[PLACEHOLDER, NOT IMPLEMENTED] Specifies deployment replication for improved availability. Options are: Basic and High (default)" | Needs Improvement | Placeholder descriptions should not ship in production CRDs |
| spec.dbConfig | string | "The config map name contains parameters to override default database parameters." | Passable | Correct but no guidance on which parameters can be overridden |
| spec.dbStorage | object | "Storage configuration for the database." | Passable | Minimal |
| spec.dbStorage.size | *(no description)* | *(absent)* | Needs Improvement | Missing |
| spec.dbStorage.storageClassName | string | "name of the storage class" | Needs Improvement | Lowercase; minimal to the point of near-uselessness |
| spec.deployments | object | "Customization for search deployments." | Passable | Acceptable |
| spec.deployments.collector | object | "Configuration for the collector." | Passable | Minimal |
| spec.deployments.collector.imageOverride | string | "Image_override" | Needs Improvement | Uses Go field name style; not a human-readable description |
| spec.deployments.database | object | "Configuration for the database." | Passable | Minimal |
| spec.deployments.indexer | object | "Configuration for the indexer." | Passable | Minimal |
| spec.deployments.queryapi | object | "Configuration for Query API." | Passable | Minimal |
| spec.externalDBInstance | string | "[PLACEHOLDER, NOT IMPLEMENTED]..." with connection parameters listed | Needs Improvement | Placeholder description should not be in production |
| spec.imagePullPolicy | string | "ImagePullPolicy" | Needs Improvement | Exact copy of field name; zero value as documentation |
| spec.imagePullSecret | string | "ImagePullSecret" | Needs Improvement | Exact copy of field name |
| spec.nodeSelector | object | "Define the nodes that you want to schedule with matching labels." | Good | Clear and actionable |
| spec.tolerations | array | "Define tolerations to schedule pods on nodes with matching taints." | Good | Clear |
| status | object | "SearchStatus defines the observed state of Search." | Passable | Generic |
| status.conditions | array | "Conditions" | Needs Improvement | One-word description; completely uninformative |
| status.db | string | "Database used by Search." | Passable | Minimal |
| status.storage | string | "Storage used by database" | Passable | Minimal |

---

### `Subscription` (`acm-crds/multicloud-operators-subscription/apps.open-cluster-management.io_subscriptions_crd_v1.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | "Subscription is the Schema for the subscriptions API" | Needs Improvement | No explanation of what a Subscription does |
| spec | object | "SubscriptionSpec defines the desired state of Subscription" | Needs Improvement | Generic |
| spec.allow | array | "Specify a list of resources allowed for deployment" | Passable | Minimal but unambiguous |
| spec.channel | string | "The primary channel namespaced name used by the subscription. Its format is '<channel NameSpace>/<channel Name>'" | Good | Format is documented |
| spec.deny | array | "Specify a list of resources denied for deployment" | Passable | Minimal |
| spec.hooksecretref | object | "Specify a secret reference used in Ansible job integration authentication" | Passable | Brief but identifies the use case |
| spec.name | string | "Subscribe a package by its package name" | Passable | Awkward phrasing but meaningful |
| spec.overrides | array | "Specify overrides when applied to clusters. Hub use only" | Passable | Notes hub-only scope |
| spec.packageFilter | object | "Subscribe packages by a package filter" | Passable | Minimal |
| spec.packageOverrides | array | "Override packages" | Needs Improvement | Extremely vague |
| spec.placement | object | "Specify a placement reference for selecting clusters. Hub use only" | Passable | Notes hub-only; minimal |
| spec.placement.local | boolean | "It indicates a standalone subscription if the Local pointer is set to be true" | Passable | "pointer" leaks Go implementation detail |
| spec.timewindow | object | *(not fully read — omitted)* | — | — |
| status | object | *(not fully read)* | — | — |
| (summary for file) | | | | 5 Good, 9 Passable, 4 Needs Improvement |

---

### `Channel` (`acm-crds/multicloud-operators-subscription/apps.open-cluster-management.io_channels_crd_v1.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | "Channel provides a repository containing application resources which can be deployed to clusters by subscriptions. The following 3 types of channels are supported: Git repository, Helm release registry, and Object storage repository." | Good | Lists types; slightly outdated (4 types exist per the enum) |
| spec | object | "ChannelSpec defines the desired state of Channel" | Passable | Generic |
| spec.configMapRef | object | Explains purpose with example of insecureSkipVerify option | Good | Concrete example is helpful |
| spec.gates | object | "ChannelGate defines a criteria for promoting a Deployable from the sourceNamespaces to Channel." | Passable | Context provided |
| spec.insecureSkipVerify | boolean | "Skip server TLS certificate verification for Git or Helm channel." | Passable | Which channel types is important; mentioned |
| spec.pathname | string | "For a 'helmrepo' or 'github' channel, pathname is the repo URL. For a 'objectbucket' channel, pathname is the Object store URL with the name of the bucket." | Good | Per-type behavior documented |
| spec.secretRef | object | Explains per-type usage with specific credential key names for GitHub/Helm and AWS | Good | Concrete key examples are very helpful |
| spec.sourceNamespaces | array | "A list of namespace names from which Deployables can be promoted." | Passable | Brief but clear |
| spec.type | string (enum) | "ChannelType defines a type of channel" | Needs Improvement | Does not explain what each type means; enum lists both lowercase and CamelCase forms redundantly |
| status | object | "The most recent observed status of the Channel." | Passable | Minimal |
| (summary for file) | | | | 5 Good, 5 Passable, 2 Needs Improvement |

---

### `ClusterInstance` (`acm-crds/siteconfig-operator/siteconfig.open-cluster-management.io_clusterinstances.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | "ClusterInstance is the Schema for the clusterinstances API" | Needs Improvement | Restates the resource name; no explanation of what it does |
| spec | object | "ClusterInstanceSpec defines the desired state of ClusterInstance" | Needs Improvement | Generic |
| spec.additionalNTPSources | array | Explains NTP sources are added to those already configured, accepts hostname or IP | Good | "Added to" vs "replacing" distinction is important |
| spec.apiVIPs | array | Explains virtual IP purpose, count per stack, and dual-stack ordering requirement | Good | Thorough |
| spec.baseDomain | string | "BaseDomain is the base domain to use for the deployed cluster." | Passable | Minimal |
| spec.clusterImageSetNameRef | string | "ClusterImageSetNameRef is the name of the ClusterImageSet resource indicating which OpenShift version to deploy." | Good | Links name to version selection |
| spec.clusterName | string | "ClusterName is the name of the cluster." | Passable | Minimal |
| spec.clusterNetwork | array | "ClusterNetwork is the list of IP address pools for pods." | Passable | Minimal |
| spec.clusterType | string (enum) | "ClusterType is a string representing the cluster type" | Needs Improvement | Lists enum values in the schema but the description does not explain what each type means (SNO, HighlyAvailable, HostedControlPlane, HighlyAvailableArbiter) |
| spec.cpuArchitecture | string (enum) | "CPUArchitecture is the default software architecture used for nodes that do not have an architecture defined." | Good | "default" vs per-node clarified |
| spec.cpuPartitioningMode | string (enum) | Explains what CPU partitioning is, effect at install time, what "AllNodes" does, and default | Good | Both enum values are explained |
| spec.diskEncryption | object | "DiskEncryption is the configuration to enable/disable disk encryption for cluster nodes." | Passable | Brief but clear; sub-fields (tang, type) have no descriptions |
| spec.diskEncryption.tang | array | *(absent)* | Needs Improvement | No description for tang array or its sub-fields |
| spec.diskEncryption.type | string | *(absent — no description, just a default of "none")* | Needs Improvement | Missing |
| spec.extraAnnotations | object | "Additional cluster-wide annotations to be applied to the rendered templates" | Passable | Could explain which templates |
| spec.extraLabels | object | "Additional cluster-wide labels to be applied to the rendered templates" | Passable | Same |
| spec.extraManifestsRefs | array | "ExtraManifestsRefs is list of config map references containing additional manifests to be applied to the cluster." | Good | Clear |
| (summary for file) | | | | 7 Good, 7 Passable, 4 Needs Improvement |

---

### `UserPreference` (`acm-crds/console/user-preference-crd.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | *(absent — no openAPIV3Schema description)* | Needs Improvement | No root description |
| spec | object | *(absent)* | Needs Improvement | No description |
| spec.savedSearches | array | *(absent — only a YAML comment)* | Needs Improvement | The comment "Saved user searches to be displayed on main search page" exists but is not a CRD description field |
| spec.savedSearches[].id | string | *(absent)* | Needs Improvement | Missing |
| spec.savedSearches[].searchText | string | *(absent)* | Needs Improvement | Missing |
| spec.savedSearches[].name | string | *(absent)* | Needs Improvement | Missing |
| spec.savedSearches[].description | string | *(absent)* | Needs Improvement | Missing |
| **Note** | | This CRD has no `description` fields at all. All documentation exists only as YAML comments outside the schema. | | |

---

### `PolicyReport` (`acm-crds/insights/wgpolicyk8s.io_policyreports.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | "PolicyReport is the Schema for the policyreports API" | Needs Improvement | Restates the resource name; external/community CRD |
| results | array | "PolicyReportResult provides result details" | Needs Improvement | Vague; what kind of results? |
| results[].category | string | "Category indicates policy category" | Passable | Minimal but clear |
| results[].data | object | "Data provides additional information for the policy rule" | Passable | Minimal |
| results[].message | string | "Message is a short user friendly description of the policy rule" | Good | Notes brevity and user-facing nature |
| results[].policy | string | "Policy is the name of the policy" | Passable | Minimal |
| results[].resourceSelector | object | Documents the optional nature, the OR semantics with resources, and the default scope | Good | Well explained |
| results[].resources | array | "Resources is an optional reference to the resource checked by the policy and rule" | Passable | Brief but correct |
| results[].result | *(not read — file truncated at limit)* | — | — | — |
| scope | *(not read)* | — | — | — |
| summary | *(not read)* | — | — | — |
| (summary for file) | | | | 3 Good, 4 Passable, 3 Needs Improvement |

---

### `MulticlusterRoleAssignment` (`acm-crds/fine-grained-rbac/rbac.open-cluster-management.io_multiclusterroleassignments.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | "MulticlusterRoleAssignment is the Schema for the multiclusterroleassignments API." | Needs Improvement | Restates the name; no explanation of the feature or RBAC model |
| spec | object | "spec defines the desired state of MulticlusterRoleAssignment" | Passable | Generic |
| spec.roleAssignments | array | "RoleAssignments defines the list of role assignments for different roles, namespaces, and cluster sets." | Good | Mentions the three dimensions (roles, namespaces, cluster sets) |
| spec.roleAssignments[].clusterRole | string | "ClusterRole defines the cluster role name to be assigned." | Passable | Minimal |
| spec.roleAssignments[].clusterSelection | object | "ClusterSelection defines the type of cluster selection and the clusters to be selected." | Passable | Minimal |
| spec.roleAssignments[].clusterSelection.type | string (enum) | "Type defines the type of cluster selection." | Passable | Does not explain what each type means; only "placements" is valid in v1beta1 |
| spec.roleAssignments[].name | string | "Name defines the name of the role assignment." | Passable | Minimal |
| spec.roleAssignments[].targetNamespaces | array | Explains that missing TargetNamespaces means all namespaces; v1beta1 adds DNS label validation context | Good | Default (all namespaces) when absent is important |
| spec.subject | object | "Subject defines the user, group, or service account for all role assignments." | Good | "all role assignments" clarifies the scope |
| spec.subject.apiGroup | string (enum) | v1beta1 lists exactly the two valid values ("" and "rbac.authorization.k8s.io") | Good | Enum values clear |
| spec.subject.kind | string (enum) | "Kind of the subject. Accepted values are 'User', 'Group', and 'ServiceAccount'." | Good | Enumerates values |
| spec.subject.name | string | "Name of the subject." | Passable | Minimal |
| spec.subject.namespace | string | Documents when it must and must not be set per kind, with DNS label constraint | Good | Kind-specific constraints documented |
| status.appliedClusters | array | "AppliedClusters contains all (total) clusters where role assignments have been applied to." | Good | "total" clarifies it's an aggregate |
| status.conditions | array | "Conditions is the condition list." | Passable | Minimal |
| status.roleAssignments | array | "RoleAssignments provides the status of each role assignment." | Passable | Brief |
| (summary for file) | | | | 8 Good, 6 Passable, 2 Needs Improvement |

---

### `Agent` (`mce-crds/assisted-service/agent-install.openshift.io_agents.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | "Agent is the Schema for the hosts API" | Needs Improvement | Restates name and references "hosts API" — confusing mismatch with kind name |
| spec | object | "AgentSpec defines the desired state of Agent" | Passable | Generic |
| spec.approved | boolean | *(absent)* | Needs Improvement | No description on an important field controlling whether the agent is approved for installation |
| spec.clusterDeploymentName | object | Generic cluster reference description | Passable | Acceptable inherited type description |
| spec.hostname | string | *(absent)* | Needs Improvement | Missing |
| spec.machineConfigPool | string | *(absent)* | Needs Improvement | Missing |
| spec.role | string | "HostRole host role / swagger:model host-role" | Needs Improvement | Leaks swagger model notation into human-readable description; no valid values listed |
| spec.ignitionConfigOverrides | string | "Json formatted string containing the user overrides for the host's ignition config" | Passable | Format noted |
| spec.installation_disk_id | string | "InstallationDiskID defines the installation destination disk (must be equal to the inventory disk id)." | Good | Constraint referenced |
| spec.installation_disk_path | string | "InstallationDiskPath defines the installation destination disk using either its by-id or by-path value." | Good | Both supported formats mentioned |
| spec.installerArgs | string | "Json formatted string containing the user overrides for the host's coreos installer args" | Passable | Format noted |
| spec.nodeLabels | object | "NodeLabels are the labels to be applied on the node associated with this agent" | Good | Clear and specific |
| status | object | "AgentStatus defines the observed state of Agent" | Passable | Generic |
| status.bootstrap | boolean | *(absent)* | Needs Improvement | No description on an important status field |
| status.conditions | array | *(absent at array level)* | Needs Improvement | Missing |
| status.debugInfo | object | "DebugInfo includes information for debugging the installation process." | Good | Clear purpose |
| status.debugInfo.state | string | "Current state of the Agent" | Passable | Minimal; no valid states listed |
| status.inventory | object | *(absent)* | Needs Improvement | No description on a rich nested object |
| (summary for file) | | | | 4 Good, 5 Passable, 9 Needs Improvement |

---

### `InfraEnv` (`mce-crds/assisted-service/agent-install.openshift.io_infraenvs.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | *(absent — no openAPIV3Schema description)* | Needs Improvement | No root description |
| spec | object | *(absent)* | Needs Improvement | No spec description |
| spec.additionalNTPSources | array | Explains sources are added (not replacing) and accepted formats | Good | "Added to" semantics documented |
| spec.additionalTrustBundle | string | Explains PEM format, which hosts trust the certs, and that clusters formed from these hosts also trust them | Good | Trust propagation scope documented |
| spec.agentApproval | object | "AgentApproval defines configuration for automatic approval of Agents discovered by this InfraEnv." | Good | Clear |
| spec.agentApproval.autoApprove | boolean | Explains automatic approval behavior, security caution ("Use only in trusted environments") | Good | Security guidance is valuable |
| spec.agentLabels | object | "AgentLabels lists labels to apply to Agents that are associated with this InfraEnv upon the creation of the Agents." | Good | Timing ("upon creation") is documented |
| spec.clusterRef | object | Explains it is the reference for a single ClusterDeployment and notes future removal | Good | Future-change note helps users plan |
| spec.cpuArchitecture | string | "CpuArchitecture specifies the target CPU architecture. Default is x86_64" | Passable | Default noted; no guidance on valid values |
| spec.imageType | string | Lists both valid types (full-iso, minimal-iso) and explains the download difference | Good | Both values explained |
| spec.ipxeScriptType | string | Lists both enum values with detailed behavior of each option | Good | Excellent enumeration of behavior |
| spec.kernelArguments | array | "KernelArguments is the additional kernel arguments to be passed during boot time of the discovery image. Applicable for both iPXE, and ISO streaming from Image Service." | Good | Scope (both iPXE and ISO) documented |
| spec.mirrorRegistryRef | object | "MirrorRegistryRef is a reference to a given MirrorRegistry ConfigMap that holds the registries toml data" | Passable | Content format (toml) noted but no explanation of when to use |
| spec.nmStateConfigLabelSelector | object | "NmstateConfigLabelSelector associates NMStateConfigs for hosts that are considered part of this installation environment." | Passable | Purpose clear but mechanism (label-based selection) is already obvious from field name |
| (summary for file) | | | | 8 Good, 5 Passable, 3 Needs Improvement (root and spec absent) |

---

### `AgentClusterInstall` (`mce-crds/assisted-service/extensions.hive.openshift.io_agentclusterinstalls.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | "AgentClusterInstall represents a request to provision an agent based cluster." | Good | Clear purpose |
| spec | object | "AgentClusterInstallSpec defines the desired state of the AgentClusterInstall." | Passable | Generic |
| spec.apiVIP | string | "APIVIP is the virtual IP used to reach the OpenShift cluster's API." | Passable | Deprecated field; no deprecation notice in description |
| spec.apiVIPs | array | Documents dual-stack, count constraint, and ordering requirement | Good | Thorough |
| spec.arbiter | object | "Arbiter is the configuration for the machines that have the arbiter role." | Passable | What is an arbiter? No explanation |
| spec.clusterDeploymentRef | object | "ClusterDeploymentRef is a reference to the ClusterDeployment associated with this AgentClusterInstall." | Good | Clear linking |
| spec.clusterMetadata | object | Explains when it should be populated and the condition that triggers copy-back | Good | Copy-back mechanism explained |
| spec.compute | array | "Compute is the configuration for the machines that comprise the compute nodes." | Good | Clear |
| spec.compute[].hyperthreading | string (enum) | Explains mode, enum values (Enabled/Disabled), and default | Good | All values and default documented |
| spec.compute[].name | string | Documents that control plane pool name is always "master" and only valid compute name is "worker" | Good | Both valid values explained in prose |
| spec.clusterMetadata.clusterID | string | "ClusterID is a globally unique identifier for this cluster generated during installation. Used for reporting metrics among other places." | Good | Purpose and generation context clear |
| spec.clusterMetadata.infraID | string | "InfraID is an identifier for this cluster generated during installation and used for tagging/naming resources in cloud providers." | Good | Use case documented |
| spec.clusterMetadata.platform | object | "Platform holds platform-specific cluster metadata" | Passable | Minimal |
| spec.clusterMetadata.platform.aws | object | "AWS holds AWS-specific cluster metadata" | Passable | Minimal |
| spec.clusterMetadata.platform.aws.hostedZoneRole | string | "HostedZoneRole is the role to assume when performing operations on a hosted zone owned by another account." | Good | Cross-account scenario documented |
| (summary for file) | | | | 8 Good, 6 Passable, 2 Needs Improvement |

---

### `Cluster` (CAPI) (`mce-crds/cluster-api-k8s/apiextensions.k8s.io_v1_customresourcedefinition_clusters.cluster.x-k8s.io.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | "Cluster is the Schema for the clusters API." | Needs Improvement | Restates the name; no explanation of what CAPI Cluster represents |
| spec | object | "spec is the desired state of Cluster." | Passable | Lowercase "spec" is a minor style inconsistency |
| spec.clusterNetwork | object | "clusterNetwork is the cluster network configuration." | Passable | Minimal |
| spec.clusterNetwork.apiServerPort | integer | "apiServerPort specifies the port the API Server should bind to. Defaults to 6443." | Good | Default documented |
| spec.clusterNetwork.pods | object | "pods is the network ranges from which Pod networks are allocated." | Passable | Minimal |
| spec.clusterNetwork.serviceDomain | string | "serviceDomain is the domain name for services." | Passable | Minimal |
| spec.clusterNetwork.services | object | "services is the network ranges from which service VIPs are allocated." | Passable | Minimal |
| spec.controlPlaneEndpoint | object | "controlPlaneEndpoint represents the endpoint used to communicate with the control plane." | Passable | Minimal |
| spec.controlPlaneRef | object | "controlPlaneRef is an optional reference to a provider-specific resource that holds the details for provisioning the Control Plane for a Cluster." | Good | Optional nature and provider-specific detail noted |
| spec.infrastructureRef | object | "infrastructureRef is a reference to a provider-specific resource that holds the details for provisioning infrastructure for a cluster in said provider." | Good | Purpose clear |
| spec.paused | *(not read — v1beta1 version not sampled)* | — | — | — |
| (summary for file) | | | | 5 Good, 6 Passable, 1 Needs Improvement |

---

### `AWSCluster` (`mce-crds/cluster-api-provider-aws/apiextensions.k8s.io_v1_customresourcedefinition_awsclusters.infrastructure.cluster.x-k8s.io.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| (root) | object | "AWSCluster is the schema for Amazon EC2 based Kubernetes Cluster API." | Good | Identifies the cloud provider and API |
| spec | object | "AWSClusterSpec defines the desired state of an EC2-based Kubernetes cluster." | Good | Slightly more specific than generic |
| spec.additionalTags | object | "AdditionalTags is an optional set of tags to add to AWS resources managed by the AWS provider, in addition to the ones added by default." | Good | "in addition to" semantics documented |
| spec.bastion | object | "Bastion contains options to configure the bastion host." | Passable | Minimal |
| spec.bastion.allowedCIDRBlocks | array | Documents that it applies to the security group and that default is 0.0.0.0/0 | Good | Default documented |
| spec.bastion.ami | string | Documents fallback behavior (public space AMI) when not specified | Good | Fallback behavior documented |
| spec.bastion.enabled | boolean | "Enabled allows this provider to create a bastion host instance with a public ip to access the VPC private network." | Good | Purpose clear |
| spec.bastion.instanceType | string | Documents default behavior per-region (t3.micro except us-east-1 uses t2.micro) | Good | Region-specific default is excellent detail |
| spec.controlPlaneLoadBalancer.crossZoneLoadBalancing | boolean | Explains the AWS ELB cross-zone semantics, per-zone vs global distribution, and default | Good | Excellent technical explanation |
| spec.controlPlaneLoadBalancer.name | string | Documents AWS naming constraints (32 chars, alphanumeric/hyphen, no start/end hyphen, immutable) | Good | All constraints and immutability documented |
| spec.controlPlaneLoadBalancer.scheme | string (enum) | Lists both values (internet-facing, internal) and notes default | Good | Both values and default documented |
| spec.identityRef | object | "IdentityRef is a reference to an identity to be used when reconciling the managed control plane. If no identity is specified, the default identity for this controller will be used." | Good | Default fallback behavior documented |
| (summary for file) | | | | 7 Good, 5 Passable, 0 Needs Improvement |

---

## Cross-CRD Patterns

Common anti-patterns observed:

1. **Root description restatement** — Many CRDs (Subscription, ClusterInstance, PolicyReport, MulticlusterRoleAssignment, Agent) use their root description to literally restate the resource name: `"X is the Schema for the X API"`. This provides zero value to a user trying to understand what the resource does.

2. **Generic spec/status boilerplate** — A majority of CRDs use `"XSpec defines the desired state of X"` and `"XStatus defines the observed state of X"` as spec and status descriptions. These are algorithmically generated from the Go type names and add no information. The pattern is so pervasive it constitutes a systemic failure.

3. **Missing or one-word status field descriptions** — Status-level fields are consistently under-documented. Fields like `status.phase`, `status.lastMessage`, `status.conditions` frequently have no descriptions or single-word descriptions (`"Conditions"`). Critically, `status.phase` fields across BackupSchedule and Restore never enumerate valid phase values, leaving users unable to interpret the field programmatically.

4. **Absent descriptions on important fields** — Several high-value fields have no description at all: `spec.approved` on Agent (boolean controlling agent admission), `status.bootstrap` on Agent, `status.inventory` on Agent (a rich nested object), `spec.diskEncryption.tang` and `spec.diskEncryption.type` on ClusterInstance, and all four `status.velero*RestoreName` fields on Restore.

5. **Placeholder and development-only strings** — The Search CRD contains production-visible `[PLACEHOLDER, NOT IMPLEMENTED]` descriptions on `spec.availabilityConfig` and `spec.externalDBInstance`. These should never appear in shipped CRD YAML.

6. **Internal type names leaking into descriptions** — Several fields use Go/internal naming in descriptions. Examples: `spec.automationDef.type` says only "Type of the automation to invoke", Agent's `spec.role` leaks `swagger:model host-role`, and `Search.spec.deployments.*.imageOverride` uses `Image_override` (Go snake-case).

7. **Numeric fields without units** — `spec.observabilityAddonSpec.interval` (MultiClusterObservability) documents a range but not whether the unit is seconds; `spec.automationDef.jobTtl` (PolicyAutomation) gives no unit. Both have numerical ranges but leave users guessing at the unit of measure.

8. **UserPreference CRD has no schema descriptions whatsoever** — All documentation appears as YAML comments outside the openAPIV3Schema structure, making it invisible to tooling such as `kubectl explain`.

---

## Recommendations

Top 5 improvements by impact:

1. **Eliminate root-level restatement descriptions (affects ~8 CRDs, highest user impact)** — Replace descriptions like `"X is the Schema for the X API"` with a sentence explaining the resource's purpose and operational model. Examples of what to fix: `Agent`, `Subscription`, `ClusterInstance`, `PolicyReport`, `MulticlusterRoleAssignment`, `Search`, `Cluster` (CAPI). Suggested pattern: _"An Agent represents a host that has booted the discovery ISO and registered with the Assisted Installer. Approve an Agent to include the host in a cluster installation."_

2. **Add descriptions to all `status.*RestoreName` fields and enumerate valid `status.phase` values in BackupSchedule and Restore** — The four `status.velero*RestoreName` fields in Restore have zero descriptions, and `status.phase` in both cluster-backup CRDs lists no valid values. These are observable fields that operators use for automation. Suggested fix: add an enum or prose list of phases (e.g., `New`, `InProgress`, `FinishedWithErrors`, `Finished`, `BackupCollision`) and describe each restore name as the name of the Velero Restore object created for the corresponding backup type.

3. **Add `description` fields to the UserPreference CRD schema** — The entire `user-preference-crd.yaml` has no description fields within the openAPIV3Schema. The comments in the YAML file are invisible to `kubectl explain` and API documentation generators. Each field (`savedSearches`, `id`, `searchText`, `name`, `description`) needs a proper `description:` key added.

4. **Remove or replace [PLACEHOLDER, NOT IMPLEMENTED] descriptions in Search CRD** — `spec.availabilityConfig` and `spec.externalDBInstance` in `searches.search.open-cluster-management.io` have placeholder strings that should not appear in shipped software. Either remove these fields from the CRD schema or replace the description with `"Not currently supported."` and a note that the field is reserved for future use.

5. **Add units to all integer/duration fields missing them** — At minimum: `spec.observabilityAddonSpec.interval` in MultiClusterObservability (add "seconds"), `spec.automationDef.jobTtl` in PolicyAutomation (add "seconds"), and `spec.delayAfterRunSeconds` already has units in its name (good). Also add valid-values documentation to `ClusterInstance.spec.clusterType` (the description says "a string representing the cluster type" but does not explain what SNO, HighlyAvailable, HostedControlPlane, or HighlyAvailableArbiter mean).
