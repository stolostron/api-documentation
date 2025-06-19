# FakeClusterInstall API

FakeClusterInstallStatus defines the observed state of the FakeClusterInstall.

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **clusterDeploymentRef** | `object` | ClusterDeploymentRef is a reference to the ClusterDeployment associated with this AgentClusterInstall. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
|  **clusterMetadata** | `object` | ClusterMetadata contains metadata information about the installed cluster. It should be populated once the cluster install is completed. (it can be populated sooner if desired, but Hive will not copy back to ClusterDeployment until the Installed condition goes True. | N/A |
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
|  **imageSetRef** | `object` | ImageSetRef is a reference to a ClusterImageSet. The release image specified in the ClusterImageSet will be used to install the cluster. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the ClusterImageSet that this refers to | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions includes more detailed status for the cluster install. | N/A |
| └>&nbsp;&nbsp; **lastProbeTime** | `string` | LastProbeTime is the last time we probed the condition. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | LastTransitionTime is the last time the condition transitioned from one status to another. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | Message is a human-readable message indicating details about last transition. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason is a unique, one-word, CamelCase reason for the condition's last transition. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | Status is the status of the condition. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type is the type of the condition. | N/A |
