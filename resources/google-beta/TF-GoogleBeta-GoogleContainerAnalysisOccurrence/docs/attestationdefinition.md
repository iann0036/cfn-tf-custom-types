# TF::GoogleBeta::GoogleContainerAnalysisOccurrence AttestationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#serializedpayload" title="SerializedPayload">SerializedPayload</a>" : <i>String</i>,
    "<a href="#signatures" title="Signatures">Signatures</a>" : <i>[ <a href="signaturesdefinition.md">SignaturesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#serializedpayload" title="SerializedPayload">SerializedPayload</a>: <i>String</i>
<a href="#signatures" title="Signatures">Signatures</a>: <i>
      - <a href="signaturesdefinition.md">SignaturesDefinition</a></i>
</pre>

## Properties

#### SerializedPayload

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Signatures

_Required_: No

_Type_: List of <a href="signaturesdefinition.md">SignaturesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

