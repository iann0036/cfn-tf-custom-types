# TF::OpenNebula::VirtualNetwork

Provides an OpenNebula virtual network resource.

This resource allows you to manage virtual networks on your OpenNebula clusters. When applied,
a new virtual network is created. When destroyed, that virtual network is removed.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpenNebula::VirtualNetwork",
    "Properties" : {
        "<a href="#automaticvlanid" title="AutomaticVlanId">AutomaticVlanId</a>" : <i>Boolean</i>,
        "<a href="#bridge" title="Bridge">Bridge</a>" : <i>String</i>,
        "<a href="#clusters" title="Clusters">Clusters</a>" : <i>[ Double, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dns" title="Dns">Dns</a>" : <i>String</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#guestmtu" title="GuestMtu">GuestMtu</a>" : <i>Double</i>,
        "<a href="#holdips" title="HoldIps">HoldIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#holdsize" title="HoldSize">HoldSize</a>" : <i>Double</i>,
        "<a href="#iphold" title="IpHold">IpHold</a>" : <i>String</i>,
        "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkmask" title="NetworkMask">NetworkMask</a>" : <i>String</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>String</i>,
        "<a href="#physicaldevice" title="PhysicalDevice">PhysicalDevice</a>" : <i>String</i>,
        "<a href="#reservationsize" title="ReservationSize">ReservationSize</a>" : <i>Double</i>,
        "<a href="#reservationvnet" title="ReservationVnet">ReservationVnet</a>" : <i>Double</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ Double, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>String</i>,
        "<a href="#ar" title="Ar">Ar</a>" : <i>[ <a href="ardefinition.md">ArDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpenNebula::VirtualNetwork
Properties:
    <a href="#automaticvlanid" title="AutomaticVlanId">AutomaticVlanId</a>: <i>Boolean</i>
    <a href="#bridge" title="Bridge">Bridge</a>: <i>String</i>
    <a href="#clusters" title="Clusters">Clusters</a>: <i>
      - Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dns" title="Dns">Dns</a>: <i>String</i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#guestmtu" title="GuestMtu">GuestMtu</a>: <i>Double</i>
    <a href="#holdips" title="HoldIps">HoldIps</a>: <i>
      - String</i>
    <a href="#holdsize" title="HoldSize">HoldSize</a>: <i>Double</i>
    <a href="#iphold" title="IpHold">IpHold</a>: <i>String</i>
    <a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkmask" title="NetworkMask">NetworkMask</a>: <i>String</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>String</i>
    <a href="#physicaldevice" title="PhysicalDevice">PhysicalDevice</a>: <i>String</i>
    <a href="#reservationsize" title="ReservationSize">ReservationSize</a>: <i>Double</i>
    <a href="#reservationvnet" title="ReservationVnet">ReservationVnet</a>: <i>Double</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vlanid" title="VlanId">VlanId</a>: <i>String</i>
    <a href="#ar" title="Ar">Ar</a>: <i>
      - <a href="ardefinition.md">ArDefinition</a></i>
</pre>

## Properties

#### AutomaticVlanId

Flag to let OpenNebula scheduler to attribute the VLAN ID. Conflicts with `reservation_vnet`, `reservation_size` and `vlan_id`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bridge

Name of the bridge interface to which the virtual network should be associated. Conflicts with `reservation_vnet` and `reservation_size`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Clusters

List of cluster IDs where the virtual network can be use. Conflicts with `reservation_vnet` and `reservation_size`.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the virtual network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns

Text String containing a comma separated list of DNS IPs. Conflicts with `reservation_vnet` and `reservation_size`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

IP of the gateway. Conflicts with `reservation_vnet` and `reservation_size`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

Name of the group which owns the virtual network. Defaults to the caller primary group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestMtu

MTU of the network caord on the virtual machine. **Cannot be greater than `mtu`**. Defaults to `1500`. Conflicts with `reservation_vnet` and `reservation_size`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HoldIps

Hold Ips from any Address Range of the Virtual Network. The IP must be available to be held`. Conflicts with `reservation_vnet` and `reservation_size`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HoldSize

Carve a network reservation of this size from the reservation starting from `ip_hold`. Conflicts with `reservation_vnet` and `reservation_size`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpHold

Start IP of the range to be held. Conflicts with `reservation_vnet` and `reservation_size`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

Virtual network MTU. Defaults to `1500`. Conflicts with `reservation_vnet` and `reservation_size`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the virtual network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkMask

Network mask. Conflicts with `reservation_vnet` and `reservation_size`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

Permissions applied on virtual network. Defaults to the UMASK in OpenNebula (in UNIX Format: owner-group-other => Use-Manage-Admin).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhysicalDevice

Name of the physical device interface to which the virtual network should be associated. Conflicts with `reservation_vnet` and `reservation_size`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservationSize

Size (in address) reserved. Conflicts with all parameters excepted `name`, `description`, `permissions`, `security_groups` and `group`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservationVnet

ID of the parent virtual network to reserve from. Conflicts with all parameters excepted `name`, `description`, `permissions`, `security_groups` and `group`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

List of security group IDs to apply on the virtual network.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Virtual Network tags (Key = Value).

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Virtual network type. One of these: `dummy`, `bridge`'`fw`, `ebtables`, `802.1Q`, `vxlan` or `ovswitch`. Defaults to `bridge`. Conflicts with `reservation_vnet` and `reservation_size`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

ID of VLAN. Only if `type` is `802.1Q`, `vxlan` or `ovswitch`. Conflicts with `reservation_vnet`, `reservation_size` and `automatic_vlan_id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ar

_Required_: No

_Type_: List of <a href="ardefinition.md">ArDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Gid

Returns the <code>Gid</code> value.

#### Gname

Returns the <code>Gname</code> value.

#### Id

Returns the <code>Id</code> value.

#### Uid

Returns the <code>Uid</code> value.

#### Uname

Returns the <code>Uname</code> value.

