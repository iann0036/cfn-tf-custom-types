# TF::AzureRM::ExpressRouteCircuitPeering

Manages an ExpressRoute Circuit Peering.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::ExpressRouteCircuitPeering",
    "Properties" : {
        "<a href="#expressroutecircuitname" title="ExpressRouteCircuitName">ExpressRouteCircuitName</a>" : <i>String</i>,
        "<a href="#peerasn" title="PeerAsn">PeerAsn</a>" : <i>Double</i>,
        "<a href="#peeringtype" title="PeeringType">PeeringType</a>" : <i>String</i>,
        "<a href="#primarypeeraddressprefix" title="PrimaryPeerAddressPrefix">PrimaryPeerAddressPrefix</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#routefilterid" title="RouteFilterId">RouteFilterId</a>" : <i>String</i>,
        "<a href="#secondarypeeraddressprefix" title="SecondaryPeerAddressPrefix">SecondaryPeerAddressPrefix</a>" : <i>String</i>,
        "<a href="#sharedkey" title="SharedKey">SharedKey</a>" : <i>String</i>,
        "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>Double</i>,
        "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>[ <a href="ipv6definition.md">Ipv6Definition</a>, ... ]</i>,
        "<a href="#microsoftpeeringconfig" title="MicrosoftPeeringConfig">MicrosoftPeeringConfig</a>" : <i>[ <a href="microsoftpeeringconfigdefinition.md">MicrosoftPeeringConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::ExpressRouteCircuitPeering
Properties:
    <a href="#expressroutecircuitname" title="ExpressRouteCircuitName">ExpressRouteCircuitName</a>: <i>String</i>
    <a href="#peerasn" title="PeerAsn">PeerAsn</a>: <i>Double</i>
    <a href="#peeringtype" title="PeeringType">PeeringType</a>: <i>String</i>
    <a href="#primarypeeraddressprefix" title="PrimaryPeerAddressPrefix">PrimaryPeerAddressPrefix</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#routefilterid" title="RouteFilterId">RouteFilterId</a>: <i>String</i>
    <a href="#secondarypeeraddressprefix" title="SecondaryPeerAddressPrefix">SecondaryPeerAddressPrefix</a>: <i>String</i>
    <a href="#sharedkey" title="SharedKey">SharedKey</a>: <i>String</i>
    <a href="#vlanid" title="VlanId">VlanId</a>: <i>Double</i>
    <a href="#ipv6" title="Ipv6">Ipv6</a>: <i>
      - <a href="ipv6definition.md">Ipv6Definition</a></i>
    <a href="#microsoftpeeringconfig" title="MicrosoftPeeringConfig">MicrosoftPeeringConfig</a>: <i>
      - <a href="microsoftpeeringconfigdefinition.md">MicrosoftPeeringConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ExpressRouteCircuitName

The name of the ExpressRoute Circuit in which to create the Peering.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAsn

The Either a 16-bit or a 32-bit ASN. Can either be public or private.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeeringType

The type of the ExpressRoute Circuit Peering. Acceptable values include `AzurePrivatePeering`, `AzurePublicPeering` and `MicrosoftPeering`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryPeerAddressPrefix

A `/30` subnet for the primary link.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the Express Route Circuit Peering. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteFilterId

The ID of the Route Filter. Only available when `peering_type` is set to `MicrosoftPeering`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryPeerAddressPrefix

A `/30` subnet for the secondary link.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedKey

The shared key. Can be a maximum of 25 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

A valid VLAN ID to establish this peering on.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

_Required_: No

_Type_: List of <a href="ipv6definition.md">Ipv6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MicrosoftPeeringConfig

_Required_: No

_Type_: List of <a href="microsoftpeeringconfigdefinition.md">MicrosoftPeeringConfigDefinition</a>

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

#### AzureAsn

Returns the <code>AzureAsn</code> value.

#### Id

Returns the <code>Id</code> value.

#### PrimaryAzurePort

Returns the <code>PrimaryAzurePort</code> value.

#### SecondaryAzurePort

Returns the <code>SecondaryAzurePort</code> value.

