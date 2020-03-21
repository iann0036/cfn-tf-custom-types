# Terraform::DigitalOcean::Volume

Provides a DigitalOcean Block Storage volume which can be attached to a Droplet in order to provide expanded storage.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::DigitalOcean::Volume",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#filesystemtype" title="FilesystemType">FilesystemType</a>" : <i>String</i>,
        "<a href="#initialfilesystemlabel" title="InitialFilesystemLabel">InitialFilesystemLabel</a>" : <i>String</i>,
        "<a href="#initialfilesystemtype" title="InitialFilesystemType">InitialFilesystemType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#snapshotid" title="SnapshotId">SnapshotId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::DigitalOcean::Volume
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#filesystemtype" title="FilesystemType">FilesystemType</a>: <i>String</i>
    <a href="#initialfilesystemlabel" title="InitialFilesystemLabel">InitialFilesystemLabel</a>: <i>String</i>
    <a href="#initialfilesystemtype" title="InitialFilesystemType">InitialFilesystemType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#snapshotid" title="SnapshotId">SnapshotId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
</pre>

## Properties

#### Description

A free-form text field up to a limit of 1024 bytes to describe a block storage volume.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilesystemType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialFilesystemLabel

Initial filesystem label for the block storage volume.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialFilesystemType

Initial filesystem type (`xfs` or `ext4`) for the block storage volume.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region that the block storage volume will be created in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The size of the block storage volume in GiB. If updated, can only be expanded.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotId

The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of the tags to be applied to this Volume.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DropletIds

Returns the <code>DropletIds</code> value.

#### FilesystemLabel

Returns the <code>FilesystemLabel</code> value.

#### Urn

Returns the <code>Urn</code> value.

