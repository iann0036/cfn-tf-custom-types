# TF::TencentCloud::DayuDdosPolicy DropOptionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#badconnthreshold" title="BadConnThreshold">BadConnThreshold</a>" : <i>Double</i>,
    "<a href="#checksyncconn" title="CheckSyncConn">CheckSyncConn</a>" : <i>Boolean</i>,
    "<a href="#conntimeout" title="ConnTimeout">ConnTimeout</a>" : <i>Double</i>,
    "<a href="#dconnlimit" title="DConnLimit">DConnLimit</a>" : <i>Double</i>,
    "<a href="#dnewlimit" title="DNewLimit">DNewLimit</a>" : <i>Double</i>,
    "<a href="#dropabroad" title="DropAbroad">DropAbroad</a>" : <i>Boolean</i>,
    "<a href="#dropicmp" title="DropIcmp">DropIcmp</a>" : <i>Boolean</i>,
    "<a href="#dropother" title="DropOther">DropOther</a>" : <i>Boolean</i>,
    "<a href="#droptcp" title="DropTcp">DropTcp</a>" : <i>Boolean</i>,
    "<a href="#dropudp" title="DropUdp">DropUdp</a>" : <i>Boolean</i>,
    "<a href="#icmpmbpslimit" title="IcmpMbpsLimit">IcmpMbpsLimit</a>" : <i>Double</i>,
    "<a href="#nullconnenable" title="NullConnEnable">NullConnEnable</a>" : <i>Boolean</i>,
    "<a href="#othermbpslimit" title="OtherMbpsLimit">OtherMbpsLimit</a>" : <i>Double</i>,
    "<a href="#sconnlimit" title="SConnLimit">SConnLimit</a>" : <i>Double</i>,
    "<a href="#snewlimit" title="SNewLimit">SNewLimit</a>" : <i>Double</i>,
    "<a href="#synlimit" title="SynLimit">SynLimit</a>" : <i>Double</i>,
    "<a href="#synrate" title="SynRate">SynRate</a>" : <i>Double</i>,
    "<a href="#tcpmbpslimit" title="TcpMbpsLimit">TcpMbpsLimit</a>" : <i>Double</i>,
    "<a href="#udpmbpslimit" title="UdpMbpsLimit">UdpMbpsLimit</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#badconnthreshold" title="BadConnThreshold">BadConnThreshold</a>: <i>Double</i>
<a href="#checksyncconn" title="CheckSyncConn">CheckSyncConn</a>: <i>Boolean</i>
<a href="#conntimeout" title="ConnTimeout">ConnTimeout</a>: <i>Double</i>
<a href="#dconnlimit" title="DConnLimit">DConnLimit</a>: <i>Double</i>
<a href="#dnewlimit" title="DNewLimit">DNewLimit</a>: <i>Double</i>
<a href="#dropabroad" title="DropAbroad">DropAbroad</a>: <i>Boolean</i>
<a href="#dropicmp" title="DropIcmp">DropIcmp</a>: <i>Boolean</i>
<a href="#dropother" title="DropOther">DropOther</a>: <i>Boolean</i>
<a href="#droptcp" title="DropTcp">DropTcp</a>: <i>Boolean</i>
<a href="#dropudp" title="DropUdp">DropUdp</a>: <i>Boolean</i>
<a href="#icmpmbpslimit" title="IcmpMbpsLimit">IcmpMbpsLimit</a>: <i>Double</i>
<a href="#nullconnenable" title="NullConnEnable">NullConnEnable</a>: <i>Boolean</i>
<a href="#othermbpslimit" title="OtherMbpsLimit">OtherMbpsLimit</a>: <i>Double</i>
<a href="#sconnlimit" title="SConnLimit">SConnLimit</a>: <i>Double</i>
<a href="#snewlimit" title="SNewLimit">SNewLimit</a>: <i>Double</i>
<a href="#synlimit" title="SynLimit">SynLimit</a>: <i>Double</i>
<a href="#synrate" title="SynRate">SynRate</a>: <i>Double</i>
<a href="#tcpmbpslimit" title="TcpMbpsLimit">TcpMbpsLimit</a>: <i>Double</i>
<a href="#udpmbpslimit" title="UdpMbpsLimit">UdpMbpsLimit</a>: <i>Double</i>
</pre>

## Properties

#### BadConnThreshold

The number of new connections based on destination IP that trigger suppression of connections. Valid value ranges: (0~4294967295).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckSyncConn

Indicate whether to check null connection or not.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnTimeout

Connection timeout of abnormal connection check. Valid value ranges: (0~65535).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DConnLimit

The limit of concurrent connections based on destination IP. Valid value ranges: (0~4294967295).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DNewLimit

The limit of new connections based on destination IP. Valid value ranges: (0~4294967295).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropAbroad

Indicate whether to drop abroad traffic or not.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropIcmp

Indicate whether to drop ICMP protocol or not.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropOther

Indicate whether to drop other protocols(exclude TCP/UDP/ICMP) or not.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropTcp

Indicate whether to drop TCP protocol or not.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropUdp

Indicate to drop UDP protocol or not.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpMbpsLimit

The limit of ICMP traffic rate. Valid value ranges: (0~4294967295)(Mbps).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NullConnEnable

Indicate to enable null connection or not.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OtherMbpsLimit

The limit of other protocols(exclude TCP/UDP/ICMP) traffic rate. Valid value ranges: (0~4294967295)(Mbps).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SConnLimit

The limit of concurrent connections based on source IP. Valid value ranges: (0~4294967295).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SNewLimit

The limit of new connections based on source IP. Valid value ranges: (0~4294967295).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SynLimit

The limit of syn of abnormal connection check. Valid value ranges: (0~100).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SynRate

The percentage of syn in ack of abnormal connection check. Valid value ranges: (0~100).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpMbpsLimit

The limit of TCP traffic. Valid value ranges: (0~4294967295)(Mbps).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpMbpsLimit

The limit of UDP traffic rate. Valid value ranges: (0~4294967295)(Mbps).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

