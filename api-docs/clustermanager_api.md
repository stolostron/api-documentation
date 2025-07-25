# ClusterManager API

## Spec Fields

Spec represents a desired deployment configuration of controllers that govern registration and work distribution for attached Klusterlets.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **addOnManagerConfiguration** | `object` | AddOnManagerConfiguration contains the configuration of addon manager | N/A |
| └>&nbsp;&nbsp; **featureGates** | `array` | FeatureGates represents the list of feature gates for addon manager If it is set empty, default feature gates will be used. If it is set, featuregate/Foo is an example of one item in FeatureGates:   1. If featuregate/Foo does not exist, registration-operator will discard it   2. If featuregate/Foo exists and is false by default. It is now possible to set featuregate/Foo=[false|true]   3. If featuregate/Foo exists and is true by default. If a cluster-admin upgrading from 1 to 2 wants to continue having featuregate/Foo=false,  	he can set featuregate/Foo=false before upgrading. Let's say the cluster-admin wants featuregate/Foo=false. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **feature** | `string` | Feature is the key of feature gate. e.g. featuregate/Foo. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **mode** | `string` | Mode is either Enable, Disable, "" where "" is Disable by default. In Enable mode, a valid feature gate `featuregate/Foo` will be set to "--featuregate/Foo=true". In Disable mode, a valid feature gate `featuregate/Foo` will be set to "--featuregate/Foo=false". | N/A |
|  **addOnManagerImagePullSpec** | `string` | AddOnManagerImagePullSpec represents the desired image configuration of addon manager controller/webhook installed on hub. | N/A |
|  **deployOption** | `object` | DeployOption contains the options of deploying a cluster-manager Default mode is used if DeployOption is not set. | N/A |
| └>&nbsp;&nbsp; **hosted** | `object` | Hosted includes configurations we need for clustermanager in the Hosted mode. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **registrationWebhookConfiguration** | `object` | RegistrationWebhookConfiguration represents the customized webhook-server configuration of registration. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **address** | `string` | Address represents the address of a webhook-server. It could be in IP format or fqdn format. The Address must be reachable by apiserver of the hub cluster. | `Pattern=^(([a-zA-Z0-9]\|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]\|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **port** | `integer` | Port represents the port of a webhook-server. The default value of Port is 443. | `Maximum=65535` |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **workWebhookConfiguration** | `object` | WorkWebhookConfiguration represents the customized webhook-server configuration of work. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **address** | `string` | Address represents the address of a webhook-server. It could be in IP format or fqdn format. The Address must be reachable by apiserver of the hub cluster. | `Pattern=^(([a-zA-Z0-9]\|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]\|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **port** | `integer` | Port represents the port of a webhook-server. The default value of Port is 443. | `Maximum=65535` |
| └>&nbsp;&nbsp; **mode** | `string` | Mode can be Default or Hosted. In Default mode, the Hub is installed as a whole and all parts of Hub are deployed in the same cluster. In Hosted mode, only crd and configurations are installed on one cluster(defined as hub-cluster). Controllers run in another cluster (defined as management-cluster) and connect to the hub with the kubeconfig in secret of "external-hub-kubeconfig"(a kubeconfig of hub-cluster with cluster-admin permission). Note: Do not modify the Mode field once it's applied. | N/A |
|  **nodePlacement** | `object` | NodePlacement enables explicit control over the scheduling of the deployed pods. | N/A |
| └>&nbsp;&nbsp; **nodeSelector** | `object` | NodeSelector defines which Nodes the Pods are scheduled on. The default is an empty list. | N/A |
| └>&nbsp;&nbsp; **tolerations** | `array` | Tolerations are attached by pods to tolerate any taint that matches the triple <key,value,effect> using the matching operator <operator>. The default is an empty list. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **effect** | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **key** | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **operator** | `string` | Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tolerationSeconds** | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. | N/A |
|  **placementImagePullSpec** | `string` | PlacementImagePullSpec represents the desired image configuration of placement controller/webhook installed on hub. | N/A |
|  **registrationConfiguration** | `object` | RegistrationConfiguration contains the configuration of registration | N/A |
| └>&nbsp;&nbsp; **autoApproveUsers** | `array` | AutoApproveUser represents a list of users that can auto approve CSR and accept client. If the credential of the bootstrap-hub-kubeconfig matches to the users, the cluster created by the bootstrap-hub-kubeconfig will be auto-registered into the hub cluster. This takes effect only when ManagedClusterAutoApproval feature gate is enabled. | N/A |
| └>&nbsp;&nbsp; **featureGates** | `array` | FeatureGates represents the list of feature gates for registration If it is set empty, default feature gates will be used. If it is set, featuregate/Foo is an example of one item in FeatureGates:   1. If featuregate/Foo does not exist, registration-operator will discard it   2. If featuregate/Foo exists and is false by default. It is now possible to set featuregate/Foo=[false|true]   3. If featuregate/Foo exists and is true by default. If a cluster-admin upgrading from 1 to 2 wants to continue having featuregate/Foo=false,  	he can set featuregate/Foo=false before upgrading. Let's say the cluster-admin wants featuregate/Foo=false. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **feature** | `string` | Feature is the key of feature gate. e.g. featuregate/Foo. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **mode** | `string` | Mode is either Enable, Disable, "" where "" is Disable by default. In Enable mode, a valid feature gate `featuregate/Foo` will be set to "--featuregate/Foo=true". In Disable mode, a valid feature gate `featuregate/Foo` will be set to "--featuregate/Foo=false". | N/A |
| └>&nbsp;&nbsp; **registrationDrivers** | `array` | RegistrationDrivers represent the list of hub registration drivers that contain information used by hub to initialize the hub cluster A RegistrationDriverHub contains details of authentication type and the hub cluster ARN | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **authType** | `string` | Type of the authentication used by hub to initialize the Hub cluster. Possible values are csr and awsirsa. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **awsirsa** | `object` | AwsIrsa represents the configuration for awsirsa driver. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **autoApprovedIdentities** | `array` | AutoApprovedIdentities represent a list of approved arn patterns | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **hubClusterArn** | `string` | This represents the hub cluster ARN Example - arn:eks:us-west-2:12345678910:cluster/hub-cluster1 | `Pattern=^arn:aws:eks:([a-zA-Z0-9-]+):(\d{12}):cluster/([a-zA-Z0-9-]+)$` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **tags** | `array` | List of tags to be added to AWS resources created by hub while processing awsirsa registration request Example - "product:v1:tenant:app-name=My-App" | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **csr** | `object` | CSR represents the configuration for csr driver. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **autoApprovedIdentities** | `array` | AutoApprovedIdentities represent a list of approved users | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **grpc** | `object` | GRPC represents the configuration for gRPC driver. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **autoApprovedIdentities** | `array` | AutoApprovedIdentities represent a list of approved arn patterns | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **endpointExposure** | `object` | EndpointExposure represents the configuration for endpoint exposure. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **hostname** | `object` | Hostname points to a fixed hostname for serving agents' handshakes. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **value** | `string` | No description provided. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **type** | `string` | Type specifies how the gRPC endpoint is exposed. You may need to apply an object to expose the gRPC endpoint, for example: a route. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **imagePullSpec** | `string` | ImagePullSpec represents the desired image of the gRPC broker installed on hub. | N/A |
|  **registrationImagePullSpec** | `string` | RegistrationImagePullSpec represents the desired image of registration controller/webhook installed on hub. | N/A |
|  **resourceRequirement** | `object` | ResourceRequirement specify QoS classes of deployments managed by clustermanager. It applies to all the containers in the deployments. | N/A |
| └>&nbsp;&nbsp; **resourceRequirements** | `object` | ResourceRequirements defines resource requests and limits when Type is ResourceQosClassResourceRequirement | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **claims** | `array` | Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container. This is an alpha field and requires enabling the DynamicResourceAllocation feature gate. This field is immutable. It can only be set for containers. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **request** | `string` | Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **limits** | `object` | Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **requests** | `object` | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | N/A |
| └>&nbsp;&nbsp; **type** | `string` | No description provided. | N/A |
|  **workConfiguration** | `object` | WorkConfiguration contains the configuration of work | N/A |
| └>&nbsp;&nbsp; **featureGates** | `array` | FeatureGates represents the list of feature gates for work If it is set empty, default feature gates will be used. If it is set, featuregate/Foo is an example of one item in FeatureGates:   1. If featuregate/Foo does not exist, registration-operator will discard it   2. If featuregate/Foo exists and is false by default. It is now possible to set featuregate/Foo=[false|true]   3. If featuregate/Foo exists and is true by default. If a cluster-admin upgrading from 1 to 2 wants to continue having featuregate/Foo=false,  	he can set featuregate/Foo=false before upgrading. Let's say the cluster-admin wants featuregate/Foo=false. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **feature** | `string` | Feature is the key of feature gate. e.g. featuregate/Foo. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **mode** | `string` | Mode is either Enable, Disable, "" where "" is Disable by default. In Enable mode, a valid feature gate `featuregate/Foo` will be set to "--featuregate/Foo=true". In Disable mode, a valid feature gate `featuregate/Foo` will be set to "--featuregate/Foo=false". | N/A |
| └>&nbsp;&nbsp; **workDriver** | `string` | WorkDriver represents the type of work driver. Possible values are "kube", "mqtt", or "grpc". If not provided, the default value is "kube". If set to non-"kube" drivers, the klusterlet need to use the same driver. and the driver configuration must be provided in a secret named "work-driver-config" in the namespace where the cluster manager is running, adhering to the following structure: config.yaml: |   <driver-config-in-yaml> For detailed driver configuration, please refer to the sdk-go documentation: https://github.com/open-cluster-management-io/sdk-go/blob/main/pkg/cloudevents/README.md#supported-protocols-and-drivers | N/A |
|  **workImagePullSpec** | `string` | WorkImagePullSpec represents the desired image configuration of work controller/webhook installed on hub. | N/A |
## Status Fields

Status represents the current status of controllers that govern the lifecycle of managed clusters.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions contain the different condition statuses for this ClusterManager. Valid condition types are: Applied: Components in hub are applied. Available: Components in hub are available and ready to serve. Progressing: Components in hub are in a transitioning state. Degraded: Components in hub do not match the desired configuration and only provide degraded service. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **generations** | `array` | Generations are used to determine when an item needs to be reconciled or has changed in a way that needs a reaction. | N/A |
| └>&nbsp;&nbsp; **group** | `string` | group is the group of the resource that you're tracking | N/A |
| └>&nbsp;&nbsp; **lastGeneration** | `integer` | lastGeneration is the last generation of the resource that controller applies | N/A |
| └>&nbsp;&nbsp; **name** | `string` | name is the name of the resource that you're tracking | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | namespace is where the resource that you're tracking is | N/A |
| └>&nbsp;&nbsp; **resource** | `string` | resource is the resource type of the resource that you're tracking | N/A |
| └>&nbsp;&nbsp; **version** | `string` | version is the version of the resource that you're tracking | N/A |
|  **observedGeneration** | `integer` | ObservedGeneration is the last generation change you've dealt with | N/A |
|  **relatedResources** | `array` | RelatedResources are used to track the resources that are related to this ClusterManager. | N/A |
| └>&nbsp;&nbsp; **group** | `string` | group is the group of the resource that you're tracking | N/A |
| └>&nbsp;&nbsp; **name** | `string` | name is the name of the resource that you're tracking | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | namespace is where the thing you're tracking is | N/A |
| └>&nbsp;&nbsp; **resource** | `string` | resource is the resource type of the resource that you're tracking | N/A |
| └>&nbsp;&nbsp; **version** | `string` | version is the version of the thing you're tracking | N/A |
