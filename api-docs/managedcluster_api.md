# ManagedCluster API

## Spec Fields

Spec represents a desired configuration for the agent on the managed cluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **hubAcceptsClient** | `boolean` | hubAcceptsClient represents that hub accepts the joining of Klusterlet agent on the managed cluster with the hub. The default value is false, and can only be set true when the user on hub has an RBAC rule to UPDATE on the virtual subresource of managedclusters/accept. When the value is set true, a namespace whose name is the same as the name of ManagedCluster is created on the hub. This namespace represents the managed cluster, also role/rolebinding is created on the namespace to grant the permision of access from the agent on the managed cluster. When the value is set to false, the namespace representing the managed cluster is deleted. | N/A |
|  **leaseDurationSeconds** | `integer` | LeaseDurationSeconds is used to coordinate the lease update time of Klusterlet agents on the managed cluster. If its value is zero, the Klusterlet agent will update its lease every 60 seconds by default | N/A |
|  **managedClusterClientConfigs** | `array` | ManagedClusterClientConfigs represents a list of the apiserver address of the managed cluster. If it is empty, the managed cluster has no accessible address for the hub to connect with it. | N/A |
| └>&nbsp;&nbsp; **caBundle** | `string` | CABundle is the ca bundle to connect to apiserver of the managed cluster. System certs are used if it is not set. | N/A |
| └>&nbsp;&nbsp; **url** | `string` | URL is the URL of apiserver endpoint of the managed cluster. | N/A |
|  **taints** | `array` | Taints is a property of managed cluster that allow the cluster to be repelled when scheduling. Taints, including 'ManagedClusterUnavailable' and 'ManagedClusterUnreachable', can not be added/removed by agent running on the managed cluster; while it's fine to add/remove other taints from either hub cluser or managed cluster. | N/A |
| └>&nbsp;&nbsp; **effect** | `string` | Effect indicates the effect of the taint on placements that do not tolerate the taint. Valid effects are NoSelect, PreferNoSelect and NoSelectIfNew. | N/A |
| └>&nbsp;&nbsp; **key** | `string` | Key is the taint key applied to a cluster. e.g. bar or foo.example.com/bar. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt) | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
| └>&nbsp;&nbsp; **timeAdded** | `string` | TimeAdded represents the time at which the taint was added. | N/A |
| └>&nbsp;&nbsp; **value** | `string` | Value is the taint value corresponding to the taint key. | N/A |
## Status Fields

Status represents the current status of joined managed cluster

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **allocatable** | `object` | Allocatable represents the total allocatable resources on the managed cluster. | N/A |
|  **capacity** | `object` | Capacity represents the total resource capacity from all nodeStatuses on the managed cluster. | N/A |
|  **clusterClaims** | `array` | ClusterClaims represents cluster information that a managed cluster claims, for example a unique cluster identifier (id.k8s.io) and kubernetes version (kubeversion.open-cluster-management.io). They are written from the managed cluster. The set of claims is not uniform across a fleet, some claims can be vendor or version specific and may not be included from all managed clusters. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of a ClusterClaim resource on managed cluster. It's a well known or customized name to identify the claim. | N/A |
| └>&nbsp;&nbsp; **value** | `string` | Value is a claim-dependent string | N/A |
|  **conditions** | `array` | Conditions contains the different condition statuses for this managed cluster. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **version** | `object` | Version represents the kubernetes version of the managed cluster. | N/A |
| └>&nbsp;&nbsp; **kubernetes** | `string` | Kubernetes is the kubernetes version of managed cluster. | N/A |
