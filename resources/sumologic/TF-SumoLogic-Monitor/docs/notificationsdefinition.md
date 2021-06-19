# TF::SumoLogic::Monitor NotificationsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#runfortriggertypes" title="RunForTriggerTypes">RunForTriggerTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#notification" title="Notification">Notification</a>" : <i>[ <a href="notificationdefinition.md">NotificationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#runfortriggertypes" title="RunForTriggerTypes">RunForTriggerTypes</a>: <i>
      - String</i>
<a href="#notification" title="Notification">Notification</a>: <i>
      - <a href="notificationdefinition.md">NotificationDefinition</a></i>
</pre>

## Properties

#### RunForTriggerTypes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notification

_Required_: No

_Type_: List of <a href="notificationdefinition.md">NotificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

