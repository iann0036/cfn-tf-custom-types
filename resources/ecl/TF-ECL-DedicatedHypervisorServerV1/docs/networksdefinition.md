# TF::ECL::DedicatedHypervisorServerV1 NetworksDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fixedip" title="FixedIp">FixedIp</a>" : <i>String</i>,
    "<a href="#plane" title="Plane">Plane</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>String</i>,
    "<a href="#segmentationid" title="SegmentationId">SegmentationId</a>" : <i>Double</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#fixedip" title="FixedIp">FixedIp</a>: <i>String</i>
<a href="#plane" title="Plane">Plane</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>String</i>
<a href="#segmentationid" title="SegmentationId">SegmentationId</a>: <i>Double</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### FixedIp

Specifies a fixed IPv4 address to be used on this network.
Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plane

The traffic type of a network to attach to the server. `data` and `storage` are supported.
Changing this creates a new server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port UUID of a network to attach to the server.
Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegmentationId

The segmentation ID of a network to attach to the server.
This value is integer, no less than 4 and no more than 4093. Changing this creates a new server.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

The network UUID to attach to the server.
Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

