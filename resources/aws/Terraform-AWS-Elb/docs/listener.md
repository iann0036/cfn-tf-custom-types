# Terraform::AWS::Elb Listener

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#instanceport" title="InstancePort">InstancePort</a>" : <i>Double</i>,
    "<a href="#instanceprotocol" title="InstanceProtocol">InstanceProtocol</a>" : <i>String</i>,
    "<a href="#lbport" title="LbPort">LbPort</a>" : <i>Double</i>,
    "<a href="#lbprotocol" title="LbProtocol">LbProtocol</a>" : <i>String</i>,
    "<a href="#sslcertificateid" title="SslCertificateId">SslCertificateId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#instanceport" title="InstancePort">InstancePort</a>: <i>Double</i>
<a href="#instanceprotocol" title="InstanceProtocol">InstanceProtocol</a>: <i>String</i>
<a href="#lbport" title="LbPort">LbPort</a>: <i>Double</i>
<a href="#lbprotocol" title="LbProtocol">LbProtocol</a>: <i>String</i>
<a href="#sslcertificateid" title="SslCertificateId">SslCertificateId</a>: <i>String</i>
</pre>

## Properties

#### InstancePort

The port on the instance to route to.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceProtocol

The protocol to use to the instance. Valid
values are `HTTP`, `HTTPS`, `TCP`, or `SSL`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbPort

The port to listen on for the load balancer.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbProtocol

The protocol to listen on. Valid values are `HTTP`,
`HTTPS`, `TCP`, or `SSL`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertificateId

The ARN of an SSL certificate you have
uploaded to AWS IAM. **Note ECDSA-specific restrictions below.  Only valid when `lb_protocol` is either HTTPS or SSL**.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

