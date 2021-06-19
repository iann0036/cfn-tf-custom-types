# TF::FortiOS::SystemGretunnel

Configure GRE tunnel.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemGretunnel",
    "Properties" : {
        "<a href="#checksumreception" title="ChecksumReception">ChecksumReception</a>" : <i>String</i>,
        "<a href="#checksumtransmission" title="ChecksumTransmission">ChecksumTransmission</a>" : <i>String</i>,
        "<a href="#diffservcode" title="Diffservcode">Diffservcode</a>" : <i>String</i>,
        "<a href="#dscpcopying" title="DscpCopying">DscpCopying</a>" : <i>String</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#ipversion" title="IpVersion">IpVersion</a>" : <i>String</i>,
        "<a href="#keepalivefailtimes" title="KeepaliveFailtimes">KeepaliveFailtimes</a>" : <i>Double</i>,
        "<a href="#keepaliveinterval" title="KeepaliveInterval">KeepaliveInterval</a>" : <i>Double</i>,
        "<a href="#keyinbound" title="KeyInbound">KeyInbound</a>" : <i>Double</i>,
        "<a href="#keyoutbound" title="KeyOutbound">KeyOutbound</a>" : <i>Double</i>,
        "<a href="#localgw" title="LocalGw">LocalGw</a>" : <i>String</i>,
        "<a href="#localgw6" title="LocalGw6">LocalGw6</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#remotegw" title="RemoteGw">RemoteGw</a>" : <i>String</i>,
        "<a href="#remotegw6" title="RemoteGw6">RemoteGw6</a>" : <i>String</i>,
        "<a href="#sequencenumberreception" title="SequenceNumberReception">SequenceNumberReception</a>" : <i>String</i>,
        "<a href="#sequencenumbertransmission" title="SequenceNumberTransmission">SequenceNumberTransmission</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemGretunnel
Properties:
    <a href="#checksumreception" title="ChecksumReception">ChecksumReception</a>: <i>String</i>
    <a href="#checksumtransmission" title="ChecksumTransmission">ChecksumTransmission</a>: <i>String</i>
    <a href="#diffservcode" title="Diffservcode">Diffservcode</a>: <i>String</i>
    <a href="#dscpcopying" title="DscpCopying">DscpCopying</a>: <i>String</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#ipversion" title="IpVersion">IpVersion</a>: <i>String</i>
    <a href="#keepalivefailtimes" title="KeepaliveFailtimes">KeepaliveFailtimes</a>: <i>Double</i>
    <a href="#keepaliveinterval" title="KeepaliveInterval">KeepaliveInterval</a>: <i>Double</i>
    <a href="#keyinbound" title="KeyInbound">KeyInbound</a>: <i>Double</i>
    <a href="#keyoutbound" title="KeyOutbound">KeyOutbound</a>: <i>Double</i>
    <a href="#localgw" title="LocalGw">LocalGw</a>: <i>String</i>
    <a href="#localgw6" title="LocalGw6">LocalGw6</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#remotegw" title="RemoteGw">RemoteGw</a>: <i>String</i>
    <a href="#remotegw6" title="RemoteGw6">RemoteGw6</a>: <i>String</i>
    <a href="#sequencenumberreception" title="SequenceNumberReception">SequenceNumberReception</a>: <i>String</i>
    <a href="#sequencenumbertransmission" title="SequenceNumberTransmission">SequenceNumberTransmission</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### ChecksumReception

Enable/disable validating checksums in received GRE packets. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChecksumTransmission

Enable/disable including checksums in transmitted GRE packets. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Diffservcode

DiffServ setting to be applied to GRE tunnel outer IP header.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DscpCopying

Enable/disable DSCP copying. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Interface name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpVersion

IP version to use for VPN interface. Valid values: `4`, `6`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepaliveFailtimes

Number of consecutive unreturned keepalive messages before a GRE connection is considered down (1 - 255).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepaliveInterval

Keepalive message interval (0 - 32767, 0 = disabled).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyInbound

Require received GRE packets contain this key (0 - 4294967295).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyOutbound

Include this key in transmitted GRE packets (0 - 4294967295).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalGw

IP address of the local gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalGw6

IPv6 address of the local gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Tunnel name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteGw

IP address of the remote gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteGw6

IPv6 address of the remote gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SequenceNumberReception

Enable/disable validating sequence numbers in received GRE packets. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SequenceNumberTransmission

Enable/disable including of sequence numbers in transmitted GRE packets. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

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

