# TF::FortiOS::WirelesscontrollerGlobal

Configure wireless controller global settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WirelesscontrollerGlobal",
    "Properties" : {
        "<a href="#aplogserver" title="ApLogServer">ApLogServer</a>" : <i>String</i>,
        "<a href="#aplogserverip" title="ApLogServerIp">ApLogServerIp</a>" : <i>String</i>,
        "<a href="#aplogserverport" title="ApLogServerPort">ApLogServerPort</a>" : <i>Double</i>,
        "<a href="#controlmessageoffload" title="ControlMessageOffload">ControlMessageOffload</a>" : <i>String</i>,
        "<a href="#dataethernetii" title="DataEthernetIi">DataEthernetIi</a>" : <i>String</i>,
        "<a href="#discoverymcaddr" title="DiscoveryMcAddr">DiscoveryMcAddr</a>" : <i>String</i>,
        "<a href="#fiappethtype" title="FiappEthType">FiappEthType</a>" : <i>Double</i>,
        "<a href="#imagedownload" title="ImageDownload">ImageDownload</a>" : <i>String</i>,
        "<a href="#ipsecbaseip" title="IpsecBaseIp">IpsecBaseIp</a>" : <i>String</i>,
        "<a href="#linkaggregation" title="LinkAggregation">LinkAggregation</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#maxclients" title="MaxClients">MaxClients</a>" : <i>Double</i>,
        "<a href="#maxretransmit" title="MaxRetransmit">MaxRetransmit</a>" : <i>Double</i>,
        "<a href="#meshethtype" title="MeshEthType">MeshEthType</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#roguescanmacadjacency" title="RogueScanMacAdjacency">RogueScanMacAdjacency</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#wtpshare" title="WtpShare">WtpShare</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WirelesscontrollerGlobal
Properties:
    <a href="#aplogserver" title="ApLogServer">ApLogServer</a>: <i>String</i>
    <a href="#aplogserverip" title="ApLogServerIp">ApLogServerIp</a>: <i>String</i>
    <a href="#aplogserverport" title="ApLogServerPort">ApLogServerPort</a>: <i>Double</i>
    <a href="#controlmessageoffload" title="ControlMessageOffload">ControlMessageOffload</a>: <i>String</i>
    <a href="#dataethernetii" title="DataEthernetIi">DataEthernetIi</a>: <i>String</i>
    <a href="#discoverymcaddr" title="DiscoveryMcAddr">DiscoveryMcAddr</a>: <i>String</i>
    <a href="#fiappethtype" title="FiappEthType">FiappEthType</a>: <i>Double</i>
    <a href="#imagedownload" title="ImageDownload">ImageDownload</a>: <i>String</i>
    <a href="#ipsecbaseip" title="IpsecBaseIp">IpsecBaseIp</a>: <i>String</i>
    <a href="#linkaggregation" title="LinkAggregation">LinkAggregation</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#maxclients" title="MaxClients">MaxClients</a>: <i>Double</i>
    <a href="#maxretransmit" title="MaxRetransmit">MaxRetransmit</a>: <i>Double</i>
    <a href="#meshethtype" title="MeshEthType">MeshEthType</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#roguescanmacadjacency" title="RogueScanMacAdjacency">RogueScanMacAdjacency</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#wtpshare" title="WtpShare">WtpShare</a>: <i>String</i>
</pre>

## Properties

#### ApLogServer

Enable/disable configuring APs or FortiAPs to send log messages to a syslog server (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApLogServerIp

IP address that APs or FortiAPs send log messages to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApLogServerPort

Port that APs or FortiAPs send log messages to.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControlMessageOffload

Configure CAPWAP control message data channel offload.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataEthernetIi

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiscoveryMcAddr

Multicast IP address for AP discovery (default = 244.0.1.140).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FiappEthType

Ethernet type for Fortinet Inter-Access Point Protocol (IAPP), or IEEE 802.11f, packets (0 - 65535, default = 5252).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageDownload

Enable/disable WTP image download at join time. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecBaseIp

Base IP address for IPsec VPN tunnels between the access points and the wireless controller (default = 169.254.0.1).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkAggregation

Enable/disable calculating the CAPWAP transmit hash to load balance sessions to link aggregation nodes (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Description of the location of the wireless controller.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxClients

Maximum number of clients that can connect simultaneously (default = 0, meaning no limitation).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRetransmit

Maximum number of tunnel packet retransmissions (0 - 64, default = 3).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MeshEthType

Mesh Ethernet identifier included in backhaul packets (0 - 65535, default = 8755).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the wireless controller.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RogueScanMacAdjacency

Maximum numerical difference between an AP's Ethernet and wireless MAC values to match for rogue detection (0 - 31, default = 7).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WtpShare

Enable/disable sharing of WTPs between VDOMs. Valid values: `enable`, `disable`.

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

