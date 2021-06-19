# TF::FortiOS::RouterOspf6 Ospf6InterfaceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#areaid" title="AreaId">AreaId</a>" : <i>String</i>,
    "<a href="#authentication" title="Authentication">Authentication</a>" : <i>String</i>,
    "<a href="#bfd" title="Bfd">Bfd</a>" : <i>String</i>,
    "<a href="#cost" title="Cost">Cost</a>" : <i>Double</i>,
    "<a href="#deadinterval" title="DeadInterval">DeadInterval</a>" : <i>Double</i>,
    "<a href="#hellointerval" title="HelloInterval">HelloInterval</a>" : <i>Double</i>,
    "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
    "<a href="#ipsecauthalg" title="IpsecAuthAlg">IpsecAuthAlg</a>" : <i>String</i>,
    "<a href="#ipsecencalg" title="IpsecEncAlg">IpsecEncAlg</a>" : <i>String</i>,
    "<a href="#keyrolloverinterval" title="KeyRolloverInterval">KeyRolloverInterval</a>" : <i>Double</i>,
    "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
    "<a href="#mtuignore" title="MtuIgnore">MtuIgnore</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#networktype" title="NetworkType">NetworkType</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#retransmitinterval" title="RetransmitInterval">RetransmitInterval</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#transmitdelay" title="TransmitDelay">TransmitDelay</a>" : <i>Double</i>,
    "<a href="#ipseckeys" title="IpsecKeys">IpsecKeys</a>" : <i>[ <a href="ipseckeysdefinition.md">IpsecKeysDefinition</a>, ... ]</i>,
    "<a href="#neighbor" title="Neighbor">Neighbor</a>" : <i>[ <a href="neighbordefinition.md">NeighborDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#areaid" title="AreaId">AreaId</a>: <i>String</i>
<a href="#authentication" title="Authentication">Authentication</a>: <i>String</i>
<a href="#bfd" title="Bfd">Bfd</a>: <i>String</i>
<a href="#cost" title="Cost">Cost</a>: <i>Double</i>
<a href="#deadinterval" title="DeadInterval">DeadInterval</a>: <i>Double</i>
<a href="#hellointerval" title="HelloInterval">HelloInterval</a>: <i>Double</i>
<a href="#interface" title="Interface">Interface</a>: <i>String</i>
<a href="#ipsecauthalg" title="IpsecAuthAlg">IpsecAuthAlg</a>: <i>String</i>
<a href="#ipsecencalg" title="IpsecEncAlg">IpsecEncAlg</a>: <i>String</i>
<a href="#keyrolloverinterval" title="KeyRolloverInterval">KeyRolloverInterval</a>: <i>Double</i>
<a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
<a href="#mtuignore" title="MtuIgnore">MtuIgnore</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#networktype" title="NetworkType">NetworkType</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#retransmitinterval" title="RetransmitInterval">RetransmitInterval</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#transmitdelay" title="TransmitDelay">TransmitDelay</a>: <i>Double</i>
<a href="#ipseckeys" title="IpsecKeys">IpsecKeys</a>: <i>
      - <a href="ipseckeysdefinition.md">IpsecKeysDefinition</a></i>
<a href="#neighbor" title="Neighbor">Neighbor</a>: <i>
      - <a href="neighbordefinition.md">NeighborDefinition</a></i>
</pre>

## Properties

#### AreaId

A.B.C.D, in IPv4 address format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authentication

Authentication mode. Valid values: `none`, `ah`, `esp`, `area`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bfd

Enable/disable Bidirectional Forwarding Detection (BFD). Valid values: `global`, `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cost

Cost of the interface, value range from 0 to 65535, 0 means auto-cost.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeadInterval

Dead interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HelloInterval

Hello interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Configuration interface name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecAuthAlg

Authentication algorithm. Valid values: `md5`, `sha1`, `sha256`, `sha384`, `sha512`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecEncAlg

Encryption algorithm. Valid values: `null`, `des`, `3des`, `aes128`, `aes192`, `aes256`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyRolloverInterval

Key roll-over interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

MTU for OSPFv3 packets.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MtuIgnore

Enable/disable ignoring MTU field in DBD packets. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Interface entry name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkType

Network type. Valid values: `broadcast`, `point-to-point`, `non-broadcast`, `point-to-multipoint`, `point-to-multipoint-non-broadcast`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

priority.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetransmitInterval

Retransmit interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable OSPF6 routing on this interface. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransmitDelay

Transmit delay.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecKeys

_Required_: No

_Type_: List of <a href="ipseckeysdefinition.md">IpsecKeysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Neighbor

_Required_: No

_Type_: List of <a href="neighbordefinition.md">NeighborDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

