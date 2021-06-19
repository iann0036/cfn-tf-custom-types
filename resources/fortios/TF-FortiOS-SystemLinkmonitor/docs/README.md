# TF::FortiOS::SystemLinkmonitor

Configure Link Health Monitor.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemLinkmonitor",
    "Properties" : {
        "<a href="#addrmode" title="AddrMode">AddrMode</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#failtime" title="Failtime">Failtime</a>" : <i>Double</i>,
        "<a href="#gatewayip" title="GatewayIp">GatewayIp</a>" : <i>String</i>,
        "<a href="#gatewayip6" title="GatewayIp6">GatewayIp6</a>" : <i>String</i>,
        "<a href="#hapriority" title="HaPriority">HaPriority</a>" : <i>Double</i>,
        "<a href="#httpagent" title="HttpAgent">HttpAgent</a>" : <i>String</i>,
        "<a href="#httpget" title="HttpGet">HttpGet</a>" : <i>String</i>,
        "<a href="#httpmatch" title="HttpMatch">HttpMatch</a>" : <i>String</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#packetsize" title="PacketSize">PacketSize</a>" : <i>Double</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#probecount" title="ProbeCount">ProbeCount</a>" : <i>Double</i>,
        "<a href="#probetimeout" title="ProbeTimeout">ProbeTimeout</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#recoverytime" title="Recoverytime">Recoverytime</a>" : <i>Double</i>,
        "<a href="#securitymode" title="SecurityMode">SecurityMode</a>" : <i>String</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
        "<a href="#sourceip6" title="SourceIp6">SourceIp6</a>" : <i>String</i>,
        "<a href="#srcintf" title="Srcintf">Srcintf</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#updatecascadeinterface" title="UpdateCascadeInterface">UpdateCascadeInterface</a>" : <i>String</i>,
        "<a href="#updatestaticroute" title="UpdateStaticRoute">UpdateStaticRoute</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#server" title="Server">Server</a>" : <i>[ <a href="serverdefinition.md">ServerDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemLinkmonitor
Properties:
    <a href="#addrmode" title="AddrMode">AddrMode</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#failtime" title="Failtime">Failtime</a>: <i>Double</i>
    <a href="#gatewayip" title="GatewayIp">GatewayIp</a>: <i>String</i>
    <a href="#gatewayip6" title="GatewayIp6">GatewayIp6</a>: <i>String</i>
    <a href="#hapriority" title="HaPriority">HaPriority</a>: <i>Double</i>
    <a href="#httpagent" title="HttpAgent">HttpAgent</a>: <i>String</i>
    <a href="#httpget" title="HttpGet">HttpGet</a>: <i>String</i>
    <a href="#httpmatch" title="HttpMatch">HttpMatch</a>: <i>String</i>
    <a href="#interval" title="Interval">Interval</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#packetsize" title="PacketSize">PacketSize</a>: <i>Double</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#probecount" title="ProbeCount">ProbeCount</a>: <i>Double</i>
    <a href="#probetimeout" title="ProbeTimeout">ProbeTimeout</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#recoverytime" title="Recoverytime">Recoverytime</a>: <i>Double</i>
    <a href="#securitymode" title="SecurityMode">SecurityMode</a>: <i>String</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
    <a href="#sourceip6" title="SourceIp6">SourceIp6</a>: <i>String</i>
    <a href="#srcintf" title="Srcintf">Srcintf</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#updatecascadeinterface" title="UpdateCascadeInterface">UpdateCascadeInterface</a>: <i>String</i>
    <a href="#updatestaticroute" title="UpdateStaticRoute">UpdateStaticRoute</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#server" title="Server">Server</a>: <i>
      - <a href="serverdefinition.md">ServerDefinition</a></i>
</pre>

## Properties

#### AddrMode

Address mode (IPv4 or IPv6). Valid values: `ipv4`, `ipv6`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Failtime

Number of retry attempts before the server is considered down (1 - 10, default = 5).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayIp

Gateway IP address used to probe the server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayIp6

Gateway IPv6 address used to probe the server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaPriority

HA election priority (1 - 50).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpAgent

String in the http-agent field in the HTTP header.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpGet

If you are monitoring an HTML server you can send an HTTP-GET request with a custom string. Use this option to define the string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMatch

String that you expect to see in the HTTP-GET requests of the traffic to be monitored.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

Detection interval (1 - 3600 sec, default = 5).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Link monitor name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketSize

Packet size of a twamp test session,.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Twamp controller password in authentication mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Port number of the traffic to be used to monitor the server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProbeCount

Number of most recent probes that should be used to calculate latency and jitter (5 - 30, default = 30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProbeTimeout

Time to wait before a probe packet is considered lost (500 - 5000 msec, default = 500).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocols used to monitor the server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recoverytime

Number of successful responses received before server is considered recovered (1 - 10, default = 5).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityMode

Twamp controller security mode. Valid values: `none`, `authentication`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

Source IP address used in packet to the server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp6

Source IPv6 address used in packet to the server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcintf

Interface that receives the traffic to be monitored.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable this link monitor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateCascadeInterface

Enable/disable update cascade interface. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateStaticRoute

Enable/disable updating the static route. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

_Required_: No

_Type_: List of <a href="serverdefinition.md">ServerDefinition</a>

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

