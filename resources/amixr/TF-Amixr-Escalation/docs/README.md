# TF::Amixr::Escalation

[Escalation policy](https://api-docs.amixr.io/#escalation-policies) configures what happened after incident is triggered: who will be notified first, second, etc., and delay before notifications.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Amixr::Escalation",
    "Properties" : {
        "<a href="#actiontotrigger" title="ActionToTrigger">ActionToTrigger</a>" : <i>String</i>,
        "<a href="#duration" title="Duration">Duration</a>" : <i>Double</i>,
        "<a href="#grouptonotify" title="GroupToNotify">GroupToNotify</a>" : <i>String</i>,
        "<a href="#important" title="Important">Important</a>" : <i>Boolean</i>,
        "<a href="#notifyiftimefrom" title="NotifyIfTimeFrom">NotifyIfTimeFrom</a>" : <i>String</i>,
        "<a href="#notifyiftimeto" title="NotifyIfTimeTo">NotifyIfTimeTo</a>" : <i>String</i>,
        "<a href="#notifyoncallfromschedule" title="NotifyOnCallFromSchedule">NotifyOnCallFromSchedule</a>" : <i>String</i>,
        "<a href="#personstonotify" title="PersonsToNotify">PersonsToNotify</a>" : <i>[ String, ... ]</i>,
        "<a href="#personstonotifynexteachtime" title="PersonsToNotifyNextEachTime">PersonsToNotifyNextEachTime</a>" : <i>[ String, ... ]</i>,
        "<a href="#position" title="Position">Position</a>" : <i>Double</i>,
        "<a href="#routeid" title="RouteId">RouteId</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Amixr::Escalation
Properties:
    <a href="#actiontotrigger" title="ActionToTrigger">ActionToTrigger</a>: <i>String</i>
    <a href="#duration" title="Duration">Duration</a>: <i>Double</i>
    <a href="#grouptonotify" title="GroupToNotify">GroupToNotify</a>: <i>String</i>
    <a href="#important" title="Important">Important</a>: <i>Boolean</i>
    <a href="#notifyiftimefrom" title="NotifyIfTimeFrom">NotifyIfTimeFrom</a>: <i>String</i>
    <a href="#notifyiftimeto" title="NotifyIfTimeTo">NotifyIfTimeTo</a>: <i>String</i>
    <a href="#notifyoncallfromschedule" title="NotifyOnCallFromSchedule">NotifyOnCallFromSchedule</a>: <i>String</i>
    <a href="#personstonotify" title="PersonsToNotify">PersonsToNotify</a>: <i>
      - String</i>
    <a href="#personstonotifynexteachtime" title="PersonsToNotifyNextEachTime">PersonsToNotifyNextEachTime</a>: <i>
      - String</i>
    <a href="#position" title="Position">Position</a>: <i>Double</i>
    <a href="#routeid" title="RouteId">RouteId</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### ActionToTrigger

ID of an Action for `trigger_action` type step.
* `group_to_notify` - (Optional) ID of a User Group for `notify_user_group` type step.
* `notify_if_time_from` - (Optional) The beginning of the time interval for `notify_if_time_from_to` type step in UTC (for example 08:00:00Z).
* `notify_if_time_to` - (Optional) The end of the time interval for `notify_if_time_from_to` type step in UTC (for example 18:00:00Z).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

The duration of delay for `wait` type step.
* `persons_to_notify` - (Optional) The list of ID's of users for `notify_persons` type step.
* `persons_to_notify_next_each_time` - (Optional) The list of ID's of users for `notify_person_next_each_time` type step.
* `notify_on_call_from_schedule` - (Optional) ID of a Schedule for `notify_on_call_from_schedule` type step.
* `action_to_trigger` - (Optional) ID of an Action for `trigger_action` type step.
* `group_to_notify` - (Optional) ID of a User Group for `notify_user_group` type step.
* `notify_if_time_from` - (Optional) The beginning of the time interval for `notify_if_time_from_to` type step in UTC (for example 08:00:00Z).
* `notify_if_time_to` - (Optional) The end of the time interval for `notify_if_time_from_to` type step in UTC (for example 18:00:00Z).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupToNotify

ID of a User Group for `notify_user_group` type step.
* `notify_if_time_from` - (Optional) The beginning of the time interval for `notify_if_time_from_to` type step in UTC (for example 08:00:00Z).
* `notify_if_time_to` - (Optional) The end of the time interval for `notify_if_time_from_to` type step in UTC (for example 18:00:00Z).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Important

Will activate "important" personal notification rules. Can be `true` or `false`. Actual for steps: `notify_persons`, `notify_on_call_from_schedule` and `notify_user_group`.
* `duration` - (Optional) The duration of delay for `wait` type step.
* `persons_to_notify` - (Optional) The list of ID's of users for `notify_persons` type step.
* `persons_to_notify_next_each_time` - (Optional) The list of ID's of users for `notify_person_next_each_time` type step.
* `notify_on_call_from_schedule` - (Optional) ID of a Schedule for `notify_on_call_from_schedule` type step.
* `action_to_trigger` - (Optional) ID of an Action for `trigger_action` type step.
* `group_to_notify` - (Optional) ID of a User Group for `notify_user_group` type step.
* `notify_if_time_from` - (Optional) The beginning of the time interval for `notify_if_time_from_to` type step in UTC (for example 08:00:00Z).
* `notify_if_time_to` - (Optional) The end of the time interval for `notify_if_time_from_to` type step in UTC (for example 18:00:00Z).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyIfTimeFrom

The beginning of the time interval for `notify_if_time_from_to` type step in UTC (for example 08:00:00Z).
* `notify_if_time_to` - (Optional) The end of the time interval for `notify_if_time_from_to` type step in UTC (for example 18:00:00Z).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyIfTimeTo

The end of the time interval for `notify_if_time_from_to` type step in UTC (for example 18:00:00Z).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyOnCallFromSchedule

ID of a Schedule for `notify_on_call_from_schedule` type step.
* `action_to_trigger` - (Optional) ID of an Action for `trigger_action` type step.
* `group_to_notify` - (Optional) ID of a User Group for `notify_user_group` type step.
* `notify_if_time_from` - (Optional) The beginning of the time interval for `notify_if_time_from_to` type step in UTC (for example 08:00:00Z).
* `notify_if_time_to` - (Optional) The end of the time interval for `notify_if_time_from_to` type step in UTC (for example 18:00:00Z).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersonsToNotify

The list of ID's of users for `notify_persons` type step.
* `persons_to_notify_next_each_time` - (Optional) The list of ID's of users for `notify_person_next_each_time` type step.
* `notify_on_call_from_schedule` - (Optional) ID of a Schedule for `notify_on_call_from_schedule` type step.
* `action_to_trigger` - (Optional) ID of an Action for `trigger_action` type step.
* `group_to_notify` - (Optional) ID of a User Group for `notify_user_group` type step.
* `notify_if_time_from` - (Optional) The beginning of the time interval for `notify_if_time_from_to` type step in UTC (for example 08:00:00Z).
* `notify_if_time_to` - (Optional) The end of the time interval for `notify_if_time_from_to` type step in UTC (for example 18:00:00Z).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersonsToNotifyNextEachTime

The list of ID's of users for `notify_person_next_each_time` type step.
* `notify_on_call_from_schedule` - (Optional) ID of a Schedule for `notify_on_call_from_schedule` type step.
* `action_to_trigger` - (Optional) ID of an Action for `trigger_action` type step.
* `group_to_notify` - (Optional) ID of a User Group for `notify_user_group` type step.
* `notify_if_time_from` - (Optional) The beginning of the time interval for `notify_if_time_from_to` type step in UTC (for example 08:00:00Z).
* `notify_if_time_to` - (Optional) The end of the time interval for `notify_if_time_from_to` type step in UTC (for example 18:00:00Z).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Position

The position of the escalation step (starts from 0)
* `type` - (Optional) The type of escalation policy. Can be:
- `wait` - just wait
- `notify_persons` - notify multiple users at the same time
- `notify_person_next_each_time` - notify one user from queue
- `notify_on_call_from_schedule` - notify by schedule
- `notify_user_group` - notify User Group (available for teams with Slack integration)
- `trigger_action` - trigger action (outgoing webhook)
- `notify_if_time_from_to` - continue escalation only if the time is within the selected interval
- `notify_whole_channel` - notify a channel in Slack (available for teams with Slack integration)
- `resolve` - resolve incident
- `null` - do nothing
* `important` - (Optional) Will activate "important" personal notification rules. Can be `true` or `false`. Actual for steps: `notify_persons`, `notify_on_call_from_schedule` and `notify_user_group`.
* `duration` - (Optional) The duration of delay for `wait` type step.
* `persons_to_notify` - (Optional) The list of ID's of users for `notify_persons` type step.
* `persons_to_notify_next_each_time` - (Optional) The list of ID's of users for `notify_person_next_each_time` type step.
* `notify_on_call_from_schedule` - (Optional) ID of a Schedule for `notify_on_call_from_schedule` type step.
* `action_to_trigger` - (Optional) ID of an Action for `trigger_action` type step.
* `group_to_notify` - (Optional) ID of a User Group for `notify_user_group` type step.
* `notify_if_time_from` - (Optional) The beginning of the time interval for `notify_if_time_from_to` type step in UTC (for example 08:00:00Z).
* `notify_if_time_to` - (Optional) The end of the time interval for `notify_if_time_from_to` type step in UTC (for example 18:00:00Z).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteId

The ID of the route.
* `position` - (Required) The position of the escalation step (starts from 0)
* `type` - (Optional) The type of escalation policy. Can be:
- `wait` - just wait
- `notify_persons` - notify multiple users at the same time
- `notify_person_next_each_time` - notify one user from queue
- `notify_on_call_from_schedule` - notify by schedule
- `notify_user_group` - notify User Group (available for teams with Slack integration)
- `trigger_action` - trigger action (outgoing webhook)
- `notify_if_time_from_to` - continue escalation only if the time is within the selected interval
- `notify_whole_channel` - notify a channel in Slack (available for teams with Slack integration)
- `resolve` - resolve incident
- `null` - do nothing
* `important` - (Optional) Will activate "important" personal notification rules. Can be `true` or `false`. Actual for steps: `notify_persons`, `notify_on_call_from_schedule` and `notify_user_group`.
* `duration` - (Optional) The duration of delay for `wait` type step.
* `persons_to_notify` - (Optional) The list of ID's of users for `notify_persons` type step.
* `persons_to_notify_next_each_time` - (Optional) The list of ID's of users for `notify_person_next_each_time` type step.
* `notify_on_call_from_schedule` - (Optional) ID of a Schedule for `notify_on_call_from_schedule` type step.
* `action_to_trigger` - (Optional) ID of an Action for `trigger_action` type step.
* `group_to_notify` - (Optional) ID of a User Group for `notify_user_group` type step.
* `notify_if_time_from` - (Optional) The beginning of the time interval for `notify_if_time_from_to` type step in UTC (for example 08:00:00Z).
* `notify_if_time_to` - (Optional) The end of the time interval for `notify_if_time_from_to` type step in UTC (for example 18:00:00Z).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of escalation policy. Can be:
- `wait` - just wait
- `notify_persons` - notify multiple users at the same time
- `notify_person_next_each_time` - notify one user from queue
- `notify_on_call_from_schedule` - notify by schedule
- `notify_user_group` - notify User Group (available for teams with Slack integration)
- `trigger_action` - trigger action (outgoing webhook)
- `notify_if_time_from_to` - continue escalation only if the time is within the selected interval
- `notify_whole_channel` - notify a channel in Slack (available for teams with Slack integration)
- `resolve` - resolve incident
- `null` - do nothing
* `important` - (Optional) Will activate "important" personal notification rules. Can be `true` or `false`. Actual for steps: `notify_persons`, `notify_on_call_from_schedule` and `notify_user_group`.
* `duration` - (Optional) The duration of delay for `wait` type step.
* `persons_to_notify` - (Optional) The list of ID's of users for `notify_persons` type step.
* `persons_to_notify_next_each_time` - (Optional) The list of ID's of users for `notify_person_next_each_time` type step.
* `notify_on_call_from_schedule` - (Optional) ID of a Schedule for `notify_on_call_from_schedule` type step.
* `action_to_trigger` - (Optional) ID of an Action for `trigger_action` type step.
* `group_to_notify` - (Optional) ID of a User Group for `notify_user_group` type step.
* `notify_if_time_from` - (Optional) The beginning of the time interval for `notify_if_time_from_to` type step in UTC (for example 08:00:00Z).
* `notify_if_time_to` - (Optional) The end of the time interval for `notify_if_time_from_to` type step in UTC (for example 18:00:00Z).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

