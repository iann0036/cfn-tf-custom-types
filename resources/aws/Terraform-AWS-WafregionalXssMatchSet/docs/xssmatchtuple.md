# Terraform::AWS::WafregionalXssMatchSet XssMatchTuple

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#texttransformation" title="TextTransformation">TextTransformation</a>" : <i>String</i>,
    "<a href="#fieldtomatch" title="FieldToMatch">FieldToMatch</a>" : <i>[ &lt;a href=&#34;xssmatchtuple-fieldtomatch.md&#34;&gt;FieldToMatch&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#texttransformation" title="TextTransformation">TextTransformation</a>: <i>String</i>
<a href="#fieldtomatch" title="FieldToMatch">FieldToMatch</a>: <i>
      - &lt;a href=&#34;xssmatchtuple-fieldtomatch.md&#34;&gt;FieldToMatch&lt;/a&gt;</i>
</pre>

## Properties

#### TextTransformation

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldToMatch

_Required_: No
_Type_: List of &lt;a href=&#34;xssmatchtuple-fieldtomatch.md&#34;&gt;FieldToMatch&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

