# Advanced Cluster Management Custom Resource API Documentation

This document provides an overview of the Custom Resource Definitions (CRDs) used in this project.

## ManagedClusterView

ManagedClusterView is the view of resources on a managed cluster

[View a detailed API Reference for ManagedClusterView](managedclusterview_api.md).

---

## KlusterletConfig

KlusterletConfig contains the configuration of a klusterlet including the upgrade strategy, config overrides, proxy configurations etc.

[View a detailed API Reference for KlusterletConfig](klusterletconfig_api.md).

---

## ManagedClusterAction

ManagedClusterAction is the action that will be done on a cluster

[View a detailed API Reference for ManagedClusterAction](managedclusteraction_api.md).

---

## ManagedClusterImageRegistry

ManagedClusterImageRegistry represents the image overridden configuration information.

[View a detailed API Reference for ManagedClusterImageRegistry](managedclusterimageregistry_api.md).

---

## ManagedClusterInfo

ManagedClusterInfo represents the information of managed cluster that acm hub needs to know

[View a detailed API Reference for ManagedClusterInfo](managedclusterinfo_api.md).

---

## ManagedServiceAccount

ManagedServiceAccount is the Schema for the managedserviceaccounts API

[View a detailed API Reference for ManagedServiceAccount](managedserviceaccount_api.md).

---

## ClusterCurator

ClusterCurator is the custom resource for the clustercurators API. This kind allows you to run Ansible prehook and posthook jobs before provisioning Hive or HyperShift and importing a cluster. Additionally, cluster upgrade and destroy operations are supported as well.

[View a detailed API Reference for ClusterCurator](clustercurator_api.md).

---

## ClusterManager

ClusterManager configures the controllers on the hub that govern registration and work distribution for attached Klusterlets.
In Default mode, ClusterManager will only be deployed in open-cluster-management-hub namespace.
In Hosted mode, ClusterManager will be deployed in the namespace with the same name as cluster manager.

[View a detailed API Reference for ClusterManager](clustermanager_api.md).

---

## AddOnTemplate

AddOnTemplate is the Custom Resource object, it is used to describe
how to deploy the addon agent and how to register the addon.
AddOnTemplate is a cluster-scoped resource, and will only be used
on the hub cluster.

[View a detailed API Reference for AddOnTemplate](addontemplate_api.md).

---

## Placement

Placement defines a rule to select a set of ManagedClusters from the ManagedClusterSets bound
to the placement namespace.
Here is how the placement policy combines with other selection methods to determine a matching
list of ManagedClusters:
 1. Kubernetes clusters are registered with hub as cluster-scoped ManagedClusters;
 2. ManagedClusters are organized into cluster-scoped ManagedClusterSets;
 3. ManagedClusterSets are bound to workload namespaces;
 4. Namespace-scoped Placements specify a slice of ManagedClusterSets which select a working set
    of potential ManagedClusters;
 5. Then Placements subselect from that working set using label/claim selection.
A ManagedCluster will not be selected if no ManagedClusterSet is bound to the placement
namespace. A user is able to bind a ManagedClusterSet to a namespace by creating a
ManagedClusterSetBinding in that namespace if they have an RBAC rule to CREATE on the virtual
subresource of `managedclustersets/bind`.
A slice of PlacementDecisions with the label cluster.open-cluster-management.io/placement={placement name}
will be created to represent the ManagedClusters selected by this placement.
If a ManagedCluster is selected and added into the PlacementDecisions, other components may
apply workload on it; once it is removed from the PlacementDecisions, the workload applied on
this ManagedCluster should be evicted accordingly.

[View a detailed API Reference for Placement](placement_api.md).

---

## ManagedClusterAddOn

ManagedClusterAddOn is the Custom Resource object which holds the current state
of an add-on. This object is used by add-on operators to convey their state.
This resource should be created in the ManagedCluster namespace.

[View a detailed API Reference for ManagedClusterAddOn](managedclusteraddon_api.md).

---

## AddOnDeploymentConfig

AddOnDeploymentConfig represents a configuration to customize the deployments of an add-on.
For example, you can specify the NodePlacement to control the scheduling of the add-on agents.

[View a detailed API Reference for AddOnDeploymentConfig](addondeploymentconfig_api.md).

---

## AddOnPlacementScore

AddOnPlacementScore represents a bundle of scores of one managed cluster, which could be used by placement.
AddOnPlacementScore is a namespace scoped resource. The namespace of the resource is the cluster namespace.

