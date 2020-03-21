# Terraform::AWS::CloudwatchMetricAlarm MetricQuery

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#expression" title="Expression">Expression</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#label" title="Label">Label</a>" : <i>String</i>,
    "<a href="#returndata" title="ReturnData">ReturnData</a>" : <i>Boolean</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>[ &lt;a href=&#34;metricquery-metric.md&#34;&gt;Metric&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#expression" title="Expression">Expression</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#label" title="Label">Label</a>: <i>String</i>
<a href="#returndata" title="ReturnData">ReturnData</a>: <i>Boolean</i>
<a href="#metric" title="Metric">Metric</a>: <i>
      - &lt;a href=&#34;metricquery-metric.md&#34;&gt;Metric&lt;/a&gt;</i>
</pre>

## Properties

#### Expression

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReturnData

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No
_Type_: List of &lt;a href=&#34;metricquery-metric.md&#34;&gt;Metric&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
