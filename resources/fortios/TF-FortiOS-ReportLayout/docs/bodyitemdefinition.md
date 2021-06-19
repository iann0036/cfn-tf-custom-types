# TF::FortiOS::ReportLayout BodyItemDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#chart" title="Chart">Chart</a>" : <i>String</i>,
    "<a href="#chartoptions" title="ChartOptions">ChartOptions</a>" : <i>String</i>,
    "<a href="#column" title="Column">Column</a>" : <i>Double</i>,
    "<a href="#content" title="Content">Content</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#drilldownitems" title="DrillDownItems">DrillDownItems</a>" : <i>String</i>,
    "<a href="#drilldowntypes" title="DrillDownTypes">DrillDownTypes</a>" : <i>String</i>,
    "<a href="#hide" title="Hide">Hide</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#imgsrc" title="ImgSrc">ImgSrc</a>" : <i>String</i>,
    "<a href="#listcomponent" title="ListComponent">ListComponent</a>" : <i>String</i>,
    "<a href="#misccomponent" title="MiscComponent">MiscComponent</a>" : <i>String</i>,
    "<a href="#style" title="Style">Style</a>" : <i>String</i>,
    "<a href="#tablecaptionstyle" title="TableCaptionStyle">TableCaptionStyle</a>" : <i>String</i>,
    "<a href="#tablecolumnwidths" title="TableColumnWidths">TableColumnWidths</a>" : <i>String</i>,
    "<a href="#tableevenrowstyle" title="TableEvenRowStyle">TableEvenRowStyle</a>" : <i>String</i>,
    "<a href="#tableheadstyle" title="TableHeadStyle">TableHeadStyle</a>" : <i>String</i>,
    "<a href="#tableoddrowstyle" title="TableOddRowStyle">TableOddRowStyle</a>" : <i>String</i>,
    "<a href="#textcomponent" title="TextComponent">TextComponent</a>" : <i>String</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#topn" title="TopN">TopN</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#list" title="List">List</a>" : <i>[ <a href="listdefinition.md">ListDefinition</a>, ... ]</i>,
    "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parametersdefinition.md">ParametersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#chart" title="Chart">Chart</a>: <i>String</i>
<a href="#chartoptions" title="ChartOptions">ChartOptions</a>: <i>String</i>
<a href="#column" title="Column">Column</a>: <i>Double</i>
<a href="#content" title="Content">Content</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#drilldownitems" title="DrillDownItems">DrillDownItems</a>: <i>String</i>
<a href="#drilldowntypes" title="DrillDownTypes">DrillDownTypes</a>: <i>String</i>
<a href="#hide" title="Hide">Hide</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#imgsrc" title="ImgSrc">ImgSrc</a>: <i>String</i>
<a href="#listcomponent" title="ListComponent">ListComponent</a>: <i>String</i>
<a href="#misccomponent" title="MiscComponent">MiscComponent</a>: <i>String</i>
<a href="#style" title="Style">Style</a>: <i>String</i>
<a href="#tablecaptionstyle" title="TableCaptionStyle">TableCaptionStyle</a>: <i>String</i>
<a href="#tablecolumnwidths" title="TableColumnWidths">TableColumnWidths</a>: <i>String</i>
<a href="#tableevenrowstyle" title="TableEvenRowStyle">TableEvenRowStyle</a>: <i>String</i>
<a href="#tableheadstyle" title="TableHeadStyle">TableHeadStyle</a>: <i>String</i>
<a href="#tableoddrowstyle" title="TableOddRowStyle">TableOddRowStyle</a>: <i>String</i>
<a href="#textcomponent" title="TextComponent">TextComponent</a>: <i>String</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#topn" title="TopN">TopN</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#list" title="List">List</a>: <i>
      - <a href="listdefinition.md">ListDefinition</a></i>
<a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parametersdefinition.md">ParametersDefinition</a></i>
</pre>

## Properties

#### Chart

Report item chart name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChartOptions

Report chart options. Valid values: `include-no-data`, `hide-title`, `show-caption`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Column

Report section column number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Content

Report item text content.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrillDownItems

Control how drill down charts are shown.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrillDownTypes

Control whether keys from the parent being combined or not.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hide

Enable/disable hide item in report. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Report item ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImgSrc

Report item image file name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListComponent

Report item list component. Valid values: `bullet`, `numbered`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MiscComponent

Report item miscellaneous component. Valid values: `hline`, `page-break`, `column-break`, `section-start`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Style

Report item style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableCaptionStyle

Table chart caption style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableColumnWidths

Report item table column widths.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableEvenRowStyle

Table chart even row style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableHeadStyle

Table chart head style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableOddRowStyle

Table chart odd row style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TextComponent

Report item text component. Valid values: `text`, `heading1`, `heading2`, `heading3`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

Report section title.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopN

Value of top.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Report item type. Valid values: `text`, `image`, `chart`, `misc`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### List

_Required_: No

_Type_: List of <a href="listdefinition.md">ListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: No

_Type_: List of <a href="parametersdefinition.md">ParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

