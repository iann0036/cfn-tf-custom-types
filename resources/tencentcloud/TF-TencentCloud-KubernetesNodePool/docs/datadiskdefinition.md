# TF::TencentCloud::KubernetesNodePool DataDiskDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoformatandmount" title="AutoFormatAndMount">AutoFormatAndMount</a>" : <i>Boolean</i>,
    "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>Double</i>,
    "<a href="#disktype" title="DiskType">DiskType</a>" : <i>String</i>,
    "<a href="#filesystem" title="FileSystem">FileSystem</a>" : <i>String</i>,
    "<a href="#mounttarget" title="MountTarget">MountTarget</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#autoformatandmount" title="AutoFormatAndMount">AutoFormatAndMount</a>: <i>Boolean</i>
<a href="#disksize" title="DiskSize">DiskSize</a>: <i>Double</i>
<a href="#disktype" title="DiskType">DiskType</a>: <i>String</i>
<a href="#filesystem" title="FileSystem">FileSystem</a>: <i>String</i>
<a href="#mounttarget" title="MountTarget">MountTarget</a>: <i>String</i>
</pre>

## Properties

#### AutoFormatAndMount

Indicate whether to auto format and mount or not. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSize

Volume of disk in GB. Default is `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskType

Types of disk. Valid value: `CLOUD_PREMIUM` and `CLOUD_SSD`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileSystem

File system, e.g. `ext3/ext4/xfs`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountTarget

Mount target.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

