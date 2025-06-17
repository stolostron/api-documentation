# DiscoveryConfig API

DiscoveryConfigStatus defines the observed state of DiscoveryConfig

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **credential** | `string` | Credential is the secret containing credentials to connect to the OCM api on behalf of a user | N/A |
|  **filters** | `object` | Sets restrictions on what kind of clusters to discover | N/A |
| └>&nbsp;&nbsp; **clusterTypes** | `array` | ClusterTypes is the list of cluster types to discover. These types represent the platform the cluster is running on, such as OpenShift Container Platform (OCP), Azure Red Hat OpenShift (ARO), or others. | N/A |
| └>&nbsp;&nbsp; **infrastructureProviders** | `array` | InfrastructureProviders is the list of infrastructure providers to discover. This can be a list of cloud providers or platforms (e.g., AWS, Azure, GCP) where clusters might be running. | N/A |
| └>&nbsp;&nbsp; **lastActive** | `integer` | LastActive is the last active in days of clusters to discover, determined by activity timestamp | N/A |
| └>&nbsp;&nbsp; **openShiftVersions** | `array` | OpenShiftVersions is the list of release versions of OpenShift of the form "<Major>.<Minor>" | N/A |
| └>&nbsp;&nbsp; **regions** | `array` | Regions is the list of regions where OpenShift clusters are located. This helps in filtering clusters based on geographic location or data center region, useful for compliance or latency requirements. | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
