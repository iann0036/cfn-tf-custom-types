# Terraform::AWS::AutoscalingPolicy

Provides an AutoScaling Scaling Policy resource.

~> **NOTE:** You may want to omit `desired_capacity` attribute from attached `aws_autoscaling_group`
when using autoscaling policies. It's good practice to pick either
[manual](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-manual-scaling.html)
or [dynamic](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-scale-based-on-demand.html)
(policy-based) scaling.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::AutoscalingPolicy",
    "Properties" : {
        "<a href="#adjustmenttype" title="AdjustmentType">AdjustmentType</a>" : <i>String</i>,
        "<a href="#autoscalinggroupname" title="AutoscalingGroupName">AutoscalingGroupName</a>" : <i>String</i>,
        "<a href="#cooldown" title="Cooldown">Cooldown</a>" : <i>Double</i>,
        "<a href="#estimatedinstancewarmup" title="EstimatedInstanceWarmup">EstimatedInstanceWarmup</a>" : <i>Double</i>,
        "<a href="#metricaggregationtype" title="MetricAggregationType">MetricAggregationType</a>" : <i>String</i>,
        "<a href="#minadjustmentmagnitude" title="MinAdjustmentMagnitude">MinAdjustmentMagnitude</a>" : <i>Double</i>,
        "<a href="#minadjustmentstep" title="MinAdjustmentStep">MinAdjustmentStep</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policytype" title="PolicyType">PolicyType</a>" : <i>String</i>,
        "<a href="#scalingadjustment" title="ScalingAdjustment">ScalingAdjustment</a>" : <i>Double</i>,
        "<a href="#stepadjustment" title="StepAdjustment">StepAdjustment</a>" : <i>[ <a href="stepadjustment.md">StepAdjustment</a>, ... ]</i>,
        "<a href="#targettrackingconfiguration" title="TargetTrackingConfiguration">TargetTrackingConfiguration</a>" : <i>[ <a href="targettrackingconfiguration.md">TargetTrackingConfiguration</a>, ... ]</i>,
        "<a href="#customizedmetricspecification" title="CustomizedMetricSpecification">CustomizedMetricSpecification</a>" : <i>[ <a href="customizedmetricspecification.md">CustomizedMetricSpecification</a>, ... ]</i>,
        "<a href="#predefinedmetricspecification" title="PredefinedMetricSpecification">PredefinedMetricSpecification</a>" : <i>[ <a href="predefinedmetricspecification.md">PredefinedMetricSpecification</a>, ... ]</i>,
        "<a href="#metricdimension" title="MetricDimension">MetricDimension</a>" : <i>[ <a href="metricdimension.md">MetricDimension</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::AutoscalingPolicy
Properties:
    <a href="#adjustmenttype" title="AdjustmentType">AdjustmentType</a>: <i>String</i>
    <a href="#autoscalinggroupname" title="AutoscalingGroupName">AutoscalingGroupName</a>: <i>String</i>
    <a href="#cooldown" title="Cooldown">Cooldown</a>: <i>Double</i>
    <a href="#estimatedinstancewarmup" title="EstimatedInstanceWarmup">EstimatedInstanceWarmup</a>: <i>Double</i>
    <a href="#metricaggregationtype" title="MetricAggregationType">MetricAggregationType</a>: <i>String</i>
    <a href="#minadjustmentmagnitude" title="MinAdjustmentMagnitude">MinAdjustmentMagnitude</a>: <i>Double</i>
    <a href="#minadjustmentstep" title="MinAdjustmentStep">MinAdjustmentStep</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policytype" title="PolicyType">PolicyType</a>: <i>String</i>
    <a href="#scalingadjustment" title="ScalingAdjustment">ScalingAdjustment</a>: <i>Double</i>
    <a href="#stepadjustment" title="StepAdjustment">StepAdjustment</a>: <i>
      - <a href="stepadjustment.md">StepAdjustment</a></i>
    <a href="#targettrackingconfiguration" title="TargetTrackingConfiguration">TargetTrackingConfiguration</a>: <i>
      - <a href="targettrackingconfiguration.md">TargetTrackingConfiguration</a></i>
    <a href="#customizedmetricspecification" title="CustomizedMetricSpecification">CustomizedMetricSpecification</a>: <i>
      - <a href="customizedmetricspecification.md">CustomizedMetricSpecification</a></i>
    <a href="#predefinedmetricspecification" title="PredefinedMetricSpecification">PredefinedMetricSpecification</a>: <i>
      - <a href="predefinedmetricspecification.md">PredefinedMetricSpecification</a></i>
    <a href="#metricdimension" title="MetricDimension">MetricDimension</a>: <i>
      - <a href="metricdimension.md">MetricDimension</a></i>
</pre>

## Properties

#### AdjustmentType

Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscalingGroupName

The name of the autoscaling group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cooldown

The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EstimatedInstanceWarmup

The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group's specified cooldown period.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricAggregationType

The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and "Average". Without a value, AWS will treat the aggregation type as "Average".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinAdjustmentMagnitude

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinAdjustmentStep

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyType

The policy type, either "SimpleScaling", "StepScaling" or "TargetTrackingScaling". If this value isn't provided, AWS will default to "SimpleScaling.".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingAdjustment

The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StepAdjustment

_Required_: No

_Type_: List of <a href="stepadjustment.md">StepAdjustment</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetTrackingConfiguration

_Required_: No

_Type_: List of <a href="targettrackingconfiguration.md">TargetTrackingConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomizedMetricSpecification

_Required_: No

_Type_: List of <a href="customizedmetricspecification.md">CustomizedMetricSpecification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PredefinedMetricSpecification

_Required_: No

_Type_: List of <a href="predefinedmetricspecification.md">PredefinedMetricSpecification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricDimension

_Required_: No

_Type_: List of <a href="metricdimension.md">MetricDimension</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

