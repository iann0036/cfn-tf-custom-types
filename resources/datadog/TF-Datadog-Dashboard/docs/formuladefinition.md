# TF::Datadog::Dashboard FormulaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alias" title="Alias">Alias</a>" : <i>String</i>,
    "<a href="#formulaexpression" title="FormulaExpression">FormulaExpression</a>" : <i>String</i>,
    "<a href="#limit" title="Limit">Limit</a>" : <i>[ <a href="limitdefinition.md">LimitDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alias" title="Alias">Alias</a>: <i>String</i>
<a href="#formulaexpression" title="FormulaExpression">FormulaExpression</a>: <i>String</i>
<a href="#limit" title="Limit">Limit</a>: <i>
      - <a href="limitdefinition.md">LimitDefinition</a></i>
</pre>

## Properties

#### Alias

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FormulaExpression

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Limit

_Required_: No

_Type_: List of <a href="limitdefinition.md">LimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

