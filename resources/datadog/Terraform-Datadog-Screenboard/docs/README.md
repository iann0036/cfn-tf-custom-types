# Terraform::Datadog::Screenboard

CloudFormation equivalent of datadog_screenboard

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::Screenboard",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#height" title="Height">Height</a>" : <i>String</i>,
        "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
        "<a href="#shared" title="Shared">Shared</a>" : <i>Boolean</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#width" title="Width">Width</a>" : <i>String</i>,
        "<a href="#templatevariable" title="TemplateVariable">TemplateVariable</a>" : <i>[ &lt;a href=&#34;templatevariable.md&#34;&gt;TemplateVariable&lt;/a&gt;, ... ]</i>,
        "<a href="#widget" title="Widget">Widget</a>" : <i>[ &lt;a href=&#34;widget.md&#34;&gt;Widget&lt;/a&gt;, ... ]</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ &lt;a href=&#34;rule.md&#34;&gt;Rule&lt;/a&gt;, ... ]</i>,
        "<a href="#tiledef" title="TileDef">TileDef</a>" : <i>[ &lt;a href=&#34;tiledef.md&#34;&gt;TileDef&lt;/a&gt;, ... ]</i>,
        "<a href="#event" title="Event">Event</a>" : <i>[ &lt;a href=&#34;event.md&#34;&gt;Event&lt;/a&gt;, ... ]</i>,
        "<a href="#marker" title="Marker">Marker</a>" : <i>[ &lt;a href=&#34;marker.md&#34;&gt;Marker&lt;/a&gt;, ... ]</i>,
        "<a href="#request" title="Request">Request</a>" : <i>[ &lt;a href=&#34;request.md&#34;&gt;Request&lt;/a&gt;, ... ]</i>,
        "<a href="#apmquery" title="ApmQuery">ApmQuery</a>" : <i>[ &lt;a href=&#34;apmquery.md&#34;&gt;ApmQuery&lt;/a&gt;, ... ]</i>,
        "<a href="#conditionalformat" title="ConditionalFormat">ConditionalFormat</a>" : <i>[ &lt;a href=&#34;conditionalformat.md&#34;&gt;ConditionalFormat&lt;/a&gt;, ... ]</i>,
        "<a href="#logquery" title="LogQuery">LogQuery</a>" : <i>[ &lt;a href=&#34;logquery.md&#34;&gt;LogQuery&lt;/a&gt;, ... ]</i>,
        "<a href="#processquery" title="ProcessQuery">ProcessQuery</a>" : <i>[ &lt;a href=&#34;processquery.md&#34;&gt;ProcessQuery&lt;/a&gt;, ... ]</i>,
        "<a href="#compute" title="Compute">Compute</a>" : <i>[ &lt;a href=&#34;compute.md&#34;&gt;Compute&lt;/a&gt;, ... ]</i>,
        "<a href="#groupby" title="GroupBy">GroupBy</a>" : <i>[ &lt;a href=&#34;groupby.md&#34;&gt;GroupBy&lt;/a&gt;, ... ]</i>,
        "<a href="#search" title="Search">Search</a>" : <i>[ &lt;a href=&#34;search.md&#34;&gt;Search&lt;/a&gt;, ... ]</i>,
        "<a href="#sort" title="Sort">Sort</a>" : <i>[ &lt;a href=&#34;sort.md&#34;&gt;Sort&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::Screenboard
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#height" title="Height">Height</a>: <i>String</i>
    <a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
    <a href="#shared" title="Shared">Shared</a>: <i>Boolean</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#width" title="Width">Width</a>: <i>String</i>
    <a href="#templatevariable" title="TemplateVariable">TemplateVariable</a>: <i>
      - &lt;a href=&#34;templatevariable.md&#34;&gt;TemplateVariable&lt;/a&gt;</i>
    <a href="#widget" title="Widget">Widget</a>: <i>
      - &lt;a href=&#34;widget.md&#34;&gt;Widget&lt;/a&gt;</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - &lt;a href=&#34;rule.md&#34;&gt;Rule&lt;/a&gt;</i>
    <a href="#tiledef" title="TileDef">TileDef</a>: <i>
      - &lt;a href=&#34;tiledef.md&#34;&gt;TileDef&lt;/a&gt;</i>
    <a href="#event" title="Event">Event</a>: <i>
      - &lt;a href=&#34;event.md&#34;&gt;Event&lt;/a&gt;</i>
    <a href="#marker" title="Marker">Marker</a>: <i>
      - &lt;a href=&#34;marker.md&#34;&gt;Marker&lt;/a&gt;</i>
    <a href="#request" title="Request">Request</a>: <i>
      - &lt;a href=&#34;request.md&#34;&gt;Request&lt;/a&gt;</i>
    <a href="#apmquery" title="ApmQuery">ApmQuery</a>: <i>
      - &lt;a href=&#34;apmquery.md&#34;&gt;ApmQuery&lt;/a&gt;</i>
    <a href="#conditionalformat" title="ConditionalFormat">ConditionalFormat</a>: <i>
      - &lt;a href=&#34;conditionalformat.md&#34;&gt;ConditionalFormat&lt;/a&gt;</i>
    <a href="#logquery" title="LogQuery">LogQuery</a>: <i>
      - &lt;a href=&#34;logquery.md&#34;&gt;LogQuery&lt;/a&gt;</i>
    <a href="#processquery" title="ProcessQuery">ProcessQuery</a>: <i>
      - &lt;a href=&#34;processquery.md&#34;&gt;ProcessQuery&lt;/a&gt;</i>
    <a href="#compute" title="Compute">Compute</a>: <i>
      - &lt;a href=&#34;compute.md&#34;&gt;Compute&lt;/a&gt;</i>
    <a href="#groupby" title="GroupBy">GroupBy</a>: <i>
      - &lt;a href=&#34;groupby.md&#34;&gt;GroupBy&lt;/a&gt;</i>
    <a href="#search" title="Search">Search</a>: <i>
      - &lt;a href=&#34;search.md&#34;&gt;Search&lt;/a&gt;</i>
    <a href="#sort" title="Sort">Sort</a>: <i>
      - &lt;a href=&#34;sort.md&#34;&gt;Sort&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Height

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shared

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Width

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateVariable

