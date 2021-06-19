# TF::FortiOS::IpsSettings

Configure IPS VDOM parameter.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::IpsSettings",
    "Properties" : {
        "<a href="#ipspacketquota" title="IpsPacketQuota">IpsPacketQuota</a>" : <i>Double</i>,
        "<a href="#packetloghistory" title="PacketLogHistory">PacketLogHistory</a>" : <i>Double</i>,
        "<a href="#packetlogmemory" title="PacketLogMemory">PacketLogMemory</a>" : <i>Double</i>,
        "<a href="#packetlogpostattack" title="PacketLogPostAttack">PacketLogPostAttack</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::IpsSettings
Properties:
    <a href="#ipspacketquota" title="IpsPacketQuota">IpsPacketQuota</a>: <i>Double</i>
    <a href="#packetloghistory" title="PacketLogHistory">PacketLogHistory</a>: <i>Double</i>
    <a href="#packetlogmemory" title="PacketLogMemory">PacketLogMemory</a>: <i>Double</i>
    <a href="#packetlogpostattack" title="PacketLogPostAttack">PacketLogPostAttack</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### IpsPacketQuota

Maximum amount of disk space in MB for logged packets when logging to disk. Range depends on disk size.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketLogHistory

Number of packets to capture before and including the one in which the IPS signature is detected (1 - 255).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketLogMemory

Maximum memory can be used by packet log (64 - 8192 kB).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketLogPostAttack

Number of packets to log after the IPS signature is detected (0 - 255).

_Required_: No

_Type_: Double

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

