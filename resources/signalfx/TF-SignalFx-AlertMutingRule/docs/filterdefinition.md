# TF::SignalFx::AlertMutingRule FilterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#negated" title="Negated">Negated</a>" : <i>Boolean</i>,
    "<a href="#property" title="Property">Property</a>" : <i>String</i>,
    "<a href="#propertyvalue" title="PropertyValue">PropertyValue</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#negated" title="Negated">Negated</a>: <i>Boolean</i>
<a href="#property" title="Property">Property</a>: <i>String</i>
<a href="#propertyvalue" title="PropertyValue">PropertyValue</a>: <i>String</i>
</pre>

## Properties

#### Negated

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Property

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropertyValue

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
