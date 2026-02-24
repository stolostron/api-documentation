# ClusterInstance API

ClusterInstance is the Schema for the clusterinstances API

## Spec Fields

ClusterInstanceSpec defines the desired state of ClusterInstance

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **additionalNTPSources** | `array` | AdditionalNTPSources is a list of NTP sources (hostname or IP) to be added to all cluster hosts. They are added to any NTP sources that were configured through other means. | N/A |
|  **apiVIPs** | `array` | APIVIPs are the virtual IPs used to reach the OpenShift cluster's API. Enter one IP address for single-stack clusters, or up to two for dual-stack clusters (at most one IP address per IP stack used). The order of stacks should be the same as order of subnets in Cluster Networks, Service Networks, and Machine Networks. | N/A |
|  **baseDomain** | `string` | BaseDomain is the base domain to use for the deployed cluster. | N/A |
|  **caBundleRef** | `object` | CABundle is a reference to a config map containing the new bundle of trusted certificates for the host. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
|  **clusterImageSetNameRef** | `string` | ClusterImageSetNameRef is the name of the ClusterImageSet resource indicating which OpenShift version to deploy. | N/A |
|  **clusterName** | `string` | ClusterName is the name of the cluster. | N/A |
|  **clusterNetwork** | `array` | ClusterNetwork is the list of IP address pools for pods. | N/A |
| └>&nbsp;&nbsp; **cidr** | `string` | CIDR is the IP block address pool. | N/A |
| └>&nbsp;&nbsp; **hostPrefix** | `integer` | HostPrefix is the prefix size to allocate to each node from the CIDR. For example, 24 would allocate 2^8=256 adresses to each node. If this field is not used by the plugin, it can be left unset. | N/A |
|  **clusterType** | `string` | ClusterType is a string representing the cluster type | N/A |
|  **cpuArchitecture** | `string` | CPUArchitecture is the default software architecture used for nodes that do not have an architecture defined. | N/A |
|  **cpuPartitioningMode** | `string` | CPUPartitioning determines if a cluster should be setup for CPU workload partitioning at install time. When this field is set the cluster will be flagged for CPU Partitioning allowing users to segregate workloads to specific CPU Sets. This does not make any decisions on workloads it only configures the nodes to allow CPU Partitioning. The "AllNodes" value will setup all nodes for CPU Partitioning, the default is "None". | N/A |
|  **diskEncryption** | `object` | DiskEncryption is the configuration to enable/disable disk encryption for cluster nodes. | N/A |
| └>&nbsp;&nbsp; **tang** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **thumbprint** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **url** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | No description provided. | N/A |
|  **extraAnnotations** | `object` | Additional cluster-wide annotations to be applied to the rendered templates | N/A |
|  **extraLabels** | `object` | Additional cluster-wide labels to be applied to the rendered templates | N/A |
|  **extraManifestsRefs** | `array` | ExtraManifestsRefs is list of config map references containing additional manifests to be applied to the cluster. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
|  **holdInstallation** | `boolean` | HoldInstallation will prevent installation from happening when true. Inspection and validation will proceed as usual, but once the RequirementsMet condition is true, installation will not begin until this field is set to false. | N/A |
|  **ignitionConfigOverride** | `string` | Json formatted string containing the user overrides for the initial ignition config | N/A |
|  **ingressVIPs** | `array` | IngressVIPs are the virtual IPs used for cluster ingress traffic. Enter one IP address for single-stack clusters, or up to two for dual-stack clusters (at most one IP address per IP stack used). The order of stacks should be the same as order of subnets in Cluster Networks, Service Networks, and Machine Networks. | N/A |
|  **installConfigOverrides** | `string` | InstallConfigOverrides is a Json formatted string that provides a generic way of passing install-config parameters. | N/A |
|  **machineNetwork** | `array` | MachineNetwork is the list of IP address pools for machines. | N/A |
| └>&nbsp;&nbsp; **cidr** | `string` | CIDR is the IP block address pool for machines within the cluster. | N/A |
|  **networkType** | `string` | NetworkType is the Container Network Interface (CNI) plug-in to install The default value is OpenShiftSDN for IPv4, and OVNKubernetes for IPv6 or SNO | N/A |
|  **nodes** | `array` | List of node objects | N/A |
| └>&nbsp;&nbsp; **automatedCleaningMode** | `string` | When set to disabled, automated cleaning will be avoided during provisioning and deprovisioning. Set the value to metadata to enable the removal of the disk’s partitioning table only, without fully wiping the disk. The default value is disabled. | N/A |
| └>&nbsp;&nbsp; **bmcAddress** | `string` | BmcAddress holds the URL for accessing the controller on the network. | N/A |
| └>&nbsp;&nbsp; **bmcCredentialsName** | `object` | BmcCredentialsName is the name of the secret containing the BMC credentials (requires keys "username" and "password"). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **bootMACAddress** | `string` | Which MAC address will PXE boot? This is optional for some types, but required for libvirt VMs driven by vbmc. | `Pattern=[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}` |
| └>&nbsp;&nbsp; **bootMode** | `string` | Provide guidance about how to choose the device for the image being provisioned. | N/A |
| └>&nbsp;&nbsp; **cpuArchitecture** | `string` | CPUArchitecture is the software architecture of the node. If it is not defined here then it is inheirited from the ClusterInstanceSpec. | N/A |
| └>&nbsp;&nbsp; **extraAnnotations** | `object` | Additional node-level annotations to be applied to the rendered templates | N/A |
| └>&nbsp;&nbsp; **extraLabels** | `object` | Additional node-level labels to be applied to the rendered templates | N/A |
| └>&nbsp;&nbsp; **hostName** | `string` | Hostname is the desired hostname for the host | N/A |
| └>&nbsp;&nbsp; **hostRef** | `object` | HostRef is used to specify a reference to a BareMetalHost resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name specifies the name of the referenced object. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace specifies the namespace of the referenced object. | N/A |
| └>&nbsp;&nbsp; **ignitionConfigOverride** | `string` | Json formatted string containing the user overrides for the host's ignition config IgnitionConfigOverride enables the assignment of partitions for persistent storage. Adjust disk ID and size to the specific hardware. | N/A |
| └>&nbsp;&nbsp; **installerArgs** | `string` | Json formatted string containing the user overrides for the host's coreos installer args | N/A |
| └>&nbsp;&nbsp; **ironicInspect** | `string` | IronicInspect is used to specify if automatic introspection carried out during registration of BMH is enabled or disabled | N/A |
| └>&nbsp;&nbsp; **nodeLabels** | `object` | NodeLabels allows the specification of custom roles for your nodes in your managed clusters. These are additional roles that are not used by any OpenShift Container Platform components, only by the user. When you add a custom role, it can be associated with a custom machine config pool that references a specific configuration for that role. Adding custom labels or roles during installation makes the deployment process more effective and prevents the need for additional reboots after the installation is complete. | N/A |
| └>&nbsp;&nbsp; **nodeNetwork** | `object` | NodeNetwork is a set of configurations pertaining to the network settings for the node. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **config** | `object` | yaml that can be processed by nmstate, using custom marshaling/unmarshaling that will allow to populate nmstate config as plain yaml. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **interfaces** | `array` | Interfaces is an array of interface objects containing the name and MAC address for interfaces that are referenced in the raw nmstate config YAML. Interfaces listed here will be automatically renamed in the nmstate config YAML to match the real device name that is observed to have the corresponding MAC address. At least one interface must be listed so that it can be used to identify the correct host, which is done by matching any MAC address in this list to any MAC address observed on the host. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **macAddress** | `string` | mac address present on the host. | `Pattern=^([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})$` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | nic name used in the yaml, which relates 1:1 to the mac address. Name in REST API: logicalNICName | N/A |
| └>&nbsp;&nbsp; **pruneManifests** | `array` | PruneManifests represents a list of Kubernetes resource references that indicates which "node-level" manifests should be pruned (removed). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiVersion** | `string` | APIVersion is the version of the Kubernetes API to use when interacting with the resource. It includes both the API group and the version, such as "v1" for core resources or "apps/v1" for deployments. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind is the type of Kubernetes resource being referenced. | N/A |
| └>&nbsp;&nbsp; **role** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **rootDeviceHints** | `object` | RootDeviceHints specifies the device for deployment. Identifiers that are stable across reboots are recommended, for example, wwn: <disk_wwn> or deviceName: /dev/disk/by-path/<device_path> | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **deviceName** | `string` | A Linux device name like "/dev/vda", or a by-path link to it like "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0". The hint must match the actual value exactly. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **hctl** | `string` | A SCSI bus address like 0:0:0:0. The hint must match the actual value exactly. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **minSizeGigabytes** | `integer` | The minimum size of the device in Gigabytes. | `Minimum=0` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **model** | `string` | A vendor-specific device identifier. The hint can be a substring of the actual value. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **rotational** | `boolean` | True if the device should use spinning media, false otherwise. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serialNumber** | `string` | Device serial number. The hint must match the actual value exactly. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vendor** | `string` | The name of the vendor or manufacturer of the device. The hint can be a substring of the actual value. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **wwn** | `string` | Unique storage identifier. The hint must match the actual value exactly. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **wwnVendorExtension** | `string` | Unique vendor storage identifier. The hint must match the actual value exactly. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **wwnWithExtension** | `string` | Unique storage identifier with the vendor extension appended. The hint must match the actual value exactly. | N/A |
| └>&nbsp;&nbsp; **suppressedManifests** | `array` | SuppressedManifests is a list of node-level manifest names to be excluded from the template rendering process | N/A |
| └>&nbsp;&nbsp; **templateRefs** | `array` | TemplateRefs is a list of references to node-level templates. A node-level template consists of a ConfigMap in which the keys of the data field represent the kind of the installation manifest(s). Node-level templates are instantiated once for each node in the ClusterInstance CR. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name specifies the name of the referenced object. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace specifies the namespace of the referenced object. | N/A |
|  **platformType** | `string` | PlatformType is the name for the specific platform upon which to perform the installation. | N/A |
|  **proxy** | `object` | Proxy defines the proxy settings used for the install config | N/A |
| └>&nbsp;&nbsp; **httpProxy** | `string` | HTTPProxy is the URL of the proxy for HTTP requests. | N/A |
| └>&nbsp;&nbsp; **httpsProxy** | `string` | HTTPSProxy is the URL of the proxy for HTTPS requests. | N/A |
| └>&nbsp;&nbsp; **noProxy** | `string` | NoProxy is a comma-separated list of domains and CIDRs for which the proxy should not be used. | N/A |
|  **pruneManifests** | `array` | PruneManifests represents a list of Kubernetes resource references that indicates which manifests should be pruned (removed). | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | APIVersion is the version of the Kubernetes API to use when interacting with the resource. It includes both the API group and the version, such as "v1" for core resources or "apps/v1" for deployments. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind is the type of Kubernetes resource being referenced. | N/A |
|  **pullSecretRef** | `object` | PullSecretRef is the reference to the secret to use when pulling images. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
|  **reinstall** | `object` | Reinstall specifications | N/A |
| └>&nbsp;&nbsp; **generation** | `string` | Generation specifies the desired generation for the reinstallation operation. Updating this field triggers a new reinstall request. | N/A |
| └>&nbsp;&nbsp; **preservationMode** | `string` | PreservationMode defines the strategy for data preservation during reinstallation. Supported values: - None: No data will be preserved. - All: All Secrets and ConfigMaps in the ClusterInstance namespace labeled with the PreservationLabelKey will be   preserved. - ClusterIdentity: Only Secrets and ConfigMaps in the ClusterInstance namespace labeled with both the   PreservationLabelKey and the ClusterIdentityLabelValue will be preserved. This field ensures critical cluster identity data is preserved when required. | N/A |
|  **serviceNetwork** | `array` | ServiceNetwork is the list of IP address pools for services. | N/A |
| └>&nbsp;&nbsp; **cidr** | `string` | CIDR is the IP block address pool for machines within the cluster. | N/A |
|  **sshPublicKey** | `string` | SSHPublicKey is the public Secure Shell (SSH) key to provide access to instances. This key will be added to the host to allow ssh access | N/A |
|  **suppressedManifests** | `array` | SuppressedManifests is a list of manifest names to be excluded from the template rendering process | N/A |
|  **templateRefs** | `array` | TemplateRefs is a list of references to cluster-level templates. A cluster-level template consists of a ConfigMap in which the keys of the data field represent the kind of the installation manifest(s). Cluster-level templates are instantiated once per cluster (ClusterInstance CR). | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name specifies the name of the referenced object. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace specifies the namespace of the referenced object. | N/A |
## Status Fields

