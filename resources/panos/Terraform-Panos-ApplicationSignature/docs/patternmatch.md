# Terraform::Panos::ApplicationSignature PatternMatch

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#context" title="Context">Context</a>" : <i>String</i>,
    "<a href="#pattern" title="Pattern">Pattern</a>" : <i>String</i>,
    "<a href="#qualifiers" title="Qualifiers">Qualifiers</a>" : <i>[ <a href="patternmatch-qualifiers.md">Qualifiers</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#context" title="Context">Context</a>: <i>String</i>
<a href="#pattern" title="Pattern">Pattern</a>: <i>String</i>
<a href="#qualifiers" title="Qualifiers">Qualifiers</a>: <i>
      - <a href="patternmatch-qualifiers.md">Qualifiers</a></i>
</pre>

## Properties

#### Context

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pattern

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Qualifiers

_Required_: No

_Type_: List of <a href="patternmatch-qualifiers.md">Qualifiers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

