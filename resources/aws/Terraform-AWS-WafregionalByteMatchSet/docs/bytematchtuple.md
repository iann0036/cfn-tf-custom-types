# Terraform::AWS::WafregionalByteMatchSet ByteMatchTuple

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#positionalconstraint" title="PositionalConstraint">PositionalConstraint</a>" : <i>String</i>,
    "<a href="#targetstring" title="TargetString">TargetString</a>" : <i>String</i>,
    "<a href="#texttransformation" title="TextTransformation">TextTransformation</a>" : <i>String</i>,
    "<a href="#fieldtomatch" title="FieldToMatch">FieldToMatch</a>" : <i>[ <a href="bytematchtuple-fieldtomatch.md">FieldToMatch</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#positionalconstraint" title="PositionalConstraint">PositionalConstraint</a>: <i>String</i>
<a href="#targetstring" title="TargetString">TargetString</a>: <i>String</i>
<a href="#texttransformation" title="TextTransformation">TextTransformation</a>: <i>String</i>
<a href="#fieldtomatch" title="FieldToMatch">FieldToMatch</a>: <i>
      - <a href="bytematchtuple-fieldtomatch.md">FieldToMatch</a></i>
</pre>

## Properties

#### PositionalConstraint

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetString

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TextTransformation

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldToMatch

_Required_: No

_Type_: List of <a href="bytematchtuple-fieldtomatch.md">FieldToMatch</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

