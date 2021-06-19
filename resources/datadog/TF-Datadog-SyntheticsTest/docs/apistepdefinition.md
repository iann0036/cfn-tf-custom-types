# TF::Datadog::SyntheticsTest ApiStepDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowfailure" title="AllowFailure">AllowFailure</a>" : <i>Boolean</i>,
    "<a href="#iscritical" title="IsCritical">IsCritical</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#requestheaders" title="RequestHeaders">RequestHeaders</a>" : <i>[ <a href="requestheadersdefinition.md">RequestHeadersDefinition</a>, ... ]</i>,
    "<a href="#requestquery" title="RequestQuery">RequestQuery</a>" : <i>[ <a href="requestquerydefinition.md">RequestQueryDefinition</a>, ... ]</i>,
    "<a href="#subtype" title="Subtype">Subtype</a>" : <i>String</i>,
    "<a href="#assertion" title="Assertion">Assertion</a>" : <i>[ <a href="assertiondefinition.md">AssertionDefinition</a>, ... ]</i>,
    "<a href="#extractedvalue" title="ExtractedValue">ExtractedValue</a>" : <i>[ <a href="extractedvaluedefinition.md">ExtractedValueDefinition</a>, ... ]</i>,
    "<a href="#requestbasicauth" title="RequestBasicauth">RequestBasicauth</a>" : <i>[ <a href="requestbasicauthdefinition.md">RequestBasicauthDefinition</a>, ... ]</i>,
    "<a href="#requestclientcertificate" title="RequestClientCertificate">RequestClientCertificate</a>" : <i>[ <a href="requestclientcertificatedefinition.md">RequestClientCertificateDefinition</a>, ... ]</i>,
    "<a href="#requestdefinition" title="RequestDefinition">RequestDefinition</a>" : <i>[ <a href="requestdefinitiondefinition.md">RequestDefinitionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowfailure" title="AllowFailure">AllowFailure</a>: <i>Boolean</i>
<a href="#iscritical" title="IsCritical">IsCritical</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#requestheaders" title="RequestHeaders">RequestHeaders</a>: <i>
      - <a href="requestheadersdefinition.md">RequestHeadersDefinition</a></i>
<a href="#requestquery" title="RequestQuery">RequestQuery</a>: <i>
      - <a href="requestquerydefinition.md">RequestQueryDefinition</a></i>
<a href="#subtype" title="Subtype">Subtype</a>: <i>String</i>
<a href="#assertion" title="Assertion">Assertion</a>: <i>
      - <a href="assertiondefinition.md">AssertionDefinition</a></i>
<a href="#extractedvalue" title="ExtractedValue">ExtractedValue</a>: <i>
      - <a href="extractedvaluedefinition.md">ExtractedValueDefinition</a></i>
<a href="#requestbasicauth" title="RequestBasicauth">RequestBasicauth</a>: <i>
      - <a href="requestbasicauthdefinition.md">RequestBasicauthDefinition</a></i>
<a href="#requestclientcertificate" title="RequestClientCertificate">RequestClientCertificate</a>: <i>
      - <a href="requestclientcertificatedefinition.md">RequestClientCertificateDefinition</a></i>
<a href="#requestdefinition" title="RequestDefinition">RequestDefinition</a>: <i>
      - <a href="requestdefinitiondefinition.md">RequestDefinitionDefinition</a></i>
</pre>

## Properties

#### AllowFailure

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsCritical

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeaders

_Required_: No

_Type_: List of <a href="requestheadersdefinition.md">RequestHeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestQuery

_Required_: No

_Type_: List of <a href="requestquerydefinition.md">RequestQueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subtype

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Assertion

_Required_: No

_Type_: List of <a href="assertiondefinition.md">AssertionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtractedValue

_Required_: No

_Type_: List of <a href="extractedvaluedefinition.md">ExtractedValueDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestBasicauth

_Required_: No

_Type_: List of <a href="requestbasicauthdefinition.md">RequestBasicauthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestClientCertificate

_Required_: No

_Type_: List of <a href="requestclientcertificatedefinition.md">RequestClientCertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestDefinition

_Required_: No

_Type_: List of <a href="requestdefinitiondefinition.md">RequestDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

