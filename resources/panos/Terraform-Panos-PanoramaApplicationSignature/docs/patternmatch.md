# Terraform::Panos::PanoramaApplicationSignature PatternMatch

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#context" title="Context">Context</a>" : <i>String</i>,
    "<a href="#pattern" title="Pattern">Pattern</a>" : <i>String</i>,
    "<a href="#qualifiers" title="Qualifiers">Qualifiers</a>" : <i>[ &lt;a href=&#34;patternmatch-qualifiers.md&#34;&gt;Qualifiers&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#context" title="Context">Context</a>: <i>String</i>
<a href="#pattern" title="Pattern">Pattern</a>: <i>String</i>
<a href="#qualifiers" title="Qualifiers">Qualifiers</a>: <i>
      - &lt;a href=&#34;patternmatch-qualifiers.md&#34;&gt;Qualifiers&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;patternmatch-qualifiers.md&#34;&gt;Qualifiers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

