# TF::OnePassword::Item SectionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#label" title="Label">Label</a>" : <i>String</i>,
    "<a href="#field" title="Field">Field</a>" : <i>[ <a href="fielddefinition.md">FieldDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#label" title="Label">Label</a>: <i>String</i>
<a href="#field" title="Field">Field</a>: <i>
      - <a href="fielddefinition.md">FieldDefinition</a></i>
</pre>

## Properties

#### Label

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Field

_Required_: No

_Type_: List of <a href="fielddefinition.md">FieldDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

