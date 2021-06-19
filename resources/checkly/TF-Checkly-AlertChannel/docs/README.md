# TF::Checkly::AlertChannel

The `checkly_alert_channel` resource allows users to manage checkly Alert Channels.

Checkly's Alert Channels feature allows you to define global alerting channels for the checks in your account:

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Checkly::AlertChannel",
    "Properties" : {
        "<a href="#senddegraded" title="SendDegraded">SendDegraded</a>" : <i>Boolean</i>,
        "<a href="#sendfailure" title="SendFailure">SendFailure</a>" : <i>Boolean</i>,
        "<a href="#sendrecovery" title="SendRecovery">SendRecovery</a>" : <i>Boolean</i>,
        "<a href="#sslexpiry" title="SslExpiry">SslExpiry</a>" : <i>Boolean</i>,
        "<a href="#sslexpirythreshold" title="SslExpiryThreshold">SslExpiryThreshold</a>" : <i>Double</i>,
        "<a href="#email" title="Email">Email</a>" : <i>[ <a href="emaildefinition.md">EmailDefinition</a>, ... ]</i>,
        "<a href="#opsgenie" title="Opsgenie">Opsgenie</a>" : <i>[ <a href="opsgeniedefinition.md">OpsgenieDefinition</a>, ... ]</i>,
        "<a href="#slack" title="Slack">Slack</a>" : <i>[ <a href="slackdefinition.md">SlackDefinition</a>, ... ]</i>,
        "<a href="#sms" title="Sms">Sms</a>" : <i>[ <a href="smsdefinition.md">SmsDefinition</a>, ... ]</i>,
        "<a href="#webhook" title="Webhook">Webhook</a>" : <i>[ <a href="webhookdefinition.md">WebhookDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Checkly::AlertChannel
Properties:
    <a href="#senddegraded" title="SendDegraded">SendDegraded</a>: <i>Boolean</i>
    <a href="#sendfailure" title="SendFailure">SendFailure</a>: <i>Boolean</i>
    <a href="#sendrecovery" title="SendRecovery">SendRecovery</a>: <i>Boolean</i>
    <a href="#sslexpiry" title="SslExpiry">SslExpiry</a>: <i>Boolean</i>
    <a href="#sslexpirythreshold" title="SslExpiryThreshold">SslExpiryThreshold</a>: <i>Double</i>
    <a href="#email" title="Email">Email</a>: <i>
      - <a href="emaildefinition.md">EmailDefinition</a></i>
    <a href="#opsgenie" title="Opsgenie">Opsgenie</a>: <i>
      - <a href="opsgeniedefinition.md">OpsgenieDefinition</a></i>
    <a href="#slack" title="Slack">Slack</a>: <i>
      - <a href="slackdefinition.md">SlackDefinition</a></i>
    <a href="#sms" title="Sms">Sms</a>: <i>
      - <a href="smsdefinition.md">SmsDefinition</a></i>
    <a href="#webhook" title="Webhook">Webhook</a>: <i>
      - <a href="webhookdefinition.md">WebhookDefinition</a></i>
</pre>

## Properties

#### SendDegraded

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendFailure

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendRecovery

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslExpiry

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslExpiryThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: No

_Type_: List of <a href="emaildefinition.md">EmailDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Opsgenie

_Required_: No

_Type_: List of <a href="opsgeniedefinition.md">OpsgenieDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slack

_Required_: No

_Type_: List of <a href="slackdefinition.md">SlackDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sms

_Required_: No

_Type_: List of <a href="smsdefinition.md">SmsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webhook

_Required_: No

_Type_: List of <a href="webhookdefinition.md">WebhookDefinition</a>

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

