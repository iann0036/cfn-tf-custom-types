# TF::FortiOS::SystemSdwan SlaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#jitterthreshold" title="JitterThreshold">JitterThreshold</a>" : <i>Double</i>,
    "<a href="#latencythreshold" title="LatencyThreshold">LatencyThreshold</a>" : <i>Double</i>,
    "<a href="#linkcostfactor" title="LinkCostFactor">LinkCostFactor</a>" : <i>String</i>,
    "<a href="#packetlossthreshold" title="PacketlossThreshold">PacketlossThreshold</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#jitterthreshold" title="JitterThreshold">JitterThreshold</a>: <i>Double</i>
<a href="#latencythreshold" title="LatencyThreshold">LatencyThreshold</a>: <i>Double</i>
<a href="#linkcostfactor" title="LinkCostFactor">LinkCostFactor</a>: <i>String</i>
<a href="#packetlossthreshold" title="PacketlossThreshold">PacketlossThreshold</a>: <i>Double</i>
</pre>

## Properties

#### Id

SLA ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JitterThreshold

Jitter for SLA to make decision in milliseconds. (0 - 10000000, default = 5).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LatencyThreshold

Latency for SLA to make decision in milliseconds. (0 - 10000000, default = 5).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkCostFactor

Criteria on which to base link selection. Valid values: `latency`, `jitter`, `packet-loss`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketlossThreshold

Packet loss for SLA to make decision in percentage. (0 - 100, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