_Required_: No

_Type_: List of &lt;a href=&#34;templatevariable.md&#34;&gt;TemplateVariable&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Widget

_Required_: No

_Type_: List of &lt;a href=&#34;widget.md&#34;&gt;Widget&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of &lt;a href=&#34;rule.md&#34;&gt;Rule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TileDef

_Required_: No

_Type_: List of &lt;a href=&#34;tiledef.md&#34;&gt;TileDef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Event

_Required_: No

_Type_: List of &lt;a href=&#34;event.md&#34;&gt;Event&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Marker

_Required_: No

_Type_: List of &lt;a href=&#34;marker.md&#34;&gt;Marker&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Request

_Required_: No

_Type_: List of &lt;a href=&#34;request.md&#34;&gt;Request&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApmQuery

_Required_: No

_Type_: List of &lt;a href=&#34;apmquery.md&#34;&gt;ApmQuery&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionalFormat

_Required_: No

_Type_: List of &lt;a href=&#34;conditionalformat.md&#34;&gt;ConditionalFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogQuery

_Required_: No

_Type_: List of &lt;a href=&#34;logquery.md&#34;&gt;LogQuery&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessQuery

_Required_: No

_Type_: List of &lt;a href=&#34;processquery.md&#34;&gt;ProcessQuery&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Compute

_Required_: No

_Type_: List of &lt;a href=&#34;compute.md&#34;&gt;Compute&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupBy

_Required_: No

_Type_: List of &lt;a href=&#34;groupby.md&#34;&gt;GroupBy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Search

_Required_: No

_Type_: List of &lt;a href=&#34;search.md&#34;&gt;Search&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sort

_Required_: No

_Type_: List of &lt;a href=&#34;sort.md&#34;&gt;Sort&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

