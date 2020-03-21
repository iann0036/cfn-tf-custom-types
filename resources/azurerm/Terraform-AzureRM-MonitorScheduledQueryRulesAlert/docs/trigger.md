# Terraform::AzureRM::MonitorScheduledQueryRulesAlert Trigger

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
    "<a href="#threshold" title="Threshold">Threshold</a>" : <i>Double</i>,
    "<a href="#metrictrigger" title="MetricTrigger">MetricTrigger</a>" : <i>[ <a href="trigger-metrictrigger.md">MetricTrigger</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#operator" title="Operator">Operator</a>: <i>String</i>
<a href="#threshold" title="Threshold">Threshold</a>: <i>Double</i>
<a href="#metrictrigger" title="MetricTrigger">MetricTrigger</a>: <i>
      - <a href="trigger-metrictrigger.md">MetricTrigger</a></i>
</pre>

## Properties

#### Operator

Evaluation operation for rule - 'Equal', 'GreaterThan' or 'LessThan'.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

Result or count threshold based on which rule should be triggered.  Values must be between 0 and 10000 inclusive.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricTrigger

_Required_: No

_Type_: List of <a href="trigger-metrictrigger.md">MetricTrigger</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

