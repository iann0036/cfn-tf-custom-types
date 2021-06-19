# TF::FortiOS::ReportTheme

Report themes configuration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::ReportTheme",
    "Properties" : {
        "<a href="#bulletliststyle" title="BulletListStyle">BulletListStyle</a>" : <i>String</i>,
        "<a href="#columncount" title="ColumnCount">ColumnCount</a>" : <i>String</i>,
        "<a href="#defaulthtmlstyle" title="DefaultHtmlStyle">DefaultHtmlStyle</a>" : <i>String</i>,
        "<a href="#defaultpdfstyle" title="DefaultPdfStyle">DefaultPdfStyle</a>" : <i>String</i>,
        "<a href="#graphchartstyle" title="GraphChartStyle">GraphChartStyle</a>" : <i>String</i>,
        "<a href="#heading1style" title="Heading1Style">Heading1Style</a>" : <i>String</i>,
        "<a href="#heading2style" title="Heading2Style">Heading2Style</a>" : <i>String</i>,
        "<a href="#heading3style" title="Heading3Style">Heading3Style</a>" : <i>String</i>,
        "<a href="#heading4style" title="Heading4Style">Heading4Style</a>" : <i>String</i>,
        "<a href="#hlinestyle" title="HlineStyle">HlineStyle</a>" : <i>String</i>,
        "<a href="#imagestyle" title="ImageStyle">ImageStyle</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#normaltextstyle" title="NormalTextStyle">NormalTextStyle</a>" : <i>String</i>,
        "<a href="#numberedliststyle" title="NumberedListStyle">NumberedListStyle</a>" : <i>String</i>,
        "<a href="#pagefooterstyle" title="PageFooterStyle">PageFooterStyle</a>" : <i>String</i>,
        "<a href="#pageheaderstyle" title="PageHeaderStyle">PageHeaderStyle</a>" : <i>String</i>,
        "<a href="#pageorient" title="PageOrient">PageOrient</a>" : <i>String</i>,
        "<a href="#pagestyle" title="PageStyle">PageStyle</a>" : <i>String</i>,
        "<a href="#reportsubtitlestyle" title="ReportSubtitleStyle">ReportSubtitleStyle</a>" : <i>String</i>,
        "<a href="#reporttitlestyle" title="ReportTitleStyle">ReportTitleStyle</a>" : <i>String</i>,
        "<a href="#tablechartcaptionstyle" title="TableChartCaptionStyle">TableChartCaptionStyle</a>" : <i>String</i>,
        "<a href="#tablechartevenrowstyle" title="TableChartEvenRowStyle">TableChartEvenRowStyle</a>" : <i>String</i>,
        "<a href="#tablechartheadstyle" title="TableChartHeadStyle">TableChartHeadStyle</a>" : <i>String</i>,
        "<a href="#tablechartoddrowstyle" title="TableChartOddRowStyle">TableChartOddRowStyle</a>" : <i>String</i>,
        "<a href="#tablechartstyle" title="TableChartStyle">TableChartStyle</a>" : <i>String</i>,
        "<a href="#tocheading1style" title="TocHeading1Style">TocHeading1Style</a>" : <i>String</i>,
        "<a href="#tocheading2style" title="TocHeading2Style">TocHeading2Style</a>" : <i>String</i>,
        "<a href="#tocheading3style" title="TocHeading3Style">TocHeading3Style</a>" : <i>String</i>,
        "<a href="#tocheading4style" title="TocHeading4Style">TocHeading4Style</a>" : <i>String</i>,
        "<a href="#toctitlestyle" title="TocTitleStyle">TocTitleStyle</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::ReportTheme
Properties:
    <a href="#bulletliststyle" title="BulletListStyle">BulletListStyle</a>: <i>String</i>
    <a href="#columncount" title="ColumnCount">ColumnCount</a>: <i>String</i>
    <a href="#defaulthtmlstyle" title="DefaultHtmlStyle">DefaultHtmlStyle</a>: <i>String</i>
    <a href="#defaultpdfstyle" title="DefaultPdfStyle">DefaultPdfStyle</a>: <i>String</i>
    <a href="#graphchartstyle" title="GraphChartStyle">GraphChartStyle</a>: <i>String</i>
    <a href="#heading1style" title="Heading1Style">Heading1Style</a>: <i>String</i>
    <a href="#heading2style" title="Heading2Style">Heading2Style</a>: <i>String</i>
    <a href="#heading3style" title="Heading3Style">Heading3Style</a>: <i>String</i>
    <a href="#heading4style" title="Heading4Style">Heading4Style</a>: <i>String</i>
    <a href="#hlinestyle" title="HlineStyle">HlineStyle</a>: <i>String</i>
    <a href="#imagestyle" title="ImageStyle">ImageStyle</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#normaltextstyle" title="NormalTextStyle">NormalTextStyle</a>: <i>String</i>
    <a href="#numberedliststyle" title="NumberedListStyle">NumberedListStyle</a>: <i>String</i>
    <a href="#pagefooterstyle" title="PageFooterStyle">PageFooterStyle</a>: <i>String</i>
    <a href="#pageheaderstyle" title="PageHeaderStyle">PageHeaderStyle</a>: <i>String</i>
    <a href="#pageorient" title="PageOrient">PageOrient</a>: <i>String</i>
    <a href="#pagestyle" title="PageStyle">PageStyle</a>: <i>String</i>
    <a href="#reportsubtitlestyle" title="ReportSubtitleStyle">ReportSubtitleStyle</a>: <i>String</i>
    <a href="#reporttitlestyle" title="ReportTitleStyle">ReportTitleStyle</a>: <i>String</i>
    <a href="#tablechartcaptionstyle" title="TableChartCaptionStyle">TableChartCaptionStyle</a>: <i>String</i>
    <a href="#tablechartevenrowstyle" title="TableChartEvenRowStyle">TableChartEvenRowStyle</a>: <i>String</i>
    <a href="#tablechartheadstyle" title="TableChartHeadStyle">TableChartHeadStyle</a>: <i>String</i>
    <a href="#tablechartoddrowstyle" title="TableChartOddRowStyle">TableChartOddRowStyle</a>: <i>String</i>
    <a href="#tablechartstyle" title="TableChartStyle">TableChartStyle</a>: <i>String</i>
    <a href="#tocheading1style" title="TocHeading1Style">TocHeading1Style</a>: <i>String</i>
    <a href="#tocheading2style" title="TocHeading2Style">TocHeading2Style</a>: <i>String</i>
    <a href="#tocheading3style" title="TocHeading3Style">TocHeading3Style</a>: <i>String</i>
    <a href="#tocheading4style" title="TocHeading4Style">TocHeading4Style</a>: <i>String</i>
    <a href="#toctitlestyle" title="TocTitleStyle">TocTitleStyle</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### BulletListStyle

Bullet list style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColumnCount

Report page column count. Valid values: `1`, `2`, `3`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultHtmlStyle

Default HTML report style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultPdfStyle

Default PDF report style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GraphChartStyle

Graph chart style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Heading1Style

Report heading style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Heading2Style

Report heading style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Heading3Style

Report heading style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Heading4Style

Report heading style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HlineStyle

Horizontal line style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageStyle

Image style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Report theme name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NormalTextStyle

Normal text style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberedListStyle

Numbered list style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PageFooterStyle

Report page footer style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PageHeaderStyle

Report page header style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PageOrient

Report page orientation. Valid values: `portrait`, `landscape`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PageStyle

Report page style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReportSubtitleStyle

Report subtitle style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReportTitleStyle

Report title style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableChartCaptionStyle

Table chart caption style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableChartEvenRowStyle

Table chart even row style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableChartHeadStyle

Table chart head row style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableChartOddRowStyle

Table chart odd row style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableChartStyle

Table chart style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TocHeading1Style

Table of contents heading style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TocHeading2Style

Table of contents heading style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TocHeading3Style

Table of contents heading style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TocHeading4Style

Table of contents heading style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TocTitleStyle

Table of contents title style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

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

