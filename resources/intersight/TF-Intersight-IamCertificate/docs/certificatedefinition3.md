# TF::Intersight::IamCertificate CertificateDefinition3

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
    "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
    "<a href="#issuer" title="Issuer">Issuer</a>" : <i>[ <a href="certificatedefinition.md">CertificateDefinition</a>, ... ]</i>,
    "<a href="#notafter" title="NotAfter">NotAfter</a>" : <i>String</i>,
    "<a href="#notbefore" title="NotBefore">NotBefore</a>" : <i>String</i>,
    "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
    "<a href="#pemcertificate" title="PemCertificate">PemCertificate</a>" : <i>String</i>,
    "<a href="#sha256fingerprint" title="Sha256Fingerprint">Sha256Fingerprint</a>" : <i>String</i>,
    "<a href="#signaturealgorithm" title="SignatureAlgorithm">SignatureAlgorithm</a>" : <i>String</i>,
    "<a href="#subject" title="Subject">Subject</a>" : <i>[ <a href="certificatedefinition2.md">CertificateDefinition2</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
<a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
<a href="#issuer" title="Issuer">Issuer</a>: <i>
      - <a href="certificatedefinition.md">CertificateDefinition</a></i>
<a href="#notafter" title="NotAfter">NotAfter</a>: <i>String</i>
<a href="#notbefore" title="NotBefore">NotBefore</a>: <i>String</i>
<a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
<a href="#pemcertificate" title="PemCertificate">PemCertificate</a>: <i>String</i>
<a href="#sha256fingerprint" title="Sha256Fingerprint">Sha256Fingerprint</a>: <i>String</i>
<a href="#signaturealgorithm" title="SignatureAlgorithm">SignatureAlgorithm</a>: <i>String</i>
<a href="#subject" title="Subject">Subject</a>: <i>
      - <a href="certificatedefinition2.md">CertificateDefinition2</a></i>
</pre>

## Properties

#### AdditionalProperties

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Issuer

_Required_: No

_Type_: List of <a href="certificatedefinition.md">CertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotAfter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotBefore

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PemCertificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sha256Fingerprint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignatureAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subject

_Required_: No

_Type_: List of <a href="certificatedefinition2.md">CertificateDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