[View a detailed API Reference for AddOnPlacementScore](addonplacementscore_api.md).

---

## PlacementDecision

PlacementDecision indicates a decision from a placement.
PlacementDecision must have a cluster.open-cluster-management.io/placement={placement name} label to reference a certain placement.
If a placement has spec.numberOfClusters specified, the total number of decisions contained in
the status.decisions of PlacementDecisions must be the same as NumberOfClusters. Otherwise, the
total number of decisions must equal the number of ManagedClusters that
match the placement requirements.
Some of the decisions might be empty when there are not enough ManagedClusters to meet the placement requirements.

[View a detailed API Reference for PlacementDecision](placementdecision_api.md).

---

## ManifestWork

ManifestWork represents a manifests workload that hub wants to deploy on the managed cluster.
A manifest workload is defined as a set of Kubernetes resources.
ManifestWork must be created in the cluster namespace on the hub, so that agent on the
corresponding managed cluster can access this resource and deploy on the managed
cluster.

[View a detailed API Reference for ManifestWork](manifestwork_api.md).

---

## ManagedClusterSet

ManagedClusterSet defines a group of ManagedClusters that you can run
workloads on. You can define a workload to be deployed on a ManagedClusterSet. See the following options  for the workload:
- The workload can run on any ManagedCluster in the ManagedClusterSet
- The workload cannot run on any ManagedCluster outside the ManagedClusterSet
- The service exposed by the workload can be shared in any ManagedCluster in the ManagedClusterSet
To assign a ManagedCluster to a certain ManagedClusterSet, add a label with the name cluster.open-cluster-management.io/clusterset
on the ManagedCluster to refer to the ManagedClusterSet. You are not
allowed to add or remove this label on a ManagedCluster unless you have an
RBAC rule to CREATE on a virtual subresource of managedclustersets/join.
To update this label, you must have the permission on both
the old and new ManagedClusterSet.

[View a detailed API Reference for ManagedClusterSet](managedclusterset_api.md).

---

## ManagedClusterSetBinding

ManagedClusterSetBinding projects a ManagedClusterSet into a certain namespace.
You can create a ManagedClusterSetBinding in a namespace and bind it to a
ManagedClusterSet if both have a RBAC rules to CREATE on the virtual subresource of managedclustersets/bind.
Workloads that you create in the same namespace can only be distributed to ManagedClusters
in ManagedClusterSets that are bound in this namespace by higher-level controllers.

[View a detailed API Reference for ManagedClusterSetBinding](managedclustersetbinding_api.md).

---

## ManagedCluster

ManagedCluster represents the desired state and current status
of a managed cluster. ManagedCluster is a cluster-scoped resource. The name
is the cluster UID.
The cluster join process is a double opt-in process. See the following join process steps:
1. The agent on the managed cluster creates a CSR on the hub with the cluster UID and agent name.
2. The agent on the managed cluster creates a ManagedCluster on the hub.
3. The cluster admin on the hub cluster approves the CSR for the UID and agent name of the ManagedCluster.
4. The cluster admin sets the spec.acceptClient of the ManagedCluster to true.
5. The cluster admin on the managed cluster creates a credential of the kubeconfig for the hub cluster.
After the hub cluster creates the cluster namespace, the klusterlet agent on the ManagedCluster pushes
the credential to the hub cluster to use against the kube-apiserver of the ManagedCluster.

[View a detailed API Reference for ManagedCluster](managedcluster_api.md).

---

## ManifestWorkReplicaSet

ManifestWorkReplicaSet is the Schema for the ManifestWorkReplicaSet API. This custom resource is able to apply
ManifestWork using Placement for 0..n ManagedCluster(in their namespaces). It will also remove the ManifestWork custom resources
when deleted. Lastly the specific ManifestWork custom resources created per ManagedCluster namespace will be adjusted based on PlacementDecision
changes.

[View a detailed API Reference for ManifestWorkReplicaSet](manifestworkreplicaset_api.md).

---

## ClusterManagementAddOn

ClusterManagementAddOn represents the registration of an add-on to the cluster manager.
This resource allows you to discover which add-ons are available for the cluster manager
and provides metadata information about the add-ons. The ClusterManagementAddOn name is used
for the namespace-scoped ManagedClusterAddOn resource.
ClusterManagementAddOn is a cluster-scoped resource.

