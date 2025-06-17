# ClusterResourceSetBinding API

ClusterResourceSetBindingSpec defines the desired state of ClusterResourceSetBinding.

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **bindings** | `array` | bindings is a list of ClusterResourceSets and their resources. | N/A |
| └>&nbsp;&nbsp; **clusterResourceSetName** | `string` | clusterResourceSetName is the name of the ClusterResourceSet that is applied to the owner cluster of the binding. | N/A |
| └>&nbsp;&nbsp; **resources** | `array` | resources is a list of resources that the ClusterResourceSet has. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **applied** | `boolean` | applied is to track if a resource is applied to the cluster or not. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **hash** | `string` | hash is the hash of a resource's data. This can be used to decide if a resource is changed. For "ApplyOnce" ClusterResourceSet.spec.strategy, this is no-op as that strategy does not act on change. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | kind of the resource. Supported kinds are: Secrets and ConfigMaps. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **lastAppliedTime** | `string` | lastAppliedTime identifies when this resource was last applied to the cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | name of the resource that is in the same namespace with ClusterResourceSet object. | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
