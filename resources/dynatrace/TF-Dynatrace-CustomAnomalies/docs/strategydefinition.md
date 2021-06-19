# TF::Dynatrace::CustomAnomalies StrategyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#auto" title="Auto">Auto</a>" : <i>[ <a href="autodefinition.md">AutoDefinition</a>, ... ]</i>,
    "<a href="#generic" title="Generic">Generic</a>" : <i>[ <a href="genericdefinition.md">GenericDefinition</a>, ... ]</i>,
    "<a href="#static" title="Static">Static</a>" : <i>[ <a href="staticdefinition.md">StaticDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#auto" title="Auto">Auto</a>: <i>
      - <a href="autodefinition.md">AutoDefinition</a></i>
<a href="#generic" title="Generic">Generic</a>: <i>
      - <a href="genericdefinition.md">GenericDefinition</a></i>
<a href="#static" title="Static">Static</a>: <i>
      - <a href="staticdefinition.md">StaticDefinition</a></i>
</pre>

## Properties

#### Auto

_Required_: No

_Type_: List of <a href="autodefinition.md">AutoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Generic

_Required_: No

_Type_: List of <a href="genericdefinition.md">GenericDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Static

_Required_: No

_Type_: List of <a href="staticdefinition.md">StaticDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

