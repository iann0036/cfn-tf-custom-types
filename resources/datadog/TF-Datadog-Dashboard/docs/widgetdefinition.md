# TF::Datadog::Dashboard WidgetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alertgraphdefinition" title="AlertGraphDefinition">AlertGraphDefinition</a>" : <i>[ <a href="alertgraphdefinitiondefinition.md">AlertGraphDefinitionDefinition</a>, ... ]</i>,
    "<a href="#alertvaluedefinition" title="AlertValueDefinition">AlertValueDefinition</a>" : <i>[ <a href="alertvaluedefinitiondefinition.md">AlertValueDefinitionDefinition</a>, ... ]</i>,
    "<a href="#changedefinition" title="ChangeDefinition">ChangeDefinition</a>" : <i>[ <a href="changedefinitiondefinition.md">ChangeDefinitionDefinition</a>, ... ]</i>,
    "<a href="#checkstatusdefinition" title="CheckStatusDefinition">CheckStatusDefinition</a>" : <i>[ <a href="checkstatusdefinitiondefinition.md">CheckStatusDefinitionDefinition</a>, ... ]</i>,
    "<a href="#distributiondefinition" title="DistributionDefinition">DistributionDefinition</a>" : <i>[ <a href="distributiondefinitiondefinition.md">DistributionDefinitionDefinition</a>, ... ]</i>,
    "<a href="#eventstreamdefinition" title="EventStreamDefinition">EventStreamDefinition</a>" : <i>[ <a href="eventstreamdefinitiondefinition.md">EventStreamDefinitionDefinition</a>, ... ]</i>,
    "<a href="#eventtimelinedefinition" title="EventTimelineDefinition">EventTimelineDefinition</a>" : <i>[ <a href="eventtimelinedefinitiondefinition.md">EventTimelineDefinitionDefinition</a>, ... ]</i>,
    "<a href="#freetextdefinition" title="FreeTextDefinition">FreeTextDefinition</a>" : <i>[ <a href="freetextdefinitiondefinition.md">FreeTextDefinitionDefinition</a>, ... ]</i>,
    "<a href="#geomapdefinition" title="GeomapDefinition">GeomapDefinition</a>" : <i>[ <a href="geomapdefinitiondefinition.md">GeomapDefinitionDefinition</a>, ... ]</i>,
    "<a href="#heatmapdefinition" title="HeatmapDefinition">HeatmapDefinition</a>" : <i>[ <a href="heatmapdefinitiondefinition.md">HeatmapDefinitionDefinition</a>, ... ]</i>,
    "<a href="#hostmapdefinition" title="HostmapDefinition">HostmapDefinition</a>" : <i>[ <a href="hostmapdefinitiondefinition.md">HostmapDefinitionDefinition</a>, ... ]</i>,
    "<a href="#iframedefinition" title="IframeDefinition">IframeDefinition</a>" : <i>[ <a href="iframedefinitiondefinition.md">IframeDefinitionDefinition</a>, ... ]</i>,
    "<a href="#imagedefinition" title="ImageDefinition">ImageDefinition</a>" : <i>[ <a href="imagedefinitiondefinition.md">ImageDefinitionDefinition</a>, ... ]</i>,
    "<a href="#logstreamdefinition" title="LogStreamDefinition">LogStreamDefinition</a>" : <i>[ <a href="logstreamdefinitiondefinition.md">LogStreamDefinitionDefinition</a>, ... ]</i>,
    "<a href="#managestatusdefinition" title="ManageStatusDefinition">ManageStatusDefinition</a>" : <i>[ <a href="managestatusdefinitiondefinition.md">ManageStatusDefinitionDefinition</a>, ... ]</i>,
    "<a href="#notedefinition" title="NoteDefinition">NoteDefinition</a>" : <i>[ <a href="notedefinitiondefinition.md">NoteDefinitionDefinition</a>, ... ]</i>,
    "<a href="#querytabledefinition" title="QueryTableDefinition">QueryTableDefinition</a>" : <i>[ <a href="querytabledefinitiondefinition.md">QueryTableDefinitionDefinition</a>, ... ]</i>,
    "<a href="#queryvaluedefinition" title="QueryValueDefinition">QueryValueDefinition</a>" : <i>[ <a href="queryvaluedefinitiondefinition.md">QueryValueDefinitionDefinition</a>, ... ]</i>,
    "<a href="#scatterplotdefinition" title="ScatterplotDefinition">ScatterplotDefinition</a>" : <i>[ <a href="scatterplotdefinitiondefinition.md">ScatterplotDefinitionDefinition</a>, ... ]</i>,
    "<a href="#servicelevelobjectivedefinition" title="ServiceLevelObjectiveDefinition">ServiceLevelObjectiveDefinition</a>" : <i>[ <a href="servicelevelobjectivedefinitiondefinition.md">ServiceLevelObjectiveDefinitionDefinition</a>, ... ]</i>,
    "<a href="#servicemapdefinition" title="ServicemapDefinition">ServicemapDefinition</a>" : <i>[ <a href="servicemapdefinitiondefinition.md">ServicemapDefinitionDefinition</a>, ... ]</i>,
    "<a href="#timeseriesdefinition" title="TimeseriesDefinition">TimeseriesDefinition</a>" : <i>[ <a href="timeseriesdefinitiondefinition.md">TimeseriesDefinitionDefinition</a>, ... ]</i>,
    "<a href="#toplistdefinition" title="ToplistDefinition">ToplistDefinition</a>" : <i>[ <a href="toplistdefinitiondefinition.md">ToplistDefinitionDefinition</a>, ... ]</i>,
    "<a href="#traceservicedefinition" title="TraceServiceDefinition">TraceServiceDefinition</a>" : <i>[ <a href="traceservicedefinitiondefinition.md">TraceServiceDefinitionDefinition</a>, ... ]</i>,
    "<a href="#widgetlayout" title="WidgetLayout">WidgetLayout</a>" : <i>[ <a href="widgetlayoutdefinition.md">WidgetLayoutDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alertgraphdefinition" title="AlertGraphDefinition">AlertGraphDefinition</a>: <i>
      - <a href="alertgraphdefinitiondefinition.md">AlertGraphDefinitionDefinition</a></i>
