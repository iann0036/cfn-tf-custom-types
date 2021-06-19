# TF::SignalFx::Dashboard

A dashboard is a curated collection of specific charts and supports dimensional [filters](http://docs.signalfx.com/en/latest/dashboards/dashboard-filter-dynamic.html#filter-dashboard-charts), [dashboard variables](http://docs.signalfx.com/en/latest/dashboards/dashboard-filter-dynamic.html#dashboard-variables) and [time range](http://docs.signalfx.com/en/latest/_sidebars-and-includes/using-time-range-selector.html#time-range-selector) options. These options are applied to all charts in the dashboard, providing a consistent view of the data displayed in that dashboard. This also means that when you open a chart to drill down for more details, you are viewing the same data that is visible in the dashboard view.

~> **NOTE** Since every dashboard is included in a [dashboard group](dashboard_group.html) (SignalFx collection of dashboards), you need to create that first and reference it as shown in the example.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SignalFx::Dashboard",
    "Properties" : {
        "<a href="#authorizedwriterteams" title="AuthorizedWriterTeams">AuthorizedWriterTeams</a>" : <i>[ String, ... ]</i>,
        "<a href="#authorizedwriterusers" title="AuthorizedWriterUsers">AuthorizedWriterUsers</a>" : <i>[ String, ... ]</i>,
        "<a href="#chartsresolution" title="ChartsResolution">ChartsResolution</a>" : <i>String</i>,
        "<a href="#dashboardgroup" title="DashboardGroup">DashboardGroup</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#discoveryoptionsquery" title="DiscoveryOptionsQuery">DiscoveryOptionsQuery</a>" : <i>String</i>,
        "<a href="#discoveryoptionsselectors" title="DiscoveryOptionsSelectors">DiscoveryOptionsSelectors</a>" : <i>[ String, ... ]</i>,
        "<a href="#endtime" title="EndTime">EndTime</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#starttime" title="StartTime">StartTime</a>" : <i>Double</i>,
        "<a href="#timerange" title="TimeRange">TimeRange</a>" : <i>String</i>,
        "<a href="#chart" title="Chart">Chart</a>" : <i>[ <a href="chartdefinition.md">ChartDefinition</a>, ... ]</i>,
        "<a href="#column" title="Column">Column</a>" : <i>[ <a href="columndefinition.md">ColumnDefinition</a>, ... ]</i>,
        "<a href="#eventoverlay" title="EventOverlay">EventOverlay</a>" : <i>[ <a href="eventoverlaydefinition.md">EventOverlayDefinition</a>, ... ]</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filterdefinition.md">FilterDefinition</a>, ... ]</i>,
        "<a href="#grid" title="Grid">Grid</a>" : <i>[ <a href="griddefinition.md">GridDefinition</a>, ... ]</i>,
        "<a href="#selectedeventoverlay" title="SelectedEventOverlay">SelectedEventOverlay</a>" : <i>[ <a href="selectedeventoverlaydefinition.md">SelectedEventOverlayDefinition</a>, ... ]</i>,
        "<a href="#variable" title="Variable">Variable</a>" : <i>[ <a href="variabledefinition.md">VariableDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SignalFx::Dashboard
Properties:
    <a href="#authorizedwriterteams" title="AuthorizedWriterTeams">AuthorizedWriterTeams</a>: <i>
      - String</i>
    <a href="#authorizedwriterusers" title="AuthorizedWriterUsers">AuthorizedWriterUsers</a>: <i>
      - String</i>
    <a href="#chartsresolution" title="ChartsResolution">ChartsResolution</a>: <i>String</i>
    <a href="#dashboardgroup" title="DashboardGroup">DashboardGroup</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#discoveryoptionsquery" title="DiscoveryOptionsQuery">DiscoveryOptionsQuery</a>: <i>String</i>
    <a href="#discoveryoptionsselectors" title="DiscoveryOptionsSelectors">DiscoveryOptionsSelectors</a>: <i>
      - String</i>
    <a href="#endtime" title="EndTime">EndTime</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#starttime" title="StartTime">StartTime</a>: <i>Double</i>
    <a href="#timerange" title="TimeRange">TimeRange</a>: <i>String</i>
    <a href="#chart" title="Chart">Chart</a>: <i>
      - <a href="chartdefinition.md">ChartDefinition</a></i>
    <a href="#column" title="Column">Column</a>: <i>
      - <a href="columndefinition.md">ColumnDefinition</a></i>
    <a href="#eventoverlay" title="EventOverlay">EventOverlay</a>: <i>
      - <a href="eventoverlaydefinition.md">EventOverlayDefinition</a></i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filterdefinition.md">FilterDefinition</a></i>
    <a href="#grid" title="Grid">Grid</a>: <i>
      - <a href="griddefinition.md">GridDefinition</a></i>
    <a href="#selectedeventoverlay" title="SelectedEventOverlay">SelectedEventOverlay</a>: <i>
      - <a href="selectedeventoverlaydefinition.md">SelectedEventOverlayDefinition</a></i>
    <a href="#variable" title="Variable">Variable</a>: <i>
      - <a href="variabledefinition.md">VariableDefinition</a></i>
</pre>

## Properties

#### AuthorizedWriterTeams

Team IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's team (or user id in `authorized_writer_teams`).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizedWriterUsers

User IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChartsResolution

Specifies the chart data display resolution for charts in this dashboard. Value can be one of `"default"`,  `"low"`, `"high"`, or  `"highest"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DashboardGroup

The ID of the dashboard group that contains the dashboard.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Variable description.
* `values` - (Optional) List of of strings (which will be treated as an OR filter on the property).
* `value_required` - (Optional) Determines whether a value is required for this variable (and therefore whether it will be possible to view this dashboard without this filter applied). `false` by default.
* `values_suggested` - (Optional) A list of strings of suggested values for this variable; these suggestions will receive priority when values are autosuggested for this variable.
* `restricted_suggestions` - (Optional) If `true`, this variable may only be set to the values listed in `values_suggested` and only these values will appear in autosuggestion menus. `false` by default.
* `replace_only` - (Optional) If `true`, this variable will only apply to charts that have a filter for the property.
* `apply_if_exist` - (Optional) If true, this variable will also match data that doesn't have this property at all.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiscoveryOptionsQuery

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiscoveryOptionsSelectors

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndTime

Seconds since epoch. Used for visualization.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the dashboard.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

Seconds since epoch. Used for visualization.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeRange

The time range prior to now to visualize. SignalFx time syntax (e.g. `"-5m"`, `"-1h"`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Chart

_Required_: No

_Type_: List of <a href="chartdefinition.md">ChartDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Column

_Required_: No

_Type_: List of <a href="columndefinition.md">ColumnDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventOverlay

_Required_: No

_Type_: List of <a href="eventoverlaydefinition.md">EventOverlayDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="filterdefinition.md">FilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Grid

_Required_: No

_Type_: List of <a href="griddefinition.md">GridDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectedEventOverlay

_Required_: No

_Type_: List of <a href="selectedeventoverlaydefinition.md">SelectedEventOverlayDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Variable

_Required_: No

_Type_: List of <a href="variabledefinition.md">VariableDefinition</a>

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

