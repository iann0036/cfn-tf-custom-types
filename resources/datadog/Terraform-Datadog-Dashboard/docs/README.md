# Terraform::Datadog::Dashboard

CloudFormation equivalent of datadog_dashboard

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::Dashboard",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#isreadonly" title="IsReadOnly">IsReadOnly</a>" : <i>Boolean</i>,
        "<a href="#layouttype" title="LayoutType">LayoutType</a>" : <i>String</i>,
        "<a href="#notifylist" title="NotifyList">NotifyList</a>" : <i>[ String, ... ]</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#templatevariable" title="TemplateVariable">TemplateVariable</a>" : <i>[ &lt;a href=&#34;templatevariable.md&#34;&gt;TemplateVariable&lt;/a&gt;, ... ]</i>,
        "<a href="#templatevariablepreset" title="TemplateVariablePreset">TemplateVariablePreset</a>" : <i>[ &lt;a href=&#34;templatevariablepreset.md&#34;&gt;TemplateVariablePreset&lt;/a&gt;, ... ]</i>,
        "<a href="#widget" title="Widget">Widget</a>" : <i>[ &lt;a href=&#34;widget.md&#34;&gt;Widget&lt;/a&gt;, ... ]</i>,
        "<a href="#alertgraphdefinition" title="AlertGraphDefinition">AlertGraphDefinition</a>" : <i>[ &lt;a href=&#34;alertgraphdefinition.md&#34;&gt;AlertGraphDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#alertvaluedefinition" title="AlertValueDefinition">AlertValueDefinition</a>" : <i>[ &lt;a href=&#34;alertvaluedefinition.md&#34;&gt;AlertValueDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#changedefinition" title="ChangeDefinition">ChangeDefinition</a>" : <i>[ &lt;a href=&#34;changedefinition.md&#34;&gt;ChangeDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#checkstatusdefinition" title="CheckStatusDefinition">CheckStatusDefinition</a>" : <i>[ &lt;a href=&#34;checkstatusdefinition.md&#34;&gt;CheckStatusDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#distributiondefinition" title="DistributionDefinition">DistributionDefinition</a>" : <i>[ &lt;a href=&#34;distributiondefinition.md&#34;&gt;DistributionDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#eventstreamdefinition" title="EventStreamDefinition">EventStreamDefinition</a>" : <i>[ &lt;a href=&#34;eventstreamdefinition.md&#34;&gt;EventStreamDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#eventtimelinedefinition" title="EventTimelineDefinition">EventTimelineDefinition</a>" : <i>[ &lt;a href=&#34;eventtimelinedefinition.md&#34;&gt;EventTimelineDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#freetextdefinition" title="FreeTextDefinition">FreeTextDefinition</a>" : <i>[ &lt;a href=&#34;freetextdefinition.md&#34;&gt;FreeTextDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#groupdefinition" title="GroupDefinition">GroupDefinition</a>" : <i>[ &lt;a href=&#34;groupdefinition.md&#34;&gt;GroupDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#heatmapdefinition" title="HeatmapDefinition">HeatmapDefinition</a>" : <i>[ &lt;a href=&#34;heatmapdefinition.md&#34;&gt;HeatmapDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#hostmapdefinition" title="HostmapDefinition">HostmapDefinition</a>" : <i>[ &lt;a href=&#34;hostmapdefinition.md&#34;&gt;HostmapDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#iframedefinition" title="IframeDefinition">IframeDefinition</a>" : <i>[ &lt;a href=&#34;iframedefinition.md&#34;&gt;IframeDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#imagedefinition" title="ImageDefinition">ImageDefinition</a>" : <i>[ &lt;a href=&#34;imagedefinition.md&#34;&gt;ImageDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#logstreamdefinition" title="LogStreamDefinition">LogStreamDefinition</a>" : <i>[ &lt;a href=&#34;logstreamdefinition.md&#34;&gt;LogStreamDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#managestatusdefinition" title="ManageStatusDefinition">ManageStatusDefinition</a>" : <i>[ &lt;a href=&#34;managestatusdefinition.md&#34;&gt;ManageStatusDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#notedefinition" title="NoteDefinition">NoteDefinition</a>" : <i>[ &lt;a href=&#34;notedefinition.md&#34;&gt;NoteDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#querytabledefinition" title="QueryTableDefinition">QueryTableDefinition</a>" : <i>[ &lt;a href=&#34;querytabledefinition.md&#34;&gt;QueryTableDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#queryvaluedefinition" title="QueryValueDefinition">QueryValueDefinition</a>" : <i>[ &lt;a href=&#34;queryvaluedefinition.md&#34;&gt;QueryValueDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#scatterplotdefinition" title="ScatterplotDefinition">ScatterplotDefinition</a>" : <i>[ &lt;a href=&#34;scatterplotdefinition.md&#34;&gt;ScatterplotDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#servicelevelobjectivedefinition" title="ServiceLevelObjectiveDefinition">ServiceLevelObjectiveDefinition</a>" : <i>[ &lt;a href=&#34;servicelevelobjectivedefinition.md&#34;&gt;ServiceLevelObjectiveDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#timeseriesdefinition" title="TimeseriesDefinition">TimeseriesDefinition</a>" : <i>[ &lt;a href=&#34;timeseriesdefinition.md&#34;&gt;TimeseriesDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#toplistdefinition" title="ToplistDefinition">ToplistDefinition</a>" : <i>[ &lt;a href=&#34;toplistdefinition.md&#34;&gt;ToplistDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#traceservicedefinition" title="TraceServiceDefinition">TraceServiceDefinition</a>" : <i>[ &lt;a href=&#34;traceservicedefinition.md&#34;&gt;TraceServiceDefinition&lt;/a&gt;, ... ]</i>,
        "<a href="#request" title="Request">Request</a>" : <i>[ &lt;a href=&#34;request.md&#34;&gt;Request&lt;/a&gt;, ... ]</i>,
        "<a href="#yaxis" title="Yaxis">Yaxis</a>" : <i>[ &lt;a href=&#34;yaxis.md&#34;&gt;Yaxis&lt;/a&gt;, ... ]</i>,
        "<a href="#style" title="Style">Style</a>" : <i>[ &lt;a href=&#34;style.md&#34;&gt;Style&lt;/a&gt;, ... ]</i>,
        "<a href="#xaxis" title="Xaxis">Xaxis</a>" : <i>[ &lt;a href=&#34;xaxis.md&#34;&gt;Xaxis&lt;/a&gt;, ... ]</i>,
        "<a href="#event" title="Event">Event</a>" : <i>[ &lt;a href=&#34;event.md&#34;&gt;Event&lt;/a&gt;, ... ]</i>,
        "<a href="#marker" title="Marker">Marker</a>" : <i>[ &lt;a href=&#34;marker.md&#34;&gt;Marker&lt;/a&gt;, ... ]</i>,
        "<a href="#apmquery" title="ApmQuery">ApmQuery</a>" : <i>[ &lt;a href=&#34;apmquery.md&#34;&gt;ApmQuery&lt;/a&gt;, ... ]</i>,
        "<a href="#conditionalformats" title="ConditionalFormats">ConditionalFormats</a>" : <i>[ &lt;a href=&#34;conditionalformats.md&#34;&gt;ConditionalFormats&lt;/a&gt;, ... ]</i>,
        "<a href="#logquery" title="LogQuery">LogQuery</a>" : <i>[ &lt;a href=&#34;logquery.md&#34;&gt;LogQuery&lt;/a&gt;, ... ]</i>,
        "<a href="#processquery" title="ProcessQuery">ProcessQuery</a>" : <i>[ &lt;a href=&#34;processquery.md&#34;&gt;ProcessQuery&lt;/a&gt;, ... ]</i>,
        "<a href="#groupby" title="GroupBy">GroupBy</a>" : <i>[ &lt;a href=&#34;groupby.md&#34;&gt;GroupBy&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::Dashboard
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#isreadonly" title="IsReadOnly">IsReadOnly</a>: <i>Boolean</i>
    <a href="#layouttype" title="LayoutType">LayoutType</a>: <i>String</i>
    <a href="#notifylist" title="NotifyList">NotifyList</a>: <i>
      - String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#templatevariable" title="TemplateVariable">TemplateVariable</a>: <i>
      - &lt;a href=&#34;templatevariable.md&#34;&gt;TemplateVariable&lt;/a&gt;</i>
    <a href="#templatevariablepreset" title="TemplateVariablePreset">TemplateVariablePreset</a>: <i>
      - &lt;a href=&#34;templatevariablepreset.md&#34;&gt;TemplateVariablePreset&lt;/a&gt;</i>
    <a href="#widget" title="Widget">Widget</a>: <i>
      - &lt;a href=&#34;widget.md&#34;&gt;Widget&lt;/a&gt;</i>
    <a href="#alertgraphdefinition" title="AlertGraphDefinition">AlertGraphDefinition</a>: <i>
      - &lt;a href=&#34;alertgraphdefinition.md&#34;&gt;AlertGraphDefinition&lt;/a&gt;</i>
    <a href="#alertvaluedefinition" title="AlertValueDefinition">AlertValueDefinition</a>: <i>
      - &lt;a href=&#34;alertvaluedefinition.md&#34;&gt;AlertValueDefinition&lt;/a&gt;</i>
    <a href="#changedefinition" title="ChangeDefinition">ChangeDefinition</a>: <i>
      - &lt;a href=&#34;changedefinition.md&#34;&gt;ChangeDefinition&lt;/a&gt;</i>
    <a href="#checkstatusdefinition" title="CheckStatusDefinition">CheckStatusDefinition</a>: <i>
      - &lt;a href=&#34;checkstatusdefinition.md&#34;&gt;CheckStatusDefinition&lt;/a&gt;</i>
    <a href="#distributiondefinition" title="DistributionDefinition">DistributionDefinition</a>: <i>
      - &lt;a href=&#34;distributiondefinition.md&#34;&gt;DistributionDefinition&lt;/a&gt;</i>
    <a href="#eventstreamdefinition" title="EventStreamDefinition">EventStreamDefinition</a>: <i>
      - &lt;a href=&#34;eventstreamdefinition.md&#34;&gt;EventStreamDefinition&lt;/a&gt;</i>
    <a href="#eventtimelinedefinition" title="EventTimelineDefinition">EventTimelineDefinition</a>: <i>
      - &lt;a href=&#34;eventtimelinedefinition.md&#34;&gt;EventTimelineDefinition&lt;/a&gt;</i>
    <a href="#freetextdefinition" title="FreeTextDefinition">FreeTextDefinition</a>: <i>
      - &lt;a href=&#34;freetextdefinition.md&#34;&gt;FreeTextDefinition&lt;/a&gt;</i>
    <a href="#groupdefinition" title="GroupDefinition">GroupDefinition</a>: <i>
      - &lt;a href=&#34;groupdefinition.md&#34;&gt;GroupDefinition&lt;/a&gt;</i>
    <a href="#heatmapdefinition" title="HeatmapDefinition">HeatmapDefinition</a>: <i>
      - &lt;a href=&#34;heatmapdefinition.md&#34;&gt;HeatmapDefinition&lt;/a&gt;</i>
    <a href="#hostmapdefinition" title="HostmapDefinition">HostmapDefinition</a>: <i>
      - &lt;a href=&#34;hostmapdefinition.md&#34;&gt;HostmapDefinition&lt;/a&gt;</i>
    <a href="#iframedefinition" title="IframeDefinition">IframeDefinition</a>: <i>
      - &lt;a href=&#34;iframedefinition.md&#34;&gt;IframeDefinition&lt;/a&gt;</i>
    <a href="#imagedefinition" title="ImageDefinition">ImageDefinition</a>: <i>
      - &lt;a href=&#34;imagedefinition.md&#34;&gt;ImageDefinition&lt;/a&gt;</i>
    <a href="#logstreamdefinition" title="LogStreamDefinition">LogStreamDefinition</a>: <i>
      - &lt;a href=&#34;logstreamdefinition.md&#34;&gt;LogStreamDefinition&lt;/a&gt;</i>
    <a href="#managestatusdefinition" title="ManageStatusDefinition">ManageStatusDefinition</a>: <i>
      - &lt;a href=&#34;managestatusdefinition.md&#34;&gt;ManageStatusDefinition&lt;/a&gt;</i>
    <a href="#notedefinition" title="NoteDefinition">NoteDefinition</a>: <i>
      - &lt;a href=&#34;notedefinition.md&#34;&gt;NoteDefinition&lt;/a&gt;</i>
    <a href="#querytabledefinition" title="QueryTableDefinition">QueryTableDefinition</a>: <i>
      - &lt;a href=&#34;querytabledefinition.md&#34;&gt;QueryTableDefinition&lt;/a&gt;</i>
    <a href="#queryvaluedefinition" title="QueryValueDefinition">QueryValueDefinition</a>: <i>
      - &lt;a href=&#34;queryvaluedefinition.md&#34;&gt;QueryValueDefinition&lt;/a&gt;</i>
    <a href="#scatterplotdefinition" title="ScatterplotDefinition">ScatterplotDefinition</a>: <i>
      - &lt;a href=&#34;scatterplotdefinition.md&#34;&gt;ScatterplotDefinition&lt;/a&gt;</i>
    <a href="#servicelevelobjectivedefinition" title="ServiceLevelObjectiveDefinition">ServiceLevelObjectiveDefinition</a>: <i>
      - &lt;a href=&#34;servicelevelobjectivedefinition.md&#34;&gt;ServiceLevelObjectiveDefinition&lt;/a&gt;</i>
    <a href="#timeseriesdefinition" title="TimeseriesDefinition">TimeseriesDefinition</a>: <i>
      - &lt;a href=&#34;timeseriesdefinition.md&#34;&gt;TimeseriesDefinition&lt;/a&gt;</i>
    <a href="#toplistdefinition" title="ToplistDefinition">ToplistDefinition</a>: <i>
      - &lt;a href=&#34;toplistdefinition.md&#34;&gt;ToplistDefinition&lt;/a&gt;</i>
    <a href="#traceservicedefinition" title="TraceServiceDefinition">TraceServiceDefinition</a>: <i>
      - &lt;a href=&#34;traceservicedefinition.md&#34;&gt;TraceServiceDefinition&lt;/a&gt;</i>
    <a href="#request" title="Request">Request</a>: <i>
      - &lt;a href=&#34;request.md&#34;&gt;Request&lt;/a&gt;</i>
    <a href="#yaxis" title="Yaxis">Yaxis</a>: <i>
      - &lt;a href=&#34;yaxis.md&#34;&gt;Yaxis&lt;/a&gt;</i>
    <a href="#style" title="Style">Style</a>: <i>
      - &lt;a href=&#34;style.md&#34;&gt;Style&lt;/a&gt;</i>
    <a href="#xaxis" title="Xaxis">Xaxis</a>: <i>
      - &lt;a href=&#34;xaxis.md&#34;&gt;Xaxis&lt;/a&gt;</i>
    <a href="#event" title="Event">Event</a>: <i>
      - &lt;a href=&#34;event.md&#34;&gt;Event&lt;/a&gt;</i>
    <a href="#marker" title="Marker">Marker</a>: <i>
      - &lt;a href=&#34;marker.md&#34;&gt;Marker&lt;/a&gt;</i>
    <a href="#apmquery" title="ApmQuery">ApmQuery</a>: <i>
      - &lt;a href=&#34;apmquery.md&#34;&gt;ApmQuery&lt;/a&gt;</i>
    <a href="#conditionalformats" title="ConditionalFormats">ConditionalFormats</a>: <i>
      - &lt;a href=&#34;conditionalformats.md&#34;&gt;ConditionalFormats&lt;/a&gt;</i>
    <a href="#logquery" title="LogQuery">LogQuery</a>: <i>
      - &lt;a href=&#34;logquery.md&#34;&gt;LogQuery&lt;/a&gt;</i>
    <a href="#processquery" title="ProcessQuery">ProcessQuery</a>: <i>
      - &lt;a href=&#34;processquery.md&#34;&gt;ProcessQuery&lt;/a&gt;</i>
    <a href="#groupby" title="GroupBy">GroupBy</a>: <i>
      - &lt;a href=&#34;groupby.md&#34;&gt;GroupBy&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

