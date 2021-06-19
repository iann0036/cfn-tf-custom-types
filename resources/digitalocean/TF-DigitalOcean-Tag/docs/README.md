# TF::DigitalOcean::Tag

Provides a DigitalOcean Tag resource. A Tag is a label that can be applied to a
Droplet resource in order to better organize or facilitate the lookups and
actions on it. Tags created with this resource can be referenced in your Droplet
configuration via their ID or name.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::DigitalOcean::Tag",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::DigitalOcean::Tag
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Name

The name of the tag.

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

#### DatabasesCount

Returns the <code>DatabasesCount</code> value.

#### DropletsCount

Returns the <code>DropletsCount</code> value.

#### Id

Returns the <code>Id</code> value.

#### ImagesCount

Returns the <code>ImagesCount</code> value.

#### TotalResourceCount

Returns the <code>TotalResourceCount</code> value.

#### VolumeSnapshotsCount

Returns the <code>VolumeSnapshotsCount</code> value.

#### VolumesCount

Returns the <code>VolumesCount</code> value.

