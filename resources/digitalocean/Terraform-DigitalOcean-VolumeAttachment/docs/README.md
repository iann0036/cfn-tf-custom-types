# Terraform::DigitalOcean::VolumeAttachment

Manages attaching a Volume to a Droplet.

~> **NOTE:** Volumes can be attached either directly on the `digitalocean_droplet` resource, or using the `digitalocean_volume_attachment` resource - but the two cannot be used together. If both are used against the same Droplet, the volume attachments will constantly drift.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::DigitalOcean::VolumeAttachment",
    "Properties" : {
        "<a href="#dropletid" title="DropletId">DropletId</a>" : <i>Double</i>,
        "<a href="#volumeid" title="VolumeId">VolumeId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::DigitalOcean::VolumeAttachment
Properties:
    <a href="#dropletid" title="DropletId">DropletId</a>: <i>Double</i>
    <a href="#volumeid" title="VolumeId">VolumeId</a>: <i>String</i>
</pre>

## Properties

#### DropletId

ID of the Droplet to attach the volume to.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeId

ID of the Volume to be attached to the Droplet.

_Required_: Yes

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

#### Id

Returns the <code>Id</code> value.