_Type_: List of &lt;a href=&#34;templatevariable.md&#34;&gt;TemplateVariable&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateVariablePreset

_Required_: No

_Type_: List of &lt;a href=&#34;templatevariablepreset.md&#34;&gt;TemplateVariablePreset&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Widget

_Required_: No

_Type_: List of &lt;a href=&#34;widget.md&#34;&gt;Widget&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertGraphDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;alertgraphdefinition.md&#34;&gt;AlertGraphDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertValueDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;alertvaluedefinition.md&#34;&gt;AlertValueDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChangeDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;changedefinition.md&#34;&gt;ChangeDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckStatusDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;checkstatusdefinition.md&#34;&gt;CheckStatusDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributionDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;distributiondefinition.md&#34;&gt;DistributionDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventStreamDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;eventstreamdefinition.md&#34;&gt;EventStreamDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventTimelineDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;eventtimelinedefinition.md&#34;&gt;EventTimelineDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeTextDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;freetextdefinition.md&#34;&gt;FreeTextDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;groupdefinition.md&#34;&gt;GroupDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeatmapDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;heatmapdefinition.md&#34;&gt;HeatmapDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostmapDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;hostmapdefinition.md&#34;&gt;HostmapDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IframeDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;iframedefinition.md&#34;&gt;IframeDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;imagedefinition.md&#34;&gt;ImageDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogStreamDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;logstreamdefinition.md&#34;&gt;LogStreamDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageStatusDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;managestatusdefinition.md&#34;&gt;ManageStatusDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoteDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;notedefinition.md&#34;&gt;NoteDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryTableDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;querytabledefinition.md&#34;&gt;QueryTableDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryValueDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;queryvaluedefinition.md&#34;&gt;QueryValueDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScatterplotDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;scatterplotdefinition.md&#34;&gt;ScatterplotDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceLevelObjectiveDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;servicelevelobjectivedefinition.md&#34;&gt;ServiceLevelObjectiveDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeseriesDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;timeseriesdefinition.md&#34;&gt;TimeseriesDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToplistDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;toplistdefinition.md&#34;&gt;ToplistDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TraceServiceDefinition

