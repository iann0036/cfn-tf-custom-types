# TF::NewRelic::NrqlAlertCondition NrqlDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#evaluationoffset" title="EvaluationOffset">EvaluationOffset</a>" : <i>Double</i>,
    "<a href="#query" title="Query">Query</a>" : <i>String</i>,
    "<a href="#sincevalue" title="SinceValue">SinceValue</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#evaluationoffset" title="EvaluationOffset">EvaluationOffset</a>: <i>Double</i>
<a href="#query" title="Query">Query</a>: <i>String</i>
<a href="#sincevalue" title="SinceValue">SinceValue</a>: <i>String</i>
</pre>

## Properties

#### EvaluationOffset

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SinceValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

