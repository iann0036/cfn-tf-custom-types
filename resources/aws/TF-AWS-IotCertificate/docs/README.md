# TF::AWS::IotCertificate

Creates and manages an AWS IoT certificate.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::IotCertificate",
    "Properties" : {
        "<a href="#active" title="Active">Active</a>" : <i>Boolean</i>,
        "<a href="#csr" title="Csr">Csr</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::IotCertificate
Properties:
    <a href="#active" title="Active">Active</a>: <i>Boolean</i>
    <a href="#csr" title="Csr">Csr</a>: <i>String</i>
</pre>

## Properties

#### Active

Boolean flag to indicate if the certificate should be active.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Csr

The certificate signing request. Review
[CreateCertificateFromCsr](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html)
for more information on generating a certificate from a certificate signing request (CSR).
If none is specified both the certificate and keys will be generated, review [CreateKeysAndCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateKeysAndCertificate.html)
for more information on generating keys and a certificate.

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

#### Arn

Returns the <code>Arn</code> value.

#### CertificatePem

Returns the <code>CertificatePem</code> value.

#### Id

Returns the <code>Id</code> value.

#### PrivateKey

Returns the <code>PrivateKey</code> value.

#### PublicKey

Returns the <code>PublicKey</code> value.

