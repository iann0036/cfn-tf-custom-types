# TF::SignalFx::ListChart

This chart type displays current data values in a list format.

The name of each value in the chart reflects the name of the plot and any associated dimensions. We recommend you click the Pencil icon and give the plot a meaningful name, as in plot B below. Otherwise, just the raw metric name will be displayed on the chart, as in plot A below.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SignalFx::ListChart",
    "Properties" : {
        "<a href="#colorby" title="ColorBy">ColorBy</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disablesampling" title="DisableSampling">DisableSampling</a>" : <i>Boolean</i>,
        "<a href="#endtime" title="EndTime">EndTime</a>" : <i>Double</i>,
        "<a href="#hidemissingvalues" title="HideMissingValues">HideMissingValues</a>" : <i>Boolean</i>,
        "<a href="#legendfieldstohide" title="LegendFieldsToHide">LegendFieldsToHide</a>" : <i>[ String, ... ]</i>,
        "<a href="#maxdelay" title="MaxDelay">MaxDelay</a>" : <i>Double</i>,
        "<a href="#maxprecision" title="MaxPrecision">MaxPrecision</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#programtext" title="ProgramText">ProgramText</a>" : <i>String</i>,
        "<a href="#refreshinterval" title="RefreshInterval">RefreshInterval</a>" : <i>Double</i>,
        "<a href="#secondaryvisualization" title="SecondaryVisualization">SecondaryVisualization</a>" : <i>String</i>,
        "<a href="#sortby" title="SortBy">SortBy</a>" : <i>String</i>,
        "<a href="#starttime" title="StartTime">StartTime</a>" : <i>Double</i>,
        "<a href="#timerange" title="TimeRange">TimeRange</a>" : <i>Double</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#unitprefix" title="UnitPrefix">UnitPrefix</a>" : <i>String</i>,
        "<a href="#colorscale" title="ColorScale">ColorScale</a>" : <i>[ <a href="colorscaledefinition.md">ColorScaleDefinition</a>, ... ]</i>,
        "<a href="#legendoptionsfields" title="LegendOptionsFields">LegendOptionsFields</a>" : <i>[ <a href="legendoptionsfieldsdefinition.md">LegendOptionsFieldsDefinition</a>, ... ]</i>,
        "<a href="#vizoptions" title="VizOptions">VizOptions</a>" : <i>[ <a href="vizoptionsdefinition.md">VizOptionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SignalFx::ListChart
Properties:
    <a href="#colorby" title="ColorBy">ColorBy</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disablesampling" title="DisableSampling">DisableSampling</a>: <i>Boolean</i>
    <a href="#endtime" title="EndTime">EndTime</a>: <i>Double</i>
    <a href="#hidemissingvalues" title="HideMissingValues">HideMissingValues</a>: <i>Boolean</i>
    <a href="#legendfieldstohide" title="LegendFieldsToHide">LegendFieldsToHide</a>: <i>
      - String</i>
    <a href="#maxdelay" title="MaxDelay">MaxDelay</a>: <i>Double</i>
    <a href="#maxprecision" title="MaxPrecision">MaxPrecision</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#programtext" title="ProgramText">ProgramText</a>: <i>String</i>
    <a href="#refreshinterval" title="RefreshInterval">RefreshInterval</a>: <i>Double</i>
    <a href="#secondaryvisualization" title="SecondaryVisualization">SecondaryVisualization</a>: <i>String</i>
    <a href="#sortby" title="SortBy">SortBy</a>: <i>String</i>
    <a href="#starttime" title="StartTime">StartTime</a>: <i>Double</i>
    <a href="#timerange" title="TimeRange">TimeRange</a>: <i>Double</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#unitprefix" title="UnitPrefix">UnitPrefix</a>: <i>String</i>
    <a href="#colorscale" title="ColorScale">ColorScale</a>: <i>
      - <a href="colorscaledefinition.md">ColorScaleDefinition</a></i>
    <a href="#legendoptionsfields" title="LegendOptionsFields">LegendOptionsFields</a>: <i>
      - <a href="legendoptionsfieldsdefinition.md">LegendOptionsFieldsDefinition</a></i>
    <a href="#vizoptions" title="VizOptions">VizOptions</a>: <i>
      - <a href="vizoptionsdefinition.md">VizOptionsDefinition</a></i>
</pre>

## Properties

#### ColorBy

Must be one of `"Scale"`, `"Dimension"` or `"Metric"`. `"Dimension"` by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the chart.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableSampling

If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndTime

Seconds since epoch. Used for visualization. Conflicts with `time_range`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HideMissingValues

Determines whether to hide missing data points in the chart. If `true`, missing data points in the chart would be hidden. `false` by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LegendFieldsToHide

List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use `legend_options_fields`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDelay

How long (in seconds) to wait for late datapoints.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPrecision

Maximum number of digits to display when rounding values up or down.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the chart.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProgramText

Signalflow program text for the chart. More info[in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RefreshInterval

How often (in seconds) to refresh the values of the list.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryVisualization

The type of secondary visualization. Can be `None`, `Radial`, `Linear`, or `Sparkline`. If unset, the SignalFx default is used (`Sparkline`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SortBy

The property to use when sorting the elements. Use `value` if you want to sort by value. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`). Note there are some special values for some of the options provided in the UX: `"value"` for Value, `"sf_originatingMetric"` for Metric, and `"sf_metric"` for plot.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

Seconds since epoch. Used for visualization. Conflicts with `time_range`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeRange

How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

The property value is a string that denotes the geographic region associated with the time zone, (default UTC).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnitPrefix

Must be `"Metric"` or `"Binary`". `"Metric"` by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColorScale

_Required_: No

_Type_: List of <a href="colorscaledefinition.md">ColorScaleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LegendOptionsFields

_Required_: No

_Type_: List of <a href="legendoptionsfieldsdefinition.md">LegendOptionsFieldsDefinition</a>

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

