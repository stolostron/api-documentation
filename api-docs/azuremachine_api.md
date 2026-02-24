# AzureMachine API

AzureMachine is the Schema for the azuremachines API.

## Spec Fields

AzureMachineSpec defines the desired state of AzureMachine.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **acceleratedNetworking** | `boolean` | Deprecated: AcceleratedNetworking should be set in the networkInterfaces field. | N/A |
|  **additionalCapabilities** | `object` | AdditionalCapabilities specifies additional capabilities enabled or disabled on the virtual machine. | N/A |
| └>&nbsp;&nbsp; **ultraSSDEnabled** | `boolean` | UltraSSDEnabled enables or disables Azure UltraSSD capability for the virtual machine. Defaults to true if Ultra SSD data disks are specified, otherwise it doesn't set the capability on the VM. | N/A |
|  **additionalTags** | `object` | AdditionalTags is an optional set of tags to add to an instance, in addition to the ones added by default by the Azure provider. If both the AzureCluster and the AzureMachine specify the same tag name with different values, the AzureMachine's value takes precedence. | N/A |
|  **allocatePublicIP** | `boolean` | AllocatePublicIP allows the ability to create dynamic public ips for machines where this value is true. | N/A |
|  **capacityReservationGroupID** | `string` | CapacityReservationGroupID specifies the capacity reservation group resource id that should be used for allocating the virtual machine. The field size should be greater than 0 and the field input must start with '/'. The input for capacityReservationGroupID must be similar to '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}'. The keys which are used should be among 'subscriptions', 'providers' and 'resourcegroups' followed by valid ID or names respectively. It is optional but may not be changed once set. | N/A |
|  **dataDisks** | `array` | DataDisk specifies the parameters that are used to add one or more data disks to the machine | N/A |
| └>&nbsp;&nbsp; **cachingType** | `string` | CachingType specifies the caching requirements. | N/A |
| └>&nbsp;&nbsp; **diskSizeGB** | `integer` | DiskSizeGB is the size in GB to assign to the data disk. | N/A |
| └>&nbsp;&nbsp; **lun** | `integer` | Lun Specifies the logical unit number of the data disk. This value is used to identify data disks within the VM and therefore must be unique for each data disk attached to a VM. The value must be between 0 and 63. | N/A |
| └>&nbsp;&nbsp; **managedDisk** | `object` | ManagedDisk specifies the Managed Disk parameters for the data disk. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **diskEncryptionSet** | `object` | DiskEncryptionSet specifies the customer-managed disk encryption set resource id for the managed disk. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID defines resourceID for diskEncryptionSet resource. It must be in the same subscription | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **securityProfile** | `object` | SecurityProfile specifies the security profile for the managed disk. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **diskEncryptionSet** | `object` | DiskEncryptionSet specifies the customer-managed disk encryption set resource id for the managed disk that is used for Customer Managed Key encrypted ConfidentialVM OS Disk and VMGuest blob. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID defines resourceID for diskEncryptionSet resource. It must be in the same subscription | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **securityEncryptionType** | `string` | SecurityEncryptionType specifies the encryption type of the managed disk. It is set to DiskWithVMGuestState to encrypt the managed disk along with the VMGuestState blob, and to VMGuestStateOnly to encrypt the VMGuestState blob only. When set to VMGuestStateOnly, VirtualizedTrustedPlatformModule should be set to Enabled. When set to DiskWithVMGuestState, EncryptionAtHost should be disabled, SecureBoot and VirtualizedTrustedPlatformModule should be set to Enabled. It can be set only for Confidential VMs. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **storageAccountType** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **nameSuffix** | `string` | NameSuffix is the suffix to be appended to the machine name to generate the disk name. Each disk name will be in format <machineName>_<nameSuffix>. | N/A |
|  **diagnostics** | `object` | Diagnostics specifies the diagnostics settings for a virtual machine. If not specified then Boot diagnostics (Managed) will be enabled. | N/A |
| └>&nbsp;&nbsp; **boot** | `object` | Boot configures the boot diagnostics settings for the virtual machine. This allows to configure capturing serial output from the virtual machine on boot. This is useful for debugging software based launch issues. If not specified then Boot diagnostics (Managed) will be enabled. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **storageAccountType** | `string` | StorageAccountType determines if the storage account for storing the diagnostics data should be disabled (Disabled), provisioned by Azure (Managed) or by the user (UserManaged). | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **userManaged** | `object` | UserManaged provides a reference to the user-managed storage account. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **storageAccountURI** | `string` | StorageAccountURI is the URI of the user-managed storage account. The URI typically will be `https://<mystorageaccountname>.blob.core.windows.net/` but may differ if you are using Azure DNS zone endpoints. You can find the correct endpoint by looking for the Blob Primary Endpoint in the endpoints tab in the Azure console or with the CLI by issuing `az storage account list --query='[].{name: name, "resource group": resourceGroup, "blob endpoint": primaryEndpoints.blob}'`. | `Pattern=^https://` |
|  **disableExtensionOperations** | `boolean` | DisableExtensionOperations specifies whether extension operations should be disabled on the virtual machine. Use this setting only if VMExtensions are not supported by your image, as it disables CAPZ bootstrapping extension used for detecting Kubernetes bootstrap failure. This may only be set to True when no extensions are configured on the virtual machine. | N/A |
|  **disableVMBootstrapExtension** | `boolean` | DisableVMBootstrapExtension specifies whether the VM bootstrap extension should be disabled on the virtual machine. Use this setting if you want to disable only the bootstrapping extension and not all extensions. | N/A |
|  **dnsServers** | `array` | DNSServers adds a list of DNS Server IP addresses to the VM NICs. | N/A |
|  **enableIPForwarding** | `boolean` | EnableIPForwarding enables IP Forwarding in Azure which is required for some CNI's to send traffic from a pods on one machine to another. This is required for IpV6 with Calico in combination with User Defined Routes (set by the Azure Cloud Controller manager). Default is false for disabled. | N/A |
|  **failureDomain** | `string` | FailureDomain is the failure domain unique identifier this Machine should be attached to, as defined in Cluster API. This relates to an Azure Availability Zone | N/A |
|  **identity** | `string` | Identity is the type of identity used for the virtual machine. The type 'SystemAssigned' is an implicitly created identity. The generated identity will be assigned a Subscription contributor role. The type 'UserAssigned' is a standalone Azure resource provided by the user and assigned to the VM | N/A |
|  **image** | `object` | Image is used to provide details of an image to use during VM creation. If image details are omitted, the default is to use an Azure Compute Gallery Image from CAPZ's community gallery. | N/A |
| └>&nbsp;&nbsp; **computeGallery** | `object` | ComputeGallery specifies an image to use from the Azure Compute Gallery | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **gallery** | `string` | Gallery specifies the name of the compute image gallery that contains the image | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the image | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **plan** | `object` | Plan contains plan information. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **offer** | `string` | Offer specifies the name of a group of related images created by the publisher. For example, UbuntuServer, WindowsServer | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **publisher** | `string` | Publisher is the name of the organization that created the image | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sku** | `string` | SKU specifies an instance of an offer, such as a major release of a distribution. For example, 18.04-LTS, 2019-Datacenter | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceGroup** | `string` | ResourceGroup specifies the resource group containing the private compute gallery. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **subscriptionID** | `string` | SubscriptionID is the identifier of the subscription that contains the private compute gallery. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | Version specifies the version of the marketplace image. The allowed formats are Major.Minor.Build or 'latest'. Major, Minor, and Build are decimal numbers. Specify 'latest' to use the latest version of an image available at deploy time. Even if you use 'latest', the VM image will not automatically update after deploy time even if a new version becomes available. | N/A |
| └>&nbsp;&nbsp; **id** | `string` | ID specifies an image to use by ID | N/A |
| └>&nbsp;&nbsp; **marketplace** | `object` | Marketplace specifies an image to use from the Azure Marketplace | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **offer** | `string` | Offer specifies the name of a group of related images created by the publisher. For example, UbuntuServer, WindowsServer | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **publisher** | `string` | Publisher is the name of the organization that created the image | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sku** | `string` | SKU specifies an instance of an offer, such as a major release of a distribution. For example, 18.04-LTS, 2019-Datacenter | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **thirdPartyImage** | `boolean` | ThirdPartyImage indicates the image is published by a third party publisher and a Plan will be generated for it. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | Version specifies the version of an image sku. The allowed formats are Major.Minor.Build or 'latest'. Major, Minor, and Build are decimal numbers. Specify 'latest' to use the latest version of an image available at deploy time. Even if you use 'latest', the VM image will not automatically update after deploy time even if a new version becomes available. | N/A |
| └>&nbsp;&nbsp; **sharedGallery** | `object` | SharedGallery specifies an image to use from an Azure Shared Image Gallery Deprecated: use ComputeGallery instead. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **gallery** | `string` | Gallery specifies the name of the shared image gallery that contains the image | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **name** | `string` | Name is the name of the image | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **offer** | `string` | Offer specifies the name of a group of related images created by the publisher. For example, UbuntuServer, WindowsServer This value will be used to add a `Plan` in the API request when creating the VM/VMSS resource. This is needed when the source image from which this SIG image was built requires the `Plan` to be used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **publisher** | `string` | Publisher is the name of the organization that created the image. This value will be used to add a `Plan` in the API request when creating the VM/VMSS resource. This is needed when the source image from which this SIG image was built requires the `Plan` to be used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **resourceGroup** | `string` | ResourceGroup specifies the resource group containing the shared image gallery | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **sku** | `string` | SKU specifies an instance of an offer, such as a major release of a distribution. For example, 18.04-LTS, 2019-Datacenter This value will be used to add a `Plan` in the API request when creating the VM/VMSS resource. This is needed when the source image from which this SIG image was built requires the `Plan` to be used. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **subscriptionID** | `string` | SubscriptionID is the identifier of the subscription that contains the shared image gallery | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **version** | `string` | Version specifies the version of the marketplace image. The allowed formats are Major.Minor.Build or 'latest'. Major, Minor, and Build are decimal numbers. Specify 'latest' to use the latest version of an image available at deploy time. Even if you use 'latest', the VM image will not automatically update after deploy time even if a new version becomes available. | N/A |
|  **networkInterfaces** | `array` | NetworkInterfaces specifies a list of network interface configurations. If left unspecified, the VM will get a single network interface with a single IPConfig in the subnet specified in the cluster's node subnet field. The primary interface will be the first networkInterface specified (index 0) in the list. | N/A |
| └>&nbsp;&nbsp; **acceleratedNetworking** | `boolean` | AcceleratedNetworking enables or disables Azure accelerated networking. If omitted, it will be set based on whether the requested VMSize supports accelerated networking. If AcceleratedNetworking is set to true with a VMSize that does not support it, Azure will return an error. | N/A |
| └>&nbsp;&nbsp; **privateIPConfigs** | `integer` | PrivateIPConfigs specifies the number of private IP addresses to attach to the interface. Defaults to 1 if not specified. | N/A |
| └>&nbsp;&nbsp; **subnetName** | `string` | SubnetName specifies the subnet in which the new network interface will be placed. | N/A |
|  **osDisk** | `object` | OSDisk specifies the parameters for the operating system disk of the machine | N/A |
| └>&nbsp;&nbsp; **cachingType** | `string` | CachingType specifies the caching requirements. | N/A |
| └>&nbsp;&nbsp; **diffDiskSettings** | `object` | DiffDiskSettings describe ephemeral disk settings for the os disk. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **option** | `string` | Option enables ephemeral OS when set to "Local" See https://learn.microsoft.com/azure/virtual-machines/ephemeral-os-disks for full details | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **placement** | `string` | Placement specifies the ephemeral disk placement for operating system disk. If placement is specified, Option must be set to "Local". | N/A |
| └>&nbsp;&nbsp; **diskSizeGB** | `integer` | DiskSizeGB is the size in GB to assign to the OS disk. Will have a default of 30GB if not provided | N/A |
| └>&nbsp;&nbsp; **managedDisk** | `object` | ManagedDisk specifies the Managed Disk parameters for the OS disk. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **diskEncryptionSet** | `object` | DiskEncryptionSet specifies the customer-managed disk encryption set resource id for the managed disk. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID defines resourceID for diskEncryptionSet resource. It must be in the same subscription | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **securityProfile** | `object` | SecurityProfile specifies the security profile for the managed disk. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **diskEncryptionSet** | `object` | DiskEncryptionSet specifies the customer-managed disk encryption set resource id for the managed disk that is used for Customer Managed Key encrypted ConfidentialVM OS Disk and VMGuest blob. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **id** | `string` | ID defines resourceID for diskEncryptionSet resource. It must be in the same subscription | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **securityEncryptionType** | `string` | SecurityEncryptionType specifies the encryption type of the managed disk. It is set to DiskWithVMGuestState to encrypt the managed disk along with the VMGuestState blob, and to VMGuestStateOnly to encrypt the VMGuestState blob only. When set to VMGuestStateOnly, VirtualizedTrustedPlatformModule should be set to Enabled. When set to DiskWithVMGuestState, EncryptionAtHost should be disabled, SecureBoot and VirtualizedTrustedPlatformModule should be set to Enabled. It can be set only for Confidential VMs. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **storageAccountType** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **osType** | `string` | No description provided. | N/A |
|  **providerID** | `string` | ProviderID is the unique identifier as specified by the cloud provider. | N/A |
|  **roleAssignmentName** | `string` | Deprecated: RoleAssignmentName should be set in the systemAssignedIdentityRole field. | N/A |
|  **securityProfile** | `object` | SecurityProfile specifies the Security profile settings for a virtual machine. | N/A |
| └>&nbsp;&nbsp; **encryptionAtHost** | `boolean` | This field indicates whether Host Encryption should be enabled or disabled for a virtual machine or virtual machine scale set. This should be disabled when SecurityEncryptionType is set to DiskWithVMGuestState. Default is disabled. | N/A |
| └>&nbsp;&nbsp; **securityType** | `string` | SecurityType specifies the SecurityType of the virtual machine. It has to be set to any specified value to enable UefiSettings. The default behavior is: UefiSettings will not be enabled unless this property is set. | N/A |
| └>&nbsp;&nbsp; **uefiSettings** | `object` | UefiSettings specifies the security settings like secure boot and vTPM used while creating the virtual machine. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **secureBootEnabled** | `boolean` | SecureBootEnabled specifies whether secure boot should be enabled on the virtual machine. Secure Boot verifies the digital signature of all boot components and halts the boot process if signature verification fails. If omitted, the platform chooses a default, which is subject to change over time, currently that default is false. | N/A |
| &nbsp;&nbsp;&nbsp;&nbsp;└>&nbsp;&nbsp; **vTpmEnabled** | `boolean` | VTpmEnabled specifies whether vTPM should be enabled on the virtual machine. When true it enables the virtualized trusted platform module measurements to create a known good boot integrity policy baseline. The integrity policy baseline is used for comparison with measurements from subsequent VM boots to determine if anything has changed. This is required to be set to Enabled if SecurityEncryptionType is defined. If omitted, the platform chooses a default, which is subject to change over time, currently that default is false. | N/A |
|  **spotVMOptions** | `object` | SpotVMOptions allows the ability to specify the Machine should use a Spot VM | N/A |
| └>&nbsp;&nbsp; **evictionPolicy** | `string` | EvictionPolicy defines the behavior of the virtual machine when it is evicted. It can be either Delete or Deallocate. | N/A |
| └>&nbsp;&nbsp; **maxPrice** | `N/A` | MaxPrice defines the maximum price the user is willing to pay for Spot VM instances | `Pattern=^(\+\|-)?(([0-9]+(\.[0-9]*)?)\|(\.[0-9]+))(([KMGTPE]i)\|[numkMGTPE]\|([eE](\+\|-)?(([0-9]+(\.[0-9]*)?)\|(\.[0-9]+))))?$` |
|  **sshPublicKey** | `string` | SSHPublicKey is the SSH public key string, base64-encoded to add to a Virtual Machine. Linux only. Refer to documentation on how to set up SSH access on Windows instances. | N/A |
|  **subnetName** | `string` | Deprecated: SubnetName should be set in the networkInterfaces field. | N/A |
|  **systemAssignedIdentityRole** | `object` | SystemAssignedIdentityRole defines the role and scope to assign to the system-assigned identity. | N/A |
| └>&nbsp;&nbsp; **definitionID** | `string` | DefinitionID is the ID of the role definition to create for a system assigned identity. It can be an Azure built-in role or a custom role. Refer to built-in roles: https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the role assignment to create for a system assigned identity. It can be any valid UUID. If not specified, a random UUID will be generated. | N/A |
| └>&nbsp;&nbsp; **scope** | `string` | Scope is the scope that the role assignment or definition applies to. The scope can be any REST resource instance. If not specified, the scope will be the subscription. | N/A |
|  **userAssignedIdentities** | `array` | UserAssignedIdentities is a list of standalone Azure identities provided by the user The lifecycle of a user-assigned identity is managed separately from the lifecycle of the AzureMachine. See https://learn.microsoft.com/azure/active-directory/managed-identities-azure-resources/how-to-manage-ua-identity-cli | N/A |
| └>&nbsp;&nbsp; **providerID** | `string` | ProviderID is the identification ID of the user-assigned Identity, the format of an identity is: 'azure:///subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}' | N/A |
|  **vmExtensions** | `array` | VMExtensions specifies a list of extensions to be added to the virtual machine. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the extension. | N/A |
| └>&nbsp;&nbsp; **protectedSettings** | `object` | ProtectedSettings is a JSON formatted protected settings for the extension. | N/A |
| └>&nbsp;&nbsp; **publisher** | `string` | Publisher is the name of the extension handler publisher. | N/A |
| └>&nbsp;&nbsp; **settings** | `object` | Settings is a JSON formatted public settings for the extension. | N/A |
| └>&nbsp;&nbsp; **version** | `string` | Version specifies the version of the script handler. | N/A |
|  **vmSize** | `string` | No description provided. | N/A |
## Status Fields

