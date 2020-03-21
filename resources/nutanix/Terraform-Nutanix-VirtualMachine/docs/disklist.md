# Terraform::Nutanix::VirtualMachine DiskList

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#datasourcereference" title="DataSourceReference">DataSourceReference</a>" : <i>[ <a href="disklist-datasourcereference.md">DataSourceReference</a>, ... ]</i>,
    "<a href="#disksizebytes" title="DiskSizeBytes">DiskSizeBytes</a>" : <i>Double</i>,
    "<a href="#disksizemib" title="DiskSizeMib">DiskSizeMib</a>" : <i>Double</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#volumegroupreference" title="VolumeGroupReference">VolumeGroupReference</a>" : <i>[ <a href="disklist-volumegroupreference.md">VolumeGroupReference</a>, ... ]</i>,
    "<a href="#deviceproperties" title="DeviceProperties">DeviceProperties</a>" : <i>[ <a href="disklist-deviceproperties.md">DeviceProperties</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#datasourcereference" title="DataSourceReference">DataSourceReference</a>: <i>
      - <a href="disklist-datasourcereference.md">DataSourceReference</a></i>
<a href="#disksizebytes" title="DiskSizeBytes">DiskSizeBytes</a>: <i>Double</i>
<a href="#disksizemib" title="DiskSizeMib">DiskSizeMib</a>: <i>Double</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#volumegroupreference" title="VolumeGroupReference">VolumeGroupReference</a>: <i>
      - <a href="disklist-volumegroupreference.md">VolumeGroupReference</a></i>
<a href="#deviceproperties" title="DeviceProperties">DeviceProperties</a>: <i>
      - <a href="disklist-deviceproperties.md">DeviceProperties</a></i>
</pre>

## Properties

#### DataSourceReference

_Required_: No

_Type_: List of <a href="disklist-datasourcereference.md">DataSourceReference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSizeBytes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSizeMib

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeGroupReference

_Required_: No

_Type_: List of <a href="disklist-volumegroupreference.md">VolumeGroupReference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceProperties

_Required_: No

_Type_: List of <a href="disklist-deviceproperties.md">DeviceProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

