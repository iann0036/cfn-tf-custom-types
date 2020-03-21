# Terraform::PagerDuty::UserNotificationRule

CloudFormation equivalent of pagerduty_user_notification_rule

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

_Required_: Yes

_Type_: List of <a href="contactmethod.md">ContactMethod</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartDelayInMinutes

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Urgency

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserId

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

