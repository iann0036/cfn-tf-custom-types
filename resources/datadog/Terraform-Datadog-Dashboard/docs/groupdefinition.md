# Terraform::Datadog::Dashboard GroupDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#layouttype" title="LayoutType">LayoutType</a>" : <i>String</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#widget" title="Widget">Widget</a>" : <i>[ <a href="groupdefinition-widget.md">Widget</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#layouttype" title="LayoutType">LayoutType</a>: <i>String</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#widget" title="Widget">Widget</a>: <i>
      - <a href="groupdefinition-widget.md">Widget</a></i>
</pre>

## Properties

#### LayoutType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Widget

_Required_: No

_Type_: List of <a href="groupdefinition-widget.md">Widget</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

