# EKSConfigTemplate API

EKSConfigTemplate is the Amazon EKS Bootstrap Configuration Template API.

## Spec Fields

EKSConfigTemplateSpec defines the desired state of templated EKSConfig Amazon EKS Bootstrap Configuration resources.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **template** | `object` | EKSConfigTemplateResource defines the Template structure. | N/A |
| └>&nbsp;&nbsp; **spec** | `object` | EKSConfigSpec defines the desired state of Amazon EKS Bootstrap Configuration. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **apiRetryAttempts** | `integer` | APIRetryAttempts is the number of retry attempts for AWS API call. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **containerRuntime** | `string` | ContainerRuntime specify the container runtime to use when bootstrapping EKS. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dnsClusterIP** | `string` |  DNSClusterIP overrides the IP address to use for DNS queries within the cluster. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **dockerConfigJson** | `string` | DockerConfigJson is used for the contents of the /etc/docker/daemon.json file. Useful if you want a custom config differing from the default one in the AMI. This is expected to be a json string. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **kubeletExtraArgs** | `object` | KubeletExtraArgs passes the specified kubelet args into the Amazon EKS machine bootstrap script | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **pauseContainer** | `object` | PauseContainer allows customization of the pause container to use. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **accountNumber** | `string` |  AccountNumber is the AWS account number to pull the pause container from. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | Version is the tag of the pause container to use. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **serviceIPV6Cidr** | `string` | ServiceIPV6Cidr is the ipv6 cidr range of the cluster. If this is specified then the ip family will be set to ipv6. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **useMaxPods** | `boolean` | UseMaxPods  sets --max-pods for the kubelet when true. | N/A |
## Status Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
