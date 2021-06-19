# TF::AWS::AutoscalingplansScalingPlan TargetTrackingConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disablescalein" title="DisableScaleIn">DisableScaleIn</a>" : <i>Boolean</i>,
    "<a href="#estimatedinstancewarmup" title="EstimatedInstanceWarmup">EstimatedInstanceWarmup</a>" : <i>Double</i>,
    "<a href="#scaleincooldown" title="ScaleInCooldown">ScaleInCooldown</a>" : <i>Double</i>,
    "<a href="#scaleoutcooldown" title="ScaleOutCooldown">ScaleOutCooldown</a>" : <i>Double</i>,
    "<a href="#targetvalue" title="TargetValue">TargetValue</a>" : <i>Double</i>,
    "<a href="#customizedscalingmetricspecification" title="CustomizedScalingMetricSpecification">CustomizedScalingMetricSpecification</a>" : <i>[ <a href="customizedscalingmetricspecificationdefinition.md">CustomizedScalingMetricSpecificationDefinition</a>, ... ]</i>,
    "<a href="#predefinedscalingmetricspecification" title="PredefinedScalingMetricSpecification">PredefinedScalingMetricSpecification</a>" : <i>[ <a href="predefinedscalingmetricspecificationdefinition.md">PredefinedScalingMetricSpecificationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disablescalein" title="DisableScaleIn">DisableScaleIn</a>: <i>Boolean</i>
<a href="#estimatedinstancewarmup" title="EstimatedInstanceWarmup">EstimatedInstanceWarmup</a>: <i>Double</i>
<a href="#scaleincooldown" title="ScaleInCooldown">ScaleInCooldown</a>: <i>Double</i>
<a href="#scaleoutcooldown" title="ScaleOutCooldown">ScaleOutCooldown</a>: <i>Double</i>
<a href="#targetvalue" title="TargetValue">TargetValue</a>: <i>Double</i>
<a href="#customizedscalingmetricspecification" title="CustomizedScalingMetricSpecification">CustomizedScalingMetricSpecification</a>: <i>
      - <a href="customizedscalingmetricspecificationdefinition.md">CustomizedScalingMetricSpecificationDefinition</a></i>
<a href="#predefinedscalingmetricspecification" title="PredefinedScalingMetricSpecification">PredefinedScalingMetricSpecification</a>: <i>
      - <a href="predefinedscalingmetricspecificationdefinition.md">PredefinedScalingMetricSpecificationDefinition</a></i>
</pre>

## Properties

#### DisableScaleIn

Boolean indicating whether scale in by the target tracking scaling policy is disabled. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EstimatedInstanceWarmup

The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics.
This value is used only if the resource is an Auto Scaling group.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleInCooldown

The amount of time, in seconds, after a scale in activity completes before another scale in activity can start.
This value is not used if the scalable resource is an Auto Scaling group.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleOutCooldown

The amount of time, in seconds, after a scale-out activity completes before another scale-out activity can start.
This value is not used if the scalable resource is an Auto Scaling group.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetValue

The target value for the metric.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomizedScalingMetricSpecification

_Required_: No

_Type_: List of <a href="customizedscalingmetricspecificationdefinition.md">CustomizedScalingMetricSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PredefinedScalingMetricSpecification

_Required_: No

_Type_: List of <a href="predefinedscalingmetricspecificationdefinition.md">PredefinedScalingMetricSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

