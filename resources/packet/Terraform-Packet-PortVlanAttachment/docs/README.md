# Terraform::Packet::PortVlanAttachment

CloudFormation equivalent of packet_port_vlan_attachment

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Packet::PortVlanAttachment",
    "Properties" : {
        "<a href="#deviceid" title="DeviceId">DeviceId</a>" : <i>String</i>,
        "<a href="#forcebond" title="ForceBond">ForceBond</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#native" title="Native">Native</a>: <i>Boolean</i>
    <a href="#portname" title="PortName">PortName</a>: <i>String</i>
    <a href="#vlanvnid" title="VlanVnid">VlanVnid</a>: <i>Double</i>
</pre>

## Properties

#### DeviceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceBond

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Native

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanVnid

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

#### PortId

Returns the &lt;code&gt;PortId&lt;/code&gt; value.

#### VlanId

Returns the &lt;code&gt;VlanId&lt;/code&gt; value.

