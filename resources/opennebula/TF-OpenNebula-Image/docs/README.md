# TF::OpenNebula::Image

Provides an OpenNebula image resource.

This resource allows you to manage images on your OpenNebula clusters. When applied,
a new image is created. When destroyed, this image is removed.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpenNebula::Image",
    "Properties" : {
        "<a href="#clonefromimage" title="CloneFromImage">CloneFromImage</a>" : <i>String</i>,
        "<a href="#datastoreid" title="DatastoreId">DatastoreId</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#devprefix" title="DevPrefix">DevPrefix</a>" : <i>String</i>,
        "<a href="#driver" title="Driver">Driver</a>" : <i>String</i>,
        "<a href="#format" title="Format">Format</a>" : <i>String</i>,
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#lock" title="Lock">Lock</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>String</i>,
        "<a href="#persistent" title="Persistent">Persistent</a>" : <i>Boolean</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#target" title="Target">Target</a>" : <i>String</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::OpenNebula::Image
Properties:
    <a href="#clonefromimage" title="CloneFromImage">CloneFromImage</a>: <i>String</i>
    <a href="#datastoreid" title="DatastoreId">DatastoreId</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#devprefix" title="DevPrefix">DevPrefix</a>: <i>String</i>
    <a href="#driver" title="Driver">Driver</a>: <i>String</i>
    <a href="#format" title="Format">Format</a>: <i>String</i>
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#lock" title="Lock">Lock</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>String</i>
    <a href="#persistent" title="Persistent">Persistent</a>: <i>Boolean</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#target" title="Target">Target</a>: <i>String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### CloneFromImage

ID or name of the image to clone from. Conflicts with `path`, `size` and `type`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatastoreId

ID of the datastore used to store the image. The `datastore_id` must be an active `IMAGE` datastore.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the image.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DevPrefix

Device prefix on Virtual Machine. Usually one of these: `hd`, `sd` or `vd`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Driver

OpenNebula Driver to use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

Image format. Example: `raw`, `qcow2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

Name of the group which owns the image. Defaults to the caller primary group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lock

Lock the image with a specific lock level. Supported values: `USE`, `MANAGE`, `ADMIN`, `ALL` or `UNLOCK`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the image.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

Path or URL of the original image to use. Conflicts with `clone_from_image`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

Permissions applied to the image. Defaults to the UMASK in OpenNebula (in UNIX Format: owner-group-other => Use-Manage-Admin).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Persistent

Flag which indicates if the Image has to be persistent. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

Size of the image in MB. Conflicts with `clone_from_image`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Image tags (Key = value).

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

Device target on Virtual Machine.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Timeout (in Minutes) for Image availability. Defaults to 10 minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of the image. Supported values: `OS`, `CDROM`, `DATABLOCK`, `KERNEL`, `RAMDISK` or `CONTEXT`. Conflicts with `clone_from_image`.

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

#### Gid

Returns the <code>Gid</code> value.

#### Gname

Returns the <code>Gname</code> value.

#### Id

Returns the <code>Id</code> value.

#### Uid

Returns the <code>Uid</code> value.

#### Uname

Returns the <code>Uname</code> value.

