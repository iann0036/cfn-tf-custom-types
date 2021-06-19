# TF::SignalFx::EventFeedChart

Displays a listing of events as a widget in a dashboard.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SignalFx::EventFeedChart",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#endtime" title="EndTime">EndTime</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#programtext" title="ProgramText">ProgramText</a>" : <i>String</i>,
        "<a href="#starttime" title="StartTime">StartTime</a>" : <i>Double</i>,
        "<a href="#timerange" title="TimeRange">TimeRange</a>" : <i>Double</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::SignalFx::EventFeedChart
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#endtime" title="EndTime">EndTime</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#programtext" title="ProgramText">ProgramText</a>: <i>String</i>
    <a href="#starttime" title="StartTime">StartTime</a>: <i>Double</i>
    <a href="#timerange" title="TimeRange">TimeRange</a>: <i>Double</i>
</pre>

## Properties

#### Description

Description of the text note.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndTime

Seconds since epoch. Used for visualization. Conflicts with `time_range`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the text note.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProgramText

Signalflow program text for the chart. More info[in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

Seconds since epoch. Used for visualization. Conflicts with `time_range`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeRange

From when to display data. SignalFx time syntax (e.g. `"-5m"`, `"-1h"`). Conflicts with `start_time` and `end_time`.

_Required_: No

_Type_: Double

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

