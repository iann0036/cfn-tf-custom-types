# Terraform::Datadog::Dashboard Widget

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#layout" title="Layout">Layout</a>" : <i>[ <a href="widget-layout.md">Layout</a>, ... ]</i>,
    "<a href="#alertgraphdefinition" title="AlertGraphDefinition">AlertGraphDefinition</a>" : <i>[ <a href="widget-alertgraphdefinition.md">AlertGraphDefinition</a>, ... ]</i>,
    "<a href="#alertvaluedefinition" title="AlertValueDefinition">AlertValueDefinition</a>" : <i>[ <a href="widget-alertvaluedefinition.md">AlertValueDefinition</a>, ... ]</i>,
    "<a href="#changedefinition" title="ChangeDefinition">ChangeDefinition</a>" : <i>[ <a href="widget-changedefinition.md">ChangeDefinition</a>, ... ]</i>,
    "<a href="#checkstatusdefinition" title="CheckStatusDefinition">CheckStatusDefinition</a>" : <i>[ <a href="widget-checkstatusdefinition.md">CheckStatusDefinition</a>, ... ]</i>,
    "<a href="#distributiondefinition" title="DistributionDefinition">DistributionDefinition</a>" : <i>[ <a href="widget-distributiondefinition.md">DistributionDefinition</a>, ... ]</i>,
    "<a href="#eventstreamdefinition" title="EventStreamDefinition">EventStreamDefinition</a>" : <i>[ <a href="widget-eventstreamdefinition.md">EventStreamDefinition</a>, ... ]</i>,
    "<a href="#eventtimelinedefinition" title="EventTimelineDefinition">EventTimelineDefinition</a>" : <i>[ <a href="widget-eventtimelinedefinition.md">EventTimelineDefinition</a>, ... ]</i>,
    "<a href="#freetextdefinition" title="FreeTextDefinition">FreeTextDefinition</a>" : <i>[ <a href="widget-freetextdefinition.md">FreeTextDefinition</a>, ... ]</i>,
    "<a href="#heatmapdefinition" title="HeatmapDefinition">HeatmapDefinition</a>" : <i>[ <a href="widget-heatmapdefinition.md">HeatmapDefinition</a>, ... ]</i>,
    "<a href="#hostmapdefinition" title="HostmapDefinition">HostmapDefinition</a>" : <i>[ <a href="widget-hostmapdefinition.md">HostmapDefinition</a>, ... ]</i>,
    "<a href="#iframedefinition" title="IframeDefinition">IframeDefinition</a>" : <i>[ <a href="widget-iframedefinition.md">IframeDefinition</a>, ... ]</i>,
    "<a href="#imagedefinition" title="ImageDefinition">ImageDefinition</a>" : <i>[ <a href="widget-imagedefinition.md">ImageDefinition</a>, ... ]</i>,
    "<a href="#logstreamdefinition" title="LogStreamDefinition">LogStreamDefinition</a>" : <i>[ <a href="widget-logstreamdefinition.md">LogStreamDefinition</a>, ... ]</i>,
    "<a href="#managestatusdefinition" title="ManageStatusDefinition">ManageStatusDefinition</a>" : <i>[ <a href="widget-managestatusdefinition.md">ManageStatusDefinition</a>, ... ]</i>,
    "<a href="#notedefinition" title="NoteDefinition">NoteDefinition</a>" : <i>[ <a href="widget-notedefinition.md">NoteDefinition</a>, ... ]</i>,
    "<a href="#querytabledefinition" title="QueryTableDefinition">QueryTableDefinition</a>" : <i>[ <a href="widget-querytabledefinition.md">QueryTableDefinition</a>, ... ]</i>,
    "<a href="#queryvaluedefinition" title="QueryValueDefinition">QueryValueDefinition</a>" : <i>[ <a href="widget-queryvaluedefinition.md">QueryValueDefinition</a>, ... ]</i>,
    "<a href="#scatterplotdefinition" title="ScatterplotDefinition">ScatterplotDefinition</a>" : <i>[ <a href="widget-scatterplotdefinition.md">ScatterplotDefinition</a>, ... ]</i>,
    "<a href="#servicelevelobjectivedefinition" title="ServiceLevelObjectiveDefinition">ServiceLevelObjectiveDefinition</a>" : <i>[ <a href="widget-servicelevelobjectivedefinition.md">ServiceLevelObjectiveDefinition</a>, ... ]</i>,
    "<a href="#timeseriesdefinition" title="TimeseriesDefinition">TimeseriesDefinition</a>" : <i>[ <a href="widget-timeseriesdefinition.md">TimeseriesDefinition</a>, ... ]</i>,
    "<a href="#toplistdefinition" title="ToplistDefinition">ToplistDefinition</a>" : <i>[ <a href="widget-toplistdefinition.md">ToplistDefinition</a>, ... ]</i>,
    "<a href="#traceservicedefinition" title="TraceServiceDefinition">TraceServiceDefinition</a>" : <i>[ <a href="widget-traceservicedefinition.md">TraceServiceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#layout" title="Layout">Layout</a>: <i>
      - <a href="widget-layout.md">Layout</a></i>
