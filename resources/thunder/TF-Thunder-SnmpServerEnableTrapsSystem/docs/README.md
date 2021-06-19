# TF::Thunder::SnmpServerEnableTrapsSystem

`thunder_snmp_server_enable_traps_system` Provides details about thunder snmp server enable traps system

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SnmpServerEnableTrapsSystem",
    "Properties" : {
        "<a href="#all" title="All">All</a>" : <i>Double</i>,
        "<a href="#controlcpuhigh" title="ControlCpuHigh">ControlCpuHigh</a>" : <i>Double</i>,
        "<a href="#datacpuhigh" title="DataCpuHigh">DataCpuHigh</a>" : <i>Double</i>,
        "<a href="#fan" title="Fan">Fan</a>" : <i>Double</i>,
        "<a href="#filesysreadonly" title="FileSysReadOnly">FileSysReadOnly</a>" : <i>Double</i>,
        "<a href="#highdiskuse" title="HighDiskUse">HighDiskUse</a>" : <i>Double</i>,
        "<a href="#highmemoryuse" title="HighMemoryUse">HighMemoryUse</a>" : <i>Double</i>,
        "<a href="#hightemp" title="HighTemp">HighTemp</a>" : <i>Double</i>,
        "<a href="#licensemanagement" title="LicenseManagement">LicenseManagement</a>" : <i>Double</i>,
        "<a href="#lowtemp" title="LowTemp">LowTemp</a>" : <i>Double</i>,
        "<a href="#packetdrop" title="PacketDrop">PacketDrop</a>" : <i>Double</i>,
        "<a href="#power" title="Power">Power</a>" : <i>Double</i>,
        "<a href="#pridisk" title="PriDisk">PriDisk</a>" : <i>Double</i>,
        "<a href="#restart" title="Restart">Restart</a>" : <i>Double</i>,
        "<a href="#secdisk" title="SecDisk">SecDisk</a>" : <i>Double</i>,
        "<a href="#shutdown" title="Shutdown">Shutdown</a>" : <i>Double</i>,
        "<a href="#smpresourceevent" title="SmpResourceEvent">SmpResourceEvent</a>" : <i>Double</i>,
        "<a href="#start" title="Start">Start</a>" : <i>Double</i>,
        "<a href="#syslogseverityone" title="SyslogSeverityOne">SyslogSeverityOne</a>" : <i>Double</i>,
        "<a href="#tacacsserverupdown" title="TacacsServerUpDown">TacacsServerUpDown</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SnmpServerEnableTrapsSystem
Properties:
    <a href="#all" title="All">All</a>: <i>Double</i>
    <a href="#controlcpuhigh" title="ControlCpuHigh">ControlCpuHigh</a>: <i>Double</i>
    <a href="#datacpuhigh" title="DataCpuHigh">DataCpuHigh</a>: <i>Double</i>
    <a href="#fan" title="Fan">Fan</a>: <i>Double</i>
    <a href="#filesysreadonly" title="FileSysReadOnly">FileSysReadOnly</a>: <i>Double</i>
    <a href="#highdiskuse" title="HighDiskUse">HighDiskUse</a>: <i>Double</i>
    <a href="#highmemoryuse" title="HighMemoryUse">HighMemoryUse</a>: <i>Double</i>
    <a href="#hightemp" title="HighTemp">HighTemp</a>: <i>Double</i>
    <a href="#licensemanagement" title="LicenseManagement">LicenseManagement</a>: <i>Double</i>
    <a href="#lowtemp" title="LowTemp">LowTemp</a>: <i>Double</i>
    <a href="#packetdrop" title="PacketDrop">PacketDrop</a>: <i>Double</i>
    <a href="#power" title="Power">Power</a>: <i>Double</i>
    <a href="#pridisk" title="PriDisk">PriDisk</a>: <i>Double</i>
    <a href="#restart" title="Restart">Restart</a>: <i>Double</i>
    <a href="#secdisk" title="SecDisk">SecDisk</a>: <i>Double</i>
    <a href="#shutdown" title="Shutdown">Shutdown</a>: <i>Double</i>
    <a href="#smpresourceevent" title="SmpResourceEvent">SmpResourceEvent</a>: <i>Double</i>
    <a href="#start" title="Start">Start</a>: <i>Double</i>
    <a href="#syslogseverityone" title="SyslogSeverityOne">SyslogSeverityOne</a>: <i>Double</i>
    <a href="#tacacsserverupdown" title="TacacsServerUpDown">TacacsServerUpDown</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### All

Enable all system group traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControlCpuHigh

Enable control CPU usage high trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataCpuHigh

Enable data CPU usage high trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fan

Enable system fan trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileSysReadOnly

Enable file system read-only trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HighDiskUse

Enable system high disk usage trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HighMemoryUse

Enable system high memory usage trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HighTemp

Enable system high temperature trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseManagement

Enable system license management traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LowTemp

Enable system low temperature trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketDrop

Enable system packet dropped trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Power

Enable system power supply trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PriDisk

Enable system primary hard disk trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restart

Enable system restart trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecDisk

Enable system secondary hard disk trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shutdown

Enable system shutdown trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmpResourceEvent

Enable system smp resource event trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Start

Enable system start trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyslogSeverityOne

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TacacsServerUpDown

Enable system TACACS monitor server up/down trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

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

