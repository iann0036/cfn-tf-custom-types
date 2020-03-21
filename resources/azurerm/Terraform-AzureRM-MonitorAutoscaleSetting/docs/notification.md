# Terraform::AzureRM::MonitorAutoscaleSetting Notification

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#email" title="Email">Email</a>" : <i>[ <a href="notification-email.md">Email</a>, ... ]</i>,
    "<a href="#webhook" title="Webhook">Webhook</a>" : <i>[ <a href="notification-webhook.md">Webhook</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#email" title="Email">Email</a>: <i>
      - <a href="notification-email.md">Email</a></i>
<a href="#webhook" title="Webhook">Webhook</a>: <i>
      - <a href="notification-webhook.md">Webhook</a></i>
</pre>

## Properties

#### Email

_Required_: No
_Type_: List of <a href="notification-email.md">Email</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webhook

_Required_: No
_Type_: List of <a href="notification-webhook.md">Webhook</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

