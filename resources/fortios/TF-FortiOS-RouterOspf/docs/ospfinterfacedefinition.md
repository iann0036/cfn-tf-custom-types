# TF::FortiOS::RouterOspf OspfInterfaceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authentication" title="Authentication">Authentication</a>" : <i>String</i>,
    "<a href="#authenticationkey" title="AuthenticationKey">AuthenticationKey</a>" : <i>String</i>,
    "<a href="#bfd" title="Bfd">Bfd</a>" : <i>String</i>,
    "<a href="#cost" title="Cost">Cost</a>" : <i>Double</i>,
    "<a href="#databasefilterout" title="DatabaseFilterOut">DatabaseFilterOut</a>" : <i>String</i>,
    "<a href="#deadinterval" title="DeadInterval">DeadInterval</a>" : <i>Double</i>,
    "<a href="#hellointerval" title="HelloInterval">HelloInterval</a>" : <i>Double</i>,
    "<a href="#hellomultiplier" title="HelloMultiplier">HelloMultiplier</a>" : <i>Double</i>,
    "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
    "<a href="#md5key" title="Md5Key">Md5Key</a>" : <i>String</i>,
    "<a href="#md5keychain" title="Md5Keychain">Md5Keychain</a>" : <i>String</i>,
    "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
    "<a href="#mtuignore" title="MtuIgnore">MtuIgnore</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#networktype" title="NetworkType">NetworkType</a>" : <i>String</i>,
    "<a href="#prefixlength" title="PrefixLength">PrefixLength</a>" : <i>Double</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#resynctimeout" title="ResyncTimeout">ResyncTimeout</a>" : <i>Double</i>,
    "<a href="#retransmitinterval" title="RetransmitInterval">RetransmitInterval</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#transmitdelay" title="TransmitDelay">TransmitDelay</a>" : <i>Double</i>,
    "<a href="#md5keys" title="Md5Keys">Md5Keys</a>" : <i>[ <a href="md5keysdefinition.md">Md5KeysDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authentication" title="Authentication">Authentication</a>: <i>String</i>
<a href="#authenticationkey" title="AuthenticationKey">AuthenticationKey</a>: <i>String</i>
<a href="#bfd" title="Bfd">Bfd</a>: <i>String</i>
<a href="#cost" title="Cost">Cost</a>: <i>Double</i>
<a href="#databasefilterout" title="DatabaseFilterOut">DatabaseFilterOut</a>: <i>String</i>
<a href="#deadinterval" title="DeadInterval">DeadInterval</a>: <i>Double</i>
<a href="#hellointerval" title="HelloInterval">HelloInterval</a>: <i>Double</i>
<a href="#hellomultiplier" title="HelloMultiplier">HelloMultiplier</a>: <i>Double</i>
<a href="#interface" title="Interface">Interface</a>: <i>String</i>
<a href="#ip" title="Ip">Ip</a>: <i>String</i>
<a href="#md5key" title="Md5Key">Md5Key</a>: <i>String</i>
<a href="#md5keychain" title="Md5Keychain">Md5Keychain</a>: <i>String</i>
<a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
<a href="#mtuignore" title="MtuIgnore">MtuIgnore</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#networktype" title="NetworkType">NetworkType</a>: <i>String</i>
<a href="#prefixlength" title="PrefixLength">PrefixLength</a>: <i>Double</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#resynctimeout" title="ResyncTimeout">ResyncTimeout</a>: <i>Double</i>
<a href="#retransmitinterval" title="RetransmitInterval">RetransmitInterval</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#transmitdelay" title="TransmitDelay">TransmitDelay</a>: <i>Double</i>
<a href="#md5keys" title="Md5Keys">Md5Keys</a>: <i>
      - <a href="md5keysdefinition.md">Md5KeysDefinition</a></i>
</pre>

## Properties

#### Authentication

Authentication type. Valid values: `none`, `text`, `md5`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationKey

Authentication key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bfd

Bidirectional Forwarding Detection (BFD). Valid values: `global`, `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cost

Cost of the interface, value range from 0 to 65535, 0 means auto-cost.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseFilterOut

Enable/disable control of flooding out LSAs. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

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

#### HelloMultiplier

Number of hello packets within dead interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Configuration interface name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Md5Key

MD5 key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Md5Keychain

Authentication MD5 key-chain name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

MTU for database description packets.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MtuIgnore

Enable/disable ignore MTU. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Interface entry name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkType

Network type. Valid values: `broadcast`, `non-broadcast`, `point-to-point`, `point-to-multipoint`, `point-to-multipoint-non-broadcast`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixLength

Prefix length.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Priority.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResyncTimeout

Graceful restart neighbor resynchronization timeout.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetransmitInterval

Retransmit interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable status. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransmitDelay

Transmit delay.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Md5Keys

_Required_: No

_Type_: List of <a href="md5keysdefinition.md">Md5KeysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

