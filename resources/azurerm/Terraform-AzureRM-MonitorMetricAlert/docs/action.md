# Terraform::AzureRM::MonitorMetricAlert Action

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#actiongroupid" title="ActionGroupId">ActionGroupId</a>" : <i>String</i>,
    "<a href="#webhookproperties" title="WebhookProperties">WebhookProperties</a>" : <i>[ <a href="action-webhookproperties.md">WebhookProperties</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#actiongroupid" title="ActionGroupId">ActionGroupId</a>: <i>String</i>
<a href="#webhookproperties" title="WebhookProperties">WebhookProperties</a>: <i>
      - <a href="action-webhookproperties.md">WebhookProperties</a></i>
</pre>

## Properties

#### ActionGroupId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebhookProperties

_Required_: No
_Type_: List of <a href="action-webhookproperties.md">WebhookProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

