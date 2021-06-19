# TF::SignalFx::TimeChart

Provides a SignalFx time chart resource. This can be used to create and manage the different types of time charts.

Time charts display data points over a period of time.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SignalFx::TimeChart",
    "Properties" : {
        "<a href="#axesincludezero" title="AxesIncludeZero">AxesIncludeZero</a>" : <i>Boolean</i>,
        "<a href="#axesprecision" title="AxesPrecision">AxesPrecision</a>" : <i>Double</i>,
        "<a href="#colorby" title="ColorBy">ColorBy</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disablesampling" title="DisableSampling">DisableSampling</a>" : <i>Boolean</i>,
        "<a href="#endtime" title="EndTime">EndTime</a>" : <i>Double</i>,
        "<a href="#legendfieldstohide" title="LegendFieldsToHide">LegendFieldsToHide</a>" : <i>[ String, ... ]</i>,
        "<a href="#maxdelay" title="MaxDelay">MaxDelay</a>" : <i>Double</i>,
        "<a href="#minimumresolution" title="MinimumResolution">MinimumResolution</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#onchartlegenddimension" title="OnChartLegendDimension">OnChartLegendDimension</a>" : <i>String</i>,
        "<a href="#plottype" title="PlotType">PlotType</a>" : <i>String</i>,
        "<a href="#programtext" title="ProgramText">ProgramText</a>" : <i>String</i>,
        "<a href="#showdatamarkers" title="ShowDataMarkers">ShowDataMarkers</a>" : <i>Boolean</i>,
        "<a href="#showeventlines" title="ShowEventLines">ShowEventLines</a>" : <i>Boolean</i>,
        "<a href="#stacked" title="Stacked">Stacked</a>" : <i>Boolean</i>,
        "<a href="#starttime" title="StartTime">StartTime</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#timerange" title="TimeRange">TimeRange</a>" : <i>Double</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#unitprefix" title="UnitPrefix">UnitPrefix</a>" : <i>String</i>,
        "<a href="#axisleft" title="AxisLeft">AxisLeft</a>" : <i>[ <a href="axisleftdefinition.md">AxisLeftDefinition</a>, ... ]</i>,
        "<a href="#axisright" title="AxisRight">AxisRight</a>" : <i>[ <a href="axisrightdefinition.md">AxisRightDefinition</a>, ... ]</i>,
        "<a href="#eventoptions" title="EventOptions">EventOptions</a>" : <i>[ <a href="eventoptionsdefinition.md">EventOptionsDefinition</a>, ... ]</i>,
        "<a href="#histogramoptions" title="HistogramOptions">HistogramOptions</a>" : <i>[ <a href="histogramoptionsdefinition.md">HistogramOptionsDefinition</a>, ... ]</i>,
        "<a href="#legendoptionsfields" title="LegendOptionsFields">LegendOptionsFields</a>" : <i>[ <a href="legendoptionsfieldsdefinition.md">LegendOptionsFieldsDefinition</a>, ... ]</i>,
        "<a href="#vizoptions" title="VizOptions">VizOptions</a>" : <i>[ <a href="vizoptionsdefinition.md">VizOptionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SignalFx::TimeChart
Properties:
    <a href="#axesincludezero" title="AxesIncludeZero">AxesIncludeZero</a>: <i>Boolean</i>
    <a href="#axesprecision" title="AxesPrecision">AxesPrecision</a>: <i>Double</i>
    <a href="#colorby" title="ColorBy">ColorBy</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disablesampling" title="DisableSampling">DisableSampling</a>: <i>Boolean</i>
    <a href="#endtime" title="EndTime">EndTime</a>: <i>Double</i>
    <a href="#legendfieldstohide" title="LegendFieldsToHide">LegendFieldsToHide</a>: <i>
      - String</i>
    <a href="#maxdelay" title="MaxDelay">MaxDelay</a>: <i>Double</i>
    <a href="#minimumresolution" title="MinimumResolution">MinimumResolution</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#onchartlegenddimension" title="OnChartLegendDimension">OnChartLegendDimension</a>: <i>String</i>
    <a href="#plottype" title="PlotType">PlotType</a>: <i>String</i>
    <a href="#programtext" title="ProgramText">ProgramText</a>: <i>String</i>
    <a href="#showdatamarkers" title="ShowDataMarkers">ShowDataMarkers</a>: <i>Boolean</i>
    <a href="#showeventlines" title="ShowEventLines">ShowEventLines</a>: <i>Boolean</i>
    <a href="#stacked" title="Stacked">Stacked</a>: <i>Boolean</i>
    <a href="#starttime" title="StartTime">StartTime</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#timerange" title="TimeRange">TimeRange</a>: <i>Double</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#unitprefix" title="UnitPrefix">UnitPrefix</a>: <i>String</i>
    <a href="#axisleft" title="AxisLeft">AxisLeft</a>: <i>
      - <a href="axisleftdefinition.md">AxisLeftDefinition</a></i>
    <a href="#axisright" title="AxisRight">AxisRight</a>: <i>
      - <a href="axisrightdefinition.md">AxisRightDefinition</a></i>
    <a href="#eventoptions" title="EventOptions">EventOptions</a>: <i>
      - <a href="eventoptionsdefinition.md">EventOptionsDefinition</a></i>
    <a href="#histogramoptions" title="HistogramOptions">HistogramOptions</a>: <i>
      - <a href="histogramoptionsdefinition.md">HistogramOptionsDefinition</a></i>
    <a href="#legendoptionsfields" title="LegendOptionsFields">LegendOptionsFields</a>: <i>
      - <a href="legendoptionsfieldsdefinition.md">LegendOptionsFieldsDefinition</a></i>
    <a href="#vizoptions" title="VizOptions">VizOptions</a>: <i>
      - <a href="vizoptionsdefinition.md">VizOptionsDefinition</a></i>
</pre>

## Properties

#### AxesIncludeZero

Force the chart to display zero on the y-axes, even if none of the data is near zero.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AxesPrecision

Specifies the digits SignalFx displays for values plotted on the chart. Defaults to `3`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColorBy

Must be `"Dimension"` or `"Metric"`. `"Dimension"` by default.

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

#### MinimumResolution

The minimum resolution (in seconds) to use for computing the underlying program.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the chart.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnChartLegendDimension

Dimensions to show in the on-chart legend. On-chart legend is off unless a dimension is specified. Allowed: `"metric"`, `"plot_label"` and any dimension.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlotType

The visualization style to use. Must be `"LineChart"`, `"AreaChart"`, `"ColumnChart"`, or `"Histogram"`. Chart level `plot_type` by default.
* `value_unit` - (Optional) A unit to attach to this plot. Units support automatic scaling (eg thousands of bytes will be displayed as kilobytes). Values values are `Bit, Kilobit, Megabit, Gigabit, Terabit, Petabit, Exabit, Zettabit, Yottabit, Byte, Kibibyte, Mebibyte, Gigibyte, Tebibyte, Pebibyte, Exbibyte, Zebibyte, Yobibyte, Nanosecond, Microsecond, Millisecond, Second, Minute, Hour, Day, Week`.
* `value_prefix`, `value_suffix` - (Optional) Arbitrary prefix/suffix to display with the value of this plot.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProgramText

Signalflow program text for the chart. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowDataMarkers

Show markers (circles) for each datapoint used to draw line or area charts. `false` by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowEventLines

Whether vertical highlight lines should be drawn in the visualizations at times when events occurred. `false` by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stacked

Whether area and bar charts in the visualization should be stacked. `false` by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

Seconds since epoch. Used for visualization. Conflicts with `time_range`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeRange

How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

Time zone that SignalFlow uses as the basis of calendar window transformation methods. For example, if you set "timezone": "Europe/Paris" and then use the transformation sum(cycle="week", cycle_start="Monday") in your chart's SignalFlow program, the calendar window starts on Monday, Paris time. See the [full list of timezones for more](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_supported_signalflow_time_zones). `"UTC"` by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnitPrefix

Must be `"Metric"` or `"Binary`". `"Metric"` by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AxisLeft

_Required_: No

_Type_: List of <a href="axisleftdefinition.md">AxisLeftDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AxisRight

_Required_: No

_Type_: List of <a href="axisrightdefinition.md">AxisRightDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventOptions

_Required_: No

_Type_: List of <a href="eventoptionsdefinition.md">EventOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HistogramOptions

_Required_: No

_Type_: List of <a href="histogramoptionsdefinition.md">HistogramOptionsDefinition</a>

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

