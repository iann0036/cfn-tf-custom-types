# Terraform::OpsGenie::Escalation Rules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#condition" title="Condition">Condition</a>" : <i>String</i>,
    "<a href="#delay" title="Delay">Delay</a>" : <i>Double</i>,
    "<a href="#notifytype" title="NotifyType">NotifyType</a>" : <i>String</i>,
    "<a href="#recipient" title="Recipient">Recipient</a>" : <i>[ <a href="rules-recipient.md">Recipient</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#condition" title="Condition">Condition</a>: <i>String</i>
<a href="#delay" title="Delay">Delay</a>: <i>Double</i>
<a href="#notifytype" title="NotifyType">NotifyType</a>: <i>String</i>
<a href="#recipient" title="Recipient">Recipient</a>: <i>
      - <a href="rules-recipient.md">Recipient</a></i>
</pre>

## Properties

#### Condition

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Delay

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipient

_Required_: No
_Type_: List of <a href="rules-recipient.md">Recipient</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

