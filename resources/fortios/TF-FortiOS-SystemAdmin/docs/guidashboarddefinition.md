# TF::FortiOS::SystemAdmin GuiDashboardDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#columns" title="Columns">Columns</a>" : <i>Double</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#layouttype" title="LayoutType">LayoutType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
    "<a href="#widget" title="Widget">Widget</a>" : <i>[ <a href="widgetdefinition.md">WidgetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#columns" title="Columns">Columns</a>: <i>Double</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#layouttype" title="LayoutType">LayoutType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#scope" title="Scope">Scope</a>: <i>String</i>
<a href="#widget" title="Widget">Widget</a>: <i>
      - <a href="widgetdefinition.md">WidgetDefinition</a></i>
</pre>

## Properties

#### Columns

Number of columns.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Dashboard ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LayoutType

Layout type. Valid values: `responsive`, `fixed`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Dashboard name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

Dashboard scope. Valid values: `global`, `vdom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Widget

_Required_: No

_Type_: List of <a href="widgetdefinition.md">WidgetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

