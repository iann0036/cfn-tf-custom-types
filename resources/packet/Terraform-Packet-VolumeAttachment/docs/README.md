# Terraform::Packet::VolumeAttachment

Provides attachment of Packet Block Storage Volume to Devices.

Device and volume must be in the same location (facility).

Once attached by Terraform, they must then be mounted using the `packet-block-storage-attach` and `packet-block-storage-detach` scripts, which are presinstalled on most OS images. They can also be found in [https://github.com/packethost/packet-block-storage](https://github.com/packethost/packet-block-storage).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Packet::VolumeAttachment",
    "Properties" : {
        "<a href="#deviceid" title="DeviceId">DeviceId</a>" : <i>String</i>,
        "<a href="#volumeid" title="VolumeId">VolumeId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Packet::VolumeAttachment
Properties:
    <a href="#deviceid" title="DeviceId">DeviceId</a>: <i>String</i>
    <a href="#volumeid" title="VolumeId">VolumeId</a>: <i>String</i>
</pre>

## Properties

#### DeviceId

The ID of the device to which the volume should be attached.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeId

The ID of the volume to attach.

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

