# TF::BIGIP::LtmPolicy RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#action" title="Action">Action</a>" : <i>[ <a href="actiondefinition.md">ActionDefinition</a>, ... ]</i>,
    "<a href="#condition" title="Condition">Condition</a>" : <i>[ <a href="conditiondefinition.md">ConditionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#action" title="Action">Action</a>: <i>
      - <a href="actiondefinition.md">ActionDefinition</a></i>
<a href="#condition" title="Condition">Condition</a>: <i>
      - <a href="conditiondefinition.md">ConditionDefinition</a></i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of <a href="actiondefinition.md">ActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: List of <a href="conditiondefinition.md">ConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

