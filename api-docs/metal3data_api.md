# Metal3Data API

Metal3DataStatus defines the observed state of Metal3Data.

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **claim** | `object` | DataClaim points to the Metal3DataClaim the Metal3Data was created for. | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| └>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| └>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
|  **index** | `integer` | Index stores the index value of this instance in the Metal3DataTemplate. | N/A |
|  **metaData** | `object` | MetaData points to the rendered MetaData secret. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | name is unique within a namespace to reference a secret resource. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | namespace defines the space within which the secret name must be unique. | N/A |
|  **networkData** | `object` | NetworkData points to the rendered NetworkData secret. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | name is unique within a namespace to reference a secret resource. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | namespace defines the space within which the secret name must be unique. | N/A |
|  **template** | `object` | DataTemplate is the Metal3DataTemplate this was generated from. | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| └>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| └>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
|  **templateReference** | `string` | TemplateReference refers to the Template the Metal3MachineTemplate refers to. It can be matched against the key or it may also point to the name of the template Metal3Data refers to | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **errorMessage** | `string` | ErrorMessage contains the error message | N/A |
|  **ready** | `boolean` | Ready is a flag set to True if the secrets were rendered properly | N/A |
