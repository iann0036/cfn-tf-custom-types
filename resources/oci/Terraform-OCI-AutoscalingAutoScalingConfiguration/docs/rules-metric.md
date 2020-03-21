# Terraform::OCI::AutoscalingAutoScalingConfiguration Rules Metric

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#metrictype" title="MetricType">MetricType</a>" : <i>String</i>,
    "<a href="#threshold" title="Threshold">Threshold</a>" : <i>[ &lt;a href=&#34;rules-metric-threshold.md&#34;&gt;Threshold&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#metrictype" title="MetricType">MetricType</a>: <i>String</i>
<a href="#threshold" title="Threshold">Threshold</a>: <i>
      - &lt;a href=&#34;rules-metric-threshold.md&#34;&gt;Threshold&lt;/a&gt;</i>
</pre>

## Properties

#### MetricType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

_Required_: No
_Type_: List of &lt;a href=&#34;rules-metric-threshold.md&#34;&gt;Threshold&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

