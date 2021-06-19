# TF::Panos::ApplicationSignature LessThanDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#context" title="Context">Context</a>" : <i>String</i>,
    "<a href="#qualifiers" title="Qualifiers">Qualifiers</a>" : <i>[ <a href="qualifiersdefinition.md">QualifiersDefinition</a>, ... ]</i>,
    "<a href="#value" title="Value">Value</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#context" title="Context">Context</a>: <i>String</i>
<a href="#qualifiers" title="Qualifiers">Qualifiers</a>: <i>
      - <a href="qualifiersdefinition.md">QualifiersDefinition</a></i>
<a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### Context

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Qualifiers

_Required_: No

_Type_: List of <a href="qualifiersdefinition.md">QualifiersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

