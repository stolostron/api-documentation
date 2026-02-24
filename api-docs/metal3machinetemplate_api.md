# Metal3MachineTemplate API

Metal3MachineTemplate is the Schema for the metal3machinetemplates API.

## Spec Fields

Metal3MachineTemplateSpec defines the desired state of Metal3MachineTemplate.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **nodeReuse** | `boolean` | When set to True, CAPM3 Machine controller will pick the same pool of BMHs' that were released during the upgrade operation. | N/A |
|  **template** | `object` | Metal3MachineTemplateResource describes the data needed to create a Metal3Machine from a template. | N/A |
| └>&nbsp;&nbsp; **spec** | `object` | Spec is the specification of the desired behavior of the machine. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **automatedCleaningMode** | `string` | When set to disabled, automated cleaning of host disks will be skipped during provisioning and deprovisioning. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **customDeploy** | `object` | A custom deploy procedure. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **method** | `string` | Custom deploy method name. This name is specific to the deploy ramdisk used. If you don't have a custom deploy ramdisk, you shouldn't use CustomDeploy. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dataTemplate** | `object` | MetadataTemplate is a reference to a Metal3DataTemplate object containing a template of metadata to be rendered. Metadata keys defined in the metadataTemplate take precedence over keys defined in metadata field. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **hostSelector** | `object` | HostSelector specifies matching criteria for labels on BareMetalHosts. This is used to limit the set of BareMetalHost objects considered for claiming for a metal3machine. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchExpressions** | `array` | Label match expressions that must be true on a chosen BareMetalHost | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | Operator represents a key/field's relationship to value(s). See labels.Requirement and fields.Requirement for more details. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **matchLabels** | `object` | Key/value pairs of labels that must exist on a chosen BareMetalHost | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **image** | `object` | Image is the image to be provisioned. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **checksum** | `string` | Checksum is a md5sum, sha256sum or sha512sum value or a URL to retrieve one. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **checksumType** | `string` | ChecksumType is the checksum algorithm for the image. e.g md5, sha256, sha512 | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **format** | `string` | DiskFormat contains the image disk format. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **url** | `string` | URL is a location of an image to deploy. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **metaData** | `object` | MetaData is an object storing the reference to the secret containing the Metadata given by the user. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | name is unique within a namespace to reference a secret resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | namespace defines the space within which the secret name must be unique. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **networkData** | `object` | NetworkData is an object storing the reference to the secret containing the network data given by the user. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | name is unique within a namespace to reference a secret resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | namespace defines the space within which the secret name must be unique. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **providerID** | `string` | ProviderID will be the Metal3 machine in ProviderID format (metal3://<bmh-uuid>) | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **userData** | `object` | UserData references the Secret that holds user data needed by the bare metal operator. The Namespace is optional; it will default to the metal3machine's namespace if not specified. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | name is unique within a namespace to reference a secret resource. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **namespace** | `string` | namespace defines the space within which the secret name must be unique. | N/A |
## Status Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
