# TF::CheckPoint::ManagementThreatIndicator ObservablesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#confidence" title="Confidence">Confidence</a>" : <i>String</i>,
    "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
    "<a href="#ipaddressfirst" title="IpAddressFirst">IpAddressFirst</a>" : <i>String</i>,
    "<a href="#ipaddresslast" title="IpAddressLast">IpAddressLast</a>" : <i>String</i>,
    "<a href="#mailcc" title="MailCc">MailCc</a>" : <i>String</i>,
    "<a href="#mailfrom" title="MailFrom">MailFrom</a>" : <i>String</i>,
    "<a href="#mailreplyto" title="MailReplyTo">MailReplyTo</a>" : <i>String</i>,
    "<a href="#mailsubject" title="MailSubject">MailSubject</a>" : <i>String</i>,
    "<a href="#mailto" title="MailTo">MailTo</a>" : <i>String</i>,
    "<a href="#md5" title="Md5">Md5</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#product" title="Product">Product</a>" : <i>String</i>,
    "<a href="#severity" title="Severity">Severity</a>" : <i>String</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#confidence" title="Confidence">Confidence</a>: <i>String</i>
<a href="#domain" title="Domain">Domain</a>: <i>String</i>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
<a href="#ipaddressfirst" title="IpAddressFirst">IpAddressFirst</a>: <i>String</i>
<a href="#ipaddresslast" title="IpAddressLast">IpAddressLast</a>: <i>String</i>
<a href="#mailcc" title="MailCc">MailCc</a>: <i>String</i>
<a href="#mailfrom" title="MailFrom">MailFrom</a>: <i>String</i>
<a href="#mailreplyto" title="MailReplyTo">MailReplyTo</a>: <i>String</i>
<a href="#mailsubject" title="MailSubject">MailSubject</a>: <i>String</i>
<a href="#mailto" title="MailTo">MailTo</a>: <i>String</i>
<a href="#md5" title="Md5">Md5</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#product" title="Product">Product</a>: <i>String</i>
<a href="#severity" title="Severity">Severity</a>: <i>String</i>
<a href="#url" title="Url">Url</a>: <i>String</i>
</pre>

## Properties

#### Confidence

The confidence level the indicator has that a real threat has been uncovered.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

The name of a domain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

A valid IP-Address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddressFirst

A valid IP-Address, the beginning of the range. If you configure this parameter with a value, you must also configure the value of the 'ip-address-last' parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddressLast

A valid IP-Address, the end of the range. If you configure this parameter with a value, you must also configure the value of the 'ip-address-first' parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MailCc

A valid E-Mail address, cc field.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MailFrom

A valid E-Mail address, sender field.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MailReplyTo

A valid E-Mail address, reply-to field.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MailSubject

Subject of E-Mail.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MailTo

A valid E-Mail address, recipient filed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Md5

A valid MD5 sequence.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Object name. Should be unique in the domain.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Product

The software blade that processes the observable: AV - AntiVirus, AB - AntiBot.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

The severity level of the threat.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

A valid URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

