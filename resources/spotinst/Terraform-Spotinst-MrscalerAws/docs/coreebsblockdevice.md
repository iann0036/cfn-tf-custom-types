# Terraform::Spotinst::MrscalerAws CoreEbsBlockDevice

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#iops" title="Iops">Iops</a>" : <i>Double</i>,
    "<a href="#sizeingb" title="SizeInGb">SizeInGb</a>" : <i>Double</i>,
    "<a href="#volumetype" title="VolumeType">VolumeType</a>" : <i>String</i>,
    "<a href="#volumesperinstance" title="VolumesPerInstance">VolumesPerInstance</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#iops" title="Iops">Iops</a>: <i>Double</i>
<a href="#sizeingb" title="SizeInGb">SizeInGb</a>: <i>Double</i>
<a href="#volumetype" title="VolumeType">VolumeType</a>: <i>String</i>
<a href="#volumesperinstance" title="VolumesPerInstance">VolumesPerInstance</a>: <i>Double</i>
</pre>

## Properties

#### Iops

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizeInGb

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumesPerInstance

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