[View a detailed API Reference for ClusterManagementAddOn](clustermanagementaddon_api.md).

---

## ClusterProfile

ClusterProfile represents a single cluster in a multi-cluster deployment.

[View a detailed API Reference for ClusterProfile](clusterprofile_api.md).

---

## MachineSet

MachineSet is the Schema for the machinesets API.
Deprecated: This type will be removed in one of the next releases.

[View a detailed API Reference for MachineSet](machineset_api.md).

---

## ClusterResourceSetBinding

ClusterResourceSetBinding lists all matching ClusterResourceSets with the cluster it belongs to.
Deprecated: This type will be removed in one of the next releases.

[View a detailed API Reference for ClusterResourceSetBinding](clusterresourcesetbinding_api.md).

---

## Cluster

Cluster is the Schema for the clusters API.

[View a detailed API Reference for Cluster](cluster_api.md).

---

## ClusterClass

ClusterClass is a template which can be used to create managed topologies.
Deprecated: This type will be removed in one of the next releases.

[View a detailed API Reference for ClusterClass](clusterclass_api.md).

---

## MachineDrainRule

MachineDrainRule is the Schema for the MachineDrainRule API.

[View a detailed API Reference for MachineDrainRule](machinedrainrule_api.md).

---

## MachineHealthCheck

MachineHealthCheck is the Schema for the machinehealthchecks API.
Deprecated: This type will be removed in one of the next releases.

[View a detailed API Reference for MachineHealthCheck](machinehealthcheck_api.md).

---

## MachineDeployment

MachineDeployment is the Schema for the machinedeployments API.
Deprecated: This type will be removed in one of the next releases.

[View a detailed API Reference for MachineDeployment](machinedeployment_api.md).

---

## Machine

Machine is the Schema for the machines API.
Deprecated: This type will be removed in one of the next releases.

[View a detailed API Reference for Machine](machine_api.md).

---

## ExtensionConfig

ExtensionConfig is the Schema for the ExtensionConfig API.

[View a detailed API Reference for ExtensionConfig](extensionconfig_api.md).

---

## ClusterResourceSet

ClusterResourceSet is the Schema for the clusterresourcesets API.
Deprecated: This type will be removed in one of the next releases.

[View a detailed API Reference for ClusterResourceSet](clusterresourceset_api.md).

---

## InternalEngineComponent

Description not found in CRD.

[View a detailed API Reference for InternalEngineComponent](internalenginecomponent_api.md).

---

## ImageClusterInstall

ImageClusterInstall is the Schema for the imageclusterinstall API

[View a detailed API Reference for ImageClusterInstall](imageclusterinstall_api.md).

---

## EKSConfig

EKSConfig is the schema for the Amazon EKS Machine Bootstrap Configuration API.

[View a detailed API Reference for EKSConfig](eksconfig_api.md).

---

## AWSFargateProfile

AWSFargateProfile is the Schema for the awsfargateprofiles API.

[View a detailed API Reference for AWSFargateProfile](awsfargateprofile_api.md).

---

## AWSMachineTemplate

AWSMachineTemplate is the schema for the Amazon EC2 Machine Templates API.

[View a detailed API Reference for AWSMachineTemplate](awsmachinetemplate_api.md).

---

## AWSClusterTemplate

AWSClusterTemplate is the schema for Amazon EC2 based Kubernetes Cluster Templates.

[View a detailed API Reference for AWSClusterTemplate](awsclustertemplate_api.md).

---

## ROSAControlPlane

ROSAControlPlane is the Schema for the ROSAControlPlanes API.

[View a detailed API Reference for ROSAControlPlane](rosacontrolplane_api.md).

---

## AWSMachinePool

AWSMachinePool is the Schema for the awsmachinepools API.

[View a detailed API Reference for AWSMachinePool](awsmachinepool_api.md).

---

## AWSClusterControllerIdentity

AWSClusterControllerIdentity is the Schema for the awsclustercontrolleridentities API
It is used to grant access to use Cluster API Provider AWS Controller credentials.

[View a detailed API Reference for AWSClusterControllerIdentity](awsclustercontrolleridentity_api.md).

---

## AWSCluster

AWSCluster is the schema for Amazon EC2 based Kubernetes Cluster API.

[View a detailed API Reference for AWSCluster](awscluster_api.md).

---

## AWSManagedCluster

AWSManagedCluster is the Schema for the awsmanagedclusters API

