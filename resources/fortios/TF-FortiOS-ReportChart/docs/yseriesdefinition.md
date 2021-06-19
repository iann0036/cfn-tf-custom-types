# TF::FortiOS::ReportChart YSeriesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#caption" title="Caption">Caption</a>" : <i>String</i>,
    "<a href="#captionfontsize" title="CaptionFontSize">CaptionFontSize</a>" : <i>Double</i>,
    "<a href="#databind" title="Databind">Databind</a>" : <i>String</i>,
    "<a href="#extradatabind" title="ExtraDatabind">ExtraDatabind</a>" : <i>String</i>,
    "<a href="#extray" title="ExtraY">ExtraY</a>" : <i>String</i>,
    "<a href="#extraylegend" title="ExtraYLegend">ExtraYLegend</a>" : <i>String</i>,
    "<a href="#fontsize" title="FontSize">FontSize</a>" : <i>Double</i>,
    "<a href="#group" title="Group">Group</a>" : <i>String</i>,
    "<a href="#labelangle" title="LabelAngle">LabelAngle</a>" : <i>String</i>,
    "<a href="#unit" title="Unit">Unit</a>" : <i>String</i>,
    "<a href="#ylegend" title="YLegend">YLegend</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#caption" title="Caption">Caption</a>: <i>String</i>
<a href="#captionfontsize" title="CaptionFontSize">CaptionFontSize</a>: <i>Double</i>
<a href="#databind" title="Databind">Databind</a>: <i>String</i>
<a href="#extradatabind" title="ExtraDatabind">ExtraDatabind</a>: <i>String</i>
<a href="#extray" title="ExtraY">ExtraY</a>: <i>String</i>
<a href="#extraylegend" title="ExtraYLegend">ExtraYLegend</a>: <i>String</i>
<a href="#fontsize" title="FontSize">FontSize</a>: <i>Double</i>
<a href="#group" title="Group">Group</a>: <i>String</i>
<a href="#labelangle" title="LabelAngle">LabelAngle</a>: <i>String</i>
<a href="#unit" title="Unit">Unit</a>: <i>String</i>
<a href="#ylegend" title="YLegend">YLegend</a>: <i>String</i>
</pre>

## Properties

#### Caption

Y-series caption.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptionFontSize

Y-series caption font size.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Databind

Y-series value expression.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraDatabind

Extra Y-series value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraY

Allow another Y-series value Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraYLegend

Extra Y-series legend type/name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FontSize

Y-series label font size.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

Y-series group option.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LabelAngle

Y-series label angle. Valid values: `45-degree`, `vertical`, `horizontal`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unit

Y-series unit.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### YLegend

First Y-series legend type/name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

