# Terraform::DigitalOcean::Loadbalancer ForwardingRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificateid" title="CertificateId">CertificateId</a>" : <i>String</i>,
    "<a href="#entryport" title="EntryPort">EntryPort</a>" : <i>Double</i>,
    "<a href="#entryprotocol" title="EntryProtocol">EntryProtocol</a>" : <i>String</i>,
    "<a href="#targetport" title="TargetPort">TargetPort</a>" : <i>Double</i>,
    "<a href="#targetprotocol" title="TargetProtocol">TargetProtocol</a>" : <i>String</i>,
    "<a href="#tlspassthrough" title="TlsPassthrough">TlsPassthrough</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#certificateid" title="CertificateId">CertificateId</a>: <i>String</i>
<a href="#entryport" title="EntryPort">EntryPort</a>: <i>Double</i>
<a href="#entryprotocol" title="EntryProtocol">EntryProtocol</a>: <i>String</i>
<a href="#targetport" title="TargetPort">TargetPort</a>: <i>Double</i>
<a href="#targetprotocol" title="TargetProtocol">TargetProtocol</a>: <i>String</i>
<a href="#tlspassthrough" title="TlsPassthrough">TlsPassthrough</a>: <i>Boolean</i>
</pre>

## Properties

#### CertificateId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntryPort

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntryProtocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetPort

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetProtocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsPassthrough

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

