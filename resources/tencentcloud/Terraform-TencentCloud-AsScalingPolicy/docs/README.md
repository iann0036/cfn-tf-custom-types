# Terraform::TencentCloud::AsScalingPolicy

Provides a resource for an AS (Auto scaling) policy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::AsScalingPolicy",
    "Properties" : {
        "<a href="#adjustmenttype" title="AdjustmentType">AdjustmentType</a>" : <i>String</i>,
        "<a href="#adjustmentvalue" title="AdjustmentValue">AdjustmentValue</a>" : <i>Double</i>,
        "<a href="#comparisonoperator" title="ComparisonOperator">ComparisonOperator</a>" : <i>String</i>,
        "<a href="#continuoustime" title="ContinuousTime">ContinuousTime</a>" : <i>Double</i>,
        "<a href="#cooldown" title="Cooldown">Cooldown</a>" : <i>Double</i>,
        "<a href="#metricname" title="MetricName">MetricName</a>" : <i>String</i>,
        "<a href="#notificationusergroupids" title="NotificationUserGroupIds">NotificationUserGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#policyname" title="PolicyName">PolicyName</a>" : <i>String</i>,
        "<a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>" : <i>String</i>,
        "<a href="#statistic" title="Statistic">Statistic</a>" : <i>String</i>,
        "<a href="#threshold" title="Threshold">Threshold</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::AsScalingPolicy
Properties:
    <a href="#adjustmenttype" title="AdjustmentType">AdjustmentType</a>: <i>String</i>
    <a href="#adjustmentvalue" title="AdjustmentValue">AdjustmentValue</a>: <i>Double</i>
    <a href="#comparisonoperator" title="ComparisonOperator">ComparisonOperator</a>: <i>String</i>
    <a href="#continuoustime" title="ContinuousTime">ContinuousTime</a>: <i>Double</i>
    <a href="#cooldown" title="Cooldown">Cooldown</a>: <i>Double</i>
    <a href="#metricname" title="MetricName">MetricName</a>: <i>String</i>
    <a href="#notificationusergroupids" title="NotificationUserGroupIds">NotificationUserGroupIds</a>: <i>
      - String</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#policyname" title="PolicyName">PolicyName</a>: <i>String</i>
    <a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>: <i>String</i>
    <a href="#statistic" title="Statistic">Statistic</a>: <i>String</i>
    <a href="#threshold" title="Threshold">Threshold</a>: <i>Double</i>
</pre>

## Properties

#### AdjustmentType

Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Available values include CHANGE_IN_CAPACITY, EXACT_CAPACITY and PERCENT_CHANGE_IN_CAPACITY.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdjustmentValue

Define the number of instances by which to scale.For CHANGE_IN_CAPACITY type or PERCENT_CHANGE_IN_CAPACITY, a positive increment adds to the current capacity and a negative value removes from the current capacity. For EXACT_CAPACITY type, it defines an absolute number of the existing Auto Scaling group size.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComparisonOperator

Comparison operator, of which valid values can be GREATER_THAN, GREATER_THAN_OR_EQUAL_TO, LESS_THAN, LESS_THAN_OR_EQUAL_TO, EQUAL_TO and NOT_EQUAL_TO.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContinuousTime

Retry times (1~10).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cooldown

Cooldwon time in second. Default is 300.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricName

Name of an indicator, which can be CPU_UTILIZATION, MEM_UTILIZATION, LAN_TRAFFIC_OUT, LAN_TRAFFIC_IN, WAN_TRAFFIC_OUT and WAN_TRAFFIC_IN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationUserGroupIds

An ID group of users to be notified when an alarm is triggered.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

Time period in second, of which valid values can be 60 and 300.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyName

Name of a policy used to define a reaction when an alarm is triggered.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingGroupId

ID of a scaling group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Statistic

Statistic types, include AVERAGE, MAXIMUM and MINIMUM. Default is AVERAGE.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

Alarm threshold.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