_Required_: No

_Type_: List of &lt;a href=&#34;traceservicedefinition.md&#34;&gt;TraceServiceDefinition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Request

_Required_: No

_Type_: List of &lt;a href=&#34;request.md&#34;&gt;Request&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Yaxis

_Required_: No

_Type_: List of &lt;a href=&#34;yaxis.md&#34;&gt;Yaxis&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Style

_Required_: No

_Type_: List of &lt;a href=&#34;style.md&#34;&gt;Style&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Xaxis

_Required_: No

_Type_: List of &lt;a href=&#34;xaxis.md&#34;&gt;Xaxis&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Event

_Required_: No

_Type_: List of &lt;a href=&#34;event.md&#34;&gt;Event&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Marker

_Required_: No

_Type_: List of &lt;a href=&#34;marker.md&#34;&gt;Marker&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApmQuery

_Required_: No

_Type_: List of &lt;a href=&#34;apmquery.md&#34;&gt;ApmQuery&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionalFormats

_Required_: No

_Type_: List of &lt;a href=&#34;conditionalformats.md&#34;&gt;ConditionalFormats&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogQuery

_Required_: No

_Type_: List of &lt;a href=&#34;logquery.md&#34;&gt;LogQuery&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessQuery

_Required_: No

_Type_: List of &lt;a href=&#34;processquery.md&#34;&gt;ProcessQuery&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupBy

_Required_: No

_Type_: List of &lt;a href=&#34;groupby.md&#34;&gt;GroupBy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

