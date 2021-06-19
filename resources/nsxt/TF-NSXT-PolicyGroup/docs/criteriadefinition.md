# TF::NSXT::PolicyGroup CriteriaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#condition" title="Condition">Condition</a>" : <i>[ <a href="conditiondefinition.md">ConditionDefinition</a>, ... ]</i>,
    "<a href="#ipaddressexpression" title="IpaddressExpression">IpaddressExpression</a>" : <i>[ <a href="ipaddressexpressiondefinition.md">IpaddressExpressionDefinition</a>, ... ]</i>,
    "<a href="#macaddressexpression" title="MacaddressExpression">MacaddressExpression</a>" : <i>[ <a href="macaddressexpressiondefinition.md">MacaddressExpressionDefinition</a>, ... ]</i>,
    "<a href="#pathexpression" title="PathExpression">PathExpression</a>" : <i>[ <a href="pathexpressiondefinition.md">PathExpressionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#condition" title="Condition">Condition</a>: <i>
      - <a href="conditiondefinition.md">ConditionDefinition</a></i>
<a href="#ipaddressexpression" title="IpaddressExpression">IpaddressExpression</a>: <i>
      - <a href="ipaddressexpressiondefinition.md">IpaddressExpressionDefinition</a></i>
<a href="#macaddressexpression" title="MacaddressExpression">MacaddressExpression</a>: <i>
      - <a href="macaddressexpressiondefinition.md">MacaddressExpressionDefinition</a></i>
<a href="#pathexpression" title="PathExpression">PathExpression</a>: <i>
      - <a href="pathexpressiondefinition.md">PathExpressionDefinition</a></i>
</pre>

## Properties

#### Condition

_Required_: No

_Type_: List of <a href="conditiondefinition.md">ConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpaddressExpression

_Required_: No

_Type_: List of <a href="ipaddressexpressiondefinition.md">IpaddressExpressionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacaddressExpression

_Required_: No

_Type_: List of <a href="macaddressexpressiondefinition.md">MacaddressExpressionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathExpression

_Required_: No

_Type_: List of <a href="pathexpressiondefinition.md">PathExpressionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

