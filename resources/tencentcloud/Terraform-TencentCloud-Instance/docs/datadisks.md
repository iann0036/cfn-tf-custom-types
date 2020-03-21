# Terraform::TencentCloud::Instance DataDisks

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#datadiskid" title="DataDiskId">DataDiskId</a>" : <i>String</i>,
    "<a href="#datadisksize" title="DataDiskSize">DataDiskSize</a>" : <i>Double</i>,
    "<a href="#datadisktype" title="DataDiskType">DataDiskType</a>" : <i>String</i>,
    "<a href="#deletewithinstance" title="DeleteWithInstance">DeleteWithInstance</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#datadiskid" title="DataDiskId">DataDiskId</a>: <i>String</i>
<a href="#datadisksize" title="DataDiskSize">DataDiskSize</a>: <i>Double</i>
<a href="#datadisktype" title="DataDiskType">DataDiskType</a>: <i>String</i>
<a href="#deletewithinstance" title="DeleteWithInstance">DeleteWithInstance</a>: <i>Boolean</i>
</pre>

## Properties

#### DataDiskId

Data disk snapshot ID used to initialize the data disk. When data disk type is `LOCAL_BASIC` and `LOCAL_SSD`, disk id is not supported.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDiskSize

Size of the data disk, and unit is GB. If disk type is `CLOUD_SSD`, the size range is [100, 16000], and the others are [10-16000].

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDiskType

Type of the data disk. Valid values are `LOCAL_BASIC`, `LOCAL_SSD`, `CLOUD_BASIC`, `CLOUD_SSD` and `CLOUD_PREMIUM`. NOTE: `LOCAL_BASIC` and `LOCAL_SSD` are deprecated.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteWithInstance

Decides whether the disk is deleted with instance(only applied to cloud disk), default to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

