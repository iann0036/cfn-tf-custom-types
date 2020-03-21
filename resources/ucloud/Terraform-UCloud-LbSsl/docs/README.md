# Terraform::UCloud::LbSsl

Provides a Load Balancer SSL certificate resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::UCloud::LbSsl",
    "Properties" : {
        "<a href="#cacert" title="CaCert">CaCert</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#privatekey" title="PrivateKey">PrivateKey</a>" : <i>String</i>,
        "<a href="#usercert" title="UserCert">UserCert</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::UCloud::LbSsl
Properties:
    <a href="#cacert" title="CaCert">CaCert</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#privatekey" title="PrivateKey">PrivateKey</a>: <i>String</i>
    <a href="#usercert" title="UserCert">UserCert</a>: <i>String</i>
</pre>

## Properties

#### CaCert

The content of the CA certificate about ssl certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the LB ssl, which contains 1-63 characters and only support Chinese, English, numbers, '-', '_', '.'. If not specified, terraform will auto-generate a name beginning with `tf-lb-ssl`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKey

The content of the private key about ssl certificate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserCert

The content of the user certificate about ssl certificate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

