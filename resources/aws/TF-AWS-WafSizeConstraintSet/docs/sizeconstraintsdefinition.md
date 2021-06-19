# TF::AWS::WafSizeConstraintSet SizeConstraintsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#comparisonoperator" title="ComparisonOperator">ComparisonOperator</a>" : <i>String</i>,
    "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
    "<a href="#texttransformation" title="TextTransformation">TextTransformation</a>" : <i>String</i>,
    "<a href="#fieldtomatch" title="FieldToMatch">FieldToMatch</a>" : <i>[ <a href="fieldtomatchdefinition.md">FieldToMatchDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#comparisonoperator" title="ComparisonOperator">ComparisonOperator</a>: <i>String</i>
<a href="#size" title="Size">Size</a>: <i>Double</i>
<a href="#texttransformation" title="TextTransformation">TextTransformation</a>: <i>String</i>
<a href="#fieldtomatch" title="FieldToMatch">FieldToMatch</a>: <i>
      - <a href="fieldtomatchdefinition.md">FieldToMatchDefinition</a></i>
</pre>

## Properties

#### ComparisonOperator

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TextTransformation

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldToMatch

_Required_: No

_Type_: List of <a href="fieldtomatchdefinition.md">FieldToMatchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

