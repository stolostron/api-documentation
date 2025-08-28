# ClusterDeploymentCustomization API

ClusterDeploymentCustomization is the Schema for clusterdeploymentcustomizations API.

## Spec Fields

ClusterDeploymentCustomizationSpec defines the desired state of ClusterDeploymentCustomization.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **installConfigPatches** | `array` | InstallConfigPatches is a list of patches to be applied to the install-config. | N/A |
| └>&nbsp;&nbsp; **from** | `string` | From is the json path to copy or move the value from | N/A |
| └>&nbsp;&nbsp; **op** | `string` | Op is the operation to perform. | N/A |
| └>&nbsp;&nbsp; **path** | `string` | Path is the json path to the value to be modified | N/A |
| └>&nbsp;&nbsp; **value** | `string` | Value is the *string* value to be used in the operation. For more complex values, use ValueJSON. | N/A |
| └>&nbsp;&nbsp; **valueJSON** | `string` | ValueJSON is a string representing a JSON object to be used in the operation. As such, internal quotes must be escaped. If nonempty, Value is ignored. | N/A |
|  **installerManifestPatches** | `array` | InstallerManifestPatches is a list of patches to be applied to installer-generated manifests. | N/A |
| └>&nbsp;&nbsp; **manifestSelector** | `object` | ManifestSelector identifies one or more manifests to patch | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **glob** | `string` | Glob is a file glob (per https://pkg.go.dev/path/filepath#Glob) identifying one or more manifests. Paths should be relative to the installer's working directory. Examples: - openshift/99_role-cloud-creds-secret-reader.yaml - openshift/99_openshift-cluster-api_worker-machineset-*.yaml - */*secret* It is an error if a glob matches zero manifests. | N/A |
| └>&nbsp;&nbsp; **patches** | `array` | Patches is a list of RFC6902 patches to apply to manifests identified by manifestSelector. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **from** | `string` | From is the json path to copy or move the value from | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **op** | `string` | Op is the operation to perform. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **path** | `string` | Path is the json path to the value to be modified | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is the *string* value to be used in the operation. For more complex values, use ValueJSON. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **valueJSON** | `string` | ValueJSON is a string representing a JSON object to be used in the operation. As such, internal quotes must be escaped. If nonempty, Value is ignored. | N/A |
## Status Fields

ClusterDeploymentCustomizationStatus defines the observed state of ClusterDeploymentCustomization.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **clusterDeploymentRef** | `object` | ClusterDeploymentRef is a reference to the cluster deployment that this customization is applied on. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
|  **clusterPoolRef** | `object` | ClusterPoolRef is the name of the current cluster pool the CDC used at. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
|  **conditions** | `array` | Conditions describes the state of the operator's reconciliation functionality. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **lastAppliedConfiguration** | `string` | LastAppliedConfiguration contains the last applied patches to the install-config. The information will retain for reference in case the customization is updated. | N/A |
