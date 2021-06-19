# TF::AzureRM::ExpressRouteCircuitPeering MicrosoftPeeringDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#advertisedpublicprefixes" title="AdvertisedPublicPrefixes">AdvertisedPublicPrefixes</a>" : <i>[ String, ... ]</i>,
    "<a href="#customerasn" title="CustomerAsn">CustomerAsn</a>" : <i>Double</i>,
    "<a href="#routingregistryname" title="RoutingRegistryName">RoutingRegistryName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#advertisedpublicprefixes" title="AdvertisedPublicPrefixes">AdvertisedPublicPrefixes</a>: <i>
      - String</i>
<a href="#customerasn" title="CustomerAsn">CustomerAsn</a>: <i>Double</i>
<a href="#routingregistryname" title="RoutingRegistryName">RoutingRegistryName</a>: <i>String</i>
</pre>

## Properties

#### AdvertisedPublicPrefixes

A list of Advertised Public Prefixes.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerAsn

The CustomerASN of the peering.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingRegistryName

The Routing Registry against which the AS number and prefixes are registered. For example:  `ARIN`, `RIPE`, `AFRINIC` etc.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

