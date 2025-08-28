# Policy API

Policy is the schema for the policies API. Policy wraps other policy engine resources in its "policy-templates" array in order to deliver the resources to managed clusters.

## Spec Fields

PolicySpec defines the configurations of the policy engine resources to deliver to the managed clusters.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **copyPolicyMetadata** | `boolean` | CopyPolicyMetadata specifies whether the labels and annotations of a policy should be copied when replicating the policy to a managed cluster. If set to "true", all of the labels and annotations of the policy are copied to the replicated policy. If set to "false", only the policy framework-specific policy labels and annotations are copied to the replicated policy. This setting is useful if there is tracking for metadata that should only exist on the root policy. It is recommended to set this to "false" when using Argo CD to deploy the policy definition since Argo CD uses metadata for tracking that should not be replicated. The default value is "true". | N/A |
|  **dependencies** | `array` | PolicyDependencies is a list of dependency objects detailed with extra considerations for compliance that should be fulfilled before applying the policies to the managed clusters. | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | N/A |
| └>&nbsp;&nbsp; **compliance** | `string` | Compliance is the required ComplianceState of the object that the policy depends on, at the following path, .status.compliant. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the object that the policy depends on. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace is the namespace of the object that the policy depends on (optional). | N/A |
|  **disabled** | `boolean` | Disabled is a boolean parameter you can use to enable and disable the policy. When disabled, the policy is removed from managed clusters. | N/A |
|  **hubTemplateOptions** | `object` | HubTemplateOptions changes the default behavior of hub templates. | N/A |
| └>&nbsp;&nbsp; **serviceAccountName** | `string` | ServiceAccountName is the name of a service account in the same namespace as the policy to use for all hub template lookups. The service account must have list and watch permissions on any object the hub templates look up. If not specified, lookups are restricted to namespaced objects in the same namespace as the policy and to the `ManagedCluster` object associated with the propagated policy. | N/A |
|  **policy-templates** | `array` | PolicyTemplates is a list of definitions of policy engine resources to apply to managed clusters along with configurations on how it should be applied. | N/A |
| └>&nbsp;&nbsp; **extraDependencies** | `array` | ExtraDependencies is additional PolicyDependencies that only apply to this policy template. ExtraDependencies is a list of dependency objects detailed with extra considerations for compliance that should be fulfilled before applying the policy template to the managed clusters. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiVersion** | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **compliance** | `string` | Compliance is the required ComplianceState of the object that the policy depends on, at the following path, .status.compliant. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the object that the policy depends on. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace is the namespace of the object that the policy depends on (optional). | N/A |
| └>&nbsp;&nbsp; **ignorePending** | `boolean` | IgnorePending is a boolean parameter to specify whether to ignore the "Pending" status of this template when calculating the overall policy status. The default value is "false" to not ignore a "Pending" status. | N/A |
| └>&nbsp;&nbsp; **objectDefinition** | `object` | A Kubernetes object defining the policy to apply to a managed cluster | N/A |
|  **remediationAction** | `string` | RemediationAction specifies the remediation of the policy. The parameter values are "enforce" and "inform". If specified, the value that is defined overrides any remediationAction parameter defined in the child policies in the "policy-templates" section. Important: Not all policy engine kinds support the enforce feature. | N/A |
## Status Fields

PolicyStatus reports the observed status of the policy resulting from its policy templates.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **compliant** | `string` | ComplianceState reports the observed status resulting from the definitions of this policy. This status field is only used in the replicated policy in the managed cluster namespace. | N/A |
|  **details** | `array` | Details is the list of compliance details for each policy template definition. This status field is only used in the replicated policy in the managed cluster namespace. | N/A |
| └>&nbsp;&nbsp; **compliant** | `string` | ComplianceState reports the observed status resulting from the definitions of the policy. | N/A |
| └>&nbsp;&nbsp; **history** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **eventName** | `string` | EventName is the name of the event attached to the message. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **lastTimestamp** | `string` | LastTimestamp is the timestamp of the event that reported the message. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **message** | `string` | Message is the compliance message resulting from evaluating the policy resource. | N/A |
| └>&nbsp;&nbsp; **templateMeta** | `object` | No description provided. | N/A |
|  **placement** | `array` | Placement is a list of managed cluster placement resources bound to the policy. This status field is only used in the root policy on the hub cluster. | N/A |
| └>&nbsp;&nbsp; **decisions** | `array` | Decisions is the list of managed clusters returned by the placement resource for this binding. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **clusterName** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **clusterNamespace** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **placement** | `string` | Placement is the name of the Placement resource, from the cluster.open-cluster-management.io API group, that is bound to the policy. | N/A |
| └>&nbsp;&nbsp; **placementBinding** | `string` | PlacementBinding is the name of the PlacementBinding resource, from the policies.open-cluster-management.io API group, that binds the placement resource to the policy. | N/A |
| └>&nbsp;&nbsp; **placementRule** | `string` | PlacementRule (deprecated) is the name of the PlacementRule resource, from the apps.open-cluster-management.io API group, that is bound to the policy. | N/A |
| └>&nbsp;&nbsp; **policySet** | `string` | PolicySet is the name of the policy set containing this policy and bound to the placement. If specified, then for this placement the policy is being propagated through this policy set rather than the policy being bound directly to a placement and propagated individually. | N/A |
|  **status** | `array` | Status is a list of managed clusters and the current compliance state of each one. This status field is only used in the root policy on the hub cluster. | N/A |
| └>&nbsp;&nbsp; **clustername** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **clusternamespace** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **compliant** | `string` | ComplianceState reports the observed status resulting from the definitions of the policy. | N/A |
