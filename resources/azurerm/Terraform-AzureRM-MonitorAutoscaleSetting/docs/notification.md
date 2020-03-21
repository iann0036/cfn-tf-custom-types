# Terraform::AzureRM::MonitorAutoscaleSetting Notification

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#email" title="Email">Email</a>" : <i>[ &lt;a href=&#34;notification-email.md&#34;&gt;Email&lt;/a&gt;, ... ]</i>,
    "<a href="#webhook" title="Webhook">Webhook</a>" : <i>[ &lt;a href=&#34;notification-webhook.md&#34;&gt;Webhook&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#email" title="Email">Email</a>: <i>
      - &lt;a href=&#34;notification-email.md&#34;&gt;Email&lt;/a&gt;</i>
<a href="#webhook" title="Webhook">Webhook</a>: <i>
      - &lt;a href=&#34;notification-webhook.md&#34;&gt;Webhook&lt;/a&gt;</i>
</pre>

## Properties

#### Email

_Required_: No
_Type_: List of &lt;a href=&#34;notification-email.md&#34;&gt;Email&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webhook

_Required_: No
_Type_: List of &lt;a href=&#34;notification-webhook.md&#34;&gt;Webhook&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

