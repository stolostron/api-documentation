# Metal3ClusterTemplate API

Metal3ClusterTemplateSpec defines the desired state of Metal3ClusterTemplate.

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **template** | `object` | Metal3ClusterTemplateResource describes the data for creating a Metal3Cluster from a template. | N/A |
| └>&nbsp;&nbsp; **spec** | `object` | Metal3ClusterSpec defines the desired state of Metal3Cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **cloudProviderEnabled** | `boolean` | Determines if the cluster is to be deployed with an external cloud provider. If set to false, CAPM3 will use node labels to set providerID on the kubernetes nodes. If set to true, providerID is set on nodes by other entities and CAPM3 uses the value of the providerID on the m3m resource. Default value is true, it is set in the webhook. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **controlPlaneEndpoint** | `object` | ControlPlaneEndpoint represents the endpoint used to communicate with the control plane. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **host** | `string` | Host is the hostname on which the API server is serving. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **port** | `integer` | Port is the port on which the API server is serving. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **noCloudProvider** | `boolean` | Determines if the cluster is not to be deployed with an external cloud provider. If set to true, CAPM3 will use node labels to set providerID on the kubernetes nodes. If set to false, providerID is set on nodes by other entities and CAPM3 uses the value of the providerID on the m3m resource.  Deprecated: This field is deprecated, use cloudProviderEnabled instead | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
