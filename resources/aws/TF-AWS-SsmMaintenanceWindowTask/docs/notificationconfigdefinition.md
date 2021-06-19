# TF::AWS::SsmMaintenanceWindowTask NotificationConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#notificationarn" title="NotificationArn">NotificationArn</a>" : <i>String</i>,
    "<a href="#notificationevents" title="NotificationEvents">NotificationEvents</a>" : <i>[ String, ... ]</i>,
    "<a href="#notificationtype" title="NotificationType">NotificationType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#notificationarn" title="NotificationArn">NotificationArn</a>: <i>String</i>
<a href="#notificationevents" title="NotificationEvents">NotificationEvents</a>: <i>
      - String</i>
<a href="#notificationtype" title="NotificationType">NotificationType</a>: <i>String</i>
</pre>

## Properties

#### NotificationArn

An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationEvents

The different events for which you can receive notifications. Valid values: `All`, `InProgress`, `Success`, `TimedOut`, `Cancelled`, and `Failed`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationType

When specified with `Command`, receive notification when the status of a command changes. When specified with `Invocation`, for commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. Valid values: `Command` and `Invocation`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

