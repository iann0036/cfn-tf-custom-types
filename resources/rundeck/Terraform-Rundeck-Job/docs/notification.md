# Terraform::Rundeck::Job Notification

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#webhookurls" title="WebhookUrls">WebhookUrls</a>" : <i>[ String, ... ]</i>,
    "<a href="#email" title="Email">Email</a>" : <i>[ &lt;a href=&#34;notification-email.md&#34;&gt;Email&lt;/a&gt;, ... ]</i>,
    "<a href="#plugin" title="Plugin">Plugin</a>" : <i>[ &lt;a href=&#34;notification-plugin.md&#34;&gt;Plugin&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#webhookurls" title="WebhookUrls">WebhookUrls</a>: <i>
      - String</i>
<a href="#email" title="Email">Email</a>: <i>
      - &lt;a href=&#34;notification-email.md&#34;&gt;Email&lt;/a&gt;</i>
<a href="#plugin" title="Plugin">Plugin</a>: <i>
      - &lt;a href=&#34;notification-plugin.md&#34;&gt;Plugin&lt;/a&gt;</i>
</pre>

## Properties

#### Type

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebhookUrls

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: No
_Type_: List of &lt;a href=&#34;notification-email.md&#34;&gt;Email&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plugin

_Required_: No
_Type_: List of &lt;a href=&#34;notification-plugin.md&#34;&gt;Plugin&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

