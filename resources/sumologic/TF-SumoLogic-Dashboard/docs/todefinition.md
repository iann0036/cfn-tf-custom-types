# TF::SumoLogic::Dashboard ToDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#epochtimerange" title="EpochTimeRange">EpochTimeRange</a>" : <i>[ <a href="epochtimerangedefinition.md">EpochTimeRangeDefinition</a>, ... ]</i>,
    "<a href="#iso8601timerange" title="Iso8601TimeRange">Iso8601TimeRange</a>" : <i>[ <a href="iso8601timerangedefinition.md">Iso8601TimeRangeDefinition</a>, ... ]</i>,
    "<a href="#literaltimerange" title="LiteralTimeRange">LiteralTimeRange</a>" : <i>[ <a href="literaltimerangedefinition.md">LiteralTimeRangeDefinition</a>, ... ]</i>,
    "<a href="#relativetimerange" title="RelativeTimeRange">RelativeTimeRange</a>" : <i>[ <a href="relativetimerangedefinition.md">RelativeTimeRangeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#epochtimerange" title="EpochTimeRange">EpochTimeRange</a>: <i>
      - <a href="epochtimerangedefinition.md">EpochTimeRangeDefinition</a></i>
<a href="#iso8601timerange" title="Iso8601TimeRange">Iso8601TimeRange</a>: <i>
      - <a href="iso8601timerangedefinition.md">Iso8601TimeRangeDefinition</a></i>
<a href="#literaltimerange" title="LiteralTimeRange">LiteralTimeRange</a>: <i>
      - <a href="literaltimerangedefinition.md">LiteralTimeRangeDefinition</a></i>
<a href="#relativetimerange" title="RelativeTimeRange">RelativeTimeRange</a>: <i>
      - <a href="relativetimerangedefinition.md">RelativeTimeRangeDefinition</a></i>
</pre>

## Properties

#### EpochTimeRange

_Required_: No

_Type_: List of <a href="epochtimerangedefinition.md">EpochTimeRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iso8601TimeRange

_Required_: No

_Type_: List of <a href="iso8601timerangedefinition.md">Iso8601TimeRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LiteralTimeRange

_Required_: No

_Type_: List of <a href="literaltimerangedefinition.md">LiteralTimeRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelativeTimeRange

_Required_: No

_Type_: List of <a href="relativetimerangedefinition.md">RelativeTimeRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

