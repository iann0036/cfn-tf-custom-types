# TF::AWS::BatchJobDefinition RetryStrategyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#attempts" title="Attempts">Attempts</a>" : <i>Double</i>,
    "<a href="#evaluateonexit" title="EvaluateOnExit">EvaluateOnExit</a>" : <i>[ <a href="evaluateonexitdefinition.md">EvaluateOnExitDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#attempts" title="Attempts">Attempts</a>: <i>Double</i>
<a href="#evaluateonexit" title="EvaluateOnExit">EvaluateOnExit</a>: <i>
      - <a href="evaluateonexitdefinition.md">EvaluateOnExitDefinition</a></i>
</pre>

## Properties

#### Attempts

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvaluateOnExit

_Required_: No

_Type_: List of <a href="evaluateonexitdefinition.md">EvaluateOnExitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

