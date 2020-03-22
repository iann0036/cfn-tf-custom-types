# Terraform::Alicloud::EssScalingRule

Provides a ESS scaling rule resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::EssScalingRule",
    "Properties" : {
        "<a href="#adjustmenttype" title="AdjustmentType">AdjustmentType</a>" : <i>String</i>,
        "<a href="#adjustmentvalue" title="AdjustmentValue">AdjustmentValue</a>" : <i>Double</i>,
        "<a href="#cooldown" title="Cooldown">Cooldown</a>" : <i>Double</i>,
        "<a href="#disablescalein" title="DisableScaleIn">DisableScaleIn</a>" : <i>Boolean</i>,
        "<a href="#estimatedinstancewarmup" title="EstimatedInstanceWarmup">EstimatedInstanceWarmup</a>" : <i>Double</i>,
        "<a href="#metricname" title="MetricName">MetricName</a>" : <i>String</i>,
        "<a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>" : <i>String</i>,
        "<a href="#scalingrulename" title="ScalingRuleName">ScalingRuleName</a>" : <i>String</i>,
        "<a href="#scalingruletype" title="ScalingRuleType">ScalingRuleType</a>" : <i>String</i>,
        "<a href="#targetvalue" title="TargetValue">TargetValue</a>" : <i>Double</i>,
        "<a href="#stepadjustment" title="StepAdjustment">StepAdjustment</a>" : <i>[ <a href="stepadjustment.md">StepAdjustment</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::EssScalingRule
Properties:
    <a href="#adjustmenttype" title="AdjustmentType">AdjustmentType</a>: <i>String</i>
    <a href="#adjustmentvalue" title="AdjustmentValue">AdjustmentValue</a>: <i>Double</i>
    <a href="#cooldown" title="Cooldown">Cooldown</a>: <i>Double</i>
    <a href="#disablescalein" title="DisableScaleIn">DisableScaleIn</a>: <i>Boolean</i>
    <a href="#estimatedinstancewarmup" title="EstimatedInstanceWarmup">EstimatedInstanceWarmup</a>: <i>Double</i>
    <a href="#metricname" title="MetricName">MetricName</a>: <i>String</i>
    <a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>: <i>String</i>
    <a href="#scalingrulename" title="ScalingRuleName">ScalingRuleName</a>: <i>String</i>
    <a href="#scalingruletype" title="ScalingRuleType">ScalingRuleType</a>: <i>String</i>
    <a href="#targetvalue" title="TargetValue">TargetValue</a>: <i>Double</i>
    <a href="#stepadjustment" title="StepAdjustment">StepAdjustment</a>: <i>
      - <a href="stepadjustment.md">StepAdjustment</a></i>
</pre>

## Properties

#### AdjustmentType

Adjustment mode of a scaling rule. Optional values:
- QuantityChangeInCapacity: It is used to increase or decrease a specified number of ECS instances.
- PercentChangeInCapacity: It is used to increase or decrease a specified proportion of ECS instances.
- TotalCapacity: It is used to adjust the quantity of ECS instances in the current scaling group to a specified value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdjustmentValue

Adjusted value of a scaling rule. Value range:
- QuantityChangeInCapacity：(0, 500] U (-500, 0]
- PercentChangeInCapacity：[0, 10000] U [-100, 0]
- TotalCapacity：[0, 1000].

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cooldown

Cool-down time of a scaling rule. Value range: [0, 86,400], in seconds. The default value is empty，if not set, the return value will be 0, which is the default value of integer.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableScaleIn

Indicates whether scale in by the target tracking policy is disabled. Default to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EstimatedInstanceWarmup

The estimated time, in seconds, until a newly launched instance will contribute CloudMonitor metrics. Default to 300.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricName

A CloudMonitor metric name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingGroupId

ID of the scaling group of a scaling rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingRuleName

Name shown for the scaling rule, which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain number, underscores `_`, hypens `-`, and decimal point `.`. If this parameter value is not specified, the default value is scaling rule id.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingRuleType

The scaling rule type, either "SimpleScalingRule", "TargetTrackingScalingRule", "StepScalingRule". Default to "SimpleScalingRule".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetValue

The target value for the metric.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StepAdjustment

_Required_: No

_Type_: List of <a href="stepadjustment.md">StepAdjustment</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Ari

Returns the <code>Ari</code> value.

#### Id

Returns the <code>Id</code> value.

