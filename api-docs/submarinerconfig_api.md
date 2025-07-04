# SubmarinerConfig API

## Spec Fields

Spec defines the configuration of the Submariner

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **Debug** | `boolean` | Debug enables Submariner debugging (in the logs). | N/A |
|  **IPSecDebug** | `boolean` | IPSecDebug enables IPSec debugging. | N/A |
|  **IPSecIKEPort** | `integer` | IPSecIKEPort represents IPsec IKE port (default 500). | N/A |
|  **IPSecNATTPort** | `integer` | IPSecNATTPort represents IPsec NAT-T port (default 4500). | N/A |
|  **NATTDiscoveryPort** | `integer` | NATTDiscoveryPort specifies the port used for NAT-T Discovery (default UDP/4900). | N/A |
|  **NATTEnable** | `boolean` | NATTEnable represents IPsec NAT-T enabled (default true). | N/A |
|  **airGappedDeployment** | `boolean` | AirGappedDeployment specifies that the cluster is in an air-gapped environment without access to external servers. | N/A |
|  **cableDriver** | `string` | CableDriver represents the submariner cable driver implementation. Available options are libreswan (default) strongswan, wireguard, and vxlan. | N/A |
|  **credentialsSecret** | `object` | CredentialsSecret is a reference to the secret with a certain cloud platform credentials, the supported platform includes AWS, GCP, Azure, ROKS and OSD. The submariner-addon will use these credentials to prepare Submariner cluster environment. If the submariner cluster environment requires submariner-addon preparation, this field should be specified. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | N/A |
|  **forceUDPEncaps** | `boolean` | ForceUDPEncaps forces UDP Encapsulation for IPSec. | N/A |
|  **gatewayConfig** | `object` | GatewayConfig represents the gateways configuration of the Submariner. | N/A |
| └>&nbsp;&nbsp; **aws** | `object` | AWS represents the configuration for Amazon Web Services. If the platform of managed cluster is not Amazon Web Services, this field will be ignored. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **instanceType** | `string` | InstanceType represents the Amazon Web Services EC2 instance type of the gateway node that will be created on the managed cluster. The default value is `m5n.large`. | N/A |
| └>&nbsp;&nbsp; **azure** | `object` | Azure represents the configuration for Azure Cloud Platform. If the platform of managed cluster is not Azure Cloud Platform, this field will be ignored. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **instanceType** | `string` | InstanceType represents the Azure Cloud Platform instance type of the gateway node that will be created on the managed cluster. The default value is `Standard_F4s_v2`. | N/A |
| └>&nbsp;&nbsp; **gateways** | `integer` | Gateways represents the count of worker nodes that will be used to deploy the Submariner gateway component on the managed cluster. The default value is 1, if the value is greater than 1, the Submariner gateway HA will be enabled automatically. | N/A |
| └>&nbsp;&nbsp; **gcp** | `object` | GCP represents the configuration for Google Cloud Platform. If the platform of managed cluster is not Google Cloud Platform, this field will be ignored. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **instanceType** | `string` | InstanceType represents the Google Cloud Platform instance type of the gateway node that will be created on the managed cluster. The default value is `n1-standard-4`. | N/A |
| └>&nbsp;&nbsp; **rhos** | `object` | RHOS represents the configuration for Redhat Openstack Platform. If the platform of managed cluster is not Redhat Openstack Platform, this field will be ignored. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **instanceType** | `string` | InstanceType represents the Redhat Openstack instance type of the gateway node that will be created on the managed cluster. The default value is `PnTAE.CPU_4_Memory_8192_Disk_50`. | N/A |
|  **globalCIDR** | `string` | GlobalCIDR specifies the global CIDR used by the cluster. | N/A |
|  **haltOnCertificateError** | `boolean` | HaltOnCertificateError halts pods on certificate errors (so they are restarted). | N/A |
|  **hostedCluster** | `boolean` | HostedCluster enabled if the cluster is a hosted cluster. | N/A |
|  **imagePullSpecs** | `object` | ImagePullSpecs represents the desired images of submariner components installed on the managed cluster. If not specified, the default submariner images that was defined by submariner operator will be used. | N/A |
| └>&nbsp;&nbsp; **lighthouseAgentImagePullSpec** | `string` | LighthouseAgentImagePullSpec represents the desired image of the lighthouse agent. | N/A |
| └>&nbsp;&nbsp; **lighthouseCoreDNSImagePullSpec** | `string` | LighthouseCoreDNSImagePullSpec represents the desired image of lighthouse coredns. | N/A |
| └>&nbsp;&nbsp; **metricsProxyImagePullSpec** | `string` | MetricsProxyImagePullSpec represents the desired image of the metrics proxy. | N/A |
| └>&nbsp;&nbsp; **nettestImagePullSpec** | `string` | NettestImagePullSpec represents the desired image of nettest. | N/A |
| └>&nbsp;&nbsp; **submarinerGlobalnetImagePullSpec** | `string` | SubmarinerGlobalnetImagePullSpec represents the desired image of the submariner globalnet. | N/A |
| └>&nbsp;&nbsp; **submarinerImagePullSpec** | `string` | SubmarinerImagePullSpec represents the desired image of submariner. | N/A |
| └>&nbsp;&nbsp; **submarinerNetworkPluginSyncerImagePullSpec** | `string` | SubmarinerNetworkPluginSyncerImagePullSpec represents the desired image of the submariner networkplugin syncer. Deprecated: The networkplugin syncer was removed in v0.16.0. | N/A |
| └>&nbsp;&nbsp; **submarinerRouteAgentImagePullSpec** | `string` | SubmarinerRouteAgentImagePullSpec represents the desired image of the submariner route agent. | N/A |
|  **insecureBrokerConnection** | `boolean` | InsecureBrokerConnection disables certificate validation when contacting the broker. This is useful for scenarios where the certificate chain isn't the same everywhere, e.g. with self-signed certificates with a different trust chain in each cluster. | N/A |
|  **loadBalancerEnable** | `boolean` | LoadBalancerEnable enables or disables load balancer mode. When enabled, a LoadBalancer is created in the submariner-operator namespace (default false). | N/A |
|  **subscriptionConfig** | `object` | SubscriptionConfig represents a Submariner subscription. SubscriptionConfig can be used to customize the Submariner subscription. | N/A |
| └>&nbsp;&nbsp; **channel** | `string` | Channel represents the channel of a submariner subscription. | N/A |
| └>&nbsp;&nbsp; **installPlanApproval** | `string` | InstallPlanApproval determines whether subscription installation plans are applied automatically. | N/A |
| └>&nbsp;&nbsp; **source** | `string` | Source represents the catalog source of a submariner subscription. The default value is redhat-operators | N/A |
| └>&nbsp;&nbsp; **sourceNamespace** | `string` | SourceNamespace represents the catalog source namespace of a submariner subscription. The default value is openshift-marketplace | N/A |
| └>&nbsp;&nbsp; **startingCSV** | `string` | StartingCSV represents the startingCSV of a submariner subscription. | N/A |
## Status Fields

