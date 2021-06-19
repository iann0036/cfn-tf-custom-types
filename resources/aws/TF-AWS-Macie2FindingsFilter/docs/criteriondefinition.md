# TF::AWS::Macie2FindingsFilter CriterionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#eq" title="Eq">Eq</a>" : <i>[ String, ... ]</i>,
    "<a href="#eqexactmatch" title="EqExactMatch">EqExactMatch</a>" : <i>[ String, ... ]</i>,
    "<a href="#field" title="Field">Field</a>" : <i>String</i>,
    "<a href="#gt" title="Gt">Gt</a>" : <i>String</i>,
    "<a href="#gte" title="Gte">Gte</a>" : <i>String</i>,
    "<a href="#lt" title="Lt">Lt</a>" : <i>String</i>,
    "<a href="#lte" title="Lte">Lte</a>" : <i>String</i>,
    "<a href="#neq" title="Neq">Neq</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#eq" title="Eq">Eq</a>: <i>
      - String</i>
<a href="#eqexactmatch" title="EqExactMatch">EqExactMatch</a>: <i>
      - String</i>
<a href="#field" title="Field">Field</a>: <i>String</i>
<a href="#gt" title="Gt">Gt</a>: <i>String</i>
<a href="#gte" title="Gte">Gte</a>: <i>String</i>
<a href="#lt" title="Lt">Lt</a>: <i>String</i>
<a href="#lte" title="Lte">Lte</a>: <i>String</i>
<a href="#neq" title="Neq">Neq</a>: <i>
      - String</i>
</pre>

## Properties

#### Eq

The value for the property matches (equals) the specified value. If you specify multiple values, Amazon Macie uses OR logic to join the values.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EqExactMatch

The value for the property exclusively matches (equals an exact match for) all the specified values. If you specify multiple values, Amazon Macie uses AND logic to join the values.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Field

The name of the field to be evaluated.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gt

The value for the property is greater than the specified value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gte

The value for the property is greater than or equal to the specified value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lt

The value for the property is less than the specified value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lte

The value for the property is less than or equal to the specified value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Neq

The value for the property doesn't match (doesn't equal) the specified value. If you specify multiple values, Amazon Macie uses OR logic to join the values.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

