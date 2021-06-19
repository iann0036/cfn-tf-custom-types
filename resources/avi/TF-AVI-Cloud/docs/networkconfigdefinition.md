# TF::AVI::Cloud NetworkConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#config" title="Config">Config</a>" : <i>String</i>,
    "<a href="#inband" title="Inband">Inband</a>" : <i>[ <a href="inbanddefinition.md">InbandDefinition</a>, ... ]</i>,
    "<a href="#onearm" title="OneArm">OneArm</a>" : <i>[ <a href="onearmdefinition.md">OneArmDefinition</a>, ... ]</i>,
    "<a href="#twoarm" title="TwoArm">TwoArm</a>" : <i>[ <a href="twoarmdefinition.md">TwoArmDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#config" title="Config">Config</a>: <i>String</i>
<a href="#inband" title="Inband">Inband</a>: <i>
      - <a href="inbanddefinition.md">InbandDefinition</a></i>
<a href="#onearm" title="OneArm">OneArm</a>: <i>
      - <a href="onearmdefinition.md">OneArmDefinition</a></i>
<a href="#twoarm" title="TwoArm">TwoArm</a>: <i>
      - <a href="twoarmdefinition.md">TwoArmDefinition</a></i>
</pre>

## Properties

#### Config

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inband

_Required_: No

_Type_: List of <a href="inbanddefinition.md">InbandDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OneArm

_Required_: No

_Type_: List of <a href="onearmdefinition.md">OneArmDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TwoArm

_Required_: No

_Type_: List of <a href="twoarmdefinition.md">TwoArmDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

