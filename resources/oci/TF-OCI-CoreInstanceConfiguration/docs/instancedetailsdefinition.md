# TF::OCI::CoreInstanceConfiguration InstanceDetailsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    "<a href="#blockvolumes" title="BlockVolumes">BlockVolumes</a>" : <i>[ <a href="blockvolumesdefinition.md">BlockVolumesDefinition</a>, ... ]</i>,
    "<a href="#launchdetails" title="LaunchDetails">LaunchDetails</a>" : <i>[ <a href="launchdetailsdefinition.md">LaunchDetailsDefinition</a>, ... ]</i>,
    "<a href="#secondaryvnics" title="SecondaryVnics">SecondaryVnics</a>" : <i>[ <a href="secondaryvnicsdefinition.md">SecondaryVnicsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
<a href="#blockvolumes" title="BlockVolumes">BlockVolumes</a>: <i>
      - <a href="blockvolumesdefinition.md">BlockVolumesDefinition</a></i>
<a href="#launchdetails" title="LaunchDetails">LaunchDetails</a>: <i>
      - <a href="launchdetailsdefinition.md">LaunchDetailsDefinition</a></i>
<a href="#secondaryvnics" title="SecondaryVnics">SecondaryVnics</a>: <i>
      - <a href="secondaryvnicsdefinition.md">SecondaryVnicsDefinition</a></i>
</pre>

## Properties

#### InstanceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockVolumes

_Required_: No

_Type_: List of <a href="blockvolumesdefinition.md">BlockVolumesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchDetails

_Required_: No

_Type_: List of <a href="launchdetailsdefinition.md">LaunchDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryVnics

_Required_: No

_Type_: List of <a href="secondaryvnicsdefinition.md">SecondaryVnicsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

