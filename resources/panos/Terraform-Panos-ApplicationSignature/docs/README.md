# Terraform::Panos::ApplicationSignature

This resource allows you to add/update/delete application signatures.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::ApplicationSignature",
    "Properties" : {
        "<a href="#applicationobject" title="ApplicationObject">ApplicationObject</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#orderedmatch" title="OrderedMatch">OrderedMatch</a>" : <i>Boolean</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
        "<a href="#andcondition" title="AndCondition">AndCondition</a>" : <i>[ <a href="andcondition.md">AndCondition</a>, ... ]</i>,
        "<a href="#orcondition" title="OrCondition">OrCondition</a>" : <i>[ <a href="orcondition.md">OrCondition</a>, ... ]</i>,
        "<a href="#equalto" title="EqualTo">EqualTo</a>" : <i>[ <a href="equalto.md">EqualTo</a>, ... ]</i>,
        "<a href="#greaterthan" title="GreaterThan">GreaterThan</a>" : <i>[ <a href="greaterthan.md">GreaterThan</a>, ... ]</i>,
        "<a href="#lessthan" title="LessThan">LessThan</a>" : <i>[ <a href="lessthan.md">LessThan</a>, ... ]</i>,
        "<a href="#patternmatch" title="PatternMatch">PatternMatch</a>" : <i>[ <a href="patternmatch.md">PatternMatch</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::ApplicationSignature
Properties:
    <a href="#applicationobject" title="ApplicationObject">ApplicationObject</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#orderedmatch" title="OrderedMatch">OrderedMatch</a>: <i>Boolean</i>
    <a href="#scope" title="Scope">Scope</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
    <a href="#andcondition" title="AndCondition">AndCondition</a>: <i>
      - <a href="andcondition.md">AndCondition</a></i>
    <a href="#orcondition" title="OrCondition">OrCondition</a>: <i>
      - <a href="orcondition.md">OrCondition</a></i>
    <a href="#equalto" title="EqualTo">EqualTo</a>: <i>
      - <a href="equalto.md">EqualTo</a></i>
    <a href="#greaterthan" title="GreaterThan">GreaterThan</a>: <i>
      - <a href="greaterthan.md">GreaterThan</a></i>
    <a href="#lessthan" title="LessThan">LessThan</a>: <i>
      - <a href="lessthan.md">LessThan</a></i>
    <a href="#patternmatch" title="PatternMatch">PatternMatch</a>: <i>
      - <a href="patternmatch.md">PatternMatch</a></i>
</pre>

## Properties

#### ApplicationObject

The applciation object for this signature.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

The description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The signature's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderedMatch

Set to `false` to disable ordered matching
(default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

The signature's scope.  Valid values are
`transaction` (default) or `session`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

The signature's vsys (default: `vsys1`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AndCondition

_Required_: No

_Type_: List of <a href="andcondition.md">AndCondition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrCondition

_Required_: No

_Type_: List of <a href="orcondition.md">OrCondition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EqualTo

_Required_: No

_Type_: List of <a href="equalto.md">EqualTo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GreaterThan

_Required_: No

_Type_: List of <a href="greaterthan.md">GreaterThan</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LessThan

_Required_: No

_Type_: List of <a href="lessthan.md">LessThan</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatternMatch

_Required_: No

_Type_: List of <a href="patternmatch.md">PatternMatch</a>

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

