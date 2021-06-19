# TF::Volterra::Discovery TlsInfoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
    "<a href="#servername" title="ServerName">ServerName</a>" : <i>String</i>,
    "<a href="#trustedcaurl" title="TrustedCaUrl">TrustedCaUrl</a>" : <i>String</i>,
    "<a href="#cacertificateurl" title="CaCertificateUrl">CaCertificateUrl</a>" : <i>[ <a href="cacertificateurldefinition.md">CaCertificateUrlDefinition</a>, ... ]</i>,
    "<a href="#certificateurl" title="CertificateUrl">CertificateUrl</a>" : <i>[ <a href="certificateurldefinition.md">CertificateUrlDefinition</a>, ... ]</i>,
    "<a href="#keyurl" title="KeyUrl">KeyUrl</a>" : <i>[ <a href="keyurldefinition.md">KeyUrlDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
<a href="#servername" title="ServerName">ServerName</a>: <i>String</i>
<a href="#trustedcaurl" title="TrustedCaUrl">TrustedCaUrl</a>: <i>String</i>
<a href="#cacertificateurl" title="CaCertificateUrl">CaCertificateUrl</a>: <i>
      - <a href="cacertificateurldefinition.md">CaCertificateUrlDefinition</a></i>
<a href="#certificateurl" title="CertificateUrl">CertificateUrl</a>: <i>
      - <a href="certificateurldefinition.md">CertificateUrlDefinition</a></i>
<a href="#keyurl" title="KeyUrl">KeyUrl</a>: <i>
      - <a href="keyurldefinition.md">KeyUrlDefinition</a></i>
</pre>

## Properties

#### Certificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedCaUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaCertificateUrl

_Required_: No

_Type_: List of <a href="cacertificateurldefinition.md">CaCertificateUrlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateUrl

_Required_: No

_Type_: List of <a href="certificateurldefinition.md">CertificateUrlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyUrl

_Required_: No

_Type_: List of <a href="keyurldefinition.md">KeyUrlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

