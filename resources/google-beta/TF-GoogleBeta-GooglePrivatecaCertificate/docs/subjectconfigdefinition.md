# TF::GoogleBeta::GooglePrivatecaCertificate SubjectConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#commonname" title="CommonName">CommonName</a>" : <i>String</i>,
    "<a href="#subject" title="Subject">Subject</a>" : <i>[ <a href="certificatedescriptiondefinition11.md">CertificateDescriptionDefinition11</a>, ... ]</i>,
    "<a href="#subjectaltname" title="SubjectAltName">SubjectAltName</a>" : <i>[ <a href="certificatedescriptiondefinition14.md">CertificateDescriptionDefinition14</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#commonname" title="CommonName">CommonName</a>: <i>String</i>
<a href="#subject" title="Subject">Subject</a>: <i>
      - <a href="certificatedescriptiondefinition11.md">CertificateDescriptionDefinition11</a></i>
<a href="#subjectaltname" title="SubjectAltName">SubjectAltName</a>: <i>
      - <a href="certificatedescriptiondefinition14.md">CertificateDescriptionDefinition14</a></i>
</pre>

## Properties

#### CommonName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subject

_Required_: No

_Type_: List of <a href="certificatedescriptiondefinition11.md">CertificateDescriptionDefinition11</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectAltName

_Required_: No

_Type_: List of <a href="certificatedescriptiondefinition14.md">CertificateDescriptionDefinition14</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

