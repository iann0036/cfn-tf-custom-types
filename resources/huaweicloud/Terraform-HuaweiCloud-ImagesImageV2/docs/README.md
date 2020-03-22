# Terraform::HuaweiCloud::ImagesImageV2

Manages a V2 Image resource within HuaweiCloud IMS.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::ImagesImageV2",
    "Properties" : {
        "<a href="#containerformat" title="ContainerFormat">ContainerFormat</a>" : <i>String</i>,
        "<a href="#diskformat" title="DiskFormat">DiskFormat</a>" : <i>String</i>,
        "<a href="#imagecachepath" title="ImageCachePath">ImageCachePath</a>" : <i>String</i>,
        "<a href="#imagesourceurl" title="ImageSourceUrl">ImageSourceUrl</a>" : <i>String</i>,
        "<a href="#localfilepath" title="LocalFilePath">LocalFilePath</a>" : <i>String</i>,
        "<a href="#mindiskgb" title="MinDiskGb">MinDiskGb</a>" : <i>Double</i>,
        "<a href="#minrammb" title="MinRamMb">MinRamMb</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#protected" title="Protected">Protected</a>" : <i>Boolean</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#visibility" title="Visibility">Visibility</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::ImagesImageV2
Properties:
    <a href="#containerformat" title="ContainerFormat">ContainerFormat</a>: <i>String</i>
    <a href="#diskformat" title="DiskFormat">DiskFormat</a>: <i>String</i>
    <a href="#imagecachepath" title="ImageCachePath">ImageCachePath</a>: <i>String</i>
    <a href="#imagesourceurl" title="ImageSourceUrl">ImageSourceUrl</a>: <i>String</i>
    <a href="#localfilepath" title="LocalFilePath">LocalFilePath</a>: <i>String</i>
    <a href="#mindiskgb" title="MinDiskGb">MinDiskGb</a>: <i>Double</i>
    <a href="#minrammb" title="MinRamMb">MinRamMb</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#protected" title="Protected">Protected</a>: <i>Boolean</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#visibility" title="Visibility">Visibility</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### ContainerFormat

The container format. Must be "bare".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskFormat

The disk format. Must be one of "qcow2", "vhd".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageCachePath

This is the directory where the images will
be downloaded. Images will be stored with a filename corresponding to
the url's md5 hash. Defaults to "$HOME/.terraform/image_cache".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageSourceUrl

This is the url of the raw image that will
be downloaded in the `image_cache_path` before being uploaded to Glance.
Glance is able to download image from internet but the `golangsdk` library
does not yet provide a way to do so.
Conflicts with `local_file_path`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalFilePath

This is the filepath of the raw image file
that will be uploaded to Glance. Conflicts with `image_source_url`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinDiskGb

Amount of disk space (in GB) required to boot image.
Defaults to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinRamMb

Amount of ram (in MB) required to boot image.
Defauts to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the image.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protected

If true, image will not be deletable.
Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Glance client.
A Glance client is needed to create an Image that can be used with
a compute instance. If omitted, the `region` argument of the provider
is used. Changing this creates a new Image.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

The tags of the image. It must be a list of strings.
At this time, it is not possible to delete all tags of an image.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visibility

The visibility of the image. Must be "private".
The ability to set the visibility depends upon the configuration of
the HuaweiCloud cloud.

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

#### Checksum

Returns the <code>Checksum</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### File

Returns the <code>File</code> value.

#### Id

Returns the <code>Id</code> value.

#### Metadata

Returns the <code>Metadata</code> value.

#### Owner

Returns the <code>Owner</code> value.

#### Schema

Returns the <code>Schema</code> value.

#### SizeBytes

Returns the <code>SizeBytes</code> value.

#### Status

Returns the <code>Status</code> value.

#### UpdateAt

Returns the <code>UpdateAt</code> value.

