# TF::AVI::Pkiprofile CaCertsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
    "<a href="#certificatesigningrequest" title="CertificateSigningRequest">CertificateSigningRequest</a>" : <i>String</i>,
    "<a href="#chainverified" title="ChainVerified">ChainVerified</a>" : <i>Boolean</i>,
    "<a href="#daysuntilexpire" title="DaysUntilExpire">DaysUntilExpire</a>" : <i>Double</i>,
    "<a href="#expirystatus" title="ExpiryStatus">ExpiryStatus</a>" : <i>String</i>,
    "<a href="#fingerprint" title="Fingerprint">Fingerprint</a>" : <i>String</i>,
    "<a href="#notafter" title="NotAfter">NotAfter</a>" : <i>String</i>,
    "<a href="#notbefore" title="NotBefore">NotBefore</a>" : <i>String</i>,
    "<a href="#publickey" title="PublicKey">PublicKey</a>" : <i>String</i>,
    "<a href="#selfsigned" title="SelfSigned">SelfSigned</a>" : <i>Boolean</i>,
    "<a href="#serialnumber" title="SerialNumber">SerialNumber</a>" : <i>String</i>,
    "<a href="#signature" title="Signature">Signature</a>" : <i>String</i>,
    "<a href="#signaturealgorithm" title="SignatureAlgorithm">SignatureAlgorithm</a>" : <i>String</i>,
    "<a href="#subjectaltnames" title="SubjectAltNames">SubjectAltNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#text" title="Text">Text</a>" : <i>String</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#issuer" title="Issuer">Issuer</a>" : <i>[ <a href="issuerdefinition.md">IssuerDefinition</a>, ... ]</i>,
    "<a href="#keyparams" title="KeyParams">KeyParams</a>" : <i>[ <a href="keyparamsdefinition.md">KeyParamsDefinition</a>, ... ]</i>,
    "<a href="#subject" title="Subject">Subject</a>" : <i>[ <a href="subjectdefinition.md">SubjectDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
<a href="#certificatesigningrequest" title="CertificateSigningRequest">CertificateSigningRequest</a>: <i>String</i>
<a href="#chainverified" title="ChainVerified">ChainVerified</a>: <i>Boolean</i>
<a href="#daysuntilexpire" title="DaysUntilExpire">DaysUntilExpire</a>: <i>Double</i>
<a href="#expirystatus" title="ExpiryStatus">ExpiryStatus</a>: <i>String</i>
<a href="#fingerprint" title="Fingerprint">Fingerprint</a>: <i>String</i>
<a href="#notafter" title="NotAfter">NotAfter</a>: <i>String</i>
<a href="#notbefore" title="NotBefore">NotBefore</a>: <i>String</i>
<a href="#publickey" title="PublicKey">PublicKey</a>: <i>String</i>
<a href="#selfsigned" title="SelfSigned">SelfSigned</a>: <i>Boolean</i>
<a href="#serialnumber" title="SerialNumber">SerialNumber</a>: <i>String</i>
<a href="#signature" title="Signature">Signature</a>: <i>String</i>
<a href="#signaturealgorithm" title="SignatureAlgorithm">SignatureAlgorithm</a>: <i>String</i>
<a href="#subjectaltnames" title="SubjectAltNames">SubjectAltNames</a>: <i>
      - String</i>
<a href="#text" title="Text">Text</a>: <i>String</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#issuer" title="Issuer">Issuer</a>: <i>
      - <a href="issuerdefinition.md">IssuerDefinition</a></i>
<a href="#keyparams" title="KeyParams">KeyParams</a>: <i>
      - <a href="keyparamsdefinition.md">KeyParamsDefinition</a></i>
<a href="#subject" title="Subject">Subject</a>: <i>
      - <a href="subjectdefinition.md">SubjectDefinition</a></i>
</pre>

## Properties

#### Certificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateSigningRequest

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChainVerified

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DaysUntilExpire

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpiryStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fingerprint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotAfter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotBefore

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelfSigned

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerialNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Signature

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignatureAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectAltNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Text

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Issuer

_Required_: No

_Type_: List of <a href="issuerdefinition.md">IssuerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyParams

_Required_: No

_Type_: List of <a href="keyparamsdefinition.md">KeyParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subject

_Required_: No

_Type_: List of <a href="subjectdefinition.md">SubjectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

