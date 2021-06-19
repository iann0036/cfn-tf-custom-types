# TF::Fastly::TlsPrivateKey

Uploads a Custom TLS Private Key to Fastly. This can be combined with a `fastly_tls_custom_certificate` resource to provide a TLS Certificate able to be applied to a Fastly Service.

The Private Key resource requires a key in PEM format, and a name to identify it.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Fastly::TlsPrivateKey",
    "Properties" : {
        "<a href="#keypem" title="KeyPem">KeyPem</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Fastly::TlsPrivateKey
Properties:
    <a href="#keypem" title="KeyPem">KeyPem</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### KeyPem

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

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

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### KeyLength

Returns the <code>KeyLength</code> value.

#### KeyType

Returns the <code>KeyType</code> value.

#### PublicKeySha1

Returns the <code>PublicKeySha1</code> value.

#### Replace

Returns the <code>Replace</code> value.

