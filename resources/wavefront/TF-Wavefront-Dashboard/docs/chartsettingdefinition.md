# TF::Wavefront::Dashboard ChartSettingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autocolumntags" title="AutoColumnTags">AutoColumnTags</a>" : <i>Boolean</i>,
    "<a href="#columntags" title="ColumnTags">ColumnTags</a>" : <i>String</i>,
    "<a href="#customtags" title="CustomTags">CustomTags</a>" : <i>[ String, ... ]</i>,
    "<a href="#expecteddataspacing" title="ExpectedDataSpacing">ExpectedDataSpacing</a>" : <i>Double</i>,
    "<a href="#fixedlegenddisplaystats" title="FixedLegendDisplayStats">FixedLegendDisplayStats</a>" : <i>[ String, ... ]</i>,
    "<a href="#fixedlegendenabled" title="FixedLegendEnabled">FixedLegendEnabled</a>" : <i>Boolean</i>,
    "<a href="#fixedlegendfilterfield" title="FixedLegendFilterField">FixedLegendFilterField</a>" : <i>String</i>,
    "<a href="#fixedlegendfilterlimit" title="FixedLegendFilterLimit">FixedLegendFilterLimit</a>" : <i>Double</i>,
    "<a href="#fixedlegendfiltersort" title="FixedLegendFilterSort">FixedLegendFilterSort</a>" : <i>String</i>,
    "<a href="#fixedlegendhidelabel" title="FixedLegendHideLabel">FixedLegendHideLabel</a>" : <i>Boolean</i>,
    "<a href="#fixedlegendposition" title="FixedLegendPosition">FixedLegendPosition</a>" : <i>String</i>,
    "<a href="#fixedlegenduserawstats" title="FixedLegendUseRawStats">FixedLegendUseRawStats</a>" : <i>Boolean</i>,
    "<a href="#groupbysource" title="GroupBySource">GroupBySource</a>" : <i>Boolean</i>,
    "<a href="#invertdynamiclegendhovercontrol" title="InvertDynamicLegendHoverControl">InvertDynamicLegendHoverControl</a>" : <i>Boolean</i>,
    "<a href="#linetype" title="LineType">LineType</a>" : <i>String</i>,
    "<a href="#max" title="Max">Max</a>" : <i>Double</i>,
    "<a href="#min" title="Min">Min</a>" : <i>Double</i>,
    "<a href="#numtags" title="NumTags">NumTags</a>" : <i>Double</i>,
    "<a href="#plainmarkdowncontent" title="PlainMarkdownContent">PlainMarkdownContent</a>" : <i>String</i>,
    "<a href="#showhosts" title="ShowHosts">ShowHosts</a>" : <i>Boolean</i>,
    "<a href="#showlabels" title="ShowLabels">ShowLabels</a>" : <i>Boolean</i>,
    "<a href="#showrawvalues" title="ShowRawValues">ShowRawValues</a>" : <i>Boolean</i>,
    "<a href="#sortvaluesdescending" title="SortValuesDescending">SortValuesDescending</a>" : <i>Boolean</i>,
    "<a href="#sparklinedecimalprecision" title="SparklineDecimalPrecision">SparklineDecimalPrecision</a>" : <i>Double</i>,
    "<a href="#sparklinedisplaycolor" title="SparklineDisplayColor">SparklineDisplayColor</a>" : <i>String</i>,
    "<a href="#sparklinedisplayfontsize" title="SparklineDisplayFontSize">SparklineDisplayFontSize</a>" : <i>String</i>,
    "<a href="#sparklinedisplayhorizontalposition" title="SparklineDisplayHorizontalPosition">SparklineDisplayHorizontalPosition</a>" : <i>String</i>,
    "<a href="#sparklinedisplaypostfix" title="SparklineDisplayPostfix">SparklineDisplayPostfix</a>" : <i>String</i>,
    "<a href="#sparklinedisplayprefix" title="SparklineDisplayPrefix">SparklineDisplayPrefix</a>" : <i>String</i>,
    "<a href="#sparklinedisplayvaluetype" title="SparklineDisplayValueType">SparklineDisplayValueType</a>" : <i>String</i>,
    "<a href="#sparklinedisplayverticalposition" title="SparklineDisplayVerticalPosition">SparklineDisplayVerticalPosition</a>" : <i>String</i>,
    "<a href="#sparklinefillcolor" title="SparklineFillColor">SparklineFillColor</a>" : <i>String</i>,
    "<a href="#sparklinelinecolor" title="SparklineLineColor">SparklineLineColor</a>" : <i>String</i>,
    "<a href="#sparklinesize" title="SparklineSize">SparklineSize</a>" : <i>String</i>,
    "<a href="#sparklinevaluecolormapapplyto" title="SparklineValueColorMapApplyTo">SparklineValueColorMapApplyTo</a>" : <i>String</i>,
    "<a href="#sparklinevaluecolormapcolors" title="SparklineValueColorMapColors">SparklineValueColorMapColors</a>" : <i>[ String, ... ]</i>,
    "<a href="#sparklinevaluecolormapvalues" title="SparklineValueColorMapValues">SparklineValueColorMapValues</a>" : <i>[ Double, ... ]</i>,
    "<a href="#sparklinevaluecolormapvaluesv2" title="SparklineValueColorMapValuesV2">SparklineValueColorMapValuesV2</a>" : <i>[ Double, ... ]</i>,
    "<a href="#sparklinevaluetextmaptext" title="SparklineValueTextMapText">SparklineValueTextMapText</a>" : <i>[ String, ... ]</i>,
    "<a href="#sparklinevaluetextmapthresholds" title="SparklineValueTextMapThresholds">SparklineValueTextMapThresholds</a>" : <i>[ Double, ... ]</i>,
    "<a href="#stacktype" title="StackType">StackType</a>" : <i>String</i>,
    "<a href="#tagmode" title="TagMode">TagMode</a>" : <i>String</i>,
    "<a href="#timebasedcoloring" title="TimeBasedColoring">TimeBasedColoring</a>" : <i>Boolean</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#windowsize" title="WindowSize">WindowSize</a>" : <i>Double</i>,
    "<a href="#windowing" title="Windowing">Windowing</a>" : <i>String</i>,
    "<a href="#xmax" title="Xmax">Xmax</a>" : <i>Double</i>,
    "<a href="#xmin" title="Xmin">Xmin</a>" : <i>Double</i>,
    "<a href="#y0scalesiby1024" title="Y0ScaleSiBy1024">Y0ScaleSiBy1024</a>" : <i>Boolean</i>,
    "<a href="#y0unitautoscaling" title="Y0UnitAutoscaling">Y0UnitAutoscaling</a>" : <i>Boolean</i>,
    "<a href="#y1scalesiby1024" title="Y1ScaleSiBy1024">Y1ScaleSiBy1024</a>" : <i>Boolean</i>,
    "<a href="#y1unitautoscaling" title="Y1UnitAutoscaling">Y1UnitAutoscaling</a>" : <i>Boolean</i>,
    "<a href="#y1units" title="Y1Units">Y1Units</a>" : <i>String</i>,
    "<a href="#y1max" title="Y1max">Y1max</a>" : <i>Double</i>,
    "<a href="#y1min" title="Y1min">Y1min</a>" : <i>Double</i>,
    "<a href="#ymax" title="Ymax">Ymax</a>" : <i>Double</i>,
    "<a href="#ymin" title="Ymin">Ymin</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#autocolumntags" title="AutoColumnTags">AutoColumnTags</a>: <i>Boolean</i>
