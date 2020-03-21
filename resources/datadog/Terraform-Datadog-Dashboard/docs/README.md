# Terraform::Datadog::Dashboard

Provides a Datadog dashboard resource. This can be used to create and manage Datadog dashboards.

~> **Note:** This resource uses the new [Dashboard API](https://docs.datadoghq.com/api/#dashboards) which adds new features like better validation and support for the [Group widget](https://docs.datadoghq.com/graphing/widgets/group/). Additionally, this resource unifies [`datadog_timeboard`](timeboard.html) and [`datadog_screenboard`](screenboard.html) resources to allow you to manage all of your dashboards using a single format.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::Dashboard",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#isreadonly" title="IsReadOnly">IsReadOnly</a>" : <i>Boolean</i>,
        "<a href="#layouttype" title="LayoutType">LayoutType</a>" : <i>String</i>,
        "<a href="#notifylist" title="NotifyList">NotifyList</a>" : <i>[ String, ... ]</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#templatevariable" title="TemplateVariable">TemplateVariable</a>" : <i>[ <a href="templatevariable.md">TemplateVariable</a>, ... ]</i>,
        "<a href="#templatevariablepreset" title="TemplateVariablePreset">TemplateVariablePreset</a>" : <i>[ <a href="templatevariablepreset.md">TemplateVariablePreset</a>, ... ]</i>,
        "<a href="#widget" title="Widget">Widget</a>" : <i>[ <a href="widget.md">Widget</a>, ... ]</i>,
        "<a href="#alertgraphdefinition" title="AlertGraphDefinition">AlertGraphDefinition</a>" : <i>[ <a href="alertgraphdefinition.md">AlertGraphDefinition</a>, ... ]</i>,
        "<a href="#alertvaluedefinition" title="AlertValueDefinition">AlertValueDefinition</a>" : <i>[ <a href="alertvaluedefinition.md">AlertValueDefinition</a>, ... ]</i>,
        "<a href="#changedefinition" title="ChangeDefinition">ChangeDefinition</a>" : <i>[ <a href="changedefinition.md">ChangeDefinition</a>, ... ]</i>,
        "<a href="#checkstatusdefinition" title="CheckStatusDefinition">CheckStatusDefinition</a>" : <i>[ <a href="checkstatusdefinition.md">CheckStatusDefinition</a>, ... ]</i>,
        "<a href="#distributiondefinition" title="DistributionDefinition">DistributionDefinition</a>" : <i>[ <a href="distributiondefinition.md">DistributionDefinition</a>, ... ]</i>,
        "<a href="#eventstreamdefinition" title="EventStreamDefinition">EventStreamDefinition</a>" : <i>[ <a href="eventstreamdefinition.md">EventStreamDefinition</a>, ... ]</i>,
        "<a href="#eventtimelinedefinition" title="EventTimelineDefinition">EventTimelineDefinition</a>" : <i>[ <a href="eventtimelinedefinition.md">EventTimelineDefinition</a>, ... ]</i>,
        "<a href="#freetextdefinition" title="FreeTextDefinition">FreeTextDefinition</a>" : <i>[ <a href="freetextdefinition.md">FreeTextDefinition</a>, ... ]</i>,
        "<a href="#groupdefinition" title="GroupDefinition">GroupDefinition</a>" : <i>[ <a href="groupdefinition.md">GroupDefinition</a>, ... ]</i>,
        "<a href="#heatmapdefinition" title="HeatmapDefinition">HeatmapDefinition</a>" : <i>[ <a href="heatmapdefinition.md">HeatmapDefinition</a>, ... ]</i>,
        "<a href="#hostmapdefinition" title="HostmapDefinition">HostmapDefinition</a>" : <i>[ <a href="hostmapdefinition.md">HostmapDefinition</a>, ... ]</i>,
        "<a href="#iframedefinition" title="IframeDefinition">IframeDefinition</a>" : <i>[ <a href="iframedefinition.md">IframeDefinition</a>, ... ]</i>,
        "<a href="#imagedefinition" title="ImageDefinition">ImageDefinition</a>" : <i>[ <a href="imagedefinition.md">ImageDefinition</a>, ... ]</i>,
        "<a href="#logstreamdefinition" title="LogStreamDefinition">LogStreamDefinition</a>" : <i>[ <a href="logstreamdefinition.md">LogStreamDefinition</a>, ... ]</i>,
        "<a href="#managestatusdefinition" title="ManageStatusDefinition">ManageStatusDefinition</a>" : <i>[ <a href="managestatusdefinition.md">ManageStatusDefinition</a>, ... ]</i>,
        "<a href="#notedefinition" title="NoteDefinition">NoteDefinition</a>" : <i>[ <a href="notedefinition.md">NoteDefinition</a>, ... ]</i>,
        "<a href="#querytabledefinition" title="QueryTableDefinition">QueryTableDefinition</a>" : <i>[ <a href="querytabledefinition.md">QueryTableDefinition</a>, ... ]</i>,
        "<a href="#queryvaluedefinition" title="QueryValueDefinition">QueryValueDefinition</a>" : <i>[ <a href="queryvaluedefinition.md">QueryValueDefinition</a>, ... ]</i>,
        "<a href="#scatterplotdefinition" title="ScatterplotDefinition">ScatterplotDefinition</a>" : <i>[ <a href="scatterplotdefinition.md">ScatterplotDefinition</a>, ... ]</i>,
        "<a href="#servicelevelobjectivedefinition" title="ServiceLevelObjectiveDefinition">ServiceLevelObjectiveDefinition</a>" : <i>[ <a href="servicelevelobjectivedefinition.md">ServiceLevelObjectiveDefinition</a>, ... ]</i>,
        "<a href="#timeseriesdefinition" title="TimeseriesDefinition">TimeseriesDefinition</a>" : <i>[ <a href="timeseriesdefinition.md">TimeseriesDefinition</a>, ... ]</i>,
        "<a href="#toplistdefinition" title="ToplistDefinition">ToplistDefinition</a>" : <i>[ <a href="toplistdefinition.md">ToplistDefinition</a>, ... ]</i>,
        "<a href="#traceservicedefinition" title="TraceServiceDefinition">TraceServiceDefinition</a>" : <i>[ <a href="traceservicedefinition.md">TraceServiceDefinition</a>, ... ]</i>,
        "<a href="#request" title="Request">Request</a>" : <i>[ <a href="request.md">Request</a>, ... ]</i>,
        "<a href="#yaxis" title="Yaxis">Yaxis</a>" : <i>[ <a href="yaxis.md">Yaxis</a>, ... ]</i>,
        "<a href="#style" title="Style">Style</a>" : <i>[ <a href="style.md">Style</a>, ... ]</i>,
        "<a href="#xaxis" title="Xaxis">Xaxis</a>" : <i>[ <a href="xaxis.md">Xaxis</a>, ... ]</i>,
        "<a href="#event" title="Event">Event</a>" : <i>[ <a href="event.md">Event</a>, ... ]</i>,
        "<a href="#marker" title="Marker">Marker</a>" : <i>[ <a href="marker.md">Marker</a>, ... ]</i>,
        "<a href="#apmquery" title="ApmQuery">ApmQuery</a>" : <i>[ <a href="apmquery.md">ApmQuery</a>, ... ]</i>,
        "<a href="#conditionalformats" title="ConditionalFormats">ConditionalFormats</a>" : <i>[ <a href="conditionalformats.md">ConditionalFormats</a>, ... ]</i>,
        "<a href="#logquery" title="LogQuery">LogQuery</a>" : <i>[ <a href="logquery.md">LogQuery</a>, ... ]</i>,
        "<a href="#processquery" title="ProcessQuery">ProcessQuery</a>" : <i>[ <a href="processquery.md">ProcessQuery</a>, ... ]</i>,
        "<a href="#groupby" title="GroupBy">GroupBy</a>" : <i>[ <a href="groupby.md">GroupBy</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::Dashboard
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#isreadonly" title="IsReadOnly">IsReadOnly</a>: <i>Boolean</i>
    <a href="#layouttype" title="LayoutType">LayoutType</a>: <i>String</i>
    <a href="#notifylist" title="NotifyList">NotifyList</a>: <i>
      - String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#templatevariable" title="TemplateVariable">TemplateVariable</a>: <i>
      - <a href="templatevariable.md">TemplateVariable</a></i>
    <a href="#templatevariablepreset" title="TemplateVariablePreset">TemplateVariablePreset</a>: <i>
      - <a href="templatevariablepreset.md">TemplateVariablePreset</a></i>
    <a href="#widget" title="Widget">Widget</a>: <i>
      - <a href="widget.md">Widget</a></i>
    <a href="#alertgraphdefinition" title="AlertGraphDefinition">AlertGraphDefinition</a>: <i>
      - <a href="alertgraphdefinition.md">AlertGraphDefinition</a></i>
    <a href="#alertvaluedefinition" title="AlertValueDefinition">AlertValueDefinition</a>: <i>
      - <a href="alertvaluedefinition.md">AlertValueDefinition</a></i>
    <a href="#changedefinition" title="ChangeDefinition">ChangeDefinition</a>: <i>
      - <a href="changedefinition.md">ChangeDefinition</a></i>
    <a href="#checkstatusdefinition" title="CheckStatusDefinition">CheckStatusDefinition</a>: <i>
      - <a href="checkstatusdefinition.md">CheckStatusDefinition</a></i>
    <a href="#distributiondefinition" title="DistributionDefinition">DistributionDefinition</a>: <i>
      - <a href="distributiondefinition.md">DistributionDefinition</a></i>
    <a href="#eventstreamdefinition" title="EventStreamDefinition">EventStreamDefinition</a>: <i>
      - <a href="eventstreamdefinition.md">EventStreamDefinition</a></i>
    <a href="#eventtimelinedefinition" title="EventTimelineDefinition">EventTimelineDefinition</a>: <i>
      - <a href="eventtimelinedefinition.md">EventTimelineDefinition</a></i>
    <a href="#freetextdefinition" title="FreeTextDefinition">FreeTextDefinition</a>: <i>
      - <a href="freetextdefinition.md">FreeTextDefinition</a></i>
    <a href="#groupdefinition" title="GroupDefinition">GroupDefinition</a>: <i>
      - <a href="groupdefinition.md">GroupDefinition</a></i>
    <a href="#heatmapdefinition" title="HeatmapDefinition">HeatmapDefinition</a>: <i>
      - <a href="heatmapdefinition.md">HeatmapDefinition</a></i>
    <a href="#hostmapdefinition" title="HostmapDefinition">HostmapDefinition</a>: <i>
      - <a href="hostmapdefinition.md">HostmapDefinition</a></i>
    <a href="#iframedefinition" title="IframeDefinition">IframeDefinition</a>: <i>
      - <a href="iframedefinition.md">IframeDefinition</a></i>
    <a href="#imagedefinition" title="ImageDefinition">ImageDefinition</a>: <i>
      - <a href="imagedefinition.md">ImageDefinition</a></i>
    <a href="#logstreamdefinition" title="LogStreamDefinition">LogStreamDefinition</a>: <i>
      - <a href="logstreamdefinition.md">LogStreamDefinition</a></i>
    <a href="#managestatusdefinition" title="ManageStatusDefinition">ManageStatusDefinition</a>: <i>
      - <a href="managestatusdefinition.md">ManageStatusDefinition</a></i>
    <a href="#notedefinition" title="NoteDefinition">NoteDefinition</a>: <i>
      - <a href="notedefinition.md">NoteDefinition</a></i>
    <a href="#querytabledefinition" title="QueryTableDefinition">QueryTableDefinition</a>: <i>
      - <a href="querytabledefinition.md">QueryTableDefinition</a></i>
    <a href="#queryvaluedefinition" title="QueryValueDefinition">QueryValueDefinition</a>: <i>
      - <a href="queryvaluedefinition.md">QueryValueDefinition</a></i>
    <a href="#scatterplotdefinition" title="ScatterplotDefinition">ScatterplotDefinition</a>: <i>
      - <a href="scatterplotdefinition.md">ScatterplotDefinition</a></i>
    <a href="#servicelevelobjectivedefinition" title="ServiceLevelObjectiveDefinition">ServiceLevelObjectiveDefinition</a>: <i>
      - <a href="servicelevelobjectivedefinition.md">ServiceLevelObjectiveDefinition</a></i>
    <a href="#timeseriesdefinition" title="TimeseriesDefinition">TimeseriesDefinition</a>: <i>
      - <a href="timeseriesdefinition.md">TimeseriesDefinition</a></i>
    <a href="#toplistdefinition" title="ToplistDefinition">ToplistDefinition</a>: <i>
      - <a href="toplistdefinition.md">ToplistDefinition</a></i>
    <a href="#traceservicedefinition" title="TraceServiceDefinition">TraceServiceDefinition</a>: <i>
      - <a href="traceservicedefinition.md">TraceServiceDefinition</a></i>
    <a href="#request" title="Request">Request</a>: <i>
      - <a href="request.md">Request</a></i>
    <a href="#yaxis" title="Yaxis">Yaxis</a>: <i>
      - <a href="yaxis.md">Yaxis</a></i>
    <a href="#style" title="Style">Style</a>: <i>
      - <a href="style.md">Style</a></i>
    <a href="#xaxis" title="Xaxis">Xaxis</a>: <i>
      - <a href="xaxis.md">Xaxis</a></i>
    <a href="#event" title="Event">Event</a>: <i>
      - <a href="event.md">Event</a></i>
    <a href="#marker" title="Marker">Marker</a>: <i>
      - <a href="marker.md">Marker</a></i>
    <a href="#apmquery" title="ApmQuery">ApmQuery</a>: <i>
      - <a href="apmquery.md">ApmQuery</a></i>
    <a href="#conditionalformats" title="ConditionalFormats">ConditionalFormats</a>: <i>
      - <a href="conditionalformats.md">ConditionalFormats</a></i>
    <a href="#logquery" title="LogQuery">LogQuery</a>: <i>
      - <a href="logquery.md">LogQuery</a></i>
    <a href="#processquery" title="ProcessQuery">ProcessQuery</a>: <i>
      - <a href="processquery.md">ProcessQuery</a></i>
    <a href="#groupby" title="GroupBy">GroupBy</a>: <i>
      - <a href="groupby.md">GroupBy</a></i>
</pre>

## Properties

#### Description

Description of the dashboard.
- `is_read_only` - (Optional) Whether this dashboard is read-only. If `true`, only the author and admins can make changes to it.
- `notify_list` - (Optional) List of handles of users to notify when changes are made to this dashboard.
- `template_variables` - (Optional) Nested block describing a template variable. The structure of this block is described [below](dashboard.html#nested-template_variable-blocks). Multiple template_variable blocks are allowed within a `datadog_dashboard` resource.
- `template_variable_presets` - (Optional) Nested block describing saved configurations of existing template variables. The structure of this block is described [below](dashboard.html#nested-template_variable_preset-blocks). Multiple template_variable_preset blocks are allowed within a `datadog_dashboard` resource, and multiple template_variables can be described by each template_variable_preset.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsReadOnly

Whether this dashboard is read-only. If `true`, only the author and admins can make changes to it.
- `notify_list` - (Optional) List of handles of users to notify when changes are made to this dashboard.
- `template_variables` - (Optional) Nested block describing a template variable. The structure of this block is described [below](dashboard.html#nested-template_variable-blocks). Multiple template_variable blocks are allowed within a `datadog_dashboard` resource.
- `template_variable_presets` - (Optional) Nested block describing saved configurations of existing template variables. The structure of this block is described [below](dashboard.html#nested-template_variable_preset-blocks). Multiple template_variable_preset blocks are allowed within a `datadog_dashboard` resource, and multiple template_variables can be described by each template_variable_preset.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LayoutType

Layout type of the dashboard. Available values are: `ordered` (previous timeboard) or `free` (previous screenboard layout).
<br>**Note: This value cannot be changed. Converting a dashboard from `free` <-> `ordered` requires destroying and re-creating the dashboard.** Instead of using `ForceNew`, this is a manual action as many underlying widget configs need to be updated to work for the updated layout, otherwise the new dashboard won't be created properly.
- `description` - (Optional) Description of the dashboard.
- `is_read_only` - (Optional) Whether this dashboard is read-only. If `true`, only the author and admins can make changes to it.
- `notify_list` - (Optional) List of handles of users to notify when changes are made to this dashboard.
- `template_variables` - (Optional) Nested block describing a template variable. The structure of this block is described [below](dashboard.html#nested-template_variable-blocks). Multiple template_variable blocks are allowed within a `datadog_dashboard` resource.
- `template_variable_presets` - (Optional) Nested block describing saved configurations of existing template variables. The structure of this block is described [below](dashboard.html#nested-template_variable_preset-blocks). Multiple template_variable_preset blocks are allowed within a `datadog_dashboard` resource, and multiple template_variables can be described by each template_variable_preset.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyList

List of handles of users to notify when changes are made to this dashboard.
- `template_variables` - (Optional) Nested block describing a template variable. The structure of this block is described [below](dashboard.html#nested-template_variable-blocks). Multiple template_variable blocks are allowed within a `datadog_dashboard` resource.
- `template_variable_presets` - (Optional) Nested block describing saved configurations of existing template variables. The structure of this block is described [below](dashboard.html#nested-template_variable_preset-blocks). Multiple template_variable_preset blocks are allowed within a `datadog_dashboard` resource, and multiple template_variables can be described by each template_variable_preset.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

Title of the dashboard.
- `widget` - (Required) Nested block describing a widget. The structure of this block is described [below](dashboard.html#nested-widget-blocks). Multiple `widget` blocks are allowed within a `datadog_dashboard` resource.
- `layout_type` - (Required) Layout type of the dashboard. Available values are: `ordered` (previous timeboard) or `free` (previous screenboard layout).
<br>**Note: This value cannot be changed. Converting a dashboard from `free` <-> `ordered` requires destroying and re-creating the dashboard.** Instead of using `ForceNew`, this is a manual action as many underlying widget configs need to be updated to work for the updated layout, otherwise the new dashboard won't be created properly.
- `description` - (Optional) Description of the dashboard.
- `is_read_only` - (Optional) Whether this dashboard is read-only. If `true`, only the author and admins can make changes to it.
- `notify_list` - (Optional) List of handles of users to notify when changes are made to this dashboard.
- `template_variables` - (Optional) Nested block describing a template variable. The structure of this block is described [below](dashboard.html#nested-template_variable-blocks). Multiple template_variable blocks are allowed within a `datadog_dashboard` resource.
- `template_variable_presets` - (Optional) Nested block describing saved configurations of existing template variables. The structure of this block is described [below](dashboard.html#nested-template_variable_preset-blocks). Multiple template_variable_preset blocks are allowed within a `datadog_dashboard` resource, and multiple template_variables can be described by each template_variable_preset.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateVariable

_Required_: No

_Type_: List of <a href="templatevariable.md">TemplateVariable</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateVariablePreset

_Required_: No

_Type_: List of <a href="templatevariablepreset.md">TemplateVariablePreset</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Widget

_Required_: No

_Type_: List of <a href="widget.md">Widget</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertGraphDefinition

_Required_: No

_Type_: List of <a href="alertgraphdefinition.md">AlertGraphDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertValueDefinition

_Required_: No

_Type_: List of <a href="alertvaluedefinition.md">AlertValueDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChangeDefinition

_Required_: No

_Type_: List of <a href="changedefinition.md">ChangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckStatusDefinition

_Required_: No

_Type_: List of <a href="checkstatusdefinition.md">CheckStatusDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributionDefinition

_Required_: No

_Type_: List of <a href="distributiondefinition.md">DistributionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventStreamDefinition

_Required_: No

_Type_: List of <a href="eventstreamdefinition.md">EventStreamDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventTimelineDefinition

_Required_: No

_Type_: List of <a href="eventtimelinedefinition.md">EventTimelineDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeTextDefinition

_Required_: No

_Type_: List of <a href="freetextdefinition.md">FreeTextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupDefinition

_Required_: No

_Type_: List of <a href="groupdefinition.md">GroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeatmapDefinition

_Required_: No

_Type_: List of <a href="heatmapdefinition.md">HeatmapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostmapDefinition

_Required_: No

_Type_: List of <a href="hostmapdefinition.md">HostmapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IframeDefinition

_Required_: No

_Type_: List of <a href="iframedefinition.md">IframeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageDefinition

_Required_: No

_Type_: List of <a href="imagedefinition.md">ImageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogStreamDefinition

_Required_: No

_Type_: List of <a href="logstreamdefinition.md">LogStreamDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageStatusDefinition

_Required_: No

_Type_: List of <a href="managestatusdefinition.md">ManageStatusDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoteDefinition

_Required_: No

_Type_: List of <a href="notedefinition.md">NoteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryTableDefinition

_Required_: No

_Type_: List of <a href="querytabledefinition.md">QueryTableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryValueDefinition

_Required_: No

_Type_: List of <a href="queryvaluedefinition.md">QueryValueDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScatterplotDefinition

_Required_: No

_Type_: List of <a href="scatterplotdefinition.md">ScatterplotDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceLevelObjectiveDefinition

_Required_: No

_Type_: List of <a href="servicelevelobjectivedefinition.md">ServiceLevelObjectiveDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeseriesDefinition

_Required_: No

_Type_: List of <a href="timeseriesdefinition.md">TimeseriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToplistDefinition

_Required_: No

_Type_: List of <a href="toplistdefinition.md">ToplistDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TraceServiceDefinition

_Required_: No

_Type_: List of <a href="traceservicedefinition.md">TraceServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Request

_Required_: No

_Type_: List of <a href="request.md">Request</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Yaxis

_Required_: No

_Type_: List of <a href="yaxis.md">Yaxis</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Style

_Required_: No

_Type_: List of <a href="style.md">Style</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Xaxis

_Required_: No

_Type_: List of <a href="xaxis.md">Xaxis</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Event

_Required_: No

_Type_: List of <a href="event.md">Event</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Marker

_Required_: No

_Type_: List of <a href="marker.md">Marker</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApmQuery

_Required_: No

_Type_: List of <a href="apmquery.md">ApmQuery</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionalFormats

_Required_: No

_Type_: List of <a href="conditionalformats.md">ConditionalFormats</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogQuery

_Required_: No

_Type_: List of <a href="logquery.md">LogQuery</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessQuery

_Required_: No

_Type_: List of <a href="processquery.md">ProcessQuery</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupBy

_Required_: No

_Type_: List of <a href="groupby.md">GroupBy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