<a href="#alertgraphdefinition" title="AlertGraphDefinition">AlertGraphDefinition</a>: <i>
      - <a href="widget-alertgraphdefinition.md">AlertGraphDefinition</a></i>
<a href="#alertvaluedefinition" title="AlertValueDefinition">AlertValueDefinition</a>: <i>
      - <a href="widget-alertvaluedefinition.md">AlertValueDefinition</a></i>
<a href="#changedefinition" title="ChangeDefinition">ChangeDefinition</a>: <i>
      - <a href="widget-changedefinition.md">ChangeDefinition</a></i>
<a href="#checkstatusdefinition" title="CheckStatusDefinition">CheckStatusDefinition</a>: <i>
      - <a href="widget-checkstatusdefinition.md">CheckStatusDefinition</a></i>
<a href="#distributiondefinition" title="DistributionDefinition">DistributionDefinition</a>: <i>
      - <a href="widget-distributiondefinition.md">DistributionDefinition</a></i>
<a href="#eventstreamdefinition" title="EventStreamDefinition">EventStreamDefinition</a>: <i>
      - <a href="widget-eventstreamdefinition.md">EventStreamDefinition</a></i>
<a href="#eventtimelinedefinition" title="EventTimelineDefinition">EventTimelineDefinition</a>: <i>
      - <a href="widget-eventtimelinedefinition.md">EventTimelineDefinition</a></i>
<a href="#freetextdefinition" title="FreeTextDefinition">FreeTextDefinition</a>: <i>
      - <a href="widget-freetextdefinition.md">FreeTextDefinition</a></i>
<a href="#heatmapdefinition" title="HeatmapDefinition">HeatmapDefinition</a>: <i>
      - <a href="widget-heatmapdefinition.md">HeatmapDefinition</a></i>
<a href="#hostmapdefinition" title="HostmapDefinition">HostmapDefinition</a>: <i>
      - <a href="widget-hostmapdefinition.md">HostmapDefinition</a></i>
<a href="#iframedefinition" title="IframeDefinition">IframeDefinition</a>: <i>
      - <a href="widget-iframedefinition.md">IframeDefinition</a></i>
<a href="#imagedefinition" title="ImageDefinition">ImageDefinition</a>: <i>
      - <a href="widget-imagedefinition.md">ImageDefinition</a></i>
<a href="#logstreamdefinition" title="LogStreamDefinition">LogStreamDefinition</a>: <i>
      - <a href="widget-logstreamdefinition.md">LogStreamDefinition</a></i>
<a href="#managestatusdefinition" title="ManageStatusDefinition">ManageStatusDefinition</a>: <i>
      - <a href="widget-managestatusdefinition.md">ManageStatusDefinition</a></i>
<a href="#notedefinition" title="NoteDefinition">NoteDefinition</a>: <i>
      - <a href="widget-notedefinition.md">NoteDefinition</a></i>
<a href="#querytabledefinition" title="QueryTableDefinition">QueryTableDefinition</a>: <i>
      - <a href="widget-querytabledefinition.md">QueryTableDefinition</a></i>
