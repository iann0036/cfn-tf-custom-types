# Terraform::Datadog::Dashboard TimeseriesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#legendsize" title="LegendSize">LegendSize</a>" : <i>String</i>,
    "<a href="#showlegend" title="ShowLegend">ShowLegend</a>" : <i>Boolean</i>,
    "<a href="#time" title="Time">Time</a>" : <i>[ <a href="timeseriesdefinition-time.md">Time</a>, ... ]</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#titlealign" title="TitleAlign">TitleAlign</a>" : <i>String</i>,
    "<a href="#titlesize" title="TitleSize">TitleSize</a>" : <i>String</i>,
    "<a href="#event" title="Event">Event</a>" : <i>[ <a href="timeseriesdefinition-event.md">Event</a>, ... ]</i>,
    "<a href="#marker" title="Marker">Marker</a>" : <i>[ <a href="timeseriesdefinition-marker.md">Marker</a>, ... ]</i>,
    "<a href="#request" title="Request">Request</a>" : <i>[ <a href="timeseriesdefinition-request.md">Request</a>, ... ]</i>,
    "<a href="#yaxis" title="Yaxis">Yaxis</a>" : <i>[ <a href="timeseriesdefinition-yaxis.md">Yaxis</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#legendsize" title="LegendSize">LegendSize</a>: <i>String</i>
<a href="#showlegend" title="ShowLegend">ShowLegend</a>: <i>Boolean</i>
<a href="#time" title="Time">Time</a>: <i>
      - <a href="timeseriesdefinition-time.md">Time</a></i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#titlealign" title="TitleAlign">TitleAlign</a>: <i>String</i>
<a href="#titlesize" title="TitleSize">TitleSize</a>: <i>String</i>
<a href="#event" title="Event">Event</a>: <i>
      - <a href="timeseriesdefinition-event.md">Event</a></i>
<a href="#marker" title="Marker">Marker</a>: <i>
      - <a href="timeseriesdefinition-marker.md">Marker</a></i>
<a href="#request" title="Request">Request</a>: <i>
      - <a href="timeseriesdefinition-request.md">Request</a></i>
<a href="#yaxis" title="Yaxis">Yaxis</a>: <i>
      - <a href="timeseriesdefinition-yaxis.md">Yaxis</a></i>
</pre>

## Properties

#### LegendSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowLegend

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Time

_Required_: No

_Type_: List of <a href="timeseriesdefinition-time.md">Time</a>

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

#### Event

_Required_: No

_Type_: List of <a href="timeseriesdefinition-event.md">Event</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Marker

_Required_: No

_Type_: List of <a href="timeseriesdefinition-marker.md">Marker</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Request

_Required_: No

_Type_: List of <a href="timeseriesdefinition-request.md">Request</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Yaxis

_Required_: No

_Type_: List of <a href="timeseriesdefinition-yaxis.md">Yaxis</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

