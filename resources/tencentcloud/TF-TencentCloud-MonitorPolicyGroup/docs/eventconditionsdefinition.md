# TF::TencentCloud::MonitorPolicyGroup EventConditionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alarmnotifyperiod" title="AlarmNotifyPeriod">AlarmNotifyPeriod</a>" : <i>Double</i>,
    "<a href="#alarmnotifytype" title="AlarmNotifyType">AlarmNotifyType</a>" : <i>Double</i>,
    "<a href="#eventid" title="EventId">EventId</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#alarmnotifyperiod" title="AlarmNotifyPeriod">AlarmNotifyPeriod</a>: <i>Double</i>
<a href="#alarmnotifytype" title="AlarmNotifyType">AlarmNotifyType</a>: <i>Double</i>
<a href="#eventid" title="EventId">EventId</a>: <i>Double</i>
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

#### EventId

The ID of this event metric, refer to `data.tencentcloud_monitor_policy_conditions(event_id).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

