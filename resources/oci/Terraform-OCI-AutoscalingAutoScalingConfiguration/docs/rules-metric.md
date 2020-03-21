# Terraform::OCI::AutoscalingAutoScalingConfiguration Rules Metric

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#metrictype" title="MetricType">MetricType</a>" : <i>String</i>,
    "<a href="#threshold" title="Threshold">Threshold</a>" : <i>[ <a href="rules-metric-threshold.md">Threshold</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#metrictype" title="MetricType">MetricType</a>: <i>String</i>
<a href="#threshold" title="Threshold">Threshold</a>: <i>
      - <a href="rules-metric-threshold.md">Threshold</a></i>
</pre>

## Properties

#### MetricType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

_Required_: No

_Type_: List of <a href="rules-metric-threshold.md">Threshold</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

