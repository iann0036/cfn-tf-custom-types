# TF::Datadog::Dashboard TimeseriesDefinitionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#legendcolumns" title="LegendColumns">LegendColumns</a>" : <i>[ String, ... ]</i>,
    "<a href="#legendlayout" title="LegendLayout">LegendLayout</a>" : <i>String</i>,
    "<a href="#legendsize" title="LegendSize">LegendSize</a>" : <i>String</i>,
    "<a href="#livespan" title="LiveSpan">LiveSpan</a>" : <i>String</i>,
    "<a href="#showlegend" title="ShowLegend">ShowLegend</a>" : <i>Boolean</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#titlealign" title="TitleAlign">TitleAlign</a>" : <i>String</i>,
    "<a href="#titlesize" title="TitleSize">TitleSize</a>" : <i>String</i>,
    "<a href="#customlink" title="CustomLink">CustomLink</a>" : <i>[ <a href="customlinkdefinition.md">CustomLinkDefinition</a>, ... ]</i>,
    "<a href="#event" title="Event">Event</a>" : <i>[ <a href="eventdefinition.md">EventDefinition</a>, ... ]</i>,
    "<a href="#marker" title="Marker">Marker</a>" : <i>[ <a href="markerdefinition.md">MarkerDefinition</a>, ... ]</i>,
    "<a href="#request" title="Request">Request</a>" : <i>[ <a href="requestdefinition.md">RequestDefinition</a>, ... ]</i>,
    "<a href="#rightyaxis" title="RightYaxis">RightYaxis</a>" : <i>[ <a href="rightyaxisdefinition.md">RightYaxisDefinition</a>, ... ]</i>,
    "<a href="#yaxis" title="Yaxis">Yaxis</a>" : <i>[ <a href="yaxisdefinition.md">YaxisDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#legendcolumns" title="LegendColumns">LegendColumns</a>: <i>
      - String</i>
<a href="#legendlayout" title="LegendLayout">LegendLayout</a>: <i>String</i>
<a href="#legendsize" title="LegendSize">LegendSize</a>: <i>String</i>
<a href="#livespan" title="LiveSpan">LiveSpan</a>: <i>String</i>
<a href="#showlegend" title="ShowLegend">ShowLegend</a>: <i>Boolean</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#titlealign" title="TitleAlign">TitleAlign</a>: <i>String</i>
<a href="#titlesize" title="TitleSize">TitleSize</a>: <i>String</i>
<a href="#customlink" title="CustomLink">CustomLink</a>: <i>
      - <a href="customlinkdefinition.md">CustomLinkDefinition</a></i>
<a href="#event" title="Event">Event</a>: <i>
      - <a href="eventdefinition.md">EventDefinition</a></i>
<a href="#marker" title="Marker">Marker</a>: <i>
      - <a href="markerdefinition.md">MarkerDefinition</a></i>
<a href="#request" title="Request">Request</a>: <i>
      - <a href="requestdefinition.md">RequestDefinition</a></i>
<a href="#rightyaxis" title="RightYaxis">RightYaxis</a>: <i>
      - <a href="rightyaxisdefinition.md">RightYaxisDefinition</a></i>
<a href="#yaxis" title="Yaxis">Yaxis</a>: <i>
      - <a href="yaxisdefinition.md">YaxisDefinition</a></i>
</pre>

## Properties

#### LegendColumns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LegendLayout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LegendSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LiveSpan

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowLegend

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TitleAlign

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TitleSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomLink

_Required_: No

_Type_: List of <a href="customlinkdefinition.md">CustomLinkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Event

_Required_: No

_Type_: List of <a href="eventdefinition.md">EventDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Marker

_Required_: No

_Type_: List of <a href="markerdefinition.md">MarkerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Request

_Required_: No

_Type_: List of <a href="requestdefinition.md">RequestDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RightYaxis

_Required_: No

_Type_: List of <a href="rightyaxisdefinition.md">RightYaxisDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Yaxis

_Required_: No

_Type_: List of <a href="yaxisdefinition.md">YaxisDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

