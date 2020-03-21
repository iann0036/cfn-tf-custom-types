# Terraform::Alicloud::Disk

Provides a ECS disk resource.

-> **NOTE:** One of `size` or `snapshot_id` is required when specifying an ECS disk. If all of them be specified, `size` must more than the size of snapshot which `snapshot_id` represents. Currently, `alicloud_disk` doesn't resize disk.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::Disk",
    "Properties" : {
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#category" title="Category">Category</a>" : <i>String</i>,
        "<a href="#deleteautosnapshot" title="DeleteAutoSnapshot">DeleteAutoSnapshot</a>" : <i>Boolean</i>,
        "<a href="#deletewithinstance" title="DeleteWithInstance">DeleteWithInstance</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enableautosnapshot" title="EnableAutoSnapshot">EnableAutoSnapshot</a>" : <i>Boolean</i>,
        "<a href="#encrypted" title="Encrypted">Encrypted</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#snapshotid" title="SnapshotId">SnapshotId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::Disk
Properties:
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#category" title="Category">Category</a>: <i>String</i>
    <a href="#deleteautosnapshot" title="DeleteAutoSnapshot">DeleteAutoSnapshot</a>: <i>Boolean</i>
    <a href="#deletewithinstance" title="DeleteWithInstance">DeleteWithInstance</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enableautosnapshot" title="EnableAutoSnapshot">EnableAutoSnapshot</a>: <i>Boolean</i>
    <a href="#encrypted" title="Encrypted">Encrypted</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#snapshotid" title="SnapshotId">SnapshotId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
</pre>

## Properties

#### AvailabilityZone

The Zone to create the disk in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Category

Category of the disk. Valid values are `cloud`, `cloud_efficiency`, `cloud_ssd`, `cloud_essd`. Default is `cloud_efficiency`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteAutoSnapshot

Indicates whether the automatic snapshot is deleted when the disk is released. Default value: false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteWithInstance

Indicates whether the disk is released together with the instance: Default value: false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the disk. This description can have a string of 2 to 256 characters, It cannot begin with http:// or https://. Default value is null.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutoSnapshot

Indicates whether to apply a created automatic snapshot policy to the disk. Default value: false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encrypted

If true, the disk will be encrypted, conflict with `snapshot_id`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the ECS disk. This name can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin or end with a hyphen, and must not begin with http:// or https://. Default value is null.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

The Id of resource group which the disk belongs.
-> **NOTE:** Disk category `cloud` has been outdated and it only can be used none I/O Optimized ECS instances. Recommend `cloud_efficiency` and `cloud_ssd` disk.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The size of the disk in GiBs. When resize the disk, the new size must be greater than the former value, or you would get an error `InvalidDiskSize.TooSmall`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotId

A snapshot to base the disk off of. If the disk size required by snapshot is greater than `size`, the `size` will be ignored, conflict with `encrypted`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Status

Returns the <code>Status</code> value.

