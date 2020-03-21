# Terraform::FlexibleEngine::AsConfigurationV1 Disk

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disktype" title="DiskType">DiskType</a>" : <i>String</i>,
    "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
    "<a href="#volumetype" title="VolumeType">VolumeType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#disktype" title="DiskType">DiskType</a>: <i>String</i>
<a href="#size" title="Size">Size</a>: <i>Double</i>
<a href="#volumetype" title="VolumeType">VolumeType</a>: <i>String</i>
</pre>

## Properties

#### DiskType

Whether the disk is a system disk or a data disk. Option `DATA` indicates
a data disk. option `SYS` indicates a system disk.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The disk size. The unit is GB. The system disk size ranges from 1 to 32768,
and the data disk size ranges from 10 to 32768.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeType

The disk type, which must be the same as the disk type available in the system.
The options include `SATA` (common I/O disk type) and `SSD` (ultra-high I/O disk type).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