<a href="#columntags" title="ColumnTags">ColumnTags</a>: <i>String</i>
<a href="#customtags" title="CustomTags">CustomTags</a>: <i>
      - String</i>
<a href="#expecteddataspacing" title="ExpectedDataSpacing">ExpectedDataSpacing</a>: <i>Double</i>
<a href="#fixedlegenddisplaystats" title="FixedLegendDisplayStats">FixedLegendDisplayStats</a>: <i>
      - String</i>
<a href="#fixedlegendenabled" title="FixedLegendEnabled">FixedLegendEnabled</a>: <i>Boolean</i>
<a href="#fixedlegendfilterfield" title="FixedLegendFilterField">FixedLegendFilterField</a>: <i>String</i>
<a href="#fixedlegendfilterlimit" title="FixedLegendFilterLimit">FixedLegendFilterLimit</a>: <i>Double</i>
<a href="#fixedlegendfiltersort" title="FixedLegendFilterSort">FixedLegendFilterSort</a>: <i>String</i>
<a href="#fixedlegendhidelabel" title="FixedLegendHideLabel">FixedLegendHideLabel</a>: <i>Boolean</i>
<a href="#fixedlegendposition" title="FixedLegendPosition">FixedLegendPosition</a>: <i>String</i>
<a href="#fixedlegenduserawstats" title="FixedLegendUseRawStats">FixedLegendUseRawStats</a>: <i>Boolean</i>
<a href="#groupbysource" title="GroupBySource">GroupBySource</a>: <i>Boolean</i>
<a href="#invertdynamiclegendhovercontrol" title="InvertDynamicLegendHoverControl">InvertDynamicLegendHoverControl</a>: <i>Boolean</i>
<a href="#linetype" title="LineType">LineType</a>: <i>String</i>
<a href="#max" title="Max">Max</a>: <i>Double</i>
<a href="#min" title="Min">Min</a>: <i>Double</i>
<a href="#numtags" title="NumTags">NumTags</a>: <i>Double</i>
<a href="#plainmarkdowncontent" title="PlainMarkdownContent">PlainMarkdownContent</a>: <i>String</i>
<a href="#showhosts" title="ShowHosts">ShowHosts</a>: <i>Boolean</i>
<a href="#showlabels" title="ShowLabels">ShowLabels</a>: <i>Boolean</i>
<a href="#showrawvalues" title="ShowRawValues">ShowRawValues</a>: <i>Boolean</i>
<a href="#sortvaluesdescending" title="SortValuesDescending">SortValuesDescending</a>: <i>Boolean</i>
<a href="#sparklinedecimalprecision" title="SparklineDecimalPrecision">SparklineDecimalPrecision</a>: <i>Double</i>
<a href="#sparklinedisplaycolor" title="SparklineDisplayColor">SparklineDisplayColor</a>: <i>String</i>
<a href="#sparklinedisplayfontsize" title="SparklineDisplayFontSize">SparklineDisplayFontSize</a>: <i>String</i>
<a href="#sparklinedisplayhorizontalposition" title="SparklineDisplayHorizontalPosition">SparklineDisplayHorizontalPosition</a>: <i>String</i>
<a href="#sparklinedisplaypostfix" title="SparklineDisplayPostfix">SparklineDisplayPostfix</a>: <i>String</i>
<a href="#sparklinedisplayprefix" title="SparklineDisplayPrefix">SparklineDisplayPrefix</a>: <i>String</i>
<a href="#sparklinedisplayvaluetype" title="SparklineDisplayValueType">SparklineDisplayValueType</a>: <i>String</i>
<a href="#sparklinedisplayverticalposition" title="SparklineDisplayVerticalPosition">SparklineDisplayVerticalPosition</a>: <i>String</i>
<a href="#sparklinefillcolor" title="SparklineFillColor">SparklineFillColor</a>: <i>String</i>
<a href="#sparklinelinecolor" title="SparklineLineColor">SparklineLineColor</a>: <i>String</i>
<a href="#sparklinesize" title="SparklineSize">SparklineSize</a>: <i>String</i>
<a href="#sparklinevaluecolormapapplyto" title="SparklineValueColorMapApplyTo">SparklineValueColorMapApplyTo</a>: <i>String</i>
<a href="#sparklinevaluecolormapcolors" title="SparklineValueColorMapColors">SparklineValueColorMapColors</a>: <i>
      - String</i>
