# Terraform::AzureRM::MonitorMetricAlert Action

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#actiongroupid" title="ActionGroupId">ActionGroupId</a>" : <i>String</i>,
    "<a href="#webhookproperties" title="WebhookProperties">WebhookProperties</a>" : <i>[ &lt;a href=&#34;action-webhookproperties.md&#34;&gt;WebhookProperties&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#actiongroupid" title="ActionGroupId">ActionGroupId</a>: <i>String</i>
<a href="#webhookproperties" title="WebhookProperties">WebhookProperties</a>: <i>
      - &lt;a href=&#34;action-webhookproperties.md&#34;&gt;WebhookProperties&lt;/a&gt;</i>
</pre>

## Properties

#### ActionGroupId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebhookProperties

_Required_: No
_Type_: List of &lt;a href=&#34;action-webhookproperties.md&#34;&gt;WebhookProperties&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

