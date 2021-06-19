# TF::AzureRM::BatchPool AutoScaleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#evaluationinterval" title="EvaluationInterval">EvaluationInterval</a>" : <i>String</i>,
    "<a href="#formula" title="Formula">Formula</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#evaluationinterval" title="EvaluationInterval">EvaluationInterval</a>: <i>String</i>
<a href="#formula" title="Formula">Formula</a>: <i>String</i>
</pre>

## Properties

#### EvaluationInterval

The interval to wait before evaluating if the pool needs to be scaled. Defaults to `PT15M`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Formula

The autoscale formula that needs to be used for scaling the Batch pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

