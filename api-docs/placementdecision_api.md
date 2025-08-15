# PlacementDecision API

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
