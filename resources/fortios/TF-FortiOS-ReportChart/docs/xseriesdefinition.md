# TF::FortiOS::ReportChart XSeriesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#caption" title="Caption">Caption</a>" : <i>String</i>,
    "<a href="#captionfontsize" title="CaptionFontSize">CaptionFontSize</a>" : <i>Double</i>,
    "<a href="#databind" title="Databind">Databind</a>" : <i>String</i>,
    "<a href="#fontsize" title="FontSize">FontSize</a>" : <i>Double</i>,
    "<a href="#iscategory" title="IsCategory">IsCategory</a>" : <i>String</i>,
    "<a href="#labelangle" title="LabelAngle">LabelAngle</a>" : <i>String</i>,
    "<a href="#scaledirection" title="ScaleDirection">ScaleDirection</a>" : <i>String</i>,
    "<a href="#scaleformat" title="ScaleFormat">ScaleFormat</a>" : <i>String</i>,
    "<a href="#scalestep" title="ScaleStep">ScaleStep</a>" : <i>Double</i>,
    "<a href="#scaleunit" title="ScaleUnit">ScaleUnit</a>" : <i>String</i>,
    "<a href="#unit" title="Unit">Unit</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#caption" title="Caption">Caption</a>: <i>String</i>
<a href="#captionfontsize" title="CaptionFontSize">CaptionFontSize</a>: <i>Double</i>
<a href="#databind" title="Databind">Databind</a>: <i>String</i>
<a href="#fontsize" title="FontSize">FontSize</a>: <i>Double</i>
<a href="#iscategory" title="IsCategory">IsCategory</a>: <i>String</i>
<a href="#labelangle" title="LabelAngle">LabelAngle</a>: <i>String</i>
<a href="#scaledirection" title="ScaleDirection">ScaleDirection</a>: <i>String</i>
<a href="#scaleformat" title="ScaleFormat">ScaleFormat</a>: <i>String</i>
<a href="#scalestep" title="ScaleStep">ScaleStep</a>: <i>Double</i>
<a href="#scaleunit" title="ScaleUnit">ScaleUnit</a>: <i>String</i>
<a href="#unit" title="Unit">Unit</a>: <i>String</i>
</pre>

## Properties

#### Caption

X-series caption.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptionFontSize

X-series caption font size.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Databind

X-series value expression.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FontSize

X-series label font size.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsCategory

X-series represent category or not. Valid values: `yes`, `no`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LabelAngle

X-series label angle. Valid values: `45-degree`, `vertical`, `horizontal`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleDirection

Scale increase or decrease. Valid values: `decrease`, `increase`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleFormat

Date/time format. Valid values: `YYYY-MM-DD-HH-MM`, `YYYY-MM-DD HH`, `YYYY-MM-DD`, `YYYY-MM`, `YYYY`, `HH-MM`, `MM-DD`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleStep

Scale step.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleUnit

Scale unit. Valid values: `minute`, `hour`, `day`, `month`, `year`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unit

X-series unit.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

