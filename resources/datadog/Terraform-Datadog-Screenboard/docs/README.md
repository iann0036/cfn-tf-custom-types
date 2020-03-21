# Terraform::Datadog::Screenboard

Provides a Datadog screenboard resource. This can be used to create and manage Datadog screenboards.

~> **Note:** This resource is outdated. Use the new [`datadog_dashboard`](dashboard.html) resource instead.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::Screenboard",
    "Properties" : {
        "<a href="#height" title="Height">Height</a>" : <i>String</i>,
        "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
        "<a href="#shared" title="Shared">Shared</a>" : <i>Boolean</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#width" title="Width">Width</a>" : <i>String</i>,
        "<a href="#templatevariable" title="TemplateVariable">TemplateVariable</a>" : <i>[ <a href="templatevariable.md">TemplateVariable</a>, ... ]</i>,
        "<a href="#widget" title="Widget">Widget</a>" : <i>[ <a href="widget.md">Widget</a>, ... ]</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="rule.md">Rule</a>, ... ]</i>,
        "<a href="#tiledef" title="TileDef">TileDef</a>" : <i>[ <a href="tiledef.md">TileDef</a>, ... ]</i>,
        "<a href="#event" title="Event">Event</a>" : <i>[ <a href="event.md">Event</a>, ... ]</i>,
        "<a href="#marker" title="Marker">Marker</a>" : <i>[ <a href="marker.md">Marker</a>, ... ]</i>,
        "<a href="#request" title="Request">Request</a>" : <i>[ <a href="request.md">Request</a>, ... ]</i>,
        "<a href="#apmquery" title="ApmQuery">ApmQuery</a>" : <i>[ <a href="apmquery.md">ApmQuery</a>, ... ]</i>,
        "<a href="#conditionalformat" title="ConditionalFormat">ConditionalFormat</a>" : <i>[ <a href="conditionalformat.md">ConditionalFormat</a>, ... ]</i>,
        "<a href="#logquery" title="LogQuery">LogQuery</a>" : <i>[ <a href="logquery.md">LogQuery</a>, ... ]</i>,
        "<a href="#processquery" title="ProcessQuery">ProcessQuery</a>" : <i>[ <a href="processquery.md">ProcessQuery</a>, ... ]</i>,
        "<a href="#compute" title="Compute">Compute</a>" : <i>[ <a href="compute.md">Compute</a>, ... ]</i>,
        "<a href="#groupby" title="GroupBy">GroupBy</a>" : <i>[ <a href="groupby.md">GroupBy</a>, ... ]</i>,
        "<a href="#search" title="Search">Search</a>" : <i>[ <a href="search.md">Search</a>, ... ]</i>,
        "<a href="#sort" title="Sort">Sort</a>" : <i>[ <a href="sort.md">Sort</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::Screenboard
Properties:
    <a href="#height" title="Height">Height</a>: <i>String</i>
    <a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
    <a href="#shared" title="Shared">Shared</a>: <i>Boolean</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#width" title="Width">Width</a>: <i>String</i>
    <a href="#templatevariable" title="TemplateVariable">TemplateVariable</a>: <i>
      - <a href="templatevariable.md">TemplateVariable</a></i>
    <a href="#widget" title="Widget">Widget</a>: <i>
      - <a href="widget.md">Widget</a></i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="rule.md">Rule</a></i>
    <a href="#tiledef" title="TileDef">TileDef</a>: <i>
      - <a href="tiledef.md">TileDef</a></i>
    <a href="#event" title="Event">Event</a>: <i>
      - <a href="event.md">Event</a></i>
    <a href="#marker" title="Marker">Marker</a>: <i>
      - <a href="marker.md">Marker</a></i>
    <a href="#request" title="Request">Request</a>: <i>
      - <a href="request.md">Request</a></i>
    <a href="#apmquery" title="ApmQuery">ApmQuery</a>: <i>
      - <a href="apmquery.md">ApmQuery</a></i>
    <a href="#conditionalformat" title="ConditionalFormat">ConditionalFormat</a>: <i>
      - <a href="conditionalformat.md">ConditionalFormat</a></i>
    <a href="#logquery" title="LogQuery">LogQuery</a>: <i>
      - <a href="logquery.md">LogQuery</a></i>
    <a href="#processquery" title="ProcessQuery">ProcessQuery</a>: <i>
      - <a href="processquery.md">ProcessQuery</a></i>
    <a href="#compute" title="Compute">Compute</a>: <i>
      - <a href="compute.md">Compute</a></i>
    <a href="#groupby" title="GroupBy">GroupBy</a>: <i>
      - <a href="groupby.md">GroupBy</a></i>
    <a href="#search" title="Search">Search</a>: <i>
      - <a href="search.md">Search</a></i>
    <a href="#sort" title="Sort">Sort</a>: <i>
      - <a href="sort.md">Sort</a></i>
</pre>

## Properties

#### Height

The screenboard's height.
- `width` - (Optional) The screenboard's width.
- `read_only` - (Optional) The read-only status of the screenboard. Default is false.
- `shared` - (Optional) Whether the screenboard is shared or not. Default is false.
- `widget` - (Required) Nested block describing a widget. The structure of this block is described below. Multiple widget blocks are allowed within a datadog_screenboard resource.
- `template_variable` - (Optional) Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a datadog_screenboard resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

The read-only status of the screenboard. Default is false.
- `shared` - (Optional) Whether the screenboard is shared or not. Default is false.
- `widget` - (Required) Nested block describing a widget. The structure of this block is described below. Multiple widget blocks are allowed within a datadog_screenboard resource.
- `template_variable` - (Optional) Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a datadog_screenboard resource.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shared

Whether the screenboard is shared or not. Default is false.
- `widget` - (Required) Nested block describing a widget. The structure of this block is described below. Multiple widget blocks are allowed within a datadog_screenboard resource.
- `template_variable` - (Optional) Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a datadog_screenboard resource.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

The name of the screenboard.
- `height` - (Optional) The screenboard's height.
- `width` - (Optional) The screenboard's width.
- `read_only` - (Optional) The read-only status of the screenboard. Default is false.
- `shared` - (Optional) Whether the screenboard is shared or not. Default is false.
- `widget` - (Required) Nested block describing a widget. The structure of this block is described below. Multiple widget blocks are allowed within a datadog_screenboard resource.
- `template_variable` - (Optional) Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a datadog_screenboard resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Width

The screenboard's width.
- `read_only` - (Optional) The read-only status of the screenboard. Default is false.
- `shared` - (Optional) Whether the screenboard is shared or not. Default is false.
- `widget` - (Required) Nested block describing a widget. The structure of this block is described below. Multiple widget blocks are allowed within a datadog_screenboard resource.
- `template_variable` - (Optional) Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a datadog_screenboard resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateVariable

_Required_: No

_Type_: List of <a href="templatevariable.md">TemplateVariable</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Widget

_Required_: No

_Type_: List of <a href="widget.md">Widget</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="rule.md">Rule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TileDef

_Required_: No

_Type_: List of <a href="tiledef.md">TileDef</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Event

_Required_: No

_Type_: List of <a href="event.md">Event</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Marker

_Required_: No

_Type_: List of <a href="marker.md">Marker</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Request

_Required_: No

_Type_: List of <a href="request.md">Request</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApmQuery

_Required_: No

_Type_: List of <a href="apmquery.md">ApmQuery</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionalFormat

_Required_: No

_Type_: List of <a href="conditionalformat.md">ConditionalFormat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogQuery

_Required_: No

_Type_: List of <a href="logquery.md">LogQuery</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessQuery

_Required_: No

_Type_: List of <a href="processquery.md">ProcessQuery</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Compute

_Required_: No

_Type_: List of <a href="compute.md">Compute</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupBy

_Required_: No

_Type_: List of <a href="groupby.md">GroupBy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Search

_Required_: No

_Type_: List of <a href="search.md">Search</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sort

_Required_: No

_Type_: List of <a href="sort.md">Sort</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