<a href="#queryvaluedefinition" title="QueryValueDefinition">QueryValueDefinition</a>: <i>
      - <a href="widget-queryvaluedefinition.md">QueryValueDefinition</a></i>
<a href="#scatterplotdefinition" title="ScatterplotDefinition">ScatterplotDefinition</a>: <i>
      - <a href="widget-scatterplotdefinition.md">ScatterplotDefinition</a></i>
<a href="#servicelevelobjectivedefinition" title="ServiceLevelObjectiveDefinition">ServiceLevelObjectiveDefinition</a>: <i>
      - <a href="widget-servicelevelobjectivedefinition.md">ServiceLevelObjectiveDefinition</a></i>
<a href="#timeseriesdefinition" title="TimeseriesDefinition">TimeseriesDefinition</a>: <i>
      - <a href="widget-timeseriesdefinition.md">TimeseriesDefinition</a></i>
<a href="#toplistdefinition" title="ToplistDefinition">ToplistDefinition</a>: <i>
      - <a href="widget-toplistdefinition.md">ToplistDefinition</a></i>
<a href="#traceservicedefinition" title="TraceServiceDefinition">TraceServiceDefinition</a>: <i>
      - <a href="widget-traceservicedefinition.md">TraceServiceDefinition</a></i>
</pre>

## Properties

#### Layout

_Required_: No

_Type_: List of <a href="widget-layout.md">Layout</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertGraphDefinition

_Required_: No

_Type_: List of <a href="widget-alertgraphdefinition.md">AlertGraphDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertValueDefinition

_Required_: No

_Type_: List of <a href="widget-alertvaluedefinition.md">AlertValueDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChangeDefinition

_Required_: No

_Type_: List of <a href="widget-changedefinition.md">ChangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckStatusDefinition

_Required_: No

_Type_: List of <a href="widget-checkstatusdefinition.md">CheckStatusDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributionDefinition

_Required_: No

_Type_: List of <a href="widget-distributiondefinition.md">DistributionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventStreamDefinition

_Required_: No

_Type_: List of <a href="widget-eventstreamdefinition.md">EventStreamDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventTimelineDefinition

_Required_: No

_Type_: List of <a href="widget-eventtimelinedefinition.md">EventTimelineDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeTextDefinition

_Required_: No

_Type_: List of <a href="widget-freetextdefinition.md">FreeTextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeatmapDefinition

_Required_: No

_Type_: List of <a href="widget-heatmapdefinition.md">HeatmapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostmapDefinition

_Required_: No

_Type_: List of <a href="widget-hostmapdefinition.md">HostmapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IframeDefinition

_Required_: No

_Type_: List of <a href="widget-iframedefinition.md">IframeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageDefinition

_Required_: No

_Type_: List of <a href="widget-imagedefinition.md">ImageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogStreamDefinition

_Required_: No

_Type_: List of <a href="widget-logstreamdefinition.md">LogStreamDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageStatusDefinition

_Required_: No

_Type_: List of <a href="widget-managestatusdefinition.md">ManageStatusDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoteDefinition

_Required_: No

_Type_: List of <a href="widget-notedefinition.md">NoteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryTableDefinition

_Required_: No

_Type_: List of <a href="widget-querytabledefinition.md">QueryTableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryValueDefinition

_Required_: No

_Type_: List of <a href="widget-queryvaluedefinition.md">QueryValueDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScatterplotDefinition

_Required_: No

_Type_: List of <a href="widget-scatterplotdefinition.md">ScatterplotDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceLevelObjectiveDefinition

_Required_: No

_Type_: List of <a href="widget-servicelevelobjectivedefinition.md">ServiceLevelObjectiveDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeseriesDefinition

_Required_: No

_Type_: List of <a href="widget-timeseriesdefinition.md">TimeseriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToplistDefinition

_Required_: No

_Type_: List of <a href="widget-toplistdefinition.md">ToplistDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TraceServiceDefinition

_Required_: No

_Type_: List of <a href="widget-traceservicedefinition.md">TraceServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

