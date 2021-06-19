# TF::Thunder::RouterBgpAddressFamilyIpv6 Ipv6NeighborListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#activate" title="Activate">Activate</a>" : <i>Double</i>,
    "<a href="#allowasin" title="AllowasIn">AllowasIn</a>" : <i>Double</i>,
    "<a href="#allowasincount" title="AllowasInCount">AllowasInCount</a>" : <i>Double</i>,
    "<a href="#defaultoriginate" title="DefaultOriginate">DefaultOriginate</a>" : <i>Double</i>,
    "<a href="#gracefulrestart" title="GracefulRestart">GracefulRestart</a>" : <i>Double</i>,
    "<a href="#inbound" title="Inbound">Inbound</a>" : <i>Double</i>,
    "<a href="#maximumprefix" title="MaximumPrefix">MaximumPrefix</a>" : <i>Double</i>,
    "<a href="#maximumprefixthres" title="MaximumPrefixThres">MaximumPrefixThres</a>" : <i>Double</i>,
    "<a href="#neighboripv6" title="NeighborIpv6">NeighborIpv6</a>" : <i>String</i>,
    "<a href="#nexthopself" title="NextHopSelf">NextHopSelf</a>" : <i>Double</i>,
    "<a href="#peergroupname" title="PeerGroupName">PeerGroupName</a>" : <i>String</i>,
    "<a href="#prefixlistdirection" title="PrefixListDirection">PrefixListDirection</a>" : <i>String</i>,
    "<a href="#removeprivateas" title="RemovePrivateAs">RemovePrivateAs</a>" : <i>Double</i>,
    "<a href="#routemap" title="RouteMap">RouteMap</a>" : <i>String</i>,
    "<a href="#sendcommunityval" title="SendCommunityVal">SendCommunityVal</a>" : <i>String</i>,
    "<a href="#unsuppressmap" title="UnsuppressMap">UnsuppressMap</a>" : <i>String</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>,
    "<a href="#distributelists" title="DistributeLists">DistributeLists</a>" : <i>[ <a href="distributelistsdefinition.md">DistributeListsDefinition</a>, ... ]</i>,
    "<a href="#neighborfilterlists" title="NeighborFilterLists">NeighborFilterLists</a>" : <i>[ <a href="neighborfilterlistsdefinition.md">NeighborFilterListsDefinition</a>, ... ]</i>,
    "<a href="#neighborprefixlists" title="NeighborPrefixLists">NeighborPrefixLists</a>" : <i>[ <a href="neighborprefixlistsdefinition.md">NeighborPrefixListsDefinition</a>, ... ]</i>,
    "<a href="#neighborroutemaplists" title="NeighborRouteMapLists">NeighborRouteMapLists</a>" : <i>[ <a href="neighborroutemaplistsdefinition.md">NeighborRouteMapListsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#activate" title="Activate">Activate</a>: <i>Double</i>
<a href="#allowasin" title="AllowasIn">AllowasIn</a>: <i>Double</i>
<a href="#allowasincount" title="AllowasInCount">AllowasInCount</a>: <i>Double</i>
<a href="#defaultoriginate" title="DefaultOriginate">DefaultOriginate</a>: <i>Double</i>
<a href="#gracefulrestart" title="GracefulRestart">GracefulRestart</a>: <i>Double</i>
<a href="#inbound" title="Inbound">Inbound</a>: <i>Double</i>
<a href="#maximumprefix" title="MaximumPrefix">MaximumPrefix</a>: <i>Double</i>
<a href="#maximumprefixthres" title="MaximumPrefixThres">MaximumPrefixThres</a>: <i>Double</i>
<a href="#neighboripv6" title="NeighborIpv6">NeighborIpv6</a>: <i>String</i>
<a href="#nexthopself" title="NextHopSelf">NextHopSelf</a>: <i>Double</i>
<a href="#peergroupname" title="PeerGroupName">PeerGroupName</a>: <i>String</i>
<a href="#prefixlistdirection" title="PrefixListDirection">PrefixListDirection</a>: <i>String</i>
<a href="#removeprivateas" title="RemovePrivateAs">RemovePrivateAs</a>: <i>Double</i>
<a href="#routemap" title="RouteMap">RouteMap</a>: <i>String</i>
<a href="#sendcommunityval" title="SendCommunityVal">SendCommunityVal</a>: <i>String</i>
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

#### Activate

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

#### DefaultOriginate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulRestart

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inbound

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

#### NeighborIpv6

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

#### UnsuppressMap

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

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

