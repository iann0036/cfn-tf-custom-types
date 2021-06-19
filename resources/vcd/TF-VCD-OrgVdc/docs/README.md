# TF::VCD::OrgVdc

Provides a vCloud Director Organization VDC resource. This can be used to create and delete an Organization VDC.
Requires system administrator privileges.

-> **Note:** This resource supports NSX-T and NSX-V based Org Vdcs by providing relevant
`network_pool_name` and `provider_vdc_name`

Supported in provider *v2.2+*

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VCD::OrgVdc",
    "Properties" : {
        "<a href="#allocationmodel" title="AllocationModel">AllocationModel</a>" : <i>String</i>,
        "<a href="#allowovercommit" title="AllowOverCommit">AllowOverCommit</a>" : <i>Boolean</i>,
        "<a href="#cpuguaranteed" title="CpuGuaranteed">CpuGuaranteed</a>" : <i>Double</i>,
        "<a href="#cpuspeed" title="CpuSpeed">CpuSpeed</a>" : <i>Double</i>,
        "<a href="#defaultvmsizingpolicyid" title="DefaultVmSizingPolicyId">DefaultVmSizingPolicyId</a>" : <i>String</i>,
        "<a href="#deleteforce" title="DeleteForce">DeleteForce</a>" : <i>Boolean</i>,
        "<a href="#deleterecursive" title="DeleteRecursive">DeleteRecursive</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#elasticity" title="Elasticity">Elasticity</a>" : <i>Boolean</i>,
        "<a href="#enablefastprovisioning" title="EnableFastProvisioning">EnableFastProvisioning</a>" : <i>Boolean</i>,
        "<a href="#enablethinprovisioning" title="EnableThinProvisioning">EnableThinProvisioning</a>" : <i>Boolean</i>,
        "<a href="#enablevmdiscovery" title="EnableVmDiscovery">EnableVmDiscovery</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#includevmmemoryoverhead" title="IncludeVmMemoryOverhead">IncludeVmMemoryOverhead</a>" : <i>Boolean</i>,
        "<a href="#memoryguaranteed" title="MemoryGuaranteed">MemoryGuaranteed</a>" : <i>Double</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkpoolname" title="NetworkPoolName">NetworkPoolName</a>" : <i>String</i>,
        "<a href="#networkquota" title="NetworkQuota">NetworkQuota</a>" : <i>Double</i>,
        "<a href="#nicquota" title="NicQuota">NicQuota</a>" : <i>Double</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#providervdcname" title="ProviderVdcName">ProviderVdcName</a>" : <i>String</i>,
        "<a href="#vmquota" title="VmQuota">VmQuota</a>" : <i>Double</i>,
        "<a href="#vmsizingpolicyids" title="VmSizingPolicyIds">VmSizingPolicyIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#computecapacity" title="ComputeCapacity">ComputeCapacity</a>" : <i>[ <a href="computecapacitydefinition.md">ComputeCapacityDefinition</a>, ... ]</i>,
        "<a href="#storageprofile" title="StorageProfile">StorageProfile</a>" : <i>[ <a href="storageprofiledefinition.md">StorageProfileDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VCD::OrgVdc
Properties:
    <a href="#allocationmodel" title="AllocationModel">AllocationModel</a>: <i>String</i>
    <a href="#allowovercommit" title="AllowOverCommit">AllowOverCommit</a>: <i>Boolean</i>
    <a href="#cpuguaranteed" title="CpuGuaranteed">CpuGuaranteed</a>: <i>Double</i>
    <a href="#cpuspeed" title="CpuSpeed">CpuSpeed</a>: <i>Double</i>
    <a href="#defaultvmsizingpolicyid" title="DefaultVmSizingPolicyId">DefaultVmSizingPolicyId</a>: <i>String</i>
    <a href="#deleteforce" title="DeleteForce">DeleteForce</a>: <i>Boolean</i>
    <a href="#deleterecursive" title="DeleteRecursive">DeleteRecursive</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#elasticity" title="Elasticity">Elasticity</a>: <i>Boolean</i>
    <a href="#enablefastprovisioning" title="EnableFastProvisioning">EnableFastProvisioning</a>: <i>Boolean</i>
    <a href="#enablethinprovisioning" title="EnableThinProvisioning">EnableThinProvisioning</a>: <i>Boolean</i>
    <a href="#enablevmdiscovery" title="EnableVmDiscovery">EnableVmDiscovery</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#includevmmemoryoverhead" title="IncludeVmMemoryOverhead">IncludeVmMemoryOverhead</a>: <i>Boolean</i>
    <a href="#memoryguaranteed" title="MemoryGuaranteed">MemoryGuaranteed</a>: <i>Double</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkpoolname" title="NetworkPoolName">NetworkPoolName</a>: <i>String</i>
    <a href="#networkquota" title="NetworkQuota">NetworkQuota</a>: <i>Double</i>
    <a href="#nicquota" title="NicQuota">NicQuota</a>: <i>Double</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#providervdcname" title="ProviderVdcName">ProviderVdcName</a>: <i>String</i>
    <a href="#vmquota" title="VmQuota">VmQuota</a>: <i>Double</i>
    <a href="#vmsizingpolicyids" title="VmSizingPolicyIds">VmSizingPolicyIds</a>: <i>
      - String</i>
    <a href="#computecapacity" title="ComputeCapacity">ComputeCapacity</a>: <i>
      - <a href="computecapacitydefinition.md">ComputeCapacityDefinition</a></i>
    <a href="#storageprofile" title="StorageProfile">StorageProfile</a>: <i>
      - <a href="storageprofiledefinition.md">StorageProfileDefinition</a></i>
</pre>

## Properties

#### AllocationModel

The allocation model used by this VDC; must be one of
* AllocationVApp ("Pay as you go")
* AllocationPool ("Allocation pool")
* ReservationPool ("Reservation pool")
* Flex ("Flex") (*v2.7+*, *vCD 9.7+*).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowOverCommit

Set to false to disallow creation of the VDC if the `allocation_model` is AllocationPool or ReservationPool and the ComputeCapacity you specified is greater than what the backing Provider VDC can supply. Default is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuGuaranteed

Percentage of allocated CPU resources guaranteed to vApps deployed in this VDC. For example, if this value is 0.75, then 75% of allocated resources are guaranteed. Required when `allocation_model` is AllocationVApp, AllocationPool or Flex. If left empty, vCD sets a value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuSpeed

Specifies the clock frequency, in Megahertz, for any virtual CPU that is allocated to a VM. A VM with 2 vCPUs will consume twice as much of this value. Ignored for ReservationPool. Required when `allocation_model` is AllocationVApp, AllocationPool or Flex, and may not be less than 256 MHz. Defaults to 1000 MHz if value isn't provided.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultVmSizingPolicyId

Set of VM sizing policy IDs. This field requires `vm_sizing_policy_ids` to be configured together.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteForce

When destroying use `delete_force=True` to remove a VDC and any objects it contains, regardless of their state.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteRecursive

When destroying use `delete_recursive=True` to remove the VDC and any objects it contains that are in a state that normally allows removal.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

VDC friendly description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Elasticity

Indicates if the Flex VDC should be elastic. Required with the Flex allocation model.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableFastProvisioning

Request fast provisioning. Request will be honored only if the underlying datastore supports it. Fast provisioning can reduce the time it takes to create virtual machines by using vSphere linked clones. If you disable fast provisioning, all provisioning operations will result in full clones.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableThinProvisioning

Boolean to request thin provisioning. Request will be honored only if the underlying data store supports it. Thin provisioning saves storage space by committing it on demand. This allows over-allocation of storage.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableVmDiscovery

If true, discovery of vCenter VMs is enabled for resource pools backing this VDC. If false, discovery is disabled. If left unspecified, the actual behaviour depends on enablement at the organization level and at the system level.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

True if this VDC is enabled for use by the organization VDCs. Default is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeVmMemoryOverhead

Indicates if the Flex VDC should include memory overhead into its accounting for admission control. Required with the Flex allocation model.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryGuaranteed

Percentage of allocated memory resources guaranteed to vApps deployed in this VDC. For example, if this value is 0.75, then 75% of allocated resources are guaranteed. Required when `allocation_model` is AllocationVApp, AllocationPool or Flex. When Allocation model is AllocationPool minimum value is 0.2. If left empty, vCD sets a value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

Key value map of metadata to assign to this VDC.

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

VDC name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPoolName

Reference to a network pool in the Provider VDC. Required if this VDC will contain routed or isolated networks.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkQuota

Maximum number of network objects that can be deployed in this VDC. Defaults to 0, which means no networks can be deployed.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NicQuota

Maximum number of virtual NICs allowed in this VDC. Defaults to 0, which specifies an unlimited number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

Organization to create the VDC in, optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderVdcName

Name of the Provider VDC from which this organization VDC is provisioned.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmQuota

The maximum number of VMs that can be created in this VDC. Includes deployed and undeployed VMs in vApps and vApp templates. Defaults to 0, which specifies an unlimited number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmSizingPolicyIds

Default VM sizing policy ID. This field requires `default_vm_sizing_policy_id` to be configured together.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputeCapacity

_Required_: No

_Type_: List of <a href="computecapacitydefinition.md">ComputeCapacityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProfile

_Required_: No

_Type_: List of <a href="storageprofiledefinition.md">StorageProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

