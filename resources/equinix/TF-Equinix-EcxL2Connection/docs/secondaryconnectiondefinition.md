# TF::Equinix::EcxL2Connection SecondaryConnectionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authorizationkey" title="AuthorizationKey">AuthorizationKey</a>" : <i>String</i>,
    "<a href="#deviceinterfaceid" title="DeviceInterfaceId">DeviceInterfaceId</a>" : <i>Double</i>,
    "<a href="#deviceuuid" title="DeviceUuid">DeviceUuid</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#portuuid" title="PortUuid">PortUuid</a>" : <i>String</i>,
    "<a href="#profileuuid" title="ProfileUuid">ProfileUuid</a>" : <i>String</i>,
    "<a href="#sellermetrocode" title="SellerMetroCode">SellerMetroCode</a>" : <i>String</i>,
    "<a href="#sellerregion" title="SellerRegion">SellerRegion</a>" : <i>String</i>,
    "<a href="#speed" title="Speed">Speed</a>" : <i>Double</i>,
    "<a href="#speedunit" title="SpeedUnit">SpeedUnit</a>" : <i>String</i>,
    "<a href="#vlanctag" title="VlanCtag">VlanCtag</a>" : <i>Double</i>,
    "<a href="#vlanstag" title="VlanStag">VlanStag</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#authorizationkey" title="AuthorizationKey">AuthorizationKey</a>: <i>String</i>
<a href="#deviceinterfaceid" title="DeviceInterfaceId">DeviceInterfaceId</a>: <i>Double</i>
<a href="#deviceuuid" title="DeviceUuid">DeviceUuid</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#portuuid" title="PortUuid">PortUuid</a>: <i>String</i>
<a href="#profileuuid" title="ProfileUuid">ProfileUuid</a>: <i>String</i>
<a href="#sellermetrocode" title="SellerMetroCode">SellerMetroCode</a>: <i>String</i>
<a href="#sellerregion" title="SellerRegion">SellerRegion</a>: <i>String</i>
<a href="#speed" title="Speed">Speed</a>: <i>Double</i>
<a href="#speedunit" title="SpeedUnit">SpeedUnit</a>: <i>String</i>
<a href="#vlanctag" title="VlanCtag">VlanCtag</a>: <i>Double</i>
<a href="#vlanstag" title="VlanStag">VlanStag</a>: <i>Double</i>
</pre>

## Properties

#### AuthorizationKey

Text field based on the service profile
you want to connect to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceInterfaceId

Applicable with `device_uuid`, identifier of
network interface on a given device. If not specified then first available interface
will be selected.
- `vlan_stag` - (Required when `port_uuid` is set)
- `vlan_ctag` - (Optional, can be set with `port_uuid`)
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
destination (Z side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `authorization_key` - (Optional) Text field based on the service profile
you want to connect to.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceUuid

Identifier of
the Network Edge virtual device from which the connection would originate.
- `device_interface_id` - (Optional) Applicable with `device_uuid`, identifier of
network interface on a given device. If not specified then first available interface
will be selected.
- `vlan_stag` - (Required when `port_uuid` is set)
- `vlan_ctag` - (Optional, can be set with `port_uuid`)
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
destination (Z side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `authorization_key` - (Optional) Text field based on the service profile
you want to connect to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

secondary connection name
- `speed` - (Optional) Speed/Bandwidth to be allocated to the connection.
- `speed_unit` - (Optional) Unit of the speed/bandwidth to be allocated
to the connection.
- `port_uuid` - (Required when `device_uuid` is not set) Identifier of
the buyer's port from which the connection would originate.
- `device_uuid` - (Required when `port_uuid` is not set) Identifier of
the Network Edge virtual device from which the connection would originate.
- `device_interface_id` - (Optional) Applicable with `device_uuid`, identifier of
network interface on a given device. If not specified then first available interface
will be selected.
- `vlan_stag` - (Required when `port_uuid` is set)
- `vlan_ctag` - (Optional, can be set with `port_uuid`)
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
destination (Z side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `authorization_key` - (Optional) Text field based on the service profile
you want to connect to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortUuid

Identifier of
the buyer's port from which the connection would originate.
- `device_uuid` - (Required when `port_uuid` is not set) Identifier of
the Network Edge virtual device from which the connection would originate.
- `device_interface_id` - (Optional) Applicable with `device_uuid`, identifier of
network interface on a given device. If not specified then first available interface
will be selected.
- `vlan_stag` - (Required when `port_uuid` is set)
- `vlan_ctag` - (Optional, can be set with `port_uuid`)
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
destination (Z side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `authorization_key` - (Optional) Text field based on the service profile
you want to connect to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SellerMetroCode

The metro code that denotes the connection’s
destination (Z side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `authorization_key` - (Optional) Text field based on the service profile
you want to connect to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SellerRegion

The region in which the seller port resides.
- `authorization_key` - (Optional) Text field based on the service profile
you want to connect to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Speed

Speed/Bandwidth to be allocated to the connection.
- `speed_unit` - (Optional) Unit of the speed/bandwidth to be allocated
to the connection.
- `port_uuid` - (Required when `device_uuid` is not set) Identifier of
the buyer's port from which the connection would originate.
- `device_uuid` - (Required when `port_uuid` is not set) Identifier of
the Network Edge virtual device from which the connection would originate.
- `device_interface_id` - (Optional) Applicable with `device_uuid`, identifier of
network interface on a given device. If not specified then first available interface
will be selected.
- `vlan_stag` - (Required when `port_uuid` is set)
- `vlan_ctag` - (Optional, can be set with `port_uuid`)
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
destination (Z side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `authorization_key` - (Optional) Text field based on the service profile
you want to connect to.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpeedUnit

Unit of the speed/bandwidth to be allocated
to the connection.
- `port_uuid` - (Required when `device_uuid` is not set) Identifier of
the buyer's port from which the connection would originate.
- `device_uuid` - (Required when `port_uuid` is not set) Identifier of
the Network Edge virtual device from which the connection would originate.
- `device_interface_id` - (Optional) Applicable with `device_uuid`, identifier of
network interface on a given device. If not specified then first available interface
will be selected.
- `vlan_stag` - (Required when `port_uuid` is set)
- `vlan_ctag` - (Optional, can be set with `port_uuid`)
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
destination (Z side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `authorization_key` - (Optional) Text field based on the service profile
you want to connect to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanCtag

- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
destination (Z side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `authorization_key` - (Optional) Text field based on the service profile
you want to connect to.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanStag

- `vlan_ctag` - (Optional, can be set with `port_uuid`)
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
destination (Z side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `authorization_key` - (Optional) Text field based on the service profile
you want to connect to.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