Status represents the current status of submariner configuration

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **conditions** | `array` | Conditions contain the different condition statuses for this configuration. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This may be an empty string. | N/A |
| └>&nbsp;&nbsp; **observedGeneration** | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | `Minimum=0` |
| └>&nbsp;&nbsp; **reason** | `string` | reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | `Pattern=^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$` |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. | `Pattern=^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$` |
|  **managedClusterInfo** | `object` | ManagedClusterInfo represents the information of a managed cluster. | N/A |
| └>&nbsp;&nbsp; **clusterName** | `string` | ClusterName represents the name of the managed cluster. | N/A |
| └>&nbsp;&nbsp; **infraId** | `string` | InfraId represents the infrastructure id of the managed cluster. | N/A |
| └>&nbsp;&nbsp; **networkType** | `string` | NetworkType represents the network type (cni) of the managed cluster. | N/A |
| └>&nbsp;&nbsp; **platform** | `string` | Platform represents the cloud provider of the managed cluster. | N/A |
| └>&nbsp;&nbsp; **region** | `string` | Region represents the cloud region of the managed cluster. | N/A |
| └>&nbsp;&nbsp; **vendor** | `string` | Vendor represents the kubernetes vendor of the managed cluster. | N/A |
| └>&nbsp;&nbsp; **vendorVersion** | `string` | VendorVersion represents k8s vendor version of the managed cluster. | N/A |
