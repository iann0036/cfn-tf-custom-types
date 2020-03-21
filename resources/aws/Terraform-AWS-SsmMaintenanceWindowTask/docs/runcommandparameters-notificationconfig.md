# Terraform::AWS::SsmMaintenanceWindowTask RunCommandParameters NotificationConfig

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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationEvents

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

