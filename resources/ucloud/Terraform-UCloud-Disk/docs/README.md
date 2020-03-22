# Terraform::UCloud::Disk

Provides a Cloud Disk resource.

~> **Note** If the disk have attached to the instance, the instance will reboot automatically to make the change take effect when update the  `disk_size`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::UCloud::Disk",
    "Properties" : {
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#chargetype" title="ChargeType">ChargeType</a>" : <i>String</i>,
        "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>Double</i>,
        "<a href="#disktype" title="DiskType">DiskType</a>" : <i>String</i>,
        "<a href="#duration" title="Duration">Duration</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::UCloud::Disk
Properties:
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#chargetype" title="ChargeType">ChargeType</a>: <i>String</i>
    <a href="#disksize" title="DiskSize">DiskSize</a>: <i>Double</i>
    <a href="#disktype" title="DiskType">DiskType</a>: <i>String</i>
    <a href="#duration" title="Duration">Duration</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tag" title="Tag">Tag</a>: <i>String</i>
</pre>

## Properties

#### AvailabilityZone

Availability zone where cloud disk is located. Such as: "cn-bj2-02". You may refer to [list of availability zone](https://docs.ucloud.cn/api/summary/regionlist).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChargeType

Charge type of disk. Possible values are: `year` as pay by year, `month` as pay by month, `dynamic` as pay by hour. (Default: `month`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSize

The size of disk. Purchase the size of disk in GB. 1-8000 for a cloud disk, 1-4000 for SSD cloud disk. If the disk have attached to the instance, the instance will reboot automatically to make the change take effect when update the  `disk_size`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskType

The type of disk. Possible values are: `data_disk`as cloud disk, `ssd_data_disk` as ssd cloud disk, `rssd_data_disk` as RDMA-SSD cloud disk (the `rssd_data_disk` only be supported in `cn-bj2-05`).(Default: `data_disk`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

The duration that you will buy the resource. (Default: `1`). It is not required when `dynamic` (pay by hour), the value is `0` when `month`(pay by month) and the disk will be vaild till the last day of that month.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of disk, should have 6-63 characters and only support Chinese, English, numbers, '-', '_'. If not specified, terraform will auto-generate a name beginning with `tf-disk`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

A tag assigned to VPC, which contains at most 63 characters and only support Chinese, English, numbers, '-', '_', and '.'. If it is not filled in or a empty string is filled in, then default tag will be assigned. (Default: `Default`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### ExpireTime

Returns the <code>ExpireTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

