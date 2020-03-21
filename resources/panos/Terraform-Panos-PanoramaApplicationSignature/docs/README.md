# Terraform::Panos::PanoramaApplicationSignature

CloudFormation equivalent of panos_panorama_application_signature

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaApplicationSignature",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#applicationobject" title="ApplicationObject">ApplicationObject</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#orderedmatch" title="OrderedMatch">OrderedMatch</a>" : <i>Boolean</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
        "<a href="#andcondition" title="AndCondition">AndCondition</a>" : <i>[ &lt;a href=&#34;andcondition.md&#34;&gt;AndCondition&lt;/a&gt;, ... ]</i>,
        "<a href="#orcondition" title="OrCondition">OrCondition</a>" : <i>[ &lt;a href=&#34;orcondition.md&#34;&gt;OrCondition&lt;/a&gt;, ... ]</i>,
        "<a href="#equalto" title="EqualTo">EqualTo</a>" : <i>[ &lt;a href=&#34;equalto.md&#34;&gt;EqualTo&lt;/a&gt;, ... ]</i>,
        "<a href="#greaterthan" title="GreaterThan">GreaterThan</a>" : <i>[ &lt;a href=&#34;greaterthan.md&#34;&gt;GreaterThan&lt;/a&gt;, ... ]</i>,
        "<a href="#lessthan" title="LessThan">LessThan</a>" : <i>[ &lt;a href=&#34;lessthan.md&#34;&gt;LessThan&lt;/a&gt;, ... ]</i>,
        "<a href="#patternmatch" title="PatternMatch">PatternMatch</a>" : <i>[ &lt;a href=&#34;patternmatch.md&#34;&gt;PatternMatch&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaApplicationSignature
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#applicationobject" title="ApplicationObject">ApplicationObject</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#orderedmatch" title="OrderedMatch">OrderedMatch</a>: <i>Boolean</i>
    <a href="#scope" title="Scope">Scope</a>: <i>String</i>
    <a href="#andcondition" title="AndCondition">AndCondition</a>: <i>
      - &lt;a href=&#34;andcondition.md&#34;&gt;AndCondition&lt;/a&gt;</i>
    <a href="#orcondition" title="OrCondition">OrCondition</a>: <i>
      - &lt;a href=&#34;orcondition.md&#34;&gt;OrCondition&lt;/a&gt;</i>
    <a href="#equalto" title="EqualTo">EqualTo</a>: <i>
      - &lt;a href=&#34;equalto.md&#34;&gt;EqualTo&lt;/a&gt;</i>
    <a href="#greaterthan" title="GreaterThan">GreaterThan</a>: <i>
      - &lt;a href=&#34;greaterthan.md&#34;&gt;GreaterThan&lt;/a&gt;</i>
    <a href="#lessthan" title="LessThan">LessThan</a>: <i>
      - &lt;a href=&#34;lessthan.md&#34;&gt;LessThan&lt;/a&gt;</i>
    <a href="#patternmatch" title="PatternMatch">PatternMatch</a>: <i>
      - &lt;a href=&#34;patternmatch.md&#34;&gt;PatternMatch&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationObject

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderedMatch

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AndCondition

_Required_: No

_Type_: List of &lt;a href=&#34;andcondition.md&#34;&gt;AndCondition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrCondition

_Required_: No

_Type_: List of &lt;a href=&#34;orcondition.md&#34;&gt;OrCondition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EqualTo

_Required_: No

_Type_: List of &lt;a href=&#34;equalto.md&#34;&gt;EqualTo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GreaterThan

_Required_: No

_Type_: List of &lt;a href=&#34;greaterthan.md&#34;&gt;GreaterThan&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LessThan

_Required_: No

_Type_: List of &lt;a href=&#34;lessthan.md&#34;&gt;LessThan&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatternMatch

_Required_: No

_Type_: List of &lt;a href=&#34;patternmatch.md&#34;&gt;PatternMatch&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

