# TF::Anxcloud::VirtualServer

CloudFormation equivalent of anxcloud_virtual_server

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Anxcloud::VirtualServer",
    "Properties" : {
        "<a href="#bootdelay" title="BootDelay">BootDelay</a>" : <i>Double</i>,
        "<a href="#cpuperformancetype" title="CpuPerformanceType">CpuPerformanceType</a>" : <i>String</i>,
        "<a href="#cpus" title="Cpus">Cpus</a>" : <i>Double</i>,
        "<a href="#criticaloperationconfirmed" title="CriticalOperationConfirmed">CriticalOperationConfirmed</a>" : <i>Boolean</i>,
        "<a href="#dns" title="Dns">Dns</a>" : <i>[ String, ... ]</i>,
        "<a href="#enterbiossetup" title="EnterBiosSetup">EnterBiosSetup</a>" : <i>Boolean</i>,
        "<a href="#forcerestartifneeded" title="ForceRestartIfNeeded">ForceRestartIfNeeded</a>" : <i>Boolean</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#locationid" title="LocationId">LocationId</a>" : <i>String</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#script" title="Script">Script</a>" : <i>String</i>,
        "<a href="#sockets" title="Sockets">Sockets</a>" : <i>Double</i>,
        "<a href="#sshkey" title="SshKey">SshKey</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#templateid" title="TemplateId">TemplateId</a>" : <i>String</i>,
        "<a href="#templatetype" title="TemplateType">TemplateType</a>" : <i>String</i>,
        "<a href="#disk" title="Disk">Disk</a>" : <i>[ <a href="diskdefinition.md">DiskDefinition</a>, ... ]</i>,
        "<a href="#network" title="Network">Network</a>" : <i>[ <a href="infodefinition2.md">InfoDefinition2</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Anxcloud::VirtualServer
Properties:
    <a href="#bootdelay" title="BootDelay">BootDelay</a>: <i>Double</i>
    <a href="#cpuperformancetype" title="CpuPerformanceType">CpuPerformanceType</a>: <i>String</i>
    <a href="#cpus" title="Cpus">Cpus</a>: <i>Double</i>
    <a href="#criticaloperationconfirmed" title="CriticalOperationConfirmed">CriticalOperationConfirmed</a>: <i>Boolean</i>
    <a href="#dns" title="Dns">Dns</a>: <i>
      - String</i>
    <a href="#enterbiossetup" title="EnterBiosSetup">EnterBiosSetup</a>: <i>Boolean</i>
    <a href="#forcerestartifneeded" title="ForceRestartIfNeeded">ForceRestartIfNeeded</a>: <i>Boolean</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#locationid" title="LocationId">LocationId</a>: <i>String</i>
    <a href="#memory" title="Memory">Memory</a>: <i>Double</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#script" title="Script">Script</a>: <i>String</i>
    <a href="#sockets" title="Sockets">Sockets</a>: <i>Double</i>
    <a href="#sshkey" title="SshKey">SshKey</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#templateid" title="TemplateId">TemplateId</a>: <i>String</i>
    <a href="#templatetype" title="TemplateType">TemplateType</a>: <i>String</i>
    <a href="#disk" title="Disk">Disk</a>: <i>
      - <a href="diskdefinition.md">DiskDefinition</a></i>
    <a href="#network" title="Network">Network</a>: <i>
      - <a href="infodefinition2.md">InfoDefinition2</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### BootDelay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuPerformanceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpus

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CriticalOperationConfirmed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnterBiosSetup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceRestartIfNeeded

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocationId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Script

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sockets

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disk

_Required_: No

_Type_: List of <a href="diskdefinition.md">DiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="infodefinition2.md">InfoDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### Info

Returns the <code>Info</code> value.

