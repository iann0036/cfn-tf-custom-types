# TF::Datadog::SyntheticsTest AssertionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
    "<a href="#property" title="Property">Property</a>" : <i>String</i>,
    "<a href="#target" title="Target">Target</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#targetjsonpath" title="Targetjsonpath">Targetjsonpath</a>" : <i>[ <a href="targetjsonpathdefinition.md">TargetjsonpathDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#operator" title="Operator">Operator</a>: <i>String</i>
<a href="#property" title="Property">Property</a>: <i>String</i>
<a href="#target" title="Target">Target</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#targetjsonpath" title="Targetjsonpath">Targetjsonpath</a>: <i>
      - <a href="targetjsonpathdefinition.md">TargetjsonpathDefinition</a></i>
</pre>

## Properties

#### Operator

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Property

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Targetjsonpath

_Required_: No

_Type_: List of <a href="targetjsonpathdefinition.md">TargetjsonpathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

