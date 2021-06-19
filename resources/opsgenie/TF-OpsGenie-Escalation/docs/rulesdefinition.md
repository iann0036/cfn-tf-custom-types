# TF::OpsGenie::Escalation RulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#condition" title="Condition">Condition</a>" : <i>String</i>,
    "<a href="#delay" title="Delay">Delay</a>" : <i>Double</i>,
    "<a href="#notifytype" title="NotifyType">NotifyType</a>" : <i>String</i>,
    "<a href="#recipient" title="Recipient">Recipient</a>" : <i>[ <a href="recipientdefinition.md">RecipientDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#condition" title="Condition">Condition</a>: <i>String</i>
<a href="#delay" title="Delay">Delay</a>: <i>Double</i>
<a href="#notifytype" title="NotifyType">NotifyType</a>: <i>String</i>
<a href="#recipient" title="Recipient">Recipient</a>: <i>
      - <a href="recipientdefinition.md">RecipientDefinition</a></i>
</pre>

## Properties

#### Condition

The condition for notifying the recipient of escalation rule that is based on the alert state. Possible values are: `if-not-acked` and `if-not-closed`. Default: `if-not-acked`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Delay

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyType

Recipient calculation logic for schedules. Possible values are:.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipient

_Required_: No

_Type_: List of <a href="recipientdefinition.md">RecipientDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

