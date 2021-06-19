# TF::AzureRM::MonitorAutoscaleSetting NotificationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#email" title="Email">Email</a>" : <i>[ <a href="emaildefinition.md">EmailDefinition</a>, ... ]</i>,
    "<a href="#webhook" title="Webhook">Webhook</a>" : <i>[ <a href="webhookdefinition.md">WebhookDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#email" title="Email">Email</a>: <i>
      - <a href="emaildefinition.md">EmailDefinition</a></i>
<a href="#webhook" title="Webhook">Webhook</a>: <i>
      - <a href="webhookdefinition.md">WebhookDefinition</a></i>
</pre>

## Properties

#### Email

_Required_: No

_Type_: List of <a href="emaildefinition.md">EmailDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webhook

_Required_: No

_Type_: List of <a href="webhookdefinition.md">WebhookDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

