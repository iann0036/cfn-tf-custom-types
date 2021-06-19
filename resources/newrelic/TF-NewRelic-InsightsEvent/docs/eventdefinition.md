# TF::NewRelic::InsightsEvent EventDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#timestamp" title="Timestamp">Timestamp</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#attribute" title="Attribute">Attribute</a>" : <i>[ <a href="attributedefinition.md">AttributeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#timestamp" title="Timestamp">Timestamp</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#attribute" title="Attribute">Attribute</a>: <i>
      - <a href="attributedefinition.md">AttributeDefinition</a></i>
</pre>

## Properties

#### Timestamp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Attribute

_Required_: No

_Type_: List of <a href="attributedefinition.md">AttributeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

