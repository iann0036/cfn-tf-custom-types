# TF::AWS::EmrInstanceGroup EbsConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#iops" title="Iops">Iops</a>" : <i>Double</i>,
    "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#volumesperinstance" title="VolumesPerInstance">VolumesPerInstance</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#iops" title="Iops">Iops</a>: <i>Double</i>
<a href="#size" title="Size">Size</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#volumesperinstance" title="VolumesPerInstance">VolumesPerInstance</a>: <i>Double</i>
</pre>

## Properties

#### Iops

The number of I/O operations per second (IOPS) that the volume supports.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The volume type. Valid options are 'gp2', 'io1' and 'standard'.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumesPerInstance

The number of EBS Volumes to attach per instance.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

