# Terraform::Datadog::Dashboard GroupDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#layouttype" title="LayoutType">LayoutType</a>" : <i>String</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#widget" title="Widget">Widget</a>" : <i>[ &lt;a href=&#34;groupdefinition-widget.md&#34;&gt;Widget&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#layouttype" title="LayoutType">LayoutType</a>: <i>String</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#widget" title="Widget">Widget</a>: <i>
      - &lt;a href=&#34;groupdefinition-widget.md&#34;&gt;Widget&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;groupdefinition-widget.md&#34;&gt;Widget&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