<a href="#sparklinevaluecolormapvalues" title="SparklineValueColorMapValues">SparklineValueColorMapValues</a>: <i>
      - Double</i>
<a href="#sparklinevaluecolormapvaluesv2" title="SparklineValueColorMapValuesV2">SparklineValueColorMapValuesV2</a>: <i>
      - Double</i>
<a href="#sparklinevaluetextmaptext" title="SparklineValueTextMapText">SparklineValueTextMapText</a>: <i>
      - String</i>
<a href="#sparklinevaluetextmapthresholds" title="SparklineValueTextMapThresholds">SparklineValueTextMapThresholds</a>: <i>
      - Double</i>
<a href="#stacktype" title="StackType">StackType</a>: <i>String</i>
<a href="#tagmode" title="TagMode">TagMode</a>: <i>String</i>
<a href="#timebasedcoloring" title="TimeBasedColoring">TimeBasedColoring</a>: <i>Boolean</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#windowsize" title="WindowSize">WindowSize</a>: <i>Double</i>
<a href="#windowing" title="Windowing">Windowing</a>: <i>String</i>
<a href="#xmax" title="Xmax">Xmax</a>: <i>Double</i>
<a href="#xmin" title="Xmin">Xmin</a>: <i>Double</i>
<a href="#y0scalesiby1024" title="Y0ScaleSiBy1024">Y0ScaleSiBy1024</a>: <i>Boolean</i>
<a href="#y0unitautoscaling" title="Y0UnitAutoscaling">Y0UnitAutoscaling</a>: <i>Boolean</i>
<a href="#y1scalesiby1024" title="Y1ScaleSiBy1024">Y1ScaleSiBy1024</a>: <i>Boolean</i>
<a href="#y1unitautoscaling" title="Y1UnitAutoscaling">Y1UnitAutoscaling</a>: <i>Boolean</i>
<a href="#y1units" title="Y1Units">Y1Units</a>: <i>String</i>
<a href="#y1max" title="Y1max">Y1max</a>: <i>Double</i>
<a href="#y1min" title="Y1min">Y1min</a>: <i>Double</i>
<a href="#ymax" title="Ymax">Ymax</a>: <i>Double</i>
<a href="#ymin" title="Ymin">Ymin</a>: <i>Double</i>
</pre>

