# Terraform::VCD::OrgVdc

CloudFormation equivalent of vcd_org_vdc

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VCD::OrgVdc",
    "Properties" : {
        "<a href="#allocationmodel" title="AllocationModel">AllocationModel</a>" : <i>String</i>,
        "<a href="#allowovercommit" title="AllowOverCommit">AllowOverCommit</a>" : <i>Boolean</i>,
        "<a href="#cpuguaranteed" title="CpuGuaranteed">CpuGuaranteed</a>" : <i>Double</i>,
        "<a href="#cpuspeed" title="CpuSpeed">CpuSpeed</a>" : <i>Double</i>,
        "<a href="#deleteforce" title="DeleteForce">DeleteForce</a>" : <i>Boolean</i>,
        "<a href="#deleterecursive" title="DeleteRecursive">DeleteRecursive</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#elasticity" title="Elasticity">Elasticity</a>" : <i>Boolean</i>,
        "<a href="#enablefastprovisioning" title="EnableFastProvisioning">EnableFastProvisioning</a>" : <i>Boolean</i>,
        "<a href="#enablethinprovisioning" title="EnableThinProvisioning">EnableThinProvisioning</a>" : <i>Boolean</i>,
        "<a href="#enablevmdiscovery" title="EnableVmDiscovery">EnableVmDiscovery</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#includevmmemoryoverhead" title="IncludeVmMemoryOverhead">IncludeVmMemoryOverhead</a>" : <i>Boolean</i>,
        "<a href="#memoryguaranteed" title="MemoryGuaranteed">MemoryGuaranteed</a>" : <i>Double</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkpoolname" title="NetworkPoolName">NetworkPoolName</a>" : <i>String</i>,
        "<a href="#networkquota" title="NetworkQuota">NetworkQuota</a>" : <i>Double</i>,
        "<a href="#nicquota" title="NicQuota">NicQuota</a>" : <i>Double</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#providervdcname" title="ProviderVdcName">ProviderVdcName</a>" : <i>String</i>,
        "<a href="#vmquota" title="VmQuota">VmQuota</a>" : <i>Double</i>,
        "<a href="#computecapacity" title="ComputeCapacity">ComputeCapacity</a>" : <i>[ &lt;a href=&#34;computecapacity.md&#34;&gt;ComputeCapacity&lt;/a&gt;, ... ]</i>,
        "<a href="#storageprofile" title="StorageProfile">StorageProfile</a>" : <i>[ &lt;a href=&#34;storageprofile.md&#34;&gt;StorageProfile&lt;/a&gt;, ... ]</i>,
        "<a href="#cpu" title="Cpu">Cpu</a>" : <i>[ &lt;a href=&#34;cpu.md&#34;&gt;Cpu&lt;/a&gt;, ... ]</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>[ &lt;a href=&#34;memory.md&#34;&gt;Memory&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VCD::OrgVdc
Properties:
    <a href="#allocationmodel" title="AllocationModel">AllocationModel</a>: <i>String</i>
    <a href="#allowovercommit" title="AllowOverCommit">AllowOverCommit</a>: <i>Boolean</i>
    <a href="#cpuguaranteed" title="CpuGuaranteed">CpuGuaranteed</a>: <i>Double</i>
    <a href="#cpuspeed" title="CpuSpeed">CpuSpeed</a>: <i>Double</i>
    <a href="#deleteforce" title="DeleteForce">DeleteForce</a>: <i>Boolean</i>
    <a href="#deleterecursive" title="DeleteRecursive">DeleteRecursive</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#elasticity" title="Elasticity">Elasticity</a>: <i>Boolean</i>
    <a href="#enablefastprovisioning" title="EnableFastProvisioning">EnableFastProvisioning</a>: <i>Boolean</i>
    <a href="#enablethinprovisioning" title="EnableThinProvisioning">EnableThinProvisioning</a>: <i>Boolean</i>
    <a href="#enablevmdiscovery" title="EnableVmDiscovery">EnableVmDiscovery</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#includevmmemoryoverhead" title="IncludeVmMemoryOverhead">IncludeVmMemoryOverhead</a>: <i>Boolean</i>
    <a href="#memoryguaranteed" title="MemoryGuaranteed">MemoryGuaranteed</a>: <i>Double</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkpoolname" title="NetworkPoolName">NetworkPoolName</a>: <i>String</i>
    <a href="#networkquota" title="NetworkQuota">NetworkQuota</a>: <i>Double</i>
    <a href="#nicquota" title="NicQuota">NicQuota</a>: <i>Double</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#providervdcname" title="ProviderVdcName">ProviderVdcName</a>: <i>String</i>
    <a href="#vmquota" title="VmQuota">VmQuota</a>: <i>Double</i>
    <a href="#computecapacity" title="ComputeCapacity">ComputeCapacity</a>: <i>
      - &lt;a href=&#34;computecapacity.md&#34;&gt;ComputeCapacity&lt;/a&gt;</i>
    <a href="#storageprofile" title="StorageProfile">StorageProfile</a>: <i>
      - &lt;a href=&#34;storageprofile.md&#34;&gt;StorageProfile&lt;/a&gt;</i>
    <a href="#cpu" title="Cpu">Cpu</a>: <i>
      - &lt;a href=&#34;cpu.md&#34;&gt;Cpu&lt;/a&gt;</i>
    <a href="#memory" title="Memory">Memory</a>: <i>
      - &lt;a href=&#34;memory.md&#34;&gt;Memory&lt;/a&gt;</i>
</pre>

## Properties

#### AllocationModel

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowOverCommit

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuGuaranteed

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuSpeed

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteForce

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteRecursive

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Elasticity

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableFastProvisioning

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableThinProvisioning

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableVmDiscovery

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeVmMemoryOverhead

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryGuaranteed

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPoolName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkQuota

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NicQuota

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderVdcName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmQuota

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputeCapacity

_Required_: No

_Type_: List of &lt;a href=&#34;computecapacity.md&#34;&gt;ComputeCapacity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProfile

_Required_: No

_Type_: List of &lt;a href=&#34;storageprofile.md&#34;&gt;StorageProfile&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpu

_Required_: No

_Type_: List of &lt;a href=&#34;cpu.md&#34;&gt;Cpu&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: No

_Type_: List of &lt;a href=&#34;memory.md&#34;&gt;Memory&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

