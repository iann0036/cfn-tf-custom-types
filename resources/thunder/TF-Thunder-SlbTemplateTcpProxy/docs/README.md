# TF::Thunder::SlbTemplateTcpProxy

`thunder_slb_template_tcp_proxy` Provides details about thunder slb template tcp proxy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateTcpProxy",
    "Properties" : {
        "<a href="#ackaggressiveness" title="AckAggressiveness">AckAggressiveness</a>" : <i>String</i>,
        "<a href="#aliveifactive" title="AliveIfActive">AliveIfActive</a>" : <i>Double</i>,
        "<a href="#backendwscale" title="BackendWscale">BackendWscale</a>" : <i>Double</i>,
        "<a href="#delsessiononserverdown" title="DelSessionOnServerDown">DelSessionOnServerDown</a>" : <i>Double</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Double</i>,
        "<a href="#disableabc" title="DisableAbc">DisableAbc</a>" : <i>Double</i>,
        "<a href="#disablesack" title="DisableSack">DisableSack</a>" : <i>Double</i>,
        "<a href="#disabletcptimestamps" title="DisableTcpTimestamps">DisableTcpTimestamps</a>" : <i>Double</i>,
        "<a href="#disablewindowscale" title="DisableWindowScale">DisableWindowScale</a>" : <i>Double</i>,
        "<a href="#down" title="Down">Down</a>" : <i>Double</i>,
        "<a href="#dynamicbufferallocation" title="DynamicBufferAllocation">DynamicBufferAllocation</a>" : <i>Double</i>,
        "<a href="#earlyretransmit" title="EarlyRetransmit">EarlyRetransmit</a>" : <i>Double</i>,
        "<a href="#fintimeout" title="FinTimeout">FinTimeout</a>" : <i>Double</i>,
        "<a href="#forcedeletetimeout" title="ForceDeleteTimeout">ForceDeleteTimeout</a>" : <i>Double</i>,
        "<a href="#forcedeletetimeout100ms" title="ForceDeleteTimeout100ms">ForceDeleteTimeout100ms</a>" : <i>Double</i>,
        "<a href="#halfcloseidletimeout" title="HalfCloseIdleTimeout">HalfCloseIdleTimeout</a>" : <i>Double</i>,
        "<a href="#halfopenidletimeout" title="HalfOpenIdleTimeout">HalfOpenIdleTimeout</a>" : <i>Double</i>,
        "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
        "<a href="#initcwnd" title="InitCwnd">InitCwnd</a>" : <i>Double</i>,
        "<a href="#initialwindowsize" title="InitialWindowSize">InitialWindowSize</a>" : <i>Double</i>,
        "<a href="#insertclientip" title="InsertClientIp">InsertClientIp</a>" : <i>Double</i>,
        "<a href="#invalidratelimit" title="InvalidRateLimit">InvalidRateLimit</a>" : <i>Double</i>,
        "<a href="#keepaliveinterval" title="KeepaliveInterval">KeepaliveInterval</a>" : <i>Double</i>,
        "<a href="#keepaliveprobes" title="KeepaliveProbes">KeepaliveProbes</a>" : <i>Double</i>,
        "<a href="#limitedslowstart" title="LimitedSlowstart">LimitedSlowstart</a>" : <i>Double</i>,
        "<a href="#maxburst" title="Maxburst">Maxburst</a>" : <i>Double</i>,
        "<a href="#minrto" title="MinRto">MinRto</a>" : <i>Double</i>,
        "<a href="#mss" title="Mss">Mss</a>" : <i>Double</i>,
        "<a href="#nagle" title="Nagle">Nagle</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pshflagoptimization" title="PshFlagOptimization">PshFlagOptimization</a>" : <i>Double</i>,
        "<a href="#qos" title="Qos">Qos</a>" : <i>Double</i>,
        "<a href="#reassemblylimit" title="ReassemblyLimit">ReassemblyLimit</a>" : <i>Double</i>,
        "<a href="#reassemblytimeout" title="ReassemblyTimeout">ReassemblyTimeout</a>" : <i>Double</i>,
        "<a href="#receivebuffer" title="ReceiveBuffer">ReceiveBuffer</a>" : <i>Double</i>,
        "<a href="#reno" title="Reno">Reno</a>" : <i>Double</i>,
        "<a href="#resetfwd" title="ResetFwd">ResetFwd</a>" : <i>Double</i>,
        "<a href="#resetrev" title="ResetRev">ResetRev</a>" : <i>Double</i>,
        "<a href="#retransmitretries" title="RetransmitRetries">RetransmitRetries</a>" : <i>Double</i>,
        "<a href="#serverdownaction" title="ServerDownAction">ServerDownAction</a>" : <i>String</i>,
        "<a href="#synretries" title="SynRetries">SynRetries</a>" : <i>Double</i>,
        "<a href="#timewait" title="Timewait">Timewait</a>" : <i>Double</i>,
        "<a href="#transmitbuffer" title="TransmitBuffer">TransmitBuffer</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateTcpProxy
Properties:
    <a href="#ackaggressiveness" title="AckAggressiveness">AckAggressiveness</a>: <i>String</i>
    <a href="#aliveifactive" title="AliveIfActive">AliveIfActive</a>: <i>Double</i>
    <a href="#backendwscale" title="BackendWscale">BackendWscale</a>: <i>Double</i>
    <a href="#delsessiononserverdown" title="DelSessionOnServerDown">DelSessionOnServerDown</a>: <i>Double</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Double</i>
    <a href="#disableabc" title="DisableAbc">DisableAbc</a>: <i>Double</i>
    <a href="#disablesack" title="DisableSack">DisableSack</a>: <i>Double</i>
    <a href="#disabletcptimestamps" title="DisableTcpTimestamps">DisableTcpTimestamps</a>: <i>Double</i>
    <a href="#disablewindowscale" title="DisableWindowScale">DisableWindowScale</a>: <i>Double</i>
    <a href="#down" title="Down">Down</a>: <i>Double</i>
    <a href="#dynamicbufferallocation" title="DynamicBufferAllocation">DynamicBufferAllocation</a>: <i>Double</i>
    <a href="#earlyretransmit" title="EarlyRetransmit">EarlyRetransmit</a>: <i>Double</i>
    <a href="#fintimeout" title="FinTimeout">FinTimeout</a>: <i>Double</i>
    <a href="#forcedeletetimeout" title="ForceDeleteTimeout">ForceDeleteTimeout</a>: <i>Double</i>
    <a href="#forcedeletetimeout100ms" title="ForceDeleteTimeout100ms">ForceDeleteTimeout100ms</a>: <i>Double</i>
    <a href="#halfcloseidletimeout" title="HalfCloseIdleTimeout">HalfCloseIdleTimeout</a>: <i>Double</i>
    <a href="#halfopenidletimeout" title="HalfOpenIdleTimeout">HalfOpenIdleTimeout</a>: <i>Double</i>
    <a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
    <a href="#initcwnd" title="InitCwnd">InitCwnd</a>: <i>Double</i>
    <a href="#initialwindowsize" title="InitialWindowSize">InitialWindowSize</a>: <i>Double</i>
    <a href="#insertclientip" title="InsertClientIp">InsertClientIp</a>: <i>Double</i>
    <a href="#invalidratelimit" title="InvalidRateLimit">InvalidRateLimit</a>: <i>Double</i>
    <a href="#keepaliveinterval" title="KeepaliveInterval">KeepaliveInterval</a>: <i>Double</i>
    <a href="#keepaliveprobes" title="KeepaliveProbes">KeepaliveProbes</a>: <i>Double</i>
    <a href="#limitedslowstart" title="LimitedSlowstart">LimitedSlowstart</a>: <i>Double</i>
    <a href="#maxburst" title="Maxburst">Maxburst</a>: <i>Double</i>
    <a href="#minrto" title="MinRto">MinRto</a>: <i>Double</i>
    <a href="#mss" title="Mss">Mss</a>: <i>Double</i>
    <a href="#nagle" title="Nagle">Nagle</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pshflagoptimization" title="PshFlagOptimization">PshFlagOptimization</a>: <i>Double</i>
    <a href="#qos" title="Qos">Qos</a>: <i>Double</i>
    <a href="#reassemblylimit" title="ReassemblyLimit">ReassemblyLimit</a>: <i>Double</i>
    <a href="#reassemblytimeout" title="ReassemblyTimeout">ReassemblyTimeout</a>: <i>Double</i>
    <a href="#receivebuffer" title="ReceiveBuffer">ReceiveBuffer</a>: <i>Double</i>
    <a href="#reno" title="Reno">Reno</a>: <i>Double</i>
    <a href="#resetfwd" title="ResetFwd">ResetFwd</a>: <i>Double</i>
    <a href="#resetrev" title="ResetRev">ResetRev</a>: <i>Double</i>
    <a href="#retransmitretries" title="RetransmitRetries">RetransmitRetries</a>: <i>Double</i>
    <a href="#serverdownaction" title="ServerDownAction">ServerDownAction</a>: <i>String</i>
    <a href="#synretries" title="SynRetries">SynRetries</a>: <i>Double</i>
    <a href="#timewait" title="Timewait">Timewait</a>: <i>Double</i>
    <a href="#transmitbuffer" title="TransmitBuffer">TransmitBuffer</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### AckAggressiveness

‘low’: Delayed ACK; ‘medium’: Delayed ACK, with ACK on each packet with PUSH flag; ‘high’: ACK on each packet;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AliveIfActive

keep connection alive if active traffic.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendWscale

The TCP window scale used for the server side, default is off (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelSessionOnServerDown

Delete session if the server/port goes down (either disabled/hm down).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disable

send reset to client when server is disabled.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableAbc

Appropriate Byte Counting RFC 3465 Disabled, default is enabled (Appropriate Byte Counting (ABC) is enabled by default).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableSack

disable Selective Ack Option.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableTcpTimestamps

disable TCP Timestamps Option.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableWindowScale

disable TCP Window-Scale Option.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Down

send reset to client when server is down.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicBufferAllocation

Optimally adjust the transmit and receive buffer sizes of TCP proxy while keeping their sum constant.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EarlyRetransmit

Configure the Early-Retransmit Algorithm (RFC 5827) (Early-Retransmit is disabled by default).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FinTimeout

FIN timeout (sec), default is 5 (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDeleteTimeout

The maximum time that a session can stay in the system before being deleted, default is off (number (second)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDeleteTimeout100ms

The maximum time that a session can stay in the system before being deleted, default is off (number in 100ms).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HalfCloseIdleTimeout

TCP Half Close Idle Timeout (sec), default is off (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HalfOpenIdleTimeout

TCP Half Open Idle Timeout (sec), default is off (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

Idle Timeout (Interval of 60 seconds), default is 600 (idle timeout in second, default 600).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitCwnd

The initial congestion control window size (packets), default is 10 (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialWindowSize

Set the initial window size, default is off (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsertClientIp

Insert client ip into TCP option.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InvalidRateLimit

Invalid Packet Response Rate Limit (ms), default is 500 (number default 500 challenges).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepaliveInterval

Interval between keepalive probes (sec), default is off (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepaliveProbes

Number of keepalive probes sent, default is off.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitedSlowstart

RFC 3742 Limited Slow-Start for TCP with Large Congestion Windows (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Maxburst

The max packet count sent per transmission event (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinRto

The minmum retransmission timeout, default is 200ms (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mss

Responding MSS to use if client MSS is large, default is off (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nagle

Enable Nagle Algorithm.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

TCP Proxy Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PshFlagOptimization

Enable Optimized PSH Flag Use.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Qos

QOS level (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReassemblyLimit

The reassembly queuing limit, default is 25 segments (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReassemblyTimeout

The reassembly timeout, default is 30sec (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReceiveBuffer

TCP Receive Buffer (default 200k) (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reno

Enable Reno Congestion Control Algorithm.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetFwd

send reset to server if error happens.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetRev

send reset to client if error happens.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetransmitRetries

Number of Retries for Retransmit, default is 5.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerDownAction

‘FIN’: FIN Connection; ‘RST’: Reset Connection;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SynRetries

SYN Retry Numbers, default is 5.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timewait

Timewait Threshold (sec), default 5 (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransmitBuffer

TCP Transmit Buffer (default 200k) (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

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

