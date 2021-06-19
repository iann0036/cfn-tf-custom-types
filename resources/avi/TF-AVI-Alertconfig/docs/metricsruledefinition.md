# TF::AVI::Alertconfig MetricsRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#duration" title="Duration">Duration</a>" : <i>Double</i>,
    "<a href="#metricid" title="MetricId">MetricId</a>" : <i>String</i>,
    "<a href="#metricthreshold" title="MetricThreshold">MetricThreshold</a>" : <i>[ <a href="metricthresholddefinition.md">MetricThresholdDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#duration" title="Duration">Duration</a>: <i>Double</i>
<a href="#metricid" title="MetricId">MetricId</a>: <i>String</i>
<a href="#metricthreshold" title="MetricThreshold">MetricThreshold</a>: <i>
      - <a href="metricthresholddefinition.md">MetricThresholdDefinition</a></i>
</pre>

## Properties

#### Duration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricThreshold

_Required_: No

_Type_: List of <a href="metricthresholddefinition.md">MetricThresholdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

