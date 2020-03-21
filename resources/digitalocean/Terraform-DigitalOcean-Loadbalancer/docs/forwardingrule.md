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

The ID of the TLS certificate to be used for SSL termination.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntryPort

An integer representing the port on which the Load Balancer instance will listen.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntryProtocol

The protocol used for traffic to the Load Balancer. The possible values are: `http`, `https`, `http2` or `tcp`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetPort

An integer representing the port on the backend Droplets to which the Load Balancer will send traffic.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetProtocol

The protocol used for traffic from the Load Balancer to the backend Droplets. The possible values are: `http`, `https`, `http2` or `tcp`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsPassthrough

A boolean value indicating whether SSL encrypted traffic will be passed through to the backend Droplets. The default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

