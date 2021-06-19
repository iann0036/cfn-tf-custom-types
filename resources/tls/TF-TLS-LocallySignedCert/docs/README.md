# TF::TLS::LocallySignedCert

Generates a TLS certificate using a *Certificate Signing Request* (CSR) and
signs it with a provided certificate authority (CA) private key.

Locally-signed certificates are generally only trusted by client software when
setup to use the provided CA. They are normally used in development environments
or when deployed internally to an organization.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TLS::LocallySignedCert",
    "Properties" : {
        "<a href="#alloweduses" title="AllowedUses">AllowedUses</a>" : <i>[ String, ... ]</i>,
        "<a href="#cacertpem" title="CaCertPem">CaCertPem</a>" : <i>String</i>,
        "<a href="#cakeyalgorithm" title="CaKeyAlgorithm">CaKeyAlgorithm</a>" : <i>String</i>,
        "<a href="#caprivatekeypem" title="CaPrivateKeyPem">CaPrivateKeyPem</a>" : <i>String</i>,
        "<a href="#certrequestpem" title="CertRequestPem">CertRequestPem</a>" : <i>String</i>,
        "<a href="#earlyrenewalhours" title="EarlyRenewalHours">EarlyRenewalHours</a>" : <i>Double</i>,
        "<a href="#iscacertificate" title="IsCaCertificate">IsCaCertificate</a>" : <i>Boolean</i>,
        "<a href="#setsubjectkeyid" title="SetSubjectKeyId">SetSubjectKeyId</a>" : <i>Boolean</i>,
        "<a href="#validityperiodhours" title="ValidityPeriodHours">ValidityPeriodHours</a>" : <i>Double</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::TLS::LocallySignedCert
Properties:
    <a href="#alloweduses" title="AllowedUses">AllowedUses</a>: <i>
      - String</i>
    <a href="#cacertpem" title="CaCertPem">CaCertPem</a>: <i>String</i>
    <a href="#cakeyalgorithm" title="CaKeyAlgorithm">CaKeyAlgorithm</a>: <i>String</i>
    <a href="#caprivatekeypem" title="CaPrivateKeyPem">CaPrivateKeyPem</a>: <i>String</i>
    <a href="#certrequestpem" title="CertRequestPem">CertRequestPem</a>: <i>String</i>
    <a href="#earlyrenewalhours" title="EarlyRenewalHours">EarlyRenewalHours</a>: <i>Double</i>
    <a href="#iscacertificate" title="IsCaCertificate">IsCaCertificate</a>: <i>Boolean</i>
    <a href="#setsubjectkeyid" title="SetSubjectKeyId">SetSubjectKeyId</a>: <i>Boolean</i>
    <a href="#validityperiodhours" title="ValidityPeriodHours">ValidityPeriodHours</a>: <i>Double</i>
</pre>

## Properties

#### AllowedUses

List of keywords each describing a use that is permitted
for the issued certificate. The valid keywords are listed below.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaCertPem

PEM-encoded certificate data for the CA.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaKeyAlgorithm

The name of the algorithm for the key provided
in `ca_private_key_pem`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaPrivateKeyPem

PEM-encoded private key data for the CA.
This can be read from a separate file using the ``file`` interpolation
function.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertRequestPem

PEM-encoded request certificate data.

_Required_: Yes

_Type_: String

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

#### IsCaCertificate

Boolean controlling whether the CA flag will be set in the
generated certificate. Defaults to `false`, meaning that the certificate does not represent
a certificate authority.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetSubjectKeyId

If `true`, the certificate will include
the subject key identifier. Defaults to `false`, in which case the subject
key identifier is not set at all.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidityPeriodHours

The number of hours after initial issuing that the
certificate will become invalid.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

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