ClusterInstanceStatus defines the observed state of ClusterInstance

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **clusterDeploymentRef** | `object` | Reference to the associated ClusterDeployment resource. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
|  **conditions** | `array` | List of conditions pertaining to actions performed on the ClusterInstance resource. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **deploymentConditions** | `array` | List of hive status conditions associated with the ClusterDeployment resource. | N/A |
| └>&nbsp;&nbsp; **lastProbeTime** | `string` | LastProbeTime is the last time we probed the condition. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the last time the condition transitioned from one status to another. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message is a human-readable message indicating details about last transition. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason is a unique, one-word, CamelCase reason for the condition's last transition. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status is the status of the condition. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type is the type of the condition. | N/A |
|  **manifestsRendered** | `array` | List of manifests that have been rendered along with their status. | N/A |
| └>&nbsp;&nbsp; **apiGroup** | `string` | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind is the type of resource being referenced | N/A |
| └>&nbsp;&nbsp; **lastAppliedTime** | `string` | lastAppliedTime is the last time the manifest was applied. This should be when the underlying manifest changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the resource being referenced | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace is the namespace of the resource being referenced | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status is the status of the manifest | N/A |
| └>&nbsp;&nbsp; **syncWave** | `integer` | SyncWave is the order in which the resource should be processed: created in ascending order, deleted in descending order. | N/A |
|  **observedGeneration** | `integer` | Track the observed generation to avoid unnecessary reconciles | N/A |
|  **paused** | `object` | Paused provides information about the pause annotation set by the controller to temporarily pause reconciliation of the ClusterInstance. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason provides an explanation for why the paused annotation was applied. This field may not be empty. | N/A |
| └>&nbsp;&nbsp; **timeSet** | `string` | TimeSet indicates when the paused annotation was applied. | N/A |
|  **reinstall** | `object` | Reinstall status information. | N/A |
| └>&nbsp;&nbsp; **conditions** | `array` | List of conditions pertaining to reinstall requests. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
| └>&nbsp;&nbsp; **history** | `array` | History maintains a record of all previous reinstallation attempts. Each entry captures details such as the generation, timestamp, and the differences in the ClusterInstance specification that triggered the reinstall. This field is useful for debugging, auditing, and tracking reinstallation events over time. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **clusterInstanceSpecDiff** | `string` | ClusterInstanceSpecDiff provides a JSON representation of the differences between the ClusterInstance spec at the time of reinstallation and the previous spec. This field helps in tracking changes that triggered the reinstallation. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **generation** | `string` | Generation specifies the generation of the ClusterInstance at the time of the reinstallation. This value corresponds to the ReinstallSpec.Generation field associated with the reinstallation request. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **requestEndTime** | `string` | RequestEndTime indicates the time at which SiteConfig completed processing the reinstall request. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **requestStartTime** | `string` | RequestStartTime indicates the time at which SiteConfig was requested to reinstall. | N/A |
| └>&nbsp;&nbsp; **inProgressGeneration** | `string` | InProgressGeneration is the generation of the ClusterInstance that is being processed for reinstallation. It corresponds to the Generation field in ReinstallSpec and indicates the latest reinstall request that the controller is acting upon. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `string` | ObservedGeneration is the generation of the ClusterInstance that has been processed for reinstallation. It corresponds to the Generation field in ReinstallSpec and indicates the latest reinstall request that the controller has acted upon. | N/A |
| └>&nbsp;&nbsp; **requestEndTime** | `string` | RequestEndTime indicates the time at which SiteConfig completed processing the reinstall request. | N/A |
| └>&nbsp;&nbsp; **requestStartTime** | `string` | RequestStartTime indicates the time at which SiteConfig was requested to reinstall. | N/A |
