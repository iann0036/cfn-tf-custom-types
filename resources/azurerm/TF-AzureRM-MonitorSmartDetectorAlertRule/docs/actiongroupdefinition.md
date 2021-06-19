# TF::AzureRM::MonitorSmartDetectorAlertRule ActionGroupDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#emailsubject" title="EmailSubject">EmailSubject</a>" : <i>String</i>,
    "<a href="#ids" title="Ids">Ids</a>" : <i>[ String, ... ]</i>,
    "<a href="#webhookpayload" title="WebhookPayload">WebhookPayload</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#emailsubject" title="EmailSubject">EmailSubject</a>: <i>String</i>
<a href="#ids" title="Ids">Ids</a>: <i>
      - String</i>
<a href="#webhookpayload" title="WebhookPayload">WebhookPayload</a>: <i>String</i>
</pre>

## Properties

#### EmailSubject

Specifies a custom email subject if Email Receiver is specified in Monitor Action Group resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ids

Specifies the action group ids.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebhookPayload

A JSON String which Specifies the custom webhook payload if Webhook Receiver is specified in Monitor Action Group resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

