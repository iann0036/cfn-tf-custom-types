# Terraform::Alicloud::EssAlarm

Provides a ESS alarm task resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::EssAlarm",
    "Properties" : {
        "<a href="#alarmactions" title="AlarmActions">AlarmActions</a>" : <i>[ String, ... ]</i>,
        "<a href="#cloudmonitorgroupid" title="CloudMonitorGroupId">CloudMonitorGroupId</a>" : <i>Double</i>,
        "<a href="#comparisonoperator" title="ComparisonOperator">ComparisonOperator</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dimensions" title="Dimensions">Dimensions</a>" : <i>[ <a href="dimensions.md">Dimensions</a>, ... ]</i>,
        "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
        "<a href="#evaluationcount" title="EvaluationCount">EvaluationCount</a>" : <i>Double</i>,
        "<a href="#metricname" title="MetricName">MetricName</a>" : <i>String</i>,
        "<a href="#metrictype" title="MetricType">MetricType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>" : <i>String</i>,
        "<a href="#statistics" title="Statistics">Statistics</a>" : <i>String</i>,
        "<a href="#threshold" title="Threshold">Threshold</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::EssAlarm
Properties:
    <a href="#alarmactions" title="AlarmActions">AlarmActions</a>: <i>
      - String</i>
    <a href="#cloudmonitorgroupid" title="CloudMonitorGroupId">CloudMonitorGroupId</a>: <i>Double</i>
    <a href="#comparisonoperator" title="ComparisonOperator">ComparisonOperator</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dimensions" title="Dimensions">Dimensions</a>: <i>
      - <a href="dimensions.md">Dimensions</a></i>
    <a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
    <a href="#evaluationcount" title="EvaluationCount">EvaluationCount</a>: <i>Double</i>
    <a href="#metricname" title="MetricName">MetricName</a>: <i>String</i>
    <a href="#metrictype" title="MetricType">MetricType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>: <i>String</i>
    <a href="#statistics" title="Statistics">Statistics</a>: <i>String</i>
    <a href="#threshold" title="Threshold">Threshold</a>: <i>String</i>
</pre>

## Properties

#### AlarmActions

The list of actions to execute when this alarm transition into an ALARM state. Each action is specified as ess scaling rule ari.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudMonitorGroupId

Defines the application group id defined by CMS which is assigned when you upload custom metric to CMS, only available for custom metirc.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComparisonOperator

The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Supported value: >=, <=, >, <. Defaults to >=.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description for the alarm.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimensions

The dimension map for the alarm's associated metric (documented below). For all metrics, you can not set the dimension key as "scaling_group" or "userId", which is set by default, the second dimension for metric, such as "device" for "PackagesNetIn", need to be set by users.

_Required_: No

_Type_: List of <a href="dimensions.md">Dimensions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable

Whether to enable specific ess alarm. Default to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvaluationCount

The number of times that needs to satisfies comparison condition before transition into ALARM state. Defaults to 3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricName

The name for the alarm's associated metric. See [Block_metricNames_and_dimensions](#block-metricnames_and_dimensions) below for details.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricType

The type for the alarm's associated metric. Supported value: system, custom. "system" means the metric data is collected by Aliyun Cloud Monitor Service(CMS), "custom" means the metric data is upload to CMS by users. Defaults to system.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name for ess alarm.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

The period in seconds over which the specified statistic is applied. Supported value: 60, 120, 300, 900. Defaults to 300.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingGroupId

The scaling group associated with this alarm, the 'ForceNew' attribute is available in 1.56.0+.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Statistics

The statistic to apply to the alarm's associated metric. Supported value: Average, Minimum, Maximum. Defaults to Average.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

The value against which the specified statistics is compared.

_Required_: Yes

_Type_: String

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

#### State

Returns the <code>State</code> value.

