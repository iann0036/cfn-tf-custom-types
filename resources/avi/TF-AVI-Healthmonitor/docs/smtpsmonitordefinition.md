# TF::AVI::Healthmonitor SmtpsMonitorDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#domainname" title="Domainname">Domainname</a>" : <i>String</i>,
    "<a href="#maildata" title="MailData">MailData</a>" : <i>String</i>,
    "<a href="#recipientsids" title="RecipientsIds">RecipientsIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#senderid" title="SenderId">SenderId</a>" : <i>String</i>,
    "<a href="#sslattributes" title="SslAttributes">SslAttributes</a>" : <i>[ <a href="sslattributesdefinition.md">SslAttributesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#domainname" title="Domainname">Domainname</a>: <i>String</i>
<a href="#maildata" title="MailData">MailData</a>: <i>String</i>
<a href="#recipientsids" title="RecipientsIds">RecipientsIds</a>: <i>
      - String</i>
<a href="#senderid" title="SenderId">SenderId</a>: <i>String</i>
<a href="#sslattributes" title="SslAttributes">SslAttributes</a>: <i>
      - <a href="sslattributesdefinition.md">SslAttributesDefinition</a></i>
</pre>

## Properties

#### Domainname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MailData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecipientsIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SenderId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslAttributes

_Required_: No

_Type_: List of <a href="sslattributesdefinition.md">SslAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

