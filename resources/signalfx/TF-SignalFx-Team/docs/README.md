# TF::SignalFx::Team

Handles management of SignalFx teams.

You can configure [team notification policies](https://docs.signalfx.com/en/latest/managing/teams/team-notifications.html) using this resource and the various `notifications_*` properties.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SignalFx::Team",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#members" title="Members">Members</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notificationscritical" title="NotificationsCritical">NotificationsCritical</a>" : <i>[ String, ... ]</i>,
        "<a href="#notificationsdefault" title="NotificationsDefault">NotificationsDefault</a>" : <i>[ String, ... ]</i>,
        "<a href="#notificationsinfo" title="NotificationsInfo">NotificationsInfo</a>" : <i>[ String, ... ]</i>,
        "<a href="#notificationsmajor" title="NotificationsMajor">NotificationsMajor</a>" : <i>[ String, ... ]</i>,
        "<a href="#notificationsminor" title="NotificationsMinor">NotificationsMinor</a>" : <i>[ String, ... ]</i>,
        "<a href="#notificationswarning" title="NotificationsWarning">NotificationsWarning</a>" : <i>[ String, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::SignalFx::Team
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#members" title="Members">Members</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notificationscritical" title="NotificationsCritical">NotificationsCritical</a>: <i>
      - String</i>
    <a href="#notificationsdefault" title="NotificationsDefault">NotificationsDefault</a>: <i>
      - String</i>
    <a href="#notificationsinfo" title="NotificationsInfo">NotificationsInfo</a>: <i>
      - String</i>
    <a href="#notificationsmajor" title="NotificationsMajor">NotificationsMajor</a>: <i>
      - String</i>
    <a href="#notificationsminor" title="NotificationsMinor">NotificationsMinor</a>: <i>
      - String</i>
    <a href="#notificationswarning" title="NotificationsWarning">NotificationsWarning</a>: <i>
      - String</i>
</pre>

## Properties

#### Description

Description of the team.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Members

List of user IDs to include in the team.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the team.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationsCritical

Where to send notifications for critical alerts.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationsDefault

Where to send notifications for default alerts.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationsInfo

Where to send notifications for info alerts.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationsMajor

Where to send notifications for major alerts.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationsMinor

Where to send notifications for minor alerts.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationsWarning

Where to send notifications for warning alerts.

_Required_: No

_Type_: List of String

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

#### Url

Returns the <code>Url</code> value.

