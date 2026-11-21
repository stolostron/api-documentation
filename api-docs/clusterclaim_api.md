# ClusterClaim API

ClusterClaim represents cluster information that a managed cluster claims
ClusterClaims with well known names include,
 1. id.k8s.io, it contains a unique identifier for the cluster.
 2. clusterset.k8s.io, it contains an identifier that relates the cluster
    to the ClusterSet in which it belongs.
ClusterClaims created on a managed cluster will be collected and saved into
the status of the corresponding ManagedCluster on hub.

## Spec Fields

Spec defines the attributes of the ClusterClaim.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **value** | `string` | Value is a claim-dependent string | N/A |
## Status Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
