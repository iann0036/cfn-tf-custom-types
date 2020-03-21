# Terraform::Datadog::Dashboard

CloudFormation equivalent of datadog_dashboard

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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsReadOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LayoutType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

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

