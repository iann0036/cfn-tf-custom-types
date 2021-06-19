# TF::Venafi::Certificate

Provides access to TLS key and certificate data enrolled using Venafi. This can be used to define a
certificate.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Venafi::Certificate",
    "Properties" : {
        "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>String</i>,
        "<a href="#certificatedn" title="CertificateDn">CertificateDn</a>" : <i>String</i>,
        "<a href="#commonname" title="CommonName">CommonName</a>" : <i>String</i>,
        "<a href="#csrpem" title="CsrPem">CsrPem</a>" : <i>String</i>,
        "<a href="#customfields" title="CustomFields">CustomFields</a>" : <i>[ <a href="customfieldsdefinition.md">CustomFieldsDefinition</a>, ... ]</i>,
        "<a href="#ecdsacurve" title="EcdsaCurve">EcdsaCurve</a>" : <i>String</i>,
        "<a href="#expirationwindow" title="ExpirationWindow">ExpirationWindow</a>" : <i>Double</i>,
        "<a href="#issuerhint" title="IssuerHint">IssuerHint</a>" : <i>String</i>,
        "<a href="#keypassword" title="KeyPassword">KeyPassword</a>" : <i>String</i>,
        "<a href="#pkcs12" title="Pkcs12">Pkcs12</a>" : <i>String</i>,
        "<a href="#privatekeypem" title="PrivateKeyPem">PrivateKeyPem</a>" : <i>String</i>,
        "<a href="#rsabits" title="RsaBits">RsaBits</a>" : <i>Double</i>,
        "<a href="#sandns" title="SanDns">SanDns</a>" : <i>[ String, ... ]</i>,
        "<a href="#sanemail" title="SanEmail">SanEmail</a>" : <i>[ String, ... ]</i>,
        "<a href="#sanip" title="SanIp">SanIp</a>" : <i>[ String, ... ]</i>,
        "<a href="#validdays" title="ValidDays">ValidDays</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Venafi::Certificate
Properties:
    <a href="#algorithm" title="Algorithm">Algorithm</a>: <i>String</i>
    <a href="#certificatedn" title="CertificateDn">CertificateDn</a>: <i>String</i>
    <a href="#commonname" title="CommonName">CommonName</a>: <i>String</i>
    <a href="#csrpem" title="CsrPem">CsrPem</a>: <i>String</i>
    <a href="#customfields" title="CustomFields">CustomFields</a>: <i>
      - <a href="customfieldsdefinition.md">CustomFieldsDefinition</a></i>
    <a href="#ecdsacurve" title="EcdsaCurve">EcdsaCurve</a>: <i>String</i>
    <a href="#expirationwindow" title="ExpirationWindow">ExpirationWindow</a>: <i>Double</i>
    <a href="#issuerhint" title="IssuerHint">IssuerHint</a>: <i>String</i>
    <a href="#keypassword" title="KeyPassword">KeyPassword</a>: <i>String</i>
    <a href="#pkcs12" title="Pkcs12">Pkcs12</a>: <i>String</i>
    <a href="#privatekeypem" title="PrivateKeyPem">PrivateKeyPem</a>: <i>String</i>
    <a href="#rsabits" title="RsaBits">RsaBits</a>: <i>Double</i>
    <a href="#sandns" title="SanDns">SanDns</a>: <i>
      - String</i>
    <a href="#sanemail" title="SanEmail">SanEmail</a>: <i>
      - String</i>
    <a href="#sanip" title="SanIp">SanIp</a>: <i>
      - String</i>
    <a href="#validdays" title="ValidDays">ValidDays</a>: <i>Double</i>
</pre>

## Properties

#### Algorithm

Key encryption algorithm, either RSA or ECDSA.
Defaults to "RSA".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateDn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommonName

The common name of the certificate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsrPem

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomFields

Collection of Custom Field name-value pairs to
assign to the certificate.

_Required_: No

_Type_: List of <a href="customfieldsdefinition.md">CustomFieldsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcdsaCurve

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpirationWindow

Number of hours before certificate expiry
to request a new certificate.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuerHint

Used with valid_days to indicate the target
issuer when using Trust Protection Platform.  Relevant values are: "DigiCert",
"Entrust", and "Microsoft".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyPassword

The password used to encrypt the private key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pkcs12

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKeyPem

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RsaBits

Number of bits to use when generating an RSA key.
Applies when algorithm=RSA.  Defaults to 2048.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SanDns

List of DNS names to use as alternative
subjects of the certificate.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SanEmail

List of email addresses to use as
alternative subjects of the certificate.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SanIp

List of IP addresses to use as alternative
subjects of the certificate.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidDays

Desired number of days for which the new
certificate will be valid.

_Required_: No

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

#### Certificate

Returns the <code>Certificate</code> value.

#### Chain

Returns the <code>Chain</code> value.

#### Id

Returns the <code>Id</code> value.

