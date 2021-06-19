# TF::FortiOS::Wirelesscontrollerhotspot20H2qpconncapability

Configure connection capability.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::Wirelesscontrollerhotspot20H2qpconncapability",
    "Properties" : {
        "<a href="#espport" title="EspPort">EspPort</a>" : <i>String</i>,
        "<a href="#ftpport" title="FtpPort">FtpPort</a>" : <i>String</i>,
        "<a href="#httpport" title="HttpPort">HttpPort</a>" : <i>String</i>,
        "<a href="#icmpport" title="IcmpPort">IcmpPort</a>" : <i>String</i>,
        "<a href="#ikev2port" title="Ikev2Port">Ikev2Port</a>" : <i>String</i>,
        "<a href="#ikev2xxport" title="Ikev2XxPort">Ikev2XxPort</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pptpvpnport" title="PptpVpnPort">PptpVpnPort</a>" : <i>String</i>,
        "<a href="#sshport" title="SshPort">SshPort</a>" : <i>String</i>,
        "<a href="#tlsport" title="TlsPort">TlsPort</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#voiptcpport" title="VoipTcpPort">VoipTcpPort</a>" : <i>String</i>,
        "<a href="#voipudpport" title="VoipUdpPort">VoipUdpPort</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::Wirelesscontrollerhotspot20H2qpconncapability
Properties:
    <a href="#espport" title="EspPort">EspPort</a>: <i>String</i>
    <a href="#ftpport" title="FtpPort">FtpPort</a>: <i>String</i>
    <a href="#httpport" title="HttpPort">HttpPort</a>: <i>String</i>
    <a href="#icmpport" title="IcmpPort">IcmpPort</a>: <i>String</i>
    <a href="#ikev2port" title="Ikev2Port">Ikev2Port</a>: <i>String</i>
    <a href="#ikev2xxport" title="Ikev2XxPort">Ikev2XxPort</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pptpvpnport" title="PptpVpnPort">PptpVpnPort</a>: <i>String</i>
    <a href="#sshport" title="SshPort">SshPort</a>: <i>String</i>
    <a href="#tlsport" title="TlsPort">TlsPort</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#voiptcpport" title="VoipTcpPort">VoipTcpPort</a>: <i>String</i>
    <a href="#voipudpport" title="VoipUdpPort">VoipUdpPort</a>: <i>String</i>
</pre>

## Properties

#### EspPort

Set ESP port service (used by IPsec VPNs) status. Valid values: `closed`, `open`, `unknown`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtpPort

Set FTP port service status. Valid values: `closed`, `open`, `unknown`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpPort

Set HTTP port service status. Valid values: `closed`, `open`, `unknown`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpPort

Set ICMP port service status. Valid values: `closed`, `open`, `unknown`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ikev2Port

Set IKEv2 port service for IPsec VPN status. Valid values: `closed`, `open`, `unknown`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ikev2XxPort

Set UDP port 4500 (which may be used by IKEv2 for IPsec VPN) service status. Valid values: `closed`, `open`, `unknown`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Connection capability name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PptpVpnPort

Set Point to Point Tunneling Protocol (PPTP) VPN port service status. Valid values: `closed`, `open`, `unknown`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPort

Set SSH port service status. Valid values: `closed`, `open`, `unknown`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsPort

Set TLS VPN (HTTPS) port service status. Valid values: `closed`, `open`, `unknown`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VoipTcpPort

Set VoIP TCP port service status. Valid values: `closed`, `open`, `unknown`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VoipUdpPort

Set VoIP UDP port service status. Valid values: `closed`, `open`, `unknown`.

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

