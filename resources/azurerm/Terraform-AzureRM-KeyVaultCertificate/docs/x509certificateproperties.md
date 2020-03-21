# Terraform::AzureRM::KeyVaultCertificate X509CertificateProperties

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#extendedkeyusage" title="ExtendedKeyUsage">ExtendedKeyUsage</a>" : <i>[ String, ... ]</i>,
    "<a href="#keyusage" title="KeyUsage">KeyUsage</a>" : <i>[ String, ... ]</i>,
    "<a href="#subject" title="Subject">Subject</a>" : <i>String</i>,
    "<a href="#validityinmonths" title="ValidityInMonths">ValidityInMonths</a>" : <i>Double</i>,
    "<a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>" : <i>[ &lt;a href=&#34;x509certificateproperties-subjectalternativenames.md&#34;&gt;SubjectAlternativeNames&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#extendedkeyusage" title="ExtendedKeyUsage">ExtendedKeyUsage</a>: <i>
      - String</i>
<a href="#keyusage" title="KeyUsage">KeyUsage</a>: <i>
      - String</i>
<a href="#subject" title="Subject">Subject</a>: <i>String</i>
<a href="#validityinmonths" title="ValidityInMonths">ValidityInMonths</a>: <i>Double</i>
<a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>: <i>
      - &lt;a href=&#34;x509certificateproperties-subjectalternativenames.md&#34;&gt;SubjectAlternativeNames&lt;/a&gt;</i>
</pre>

## Properties

#### ExtendedKeyUsage

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyUsage

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subject

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidityInMonths

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectAlternativeNames

_Required_: No
_Type_: List of &lt;a href=&#34;x509certificateproperties-subjectalternativenames.md&#34;&gt;SubjectAlternativeNames&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

