# Terraform::ACME::Certificate

The `acme_certificate` resource can be used to create and manage an ACME TLS
certificate.

-> **NOTE:** As the usage model of Terraform generally sees it as being run on
a different server than a certificate would normally be placed on, the
`acme_certificate` resource only supports DNS challenges.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::ACME::Certificate",
    "Properties" : {
        "<a href="#accountkeypem" title="AccountKeyPem">AccountKeyPem</a>" : <i>String</i>,
        "<a href="#certificatep12password" title="CertificateP12Password">CertificateP12Password</a>" : <i>String</i>,
        "<a href="#certificaterequestpem" title="CertificateRequestPem">CertificateRequestPem</a>" : <i>String</i>,
        "<a href="#commonname" title="CommonName">CommonName</a>" : <i>String</i>,
        "<a href="#keytype" title="KeyType">KeyType</a>" : <i>String</i>,
        "<a href="#mindaysremaining" title="MinDaysRemaining">MinDaysRemaining</a>" : <i>Double</i>,
        "<a href="#muststaple" title="MustStaple">MustStaple</a>" : <i>Boolean</i>,
        "<a href="#recursivenameservers" title="RecursiveNameservers">RecursiveNameservers</a>" : <i>[ String, ... ]</i>,
        "<a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#dnschallenge" title="DnsChallenge">DnsChallenge</a>" : <i>[ <a href="dnschallenge.md">DnsChallenge</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::ACME::Certificate
Properties:
    <a href="#accountkeypem" title="AccountKeyPem">AccountKeyPem</a>: <i>String</i>
    <a href="#certificatep12password" title="CertificateP12Password">CertificateP12Password</a>: <i>String</i>
    <a href="#certificaterequestpem" title="CertificateRequestPem">CertificateRequestPem</a>: <i>String</i>
    <a href="#commonname" title="CommonName">CommonName</a>: <i>String</i>
    <a href="#keytype" title="KeyType">KeyType</a>: <i>String</i>
    <a href="#mindaysremaining" title="MinDaysRemaining">MinDaysRemaining</a>: <i>Double</i>
    <a href="#muststaple" title="MustStaple">MustStaple</a>: <i>Boolean</i>
    <a href="#recursivenameservers" title="RecursiveNameservers">RecursiveNameservers</a>: <i>
      - String</i>
    <a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>: <i>
      - String</i>
    <a href="#dnschallenge" title="DnsChallenge">DnsChallenge</a>: <i>
      - <a href="dnschallenge.md">DnsChallenge</a></i>
</pre>

## Properties

#### AccountKeyPem

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateP12Password

Password to be used when generating
the PFX file stored in [`certificate_p12`](#certificate_p12). Defaults to an
empty string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateRequestPem

A pre-created certificate request, such as one
from [`tls_cert_request`][tls-cert-request], or one from an external source,
in PEM format.  Either this, or the in-resource request options (`common_name`,
`key_type`, and optionally `subject_alternative_names`) need to be specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommonName

The certificate's common name, the primary domain that the
certificate will be recognized for. Required when not specifying a CSR.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyType

The key type for the certificate's private key. Can be one of:
`P256` and `P384` (for ECDSA keys of respective length) or `2048`, `4096`, and
`8192` (for RSA keys of respective length). Required when not specifying a
CSR. The default is `2048` (RSA key of 2048 bits).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinDaysRemaining

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MustStaple

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecursiveNameservers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectAlternativeNames

The certificate's subject alternative names,
domains that this certificate will also be recognized for. Only valid when not
specifying a CSR.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsChallenge

_Required_: No

_Type_: List of <a href="dnschallenge.md">DnsChallenge</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CertificateDomain

Returns the <code>CertificateDomain</code> value.

#### CertificateP12

Returns the <code>CertificateP12</code> value.

#### CertificatePem

Returns the <code>CertificatePem</code> value.

#### CertificateUrl

Returns the <code>CertificateUrl</code> value.

#### Id

Returns the <code>Id</code> value.

#### IssuerPem

Returns the <code>IssuerPem</code> value.

#### PrivateKeyPem

Returns the <code>PrivateKeyPem</code> value.

