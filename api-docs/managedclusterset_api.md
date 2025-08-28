# ManagedClusterSet API

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

## Spec Fields

Spec defines the attributes of the ManagedClusterSet

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **clusterSelector** | `object` | ClusterSelector represents a selector of ManagedClusters | N/A |
| └>&nbsp;&nbsp; **labelSelector** | `object` | LabelSelector define the general labelSelector which clusterset will use to select target managedClusters | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchExpressions** | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | key is the label key that the selector applies to. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchLabels** | `object` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. | N/A |
| └>&nbsp;&nbsp; **selectorType** | `string` | SelectorType could only be "ExclusiveClusterSetLabel" or "LabelSelector" "ExclusiveClusterSetLabel" means to use label "cluster.open-cluster-management.io/clusterset:<ManagedClusterSet Name>"" to select target clusters. "LabelSelector" means use labelSelector to select target managedClusters | N/A |
## Status Fields

Status represents the current status of the ManagedClusterSet

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions contains the different condition statuses for this ManagedClusterSet. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
