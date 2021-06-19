# TF::FortiOS::FirewallInternetservicedefinition EntryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#categoryid" title="CategoryId">CategoryId</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>Double</i>,
    "<a href="#seqnum" title="SeqNum">SeqNum</a>" : <i>Double</i>,
    "<a href="#portrange" title="PortRange">PortRange</a>" : <i>[ <a href="portrangedefinition.md">PortRangeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#categoryid" title="CategoryId">CategoryId</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>Double</i>
<a href="#seqnum" title="SeqNum">SeqNum</a>: <i>Double</i>
<a href="#portrange" title="PortRange">PortRange</a>: <i>
      - <a href="portrangedefinition.md">PortRangeDefinition</a></i>
</pre>

## Properties

#### CategoryId

Internet Service category ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Internet Service name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Integer value for ending TCP/UDP/SCTP destination port in range (0 to 65535). 0 means undefined.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Integer value for the protocol type as defined by IANA (0 - 255).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeqNum

Entry sequence number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortRange

_Required_: No

_Type_: List of <a href="portrangedefinition.md">PortRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

