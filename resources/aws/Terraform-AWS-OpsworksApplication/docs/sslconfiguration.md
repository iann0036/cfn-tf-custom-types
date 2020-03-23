# Terraform::AWS::OpsworksApplication SslConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
    "<a href="#chain" title="Chain">Chain</a>" : <i>String</i>,
    "<a href="#privatekey" title="PrivateKey">PrivateKey</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
<a href="#chain" title="Chain">Chain</a>: <i>String</i>
<a href="#privatekey" title="PrivateKey">PrivateKey</a>: <i>String</i>
</pre>

## Properties

#### Certificate

The contents of the certificate's domain.crt file.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Chain

Can be used to specify an intermediate certificate authority key or client authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKey

The private key; the contents of the certificate's domain.key file.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

