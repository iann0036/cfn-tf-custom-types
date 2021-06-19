# TF::AWS::AutoscalingPolicy StepAdjustmentDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#metricintervallowerbound" title="MetricIntervalLowerBound">MetricIntervalLowerBound</a>" : <i>String</i>,
    "<a href="#metricintervalupperbound" title="MetricIntervalUpperBound">MetricIntervalUpperBound</a>" : <i>String</i>,
    "<a href="#scalingadjustment" title="ScalingAdjustment">ScalingAdjustment</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#metricintervallowerbound" title="MetricIntervalLowerBound">MetricIntervalLowerBound</a>: <i>String</i>
<a href="#metricintervalupperbound" title="MetricIntervalUpperBound">MetricIntervalUpperBound</a>: <i>String</i>
<a href="#scalingadjustment" title="ScalingAdjustment">ScalingAdjustment</a>: <i>Double</i>
</pre>

## Properties

#### MetricIntervalLowerBound

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricIntervalUpperBound

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingAdjustment

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

