# TF::AWS::OpsworksGangliaLayer EbsVolumeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#encrypted" title="Encrypted">Encrypted</a>" : <i>Boolean</i>,
    "<a href="#iops" title="Iops">Iops</a>" : <i>Double</i>,
    "<a href="#mountpoint" title="MountPoint">MountPoint</a>" : <i>String</i>,
    "<a href="#numberofdisks" title="NumberOfDisks">NumberOfDisks</a>" : <i>Double</i>,
    "<a href="#raidlevel" title="RaidLevel">RaidLevel</a>" : <i>String</i>,
    "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#encrypted" title="Encrypted">Encrypted</a>: <i>Boolean</i>
<a href="#iops" title="Iops">Iops</a>: <i>Double</i>
<a href="#mountpoint" title="MountPoint">MountPoint</a>: <i>String</i>
<a href="#numberofdisks" title="NumberOfDisks">NumberOfDisks</a>: <i>Double</i>
<a href="#raidlevel" title="RaidLevel">RaidLevel</a>: <i>String</i>
<a href="#size" title="Size">Size</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Encrypted

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iops

For PIOPS volumes, the IOPS per disk.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountPoint

The path to mount the EBS volume on the layer's instances.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfDisks

The number of disks to use for the EBS volume.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RaidLevel

The RAID level to use for the volume.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The size of the volume in gigabytes.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of volume to create. This may be `standard` (the default), `io1` or `gp2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

