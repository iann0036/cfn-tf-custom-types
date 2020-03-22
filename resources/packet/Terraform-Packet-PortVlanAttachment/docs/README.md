# Terraform::Packet::PortVlanAttachment

Provides a resource to attach device ports to VLANs.

Device and VLAN must be in the same facility.

If you need this resource to add the port back to bond on removal, set `force_bond = true`.

To learn more about Layer 2 networking in Packet, refer to
* https://www.packet.com/resources/guides/layer-2-configurations/ 
* https://www.packet.com/developers/docs/network/advanced/layer-2/

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Packet::PortVlanAttachment",
    "Properties" : {
        "<a href="#deviceid" title="DeviceId">DeviceId</a>" : <i>String</i>,
        "<a href="#forcebond" title="ForceBond">ForceBond</a>" : <i>Boolean</i>,
        "<a href="#native" title="Native">Native</a>" : <i>Boolean</i>,
        "<a href="#portname" title="PortName">PortName</a>" : <i>String</i>,
        "<a href="#vlanvnid" title="VlanVnid">VlanVnid</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Packet::PortVlanAttachment
Properties:
    <a href="#deviceid" title="DeviceId">DeviceId</a>: <i>String</i>
    <a href="#forcebond" title="ForceBond">ForceBond</a>: <i>Boolean</i>
    <a href="#native" title="Native">Native</a>: <i>Boolean</i>
    <a href="#portname" title="PortName">PortName</a>: <i>String</i>
    <a href="#vlanvnid" title="VlanVnid">VlanVnid</a>: <i>Double</i>
</pre>

## Properties

#### DeviceId

ID of device to be assigned to the VLAN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceBond

Add port back to the bond when this resource is removed. Default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Native

Mark this VLAN a native VLAN on the port. This can be used only if this assignment assigns second or further VLAN to the port. To ensure that this attachment is not first on a port, you can use `depends_on` pointing to another packet_port_vlan_attachment, just like in the layer2-individual example above.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortName

Name of network port to be assigned to the VLAN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanVnid

VXLAN Network Identifier, integer.

_Required_: Yes

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

#### PortId

Returns the <code>PortId</code> value.

#### VlanId

Returns the <code>VlanId</code> value.

