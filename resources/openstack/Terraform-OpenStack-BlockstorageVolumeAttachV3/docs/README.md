# Terraform::OpenStack::BlockstorageVolumeAttachV3

This resource is experimental and may be removed in the future! Feedback
is requested if you find this resource useful or if you find any problems
with it.

Creates a general purpose attachment connection to a Block
Storage volume using the OpenStack Block Storage (Cinder) v3 API.
Depending on your Block Storage service configuration, this
resource can assist in attaching a volume to a non-OpenStack resource
such as a bare-metal server or a remote virtual machine in a
different cloud provider.

This does not actually attach a volume to an instance. Please use
the `openstack_compute_volume_attach_v2` resource for that.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::BlockstorageVolumeAttachV3",
    "Properties" : {
        "<a href="#attachmode" title="AttachMode">AttachMode</a>" : <i>String</i>,
        "<a href="#device" title="Device">Device</a>" : <i>String</i>,
        "<a href="#hostname" title="HostName">HostName</a>" : <i>String</i>,
        "<a href="#initiator" title="Initiator">Initiator</a>" : <i>String</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
        "<a href="#multipath" title="Multipath">Multipath</a>" : <i>Boolean</i>,
        "<a href="#ostype" title="OsType">OsType</a>" : <i>String</i>,
        "<a href="#platform" title="Platform">Platform</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#volumeid" title="VolumeId">VolumeId</a>" : <i>String</i>,
        "<a href="#wwnn" title="Wwnn">Wwnn</a>" : <i>String</i>,
        "<a href="#wwpn" title="Wwpn">Wwpn</a>" : <i>[ String, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::BlockstorageVolumeAttachV3
Properties:
    <a href="#attachmode" title="AttachMode">AttachMode</a>: <i>String</i>
    <a href="#device" title="Device">Device</a>: <i>String</i>
    <a href="#hostname" title="HostName">HostName</a>: <i>String</i>
    <a href="#initiator" title="Initiator">Initiator</a>: <i>String</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
    <a href="#multipath" title="Multipath">Multipath</a>: <i>Boolean</i>
    <a href="#ostype" title="OsType">OsType</a>: <i>String</i>
    <a href="#platform" title="Platform">Platform</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#volumeid" title="VolumeId">VolumeId</a>: <i>String</i>
    <a href="#wwnn" title="Wwnn">Wwnn</a>: <i>String</i>
    <a href="#wwpn" title="Wwpn">Wwpn</a>: <i>
      - String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AttachMode

Specify whether to attach the volume as Read-Only
(`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
If left unspecified, the Block Storage API will apply a default of `rw`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Device

The device to tell the Block Storage service this
volume will be attached as. This is purely for informational purposes.
You can specify `auto` or a device such as `/dev/vdc`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostName

The host to attach the volume to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Initiator

The iSCSI initiator string to make the connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

The IP address of the `host_name` above.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Multipath

Whether to connect to this volume via multipath.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

The iSCSI initiator OS type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Platform

The iSCSI initiator platform.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V3 Block Storage
client. A Block Storage client is needed to create a volume attachment.
If omitted, the `region` argument of the provider is used. Changing this
creates a new volume attachment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeId

The ID of the Volume to attach to an Instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wwnn

A wwnn name. Used for Fibre Channel connections.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wwpn

An array of wwpn strings. Used for Fibre Channel
connections.

_Required_: No

_Type_: List of String

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

#### Data

Returns the <code>Data</code> value.

#### DriverVolumeType

Returns the <code>DriverVolumeType</code> value.

#### MountPointBase

Returns the <code>MountPointBase</code> value.

