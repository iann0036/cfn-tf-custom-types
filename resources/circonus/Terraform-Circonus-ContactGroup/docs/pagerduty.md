# Terraform::Circonus::ContactGroup PagerDuty

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#contactgroupfallback" title="ContactGroupFallback">ContactGroupFallback</a>" : <i>String</i>,
    "<a href="#servicekey" title="ServiceKey">ServiceKey</a>" : <i>String</i>,
    "<a href="#webhookurl" title="WebhookUrl">WebhookUrl</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#contactgroupfallback" title="ContactGroupFallback">ContactGroupFallback</a>: <i>String</i>
<a href="#servicekey" title="ServiceKey">ServiceKey</a>: <i>String</i>
<a href="#webhookurl" title="WebhookUrl">WebhookUrl</a>: <i>String</i>
</pre>

## Properties

#### ContactGroupFallback

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebhookUrl

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

