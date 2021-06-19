# TF::TencentCloud::Instance DataDisksDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#datadiskid" title="DataDiskId">DataDiskId</a>" : <i>String</i>,
    "<a href="#datadisksize" title="DataDiskSize">DataDiskSize</a>" : <i>Double</i>,
    "<a href="#datadisksnapshotid" title="DataDiskSnapshotId">DataDiskSnapshotId</a>" : <i>String</i>,
    "<a href="#datadisktype" title="DataDiskType">DataDiskType</a>" : <i>String</i>,
    "<a href="#deletewithinstance" title="DeleteWithInstance">DeleteWithInstance</a>" : <i>Boolean</i>,
    "<a href="#encrypt" title="Encrypt">Encrypt</a>" : <i>Boolean</i>,
    "<a href="#throughputperformance" title="ThroughputPerformance">ThroughputPerformance</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#datadiskid" title="DataDiskId">DataDiskId</a>: <i>String</i>
<a href="#datadisksize" title="DataDiskSize">DataDiskSize</a>: <i>Double</i>
<a href="#datadisksnapshotid" title="DataDiskSnapshotId">DataDiskSnapshotId</a>: <i>String</i>
<a href="#datadisktype" title="DataDiskType">DataDiskType</a>: <i>String</i>
<a href="#deletewithinstance" title="DeleteWithInstance">DeleteWithInstance</a>: <i>Boolean</i>
<a href="#encrypt" title="Encrypt">Encrypt</a>: <i>Boolean</i>
<a href="#throughputperformance" title="ThroughputPerformance">ThroughputPerformance</a>: <i>Double</i>
</pre>

## Properties

#### DataDiskId

Data disk ID used to initialize the data disk. When data disk type is `LOCAL_BASIC` and `LOCAL_SSD`, disk id is not supported.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDiskSize

Size of the data disk, and unit is GB. If disk type is `CLOUD_SSD`, the size range is [100, 16000], and the others are [10-16000].

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDiskSnapshotId

Snapshot ID of the data disk. The selected data disk snapshot size must be smaller than the data disk size.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDiskType

Data disk type. For more information about limits on different data disk types, see [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952). Valid values: `LOCAL_BASIC`: local disk, `LOCAL_SSD`: local SSD disk, `CLOUD_BASIC`: HDD cloud disk, `CLOUD_PREMIUM`: Premium Cloud Storage, `CLOUD_SSD`: SSD, `CLOUD_HSSD`: Enhanced SSD. NOTE: `LOCAL_BASIC` and `LOCAL_SSD` are deprecated.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteWithInstance

Decides whether the disk is deleted with instance(only applied to `CLOUD_BASIC`, `CLOUD_SSD` and `CLOUD_PREMIUM` disk with `POSTPAID_BY_HOUR` instance), default is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encrypt

Decides whether the disk is encrypted. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThroughputPerformance

Add extra performance to the data disk. Only works when disk type is `CLOUD_TSSD` or `CLOUD_HSSD`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

