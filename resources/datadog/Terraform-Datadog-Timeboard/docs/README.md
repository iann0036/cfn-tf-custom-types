# Terraform::Datadog::Timeboard

Provides a Datadog timeboard resource. This can be used to create and manage Datadog timeboards.

~> **Note:**This resource is outdated. Use the new [`datadog_dashboard`](dashboard.html) resource instead.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::Timeboard",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#graph" title="Graph">Graph</a>" : <i>[ <a href="graph.md">Graph</a>, ... ]</i>,
        "<a href="#templatevariable" title="TemplateVariable">TemplateVariable</a>" : <i>[ <a href="templatevariable.md">TemplateVariable</a>, ... ]</i>,
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
Type: Terraform::Datadog::Timeboard
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#graph" title="Graph">Graph</a>: <i>
      - <a href="graph.md">Graph</a></i>
    <a href="#templatevariable" title="TemplateVariable">TemplateVariable</a>: <i>
      - <a href="templatevariable.md">TemplateVariable</a></i>
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

#### Description

A description of the dashboard's content.
- `read_only` - (Optional) The read-only status of the timeboard. Default is false.
- `graph` - (Required) Nested block describing a graph definition. The structure of this block is described below. Multiple graph blocks are allowed within a datadog_timeboard resource.
- `template_variable` - (Optional) Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a datadog_timeboard resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

The read-only status of the timeboard. Default is false.
- `graph` - (Required) Nested block describing a graph definition. The structure of this block is described below. Multiple graph blocks are allowed within a datadog_timeboard resource.
- `template_variable` - (Optional) Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a datadog_timeboard resource.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

The name of the dashboard.
- `description` - (Required) A description of the dashboard's content.
- `read_only` - (Optional) The read-only status of the timeboard. Default is false.
- `graph` - (Required) Nested block describing a graph definition. The structure of this block is described below. Multiple graph blocks are allowed within a datadog_timeboard resource.
- `template_variable` - (Optional) Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a datadog_timeboard resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Graph

_Required_: No

_Type_: List of <a href="graph.md">Graph</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateVariable

_Required_: No

_Type_: List of <a href="templatevariable.md">TemplateVariable</a>

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

#### Id

Returns the <code>Id</code> value.

