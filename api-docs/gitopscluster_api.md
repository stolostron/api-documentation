# GitOpsCluster API

The GitOpsCluster uses placement to import selected managed clusters into the Argo CD.

## Spec Fields

GitOpsClusterSpec defines the desired state of GitOpsCluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **argoServer** | `object` | ArgoServerSpec specifies the location of the Argo CD server. | N/A |
| └>&nbsp;&nbsp; **argoNamespace** | `string` | ArgoNamespace is the namespace in which the Argo CD server is installed. | N/A |
| └>&nbsp;&nbsp; **cluster** | `string` | Not used and reserved for defining a managed cluster name. | N/A |
|  **createBlankClusterSecrets** | `boolean` | Internally used. | N/A |
|  **createPolicyTemplate** | `boolean` | Create default policy template if it is true. | N/A |
|  **managedServiceAccountRef** | `string` | ManagedServiceAccountRef defines managed service account in the managed cluster namespace used to create the ArgoCD cluster secret. | N/A |
|  **placementRef** | `object` | ObjectReference contains enough information to let you inspect or modify the referred object. --- New uses of this type are discouraged because of difficulty describing its usage when embedded in APIs. 1. Ignored fields.  It includes many fields which are not generally honored.  For instance, ResourceVersion and FieldPath are both very rarely valid in actual usage. 2. Invalid usage help.  It is impossible to add specific help for individual usage.  In most embedded usages, there are particular restrictions like, "must refer only to types A and B" or "UID not honored" or "name must be restricted". Those cannot be well described when embedded. 3. Inconsistent validation.  Because the usages are different, the validation rules are different by usage, which makes it hard for users to predict what will happen. 4. The fields are both imprecise and overly precise.  Kind is not a precise mapping to a URL. This can produce ambiguity during interpretation and require a REST mapping.  In most cases, the dependency is on the group,resource tuple and the version of the actual struct is irrelevant. 5. We cannot easily change it.  Because this type is embedded in many locations, updates to this type will affect numerous schemas.  Don't make new APIs embed an underspecified API type they do not control.   Instead of using this type, create a locally provided and used type that is well-focused on your reference. For example, ServiceReferences for admission registration: https://github.com/kubernetes/api/blob/release-1.17/admissionregistration/v1/types.go#L533 . | N/A |
| └>&nbsp;&nbsp; **apiVersion** | `string` | API version of the referent. | N/A |
| └>&nbsp;&nbsp; **fieldPath** | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. TODO: this design is not final and this field is subject to change in the future. | N/A |
| └>&nbsp;&nbsp; **kind** | `string` | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ | N/A |
| └>&nbsp;&nbsp; **resourceVersion** | `string` | Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | N/A |
| └>&nbsp;&nbsp; **uid** | `string` | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids | N/A |
## Status Fields

GitOpsClusterStatus defines the observed state of GitOpsCluster.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **lastUpdateTime** | `string` | LastUpdateTime provides the last updated timestamp of the gitOpsCluster status | N/A |
|  **message** | `string` | Message provides the detailed message of the GitOpsCluster status. | N/A |
|  **phase** | `string` | Phase provides the overall phase of the GitOpsCluster status. Valid values include failed or successful. | N/A |
