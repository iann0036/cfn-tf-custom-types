# Terraform::OpenTelekomCloud::ImsImageV2

Manages a V2 Image resource within OpenTelekomCloud IMS.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::ImsImageV2",
    "Properties" : {
        "<a href="#cmkid" title="CmkId">CmkId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#imageurl" title="ImageUrl">ImageUrl</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#isconfig" title="IsConfig">IsConfig</a>" : <i>Boolean</i>,
        "<a href="#maxram" title="MaxRam">MaxRam</a>" : <i>Double</i>,
        "<a href="#mindisk" title="MinDisk">MinDisk</a>" : <i>Double</i>,
        "<a href="#minram" title="MinRam">MinRam</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#osversion" title="OsVersion">OsVersion</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::ImsImageV2
Properties:
    <a href="#cmkid" title="CmkId">CmkId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#imageurl" title="ImageUrl">ImageUrl</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#isconfig" title="IsConfig">IsConfig</a>: <i>Boolean</i>
    <a href="#maxram" title="MaxRam">MaxRam</a>: <i>Double</i>
    <a href="#mindisk" title="MinDisk">MinDisk</a>: <i>Double</i>
    <a href="#minram" title="MinRam">MinRam</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#osversion" title="OsVersion">OsVersion</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### CmkId

The master key used for encrypting an image.
Changing this creates a new image.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the image. Changing this creates a new image.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageUrl

The URL of the external image file in the OBS bucket.
This parameter is mandatory when you create a private image from an external file
uploaded to an OBS bucket. The format is *OBS bucket name:Image file name*.
Changing this creates a new image.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

The ID of the ECS that needs to be converted into an image.
This parameter is mandatory when you create a privete image from an ECS.
Changing this creates a new image.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsConfig

If automatic configuration is required, set the value to true.
Otherwise, set the value to false. Changing this creates a new image.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRam

The maximum memory of the image in the unit of MB.
Changing this creates a new image.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinDisk

The minimum size of the system disk in the unit of GB.
This parameter is mandatory when you create a private image from an external file
uploaded to an OBS bucket. The value ranges from 1 GB to 1024 GB.
Changing this creates a new image.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinRam

The minimum memory of the image in the unit of MB.
The default value is 0, indicating that the memory is not restricted.
Changing this creates a new image.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the image.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsVersion

The OS version.
This parameter is valid when you create a private image from an external file
uploaded to an OBS bucket. Changing this creates a new image.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

The tags of the image.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The image type. Must be one of "ECS", "FusionCompute", "BMS",
or "Ironic". Changing this creates a new image.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DataOrigin

Returns the <code>DataOrigin</code> value.

#### DiskFormat

Returns the <code>DiskFormat</code> value.

#### Id

Returns the <code>Id</code> value.

#### ImageSize

Returns the <code>ImageSize</code> value.

#### Visibility

Returns the <code>Visibility</code> value.

