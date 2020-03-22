# Terraform::AzureRM::VirtualNetworkGatewayConnection

Manages a connection in an existing Virtual Network Gateway.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::VirtualNetworkGatewayConnection",
    "Properties" : {
        "<a href="#authorizationkey" title="AuthorizationKey">AuthorizationKey</a>" : <i>String</i>,
        "<a href="#connectionprotocol" title="ConnectionProtocol">ConnectionProtocol</a>" : <i>String</i>,
        "<a href="#enablebgp" title="EnableBgp">EnableBgp</a>" : <i>Boolean</i>,
        "<a href="#expressroutecircuitid" title="ExpressRouteCircuitId">ExpressRouteCircuitId</a>" : <i>String</i>,
        "<a href="#expressroutegatewaybypass" title="ExpressRouteGatewayBypass">ExpressRouteGatewayBypass</a>" : <i>Boolean</i>,
        "<a href="#localnetworkgatewayid" title="LocalNetworkGatewayId">LocalNetworkGatewayId</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#peervirtualnetworkgatewayid" title="PeerVirtualNetworkGatewayId">PeerVirtualNetworkGatewayId</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#routingweight" title="RoutingWeight">RoutingWeight</a>" : <i>Double</i>,
        "<a href="#sharedkey" title="SharedKey">SharedKey</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#usepolicybasedtrafficselectors" title="UsePolicyBasedTrafficSelectors">UsePolicyBasedTrafficSelectors</a>" : <i>Boolean</i>,
        "<a href="#virtualnetworkgatewayid" title="VirtualNetworkGatewayId">VirtualNetworkGatewayId</a>" : <i>String</i>,
        "<a href="#ipsecpolicy" title="IpsecPolicy">IpsecPolicy</a>" : <i>[ <a href="ipsecpolicy.md">IpsecPolicy</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::VirtualNetworkGatewayConnection
Properties:
    <a href="#authorizationkey" title="AuthorizationKey">AuthorizationKey</a>: <i>String</i>
    <a href="#connectionprotocol" title="ConnectionProtocol">ConnectionProtocol</a>: <i>String</i>
    <a href="#enablebgp" title="EnableBgp">EnableBgp</a>: <i>Boolean</i>
    <a href="#expressroutecircuitid" title="ExpressRouteCircuitId">ExpressRouteCircuitId</a>: <i>String</i>
    <a href="#expressroutegatewaybypass" title="ExpressRouteGatewayBypass">ExpressRouteGatewayBypass</a>: <i>Boolean</i>
    <a href="#localnetworkgatewayid" title="LocalNetworkGatewayId">LocalNetworkGatewayId</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#peervirtualnetworkgatewayid" title="PeerVirtualNetworkGatewayId">PeerVirtualNetworkGatewayId</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#routingweight" title="RoutingWeight">RoutingWeight</a>: <i>Double</i>
    <a href="#sharedkey" title="SharedKey">SharedKey</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#usepolicybasedtrafficselectors" title="UsePolicyBasedTrafficSelectors">UsePolicyBasedTrafficSelectors</a>: <i>Boolean</i>
    <a href="#virtualnetworkgatewayid" title="VirtualNetworkGatewayId">VirtualNetworkGatewayId</a>: <i>String</i>
    <a href="#ipsecpolicy" title="IpsecPolicy">IpsecPolicy</a>: <i>
      - <a href="ipsecpolicy.md">IpsecPolicy</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AuthorizationKey

The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionProtocol

The IKE protocol version to use. Possible
values are `IKEv1` and `IKEv2`. Defaults to `IKEv2`.
Changing this value will force a resource to be created.
-> **Note**: Only valid for `IPSec` connections on virtual network gateways with SKU `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw1AZ`, `VpnGw2AZ` or `VpnGw3AZ`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBgp

If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpressRouteCircuitId

The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpressRouteGatewayBypass

If `true`, data packets will bypass ExpressRoute Gateway for data forwarding This is only valid for ExpressRoute connections.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalNetworkGatewayId

The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The location/region where the connection is
located. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the connection. Changing the name forces a
new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerVirtualNetworkGatewayId

The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingWeight

The routing weight. Defaults to `10`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedKey

The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of connection. Valid options are `IPsec`
(Site-to-Site), `ExpressRoute` (ExpressRoute), and `Vnet2Vnet` (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsePolicyBasedTrafficSelectors

If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkGatewayId

The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecPolicy

_Required_: No

_Type_: List of <a href="ipsecpolicy.md">IpsecPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

