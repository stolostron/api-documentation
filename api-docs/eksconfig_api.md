# EKSConfig API

EKSConfig is the schema for the Amazon EKS Machine Bootstrap Configuration API.

## Spec Fields

EKSConfigSpec defines the desired state of Amazon EKS Bootstrap Configuration.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **apiRetryAttempts** | `integer` | APIRetryAttempts is the number of retry attempts for AWS API call. | N/A |
|  **containerRuntime** | `string` | ContainerRuntime specify the container runtime to use when bootstrapping EKS. | N/A |
|  **dnsClusterIP** | `string` |  DNSClusterIP overrides the IP address to use for DNS queries within the cluster. | N/A |
|  **dockerConfigJson** | `string` | DockerConfigJson is used for the contents of the /etc/docker/daemon.json file. Useful if you want a custom config differing from the default one in the AMI. This is expected to be a json string. | N/A |
|  **kubeletExtraArgs** | `object` | KubeletExtraArgs passes the specified kubelet args into the Amazon EKS machine bootstrap script | N/A |
|  **pauseContainer** | `object` | PauseContainer allows customization of the pause container to use. | N/A |
| └>&nbsp;&nbsp; **accountNumber** | `string` |  AccountNumber is the AWS account number to pull the pause container from. | N/A |
| └>&nbsp;&nbsp; **version** | `string` | Version is the tag of the pause container to use. | N/A |
|  **serviceIPV6Cidr** | `string` | ServiceIPV6Cidr is the ipv6 cidr range of the cluster. If this is specified then the ip family will be set to ipv6. | N/A |
|  **useMaxPods** | `boolean` | UseMaxPods  sets --max-pods for the kubelet when true. | N/A |
## Status Fields

EKSConfigStatus defines the observed state of the Amazon EKS Bootstrap Configuration.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions defines current service state of the EKSConfig. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | Last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | A human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | The reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **dataSecretName** | `string` | DataSecretName is the name of the secret that stores the bootstrap data script. | N/A |
|  **failureMessage** | `string` | FailureMessage will be set on non-retryable errors | N/A |
|  **failureReason** | `string` | FailureReason will be set on non-retryable errors | N/A |
|  **observedGeneration** | `integer` | ObservedGeneration is the latest generation observed by the controller. | N/A |
|  **ready** | `boolean` | Ready indicates the BootstrapData secret is ready to be consumed | N/A |
