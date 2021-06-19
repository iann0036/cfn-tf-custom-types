# TF::FortiOS::WirelesscontrollerIntercontroller InterControllerPeerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#peerip" title="PeerIp">PeerIp</a>" : <i>String</i>,
    "<a href="#peerport" title="PeerPort">PeerPort</a>" : <i>Double</i>,
    "<a href="#peerpriority" title="PeerPriority">PeerPriority</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#peerip" title="PeerIp">PeerIp</a>: <i>String</i>
<a href="#peerport" title="PeerPort">PeerPort</a>: <i>Double</i>
<a href="#peerpriority" title="PeerPriority">PeerPriority</a>: <i>String</i>
</pre>

## Properties

#### Id

ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerIp

Peer wireless controller's IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerPort

Port used by the wireless controller's for inter-controller communications (1024 - 49150, default = 5246).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerPriority

Peer wireless controller's priority (primary or secondary, default = primary). Valid values: `primary`, `secondary`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

