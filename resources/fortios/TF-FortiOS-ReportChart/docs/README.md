# TF::FortiOS::ReportChart

Report chart widget configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::ReportChart",
    "Properties" : {
        "<a href="#background" title="Background">Background</a>" : <i>String</i>,
        "<a href="#category" title="Category">Category</a>" : <i>String</i>,
        "<a href="#colorpalette" title="ColorPalette">ColorPalette</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#dataset" title="Dataset">Dataset</a>" : <i>String</i>,
        "<a href="#dimension" title="Dimension">Dimension</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#favorite" title="Favorite">Favorite</a>" : <i>String</i>,
        "<a href="#graphtype" title="GraphType">GraphType</a>" : <i>String</i>,
        "<a href="#legend" title="Legend">Legend</a>" : <i>String</i>,
        "<a href="#legendfontsize" title="LegendFontSize">LegendFontSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>Double</i>,
        "<a href="#style" title="Style">Style</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#titlefontsize" title="TitleFontSize">TitleFontSize</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#categoryseries" title="CategorySeries">CategorySeries</a>" : <i>[ <a href="categoryseriesdefinition.md">CategorySeriesDefinition</a>, ... ]</i>,
        "<a href="#column" title="Column">Column</a>" : <i>[ <a href="columndefinition.md">ColumnDefinition</a>, ... ]</i>,
        "<a href="#drilldowncharts" title="DrillDownCharts">DrillDownCharts</a>" : <i>[ <a href="drilldownchartsdefinition.md">DrillDownChartsDefinition</a>, ... ]</i>,
        "<a href="#valueseries" title="ValueSeries">ValueSeries</a>" : <i>[ <a href="valueseriesdefinition.md">ValueSeriesDefinition</a>, ... ]</i>,
        "<a href="#xseries" title="XSeries">XSeries</a>" : <i>[ <a href="xseriesdefinition.md">XSeriesDefinition</a>, ... ]</i>,
        "<a href="#yseries" title="YSeries">YSeries</a>" : <i>[ <a href="yseriesdefinition.md">YSeriesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::ReportChart
Properties:
    <a href="#background" title="Background">Background</a>: <i>String</i>
    <a href="#category" title="Category">Category</a>: <i>String</i>
    <a href="#colorpalette" title="ColorPalette">ColorPalette</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#dataset" title="Dataset">Dataset</a>: <i>String</i>
    <a href="#dimension" title="Dimension">Dimension</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#favorite" title="Favorite">Favorite</a>: <i>String</i>
    <a href="#graphtype" title="GraphType">GraphType</a>: <i>String</i>
    <a href="#legend" title="Legend">Legend</a>: <i>String</i>
    <a href="#legendfontsize" title="LegendFontSize">LegendFontSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>Double</i>
    <a href="#style" title="Style">Style</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#titlefontsize" title="TitleFontSize">TitleFontSize</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#categoryseries" title="CategorySeries">CategorySeries</a>: <i>
      - <a href="categoryseriesdefinition.md">CategorySeriesDefinition</a></i>
    <a href="#column" title="Column">Column</a>: <i>
      - <a href="columndefinition.md">ColumnDefinition</a></i>
    <a href="#drilldowncharts" title="DrillDownCharts">DrillDownCharts</a>: <i>
      - <a href="drilldownchartsdefinition.md">DrillDownChartsDefinition</a></i>
    <a href="#valueseries" title="ValueSeries">ValueSeries</a>: <i>
      - <a href="valueseriesdefinition.md">ValueSeriesDefinition</a></i>
    <a href="#xseries" title="XSeries">XSeries</a>: <i>
      - <a href="xseriesdefinition.md">XSeriesDefinition</a></i>
    <a href="#yseries" title="YSeries">YSeries</a>: <i>
      - <a href="yseriesdefinition.md">YSeriesDefinition</a></i>
</pre>

## Properties

#### Background

Chart background.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Category

Category. Valid values: `misc`, `traffic`, `event`, `virus`, `webfilter`, `attack`, `spam`, `dlp`, `app-ctrl`, `vulnerability`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColorPalette

Color palette (system will pick color automatically by default).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dataset

Bind dataset to chart.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimension

Dimension. Valid values: `2D`, `3D`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Favorite

Favorite. Valid values: `no`, `yes`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GraphType

Graph type. Valid values: `none`, `bar`, `pie`, `line`, `flow`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Legend

Enable/Disable Legend area. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LegendFontSize

Font size of legend area.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Chart Widget Name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

Time period. Valid values: `last24h`, `last7d`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

Used by monitor policy.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Style

Style. Valid values: `auto`, `manual`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

Chart title.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TitleFontSize

Font size of chart title.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Chart type. Valid values: `graph`, `table`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CategorySeries

_Required_: No

_Type_: List of <a href="categoryseriesdefinition.md">CategorySeriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Column

_Required_: No

_Type_: List of <a href="columndefinition.md">ColumnDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrillDownCharts

_Required_: No

_Type_: List of <a href="drilldownchartsdefinition.md">DrillDownChartsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueSeries

_Required_: No

_Type_: List of <a href="valueseriesdefinition.md">ValueSeriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XSeries

_Required_: No

_Type_: List of <a href="xseriesdefinition.md">XSeriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### YSeries

_Required_: No

_Type_: List of <a href="yseriesdefinition.md">YSeriesDefinition</a>

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

