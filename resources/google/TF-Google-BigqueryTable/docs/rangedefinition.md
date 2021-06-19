# TF::Google::BigqueryTable RangeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#end" title="End">End</a>" : <i>Double</i>,
    "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
    "<a href="#start" title="Start">Start</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#end" title="End">End</a>: <i>Double</i>
<a href="#interval" title="Interval">Interval</a>: <i>Double</i>
<a href="#start" title="Start">Start</a>: <i>Double</i>
</pre>

## Properties

#### End

End of the range partitioning, exclusive.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

The width of each range within the partition.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Start

Start of the range partitioning, inclusive.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