[View a detailed API Reference for AWSManagedCluster](awsmanagedcluster_api.md).

---

## AWSClusterStaticIdentity

AWSClusterStaticIdentity is the Schema for the awsclusterstaticidentities API
It represents a reference to an AWS access key ID and secret access key, stored in a secret.

[View a detailed API Reference for AWSClusterStaticIdentity](awsclusterstaticidentity_api.md).

---

## AWSMachine

AWSMachine is the schema for Amazon EC2 machines.

[View a detailed API Reference for AWSMachine](awsmachine_api.md).

---

## AWSManagedControlPlane

AWSManagedControlPlane is the schema for the Amazon EKS Managed Control Plane API.

[View a detailed API Reference for AWSManagedControlPlane](awsmanagedcontrolplane_api.md).

---

## ROSAMachinePool

ROSAMachinePool is the Schema for the rosamachinepools API.

[View a detailed API Reference for ROSAMachinePool](rosamachinepool_api.md).

---

## AWSClusterRoleIdentity

AWSClusterRoleIdentity is the Schema for the awsclusterroleidentities API
It is used to assume a role using the provided sourceRef.

[View a detailed API Reference for AWSClusterRoleIdentity](awsclusterroleidentity_api.md).

---

## AWSManagedMachinePool

AWSManagedMachinePool is the Schema for the awsmanagedmachinepools API.

[View a detailed API Reference for AWSManagedMachinePool](awsmanagedmachinepool_api.md).

---

## EKSConfigTemplate

EKSConfigTemplate is the Amazon EKS Bootstrap Configuration Template API.

[View a detailed API Reference for EKSConfigTemplate](eksconfigtemplate_api.md).

---

## ROSACluster

ROSACluster is the Schema for the ROSAClusters API.

[View a detailed API Reference for ROSACluster](rosacluster_api.md).

---

## AgentClassification

AgentClassification is the Schema for the AgentClassifications API

[View a detailed API Reference for AgentClassification](agentclassification_api.md).

---

## InfraEnv

Description not found in CRD.

[View a detailed API Reference for InfraEnv](infraenv_api.md).

---

## Agent

Agent is the Schema for the hosts API

[View a detailed API Reference for Agent](agent_api.md).

---

## HypershiftAgentServiceConfig

HypershiftAgentServiceConfig represents an Assisted Service deployment over zero-worker
hypershift cluster. Each resource represents a deployment scheme over hosted cluster
that runs in that namespace.

[View a detailed API Reference for HypershiftAgentServiceConfig](hypershiftagentserviceconfig_api.md).

---

## NMStateConfig

Description not found in CRD.

[View a detailed API Reference for NMStateConfig](nmstateconfig_api.md).

---

## AgentClusterInstall

AgentClusterInstall represents a request to provision an agent based cluster.

[View a detailed API Reference for AgentClusterInstall](agentclusterinstall_api.md).

---

## AgentServiceConfig

AgentServiceConfig represents an Assisted Service deployment.
Only an AgentServiceConfig with name="agent" will be reconciled. All other
names will be rejected.

[View a detailed API Reference for AgentServiceConfig](agentserviceconfig_api.md).

---

## ManagedProxyServiceResolver

ManagedProxyServiceResolver defines a target service that need to expose from a set of managed clusters to the hub. To access a target service on a managed cluster from hub. First, users need to apply a proper ManagedProxyServiceResolver. The managed cluster should match the ManagedClusterSet in the ManagedProxyServiceResolver.Spec. The serviceNamespace and serviceName should also match the target service. A usage example: /examples/access-other-services/main.go

[View a detailed API Reference for ManagedProxyServiceResolver](managedproxyserviceresolver_api.md).

---

## ManagedProxyConfiguration

ManagedProxyConfiguration is the Schema for the managedproxyconfigurations API

[View a detailed API Reference for ManagedProxyConfiguration](managedproxyconfiguration_api.md).

---

## AppliedManifestWork

