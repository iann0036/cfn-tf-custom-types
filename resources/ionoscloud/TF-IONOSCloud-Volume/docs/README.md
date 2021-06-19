# TF::IONOSCloud::Volume

Manages a volume on IonosCloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::IONOSCloud::Volume",
    "Properties" : {
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#backupunitid" title="BackupUnitId">BackupUnitId</a>" : <i>String</i>,
        "<a href="#bus" title="Bus">Bus</a>" : <i>String</i>,
        "<a href="#cpuhotplug" title="CpuHotPlug">CpuHotPlug</a>" : <i>Boolean</i>,
        "<a href="#datacenterid" title="DatacenterId">DatacenterId</a>" : <i>String</i>,
        "<a href="#discvirtiohotplug" title="DiscVirtioHotPlug">DiscVirtioHotPlug</a>" : <i>Boolean</i>,
        "<a href="#discvirtiohotunplug" title="DiscVirtioHotUnplug">DiscVirtioHotUnplug</a>" : <i>Boolean</i>,
        "<a href="#disktype" title="DiskType">DiskType</a>" : <i>String</i>,
        "<a href="#imagename" title="ImageName">ImageName</a>" : <i>String</i>,
        "<a href="#imagepassword" title="ImagePassword">ImagePassword</a>" : <i>String</i>,
        "<a href="#licencetype" title="LicenceType">LicenceType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nichotplug" title="NicHotPlug">NicHotPlug</a>" : <i>Boolean</i>,
        "<a href="#nichotunplug" title="NicHotUnplug">NicHotUnplug</a>" : <i>Boolean</i>,
        "<a href="#ramhotplug" title="RamHotPlug">RamHotPlug</a>" : <i>Boolean</i>,
        "<a href="#serverid" title="ServerId">ServerId</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#sshkeypath" title="SshKeyPath">SshKeyPath</a>" : <i>[ String, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::IONOSCloud::Volume
Properties:
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#backupunitid" title="BackupUnitId">BackupUnitId</a>: <i>String</i>
    <a href="#bus" title="Bus">Bus</a>: <i>String</i>
    <a href="#cpuhotplug" title="CpuHotPlug">CpuHotPlug</a>: <i>Boolean</i>
    <a href="#datacenterid" title="DatacenterId">DatacenterId</a>: <i>String</i>
    <a href="#discvirtiohotplug" title="DiscVirtioHotPlug">DiscVirtioHotPlug</a>: <i>Boolean</i>
    <a href="#discvirtiohotunplug" title="DiscVirtioHotUnplug">DiscVirtioHotUnplug</a>: <i>Boolean</i>
    <a href="#disktype" title="DiskType">DiskType</a>: <i>String</i>
    <a href="#imagename" title="ImageName">ImageName</a>: <i>String</i>
    <a href="#imagepassword" title="ImagePassword">ImagePassword</a>: <i>String</i>
    <a href="#licencetype" title="LicenceType">LicenceType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nichotplug" title="NicHotPlug">NicHotPlug</a>: <i>Boolean</i>
    <a href="#nichotunplug" title="NicHotUnplug">NicHotUnplug</a>: <i>Boolean</i>
    <a href="#ramhotplug" title="RamHotPlug">RamHotPlug</a>: <i>Boolean</i>
    <a href="#serverid" title="ServerId">ServerId</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#sshkeypath" title="SshKeyPath">SshKeyPath</a>: <i>
      - String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AvailabilityZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupUnitId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuHotPlug

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatacenterId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiscVirtioHotPlug

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiscVirtioHotUnplug

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImagePassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NicHotPlug

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NicHotUnplug

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RamHotPlug

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeyPath

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

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

#### Sshkey

Returns the <code>Sshkey</code> value.

