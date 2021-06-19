# TF::Thunder::RouterBgpAddressFamilyIpv6NeighborIpv4Neighbor

`thunder_router_bgp_address_family_ipv6_neighbor_ipv4_neighbor` Provides details about thunder router bgp address family ipv6 neighbor ipv4 neighbor

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::RouterBgpAddressFamilyIpv6NeighborIpv4Neighbor",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#activate" title="Activate">Activate</a>" : <i>Double</i>,
        "<a href="#allowasin" title="AllowasIn">AllowasIn</a>" : <i>Double</i>,
        "<a href="#allowasincount" title="AllowasInCount">AllowasInCount</a>" : <i>Double</i>,
        "<a href="#asnumber" title="AsNumber">AsNumber</a>" : <i>Double</i>,
        "<a href="#defaultoriginate" title="DefaultOriginate">DefaultOriginate</a>" : <i>Double</i>,
        "<a href="#gracefulrestart" title="GracefulRestart">GracefulRestart</a>" : <i>Double</i>,
        "<a href="#inbound" title="Inbound">Inbound</a>" : <i>Double</i>,
        "<a href="#maximumprefix" title="MaximumPrefix">MaximumPrefix</a>" : <i>Double</i>,
        "<a href="#maximumprefixthres" title="MaximumPrefixThres">MaximumPrefixThres</a>" : <i>Double</i>,
        "<a href="#neighboripv4" title="NeighborIpv4">NeighborIpv4</a>" : <i>String</i>,
        "<a href="#nexthopself" title="NextHopSelf">NextHopSelf</a>" : <i>Double</i>,
        "<a href="#peergroupname" title="PeerGroupName">PeerGroupName</a>" : <i>String</i>,
        "<a href="#prefixlistdirection" title="PrefixListDirection">PrefixListDirection</a>" : <i>String</i>,
        "<a href="#processid" title="ProcessId">ProcessId</a>" : <i>String</i>,
        "<a href="#removeprivateas" title="RemovePrivateAs">RemovePrivateAs</a>" : <i>Double</i>,
        "<a href="#routemap" title="RouteMap">RouteMap</a>" : <i>String</i>,
        "<a href="#sendcommunityval" title="SendCommunityVal">SendCommunityVal</a>" : <i>String</i>,
        "<a href="#sequence" title="Sequence">Sequence</a>" : <i>String</i>,
        "<a href="#unsuppressmap" title="UnsuppressMap">UnsuppressMap</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
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
Type: TF::Thunder::RouterBgpAddressFamilyIpv6NeighborIpv4Neighbor
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#activate" title="Activate">Activate</a>: <i>Double</i>
    <a href="#allowasin" title="AllowasIn">AllowasIn</a>: <i>Double</i>
    <a href="#allowasincount" title="AllowasInCount">AllowasInCount</a>: <i>Double</i>
    <a href="#asnumber" title="AsNumber">AsNumber</a>: <i>Double</i>
    <a href="#defaultoriginate" title="DefaultOriginate">DefaultOriginate</a>: <i>Double</i>
    <a href="#gracefulrestart" title="GracefulRestart">GracefulRestart</a>: <i>Double</i>
    <a href="#inbound" title="Inbound">Inbound</a>: <i>Double</i>
    <a href="#maximumprefix" title="MaximumPrefix">MaximumPrefix</a>: <i>Double</i>
    <a href="#maximumprefixthres" title="MaximumPrefixThres">MaximumPrefixThres</a>: <i>Double</i>
    <a href="#neighboripv4" title="NeighborIpv4">NeighborIpv4</a>: <i>String</i>
    <a href="#nexthopself" title="NextHopSelf">NextHopSelf</a>: <i>Double</i>
    <a href="#peergroupname" title="PeerGroupName">PeerGroupName</a>: <i>String</i>
    <a href="#prefixlistdirection" title="PrefixListDirection">PrefixListDirection</a>: <i>String</i>
    <a href="#processid" title="ProcessId">ProcessId</a>: <i>String</i>
    <a href="#removeprivateas" title="RemovePrivateAs">RemovePrivateAs</a>: <i>Double</i>
    <a href="#routemap" title="RouteMap">RouteMap</a>: <i>String</i>
    <a href="#sendcommunityval" title="SendCommunityVal">SendCommunityVal</a>: <i>String</i>
    <a href="#sequence" title="Sequence">Sequence</a>: <i>String</i>
    <a href="#unsuppressmap" title="UnsuppressMap">UnsuppressMap</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
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

#### DefaultOriginate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulRestart

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inbound

Allow inbound soft reconfiguration for this neighbor.

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

#### NeighborIpv4

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHopSelf

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerGroupName

_Required_: No

_Type_: String

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

#### SendCommunityVal

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sequence

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnsuppressMap

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

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

