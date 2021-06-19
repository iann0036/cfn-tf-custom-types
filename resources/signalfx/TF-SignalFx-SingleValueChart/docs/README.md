# TF::SignalFx::SingleValueChart

This chart type displays a single number in a large font, representing the current value of a single metric on a plot line.

If the time period is in the past, the number represents the value of the metric near the end of the time period.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SignalFx::SingleValueChart",
    "Properties" : {
        "<a href="#colorby" title="ColorBy">ColorBy</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#istimestamphidden" title="IsTimestampHidden">IsTimestampHidden</a>" : <i>Boolean</i>,
        "<a href="#maxdelay" title="MaxDelay">MaxDelay</a>" : <i>Double</i>,
        "<a href="#maxprecision" title="MaxPrecision">MaxPrecision</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#programtext" title="ProgramText">ProgramText</a>" : <i>String</i>,
        "<a href="#refreshinterval" title="RefreshInterval">RefreshInterval</a>" : <i>Double</i>,
        "<a href="#secondaryvisualization" title="SecondaryVisualization">SecondaryVisualization</a>" : <i>String</i>,
        "<a href="#showsparkline" title="ShowSparkLine">ShowSparkLine</a>" : <i>Boolean</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#unitprefix" title="UnitPrefix">UnitPrefix</a>" : <i>String</i>,
        "<a href="#colorscale" title="ColorScale">ColorScale</a>" : <i>[ <a href="colorscaledefinition.md">ColorScaleDefinition</a>, ... ]</i>,
        "<a href="#vizoptions" title="VizOptions">VizOptions</a>" : <i>[ <a href="vizoptionsdefinition.md">VizOptionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SignalFx::SingleValueChart
Properties:
    <a href="#colorby" title="ColorBy">ColorBy</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#istimestamphidden" title="IsTimestampHidden">IsTimestampHidden</a>: <i>Boolean</i>
    <a href="#maxdelay" title="MaxDelay">MaxDelay</a>: <i>Double</i>
    <a href="#maxprecision" title="MaxPrecision">MaxPrecision</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#programtext" title="ProgramText">ProgramText</a>: <i>String</i>
    <a href="#refreshinterval" title="RefreshInterval">RefreshInterval</a>: <i>Double</i>
    <a href="#secondaryvisualization" title="SecondaryVisualization">SecondaryVisualization</a>: <i>String</i>
    <a href="#showsparkline" title="ShowSparkLine">ShowSparkLine</a>: <i>Boolean</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#unitprefix" title="UnitPrefix">UnitPrefix</a>: <i>String</i>
    <a href="#colorscale" title="ColorScale">ColorScale</a>: <i>
      - <a href="colorscaledefinition.md">ColorScaleDefinition</a></i>
    <a href="#vizoptions" title="VizOptions">VizOptions</a>: <i>
      - <a href="vizoptionsdefinition.md">VizOptionsDefinition</a></i>
</pre>

## Properties

#### ColorBy

Must be `"Dimension"`, `"Scale"` or `"Metric"`. `"Dimension"` by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the chart.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsTimestampHidden

Whether to hide the timestamp in the chart. `false` by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDelay

How long (in seconds) to wait for late datapoints.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPrecision

The maximum precision to for value displayed.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the chart.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProgramText

Signalflow program text for the chart. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RefreshInterval

How often (in seconds) to refresh the value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryVisualization

The type of secondary visualization. Can be `None`, `Radial`, `Linear`, or `Sparkline`. If unset, the SignalFx default is used (`None`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowSparkLine

Whether to show a trend line below the current value. `false` by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnitPrefix

Must be `"Metric"` or `"Binary"`. `"Metric"` by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColorScale

_Required_: No

_Type_: List of <a href="colorscaledefinition.md">ColorScaleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VizOptions

_Required_: No

_Type_: List of <a href="vizoptionsdefinition.md">VizOptionsDefinition</a>

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

#### Url

Returns the <code>Url</code> value.

