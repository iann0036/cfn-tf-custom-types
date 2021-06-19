# TF::NewRelic::OneDashboard PageDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#widgetarea" title="WidgetArea">WidgetArea</a>" : <i>[ <a href="widgetareadefinition.md">WidgetAreaDefinition</a>, ... ]</i>,
    "<a href="#widgetbar" title="WidgetBar">WidgetBar</a>" : <i>[ <a href="widgetbardefinition.md">WidgetBarDefinition</a>, ... ]</i>,
    "<a href="#widgetbillboard" title="WidgetBillboard">WidgetBillboard</a>" : <i>[ <a href="widgetbillboarddefinition.md">WidgetBillboardDefinition</a>, ... ]</i>,
    "<a href="#widgetbullet" title="WidgetBullet">WidgetBullet</a>" : <i>[ <a href="widgetbulletdefinition.md">WidgetBulletDefinition</a>, ... ]</i>,
    "<a href="#widgetfunnel" title="WidgetFunnel">WidgetFunnel</a>" : <i>[ <a href="widgetfunneldefinition.md">WidgetFunnelDefinition</a>, ... ]</i>,
    "<a href="#widgetheatmap" title="WidgetHeatmap">WidgetHeatmap</a>" : <i>[ <a href="widgetheatmapdefinition.md">WidgetHeatmapDefinition</a>, ... ]</i>,
    "<a href="#widgethistogram" title="WidgetHistogram">WidgetHistogram</a>" : <i>[ <a href="widgethistogramdefinition.md">WidgetHistogramDefinition</a>, ... ]</i>,
    "<a href="#widgetjson" title="WidgetJson">WidgetJson</a>" : <i>[ <a href="widgetjsondefinition.md">WidgetJsonDefinition</a>, ... ]</i>,
    "<a href="#widgetline" title="WidgetLine">WidgetLine</a>" : <i>[ <a href="widgetlinedefinition.md">WidgetLineDefinition</a>, ... ]</i>,
    "<a href="#widgetmarkdown" title="WidgetMarkdown">WidgetMarkdown</a>" : <i>[ <a href="widgetmarkdowndefinition.md">WidgetMarkdownDefinition</a>, ... ]</i>,
    "<a href="#widgetpie" title="WidgetPie">WidgetPie</a>" : <i>[ <a href="widgetpiedefinition.md">WidgetPieDefinition</a>, ... ]</i>,
    "<a href="#widgettable" title="WidgetTable">WidgetTable</a>" : <i>[ <a href="widgettabledefinition.md">WidgetTableDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#widgetarea" title="WidgetArea">WidgetArea</a>: <i>
      - <a href="widgetareadefinition.md">WidgetAreaDefinition</a></i>
<a href="#widgetbar" title="WidgetBar">WidgetBar</a>: <i>
      - <a href="widgetbardefinition.md">WidgetBarDefinition</a></i>
<a href="#widgetbillboard" title="WidgetBillboard">WidgetBillboard</a>: <i>
      - <a href="widgetbillboarddefinition.md">WidgetBillboardDefinition</a></i>
<a href="#widgetbullet" title="WidgetBullet">WidgetBullet</a>: <i>
      - <a href="widgetbulletdefinition.md">WidgetBulletDefinition</a></i>
<a href="#widgetfunnel" title="WidgetFunnel">WidgetFunnel</a>: <i>
      - <a href="widgetfunneldefinition.md">WidgetFunnelDefinition</a></i>
<a href="#widgetheatmap" title="WidgetHeatmap">WidgetHeatmap</a>: <i>
      - <a href="widgetheatmapdefinition.md">WidgetHeatmapDefinition</a></i>
<a href="#widgethistogram" title="WidgetHistogram">WidgetHistogram</a>: <i>
      - <a href="widgethistogramdefinition.md">WidgetHistogramDefinition</a></i>
<a href="#widgetjson" title="WidgetJson">WidgetJson</a>: <i>
      - <a href="widgetjsondefinition.md">WidgetJsonDefinition</a></i>
<a href="#widgetline" title="WidgetLine">WidgetLine</a>: <i>
      - <a href="widgetlinedefinition.md">WidgetLineDefinition</a></i>
<a href="#widgetmarkdown" title="WidgetMarkdown">WidgetMarkdown</a>: <i>
      - <a href="widgetmarkdowndefinition.md">WidgetMarkdownDefinition</a></i>
<a href="#widgetpie" title="WidgetPie">WidgetPie</a>: <i>
      - <a href="widgetpiedefinition.md">WidgetPieDefinition</a></i>
<a href="#widgettable" title="WidgetTable">WidgetTable</a>: <i>
      - <a href="widgettabledefinition.md">WidgetTableDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidgetArea

_Required_: No

_Type_: List of <a href="widgetareadefinition.md">WidgetAreaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidgetBar

_Required_: No

_Type_: List of <a href="widgetbardefinition.md">WidgetBarDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidgetBillboard

_Required_: No

_Type_: List of <a href="widgetbillboarddefinition.md">WidgetBillboardDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidgetBullet

_Required_: No

_Type_: List of <a href="widgetbulletdefinition.md">WidgetBulletDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidgetFunnel

_Required_: No

_Type_: List of <a href="widgetfunneldefinition.md">WidgetFunnelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidgetHeatmap

_Required_: No

_Type_: List of <a href="widgetheatmapdefinition.md">WidgetHeatmapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidgetHistogram

_Required_: No

_Type_: List of <a href="widgethistogramdefinition.md">WidgetHistogramDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidgetJson

_Required_: No

_Type_: List of <a href="widgetjsondefinition.md">WidgetJsonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidgetLine

_Required_: No

_Type_: List of <a href="widgetlinedefinition.md">WidgetLineDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidgetMarkdown

_Required_: No

_Type_: List of <a href="widgetmarkdowndefinition.md">WidgetMarkdownDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidgetPie

_Required_: No

_Type_: List of <a href="widgetpiedefinition.md">WidgetPieDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidgetTable

_Required_: No

_Type_: List of <a href="widgettabledefinition.md">WidgetTableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

