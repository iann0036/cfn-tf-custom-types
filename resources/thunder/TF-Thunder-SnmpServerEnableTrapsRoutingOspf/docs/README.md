# TF::Thunder::SnmpServerEnableTrapsRoutingOspf

`thunder_snmp_server_enable_traps_routing_ospf` Provides details about thunder snmp server enable traps routing ospf

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SnmpServerEnableTrapsRoutingOspf",
    "Properties" : {
        "<a href="#ospfifauthfailure" title="OspfIfAuthFailure">OspfIfAuthFailure</a>" : <i>Double</i>,
        "<a href="#ospfifconfigerror" title="OspfIfConfigError">OspfIfConfigError</a>" : <i>Double</i>,
        "<a href="#ospfifrxbadpacket" title="OspfIfRxBadPacket">OspfIfRxBadPacket</a>" : <i>Double</i>,
        "<a href="#ospfifstatechange" title="OspfIfStateChange">OspfIfStateChange</a>" : <i>Double</i>,
        "<a href="#ospflsdbapproachingoverflow" title="OspfLsdbApproachingOverflow">OspfLsdbApproachingOverflow</a>" : <i>Double</i>,
        "<a href="#ospflsdboverflow" title="OspfLsdbOverflow">OspfLsdbOverflow</a>" : <i>Double</i>,
        "<a href="#ospfmaxagelsa" title="OspfMaxAgeLsa">OspfMaxAgeLsa</a>" : <i>Double</i>,
        "<a href="#ospfnbrstatechange" title="OspfNbrStateChange">OspfNbrStateChange</a>" : <i>Double</i>,
        "<a href="#ospforiginatelsa" title="OspfOriginateLsa">OspfOriginateLsa</a>" : <i>Double</i>,
        "<a href="#ospftxretransmit" title="OspfTxRetransmit">OspfTxRetransmit</a>" : <i>Double</i>,
        "<a href="#ospfvirtifauthfailure" title="OspfVirtIfAuthFailure">OspfVirtIfAuthFailure</a>" : <i>Double</i>,
        "<a href="#ospfvirtifconfigerror" title="OspfVirtIfConfigError">OspfVirtIfConfigError</a>" : <i>Double</i>,
        "<a href="#ospfvirtifrxbadpacket" title="OspfVirtIfRxBadPacket">OspfVirtIfRxBadPacket</a>" : <i>Double</i>,
        "<a href="#ospfvirtifstatechange" title="OspfVirtIfStateChange">OspfVirtIfStateChange</a>" : <i>Double</i>,
        "<a href="#ospfvirtiftxretransmit" title="OspfVirtIfTxRetransmit">OspfVirtIfTxRetransmit</a>" : <i>Double</i>,
        "<a href="#ospfvirtnbrstatechange" title="OspfVirtNbrStateChange">OspfVirtNbrStateChange</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SnmpServerEnableTrapsRoutingOspf
Properties:
    <a href="#ospfifauthfailure" title="OspfIfAuthFailure">OspfIfAuthFailure</a>: <i>Double</i>
    <a href="#ospfifconfigerror" title="OspfIfConfigError">OspfIfConfigError</a>: <i>Double</i>
    <a href="#ospfifrxbadpacket" title="OspfIfRxBadPacket">OspfIfRxBadPacket</a>: <i>Double</i>
    <a href="#ospfifstatechange" title="OspfIfStateChange">OspfIfStateChange</a>: <i>Double</i>
    <a href="#ospflsdbapproachingoverflow" title="OspfLsdbApproachingOverflow">OspfLsdbApproachingOverflow</a>: <i>Double</i>
    <a href="#ospflsdboverflow" title="OspfLsdbOverflow">OspfLsdbOverflow</a>: <i>Double</i>
    <a href="#ospfmaxagelsa" title="OspfMaxAgeLsa">OspfMaxAgeLsa</a>: <i>Double</i>
    <a href="#ospfnbrstatechange" title="OspfNbrStateChange">OspfNbrStateChange</a>: <i>Double</i>
    <a href="#ospforiginatelsa" title="OspfOriginateLsa">OspfOriginateLsa</a>: <i>Double</i>
    <a href="#ospftxretransmit" title="OspfTxRetransmit">OspfTxRetransmit</a>: <i>Double</i>
    <a href="#ospfvirtifauthfailure" title="OspfVirtIfAuthFailure">OspfVirtIfAuthFailure</a>: <i>Double</i>
    <a href="#ospfvirtifconfigerror" title="OspfVirtIfConfigError">OspfVirtIfConfigError</a>: <i>Double</i>
    <a href="#ospfvirtifrxbadpacket" title="OspfVirtIfRxBadPacket">OspfVirtIfRxBadPacket</a>: <i>Double</i>
    <a href="#ospfvirtifstatechange" title="OspfVirtIfStateChange">OspfVirtIfStateChange</a>: <i>Double</i>
    <a href="#ospfvirtiftxretransmit" title="OspfVirtIfTxRetransmit">OspfVirtIfTxRetransmit</a>: <i>Double</i>
    <a href="#ospfvirtnbrstatechange" title="OspfVirtNbrStateChange">OspfVirtNbrStateChange</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### OspfIfAuthFailure

Enable ospfIfAuthFailure traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfIfConfigError

Enable ospfIfConfigError traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfIfRxBadPacket

Enable ospfIfRxBadPacket traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfIfStateChange

Enable ospfIfStateChange traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfLsdbApproachingOverflow

Enable ospfLsdbApproachingOverflow traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfLsdbOverflow

Enable ospfLsdbOverflow traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfMaxAgeLsa

Enable ospfMaxAgeLsa traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfNbrStateChange

Enable ospfNbrStateChange traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfOriginateLsa

Enable ospfOriginateLsa traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfTxRetransmit

Enable ospfTxRetransmit traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfVirtIfAuthFailure

Enable ospfVirtIfAuthFailure traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfVirtIfConfigError

Enable ospfVirtIfConfigError traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfVirtIfRxBadPacket

Enable ospfVirtIfRxBadPacket traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfVirtIfStateChange

Enable ospfVirtIfStateChange traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfVirtIfTxRetransmit

Enable ospfVirtIfTxRetransmit traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfVirtNbrStateChange

Enable ospfVirtNbrStateChange traps.

_Required_: No

_Type_: Double

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

