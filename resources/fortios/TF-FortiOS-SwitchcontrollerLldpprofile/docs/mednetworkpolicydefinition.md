# TF::FortiOS::SwitchcontrollerLldpprofile MedNetworkPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#assignvlan" title="AssignVlan">AssignVlan</a>" : <i>String</i>,
    "<a href="#dscp" title="Dscp">Dscp</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#vlan" title="Vlan">Vlan</a>" : <i>Double</i>,
    "<a href="#vlanintf" title="VlanIntf">VlanIntf</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#assignvlan" title="AssignVlan">AssignVlan</a>: <i>String</i>
<a href="#dscp" title="Dscp">Dscp</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#vlan" title="Vlan">Vlan</a>: <i>Double</i>
<a href="#vlanintf" title="VlanIntf">VlanIntf</a>: <i>String</i>
</pre>

## Properties

#### AssignVlan

Enable/disable VLAN assignment when this profile is applied on managed FortiSwitch port. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dscp

Advertised Differentiated Services Code Point (DSCP) value, a packet header value indicating the level of service requested for traffic, such as high priority or best effort delivery.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Policy type name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Advertised Layer 2 priority (0 - 7; from lowest to highest priority).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable or disable this TLV. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vlan

ID of VLAN to advertise, if configured on port (0 - 4094, 0 = priority tag).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanIntf

VLAN interface to advertise; if configured on port.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

