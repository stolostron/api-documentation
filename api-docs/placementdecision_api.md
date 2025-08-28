# PlacementDecision API

PlacementDecision indicates a decision from a placement.
PlacementDecision must have a cluster.open-cluster-management.io/placement={placement name} label to reference a certain placement.
If a placement has spec.numberOfClusters specified, the total number of decisions contained in
the status.decisions of PlacementDecisions must be the same as NumberOfClusters. Otherwise, the
total number of decisions must equal the number of ManagedClusters that
match the placement requirements.
Some of the decisions might be empty when there are not enough ManagedClusters to meet the placement requirements.

## Spec Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
## Status Fields

Status represents the current status of the PlacementDecision

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **decisions** | `array` | Decisions is a slice of decisions according to a placement The number of decisions should not be larger than 100 | N/A |
| └>&nbsp;&nbsp; **clusterName** | `string` | ClusterName is the name of the ManagedCluster. If it is not empty, its value should be unique cross all placement decisions for the Placement. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | Reason represents the reason why the ManagedCluster is selected. | N/A |
