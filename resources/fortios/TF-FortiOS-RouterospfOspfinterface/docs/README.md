# TF::FortiOS::RouterospfOspfinterface

OSPF interface configuration.

~> The provider supports the definition of Ospf-Interface in Router Ospf `fortios_router_ospf`, and also allows the definition of separate Ospf-Interface resources `fortios_routerospf_ospfinterface`, but do not use a `fortios_router_ospf` with in-line Ospf-Interface in conjunction with any `fortios_routerospf_ospfinterface` resources, otherwise conflicts and overwrite will occur.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::RouterospfOspfinterface",
    "Properties" : {
        "<a href="#authentication" title="Authentication">Authentication</a>" : <i>String</i>,
        "<a href="#authenticationkey" title="AuthenticationKey">AuthenticationKey</a>" : <i>String</i>,
        "<a href="#bfd" title="Bfd">Bfd</a>" : <i>String</i>,
        "<a href="#cost" title="Cost">Cost</a>" : <i>Double</i>,
        "<a href="#databasefilterout" title="DatabaseFilterOut">DatabaseFilterOut</a>" : <i>String</i>,
        "<a href="#deadinterval" title="DeadInterval">DeadInterval</a>" : <i>Double</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
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
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#md5keys" title="Md5Keys">Md5Keys</a>" : <i>[ <a href="md5keysdefinition.md">Md5KeysDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::RouterospfOspfinterface
Properties:
    <a href="#authentication" title="Authentication">Authentication</a>: <i>String</i>
    <a href="#authenticationkey" title="AuthenticationKey">AuthenticationKey</a>: <i>String</i>
    <a href="#bfd" title="Bfd">Bfd</a>: <i>String</i>
    <a href="#cost" title="Cost">Cost</a>: <i>Double</i>
    <a href="#databasefilterout" title="DatabaseFilterOut">DatabaseFilterOut</a>: <i>String</i>
    <a href="#deadinterval" title="DeadInterval">DeadInterval</a>: <i>Double</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
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
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
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

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

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

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Md5Keys

_Required_: No

_Type_: List of <a href="md5keysdefinition.md">Md5KeysDefinition</a>

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

