# TF::AWS::AppmeshVirtualGateway ValidationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>" : <i>[ <a href="subjectalternativenamesdefinition.md">SubjectAlternativeNamesDefinition</a>, ... ]</i>,
    "<a href="#trust" title="Trust">Trust</a>" : <i>[ <a href="trustdefinition.md">TrustDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>: <i>
      - <a href="subjectalternativenamesdefinition.md">SubjectAlternativeNamesDefinition</a></i>
<a href="#trust" title="Trust">Trust</a>: <i>
      - <a href="trustdefinition.md">TrustDefinition</a></i>
</pre>

## Properties

#### SubjectAlternativeNames

_Required_: No

_Type_: List of <a href="subjectalternativenamesdefinition.md">SubjectAlternativeNamesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trust

_Required_: No

_Type_: List of <a href="trustdefinition.md">TrustDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

