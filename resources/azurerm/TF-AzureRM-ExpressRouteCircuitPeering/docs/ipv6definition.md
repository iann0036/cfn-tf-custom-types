# TF::AzureRM::ExpressRouteCircuitPeering Ipv6Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#primarypeeraddressprefix" title="PrimaryPeerAddressPrefix">PrimaryPeerAddressPrefix</a>" : <i>String</i>,
    "<a href="#routefilterid" title="RouteFilterId">RouteFilterId</a>" : <i>String</i>,
    "<a href="#secondarypeeraddressprefix" title="SecondaryPeerAddressPrefix">SecondaryPeerAddressPrefix</a>" : <i>String</i>,
    "<a href="#microsoftpeering" title="MicrosoftPeering">MicrosoftPeering</a>" : <i>[ <a href="microsoftpeeringdefinition.md">MicrosoftPeeringDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#primarypeeraddressprefix" title="PrimaryPeerAddressPrefix">PrimaryPeerAddressPrefix</a>: <i>String</i>
<a href="#routefilterid" title="RouteFilterId">RouteFilterId</a>: <i>String</i>
<a href="#secondarypeeraddressprefix" title="SecondaryPeerAddressPrefix">SecondaryPeerAddressPrefix</a>: <i>String</i>
<a href="#microsoftpeering" title="MicrosoftPeering">MicrosoftPeering</a>: <i>
      - <a href="microsoftpeeringdefinition.md">MicrosoftPeeringDefinition</a></i>
</pre>

## Properties

#### PrimaryPeerAddressPrefix

A subnet for the primary link.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteFilterId

The ID of the Route Filter. Only available when `peering_type` is set to `MicrosoftPeering`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryPeerAddressPrefix

A subnet for the secondary link.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MicrosoftPeering

_Required_: No

_Type_: List of <a href="microsoftpeeringdefinition.md">MicrosoftPeeringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

