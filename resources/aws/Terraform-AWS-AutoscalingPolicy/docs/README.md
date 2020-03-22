# Terraform::AWS::AutoscalingPolicy

CloudFormation equivalent of aws_autoscaling_policy

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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscalingGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cooldown

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EstimatedInstanceWarmup

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

#### MinAdjustmentStep

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingAdjustment

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

