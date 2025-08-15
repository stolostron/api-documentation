# AppliedManifestWork API

## Spec Fields

Spec represents the desired configuration of AppliedManifestWork.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **agentID** | `string` | AgentID represents the ID of the work agent who is to handle this AppliedManifestWork. | N/A |
|  **hubHash** | `string` | HubHash represents the hash of the first hub kube apiserver to identify which hub this AppliedManifestWork links to. | N/A |
|  **manifestWorkName** | `string` | ManifestWorkName represents the name of the related manifestwork on the hub. | N/A |
## Status Fields

Status represents the current status of AppliedManifestWork.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **appliedResources** | `array` | AppliedResources represents a list of resources defined within the manifestwork that are applied. Only resources with valid GroupVersionResource, namespace, and name are suitable. An item in this slice is deleted when there is no mapped manifest in manifestwork.Spec or by finalizer. The resource relating to the item will also be removed from managed cluster. The deleted resource may still be present until the finalizers for that resource are finished. However, the resource will not be undeleted, so it can be removed from this list and eventual consistency is preserved. | N/A |
| └>&nbsp;&nbsp; **group** | `string` | Group is the API Group of the Kubernetes resource, empty string indicates it is in core group. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the Kubernetes resource. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Name is the namespace of the Kubernetes resource, empty string indicates it is a cluster scoped resource. | N/A |
| └>&nbsp;&nbsp; **resource** | `string` | Resource is the resource name of the Kubernetes resource. | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID is set on successful deletion of the Kubernetes resource by controller. The resource might be still visible on the managed cluster after this field is set. It is not directly settable by a client. | N/A |
| └>&nbsp;&nbsp; **version** | `string` | Version is the version of the Kubernetes resource. | N/A |
|  **evictionStartTime** | `string` | EvictionStartTime represents the current appliedmanifestwork will be evicted after a grace period. An appliedmanifestwork will be evicted from the managed cluster in the following two scenarios:   - the manifestwork of the current appliedmanifestwork is missing on the hub, or   - the appliedmanifestwork hub hash does not match the current hub hash of the work agent. | N/A |
