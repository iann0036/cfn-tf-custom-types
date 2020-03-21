# Terraform::Alicloud::EssScheduledTask

Provides a ESS schedule resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::EssScheduledTask",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#launchexpirationtime" title="LaunchExpirationTime">LaunchExpirationTime</a>" : <i>Double</i>,
        "<a href="#launchtime" title="LaunchTime">LaunchTime</a>" : <i>String</i>,
        "<a href="#recurrenceendtime" title="RecurrenceEndTime">RecurrenceEndTime</a>" : <i>String</i>,
        "<a href="#recurrencetype" title="RecurrenceType">RecurrenceType</a>" : <i>String</i>,
        "<a href="#recurrencevalue" title="RecurrenceValue">RecurrenceValue</a>" : <i>String</i>,
        "<a href="#scheduledaction" title="ScheduledAction">ScheduledAction</a>" : <i>String</i>,
        "<a href="#scheduledtaskname" title="ScheduledTaskName">ScheduledTaskName</a>" : <i>String</i>,
        "<a href="#taskenabled" title="TaskEnabled">TaskEnabled</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::EssScheduledTask
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#launchexpirationtime" title="LaunchExpirationTime">LaunchExpirationTime</a>: <i>Double</i>
    <a href="#launchtime" title="LaunchTime">LaunchTime</a>: <i>String</i>
    <a href="#recurrenceendtime" title="RecurrenceEndTime">RecurrenceEndTime</a>: <i>String</i>
    <a href="#recurrencetype" title="RecurrenceType">RecurrenceType</a>: <i>String</i>
    <a href="#recurrencevalue" title="RecurrenceValue">RecurrenceValue</a>: <i>String</i>
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

#### LaunchExpirationTime

The time period during which a failed scheduled task is retried. Unit: seconds. Valid values: 0 to 21600. Default value: 600.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTime

The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation.
If the `recurrence_type` parameter is specified, the task is executed repeatedly at the time specified by LaunchTime.
Otherwise, the task is only executed once at the date and time specified by LaunchTime.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurrenceEndTime

Specifies the end time after which the scheduled task is no longer repeated.
Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
The time must be in UTC. You cannot enter a time point later than 365 days from the date of scheduled task creation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurrenceType

Specifies the recurrence type of the scheduled task.
If set, both `recurrence_value` and `recurrence_end_time` must be set. Valid values:
- Daily: The scheduled task is executed once every specified number of days.
- Weekly: The scheduled task is executed on each specified day of a week.
- Monthly: The scheduled task is executed on each specified day of a month.
- Cron: (Available in 1.60.0+) The scheduled task is executed based on the specified cron expression.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurrenceValue

Specifies how often a scheduled task recurs. The valid value depends on `recurrence_type`
- Daily: You can enter one value. Valid values: 1 to 31.
- Weekly: You can enter multiple values and separate them with commas (,). For example, the values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday.
- Monthly: You can enter two values in A-B format. Valid values of A and B: 1 to 31. The value of B must be greater than or equal to the value of A.
- Cron: You can enter a cron expression which is written in UTC and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W letters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledAction

The operation to be performed when a scheduled task is triggered. Enter the unique identifier of a scaling rule.

_Required_: Yes

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

