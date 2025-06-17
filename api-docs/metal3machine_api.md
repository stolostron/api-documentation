# Metal3Machine API

Metal3MachineStatus defines the observed state of Metal3Machine.

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **automatedCleaningMode** | `string` | When set to disabled, automated cleaning of host disks will be skipped during provisioning and deprovisioning. | N/A |
|  **customDeploy** | `object` | A custom deploy procedure. | N/A |
| └>&nbsp;&nbsp; **method** | `string` | Custom deploy method name. This name is specific to the deploy ramdisk used. If you don't have a custom deploy ramdisk, you shouldn't use CustomDeploy. | N/A |
|  **dataTemplate** | `object` | MetadataTemplate is a reference to a Metal3DataTemplate object containing a template of metadata to be rendered. Metadata keys defined in the metadataTemplate take precedence over keys defined in metadata field. | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| └>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| └>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
|  **hostSelector** | `object` | HostSelector specifies matching criteria for labels on BareMetalHosts. This is used to limit the set of BareMetalHost objects considered for claiming for a metal3machine. | N/A |
| └>&nbsp;&nbsp; **matchExpressions** | `array` | Label match expressions that must be true on a chosen BareMetalHost | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | Operator represents a key/field's relationship to value(s). See labels.Requirement and fields.Requirement for more details. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **values** | `array` | No description provided. | N/A |
| └>&nbsp;&nbsp; **matchLabels** | `object` | Key/value pairs of labels that must exist on a chosen BareMetalHost | N/A |
|  **image** | `object` | Image is the image to be provisioned. | N/A |
| └>&nbsp;&nbsp; **checksum** | `string` | Checksum is a md5sum, sha256sum or sha512sum value or a URL to retrieve one. | N/A |
| └>&nbsp;&nbsp; **checksumType** | `string` | ChecksumType is the checksum algorithm for the image. e.g md5, sha256, sha512 | N/A |
| └>&nbsp;&nbsp; **format** | `string` | DiskFormat contains the image disk format. | N/A |
| └>&nbsp;&nbsp; **url** | `string` | URL is a location of an image to deploy. | N/A |
|  **metaData** | `object` | MetaData is an object storing the reference to the secret containing the Metadata given by the user. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | name is unique within a namespace to reference a secret resource. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | namespace defines the space within which the secret name must be unique. | N/A |
|  **networkData** | `object` | NetworkData is an object storing the reference to the secret containing the network data given by the user. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | name is unique within a namespace to reference a secret resource. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | namespace defines the space within which the secret name must be unique. | N/A |
|  **providerID** | `string` | ProviderID will be the Metal3 machine in ProviderID format (metal3://<bmh-uuid>) | N/A |
|  **userData** | `object` | UserData references the Secret that holds user data needed by the bare metal operator. The Namespace is optional; it will default to the metal3machine's namespace if not specified. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | name is unique within a namespace to reference a secret resource. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | namespace defines the space within which the secret name must be unique. | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **addresses** | `array` | Addresses is a list of addresses assigned to the machine. This field is copied from the infrastructure provider reference. | N/A |
| └>&nbsp;&nbsp; **address** | `string` | The machine address. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Machine address type, one of Hostname, ExternalIP, InternalIP, ExternalDNS or InternalDNS. | N/A |
|  **conditions** | `array` | Conditions defines current service state of the Metal3Machine. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | Last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | A human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | The reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **failureMessage** | `string` | FailureMessage will be set in the event that there is a terminal problem reconciling the metal3machine and will contain a more verbose string suitable for logging and human consumption.  This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the metal3machine's spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured.  Any transient errors that occur during the reconciliation of metal3machines can be added as events to the metal3machine object and/or logged in the controller's output. | N/A |
|  **failureReason** | `string` | FailureReason will be set in the event that there is a terminal problem reconciling the metal3machine and will contain a succinct value suitable for machine interpretation.  This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the metal3machine's spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured.  Any transient errors that occur during the reconciliation of metal3machines can be added as events to the metal3machine object and/or logged in the controller's output. | N/A |
|  **lastUpdated** | `string` | LastUpdated identifies when this status was last observed. | N/A |
|  **metaData** | `object` | MetaData is an object storing the reference to the secret containing the Metadata used to deploy the BareMetalHost. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | name is unique within a namespace to reference a secret resource. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | namespace defines the space within which the secret name must be unique. | N/A |
|  **networkData** | `object` | NetworkData is an object storing the reference to the secret containing the network data used to deploy the BareMetalHost. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | name is unique within a namespace to reference a secret resource. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | namespace defines the space within which the secret name must be unique. | N/A |
|  **phase** | `string` | Phase represents the current phase of machine actuation. E.g. Pending, Running, Terminating, Failed etc. | N/A |
|  **ready** | `boolean` | Ready is the state of the metal3. mhrivnak: " it would be good to document what this means, how to interpret it, under what circumstances the value changes, etc." | N/A |
|  **renderedData** | `object` | RenderedData is a reference to a rendered Metal3Data object containing the references to metaData and networkData secrets. | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| └>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| └>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
|  **userData** | `object` | UserData references the Secret that holds user data needed by the bare metal operator. The Namespace is optional; it will default to the metal3machine's namespace if not specified. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | name is unique within a namespace to reference a secret resource. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | namespace defines the space within which the secret name must be unique. | N/A |
