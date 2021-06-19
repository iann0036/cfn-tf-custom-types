# TF::AzureRM::MonitorScheduledQueryRulesAlert ActionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#actiongroup" title="ActionGroup">ActionGroup</a>" : <i>[ String, ... ]</i>,
    "<a href="#customwebhookpayload" title="CustomWebhookPayload">CustomWebhookPayload</a>" : <i>String</i>,
    "<a href="#emailsubject" title="EmailSubject">EmailSubject</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#actiongroup" title="ActionGroup">ActionGroup</a>: <i>
      - String</i>
<a href="#customwebhookpayload" title="CustomWebhookPayload">CustomWebhookPayload</a>: <i>String</i>
<a href="#emailsubject" title="EmailSubject">EmailSubject</a>: <i>String</i>
</pre>

## Properties

#### ActionGroup

List of action group reference resource IDs.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomWebhookPayload

Custom payload to be sent for all webhook payloads in alerting action.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailSubject

Custom subject override for all email ids in Azure action group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

