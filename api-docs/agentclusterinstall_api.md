# AgentClusterInstall API

AgentClusterInstall represents a request to provision an agent based cluster.

## Spec Fields

AgentClusterInstallSpec defines the desired state of the AgentClusterInstall.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **apiVIP** | `string` | APIVIP is the virtual IP used to reach the OpenShift cluster's API. | N/A |
|  **apiVIPs** | `array` | APIVIPs are the virtual IPs used to reach the OpenShift cluster's API. Enter one IP address for single-stack clusters, or up to two for dual-stack clusters (at most one IP address per IP stack used). The order of stacks should be the same as order of subnets in Cluster Networks, Service Networks, and Machine Networks. | N/A |
|  **clusterDeploymentRef** | `object` | ClusterDeploymentRef is a reference to the ClusterDeployment associated with this AgentClusterInstall. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid? | N/A |
|  **clusterMetadata** | `object` | ClusterMetadata contains metadata information about the installed cluster. It should be populated once the cluster install is completed. (it can be populated sooner if desired, but Hive will not copy back to ClusterDeployment until the Installed condition goes True. | N/A |
| └>&nbsp;&nbsp; **adminKubeconfigSecretRef** | `object` | AdminKubeconfigSecretRef references the secret containing the admin kubeconfig for this cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid? | N/A |
| └>&nbsp;&nbsp; **adminPasswordSecretRef** | `object` | AdminPasswordSecretRef references the secret containing the admin username/password which can be used to login to this cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid? | N/A |
| └>&nbsp;&nbsp; **clusterID** | `string` | ClusterID is a globally unique identifier for this cluster generated during installation. Used for reporting metrics among other places. | N/A |
| └>&nbsp;&nbsp; **infraID** | `string` | InfraID is an identifier for this cluster generated during installation and used for tagging/naming resources in cloud providers. | N/A |
| └>&nbsp;&nbsp; **platform** | `object` | Platform holds platform-specific cluster metadata | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **aws** | `object` | AWS holds AWS-specific cluster metadata | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **hostedZoneRole** | `string` | HostedZoneRole is the role to assume when performing operations on a hosted zone owned by another account. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **azure** | `object` | Azure holds azure-specific cluster metadata | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceGroupName** | `string` | ResourceGroupName is the name of the resource group in which the cluster resources were created. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **gcp** | `object` | GCP holds GCP-specific cluster metadata | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **networkProjectID** | `string` | NetworkProjectID is used for shared VPC setups | N/A |
|  **compute** | `array` | Compute is the configuration for the machines that comprise the compute nodes. | N/A |
| └>&nbsp;&nbsp; **hyperthreading** | `string` | Hyperthreading determines the mode of hyperthreading that machines in the pool will utilize. Default is for hyperthreading to be enabled. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the machine pool. For the control plane machine pool, the name will always be "master". For the compute machine pools, the only valid name is "worker". | N/A |
|  **controlPlane** | `object` | ControlPlane is the configuration for the machines that comprise the control plane. | N/A |
| └>&nbsp;&nbsp; **hyperthreading** | `string` | Hyperthreading determines the mode of hyperthreading that machines in the pool will utilize. Default is for hyperthreading to be enabled. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the machine pool. For the control plane machine pool, the name will always be "master". For the compute machine pools, the only valid name is "worker". | N/A |
|  **diskEncryption** | `object` | DiskEncryption is the configuration to enable/disable disk encryption for cluster nodes. | N/A |
| └>&nbsp;&nbsp; **enableOn** | `string` | Enable/disable disk encryption on master nodes, worker nodes, or all nodes. | N/A |
| └>&nbsp;&nbsp; **mode** | `string` | The disk encryption mode to use. | N/A |
| └>&nbsp;&nbsp; **tangServers** | `string` | JSON-formatted string containing additional information regarding tang's configuration | N/A |
|  **external** | `object` | ExternalPlatformSpec represents generic infrastructure provider. Platform-specific components should be supplemented separately. | N/A |
| └>&nbsp;&nbsp; **cloudControllerManager** | `string` | CloudControllerManager when set to external, this property will enable an external cloud provider. | N/A |
| └>&nbsp;&nbsp; **platformName** | `string` | PlatformName holds the arbitrary string representing the infrastructure provider name, expected to be set at the installation time. This field is solely for informational and reporting purposes and is not expected to be used for decision-making. | N/A |
|  **holdInstallation** | `boolean` | HoldInstallation will prevent installation from happening when true. Inspection and validation will proceed as usual, but once the RequirementsMet condition is true, installation will not begin until this field is set to false. | N/A |
|  **ignitionEndpoint** | `object` | IgnitionEndpoint stores the data of the custom ignition endpoint. | N/A |
| └>&nbsp;&nbsp; **caCertificateReference** | `object` | CaCertificateReference is a reference to the secret containing CA certificate to be used when contacting the URL via HTTPS. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the secret containing the CA certificate. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace is the namespace of the secret containing the CA certificate base64 encoded. | N/A |
| └>&nbsp;&nbsp; **url** | `string` | Url stores the URL of the custom ignition endpoint. | N/A |
|  **imageSetRef** | `object` | ImageSetRef is a reference to a ClusterImageSet. The release image specified in the ClusterImageSet will be used to install the cluster. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the ClusterImageSet that this refers to | N/A |
|  **ingressVIP** | `string` | IngressVIP is the virtual IP used for cluster ingress traffic. | N/A |
|  **ingressVIPs** | `array` | IngressVIPs are the virtual IPs used for cluster ingress traffic. Enter one IP address for single-stack clusters, or up to two for dual-stack clusters (at most one IP address per IP stack used). The order of stacks should be the same as order of subnets in Cluster Networks, Service Networks, and Machine Networks. | N/A |
|  **loadBalancer** | `object` | LoadBalancer defines the load balancer used by the cluster for ingress traffic. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type defines the type of load balancer used by the cluster, which can be managed by the user or by the cluster. The default value is ClusterManaged. | N/A |
|  **manifestsConfigMapRef** | `object` | ManifestsConfigMapRef is a reference to user-provided manifests to add to or replace manifests that are generated by the installer. Deprecated: this field is ignored when ManifestsConfigMapRefs is set. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid? | N/A |
|  **manifestsConfigMapRefs** | `array` | ManifestsConfigMapRefs is an array of references to user-provided manifests ConfigMaps to add to or replace manifests that are generated by the installer. Manifest names in each ConfigMap should be unique across all referenced ConfigMaps. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the ConfigMap that this refers to | N/A |
|  **mastersSchedulable** | `boolean` | Set to true to allow control plane nodes to be schedulable | N/A |
|  **mirrorRegistryRef** | `object` | MirrorRegistryRef is a reference to ClusterMirrorRegistry ConfigMap that holds the registries toml data Set per cluster mirror registry | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the ConfigMap that this refers to | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the ConfigMap | N/A |
|  **networking** | `object` | Networking is the configuration for the pod network provider in the cluster. | N/A |
| └>&nbsp;&nbsp; **clusterNetwork** | `array` | ClusterNetwork is the list of IP address pools for pods. Default is 10.128.0.0/14 and a host prefix of /23. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cidr** | `string` | CIDR is the IP block address pool. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **hostPrefix** | `integer` | HostPrefix is the prefix size to allocate to each node from the CIDR. For example, 24 would allocate 2^8=256 adresses to each node. If this field is not used by the plugin, it can be left unset. | N/A |
| └>&nbsp;&nbsp; **machineNetwork** | `array` | MachineNetwork is the list of IP address pools for machines. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cidr** | `string` | CIDR is the IP block address pool for machines within the cluster. | N/A |
| └>&nbsp;&nbsp; **networkType** | `string` | NetworkType is the Container Network Interface (CNI) plug-in to install The default value is OpenShiftSDN for IPv4, and OVNKubernetes for IPv6 or SNO | N/A |
| └>&nbsp;&nbsp; **serviceNetwork** | `array` | ServiceNetwork is the list of IP address pools for services. Default is 172.30.0.0/16. | N/A |
| └>&nbsp;&nbsp; **userManagedNetworking** | `boolean` | UserManagedNetworking indicates if the networking is managed by the user. For single-node installations (none or external platform), set to true or leave empty. | N/A |
|  **platformType** | `string` | PlatformType is the name for the specific platform upon which to perform the installation. | N/A |
|  **provisionRequirements** | `object` | ProvisionRequirements defines configuration for when the installation is ready to be launched automatically. | N/A |
| └>&nbsp;&nbsp; **controlPlaneAgents** | `integer` | ControlPlaneAgents is the number of matching approved and ready Agents with the control plane role required to launch the install. Must be either 1 or 3-5. | N/A |
| └>&nbsp;&nbsp; **workerAgents** | `integer` | WorkerAgents is the minimum number of matching approved and ready Agents with the worker role required to launch the install. | `Minimum=0` |
|  **proxy** | `object` | Proxy defines the proxy settings used for the install config | N/A |
| └>&nbsp;&nbsp; **httpProxy** | `string` | HTTPProxy is the URL of the proxy for HTTP requests. | N/A |
| └>&nbsp;&nbsp; **httpsProxy** | `string` | HTTPSProxy is the URL of the proxy for HTTPS requests. | N/A |
| └>&nbsp;&nbsp; **noProxy** | `string` | NoProxy is a comma-separated list of domains and CIDRs for which the proxy should not be used. | N/A |
|  **sshPublicKey** | `string` | SSHPublicKey will be added to all cluster hosts for use in debugging. | N/A |
## Status Fields

AgentClusterInstallStatus defines the observed state of the AgentClusterInstall.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **apiVIP** | `string` | APIVIP is the virtual IP used to reach the OpenShift cluster's API. | N/A |
|  **apiVIPs** | `array` | APIVIPs are the virtual IPs used to reach the OpenShift cluster's API. | N/A |
|  **conditions** | `array` | Conditions includes more detailed status for the cluster install. | N/A |
| └>&nbsp;&nbsp; **lastProbeTime** | `string` | LastProbeTime is the last time we probed the condition. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the last time the condition transitioned from one status to another. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message is a human-readable message indicating details about last transition. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason is a unique, one-word, CamelCase reason for the condition's last transition. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status is the status of the condition. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type is the type of the condition. | N/A |
|  **connectivityMajorityGroups** | `string` | No description provided. | N/A |
|  **controlPlaneAgentsDiscovered** | `integer` | ControlPlaneAgentsDiscovered is the number of Agents currently linked to this ClusterDeployment. | N/A |
|  **controlPlaneAgentsReady** | `integer` | ControlPlaneAgentsDiscovered is the number of Agents currently linked to this ClusterDeployment that are ready for use. | N/A |
|  **debugInfo** | `object` | DebugInfo includes information for debugging the installation process. | N/A |
| └>&nbsp;&nbsp; **eventsURL** | `string` | EventsURL specifies an HTTP/S URL that contains events which occurred during the cluster installation process | N/A |
| └>&nbsp;&nbsp; **logsURL** | `string` | LogsURL specifies a url for download controller logs tar file. | N/A |
| └>&nbsp;&nbsp; **state** | `string` | Current state of the AgentClusterInstall | N/A |
| └>&nbsp;&nbsp; **stateInfo** | `string` | Additional information pertaining to the status of the AgentClusterInstall | N/A |
|  **ingressVIP** | `string` | IngressVIP is the virtual IP used for cluster ingress traffic. | N/A |
|  **ingressVIPs** | `array` | IngressVIPs are the virtual IPs used for cluster ingress traffic. | N/A |
|  **machineNetwork** | `array` | MachineNetwork is the list of IP address pools for machines. | N/A |
| └>&nbsp;&nbsp; **cidr** | `string` | CIDR is the IP block address pool for machines within the cluster. | N/A |
|  **platformType** | `string` | PlatformType is the name for the specific platform upon which to perform the installation. | N/A |
|  **progress** | `object` | Progress shows the installation progress of the cluster | N/A |
| └>&nbsp;&nbsp; **totalPercentage** | `integer` | Estimated installation progress (in percentage) | N/A |
|  **userManagedNetworking** | `boolean` | UserManagedNetworking indicates if the networking is managed by the user. | N/A |
|  **validationsInfo** | `object` | ValidationsInfo is a JSON-formatted string containing the validation results for each validation id grouped by category (network, hosts-data, etc.) | N/A |
|  **workerAgentsDiscovered** | `integer` | WorkerAgentsDiscovered is the number of worker Agents currently linked to this ClusterDeployment. | N/A |
|  **workerAgentsReady** | `integer` | WorkerAgentsDiscovered is the number of worker Agents currently linked to this ClusterDeployment that are ready for use. | N/A |
