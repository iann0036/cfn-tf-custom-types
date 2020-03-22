# Terraform::AWS::WafregionalRegexMatchSet

CloudFormation equivalent of aws_wafregional_regex_match_set

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::WafregionalRegexMatchSet",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#regexmatchtuple" title="RegexMatchTuple">RegexMatchTuple</a>" : <i>[ <a href="regexmatchtuple.md">RegexMatchTuple</a>, ... ]</i>,
        "<a href="#fieldtomatch" title="FieldToMatch">FieldToMatch</a>" : <i>[ <a href="fieldtomatch.md">FieldToMatch</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::WafregionalRegexMatchSet
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#regexmatchtuple" title="RegexMatchTuple">RegexMatchTuple</a>: <i>
      - <a href="regexmatchtuple.md">RegexMatchTuple</a></i>
    <a href="#fieldtomatch" title="FieldToMatch">FieldToMatch</a>: <i>
      - <a href="fieldtomatch.md">FieldToMatch</a></i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegexMatchTuple

_Required_: No

_Type_: List of <a href="regexmatchtuple.md">RegexMatchTuple</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldToMatch

_Required_: No

_Type_: List of <a href="fieldtomatch.md">FieldToMatch</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

