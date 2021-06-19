# TF::Dynatrace::ApplicationAnomalies FailureRateDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#auto" title="Auto">Auto</a>" : <i>[ <a href="autodefinition.md">AutoDefinition</a>, ... ]</i>,
    "<a href="#thresholds" title="Thresholds">Thresholds</a>" : <i>[ <a href="thresholdsdefinition.md">ThresholdsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#auto" title="Auto">Auto</a>: <i>
      - <a href="autodefinition.md">AutoDefinition</a></i>
<a href="#thresholds" title="Thresholds">Thresholds</a>: <i>
      - <a href="thresholdsdefinition.md">ThresholdsDefinition</a></i>
</pre>

## Properties

#### Auto

_Required_: No

_Type_: List of <a href="autodefinition.md">AutoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Thresholds

_Required_: No

_Type_: List of <a href="thresholdsdefinition.md">ThresholdsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

