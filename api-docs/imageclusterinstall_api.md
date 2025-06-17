# ImageClusterInstall API

ImageClusterInstallStatus defines the observed state of ImageClusterInstall

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **additionalNTPSources** | `array` | AdditionalNTPSources is a list of NTP sources (hostname or IP) to be added to all cluster hosts. They are added to any NTP sources that were configured through other means. | N/A |
|  **bareMetalHostRef** | `object` | BareMetalHostRef identifies a BareMetalHost object to be used to attach the configuration to the host. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name identifies the BareMetalHost within a namespace | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace identifies the namespace containing the referenced BareMetalHost | N/A |
|  **caBundleRef** | `object` | CABundle is a reference to a config map containing the new bundle of trusted certificates for the host. The tls-ca-bundle.pem entry in the config map will be written to /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
|  **clusterDeploymentRef** | `object` | ClusterDeploymentRef is a reference to the ClusterDeployment. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
|  **clusterMetadata** | `object` | ClusterMetadata contains metadata information about the installed cluster. This must be set as soon as all the information is available. | N/A |
| └>&nbsp;&nbsp; **adminKubeconfigSecretRef** | `object` | AdminKubeconfigSecretRef references the secret containing the admin kubeconfig for this cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **adminPasswordSecretRef** | `object` | AdminPasswordSecretRef references the secret containing the admin username/password which can be used to login to this cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **clusterID** | `string` | ClusterID is a globally unique identifier for this cluster generated during installation. Used for reporting metrics among other places. | N/A |
| └>&nbsp;&nbsp; **infraID** | `string` | InfraID is an identifier for this cluster generated during installation and used for tagging/naming resources in cloud providers. | N/A |
| └>&nbsp;&nbsp; **platform** | `object` | Platform holds platform-specific cluster metadata | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **aws** | `object` | AWS holds AWS-specific cluster metadata | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **hostedZoneRole** | `string` | HostedZoneRole is the role to assume when performing operations on a hosted zone owned by another account. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **azure** | `object` | Azure holds azure-specific cluster metadata | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceGroupName** | `string` | ResourceGroupName is the name of the resource group in which the cluster resources were created. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **gcp** | `object` | GCP holds GCP-specific cluster metadata | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **networkProjectID** | `string` | NetworkProjectID is used for shared VPC setups | N/A |
|  **extraManifestsRefs** | `array` | ExtraManifestsRefs is list of config map references containing additional manifests to be applied to the relocated cluster. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
|  **hostname** | `string` | Hostname is the desired hostname for the host | N/A |
|  **imageDigestSources** | `array` | ImageDigestSources lists sources/repositories for the release-image content. | N/A |
| └>&nbsp;&nbsp; **mirrorSourcePolicy** | `string` | mirrorSourcePolicy defines the fallback policy if fails to pull image from the mirrors. If unset, the image will continue to be pulled from the the repository in the pull spec. sourcePolicy is valid configuration only when one or more mirrors are in the mirror list. | N/A |
| └>&nbsp;&nbsp; **mirrors** | `array` | mirrors is zero or more locations that may also contain the same images. No mirror will be configured if not specified. Images can be pulled from these mirrors only if they are referenced by their digests. The mirrored location is obtained by replacing the part of the input reference that matches source by the mirrors entry, e.g. for registry.redhat.io/product/repo reference, a (source, mirror) pair *.redhat.io, mirror.local/redhat causes a mirror.local/redhat/product/repo repository to be used. The order of mirrors in this list is treated as the user's desired priority, while source is by default considered lower priority than all mirrors. If no mirror is specified or all image pulls from the mirror list fail, the image will continue to be pulled from the repository in the pull spec unless explicitly prohibited by "mirrorSourcePolicy" Other cluster configuration, including (but not limited to) other imageDigestMirrors objects, may impact the exact order mirrors are contacted in, or some mirrors may be contacted in parallel, so this should be considered a preference rather than a guarantee of ordering. "mirrors" uses one of the following formats: host[:port] host[:port]/namespace[/namespace…] host[:port]/namespace[/namespace…]/repo for more information about the format, see the document about the location field: https://github.com/containers/image/blob/main/docs/containers-registries.conf.5.md#choosing-a-registry-toml-table | N/A |
| └>&nbsp;&nbsp; **source** | `string` | source matches the repository that users refer to, e.g. in image pull specifications. Setting source to a registry hostname e.g. docker.io. quay.io, or registry.redhat.io, will match the image pull specification of corressponding registry. "source" uses one of the following formats: host[:port] host[:port]/namespace[/namespace…] host[:port]/namespace[/namespace…]/repo [*.]host for more information about the format, see the document about the location field: https://github.com/containers/image/blob/main/docs/containers-registries.conf.5.md#choosing-a-registry-toml-table | `Pattern=^\*(?:\.(?:[a-zA-Z0-9]\|[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]))+$\|^((?:[a-zA-Z0-9]\|[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9])(?:(?:\.(?:[a-zA-Z0-9]\|[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]))+)?(?::[0-9]+)?)(?:(?:/[a-z0-9]+(?:(?:(?:[._]\|__\|[-]*)[a-z0-9]+)+)?)+)?$` |
|  **imageSetRef** | `object` | ImageSetRef is a reference to a ClusterImageSet. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the ClusterImageSet that this refers to | N/A |
|  **machineNetwork** | `string` | MachineNetwork is the subnet provided by user for the ocp cluster. This will be used to create the node network and choose ip address for the node. Equivalent to install-config.yaml's machineNetwork. | N/A |
|  **nodeIP** | `string` | NodeIP is the desired IP for the host Deprecated: this field is ignored (will be removed in a future release). | N/A |
|  **proxy** | `object` | Proxy defines the proxy settings to be applied in relocated cluster | N/A |
| └>&nbsp;&nbsp; **httpProxy** | `string` | HTTPProxy is the URL of the proxy for HTTP requests. | N/A |
| └>&nbsp;&nbsp; **httpsProxy** | `string` | HTTPSProxy is the URL of the proxy for HTTPS requests. | N/A |
| └>&nbsp;&nbsp; **noProxy** | `string` | NoProxy is a comma-separated list of domains and CIDRs for which the proxy should not be used. | N/A |
|  **sshKey** | `string` | SSHKey is the public Secure Shell (SSH) key to provide access to instances. Equivalent to install-config.yaml's sshKey. This key will be added to the host to allow ssh access | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **bareMetalHostRef** | `object` | No description provided. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name identifies the BareMetalHost within a namespace | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace identifies the namespace containing the referenced BareMetalHost | N/A |
|  **bootTime** | `string` | BootTime indicates the time at which the host was requested to boot. Used to determine install timeouts. | N/A |
|  **conditions** | `array` | Conditions is a list of conditions associated with syncing to the cluster. | N/A |
| └>&nbsp;&nbsp; **lastProbeTime** | `string` | LastProbeTime is the last time we probed the condition. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the last time the condition transitioned from one status to another. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message is a human-readable message indicating details about last transition. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason is a unique, one-word, CamelCase reason for the condition's last transition. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status is the status of the condition. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type is the type of the condition. | N/A |
|  **installRestarts** | `integer` | InstallRestarts is the total count of container restarts on the clusters install job. | N/A |
