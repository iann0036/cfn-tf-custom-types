# TF::OpsGenie::NotificationRule

Manages a Notification Rule within Opsgenie.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpsGenie::NotificationRule",
    "Properties" : {
        "<a href="#actiontype" title="ActionType">ActionType</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notificationtime" title="NotificationTime">NotificationTime</a>" : <i>[ String, ... ]</i>,
        "<a href="#order" title="Order">Order</a>" : <i>Double</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#criteria" title="Criteria">Criteria</a>" : <i>[ <a href="criteriadefinition.md">CriteriaDefinition</a>, ... ]</i>,
        "<a href="#repeat" title="Repeat">Repeat</a>" : <i>[ <a href="repeatdefinition.md">RepeatDefinition</a>, ... ]</i>,
        "<a href="#schedules" title="Schedules">Schedules</a>" : <i>[ <a href="schedulesdefinition.md">SchedulesDefinition</a>, ... ]</i>,
        "<a href="#steps" title="Steps">Steps</a>" : <i>[ <a href="stepsdefinition.md">StepsDefinition</a>, ... ]</i>,
        "<a href="#timerestriction" title="TimeRestriction">TimeRestriction</a>" : <i>[ <a href="timerestrictiondefinition.md">TimeRestrictionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpsGenie::NotificationRule
Properties:
    <a href="#actiontype" title="ActionType">ActionType</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notificationtime" title="NotificationTime">NotificationTime</a>: <i>
      - String</i>
    <a href="#order" title="Order">Order</a>: <i>Double</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#criteria" title="Criteria">Criteria</a>: <i>
      - <a href="criteriadefinition.md">CriteriaDefinition</a></i>
    <a href="#repeat" title="Repeat">Repeat</a>: <i>
      - <a href="repeatdefinition.md">RepeatDefinition</a></i>
    <a href="#schedules" title="Schedules">Schedules</a>: <i>
      - <a href="schedulesdefinition.md">SchedulesDefinition</a></i>
    <a href="#steps" title="Steps">Steps</a>: <i>
      - <a href="stepsdefinition.md">StepsDefinition</a></i>
    <a href="#timerestriction" title="TimeRestriction">TimeRestriction</a>: <i>
      - <a href="timerestrictiondefinition.md">TimeRestrictionDefinition</a></i>
</pre>

## Properties

#### ActionType

Type of the action that notification rule will have. Allowed values: `create-alert`, `acknowledged-alert`, `closed-alert`, `assigned-alert`, `add-note`, `schedule-start`, `schedule-end`, `incoming-call-routing`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

If policy should be enabled. Default: `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the notification policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationTime

List of Time Periods that notification for schedule start/end will be sent. Allowed values: `just-before`, `15-minutes-ago`, `1-hour-ago`, `1-day-ago`. If `action_type` is `schedule-start` or `schedule-end` then it is required.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Order

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

Username of user to which this notification rule belongs to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Criteria

_Required_: No

_Type_: List of <a href="criteriadefinition.md">CriteriaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repeat

_Required_: No

_Type_: List of <a href="repeatdefinition.md">RepeatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedules

_Required_: No

_Type_: List of <a href="schedulesdefinition.md">SchedulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Steps

_Required_: No

_Type_: List of <a href="stepsdefinition.md">StepsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeRestriction

_Required_: No

_Type_: List of <a href="timerestrictiondefinition.md">TimeRestrictionDefinition</a>

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

