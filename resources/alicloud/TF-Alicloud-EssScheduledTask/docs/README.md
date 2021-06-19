# TF::Alicloud::EssScheduledTask

Provides a ESS schedule resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::EssScheduledTask",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>" : <i>Double</i>,
        "<a href="#launchexpirationtime" title="LaunchExpirationTime">LaunchExpirationTime</a>" : <i>Double</i>,
        "<a href="#launchtime" title="LaunchTime">LaunchTime</a>" : <i>String</i>,
        "<a href="#maxvalue" title="MaxValue">MaxValue</a>" : <i>Double</i>,
        "<a href="#minvalue" title="MinValue">MinValue</a>" : <i>Double</i>,
        "<a href="#recurrenceendtime" title="RecurrenceEndTime">RecurrenceEndTime</a>" : <i>String</i>,
        "<a href="#recurrencetype" title="RecurrenceType">RecurrenceType</a>" : <i>String</i>,
        "<a href="#recurrencevalue" title="RecurrenceValue">RecurrenceValue</a>" : <i>String</i>,
        "<a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>" : <i>String</i>,
        "<a href="#scheduledaction" title="ScheduledAction">ScheduledAction</a>" : <i>String</i>,
        "<a href="#scheduledtaskname" title="ScheduledTaskName">ScheduledTaskName</a>" : <i>String</i>,
        "<a href="#taskenabled" title="TaskEnabled">TaskEnabled</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::EssScheduledTask
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>: <i>Double</i>
    <a href="#launchexpirationtime" title="LaunchExpirationTime">LaunchExpirationTime</a>: <i>Double</i>
    <a href="#launchtime" title="LaunchTime">LaunchTime</a>: <i>String</i>
    <a href="#maxvalue" title="MaxValue">MaxValue</a>: <i>Double</i>
    <a href="#minvalue" title="MinValue">MinValue</a>: <i>Double</i>
    <a href="#recurrenceendtime" title="RecurrenceEndTime">RecurrenceEndTime</a>: <i>String</i>
    <a href="#recurrencetype" title="RecurrenceType">RecurrenceType</a>: <i>String</i>
    <a href="#recurrencevalue" title="RecurrenceValue">RecurrenceValue</a>: <i>String</i>
    <a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>: <i>String</i>
    <a href="#scheduledaction" title="ScheduledAction">ScheduledAction</a>: <i>String</i>
    <a href="#scheduledtaskname" title="ScheduledTaskName">ScheduledTaskName</a>: <i>String</i>
    <a href="#taskenabled" title="TaskEnabled">TaskEnabled</a>: <i>Boolean</i>
</pre>

## Properties

#### Description

Description of the scheduled task, which is 2-200 characters (English or Chinese) long.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCapacity

The expected number of instances in a scaling group when the scaling method of the scheduled task is to specify the number of instances in a scaling group. **NOTE:** You must specify the `DesiredCapacity` parameter when you create the scaling group.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchExpirationTime

The time period during which a failed scheduled task is retried. Unit: seconds. Valid values: 0 to 21600. Default value: 600.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTime

The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mmZ format.
The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation.
If the `recurrence_type` parameter is specified, the task is executed repeatedly at the time specified by LaunchTime.
Otherwise, the task is only executed once at the date and time specified by LaunchTime.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxValue

The maximum number of instances in a scaling group when the scaling method of the scheduled task is to specify the number of instances in a scaling group.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinValue

The minimum number of instances in a scaling group when the scaling method of the scheduled task is to specify the number of instances in a scaling group.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurrenceEndTime

Specifies the end time after which the scheduled task is no longer repeated. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
The time must be in UTC. You cannot enter a time point later than 365 days from the date of scheduled task creation. **NOTE:** You must specify `RecurrenceType`, `RecurrenceValue`, and `RecurrenceEndTime` at the same time.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurrenceType

Specifies the recurrence type of the scheduled task. **NOTE:** You must specify `RecurrenceType`, `RecurrenceValue`, and `RecurrenceEndTime` at the same time. Valid values:
- Daily: The scheduled task is executed once every specified number of days.
- Weekly: The scheduled task is executed on each specified day of a week.
- Monthly: The scheduled task is executed on each specified day of a month.
- Cron: (Available in 1.60.0+) The scheduled task is executed based on the specified cron expression.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurrenceValue

Specifies how often a scheduled task recurs. **NOTE:** You must specify `RecurrenceType`, `RecurrenceValue`, and `RecurrenceEndTime` at the same time. The valid value depends on `recurrence_type`
- Daily: You can enter one value. Valid values: 1 to 31.
- Weekly: You can enter multiple values and separate them with commas (,). For example, the values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday.
- Monthly: You can enter two values in A-B format. Valid values of A and B: 1 to 31. The value of B must be greater than or equal to the value of A.
- Cron: You can enter a cron expression which is written in UTC and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W letters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingGroupId

The ID of the scaling group where the number of instances is modified when the scheduled task is triggered. After the `ScalingGroupId` parameter is specified, the scaling method of the scheduled task is to specify the number of instances in a scaling group. You must specify at least one of the following parameters: `MinValue`, `MaxValue`, and `DesiredCapacity`. **NOTE:** You cannot specify `scheduled_action` and `scaling_group_id` at the same time.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledAction

The operation to be performed when a scheduled task is triggered. Enter the unique identifier of a scaling rule. **NOTE:** You cannot specify `scheduled_action` and `scaling_group_id` at the same time.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledTaskName

Display name of the scheduled task, which must be 2-40 characters (English or Chinese) long.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskEnabled

Specifies whether to start the scheduled task. Default to true.

_Required_: No

_Type_: Boolean

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

