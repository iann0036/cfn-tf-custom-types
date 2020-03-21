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

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceProtocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbPort

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbProtocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertificateId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

