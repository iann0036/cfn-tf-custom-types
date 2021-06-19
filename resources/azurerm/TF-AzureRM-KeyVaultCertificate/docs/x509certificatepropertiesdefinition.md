# TF::AzureRM::KeyVaultCertificate X509CertificatePropertiesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#extendedkeyusage" title="ExtendedKeyUsage">ExtendedKeyUsage</a>" : <i>[ String, ... ]</i>,
    "<a href="#keyusage" title="KeyUsage">KeyUsage</a>" : <i>[ String, ... ]</i>,
    "<a href="#subject" title="Subject">Subject</a>" : <i>String</i>,
    "<a href="#validityinmonths" title="ValidityInMonths">ValidityInMonths</a>" : <i>Double</i>,
    "<a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>" : <i>[ <a href="subjectalternativenamesdefinition.md">SubjectAlternativeNamesDefinition</a>, ... ]</i>
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
      - <a href="subjectalternativenamesdefinition.md">SubjectAlternativeNamesDefinition</a></i>
</pre>

## Properties

#### ExtendedKeyUsage

A list of Extended/Enhanced Key Usages. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyUsage

A list of uses associated with this Key. Possible values include `cRLSign`, `dataEncipherment`, `decipherOnly`, `digitalSignature`, `encipherOnly`, `keyAgreement`, `keyCertSign`, `keyEncipherment` and `nonRepudiation` and are case-sensitive. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subject

The Certificate's Subject. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidityInMonths

The Certificates Validity Period in Months. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectAlternativeNames

_Required_: No

_Type_: List of <a href="subjectalternativenamesdefinition.md">SubjectAlternativeNamesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

