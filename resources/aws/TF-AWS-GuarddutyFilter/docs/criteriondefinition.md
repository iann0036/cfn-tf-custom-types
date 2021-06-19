# TF::AWS::GuarddutyFilter CriterionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#equals" title="Equals">Equals</a>" : <i>[ String, ... ]</i>,
    "<a href="#field" title="Field">Field</a>" : <i>String</i>,
    "<a href="#greaterthan" title="GreaterThan">GreaterThan</a>" : <i>String</i>,
    "<a href="#greaterthanorequal" title="GreaterThanOrEqual">GreaterThanOrEqual</a>" : <i>String</i>,
    "<a href="#lessthan" title="LessThan">LessThan</a>" : <i>String</i>,
    "<a href="#lessthanorequal" title="LessThanOrEqual">LessThanOrEqual</a>" : <i>String</i>,
    "<a href="#notequals" title="NotEquals">NotEquals</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#equals" title="Equals">Equals</a>: <i>
      - String</i>
<a href="#field" title="Field">Field</a>: <i>String</i>
<a href="#greaterthan" title="GreaterThan">GreaterThan</a>: <i>String</i>
<a href="#greaterthanorequal" title="GreaterThanOrEqual">GreaterThanOrEqual</a>: <i>String</i>
<a href="#lessthan" title="LessThan">LessThan</a>: <i>String</i>
<a href="#lessthanorequal" title="LessThanOrEqual">LessThanOrEqual</a>: <i>String</i>
<a href="#notequals" title="NotEquals">NotEquals</a>: <i>
      - String</i>
</pre>

## Properties

#### Equals

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Field

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GreaterThan

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GreaterThanOrEqual

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LessThan

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LessThanOrEqual

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotEquals

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