AzureMachineStatus defines the observed state of AzureMachine.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **addresses** | `array` | Addresses contains the Azure instance associated addresses. | N/A |
| └>&nbsp;&nbsp; **address** | `string` | The node address. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Node address type, one of Hostname, ExternalIP or InternalIP. | N/A |
|  **conditions** | `array` | Conditions defines current service state of the AzureMachine. | N/A |
| └>&nbsp;&nbsp; **lastTransitionTime** | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | N/A |
| └>&nbsp;&nbsp; **message** | `string` | message is a human readable message indicating details about the transition. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **reason** | `string` | reason is the reason for the condition's last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may be empty. | N/A |
| └>&nbsp;&nbsp; **severity** | `string` | severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False. | N/A |
| └>&nbsp;&nbsp; **status** | `string` | status of the condition, one of True, False, Unknown. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | N/A |
|  **failureMessage** | `string` | ErrorMessage will be set in the event that there is a terminal problem reconciling the Machine and will contain a more verbose string suitable for logging and human consumption. This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the Machine's spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured. Any transient errors that occur during the reconciliation of Machines can be added as events to the Machine object and/or logged in the controller's output. | N/A |
|  **failureReason** | `string` | ErrorReason will be set in the event that there is a terminal problem reconciling the Machine and will contain a succinct value suitable for machine interpretation. This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the Machine's spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured. Any transient errors that occur during the reconciliation of Machines can be added as events to the Machine object and/or logged in the controller's output. | N/A |
|  **longRunningOperationStates** | `array` | LongRunningOperationStates saves the states for Azure long-running operations so they can be continued on the next reconciliation loop. | N/A |
| └>&nbsp;&nbsp; **data** | `string` | Data is the base64 url encoded json Azure AutoRest Future. | N/A |
| └>&nbsp;&nbsp; **name** | `string` | Name is the name of the Azure resource. Together with the service name, this forms the unique identifier for the future. | N/A |
| └>&nbsp;&nbsp; **resourceGroup** | `string` | ResourceGroup is the Azure resource group for the resource. | N/A |
| └>&nbsp;&nbsp; **serviceName** | `string` | ServiceName is the name of the Azure service. Together with the name of the resource, this forms the unique identifier for the future. | N/A |
| └>&nbsp;&nbsp; **type** | `string` | Type describes the type of future, such as update, create, delete, etc. | N/A |
|  **ready** | `boolean` | Ready is true when the provider resource is ready. | N/A |
|  **vmState** | `string` | VMState is the provisioning state of the Azure virtual machine. | N/A |