AppliedManifestWork represents an applied manifestwork on managed cluster that is placed
on a managed cluster. An AppliedManifestWork links to a manifestwork on a hub recording resources
deployed in the managed cluster.
When the agent is removed from managed cluster, cluster-admin on managed cluster
can delete appliedmanifestwork to remove resources deployed by the agent.
The name of the appliedmanifestwork must be in the format of
{hash of hub's first kube-apiserver url}-{manifestwork name}

[View a detailed API Reference for AppliedManifestWork](appliedmanifestwork_api.md).

---

## SelectorSyncIdentityProvider

SelectorSyncIdentityProvider is the Schema for the SelectorSyncSet API

[View a detailed API Reference for SelectorSyncIdentityProvider](selectorsyncidentityprovider_api.md).

---

## ClusterSyncLease

ClusterSyncLease is a record of the last time that SyncSets and SelectorSyncSets were applied to a cluster.

[View a detailed API Reference for ClusterSyncLease](clustersynclease_api.md).

---

## SyncSet

SyncSet is the Schema for the SyncSet API

[View a detailed API Reference for SyncSet](syncset_api.md).

---

## SelectorSyncSet

SelectorSyncSet is the Schema for the SelectorSyncSet API

[View a detailed API Reference for SelectorSyncSet](selectorsyncset_api.md).

---

## ClusterDeployment

ClusterDeployment is the Schema for the clusterdeployments API

[View a detailed API Reference for ClusterDeployment](clusterdeployment_api.md).

---

## ClusterState

ClusterState is the Schema for the clusterstates API

[View a detailed API Reference for ClusterState](clusterstate_api.md).

---

## SyncIdentityProvider

SyncIdentityProvider is the Schema for the SyncIdentityProvider API

[View a detailed API Reference for SyncIdentityProvider](syncidentityprovider_api.md).

---

## ClusterImageSet

ClusterImageSet is the Schema for the clusterimagesets API

[View a detailed API Reference for ClusterImageSet](clusterimageset_api.md).

---

## ClusterClaim

ClusterClaim represents a claim to a cluster from a cluster pool.

[View a detailed API Reference for ClusterClaim](clusterclaim_api.md).

---

## ClusterPool

ClusterPool represents a pool of clusters that should be kept ready to be given out to users. Clusters are removed
from the pool once claimed and then automatically replaced with a new one.

[View a detailed API Reference for ClusterPool](clusterpool_api.md).

---

## DNSZone

DNSZone is the Schema for the dnszones API

[View a detailed API Reference for DNSZone](dnszone_api.md).

---

## FakeClusterInstall

FakeClusterInstall represents a fake request to provision an agent based cluster.

[View a detailed API Reference for FakeClusterInstall](fakeclusterinstall_api.md).

---

## HiveConfig

HiveConfig is the Schema for the hives API

[View a detailed API Reference for HiveConfig](hiveconfig_api.md).

---

## ClusterDeprovision

ClusterDeprovision is the Schema for the clusterdeprovisions API

[View a detailed API Reference for ClusterDeprovision](clusterdeprovision_api.md).

---

## ClusterRelocate

ClusterRelocate is the Schema for the ClusterRelocates API

[View a detailed API Reference for ClusterRelocate](clusterrelocate_api.md).

---

## ClusterProvision

ClusterProvision is the Schema for the clusterprovisions API

[View a detailed API Reference for ClusterProvision](clusterprovision_api.md).

---

## ClusterSync

ClusterSync is the status of all of the SelectorSyncSets and SyncSets that apply to a ClusterDeployment.

[View a detailed API Reference for ClusterSync](clustersync_api.md).

---

## Checkpoint

Checkpoint is the Schema for the backup of Hive objects.

[View a detailed API Reference for Checkpoint](checkpoint_api.md).

---

## ClusterDeploymentCustomization

ClusterDeploymentCustomization is the Schema for clusterdeploymentcustomizations API.

[View a detailed API Reference for ClusterDeploymentCustomization](clusterdeploymentcustomization_api.md).

---

## MachinePool

MachinePool is the Schema for the machinepools API

[View a detailed API Reference for MachinePool](machinepool_api.md).

---

## MachinePoolNameLease

MachinePoolNameLease is the Schema for the MachinePoolNameLeases API. This resource is mostly empty
as we're primarily relying on the name to determine if a lease is available.
Note that not all cloud providers require the use of a lease for naming, at present this
is only required for GCP where we're extremely restricted on name lengths.

[View a detailed API Reference for MachinePoolNameLease](machinepoolnamelease_api.md).

---

## OpenshiftAssistedConfigTemplate

OpenshiftAssistedConfigTemplate is the Schema for the openshiftassistedconfigtemplates API

[View a detailed API Reference for OpenshiftAssistedConfigTemplate](openshiftassistedconfigtemplate_api.md).

---

## OpenshiftAssistedControlPlane

OpenshiftAssistedControlPlane is the Schema for the openshiftassistedcontrolplane API

[View a detailed API Reference for OpenshiftAssistedControlPlane](openshiftassistedcontrolplane_api.md).

---

## OpenshiftAssistedConfig

OpenshiftAssistedConfig is the Schema for the openshiftassistedconfig API

[View a detailed API Reference for OpenshiftAssistedConfig](openshiftassistedconfig_api.md).

---

## Metal3ClusterTemplate

Metal3ClusterTemplate is the Schema for the metal3clustertemplates API.

[View a detailed API Reference for Metal3ClusterTemplate](metal3clustertemplate_api.md).

---

## Metal3Cluster

Metal3Cluster is the Schema for the metal3clusters API.

[View a detailed API Reference for Metal3Cluster](metal3cluster_api.md).

---

## Metal3RemediationTemplate

Metal3RemediationTemplate is the Schema for the metal3remediationtemplates API.

[View a detailed API Reference for Metal3RemediationTemplate](metal3remediationtemplate_api.md).

---

## Metal3MachineTemplate

Metal3MachineTemplate is the Schema for the metal3machinetemplates API.

[View a detailed API Reference for Metal3MachineTemplate](metal3machinetemplate_api.md).

---

## IPClaim

IPClaim is the Schema for the ipclaims API.

[View a detailed API Reference for IPClaim](ipclaim_api.md).

---

## Metal3DataTemplate

Metal3DataTemplate is the Schema for the metal3datatemplates API.

[View a detailed API Reference for Metal3DataTemplate](metal3datatemplate_api.md).

---

## Metal3DataClaim

Metal3DataClaim is the Schema for the metal3datas API.

[View a detailed API Reference for Metal3DataClaim](metal3dataclaim_api.md).

---

## IPPool

IPPool is the Schema for the ippools API.

[View a detailed API Reference for IPPool](ippool_api.md).

---

## Metal3Data

Metal3Data is the Schema for the metal3datas API.

[View a detailed API Reference for Metal3Data](metal3data_api.md).

---

## IPAddress

IPAddress is the Schema for the ipaddresses API.

[View a detailed API Reference for IPAddress](ipaddress_api.md).

---

## Metal3Machine

Metal3Machine is the Schema for the metal3machines API.

[View a detailed API Reference for Metal3Machine](metal3machine_api.md).

---

## Metal3Remediation

Metal3Remediation is the Schema for the metal3remediations API.

[View a detailed API Reference for Metal3Remediation](metal3remediation_api.md).

---

## DiscoveryConfig

DiscoveryConfig is the Schema for the discoveryconfigs API

[View a detailed API Reference for DiscoveryConfig](discoveryconfig_api.md).

---

## DiscoveredCluster

DiscoveredCluster is the Schema for the discoveredclusters API

[View a detailed API Reference for DiscoveredCluster](discoveredcluster_api.md).

---

## ClusterPermission

ClusterPermission is the Schema for the clusterpermissions API

[View a detailed API Reference for ClusterPermission](clusterpermission_api.md).

---

## Search

Search is the schema for the searches API.

[View a detailed API Reference for Search](search_api.md).

---

## ClusterInstance

ClusterInstance is the Schema for the clusterinstances API

[View a detailed API Reference for ClusterInstance](clusterinstance_api.md).

---

## KlusterletAddonConfig

KlusterletAddonConfig is the Schema for the klusterletaddonconfigs API

[View a detailed API Reference for KlusterletAddonConfig](klusterletaddonconfig_api.md).

---

## PlacementBinding

PlacementBinding is the schema for the placementbindings API. A PlacementBinding resource binds a managed cluster placement resource to a policy or policy set, along with configurable overrides.

[View a detailed API Reference for PlacementBinding](placementbinding_api.md).

---

## Policy

Policy is the schema for the policies API. Policy wraps other policy engine resources in its "policy-templates" array in order to deliver the resources to managed clusters.

[View a detailed API Reference for Policy](policy_api.md).

---

## PolicySet

PolicySet is the schema for the policysets API. A policy set is a logical grouping of policies from the same namespace. The policy set is bound to a placement resource and applies the placement to all policies within the set. The status reports the overall compliance of the set.

[View a detailed API Reference for PolicySet](policyset_api.md).

---

## PolicyAutomation

PolicyAutomation is the schema for the policyautomations API. PolicyAutomation configures creation of an AnsibleJob, from the tower.ansible.com API group, to initiate Ansible to run upon noncompliant events of the attached policy, or when you manually initiate the run with the "policy.open-cluster-management.io/rerun=true" annotation.

[View a detailed API Reference for PolicyAutomation](policyautomation_api.md).

---

## ObservabilityAddon

ObservabilityAddon is the Schema for the observabilityaddon API

[View a detailed API Reference for ObservabilityAddon](observabilityaddon_api.md).

---

## MultiClusterObservability

MultiClusterObservability defines the configuration for the Observability installation on
Hub and Managed Clusters all through this one custom resource.

[View a detailed API Reference for MultiClusterObservability](multiclusterobservability_api.md).

---

## Observatorium

Observatorium is the Schema for the observatoria API

[View a detailed API Reference for Observatorium](observatorium_api.md).

---

## InternalHubComponent

Description not found in CRD.

[View a detailed API Reference for InternalHubComponent](internalhubcomponent_api.md).

---

## SubmarinerDiagnoseConfig

SubmarinerDiagnoseConfig represents the configuration to run SubmarinerDiagnose Job.

[View a detailed API Reference for SubmarinerDiagnoseConfig](submarinerdiagnoseconfig_api.md).

---

## SubmarinerConfig

SubmarinerConfig represents the configuration for Submariner, the submariner-addon will use it
to configure the Submariner.

[View a detailed API Reference for SubmarinerConfig](submarinerconfig_api.md).

---

## BackupSchedule

BackupSchedule is an ACM resource that you can use to schedule cluster backups at specified intervals.
The backupschedule resource creates a set of schedule.velero.io resources to periodically generate backups for
resources on your ACM hub cluster.

[View a detailed API Reference for BackupSchedule](backupschedule_api.md).

---

## Restore

Restore is an ACM resource that you can use to restore resources from a cluster backup to a target cluster.
The restore resource has properties that you can use to restore only passive data or to restore managed cluster
activation resources.
Additionally, it has a property that you can use to periodically check for new backups and automatically restore
them on the target cluster.

[View a detailed API Reference for Restore](restore_api.md).

---

## UserPreference

Description not found in CRD.

[View a detailed API Reference for UserPreference](userpreference_api.md).

---

## Application

Application is the Schema for the applications API

[View a detailed API Reference for Application](application_api.md).

---

## PlacementRule

PlacementRule is the Schema for the placementrules API

[View a detailed API Reference for PlacementRule](placementrule_api.md).

---

## SubscriptionReport

SubscriptionReport provides a report of the status of the subscriptions on the managed clusters. There are two
types of subscriptions reports: Application and Cluster. Application type reports provide the status of a particular
subscription on all the managed clusters. Cluster type reports provide the status of all the subscriptions on a
particular managed cluster.

[View a detailed API Reference for SubscriptionReport](subscriptionreport_api.md).

---

## Deployable

Deployable is the Schema for the deployables API

[View a detailed API Reference for Deployable](deployable_api.md).

---

## MulticlusterApplicationSetReport

MulticlusterApplicationSetReport provides a report of the status of an application from all the managed clusters where the application is deployed on. It provides a summary of the number of clusters in the various states. If an error or warning occurred when installing the application on a managed cluster, the conditions, including the waring and error message, is captured in the report.

[View a detailed API Reference for MulticlusterApplicationSetReport](multiclusterapplicationsetreport_api.md).

---

## Channel

Channel provides a repository containing application resources which can be deployed to clusters by subscriptions. The following 3 types of channels are supported: Git repository, Helm release registry, and Object storage repository.

[View a detailed API Reference for Channel](channel_api.md).

---

## Subscription

Subscription is the Schema for the subscriptions API

[View a detailed API Reference for Subscription](subscription_api.md).

---

## HelmRelease

HelmRelease is the Schema for the subscriptionreleases API

[View a detailed API Reference for HelmRelease](helmrelease_api.md).

---

## GitOpsCluster

The GitOpsCluster uses placement to import selected managed clusters into the Argo CD.

[View a detailed API Reference for GitOpsCluster](gitopscluster_api.md).

---

## SubscriptionStatus

SubscriptionStatus provides detailed status for all the resources that are deployed by the application in a cluster.

[View a detailed API Reference for SubscriptionStatus](subscriptionstatus_api.md).

---

## PolicyReport

PolicyReport is the Schema for the policyreports API

[View a detailed API Reference for PolicyReport](policyreport_api.md).

---