<a href="#alertvaluedefinition" title="AlertValueDefinition">AlertValueDefinition</a>: <i>
      - <a href="alertvaluedefinitiondefinition.md">AlertValueDefinitionDefinition</a></i>
<a href="#changedefinition" title="ChangeDefinition">ChangeDefinition</a>: <i>
      - <a href="changedefinitiondefinition.md">ChangeDefinitionDefinition</a></i>
<a href="#checkstatusdefinition" title="CheckStatusDefinition">CheckStatusDefinition</a>: <i>
      - <a href="checkstatusdefinitiondefinition.md">CheckStatusDefinitionDefinition</a></i>
<a href="#distributiondefinition" title="DistributionDefinition">DistributionDefinition</a>: <i>
      - <a href="distributiondefinitiondefinition.md">DistributionDefinitionDefinition</a></i>
<a href="#eventstreamdefinition" title="EventStreamDefinition">EventStreamDefinition</a>: <i>
      - <a href="eventstreamdefinitiondefinition.md">EventStreamDefinitionDefinition</a></i>
<a href="#eventtimelinedefinition" title="EventTimelineDefinition">EventTimelineDefinition</a>: <i>
      - <a href="eventtimelinedefinitiondefinition.md">EventTimelineDefinitionDefinition</a></i>
<a href="#freetextdefinition" title="FreeTextDefinition">FreeTextDefinition</a>: <i>
      - <a href="freetextdefinitiondefinition.md">FreeTextDefinitionDefinition</a></i>
<a href="#geomapdefinition" title="GeomapDefinition">GeomapDefinition</a>: <i>
      - <a href="geomapdefinitiondefinition.md">GeomapDefinitionDefinition</a></i>
<a href="#heatmapdefinition" title="HeatmapDefinition">HeatmapDefinition</a>: <i>
      - <a href="heatmapdefinitiondefinition.md">HeatmapDefinitionDefinition</a></i>
<a href="#hostmapdefinition" title="HostmapDefinition">HostmapDefinition</a>: <i>
      - <a href="hostmapdefinitiondefinition.md">HostmapDefinitionDefinition</a></i>
<a href="#iframedefinition" title="IframeDefinition">IframeDefinition</a>: <i>
      - <a href="iframedefinitiondefinition.md">IframeDefinitionDefinition</a></i>
<a href="#imagedefinition" title="ImageDefinition">ImageDefinition</a>: <i>
      - <a href="imagedefinitiondefinition.md">ImageDefinitionDefinition</a></i>
<a href="#logstreamdefinition" title="LogStreamDefinition">LogStreamDefinition</a>: <i>
      - <a href="logstreamdefinitiondefinition.md">LogStreamDefinitionDefinition</a></i>
<a href="#managestatusdefinition" title="ManageStatusDefinition">ManageStatusDefinition</a>: <i>
      - <a href="managestatusdefinitiondefinition.md">ManageStatusDefinitionDefinition</a></i>
<a href="#notedefinition" title="NoteDefinition">NoteDefinition</a>: <i>
      - <a href="notedefinitiondefinition.md">NoteDefinitionDefinition</a></i>
<a href="#querytabledefinition" title="QueryTableDefinition">QueryTableDefinition</a>: <i>
      - <a href="querytabledefinitiondefinition.md">QueryTableDefinitionDefinition</a></i>
<a href="#queryvaluedefinition" title="QueryValueDefinition">QueryValueDefinition</a>: <i>
      - <a href="queryvaluedefinitiondefinition.md">QueryValueDefinitionDefinition</a></i>
