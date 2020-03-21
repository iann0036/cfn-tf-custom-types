# Terraform::PagerDuty::UserNotificationRule

A [notification rule](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Users/get_users_id_notification_rules_notification_rule_id) configures where and when a PagerDuty user is notified when a triggered incident is assigned to him. Unique notification rules can be created for both high and low-urgency incidents.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::PagerDuty::UserNotificationRule",
    "Properties" : {
        "<a href="#contactmethod" title="ContactMethod">ContactMethod</a>" : <i>[ <a href="contactmethod.md">ContactMethod</a>, ... ]</i>,
        "<a href="#startdelayinminutes" title="StartDelayInMinutes">StartDelayInMinutes</a>" : <i>Double</i>,
        "<a href="#urgency" title="Urgency">Urgency</a>" : <i>String</i>,
        "<a href="#userid" title="UserId">UserId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::PagerDuty::UserNotificationRule
Properties:
    <a href="#contactmethod" title="ContactMethod">ContactMethod</a>: <i>
      - <a href="contactmethod.md">ContactMethod</a></i>
    <a href="#startdelayinminutes" title="StartDelayInMinutes">StartDelayInMinutes</a>: <i>Double</i>
    <a href="#urgency" title="Urgency">Urgency</a>: <i>String</i>
    <a href="#userid" title="UserId">UserId</a>: <i>String</i>
</pre>

## Properties

#### ContactMethod

A contact method block, configured as a block described below.

_Required_: Yes

_Type_: List of <a href="contactmethod.md">ContactMethod</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartDelayInMinutes

The delay before firing the rule, in minutes.
* `urgency` - (Required) Which incident urgency this rule is used for. Account must have the `urgencies` ability to have a low urgency notification rule. Can be `high` or `low`.
* `contact_method` - (Required) A contact method block, configured as a block described below.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Urgency

Which incident urgency this rule is used for. Account must have the `urgencies` ability to have a low urgency notification rule. Can be `high` or `low`.
* `contact_method` - (Required) A contact method block, configured as a block described below.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserId

The ID of the user.
* `start_delay_in_minutes` - (Required) The delay before firing the rule, in minutes.
* `urgency` - (Required) Which incident urgency this rule is used for. Account must have the `urgencies` ability to have a low urgency notification rule. Can be `high` or `low`.
* `contact_method` - (Required) A contact method block, configured as a block described below.

_Required_: Yes

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