## Properties

#### AutoColumnTags

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColumnTags

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomTags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpectedDataSpacing

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedLegendDisplayStats

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedLegendEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedLegendFilterField

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedLegendFilterLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedLegendFilterSort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedLegendHideLabel

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedLegendPosition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedLegendUseRawStats

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupBySource

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InvertDynamicLegendHoverControl

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LineType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Max

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Min

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumTags

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlainMarkdownContent

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowHosts

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowLabels

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowRawValues

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SortValuesDescending

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparklineDecimalPrecision

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparklineDisplayColor

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparklineDisplayFontSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparklineDisplayHorizontalPosition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparklineDisplayPostfix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparklineDisplayPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparklineDisplayValueType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparklineDisplayVerticalPosition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparklineFillColor

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparklineLineColor

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparklineSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparklineValueColorMapApplyTo

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparklineValueColorMapColors

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparklineValueColorMapValues

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparklineValueColorMapValuesV2

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparklineValueTextMapText

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparklineValueTextMapThresholds

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeBasedColoring

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Windowing

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Xmax

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Xmin

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Y0ScaleSiBy1024

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Y0UnitAutoscaling

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Y1ScaleSiBy1024

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Y1UnitAutoscaling

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Y1Units

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Y1max

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Y1min

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ymax

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ymin

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

