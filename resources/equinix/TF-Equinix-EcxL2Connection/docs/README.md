# TF::Equinix::EcxL2Connection

Resource `equinix_ecx_l2_connection` allows creation and management of Equinix Fabric
layer 2 connections.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Equinix::EcxL2Connection",
    "Properties" : {
        "<a href="#authorizationkey" title="AuthorizationKey">AuthorizationKey</a>" : <i>String</i>,
        "<a href="#deviceinterfaceid" title="DeviceInterfaceId">DeviceInterfaceId</a>" : <i>Double</i>,
        "<a href="#deviceuuid" title="DeviceUuid">DeviceUuid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namedtag" title="NamedTag">NamedTag</a>" : <i>String</i>,
        "<a href="#notifications" title="Notifications">Notifications</a>" : <i>[ String, ... ]</i>,
        "<a href="#portuuid" title="PortUuid">PortUuid</a>" : <i>String</i>,
        "<a href="#profileuuid" title="ProfileUuid">ProfileUuid</a>" : <i>String</i>,
        "<a href="#purchaseordernumber" title="PurchaseOrderNumber">PurchaseOrderNumber</a>" : <i>String</i>,
        "<a href="#sellermetrocode" title="SellerMetroCode">SellerMetroCode</a>" : <i>String</i>,
        "<a href="#sellerregion" title="SellerRegion">SellerRegion</a>" : <i>String</i>,
        "<a href="#speed" title="Speed">Speed</a>" : <i>Double</i>,
        "<a href="#speedunit" title="SpeedUnit">SpeedUnit</a>" : <i>String</i>,
        "<a href="#vlanctag" title="VlanCtag">VlanCtag</a>" : <i>Double</i>,
        "<a href="#vlanstag" title="VlanStag">VlanStag</a>" : <i>Double</i>,
        "<a href="#zsideportuuid" title="ZsidePortUuid">ZsidePortUuid</a>" : <i>String</i>,
        "<a href="#zsidevlanctag" title="ZsideVlanCtag">ZsideVlanCtag</a>" : <i>Double</i>,
        "<a href="#zsidevlanstag" title="ZsideVlanStag">ZsideVlanStag</a>" : <i>Double</i>,
        "<a href="#additionalinfo" title="AdditionalInfo">AdditionalInfo</a>" : <i>[ <a href="additionalinfodefinition.md">AdditionalInfoDefinition</a>, ... ]</i>,
        "<a href="#secondaryconnection" title="SecondaryConnection">SecondaryConnection</a>" : <i>[ <a href="secondaryconnectiondefinition.md">SecondaryConnectionDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Equinix::EcxL2Connection
Properties:
    <a href="#authorizationkey" title="AuthorizationKey">AuthorizationKey</a>: <i>String</i>
    <a href="#deviceinterfaceid" title="DeviceInterfaceId">DeviceInterfaceId</a>: <i>Double</i>
    <a href="#deviceuuid" title="DeviceUuid">DeviceUuid</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namedtag" title="NamedTag">NamedTag</a>: <i>String</i>
    <a href="#notifications" title="Notifications">Notifications</a>: <i>
      - String</i>
    <a href="#portuuid" title="PortUuid">PortUuid</a>: <i>String</i>
    <a href="#profileuuid" title="ProfileUuid">ProfileUuid</a>: <i>String</i>
    <a href="#purchaseordernumber" title="PurchaseOrderNumber">PurchaseOrderNumber</a>: <i>String</i>
    <a href="#sellermetrocode" title="SellerMetroCode">SellerMetroCode</a>: <i>String</i>
    <a href="#sellerregion" title="SellerRegion">SellerRegion</a>: <i>String</i>
    <a href="#speed" title="Speed">Speed</a>: <i>Double</i>
    <a href="#speedunit" title="SpeedUnit">SpeedUnit</a>: <i>String</i>
    <a href="#vlanctag" title="VlanCtag">VlanCtag</a>: <i>Double</i>
    <a href="#vlanstag" title="VlanStag">VlanStag</a>: <i>Double</i>
    <a href="#zsideportuuid" title="ZsidePortUuid">ZsidePortUuid</a>: <i>String</i>
    <a href="#zsidevlanctag" title="ZsideVlanCtag">ZsideVlanCtag</a>: <i>Double</i>
    <a href="#zsidevlanstag" title="ZsideVlanStag">ZsideVlanStag</a>: <i>Double</i>
    <a href="#additionalinfo" title="AdditionalInfo">AdditionalInfo</a>: <i>
      - <a href="additionalinfodefinition.md">AdditionalInfoDefinition</a></i>
    <a href="#secondaryconnection" title="SecondaryConnection">SecondaryConnection</a>: <i>
      - <a href="secondaryconnectiondefinition.md">SecondaryConnectionDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AuthorizationKey

Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceInterfaceId

Applicable with `device_uuid`, identifier of
network interface on a given device, used for a connection. If not specified then
first available interface will be selected.
- `vlan_stag` - (Required when port_uuid is set) S-Tag/Outer-Tag of the connection
\- a numeric character ranging from 2 - 4094.
- `vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection - a numeric
character ranging from 2 - 4094.
- `named_tag` - (Optional) The type of peering to set up in case when connecting
to Azure Express Route. One of _"Public"_, _"Private"_, _"Microsoft"_, _"Manual"_
- `additional_info` - (Optional) one or more additional information key-value objects
- `name` - (Required) additional information key
- `value` - (Required) additional information value
- `zside_port_uuid` - (Optional) Unique identifier of the port on the remote side
(z-side).
- `zside_vlan_stag` - (Optional) S-Tag/Outer-Tag of the connection on the remote
side (z side).
- `zside_vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection on the remote
side (z-side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
remote side (z-side).
- `authorization_key` - (Optional) Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceUuid

Unique identifier of
the Network Edge virtual device from which the connection would originate.
- `device_interface_id` - (Optional) Applicable with `device_uuid`, identifier of
network interface on a given device, used for a connection. If not specified then
first available interface will be selected.
- `vlan_stag` - (Required when port_uuid is set) S-Tag/Outer-Tag of the connection
\- a numeric character ranging from 2 - 4094.
- `vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection - a numeric
character ranging from 2 - 4094.
- `named_tag` - (Optional) The type of peering to set up in case when connecting
to Azure Express Route. One of _"Public"_, _"Private"_, _"Microsoft"_, _"Manual"_
- `additional_info` - (Optional) one or more additional information key-value objects
- `name` - (Required) additional information key
- `value` - (Required) additional information value
- `zside_port_uuid` - (Optional) Unique identifier of the port on the remote side
(z-side).
- `zside_vlan_stag` - (Optional) S-Tag/Outer-Tag of the connection on the remote
side (z side).
- `zside_vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection on the remote
side (z-side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
remote side (z-side).
- `authorization_key` - (Optional) Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

additional information key
- `value` - (Required) additional information value
- `zside_port_uuid` - (Optional) Unique identifier of the port on the remote side
(z-side).
- `zside_vlan_stag` - (Optional) S-Tag/Outer-Tag of the connection on the remote
side (z side).
- `zside_vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection on the remote
side (z-side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
remote side (z-side).
- `authorization_key` - (Optional) Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamedTag

The type of peering to set up in case when connecting
to Azure Express Route. One of _"Public"_, _"Private"_, _"Microsoft"_, _"Manual"_
- `additional_info` - (Optional) one or more additional information key-value objects
- `name` - (Required) additional information key
- `value` - (Required) additional information value
- `zside_port_uuid` - (Optional) Unique identifier of the port on the remote side
(z-side).
- `zside_vlan_stag` - (Optional) S-Tag/Outer-Tag of the connection on the remote
side (z side).
- `zside_vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection on the remote
side (z-side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
remote side (z-side).
- `authorization_key` - (Optional) Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notifications

A list of email addresses used for sending connection
update notifications.
- `purchase_order_number` - (Optional) Connection's purchase order number to reflect
on the invoice
- `port_uuid` - (Required when device_uuid is not set) Unique identifier of
the buyer's port from which the connection would originate.
- `device_uuid` - (Required when port_uuid is not set) Unique identifier of
the Network Edge virtual device from which the connection would originate.
- `device_interface_id` - (Optional) Applicable with `device_uuid`, identifier of
network interface on a given device, used for a connection. If not specified then
first available interface will be selected.
- `vlan_stag` - (Required when port_uuid is set) S-Tag/Outer-Tag of the connection
\- a numeric character ranging from 2 - 4094.
- `vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection - a numeric
character ranging from 2 - 4094.
- `named_tag` - (Optional) The type of peering to set up in case when connecting
to Azure Express Route. One of _"Public"_, _"Private"_, _"Microsoft"_, _"Manual"_
- `additional_info` - (Optional) one or more additional information key-value objects
- `name` - (Required) additional information key
- `value` - (Required) additional information value
- `zside_port_uuid` - (Optional) Unique identifier of the port on the remote side
(z-side).
- `zside_vlan_stag` - (Optional) S-Tag/Outer-Tag of the connection on the remote
side (z side).
- `zside_vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection on the remote
side (z-side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
remote side (z-side).
- `authorization_key` - (Optional) Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortUuid

Unique identifier of
the buyer's port from which the connection would originate.
- `device_uuid` - (Required when port_uuid is not set) Unique identifier of
the Network Edge virtual device from which the connection would originate.
- `device_interface_id` - (Optional) Applicable with `device_uuid`, identifier of
network interface on a given device, used for a connection. If not specified then
first available interface will be selected.
- `vlan_stag` - (Required when port_uuid is set) S-Tag/Outer-Tag of the connection
\- a numeric character ranging from 2 - 4094.
- `vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection - a numeric
character ranging from 2 - 4094.
- `named_tag` - (Optional) The type of peering to set up in case when connecting
to Azure Express Route. One of _"Public"_, _"Private"_, _"Microsoft"_, _"Manual"_
- `additional_info` - (Optional) one or more additional information key-value objects
- `name` - (Required) additional information key
- `value` - (Required) additional information value
- `zside_port_uuid` - (Optional) Unique identifier of the port on the remote side
(z-side).
- `zside_vlan_stag` - (Optional) S-Tag/Outer-Tag of the connection on the remote
side (z side).
- `zside_vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection on the remote
side (z-side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
remote side (z-side).
- `authorization_key` - (Optional) Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileUuid

Unique identifier of the service provider's profile.
- `speed` - (Required) Speed/Bandwidth to be allocated to the connection.
- `speed_unit` - (Required) Unit of the speed/bandwidth to be allocated
to the connection.
- `notifications` - (Required) A list of email addresses used for sending connection
update notifications.
- `purchase_order_number` - (Optional) Connection's purchase order number to reflect
on the invoice
- `port_uuid` - (Required when device_uuid is not set) Unique identifier of
the buyer's port from which the connection would originate.
- `device_uuid` - (Required when port_uuid is not set) Unique identifier of
the Network Edge virtual device from which the connection would originate.
- `device_interface_id` - (Optional) Applicable with `device_uuid`, identifier of
network interface on a given device, used for a connection. If not specified then
first available interface will be selected.
- `vlan_stag` - (Required when port_uuid is set) S-Tag/Outer-Tag of the connection
\- a numeric character ranging from 2 - 4094.
- `vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection - a numeric
character ranging from 2 - 4094.
- `named_tag` - (Optional) The type of peering to set up in case when connecting
to Azure Express Route. One of _"Public"_, _"Private"_, _"Microsoft"_, _"Manual"_
- `additional_info` - (Optional) one or more additional information key-value objects
- `name` - (Required) additional information key
- `value` - (Required) additional information value
- `zside_port_uuid` - (Optional) Unique identifier of the port on the remote side
(z-side).
- `zside_vlan_stag` - (Optional) S-Tag/Outer-Tag of the connection on the remote
side (z side).
- `zside_vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection on the remote
side (z-side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
remote side (z-side).
- `authorization_key` - (Optional) Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PurchaseOrderNumber

Connection's purchase order number to reflect
on the invoice
- `port_uuid` - (Required when device_uuid is not set) Unique identifier of
the buyer's port from which the connection would originate.
- `device_uuid` - (Required when port_uuid is not set) Unique identifier of
the Network Edge virtual device from which the connection would originate.
- `device_interface_id` - (Optional) Applicable with `device_uuid`, identifier of
network interface on a given device, used for a connection. If not specified then
first available interface will be selected.
- `vlan_stag` - (Required when port_uuid is set) S-Tag/Outer-Tag of the connection
\- a numeric character ranging from 2 - 4094.
- `vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection - a numeric
character ranging from 2 - 4094.
- `named_tag` - (Optional) The type of peering to set up in case when connecting
to Azure Express Route. One of _"Public"_, _"Private"_, _"Microsoft"_, _"Manual"_
- `additional_info` - (Optional) one or more additional information key-value objects
- `name` - (Required) additional information key
- `value` - (Required) additional information value
- `zside_port_uuid` - (Optional) Unique identifier of the port on the remote side
(z-side).
- `zside_vlan_stag` - (Optional) S-Tag/Outer-Tag of the connection on the remote
side (z side).
- `zside_vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection on the remote
side (z-side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
remote side (z-side).
- `authorization_key` - (Optional) Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SellerMetroCode

The metro code that denotes the connection’s
remote side (z-side).
- `authorization_key` - (Optional) Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SellerRegion

The region in which the seller port resides.
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
remote side (z-side).
- `authorization_key` - (Optional) Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Speed

Speed/Bandwidth to be allocated to the connection.
- `speed_unit` - (Required) Unit of the speed/bandwidth to be allocated
to the connection.
- `notifications` - (Required) A list of email addresses used for sending connection
update notifications.
- `purchase_order_number` - (Optional) Connection's purchase order number to reflect
on the invoice
- `port_uuid` - (Required when device_uuid is not set) Unique identifier of
the buyer's port from which the connection would originate.
- `device_uuid` - (Required when port_uuid is not set) Unique identifier of
the Network Edge virtual device from which the connection would originate.
- `device_interface_id` - (Optional) Applicable with `device_uuid`, identifier of
network interface on a given device, used for a connection. If not specified then
first available interface will be selected.
- `vlan_stag` - (Required when port_uuid is set) S-Tag/Outer-Tag of the connection
\- a numeric character ranging from 2 - 4094.
- `vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection - a numeric
character ranging from 2 - 4094.
- `named_tag` - (Optional) The type of peering to set up in case when connecting
to Azure Express Route. One of _"Public"_, _"Private"_, _"Microsoft"_, _"Manual"_
- `additional_info` - (Optional) one or more additional information key-value objects
- `name` - (Required) additional information key
- `value` - (Required) additional information value
- `zside_port_uuid` - (Optional) Unique identifier of the port on the remote side
(z-side).
- `zside_vlan_stag` - (Optional) S-Tag/Outer-Tag of the connection on the remote
side (z side).
- `zside_vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection on the remote
side (z-side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
remote side (z-side).
- `authorization_key` - (Optional) Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpeedUnit

Unit of the speed/bandwidth to be allocated
to the connection.
- `notifications` - (Required) A list of email addresses used for sending connection
update notifications.
- `purchase_order_number` - (Optional) Connection's purchase order number to reflect
on the invoice
- `port_uuid` - (Required when device_uuid is not set) Unique identifier of
the buyer's port from which the connection would originate.
- `device_uuid` - (Required when port_uuid is not set) Unique identifier of
the Network Edge virtual device from which the connection would originate.
- `device_interface_id` - (Optional) Applicable with `device_uuid`, identifier of
network interface on a given device, used for a connection. If not specified then
first available interface will be selected.
- `vlan_stag` - (Required when port_uuid is set) S-Tag/Outer-Tag of the connection
\- a numeric character ranging from 2 - 4094.
- `vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection - a numeric
character ranging from 2 - 4094.
- `named_tag` - (Optional) The type of peering to set up in case when connecting
to Azure Express Route. One of _"Public"_, _"Private"_, _"Microsoft"_, _"Manual"_
- `additional_info` - (Optional) one or more additional information key-value objects
- `name` - (Required) additional information key
- `value` - (Required) additional information value
- `zside_port_uuid` - (Optional) Unique identifier of the port on the remote side
(z-side).
- `zside_vlan_stag` - (Optional) S-Tag/Outer-Tag of the connection on the remote
side (z side).
- `zside_vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection on the remote
side (z-side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
remote side (z-side).
- `authorization_key` - (Optional) Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanCtag

C-Tag/Inner-Tag of the connection - a numeric
character ranging from 2 - 4094.
- `named_tag` - (Optional) The type of peering to set up in case when connecting
to Azure Express Route. One of _"Public"_, _"Private"_, _"Microsoft"_, _"Manual"_
- `additional_info` - (Optional) one or more additional information key-value objects
- `name` - (Required) additional information key
- `value` - (Required) additional information value
- `zside_port_uuid` - (Optional) Unique identifier of the port on the remote side
(z-side).
- `zside_vlan_stag` - (Optional) S-Tag/Outer-Tag of the connection on the remote
side (z side).
- `zside_vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection on the remote
side (z-side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
remote side (z-side).
- `authorization_key` - (Optional) Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanStag

S-Tag/Outer-Tag of the connection
\- a numeric character ranging from 2 - 4094.
- `vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection - a numeric
character ranging from 2 - 4094.
- `named_tag` - (Optional) The type of peering to set up in case when connecting
to Azure Express Route. One of _"Public"_, _"Private"_, _"Microsoft"_, _"Manual"_
- `additional_info` - (Optional) one or more additional information key-value objects
- `name` - (Required) additional information key
- `value` - (Required) additional information value
- `zside_port_uuid` - (Optional) Unique identifier of the port on the remote side
(z-side).
- `zside_vlan_stag` - (Optional) S-Tag/Outer-Tag of the connection on the remote
side (z side).
- `zside_vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection on the remote
side (z-side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
remote side (z-side).
- `authorization_key` - (Optional) Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZsidePortUuid

Unique identifier of the port on the remote side
(z-side).
- `zside_vlan_stag` - (Optional) S-Tag/Outer-Tag of the connection on the remote
side (z side).
- `zside_vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection on the remote
side (z-side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
remote side (z-side).
- `authorization_key` - (Optional) Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZsideVlanCtag

C-Tag/Inner-Tag of the connection on the remote
side (z-side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
remote side (z-side).
- `authorization_key` - (Optional) Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZsideVlanStag

S-Tag/Outer-Tag of the connection on the remote
side (z side).
- `zside_vlan_ctag` - (Optional) C-Tag/Inner-Tag of the connection on the remote
side (z-side).
- `seller_region` - (Optional) The region in which the seller port resides.
- `seller_metro_code` - (Optional) The metro code that denotes the connection’s
remote side (z-side).
- `authorization_key` - (Optional) Text field used to authorize connection on the
provider side. Value depends on a provider service profile used for connection.
- `secondary_connection` - (Optional) Definition of secondary connection for
redundant, HA connectivity.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalInfo

_Required_: No

_Type_: List of <a href="additionalinfodefinition.md">AdditionalInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryConnection

_Required_: No

_Type_: List of <a href="secondaryconnectiondefinition.md">SecondaryConnectionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### ProviderStatus

Returns the <code>ProviderStatus</code> value.

#### RedundancyType

Returns the <code>RedundancyType</code> value.

#### RedundantUuid

Returns the <code>RedundantUuid</code> value.

#### Status

Returns the <code>Status</code> value.

#### Uuid

Returns the <code>Uuid</code> value.

