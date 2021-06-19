# TF::AWS::AppautoscalingPolicy StepScalingPolicyConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adjustmenttype" title="AdjustmentType">AdjustmentType</a>" : <i>String</i>,
    "<a href="#cooldown" title="Cooldown">Cooldown</a>" : <i>Double</i>,
    "<a href="#metricaggregationtype" title="MetricAggregationType">MetricAggregationType</a>" : <i>String</i>,
    "<a href="#minadjustmentmagnitude" title="MinAdjustmentMagnitude">MinAdjustmentMagnitude</a>" : <i>Double</i>,
    "<a href="#stepadjustment" title="StepAdjustment">StepAdjustment</a>" : <i>[ <a href="stepadjustmentdefinition.md">StepAdjustmentDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#adjustmenttype" title="AdjustmentType">AdjustmentType</a>: <i>String</i>
<a href="#cooldown" title="Cooldown">Cooldown</a>: <i>Double</i>
<a href="#metricaggregationtype" title="MetricAggregationType">MetricAggregationType</a>: <i>String</i>
<a href="#minadjustmentmagnitude" title="MinAdjustmentMagnitude">MinAdjustmentMagnitude</a>: <i>Double</i>
<a href="#stepadjustment" title="StepAdjustment">StepAdjustment</a>: <i>
      - <a href="stepadjustmentdefinition.md">StepAdjustmentDefinition</a></i>
</pre>

## Properties

#### AdjustmentType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cooldown

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricAggregationType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinAdjustmentMagnitude

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StepAdjustment

_Required_: No

_Type_: List of <a href="stepadjustmentdefinition.md">StepAdjustmentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

