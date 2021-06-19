# TF::FortiOS::RouterOspf6 NeighborDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cost" title="Cost">Cost</a>" : <i>Double</i>,
    "<a href="#ip6" title="Ip6">Ip6</a>" : <i>String</i>,
    "<a href="#pollinterval" title="PollInterval">PollInterval</a>" : <i>Double</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#cost" title="Cost">Cost</a>: <i>Double</i>
<a href="#ip6" title="Ip6">Ip6</a>: <i>String</i>
<a href="#pollinterval" title="PollInterval">PollInterval</a>: <i>Double</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
</pre>

## Properties

#### Cost

Cost of the interface, value range from 0 to 65535, 0 means auto-cost.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6

IPv6 link local address of the neighbor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PollInterval

Poll interval time in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

priority.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

