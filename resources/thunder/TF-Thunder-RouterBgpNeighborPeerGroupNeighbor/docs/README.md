# TF::Thunder::RouterBgpNeighborPeerGroupNeighbor

`thunder_router_bgp_neighbor_peer_group_neighbor` Provides details about thunder router bgp neighbor peer group neighbor

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::RouterBgpNeighborPeerGroupNeighbor",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#activate" title="Activate">Activate</a>" : <i>Double</i>,
        "<a href="#advertisementinterval" title="AdvertisementInterval">AdvertisementInterval</a>" : <i>Double</i>,
        "<a href="#allowasin" title="AllowasIn">AllowasIn</a>" : <i>Double</i>,
        "<a href="#allowasincount" title="AllowasInCount">AllowasInCount</a>" : <i>Double</i>,
        "<a href="#asnumber" title="AsNumber">AsNumber</a>" : <i>Double</i>,
        "<a href="#asoriginationinterval" title="AsOriginationInterval">AsOriginationInterval</a>" : <i>Double</i>,
        "<a href="#bfd" title="Bfd">Bfd</a>" : <i>Double</i>,
        "<a href="#collideestablished" title="CollideEstablished">CollideEstablished</a>" : <i>Double</i>,
        "<a href="#connect" title="Connect">Connect</a>" : <i>Double</i>,
        "<a href="#defaultoriginate" title="DefaultOriginate">DefaultOriginate</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disallowinfiniteholdtime" title="DisallowInfiniteHoldtime">DisallowInfiniteHoldtime</a>" : <i>Double</i>,
        "<a href="#dontcapabilitynegotiate" title="DontCapabilityNegotiate">DontCapabilityNegotiate</a>" : <i>Double</i>,
        "<a href="#dynamic" title="Dynamic">Dynamic</a>" : <i>Double</i>,
        "<a href="#ebgpmultihop" title="EbgpMultihop">EbgpMultihop</a>" : <i>Double</i>,
        "<a href="#ebgpmultihophopcount" title="EbgpMultihopHopCount">EbgpMultihopHopCount</a>" : <i>Double</i>,
        "<a href="#enforcemultihop" title="EnforceMultihop">EnforceMultihop</a>" : <i>Double</i>,
        "<a href="#ethernet" title="Ethernet">Ethernet</a>" : <i>Double</i>,
        "<a href="#extendednexthop" title="ExtendedNexthop">ExtendedNexthop</a>" : <i>Double</i>,
        "<a href="#inbound" title="Inbound">Inbound</a>" : <i>Double</i>,
        "<a href="#lif" title="Lif">Lif</a>" : <i>Double</i>,
        "<a href="#loopback" title="Loopback">Loopback</a>" : <i>Double</i>,
        "<a href="#maximumprefix" title="MaximumPrefix">MaximumPrefix</a>" : <i>Double</i>,
        "<a href="#maximumprefixthres" title="MaximumPrefixThres">MaximumPrefixThres</a>" : <i>Double</i>,
        "<a href="#multihop" title="Multihop">Multihop</a>" : <i>Double</i>,
        "<a href="#nexthopself" title="NextHopSelf">NextHopSelf</a>" : <i>Double</i>,
        "<a href="#overridecapability" title="OverrideCapability">OverrideCapability</a>" : <i>Double</i>,
        "<a href="#passvalue" title="PassValue">PassValue</a>" : <i>String</i>,
        "<a href="#passive" title="Passive">Passive</a>" : <i>Double</i>,
        "<a href="#peergroup" title="PeerGroup">PeerGroup</a>" : <i>String</i>,
        "<a href="#peergroupkey" title="PeerGroupKey">PeerGroupKey</a>" : <i>Double</i>,
        "<a href="#peergroupremoteas" title="PeerGroupRemoteAs">PeerGroupRemoteAs</a>" : <i>Double</i>,
        "<a href="#prefixlistdirection" title="PrefixListDirection">PrefixListDirection</a>" : <i>String</i>,
        "<a href="#processid" title="ProcessId">ProcessId</a>" : <i>String</i>,
        "<a href="#removeprivateas" title="RemovePrivateAs">RemovePrivateAs</a>" : <i>Double</i>,
        "<a href="#routemap" title="RouteMap">RouteMap</a>" : <i>String</i>,
        "<a href="#routerefresh" title="RouteRefresh">RouteRefresh</a>" : <i>Double</i>,
        "<a href="#sendcommunityval" title="SendCommunityVal">SendCommunityVal</a>" : <i>String</i>,
        "<a href="#sequence" title="Sequence">Sequence</a>" : <i>String</i>,
        "<a href="#shutdown" title="Shutdown">Shutdown</a>" : <i>Double</i>,
        "<a href="#strictcapabilitymatch" title="StrictCapabilityMatch">StrictCapabilityMatch</a>" : <i>Double</i>,
        "<a href="#timersholdtime" title="TimersHoldtime">TimersHoldtime</a>" : <i>Double</i>,
        "<a href="#timerskeepalive" title="TimersKeepalive">TimersKeepalive</a>" : <i>Double</i>,
        "<a href="#trunk" title="Trunk">Trunk</a>" : <i>Double</i>,
        "<a href="#tunnel" title="Tunnel">Tunnel</a>" : <i>Double</i>,
        "<a href="#unsuppressmap" title="UnsuppressMap">UnsuppressMap</a>" : <i>String</i>,
        "<a href="#updatesourceip" title="UpdateSourceIp">UpdateSourceIp</a>" : <i>String</i>,
        "<a href="#updatesourceipv6" title="UpdateSourceIpv6">UpdateSourceIpv6</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#ve" title="Ve">Ve</a>" : <i>Double</i>,
        "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>,
        "<a href="#distributelists" title="DistributeLists">DistributeLists</a>" : <i>[ <a href="distributelistsdefinition.md">DistributeListsDefinition</a>, ... ]</i>,
        "<a href="#neighborfilterlists" title="NeighborFilterLists">NeighborFilterLists</a>" : <i>[ <a href="neighborfilterlistsdefinition.md">NeighborFilterListsDefinition</a>, ... ]</i>,
        "<a href="#neighborprefixlists" title="NeighborPrefixLists">NeighborPrefixLists</a>" : <i>[ <a href="neighborprefixlistsdefinition.md">NeighborPrefixListsDefinition</a>, ... ]</i>,
        "<a href="#neighborroutemaplists" title="NeighborRouteMapLists">NeighborRouteMapLists</a>" : <i>[ <a href="neighborroutemaplistsdefinition.md">NeighborRouteMapListsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::RouterBgpNeighborPeerGroupNeighbor
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#activate" title="Activate">Activate</a>: <i>Double</i>
    <a href="#advertisementinterval" title="AdvertisementInterval">AdvertisementInterval</a>: <i>Double</i>
    <a href="#allowasin" title="AllowasIn">AllowasIn</a>: <i>Double</i>
    <a href="#allowasincount" title="AllowasInCount">AllowasInCount</a>: <i>Double</i>
    <a href="#asnumber" title="AsNumber">AsNumber</a>: <i>Double</i>
    <a href="#asoriginationinterval" title="AsOriginationInterval">AsOriginationInterval</a>: <i>Double</i>
    <a href="#bfd" title="Bfd">Bfd</a>: <i>Double</i>
    <a href="#collideestablished" title="CollideEstablished">CollideEstablished</a>: <i>Double</i>
    <a href="#connect" title="Connect">Connect</a>: <i>Double</i>
    <a href="#defaultoriginate" title="DefaultOriginate">DefaultOriginate</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disallowinfiniteholdtime" title="DisallowInfiniteHoldtime">DisallowInfiniteHoldtime</a>: <i>Double</i>
    <a href="#dontcapabilitynegotiate" title="DontCapabilityNegotiate">DontCapabilityNegotiate</a>: <i>Double</i>
    <a href="#dynamic" title="Dynamic">Dynamic</a>: <i>Double</i>
    <a href="#ebgpmultihop" title="EbgpMultihop">EbgpMultihop</a>: <i>Double</i>
    <a href="#ebgpmultihophopcount" title="EbgpMultihopHopCount">EbgpMultihopHopCount</a>: <i>Double</i>
    <a href="#enforcemultihop" title="EnforceMultihop">EnforceMultihop</a>: <i>Double</i>
    <a href="#ethernet" title="Ethernet">Ethernet</a>: <i>Double</i>
    <a href="#extendednexthop" title="ExtendedNexthop">ExtendedNexthop</a>: <i>Double</i>
    <a href="#inbound" title="Inbound">Inbound</a>: <i>Double</i>
    <a href="#lif" title="Lif">Lif</a>: <i>Double</i>
    <a href="#loopback" title="Loopback">Loopback</a>: <i>Double</i>
    <a href="#maximumprefix" title="MaximumPrefix">MaximumPrefix</a>: <i>Double</i>
    <a href="#maximumprefixthres" title="MaximumPrefixThres">MaximumPrefixThres</a>: <i>Double</i>
    <a href="#multihop" title="Multihop">Multihop</a>: <i>Double</i>
    <a href="#nexthopself" title="NextHopSelf">NextHopSelf</a>: <i>Double</i>
    <a href="#overridecapability" title="OverrideCapability">OverrideCapability</a>: <i>Double</i>
    <a href="#passvalue" title="PassValue">PassValue</a>: <i>String</i>
    <a href="#passive" title="Passive">Passive</a>: <i>Double</i>
    <a href="#peergroup" title="PeerGroup">PeerGroup</a>: <i>String</i>
    <a href="#peergroupkey" title="PeerGroupKey">PeerGroupKey</a>: <i>Double</i>
    <a href="#peergroupremoteas" title="PeerGroupRemoteAs">PeerGroupRemoteAs</a>: <i>Double</i>
    <a href="#prefixlistdirection" title="PrefixListDirection">PrefixListDirection</a>: <i>String</i>
    <a href="#processid" title="ProcessId">ProcessId</a>: <i>String</i>
    <a href="#removeprivateas" title="RemovePrivateAs">RemovePrivateAs</a>: <i>Double</i>
    <a href="#routemap" title="RouteMap">RouteMap</a>: <i>String</i>
    <a href="#routerefresh" title="RouteRefresh">RouteRefresh</a>: <i>Double</i>
    <a href="#sendcommunityval" title="SendCommunityVal">SendCommunityVal</a>: <i>String</i>
    <a href="#sequence" title="Sequence">Sequence</a>: <i>String</i>
    <a href="#shutdown" title="Shutdown">Shutdown</a>: <i>Double</i>
    <a href="#strictcapabilitymatch" title="StrictCapabilityMatch">StrictCapabilityMatch</a>: <i>Double</i>
    <a href="#timersholdtime" title="TimersHoldtime">TimersHoldtime</a>: <i>Double</i>
    <a href="#timerskeepalive" title="TimersKeepalive">TimersKeepalive</a>: <i>Double</i>
    <a href="#trunk" title="Trunk">Trunk</a>: <i>Double</i>
    <a href="#tunnel" title="Tunnel">Tunnel</a>: <i>Double</i>
    <a href="#unsuppressmap" title="UnsuppressMap">UnsuppressMap</a>: <i>String</i>
    <a href="#updatesourceip" title="UpdateSourceIp">UpdateSourceIp</a>: <i>String</i>
    <a href="#updatesourceipv6" title="UpdateSourceIpv6">UpdateSourceIpv6</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#ve" title="Ve">Ve</a>: <i>Double</i>
    <a href="#weight" title="Weight">Weight</a>: <i>Double</i>
    <a href="#distributelists" title="DistributeLists">DistributeLists</a>: <i>
      - <a href="distributelistsdefinition.md">DistributeListsDefinition</a></i>
    <a href="#neighborfilterlists" title="NeighborFilterLists">NeighborFilterLists</a>: <i>
      - <a href="neighborfilterlistsdefinition.md">NeighborFilterListsDefinition</a></i>
    <a href="#neighborprefixlists" title="NeighborPrefixLists">NeighborPrefixLists</a>: <i>
      - <a href="neighborprefixlistsdefinition.md">NeighborPrefixListsDefinition</a></i>
    <a href="#neighborroutemaplists" title="NeighborRouteMapLists">NeighborRouteMapLists</a>: <i>
      - <a href="neighborroutemaplistsdefinition.md">NeighborRouteMapListsDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Activate

