# TF::AVI::Serviceenginegroup MetricsEventThresholdsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#metricseventthresholdtype" title="MetricsEventThresholdType">MetricsEventThresholdType</a>" : <i>String</i>,
    "<a href="#resetthreshold" title="ResetThreshold">ResetThreshold</a>" : <i>Double</i>,
    "<a href="#watermarkthresholds" title="WatermarkThresholds">WatermarkThresholds</a>" : <i>[ Double, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#metricseventthresholdtype" title="MetricsEventThresholdType">MetricsEventThresholdType</a>: <i>String</i>
<a href="#resetthreshold" title="ResetThreshold">ResetThreshold</a>: <i>Double</i>
<a href="#watermarkthresholds" title="WatermarkThresholds">WatermarkThresholds</a>: <i>
      - Double</i>
</pre>

## Properties

#### MetricsEventThresholdType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WatermarkThresholds

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

