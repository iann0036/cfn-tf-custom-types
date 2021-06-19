# TF::DCNM::Interface

CloudFormation equivalent of dcnm_interface

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::DCNM::Interface",
    "Properties" : {
        "<a href="#accessvlans" title="AccessVlans">AccessVlans</a>" : <i>String</i>,
        "<a href="#adminstate" title="AdminState">AdminState</a>" : <i>Boolean</i>,
        "<a href="#allowedvlans" title="AllowedVlans">AllowedVlans</a>" : <i>String</i>,
        "<a href="#bpdugaurdflag" title="BpduGaurdFlag">BpduGaurdFlag</a>" : <i>String</i>,
        "<a href="#configuration" title="Configuration">Configuration</a>" : <i>String</i>,
        "<a href="#deploy" title="Deploy">Deploy</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ethernetspeed" title="EthernetSpeed">EthernetSpeed</a>" : <i>String</i>,
        "<a href="#fabricname" title="FabricName">FabricName</a>" : <i>String</i>,
        "<a href="#ipv4" title="Ipv4">Ipv4</a>" : <i>String</i>,
        "<a href="#ipv4prefix" title="Ipv4Prefix">Ipv4Prefix</a>" : <i>String</i>,
        "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>String</i>,
        "<a href="#ipv6prefix" title="Ipv6Prefix">Ipv6Prefix</a>" : <i>String</i>,
        "<a href="#loopbacklsrouting" title="LoopbackLsRouting">LoopbackLsRouting</a>" : <i>String</i>,
        "<a href="#loopbackreplicationmode" title="LoopbackReplicationMode">LoopbackReplicationMode</a>" : <i>String</i>,
        "<a href="#loopbackrouterid" title="LoopbackRouterId">LoopbackRouterId</a>" : <i>String</i>,
        "<a href="#loopbackroutingtag" title="LoopbackRoutingTag">LoopbackRoutingTag</a>" : <i>String</i>,
        "<a href="#loopbacktag" title="LoopbackTag">LoopbackTag</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#mtu" title="Mtu">Mtu</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pcinterface" title="PcInterface">PcInterface</a>" : <i>[ String, ... ]</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#portfastflag" title="PortFastFlag">PortFastFlag</a>" : <i>Boolean</i>,
        "<a href="#serialnumber" title="SerialNumber">SerialNumber</a>" : <i>String</i>,
        "<a href="#subinterfacemtu" title="SubinterfaceMtu">SubinterfaceMtu</a>" : <i>String</i>,
        "<a href="#subinterfacevlan" title="SubinterfaceVlan">SubinterfaceVlan</a>" : <i>Double</i>,
        "<a href="#switchname1" title="SwitchName1">SwitchName1</a>" : <i>String</i>,
        "<a href="#switchname2" title="SwitchName2">SwitchName2</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vpcpeer1accessvlans" title="VpcPeer1AccessVlans">VpcPeer1AccessVlans</a>" : <i>String</i>,
        "<a href="#vpcpeer1allowedvlans" title="VpcPeer1AllowedVlans">VpcPeer1AllowedVlans</a>" : <i>String</i>,
        "<a href="#vpcpeer1conf" title="VpcPeer1Conf">VpcPeer1Conf</a>" : <i>String</i>,
        "<a href="#vpcpeer1desc" title="VpcPeer1Desc">VpcPeer1Desc</a>" : <i>String</i>,
        "<a href="#vpcpeer1id" title="VpcPeer1Id">VpcPeer1Id</a>" : <i>Double</i>,
        "<a href="#vpcpeer1interface" title="VpcPeer1Interface">VpcPeer1Interface</a>" : <i>[ String, ... ]</i>,
        "<a href="#vpcpeer2accessvlans" title="VpcPeer2AccessVlans">VpcPeer2AccessVlans</a>" : <i>String</i>,
        "<a href="#vpcpeer2allowedvlans" title="VpcPeer2AllowedVlans">VpcPeer2AllowedVlans</a>" : <i>String</i>,
        "<a href="#vpcpeer2conf" title="VpcPeer2Conf">VpcPeer2Conf</a>" : <i>String</i>,
        "<a href="#vpcpeer2desc" title="VpcPeer2Desc">VpcPeer2Desc</a>" : <i>String</i>,
        "<a href="#vpcpeer2id" title="VpcPeer2Id">VpcPeer2Id</a>" : <i>Double</i>,
        "<a href="#vpcpeer2interface" title="VpcPeer2Interface">VpcPeer2Interface</a>" : <i>[ String, ... ]</i>,
        "<a href="#vrf" title="Vrf">Vrf</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::DCNM::Interface
Properties:
    <a href="#accessvlans" title="AccessVlans">AccessVlans</a>: <i>String</i>
    <a href="#adminstate" title="AdminState">AdminState</a>: <i>Boolean</i>
    <a href="#allowedvlans" title="AllowedVlans">AllowedVlans</a>: <i>String</i>
    <a href="#bpdugaurdflag" title="BpduGaurdFlag">BpduGaurdFlag</a>: <i>String</i>
    <a href="#configuration" title="Configuration">Configuration</a>: <i>String</i>
    <a href="#deploy" title="Deploy">Deploy</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ethernetspeed" title="EthernetSpeed">EthernetSpeed</a>: <i>String</i>
    <a href="#fabricname" title="FabricName">FabricName</a>: <i>String</i>
    <a href="#ipv4" title="Ipv4">Ipv4</a>: <i>String</i>
    <a href="#ipv4prefix" title="Ipv4Prefix">Ipv4Prefix</a>: <i>String</i>
    <a href="#ipv6" title="Ipv6">Ipv6</a>: <i>String</i>
    <a href="#ipv6prefix" title="Ipv6Prefix">Ipv6Prefix</a>: <i>String</i>
    <a href="#loopbacklsrouting" title="LoopbackLsRouting">LoopbackLsRouting</a>: <i>String</i>
    <a href="#loopbackreplicationmode" title="LoopbackReplicationMode">LoopbackReplicationMode</a>: <i>String</i>
    <a href="#loopbackrouterid" title="LoopbackRouterId">LoopbackRouterId</a>: <i>String</i>
    <a href="#loopbackroutingtag" title="LoopbackRoutingTag">LoopbackRoutingTag</a>: <i>String</i>
    <a href="#loopbacktag" title="LoopbackTag">LoopbackTag</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#mtu" title="Mtu">Mtu</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pcinterface" title="PcInterface">PcInterface</a>: <i>
      - String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#portfastflag" title="PortFastFlag">PortFastFlag</a>: <i>Boolean</i>
    <a href="#serialnumber" title="SerialNumber">SerialNumber</a>: <i>String</i>
    <a href="#subinterfacemtu" title="SubinterfaceMtu">SubinterfaceMtu</a>: <i>String</i>
    <a href="#subinterfacevlan" title="SubinterfaceVlan">SubinterfaceVlan</a>: <i>Double</i>
    <a href="#switchname1" title="SwitchName1">SwitchName1</a>: <i>String</i>
    <a href="#switchname2" title="SwitchName2">SwitchName2</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vpcpeer1accessvlans" title="VpcPeer1AccessVlans">VpcPeer1AccessVlans</a>: <i>String</i>
    <a href="#vpcpeer1allowedvlans" title="VpcPeer1AllowedVlans">VpcPeer1AllowedVlans</a>: <i>String</i>
    <a href="#vpcpeer1conf" title="VpcPeer1Conf">VpcPeer1Conf</a>: <i>String</i>
    <a href="#vpcpeer1desc" title="VpcPeer1Desc">VpcPeer1Desc</a>: <i>String</i>
    <a href="#vpcpeer1id" title="VpcPeer1Id">VpcPeer1Id</a>: <i>Double</i>
    <a href="#vpcpeer1interface" title="VpcPeer1Interface">VpcPeer1Interface</a>: <i>
      - String</i>
    <a href="#vpcpeer2accessvlans" title="VpcPeer2AccessVlans">VpcPeer2AccessVlans</a>: <i>String</i>
    <a href="#vpcpeer2allowedvlans" title="VpcPeer2AllowedVlans">VpcPeer2AllowedVlans</a>: <i>String</i>
    <a href="#vpcpeer2conf" title="VpcPeer2Conf">VpcPeer2Conf</a>: <i>String</i>
    <a href="#vpcpeer2desc" title="VpcPeer2Desc">VpcPeer2Desc</a>: <i>String</i>
    <a href="#vpcpeer2id" title="VpcPeer2Id">VpcPeer2Id</a>: <i>Double</i>
    <a href="#vpcpeer2interface" title="VpcPeer2Interface">VpcPeer2Interface</a>: <i>
      - String</i>
    <a href="#vrf" title="Vrf">Vrf</a>: <i>String</i>
</pre>

## Properties

#### AccessVlans

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminState

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedVlans

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BpduGaurdFlag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Configuration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Deploy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EthernetSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FabricName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4Prefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Prefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoopbackLsRouting

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoopbackReplicationMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoopbackRouterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoopbackRoutingTag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoopbackTag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcInterface

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortFastFlag

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerialNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubinterfaceMtu

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubinterfaceVlan

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchName1

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchName2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcPeer1AccessVlans

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcPeer1AllowedVlans

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcPeer1Conf

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcPeer1Desc

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcPeer1Id

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcPeer1Interface

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcPeer2AccessVlans

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcPeer2AllowedVlans

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcPeer2Conf

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcPeer2Desc

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcPeer2Id

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcPeer2Interface

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vrf

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

