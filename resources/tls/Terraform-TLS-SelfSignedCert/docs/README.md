# Terraform::TLS::SelfSignedCert

Generates a *self-signed* TLS certificate in PEM format, which is the typical
format used to configure TLS server software.

Self-signed certificates are generally not trusted by client software such
as web browsers. Therefore clients are likely to generate trust warnings when
connecting to a server that has a self-signed certificate. Self-signed certificates
are usually used only in development environments or apps deployed internally
to an organization.

This resource is intended to be used in conjunction with a Terraform provider
that has a resource that requires a TLS certificate, such as:

* ``aws_iam_server_certificate`` to register certificates for use with AWS *Elastic
Load Balancer*, *Elastic Beanstalk*, *CloudFront* or *OpsWorks*.

* ``heroku_cert`` to register certificates for applications deployed on Heroku.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TLS::SelfSignedCert",
    "Properties" : {
        "<a href="#alloweduses" title="AllowedUses">AllowedUses</a>" : <i>[ String, ... ]</i>,
        "<a href="#dnsnames" title="DnsNames">DnsNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#earlyrenewalhours" title="EarlyRenewalHours">EarlyRenewalHours</a>" : <i>Double</i>,
        "<a href="#ipaddresses" title="IpAddresses">IpAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#iscacertificate" title="IsCaCertificate">IsCaCertificate</a>" : <i>Boolean</i>,
        "<a href="#keyalgorithm" title="KeyAlgorithm">KeyAlgorithm</a>" : <i>String</i>,
        "<a href="#privatekeypem" title="PrivateKeyPem">PrivateKeyPem</a>" : <i>String</i>,
        "<a href="#setsubjectkeyid" title="SetSubjectKeyId">SetSubjectKeyId</a>" : <i>Boolean</i>,
        "<a href="#uris" title="Uris">Uris</a>" : <i>[ String, ... ]</i>,
        "<a href="#validityperiodhours" title="ValidityPeriodHours">ValidityPeriodHours</a>" : <i>Double</i>,
        "<a href="#subject" title="Subject">Subject</a>" : <i>[ <a href="subject.md">Subject</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TLS::SelfSignedCert
Properties:
    <a href="#alloweduses" title="AllowedUses">AllowedUses</a>: <i>
      - String</i>
    <a href="#dnsnames" title="DnsNames">DnsNames</a>: <i>
      - String</i>
    <a href="#earlyrenewalhours" title="EarlyRenewalHours">EarlyRenewalHours</a>: <i>Double</i>
    <a href="#ipaddresses" title="IpAddresses">IpAddresses</a>: <i>
      - String</i>
    <a href="#iscacertificate" title="IsCaCertificate">IsCaCertificate</a>: <i>Boolean</i>
    <a href="#keyalgorithm" title="KeyAlgorithm">KeyAlgorithm</a>: <i>String</i>
    <a href="#privatekeypem" title="PrivateKeyPem">PrivateKeyPem</a>: <i>String</i>
    <a href="#setsubjectkeyid" title="SetSubjectKeyId">SetSubjectKeyId</a>: <i>Boolean</i>
    <a href="#uris" title="Uris">Uris</a>: <i>
      - String</i>
    <a href="#validityperiodhours" title="ValidityPeriodHours">ValidityPeriodHours</a>: <i>Double</i>
    <a href="#subject" title="Subject">Subject</a>: <i>
      - <a href="subject.md">Subject</a></i>
</pre>

## Properties

#### AllowedUses

List of keywords each describing a use that is permitted
for the issued certificate. The valid keywords are listed below.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsNames

List of DNS names for which a certificate is being requested.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EarlyRenewalHours

If set, the resource will consider the certificate to
have expired the given number of hours before its actual expiry time. This can be useful
to deploy an updated certificate in advance of the expiration of the current certificate.
Note however that the old certificate remains valid until its true expiration time, since
this resource does not (and cannot) support certificate revocation. Note also that this
advance update can only be performed should the Terraform configuration be applied during the
early renewal period.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddresses

List of IP addresses for which a certificate is being requested.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsCaCertificate

Boolean controlling whether the CA flag will be set in the
generated certificate. Defaults to `false`, meaning that the certificate does not represent
a certificate authority.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyAlgorithm

The name of the algorithm for the key provided
in `private_key_pem`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKeyPem

PEM-encoded private key data. This can be
read from a separate file using the ``file`` interpolation function. If the
certificate is being generated to be used for a throwaway development
environment or other non-critical application, the `tls_private_key` resource
can be used to generate a TLS private key from within Terraform. Only
an irreversable secure hash of the private key will be stored in the Terraform
state.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetSubjectKeyId

If `true`, the certificate will include
the subject key identifier. Defaults to `false`, in which case the subject
key identifier is not set at all.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uris

List of URIs for which a certificate is being requested.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidityPeriodHours

The number of hours after initial issuing that the
certificate will become invalid.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subject

_Required_: No

_Type_: List of <a href="subject.md">Subject</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CertPem

Returns the <code>CertPem</code> value.

#### Id

Returns the <code>Id</code> value.

#### ReadyForRenewal

Returns the <code>ReadyForRenewal</code> value.

#### ValidityEndTime

Returns the <code>ValidityEndTime</code> value.

#### ValidityStartTime

Returns the <code>ValidityStartTime</code> value.

