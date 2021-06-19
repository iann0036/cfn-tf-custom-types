# TF::AVI::Cloud LinuxserverConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#seinbandmgmt" title="SeInbandMgmt">SeInbandMgmt</a>" : <i>Boolean</i>,
    "<a href="#selogdiskpath" title="SeLogDiskPath">SeLogDiskPath</a>" : <i>String</i>,
    "<a href="#selogdisksizegb" title="SeLogDiskSizeGb">SeLogDiskSizeGb</a>" : <i>Double</i>,
    "<a href="#sesysdiskpath" title="SeSysDiskPath">SeSysDiskPath</a>" : <i>String</i>,
    "<a href="#sesysdisksizegb" title="SeSysDiskSizeGb">SeSysDiskSizeGb</a>" : <i>Double</i>,
    "<a href="#sshuserref" title="SshUserRef">SshUserRef</a>" : <i>String</i>,
    "<a href="#hosts" title="Hosts">Hosts</a>" : <i>[ <a href="hostsdefinition.md">HostsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#seinbandmgmt" title="SeInbandMgmt">SeInbandMgmt</a>: <i>Boolean</i>
<a href="#selogdiskpath" title="SeLogDiskPath">SeLogDiskPath</a>: <i>String</i>
<a href="#selogdisksizegb" title="SeLogDiskSizeGb">SeLogDiskSizeGb</a>: <i>Double</i>
<a href="#sesysdiskpath" title="SeSysDiskPath">SeSysDiskPath</a>: <i>String</i>
<a href="#sesysdisksizegb" title="SeSysDiskSizeGb">SeSysDiskSizeGb</a>: <i>Double</i>
<a href="#sshuserref" title="SshUserRef">SshUserRef</a>: <i>String</i>
<a href="#hosts" title="Hosts">Hosts</a>: <i>
      - <a href="hostsdefinition.md">HostsDefinition</a></i>
</pre>

## Properties

#### SeInbandMgmt

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLogDiskPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLogDiskSizeGb

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeSysDiskPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeSysDiskSizeGb

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshUserRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hosts

_Required_: No

_Type_: List of <a href="hostsdefinition.md">HostsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

