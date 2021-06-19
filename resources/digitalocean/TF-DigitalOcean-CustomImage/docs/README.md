# TF::DigitalOcean::CustomImage

Provides a resource which can be used to create a [custom image](https://www.digitalocean.com/docs/images/custom-images/)
from a URL. The URL must point to an image in one of the following file formats:

- Raw (.img) with an MBR or GPT partition table
- qcow2
- VHDX
- VDI
- VMDK

The image may be compressed using gzip or bzip2. See the DigitalOcean Custom
Image documentation for [additional requirements](https://www.digitalocean.com/docs/images/custom-images/#image-requirements).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::DigitalOcean::CustomImage",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#distribution" title="Distribution">Distribution</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#regions" title="Regions">Regions</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::DigitalOcean::CustomImage
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#distribution" title="Distribution">Distribution</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#regions" title="Regions">Regions</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
</pre>

## Properties

#### Description

An optional description for the image.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Distribution

An optional distribution name for the image. Valid values are documented [here](https://developers.digitalocean.com/documentation/v2/#create-a-custom-image).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A name for the Custom Image.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regions

A list of regions. (Currently only one is supported).

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of optional tags for the image.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

A URL from which the custom Linux virtual machine image may be retrieved.

_Required_: Yes

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

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### ImageId

Returns the <code>ImageId</code> value.

#### MinDiskSize

Returns the <code>MinDiskSize</code> value.

#### Public

Returns the <code>Public</code> value.

#### SizeGigabytes

Returns the <code>SizeGigabytes</code> value.

#### Slug

Returns the <code>Slug</code> value.

#### Status

Returns the <code>Status</code> value.

#### Type

Returns the <code>Type</code> value.

