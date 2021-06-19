# TF::ILert::User

An [user](https://api.ilert.com/api-docs/#tag/Users) is a member of a iLert account that have the ability to interact with incidents and other data on the account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ILert::User",
    "Properties" : {
        "<a href="#department" title="Department">Department</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#firstname" title="FirstName">FirstName</a>" : <i>String</i>,
        "<a href="#language" title="Language">Language</a>" : <i>String</i>,
        "<a href="#lastname" title="LastName">LastName</a>" : <i>String</i>,
        "<a href="#position" title="Position">Position</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#subscribedincidentupdatenotificationtypes" title="SubscribedIncidentUpdateNotificationTypes">SubscribedIncidentUpdateNotificationTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#subscribedincidentupdatestates" title="SubscribedIncidentUpdateStates">SubscribedIncidentUpdateStates</a>" : <i>[ String, ... ]</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#highprioritynotificationpreference" title="HighPriorityNotificationPreference">HighPriorityNotificationPreference</a>" : <i>[ <a href="highprioritynotificationpreferencedefinition.md">HighPriorityNotificationPreferenceDefinition</a>, ... ]</i>,
        "<a href="#landline" title="Landline">Landline</a>" : <i>[ <a href="landlinedefinition.md">LandlineDefinition</a>, ... ]</i>,
        "<a href="#lowprioritynotificationpreference" title="LowPriorityNotificationPreference">LowPriorityNotificationPreference</a>" : <i>[ <a href="lowprioritynotificationpreferencedefinition.md">LowPriorityNotificationPreferenceDefinition</a>, ... ]</i>,
        "<a href="#mobile" title="Mobile">Mobile</a>" : <i>[ <a href="mobiledefinition.md">MobileDefinition</a>, ... ]</i>,
        "<a href="#oncallnotificationpreference" title="OnCallNotificationPreference">OnCallNotificationPreference</a>" : <i>[ <a href="oncallnotificationpreferencedefinition.md">OnCallNotificationPreferenceDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ILert::User
Properties:
    <a href="#department" title="Department">Department</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#firstname" title="FirstName">FirstName</a>: <i>String</i>
    <a href="#language" title="Language">Language</a>: <i>String</i>
    <a href="#lastname" title="LastName">LastName</a>: <i>String</i>
    <a href="#position" title="Position">Position</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#subscribedincidentupdatenotificationtypes" title="SubscribedIncidentUpdateNotificationTypes">SubscribedIncidentUpdateNotificationTypes</a>: <i>
      - String</i>
    <a href="#subscribedincidentupdatestates" title="SubscribedIncidentUpdateStates">SubscribedIncidentUpdateStates</a>: <i>
      - String</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#highprioritynotificationpreference" title="HighPriorityNotificationPreference">HighPriorityNotificationPreference</a>: <i>
      - <a href="highprioritynotificationpreferencedefinition.md">HighPriorityNotificationPreferenceDefinition</a></i>
    <a href="#landline" title="Landline">Landline</a>: <i>
      - <a href="landlinedefinition.md">LandlineDefinition</a></i>
    <a href="#lowprioritynotificationpreference" title="LowPriorityNotificationPreference">LowPriorityNotificationPreference</a>: <i>
      - <a href="lowprioritynotificationpreferencedefinition.md">LowPriorityNotificationPreferenceDefinition</a></i>
    <a href="#mobile" title="Mobile">Mobile</a>: <i>
      - <a href="mobiledefinition.md">MobileDefinition</a></i>
    <a href="#oncallnotificationpreference" title="OnCallNotificationPreference">OnCallNotificationPreference</a>: <i>
      - <a href="oncallnotificationpreferencedefinition.md">OnCallNotificationPreferenceDefinition</a></i>
</pre>

## Properties

#### Department

The user's department.
- `language` - (Optional) The user's language. Allowed values are `en`, `de`.
- `role` - (Optional) The user's role. Allowed values are `ADMIN`, `USER`, `RESPONDER` or `STAKEHOLDER`. Default: `USER`
- `high_priority_notification_preference` - (Optional) One or more [high priority notification preference](#high-priority-notification-preference-arguments) blocks.
- `low_priority_notification_preference` - (Optional) One or more [low priority notification preference](#low-priority-notification-preference-arguments) blocks.
- `on_call_notification_preference` - (Optional) One or more [on-call notification preference](#on-call-notification-preference-arguments) blocks.
- `subscribed_incident_update_states` - (Optional) A list of subscribed incident update states. Allowed values are `ACCEPTED`, `ESCALATED` or `RESOLVED`.
- `subscribed_incident_update_notification_types` - (Optional) A list of subscribed incident update notification types. Allowed values are `EMAIL`, `ANDROID`, `IPHONE`, `SMS`, `VOICE_MOBILE` or `VOICE_LANDLINE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

The user's email address.
- `mobile` - (Optional) The [mobile](#mobile-arguments) block.
- `landline` - (Optional) The [landline](#landline-arguments) block.
- `timezone` - (Optional) The user's timezone. Allowed values are `Europe/Berlin`, `America/New_York`, `America/Los_Angeles`, `Asia/Istanbul`.
- `position` - (Optional) The user's position.
- `department` - (Optional) The user's department.
- `language` - (Optional) The user's language. Allowed values are `en`, `de`.
- `role` - (Optional) The user's role. Allowed values are `ADMIN`, `USER`, `RESPONDER` or `STAKEHOLDER`. Default: `USER`
- `high_priority_notification_preference` - (Optional) One or more [high priority notification preference](#high-priority-notification-preference-arguments) blocks.
- `low_priority_notification_preference` - (Optional) One or more [low priority notification preference](#low-priority-notification-preference-arguments) blocks.
- `on_call_notification_preference` - (Optional) One or more [on-call notification preference](#on-call-notification-preference-arguments) blocks.
- `subscribed_incident_update_states` - (Optional) A list of subscribed incident update states. Allowed values are `ACCEPTED`, `ESCALATED` or `RESOLVED`.
- `subscribed_incident_update_notification_types` - (Optional) A list of subscribed incident update notification types. Allowed values are `EMAIL`, `ANDROID`, `IPHONE`, `SMS`, `VOICE_MOBILE` or `VOICE_LANDLINE`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirstName

The first name of the user.
- `last_name` - (Required) The last name of the user.
- `email` - (Required) The user's email address.
- `mobile` - (Optional) The [mobile](#mobile-arguments) block.
- `landline` - (Optional) The [landline](#landline-arguments) block.
- `timezone` - (Optional) The user's timezone. Allowed values are `Europe/Berlin`, `America/New_York`, `America/Los_Angeles`, `Asia/Istanbul`.
- `position` - (Optional) The user's position.
- `department` - (Optional) The user's department.
- `language` - (Optional) The user's language. Allowed values are `en`, `de`.
- `role` - (Optional) The user's role. Allowed values are `ADMIN`, `USER`, `RESPONDER` or `STAKEHOLDER`. Default: `USER`
- `high_priority_notification_preference` - (Optional) One or more [high priority notification preference](#high-priority-notification-preference-arguments) blocks.
- `low_priority_notification_preference` - (Optional) One or more [low priority notification preference](#low-priority-notification-preference-arguments) blocks.
- `on_call_notification_preference` - (Optional) One or more [on-call notification preference](#on-call-notification-preference-arguments) blocks.
- `subscribed_incident_update_states` - (Optional) A list of subscribed incident update states. Allowed values are `ACCEPTED`, `ESCALATED` or `RESOLVED`.
- `subscribed_incident_update_notification_types` - (Optional) A list of subscribed incident update notification types. Allowed values are `EMAIL`, `ANDROID`, `IPHONE`, `SMS`, `VOICE_MOBILE` or `VOICE_LANDLINE`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Language

The user's language. Allowed values are `en`, `de`.
- `role` - (Optional) The user's role. Allowed values are `ADMIN`, `USER`, `RESPONDER` or `STAKEHOLDER`. Default: `USER`
- `high_priority_notification_preference` - (Optional) One or more [high priority notification preference](#high-priority-notification-preference-arguments) blocks.
- `low_priority_notification_preference` - (Optional) One or more [low priority notification preference](#low-priority-notification-preference-arguments) blocks.
- `on_call_notification_preference` - (Optional) One or more [on-call notification preference](#on-call-notification-preference-arguments) blocks.
- `subscribed_incident_update_states` - (Optional) A list of subscribed incident update states. Allowed values are `ACCEPTED`, `ESCALATED` or `RESOLVED`.
- `subscribed_incident_update_notification_types` - (Optional) A list of subscribed incident update notification types. Allowed values are `EMAIL`, `ANDROID`, `IPHONE`, `SMS`, `VOICE_MOBILE` or `VOICE_LANDLINE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastName

The last name of the user.
- `email` - (Required) The user's email address.
- `mobile` - (Optional) The [mobile](#mobile-arguments) block.
- `landline` - (Optional) The [landline](#landline-arguments) block.
- `timezone` - (Optional) The user's timezone. Allowed values are `Europe/Berlin`, `America/New_York`, `America/Los_Angeles`, `Asia/Istanbul`.
- `position` - (Optional) The user's position.
- `department` - (Optional) The user's department.
- `language` - (Optional) The user's language. Allowed values are `en`, `de`.
- `role` - (Optional) The user's role. Allowed values are `ADMIN`, `USER`, `RESPONDER` or `STAKEHOLDER`. Default: `USER`
- `high_priority_notification_preference` - (Optional) One or more [high priority notification preference](#high-priority-notification-preference-arguments) blocks.
- `low_priority_notification_preference` - (Optional) One or more [low priority notification preference](#low-priority-notification-preference-arguments) blocks.
- `on_call_notification_preference` - (Optional) One or more [on-call notification preference](#on-call-notification-preference-arguments) blocks.
- `subscribed_incident_update_states` - (Optional) A list of subscribed incident update states. Allowed values are `ACCEPTED`, `ESCALATED` or `RESOLVED`.
- `subscribed_incident_update_notification_types` - (Optional) A list of subscribed incident update notification types. Allowed values are `EMAIL`, `ANDROID`, `IPHONE`, `SMS`, `VOICE_MOBILE` or `VOICE_LANDLINE`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Position

The user's position.
- `department` - (Optional) The user's department.
- `language` - (Optional) The user's language. Allowed values are `en`, `de`.
- `role` - (Optional) The user's role. Allowed values are `ADMIN`, `USER`, `RESPONDER` or `STAKEHOLDER`. Default: `USER`
- `high_priority_notification_preference` - (Optional) One or more [high priority notification preference](#high-priority-notification-preference-arguments) blocks.
- `low_priority_notification_preference` - (Optional) One or more [low priority notification preference](#low-priority-notification-preference-arguments) blocks.
- `on_call_notification_preference` - (Optional) One or more [on-call notification preference](#on-call-notification-preference-arguments) blocks.
- `subscribed_incident_update_states` - (Optional) A list of subscribed incident update states. Allowed values are `ACCEPTED`, `ESCALATED` or `RESOLVED`.
- `subscribed_incident_update_notification_types` - (Optional) A list of subscribed incident update notification types. Allowed values are `EMAIL`, `ANDROID`, `IPHONE`, `SMS`, `VOICE_MOBILE` or `VOICE_LANDLINE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

The user's role. Allowed values are `ADMIN`, `USER`, `RESPONDER` or `STAKEHOLDER`. Default: `USER`
- `high_priority_notification_preference` - (Optional) One or more [high priority notification preference](#high-priority-notification-preference-arguments) blocks.
- `low_priority_notification_preference` - (Optional) One or more [low priority notification preference](#low-priority-notification-preference-arguments) blocks.
- `on_call_notification_preference` - (Optional) One or more [on-call notification preference](#on-call-notification-preference-arguments) blocks.
- `subscribed_incident_update_states` - (Optional) A list of subscribed incident update states. Allowed values are `ACCEPTED`, `ESCALATED` or `RESOLVED`.
- `subscribed_incident_update_notification_types` - (Optional) A list of subscribed incident update notification types. Allowed values are `EMAIL`, `ANDROID`, `IPHONE`, `SMS`, `VOICE_MOBILE` or `VOICE_LANDLINE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscribedIncidentUpdateNotificationTypes

A list of subscribed incident update notification types. Allowed values are `EMAIL`, `ANDROID`, `IPHONE`, `SMS`, `VOICE_MOBILE` or `VOICE_LANDLINE`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscribedIncidentUpdateStates

A list of subscribed incident update states. Allowed values are `ACCEPTED`, `ESCALATED` or `RESOLVED`.
- `subscribed_incident_update_notification_types` - (Optional) A list of subscribed incident update notification types. Allowed values are `EMAIL`, `ANDROID`, `IPHONE`, `SMS`, `VOICE_MOBILE` or `VOICE_LANDLINE`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

The user's timezone. Allowed values are `Europe/Berlin`, `America/New_York`, `America/Los_Angeles`, `Asia/Istanbul`.
- `position` - (Optional) The user's position.
- `department` - (Optional) The user's department.
- `language` - (Optional) The user's language. Allowed values are `en`, `de`.
- `role` - (Optional) The user's role. Allowed values are `ADMIN`, `USER`, `RESPONDER` or `STAKEHOLDER`. Default: `USER`
- `high_priority_notification_preference` - (Optional) One or more [high priority notification preference](#high-priority-notification-preference-arguments) blocks.
- `low_priority_notification_preference` - (Optional) One or more [low priority notification preference](#low-priority-notification-preference-arguments) blocks.
- `on_call_notification_preference` - (Optional) One or more [on-call notification preference](#on-call-notification-preference-arguments) blocks.
- `subscribed_incident_update_states` - (Optional) A list of subscribed incident update states. Allowed values are `ACCEPTED`, `ESCALATED` or `RESOLVED`.
- `subscribed_incident_update_notification_types` - (Optional) A list of subscribed incident update notification types. Allowed values are `EMAIL`, `ANDROID`, `IPHONE`, `SMS`, `VOICE_MOBILE` or `VOICE_LANDLINE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The username of the user.
- `first_name` - (Required) The first name of the user.
- `last_name` - (Required) The last name of the user.
- `email` - (Required) The user's email address.
- `mobile` - (Optional) The [mobile](#mobile-arguments) block.
- `landline` - (Optional) The [landline](#landline-arguments) block.
- `timezone` - (Optional) The user's timezone. Allowed values are `Europe/Berlin`, `America/New_York`, `America/Los_Angeles`, `Asia/Istanbul`.
- `position` - (Optional) The user's position.
- `department` - (Optional) The user's department.
- `language` - (Optional) The user's language. Allowed values are `en`, `de`.
- `role` - (Optional) The user's role. Allowed values are `ADMIN`, `USER`, `RESPONDER` or `STAKEHOLDER`. Default: `USER`
- `high_priority_notification_preference` - (Optional) One or more [high priority notification preference](#high-priority-notification-preference-arguments) blocks.
- `low_priority_notification_preference` - (Optional) One or more [low priority notification preference](#low-priority-notification-preference-arguments) blocks.
- `on_call_notification_preference` - (Optional) One or more [on-call notification preference](#on-call-notification-preference-arguments) blocks.
- `subscribed_incident_update_states` - (Optional) A list of subscribed incident update states. Allowed values are `ACCEPTED`, `ESCALATED` or `RESOLVED`.
- `subscribed_incident_update_notification_types` - (Optional) A list of subscribed incident update notification types. Allowed values are `EMAIL`, `ANDROID`, `IPHONE`, `SMS`, `VOICE_MOBILE` or `VOICE_LANDLINE`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HighPriorityNotificationPreference

_Required_: No

_Type_: List of <a href="highprioritynotificationpreferencedefinition.md">HighPriorityNotificationPreferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Landline

_Required_: No

_Type_: List of <a href="landlinedefinition.md">LandlineDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LowPriorityNotificationPreference

_Required_: No

_Type_: List of <a href="lowprioritynotificationpreferencedefinition.md">LowPriorityNotificationPreferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mobile

_Required_: No

_Type_: List of <a href="mobiledefinition.md">MobileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnCallNotificationPreference

_Required_: No

_Type_: List of <a href="oncallnotificationpreferencedefinition.md">OnCallNotificationPreferenceDefinition</a>

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