<a href="#scatterplotdefinition" title="ScatterplotDefinition">ScatterplotDefinition</a>: <i>
      - <a href="scatterplotdefinitiondefinition.md">ScatterplotDefinitionDefinition</a></i>
<a href="#servicelevelobjectivedefinition" title="ServiceLevelObjectiveDefinition">ServiceLevelObjectiveDefinition</a>: <i>
      - <a href="servicelevelobjectivedefinitiondefinition.md">ServiceLevelObjectiveDefinitionDefinition</a></i>
<a href="#servicemapdefinition" title="ServicemapDefinition">ServicemapDefinition</a>: <i>
      - <a href="servicemapdefinitiondefinition.md">ServicemapDefinitionDefinition</a></i>
<a href="#timeseriesdefinition" title="TimeseriesDefinition">TimeseriesDefinition</a>: <i>
      - <a href="timeseriesdefinitiondefinition.md">TimeseriesDefinitionDefinition</a></i>
<a href="#toplistdefinition" title="ToplistDefinition">ToplistDefinition</a>: <i>
      - <a href="toplistdefinitiondefinition.md">ToplistDefinitionDefinition</a></i>
<a href="#traceservicedefinition" title="TraceServiceDefinition">TraceServiceDefinition</a>: <i>
      - <a href="traceservicedefinitiondefinition.md">TraceServiceDefinitionDefinition</a></i>
<a href="#widgetlayout" title="WidgetLayout">WidgetLayout</a>: <i>
      - <a href="widgetlayoutdefinition.md">WidgetLayoutDefinition</a></i>
</pre>

## Properties

#### AlertGraphDefinition

_Required_: No

_Type_: List of <a href="alertgraphdefinitiondefinition.md">AlertGraphDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertValueDefinition

_Required_: No

_Type_: List of <a href="alertvaluedefinitiondefinition.md">AlertValueDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChangeDefinition

_Required_: No

_Type_: List of <a href="changedefinitiondefinition.md">ChangeDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckStatusDefinition

_Required_: No

_Type_: List of <a href="checkstatusdefinitiondefinition.md">CheckStatusDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributionDefinition

_Required_: No

_Type_: List of <a href="distributiondefinitiondefinition.md">DistributionDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventStreamDefinition

_Required_: No

_Type_: List of <a href="eventstreamdefinitiondefinition.md">EventStreamDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventTimelineDefinition

_Required_: No

_Type_: List of <a href="eventtimelinedefinitiondefinition.md">EventTimelineDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeTextDefinition

_Required_: No

_Type_: List of <a href="freetextdefinitiondefinition.md">FreeTextDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeomapDefinition

_Required_: No

_Type_: List of <a href="geomapdefinitiondefinition.md">GeomapDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeatmapDefinition

_Required_: No

_Type_: List of <a href="heatmapdefinitiondefinition.md">HeatmapDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostmapDefinition

_Required_: No

_Type_: List of <a href="hostmapdefinitiondefinition.md">HostmapDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IframeDefinition

_Required_: No

_Type_: List of <a href="iframedefinitiondefinition.md">IframeDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageDefinition

_Required_: No

_Type_: List of <a href="imagedefinitiondefinition.md">ImageDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogStreamDefinition

_Required_: No

_Type_: List of <a href="logstreamdefinitiondefinition.md">LogStreamDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageStatusDefinition

_Required_: No

_Type_: List of <a href="managestatusdefinitiondefinition.md">ManageStatusDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoteDefinition

_Required_: No

_Type_: List of <a href="notedefinitiondefinition.md">NoteDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryTableDefinition

_Required_: No

_Type_: List of <a href="querytabledefinitiondefinition.md">QueryTableDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryValueDefinition

_Required_: No

_Type_: List of <a href="queryvaluedefinitiondefinition.md">QueryValueDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScatterplotDefinition

_Required_: No

_Type_: List of <a href="scatterplotdefinitiondefinition.md">ScatterplotDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceLevelObjectiveDefinition

_Required_: No

_Type_: List of <a href="servicelevelobjectivedefinitiondefinition.md">ServiceLevelObjectiveDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicemapDefinition

_Required_: No

_Type_: List of <a href="servicemapdefinitiondefinition.md">ServicemapDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeseriesDefinition

_Required_: No

_Type_: List of <a href="timeseriesdefinitiondefinition.md">TimeseriesDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToplistDefinition

_Required_: No

_Type_: List of <a href="toplistdefinitiondefinition.md">ToplistDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TraceServiceDefinition

_Required_: No

_Type_: List of <a href="traceservicedefinitiondefinition.md">TraceServiceDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidgetLayout

_Required_: No

_Type_: List of <a href="widgetlayoutdefinition.md">WidgetLayoutDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

