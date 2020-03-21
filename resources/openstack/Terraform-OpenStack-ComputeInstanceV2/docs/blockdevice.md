# Terraform::OpenStack::ComputeInstanceV2 BlockDevice

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bootindex" title="BootIndex">BootIndex</a>" : <i>Double</i>,
    "<a href="#deleteontermination" title="DeleteOnTermination">DeleteOnTermination</a>" : <i>Boolean</i>,
    "<a href="#destinationtype" title="DestinationType">DestinationType</a>" : <i>String</i>,
    "<a href="#devicetype" title="DeviceType">DeviceType</a>" : <i>String</i>,
    "<a href="#diskbus" title="DiskBus">DiskBus</a>" : <i>String</i>,
    "<a href="#guestformat" title="GuestFormat">GuestFormat</a>" : <i>String</i>,
    "<a href="#sourcetype" title="SourceType">SourceType</a>" : <i>String</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#volumesize" title="VolumeSize">VolumeSize</a>" : <i>Double</i>,
    "<a href="#volumetype" title="VolumeType">VolumeType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#bootindex" title="BootIndex">BootIndex</a>: <i>Double</i>
<a href="#deleteontermination" title="DeleteOnTermination">DeleteOnTermination</a>: <i>Boolean</i>
<a href="#destinationtype" title="DestinationType">DestinationType</a>: <i>String</i>
<a href="#devicetype" title="DeviceType">DeviceType</a>: <i>String</i>
<a href="#diskbus" title="DiskBus">DiskBus</a>: <i>String</i>
<a href="#guestformat" title="GuestFormat">GuestFormat</a>: <i>String</i>
<a href="#sourcetype" title="SourceType">SourceType</a>: <i>String</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#volumesize" title="VolumeSize">VolumeSize</a>: <i>Double</i>
<a href="#volumetype" title="VolumeType">VolumeType</a>: <i>String</i>
</pre>

## Properties

#### BootIndex

The boot index of the volume. It defaults to 0.
Changing this creates a new server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteOnTermination

Delete the volume / block device upon
termination of the instance. Defaults to false. Changing this creates a
new server.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationType

The type that gets created. Possible values
are "volume" and "local". Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceType

The low-level device type that will be used. Most
common thing is to leave this empty. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskBus

The low-level disk bus that will be used. Most common
thing is to leave this empty. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceType

The source type of the device. Must be one of
"blank", "image", "volume", or "snapshot". Changing this creates a new
server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

The UUID of
the image, volume, or snapshot. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeSize

The size of the volume to create (in gigabytes). Required
in the following combinations: source=image and destination=volume,
source=blank and destination=local, and source=blank and destination=volume.
Changing this creates a new server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeType

The volume type that will be used, for example SSD
or HDD storage. The available options depend on how your specific OpenStack
cloud is configured and what classes of storage are provided. Changing this
creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

