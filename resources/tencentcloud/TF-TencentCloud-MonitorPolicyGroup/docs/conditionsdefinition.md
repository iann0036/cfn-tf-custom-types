# TF::TencentCloud::MonitorPolicyGroup ConditionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alarmnotifyperiod" title="AlarmNotifyPeriod">AlarmNotifyPeriod</a>" : <i>Double</i>,
    "<a href="#alarmnotifytype" title="AlarmNotifyType">AlarmNotifyType</a>" : <i>Double</i>,
    "<a href="#calcperiod" title="CalcPeriod">CalcPeriod</a>" : <i>Double</i>,
    "<a href="#calctype" title="CalcType">CalcType</a>" : <i>Double</i>,
    "<a href="#calcvalue" title="CalcValue">CalcValue</a>" : <i>Double</i>,
    "<a href="#continueperiod" title="ContinuePeriod">ContinuePeriod</a>" : <i>Double</i>,
    "<a href="#metricid" title="MetricId">MetricId</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#alarmnotifyperiod" title="AlarmNotifyPeriod">AlarmNotifyPeriod</a>: <i>Double</i>
<a href="#alarmnotifytype" title="AlarmNotifyType">AlarmNotifyType</a>: <i>Double</i>
<a href="#calcperiod" title="CalcPeriod">CalcPeriod</a>: <i>Double</i>
<a href="#calctype" title="CalcType">CalcType</a>: <i>Double</i>
<a href="#calcvalue" title="CalcValue">CalcValue</a>: <i>Double</i>
<a href="#continueperiod" title="ContinuePeriod">ContinuePeriod</a>: <i>Double</i>
<a href="#metricid" title="MetricId">MetricId</a>: <i>Double</i>
</pre>

## Properties

#### AlarmNotifyPeriod

Alarm sending cycle per second. <0 does not fire, `0` only fires once, and >0 fires every triggerTime second.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmNotifyType

Alarm sending convergence type. `0` continuous alarm, `1` index alarm.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CalcPeriod

Data aggregation cycle (unit of second), if the metric has a default value can not be filled, refer to `data.tencentcloud_monitor_policy_conditions(period_keys)`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CalcType

Compare type. Valid value ranges: [1~12]. `1` means more than, `2` means greater than or equal, `3` means less than, `4` means less than or equal to, `5` means equal, `6` means not equal, `7` means days rose, `8` means days fell, `9` means weeks rose, `10` means weeks fell, `11` means period rise, `12` means period fell, refer to `data.tencentcloud_monitor_policy_conditions(calc_type_keys)`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CalcValue

Threshold value, refer to `data.tencentcloud_monitor_policy_conditions(calc_value_*)`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContinuePeriod

The rule triggers an alert that lasts for several detection cycles, refer to `data.tencentcloud_monitor_policy_conditions(period_num_keys)`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricId

Id of the metric, refer to `data.tencentcloud_monitor_policy_conditions(metric_id)`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

