# TF::Dynatrace::CalculatedServiceMetric ConditionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#attribute" title="Attribute">Attribute</a>" : <i>String</i>,
    "<a href="#comparison" title="Comparison">Comparison</a>" : <i>[ <a href="comparisondefinition.md">ComparisonDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#attribute" title="Attribute">Attribute</a>: <i>String</i>
<a href="#comparison" title="Comparison">Comparison</a>: <i>
      - <a href="comparisondefinition.md">ComparisonDefinition</a></i>
</pre>

## Properties

#### Attribute

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comparison

_Required_: No

_Type_: List of <a href="comparisondefinition.md">ComparisonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

