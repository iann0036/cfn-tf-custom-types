# TF::FortiOS::WirelesscontrollerWagprofile

Configure wireless access gateway (WAG) profiles used for tunnels on AP.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WirelesscontrollerWagprofile",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#dhcpipaddr" title="DhcpIpAddr">DhcpIpAddr</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pinginterval" title="PingInterval">PingInterval</a>" : <i>Double</i>,
        "<a href="#pingnumber" title="PingNumber">PingNumber</a>" : <i>Double</i>,
        "<a href="#returnpackettimeout" title="ReturnPacketTimeout">ReturnPacketTimeout</a>" : <i>Double</i>,
        "<a href="#tunneltype" title="TunnelType">TunnelType</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#wagip" title="WagIp">WagIp</a>" : <i>String</i>,
        "<a href="#wagport" title="WagPort">WagPort</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WirelesscontrollerWagprofile
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#dhcpipaddr" title="DhcpIpAddr">DhcpIpAddr</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pinginterval" title="PingInterval">PingInterval</a>: <i>Double</i>
    <a href="#pingnumber" title="PingNumber">PingNumber</a>: <i>Double</i>
    <a href="#returnpackettimeout" title="ReturnPacketTimeout">ReturnPacketTimeout</a>: <i>Double</i>
    <a href="#tunneltype" title="TunnelType">TunnelType</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#wagip" title="WagIp">WagIp</a>: <i>String</i>
    <a href="#wagport" title="WagPort">WagPort</a>: <i>Double</i>
</pre>

## Properties

#### Comment

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpIpAddr

IP address of the monitoring DHCP request packet sent through the tunnel.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Tunnel profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PingInterval

Interval between two tunnel monitoring echo packets (1 - 65535 sec, default = 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PingNumber

Number of the tunnel monitoring echo packets (1 - 65535, default = 5).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReturnPacketTimeout

Window of time for the return packets from the tunnel's remote end (1 - 65535 sec, default = 160).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelType

Tunnel type. Valid values: `l2tpv3`, `gre`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WagIp

IP Address of the wireless access gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WagPort

UDP port of the wireless access gateway.

_Required_: No

_Type_: Double

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