Enable the Address Family for this Neighbor.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertisementInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowasIn

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowasInCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsOriginationInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bfd

Bidirectional Forwarding Detection (BFD).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CollideEstablished

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Connect

BGP connect timer.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultOriginate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Neighbor specific description (Up to 80 characters describing this neighbor).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisallowInfiniteHoldtime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DontCapabilityNegotiate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dynamic

Advertise dynamic capability to this neighbor.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbgpMultihop

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbgpMultihopHopCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforceMultihop

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ethernet

Ethernet interface (Port number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedNexthop

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inbound

Allow inbound soft reconfiguration for this neighbor.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lif

Logical interface (Lif interface number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Loopback

Loopback interface (Port number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumPrefix

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumPrefixThres

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Multihop

Enable multihop.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHopSelf

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideCapability

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PassValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Passive

Don't send open messages to this neighbor.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerGroupKey

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerGroupRemoteAs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixListDirection

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemovePrivateAs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteMap

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteRefresh

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendCommunityVal

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sequence

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shutdown

Administratively shut down this neighbor.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrictCapabilityMatch

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimersHoldtime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimersKeepalive

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trunk

Trunk interface (Trunk interface number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel

Tunnel interface (Tunnel interface number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnsuppressMap

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateSourceIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateSourceIpv6

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ve

Virtual ethernet interface (Virtual ethernet interface number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

Set default weight for routes from this neighbor.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributeLists

_Required_: No

_Type_: List of <a href="distributelistsdefinition.md">DistributeListsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeighborFilterLists

_Required_: No

_Type_: List of <a href="neighborfilterlistsdefinition.md">NeighborFilterListsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeighborPrefixLists

_Required_: No

_Type_: List of <a href="neighborprefixlistsdefinition.md">NeighborPrefixListsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeighborRouteMapLists

_Required_: No

_Type_: List of <a href="neighborroutemaplistsdefinition.md">NeighborRouteMapListsDefinition</a>

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

