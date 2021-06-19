# TF::Spotinst::OceanEcsLaunchSpec BlockDeviceMappingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#devicename" title="DeviceName">DeviceName</a>" : <i>String</i>,
    "<a href="#nodevice" title="NoDevice">NoDevice</a>" : <i>String</i>,
    "<a href="#virtualname" title="VirtualName">VirtualName</a>" : <i>String</i>,
    "<a href="#ebs" title="Ebs">Ebs</a>" : <i>[ <a href="ebsdefinition.md">EbsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#devicename" title="DeviceName">DeviceName</a>: <i>String</i>
<a href="#nodevice" title="NoDevice">NoDevice</a>: <i>String</i>
<a href="#virtualname" title="VirtualName">VirtualName</a>: <i>String</i>
<a href="#ebs" title="Ebs">Ebs</a>: <i>
      - <a href="ebsdefinition.md">EbsDefinition</a></i>
</pre>

## Properties

#### DeviceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoDevice

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ebs

_Required_: No

_Type_: List of <a href="ebsdefinition.md">EbsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

