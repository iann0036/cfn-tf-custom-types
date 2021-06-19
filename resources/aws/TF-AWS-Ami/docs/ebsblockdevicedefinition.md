# TF::AWS::Ami EbsBlockDeviceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#deleteontermination" title="DeleteOnTermination">DeleteOnTermination</a>" : <i>Boolean</i>,
    "<a href="#devicename" title="DeviceName">DeviceName</a>" : <i>String</i>,
    "<a href="#encrypted" title="Encrypted">Encrypted</a>" : <i>Boolean</i>,
    "<a href="#iops" title="Iops">Iops</a>" : <i>Double</i>,
    "<a href="#snapshotid" title="SnapshotId">SnapshotId</a>" : <i>String</i>,
    "<a href="#throughput" title="Throughput">Throughput</a>" : <i>Double</i>,
    "<a href="#volumesize" title="VolumeSize">VolumeSize</a>" : <i>Double</i>,
    "<a href="#volumetype" title="VolumeType">VolumeType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#deleteontermination" title="DeleteOnTermination">DeleteOnTermination</a>: <i>Boolean</i>
<a href="#devicename" title="DeviceName">DeviceName</a>: <i>String</i>
<a href="#encrypted" title="Encrypted">Encrypted</a>: <i>Boolean</i>
<a href="#iops" title="Iops">Iops</a>: <i>Double</i>
<a href="#snapshotid" title="SnapshotId">SnapshotId</a>: <i>String</i>
<a href="#throughput" title="Throughput">Throughput</a>: <i>Double</i>
<a href="#volumesize" title="VolumeSize">VolumeSize</a>: <i>Double</i>
<a href="#volumetype" title="VolumeType">VolumeType</a>: <i>String</i>
</pre>

## Properties

#### DeleteOnTermination

Boolean controlling whether the EBS volumes created to
support each created instance will be deleted once that instance is terminated.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceName

The path at which the device is exposed to created instances.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encrypted

Boolean controlling whether the created EBS volumes will be encrypted. Can't be used with `snapshot_id`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iops

Number of I/O operations per second the
created volumes will support.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotId

The id of an EBS snapshot that will be used to initialize the created
EBS volumes. If set, the `volume_size` attribute must be at least as large as the referenced
snapshot.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Throughput

The throughput that the EBS volume supports, in MiB/s. Only valid for `volume_type` of `gp3`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeSize

The size of created volumes in GiB.
If `snapshot_id` is set and `volume_size` is omitted then the volume will have the same size
as the selected snapshot.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeType

The type of EBS volume to create. Can be `standard`, `gp2`, `gp3`, `io1`, `io2`, `sc1` or `st1` (Default: `standard`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

