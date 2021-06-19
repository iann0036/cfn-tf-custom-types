# TF::DigitalOcean::Certificate

Provides a DigitalOcean Certificate resource that allows you to manage
certificates for configuring TLS termination in Load Balancers.
Certificates created with this resource can be referenced in your
Load Balancer configuration via their ID. The certificate can either
be a custom one provided by you or automatically generated one with
Let's Encrypt.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::DigitalOcean::Certificate",
    "Properties" : {
        "<a href="#certificatechain" title="CertificateChain">CertificateChain</a>" : <i>String</i>,
        "<a href="#domains" title="Domains">Domains</a>" : <i>[ String, ... ]</i>,
        "<a href="#leafcertificate" title="LeafCertificate">LeafCertificate</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#privatekey" title="PrivateKey">PrivateKey</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::DigitalOcean::Certificate
Properties:
    <a href="#certificatechain" title="CertificateChain">CertificateChain</a>: <i>String</i>
    <a href="#domains" title="Domains">Domains</a>: <i>
      - String</i>
    <a href="#leafcertificate" title="LeafCertificate">LeafCertificate</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#privatekey" title="PrivateKey">PrivateKey</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### CertificateChain

The full PEM-formatted trust chain
between the certificate authority's certificate and your domain's TLS
certificate. Only valid when type is `custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domains

List of fully qualified domain names (FQDNs) for
which the certificate will be issued. The domains must be managed using
DigitalOcean's DNS. Only valid when type is `lets_encrypt`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeafCertificate

The contents of a PEM-formatted public
TLS certificate. Only valid when type is `custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the certificate for identification.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKey

The contents of a PEM-formatted private-key
corresponding to the SSL certificate. Only valid when type is `custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of certificate to provision. Can be either
`custom` or `lets_encrypt`. Defaults to `custom`.

_Required_: No

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

#### Id

Returns the <code>Id</code> value.

#### NotAfter

Returns the <code>NotAfter</code> value.

#### Sha1Fingerprint

Returns the <code>Sha1Fingerprint</code> value.

#### State

Returns the <code>State</code> value.

#### Uuid

Returns the <code>Uuid</code> value.

