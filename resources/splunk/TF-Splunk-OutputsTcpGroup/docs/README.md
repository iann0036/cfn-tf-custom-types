# TF::Splunk::OutputsTcpGroup

Access to the configuration of a group of one or more data forwarding destinations.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Splunk::OutputsTcpGroup",
    "Properties" : {
        "<a href="#compressed" title="Compressed">Compressed</a>" : <i>Boolean</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#dropeventsonqueuefull" title="DropEventsOnQueueFull">DropEventsOnQueueFull</a>" : <i>Double</i>,
        "<a href="#heartbeatfrequency" title="HeartbeatFrequency">HeartbeatFrequency</a>" : <i>Double</i>,
        "<a href="#maxqueuesize" title="MaxQueueSize">MaxQueueSize</a>" : <i>String</i>,
        "<a href="#method" title="Method">Method</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sendcookeddata" title="SendCookedData">SendCookedData</a>" : <i>Boolean</i>,
        "<a href="#servers" title="Servers">Servers</a>" : <i>[ String, ... ]</i>,
        "<a href="#token" title="Token">Token</a>" : <i>String</i>,
        "<a href="#acl" title="Acl">Acl</a>" : <i>[ <a href="acldefinition.md">AclDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Splunk::OutputsTcpGroup
Properties:
    <a href="#compressed" title="Compressed">Compressed</a>: <i>Boolean</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#dropeventsonqueuefull" title="DropEventsOnQueueFull">DropEventsOnQueueFull</a>: <i>Double</i>
    <a href="#heartbeatfrequency" title="HeartbeatFrequency">HeartbeatFrequency</a>: <i>Double</i>
    <a href="#maxqueuesize" title="MaxQueueSize">MaxQueueSize</a>: <i>String</i>
    <a href="#method" title="Method">Method</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sendcookeddata" title="SendCookedData">SendCookedData</a>: <i>Boolean</i>
    <a href="#servers" title="Servers">Servers</a>: <i>
      - String</i>
    <a href="#token" title="Token">Token</a>: <i>String</i>
    <a href="#acl" title="Acl">Acl</a>: <i>
      - <a href="acldefinition.md">AclDefinition</a></i>
</pre>

## Properties

#### Compressed

If true, forwarder sends compressed data. If set to true, the receiver port must also have compression turned on.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

If true, disables the group.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropEventsOnQueueFull

If set to a positive number, wait the specified number of seconds before throwing out all new events until the output queue has space. Defaults to -1 (do not drop events).
<br>CAUTION: Do not set this value to a positive integer if you are monitoring files.
Setting this to -1 or 0 causes the output queue to block when it gets full, which causes further blocking up the processing chain. If any target group queue is blocked, no more data reaches any other target group.
Using auto load-balancing is the best way to minimize this condition, because, in that case, multiple receivers must be down (or jammed up) before queue blocking can occur.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeartbeatFrequency

How often (in seconds) to send a heartbeat packet to the receiving server.
Heartbeats are only sent if sendCookedData=true. Defaults to 30 seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxQueueSize

Specify an integer or integer[KB|MB|GB].
<br>Sets the maximum size of the forwarder output queue. It also sets the maximum size of the wait queue to 3x this value, if you have enabled indexer acknowledgment (useACK=true).
Although the wait queue and the output queues are both configured by this attribute, they are separate queues. The setting determines the maximum size of the queue in-memory (RAM) buffer.
For heavy forwarders sending parsed data, maxQueueSize is the maximum number of events. Since events are typically much shorter than data blocks, the memory consumed by the queue on a parsing forwarder is likely to be much smaller than on a non-parsing forwarder, if you use this version of the setting.
If specified as a lone integer (for example, maxQueueSize=100), maxQueueSize indicates the maximum number of queued events (for parsed data) or blocks of data (for unparsed data). A block of data is approximately 64KB. For non-parsing forwarders, such as universal forwarders, that send unparsed data, maxQueueSize is the maximum number of data blocks.
If specified as an integer followed by KB, MB, or GB (for example, maxQueueSize=100MB), maxQueueSize indicates the maximum RAM allocated to the queue buffer. Defaults to 500KB (which means a maximum size of 500KB for the output queue and 1500KB for the wait queue, if any).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

Valid values: (tcpout | syslog). Specifies the type of output processor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the group of receivers.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendCookedData

If true, events are cooked (processed by Splunk software). If false, events are raw and untouched prior to sending. Defaults to true.
Set to false if you are sending to a third-party system.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Servers

Comma-separated list of servers to include in the group.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

Token value generated by the indexer after configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Acl

_Required_: No

_Type_: List of <a href="acldefinition.md">AclDefinition</a>

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

