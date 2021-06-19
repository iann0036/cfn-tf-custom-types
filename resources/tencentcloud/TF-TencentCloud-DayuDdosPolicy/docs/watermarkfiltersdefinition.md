# TF::TencentCloud::DayuDdosPolicy WatermarkFiltersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoremove" title="AutoRemove">AutoRemove</a>" : <i>Boolean</i>,
    "<a href="#offset" title="Offset">Offset</a>" : <i>Double</i>,
    "<a href="#openswitch" title="OpenSwitch">OpenSwitch</a>" : <i>Boolean</i>,
    "<a href="#tcpportlist" title="TcpPortList">TcpPortList</a>" : <i>[ String, ... ]</i>,
    "<a href="#udpportlist" title="UdpPortList">UdpPortList</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoremove" title="AutoRemove">AutoRemove</a>: <i>Boolean</i>
<a href="#offset" title="Offset">Offset</a>: <i>Double</i>
<a href="#openswitch" title="OpenSwitch">OpenSwitch</a>: <i>Boolean</i>
<a href="#tcpportlist" title="TcpPortList">TcpPortList</a>: <i>
      - String</i>
<a href="#udpportlist" title="UdpPortList">UdpPortList</a>: <i>
      - String</i>
</pre>

## Properties

#### AutoRemove

Indicate whether to auto-remove the watermark or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Offset

The offset of watermark. Valid value ranges: (0~1500).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenSwitch

Indicate whether to open watermark or not. It muse be set `true` when any field of watermark was set.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpPortList

Port range of TCP, the format is like `2000-3000`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpPortList

Port range of TCP, the format is like `2000-3000`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

