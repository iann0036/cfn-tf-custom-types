# TF::AzureRM::MonitorActivityLogAlert ActionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#actiongroupid" title="ActionGroupId">ActionGroupId</a>" : <i>String</i>,
    "<a href="#webhookproperties" title="WebhookProperties">WebhookProperties</a>" : <i>[ <a href="webhookpropertiesdefinition.md">WebhookPropertiesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#actiongroupid" title="ActionGroupId">ActionGroupId</a>: <i>String</i>
<a href="#webhookproperties" title="WebhookProperties">WebhookProperties</a>: <i>
      - <a href="webhookpropertiesdefinition.md">WebhookPropertiesDefinition</a></i>
</pre>

## Properties

#### ActionGroupId

The ID of the Action Group can be sourced from [the `azurerm_monitor_action_group` resource](./monitor_action_group.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebhookProperties

The map of custom string properties to include with the post operation. These data are appended to the webhook payload.

_Required_: No

_Type_: List of <a href="webhookpropertiesdefinition.md">WebhookPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

