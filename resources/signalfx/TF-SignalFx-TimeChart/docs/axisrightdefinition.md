# TF::SignalFx::TimeChart AxisRightDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#highwatermark" title="HighWatermark">HighWatermark</a>" : <i>Double</i>,
    "<a href="#highwatermarklabel" title="HighWatermarkLabel">HighWatermarkLabel</a>" : <i>String</i>,
    "<a href="#label" title="Label">Label</a>" : <i>String</i>,
    "<a href="#lowwatermark" title="LowWatermark">LowWatermark</a>" : <i>Double</i>,
    "<a href="#lowwatermarklabel" title="LowWatermarkLabel">LowWatermarkLabel</a>" : <i>String</i>,
    "<a href="#maxvalue" title="MaxValue">MaxValue</a>" : <i>Double</i>,
    "<a href="#minvalue" title="MinValue">MinValue</a>" : <i>Double</i>,
    "<a href="#watermarks" title="Watermarks">Watermarks</a>" : <i>[ <a href="watermarksdefinition.md">WatermarksDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#highwatermark" title="HighWatermark">HighWatermark</a>: <i>Double</i>
<a href="#highwatermarklabel" title="HighWatermarkLabel">HighWatermarkLabel</a>: <i>String</i>
<a href="#label" title="Label">Label</a>: <i>String</i>
<a href="#lowwatermark" title="LowWatermark">LowWatermark</a>: <i>Double</i>
<a href="#lowwatermarklabel" title="LowWatermarkLabel">LowWatermarkLabel</a>: <i>String</i>
<a href="#maxvalue" title="MaxValue">MaxValue</a>: <i>Double</i>
<a href="#minvalue" title="MinValue">MinValue</a>: <i>Double</i>
<a href="#watermarks" title="Watermarks">Watermarks</a>: <i>
      - <a href="watermarksdefinition.md">WatermarksDefinition</a></i>
</pre>

## Properties

#### HighWatermark

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HighWatermarkLabel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LowWatermark

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LowWatermarkLabel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxValue

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinValue

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Watermarks

_Required_: No

_Type_: List of <a href="watermarksdefinition.md">WatermarksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

