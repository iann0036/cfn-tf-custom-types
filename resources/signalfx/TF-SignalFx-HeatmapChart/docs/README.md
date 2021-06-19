# TF::SignalFx::HeatmapChart

This chart type displays the specified plot in a heatmap fashion. This format is similar to the [Infrastructure Navigator](https://signalfx-product-docs.readthedocs-hosted.com/en/latest/built-in-content/infra-nav.html#infra), with squares representing each source for the selected metric, and the color of each square representing the value range of the metric.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SignalFx::HeatmapChart",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disablesampling" title="DisableSampling">DisableSampling</a>" : <i>Boolean</i>,
        "<a href="#groupby" title="GroupBy">GroupBy</a>" : <i>[ String, ... ]</i>,
        "<a href="#hidetimestamp" title="HideTimestamp">HideTimestamp</a>" : <i>Boolean</i>,
        "<a href="#maxdelay" title="MaxDelay">MaxDelay</a>" : <i>Double</i>,
        "<a href="#minimumresolution" title="MinimumResolution">MinimumResolution</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#programtext" title="ProgramText">ProgramText</a>" : <i>String</i>,
        "<a href="#refreshinterval" title="RefreshInterval">RefreshInterval</a>" : <i>Double</i>,
        "<a href="#sortby" title="SortBy">SortBy</a>" : <i>String</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#unitprefix" title="UnitPrefix">UnitPrefix</a>" : <i>String</i>,
        "<a href="#colorrange" title="ColorRange">ColorRange</a>" : <i>[ <a href="colorrangedefinition.md">ColorRangeDefinition</a>, ... ]</i>,
        "<a href="#colorscale" title="ColorScale">ColorScale</a>" : <i>[ <a href="colorscaledefinition.md">ColorScaleDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SignalFx::HeatmapChart
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disablesampling" title="DisableSampling">DisableSampling</a>: <i>Boolean</i>
    <a href="#groupby" title="GroupBy">GroupBy</a>: <i>
      - String</i>
    <a href="#hidetimestamp" title="HideTimestamp">HideTimestamp</a>: <i>Boolean</i>
    <a href="#maxdelay" title="MaxDelay">MaxDelay</a>: <i>Double</i>
    <a href="#minimumresolution" title="MinimumResolution">MinimumResolution</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#programtext" title="ProgramText">ProgramText</a>: <i>String</i>
    <a href="#refreshinterval" title="RefreshInterval">RefreshInterval</a>: <i>Double</i>
    <a href="#sortby" title="SortBy">SortBy</a>: <i>String</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#unitprefix" title="UnitPrefix">UnitPrefix</a>: <i>String</i>
    <a href="#colorrange" title="ColorRange">ColorRange</a>: <i>
      - <a href="colorrangedefinition.md">ColorRangeDefinition</a></i>
    <a href="#colorscale" title="ColorScale">ColorScale</a>: <i>
      - <a href="colorscaledefinition.md">ColorScaleDefinition</a></i>
</pre>

## Properties

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

#### GroupBy

Properties to group by in the heatmap (in nesting order).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HideTimestamp

Whether to show the timestamp in the chart. `false` by default.

_Required_: No

_Type_: Boolean

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

#### ProgramText

Signalflow program text for the chart. More info at <https://developers.signalfx.com/docs/signalflow-overview>.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RefreshInterval

How often (in seconds) to refresh the values of the heatmap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SortBy

The property to use when sorting the elements. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`).

_Required_: No

_Type_: String

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

#### ColorRange

_Required_: No

_Type_: List of <a href="colorrangedefinition.md">ColorRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColorScale

_Required_: No

_Type_: List of <a href="colorscaledefinition.md">ColorScaleDefinition</a>

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

