# TF::FortiOS::RouterRoutemap RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#matchaspath" title="MatchAsPath">MatchAsPath</a>" : <i>String</i>,
    "<a href="#matchcommunity" title="MatchCommunity">MatchCommunity</a>" : <i>String</i>,
    "<a href="#matchcommunityexact" title="MatchCommunityExact">MatchCommunityExact</a>" : <i>String</i>,
    "<a href="#matchflags" title="MatchFlags">MatchFlags</a>" : <i>Double</i>,
    "<a href="#matchinterface" title="MatchInterface">MatchInterface</a>" : <i>String</i>,
    "<a href="#matchip6address" title="MatchIp6Address">MatchIp6Address</a>" : <i>String</i>,
    "<a href="#matchip6nexthop" title="MatchIp6Nexthop">MatchIp6Nexthop</a>" : <i>String</i>,
    "<a href="#matchipaddress" title="MatchIpAddress">MatchIpAddress</a>" : <i>String</i>,
    "<a href="#matchipnexthop" title="MatchIpNexthop">MatchIpNexthop</a>" : <i>String</i>,
    "<a href="#matchmetric" title="MatchMetric">MatchMetric</a>" : <i>Double</i>,
    "<a href="#matchorigin" title="MatchOrigin">MatchOrigin</a>" : <i>String</i>,
    "<a href="#matchroutetype" title="MatchRouteType">MatchRouteType</a>" : <i>String</i>,
    "<a href="#matchtag" title="MatchTag">MatchTag</a>" : <i>Double</i>,
    "<a href="#matchvrf" title="MatchVrf">MatchVrf</a>" : <i>Double</i>,
    "<a href="#setaggregatoras" title="SetAggregatorAs">SetAggregatorAs</a>" : <i>Double</i>,
    "<a href="#setaggregatorip" title="SetAggregatorIp">SetAggregatorIp</a>" : <i>String</i>,
    "<a href="#setaspathaction" title="SetAspathAction">SetAspathAction</a>" : <i>String</i>,
    "<a href="#setatomicaggregate" title="SetAtomicAggregate">SetAtomicAggregate</a>" : <i>String</i>,
    "<a href="#setcommunityadditive" title="SetCommunityAdditive">SetCommunityAdditive</a>" : <i>String</i>,
    "<a href="#setcommunitydelete" title="SetCommunityDelete">SetCommunityDelete</a>" : <i>String</i>,
    "<a href="#setdampeningmaxsuppress" title="SetDampeningMaxSuppress">SetDampeningMaxSuppress</a>" : <i>Double</i>,
    "<a href="#setdampeningreachabilityhalflife" title="SetDampeningReachabilityHalfLife">SetDampeningReachabilityHalfLife</a>" : <i>Double</i>,
    "<a href="#setdampeningreuse" title="SetDampeningReuse">SetDampeningReuse</a>" : <i>Double</i>,
    "<a href="#setdampeningsuppress" title="SetDampeningSuppress">SetDampeningSuppress</a>" : <i>Double</i>,
    "<a href="#setdampeningunreachabilityhalflife" title="SetDampeningUnreachabilityHalfLife">SetDampeningUnreachabilityHalfLife</a>" : <i>Double</i>,
    "<a href="#setflags" title="SetFlags">SetFlags</a>" : <i>Double</i>,
    "<a href="#setip6nexthop" title="SetIp6Nexthop">SetIp6Nexthop</a>" : <i>String</i>,
    "<a href="#setip6nexthoplocal" title="SetIp6NexthopLocal">SetIp6NexthopLocal</a>" : <i>String</i>,
    "<a href="#setipnexthop" title="SetIpNexthop">SetIpNexthop</a>" : <i>String</i>,
    "<a href="#setlocalpreference" title="SetLocalPreference">SetLocalPreference</a>" : <i>Double</i>,
    "<a href="#setmetric" title="SetMetric">SetMetric</a>" : <i>Double</i>,
    "<a href="#setmetrictype" title="SetMetricType">SetMetricType</a>" : <i>String</i>,
    "<a href="#setorigin" title="SetOrigin">SetOrigin</a>" : <i>String</i>,
    "<a href="#setoriginatorid" title="SetOriginatorId">SetOriginatorId</a>" : <i>String</i>,
    "<a href="#setroutetag" title="SetRouteTag">SetRouteTag</a>" : <i>Double</i>,
    "<a href="#settag" title="SetTag">SetTag</a>" : <i>Double</i>,
    "<a href="#setweight" title="SetWeight">SetWeight</a>" : <i>Double</i>,
    "<a href="#setaspath" title="SetAspath">SetAspath</a>" : <i>[ <a href="setaspathdefinition.md">SetAspathDefinition</a>, ... ]</i>,
    "<a href="#setcommunity" title="SetCommunity">SetCommunity</a>" : <i>[ <a href="setcommunitydefinition.md">SetCommunityDefinition</a>, ... ]</i>,
    "<a href="#setextcommunityrt" title="SetExtcommunityRt">SetExtcommunityRt</a>" : <i>[ <a href="setextcommunityrtdefinition.md">SetExtcommunityRtDefinition</a>, ... ]</i>,
    "<a href="#setextcommunitysoo" title="SetExtcommunitySoo">SetExtcommunitySoo</a>" : <i>[ <a href="setextcommunitysoodefinition.md">SetExtcommunitySooDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#matchaspath" title="MatchAsPath">MatchAsPath</a>: <i>String</i>
<a href="#matchcommunity" title="MatchCommunity">MatchCommunity</a>: <i>String</i>
<a href="#matchcommunityexact" title="MatchCommunityExact">MatchCommunityExact</a>: <i>String</i>
<a href="#matchflags" title="MatchFlags">MatchFlags</a>: <i>Double</i>
<a href="#matchinterface" title="MatchInterface">MatchInterface</a>: <i>String</i>
<a href="#matchip6address" title="MatchIp6Address">MatchIp6Address</a>: <i>String</i>
<a href="#matchip6nexthop" title="MatchIp6Nexthop">MatchIp6Nexthop</a>: <i>String</i>
<a href="#matchipaddress" title="MatchIpAddress">MatchIpAddress</a>: <i>String</i>
<a href="#matchipnexthop" title="MatchIpNexthop">MatchIpNexthop</a>: <i>String</i>
<a href="#matchmetric" title="MatchMetric">MatchMetric</a>: <i>Double</i>
<a href="#matchorigin" title="MatchOrigin">MatchOrigin</a>: <i>String</i>
<a href="#matchroutetype" title="MatchRouteType">MatchRouteType</a>: <i>String</i>
<a href="#matchtag" title="MatchTag">MatchTag</a>: <i>Double</i>
<a href="#matchvrf" title="MatchVrf">MatchVrf</a>: <i>Double</i>
<a href="#setaggregatoras" title="SetAggregatorAs">SetAggregatorAs</a>: <i>Double</i>
<a href="#setaggregatorip" title="SetAggregatorIp">SetAggregatorIp</a>: <i>String</i>
<a href="#setaspathaction" title="SetAspathAction">SetAspathAction</a>: <i>String</i>
<a href="#setatomicaggregate" title="SetAtomicAggregate">SetAtomicAggregate</a>: <i>String</i>
<a href="#setcommunityadditive" title="SetCommunityAdditive">SetCommunityAdditive</a>: <i>String</i>
<a href="#setcommunitydelete" title="SetCommunityDelete">SetCommunityDelete</a>: <i>String</i>
<a href="#setdampeningmaxsuppress" title="SetDampeningMaxSuppress">SetDampeningMaxSuppress</a>: <i>Double</i>
<a href="#setdampeningreachabilityhalflife" title="SetDampeningReachabilityHalfLife">SetDampeningReachabilityHalfLife</a>: <i>Double</i>
<a href="#setdampeningreuse" title="SetDampeningReuse">SetDampeningReuse</a>: <i>Double</i>
<a href="#setdampeningsuppress" title="SetDampeningSuppress">SetDampeningSuppress</a>: <i>Double</i>
<a href="#setdampeningunreachabilityhalflife" title="SetDampeningUnreachabilityHalfLife">SetDampeningUnreachabilityHalfLife</a>: <i>Double</i>
<a href="#setflags" title="SetFlags">SetFlags</a>: <i>Double</i>
<a href="#setip6nexthop" title="SetIp6Nexthop">SetIp6Nexthop</a>: <i>String</i>
<a href="#setip6nexthoplocal" title="SetIp6NexthopLocal">SetIp6NexthopLocal</a>: <i>String</i>
<a href="#setipnexthop" title="SetIpNexthop">SetIpNexthop</a>: <i>String</i>
<a href="#setlocalpreference" title="SetLocalPreference">SetLocalPreference</a>: <i>Double</i>
<a href="#setmetric" title="SetMetric">SetMetric</a>: <i>Double</i>
<a href="#setmetrictype" title="SetMetricType">SetMetricType</a>: <i>String</i>
<a href="#setorigin" title="SetOrigin">SetOrigin</a>: <i>String</i>
<a href="#setoriginatorid" title="SetOriginatorId">SetOriginatorId</a>: <i>String</i>
<a href="#setroutetag" title="SetRouteTag">SetRouteTag</a>: <i>Double</i>
<a href="#settag" title="SetTag">SetTag</a>: <i>Double</i>
<a href="#setweight" title="SetWeight">SetWeight</a>: <i>Double</i>
<a href="#setaspath" title="SetAspath">SetAspath</a>: <i>
      - <a href="setaspathdefinition.md">SetAspathDefinition</a></i>
<a href="#setcommunity" title="SetCommunity">SetCommunity</a>: <i>
      - <a href="setcommunitydefinition.md">SetCommunityDefinition</a></i>
<a href="#setextcommunityrt" title="SetExtcommunityRt">SetExtcommunityRt</a>: <i>
      - <a href="setextcommunityrtdefinition.md">SetExtcommunityRtDefinition</a></i>
<a href="#setextcommunitysoo" title="SetExtcommunitySoo">SetExtcommunitySoo</a>: <i>
      - <a href="setextcommunitysoodefinition.md">SetExtcommunitySooDefinition</a></i>
</pre>

## Properties

#### Action

Action. Valid values: `permit`, `deny`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Rule ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchAsPath

Match BGP AS path list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchCommunity

Match BGP community list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchCommunityExact

Enable/disable exact matching of communities. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchFlags

BGP flag value to match (0 - 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchInterface

Match interface configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchIp6Address

Match IPv6 address permitted by access-list6 or prefix-list6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchIp6Nexthop

Match next hop IPv6 address passed by access-list6 or prefix-list6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchIpAddress

Match IP address permitted by access-list or prefix-list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchIpNexthop

Match next hop IP address passed by access-list or prefix-list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchMetric

Match metric for redistribute routes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchOrigin

Match BGP origin code. Valid values: `none`, `egp`, `igp`, `incomplete`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchRouteType

Match route type. Valid values: `1`, `2`, `none`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchTag

Match tag.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchVrf

Match VRF ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetAggregatorAs

BGP aggregator AS.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetAggregatorIp

BGP aggregator IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetAspathAction

Specify preferred action of set-aspath. Valid values: `prepend`, `replace`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetAtomicAggregate

Enable/disable BGP atomic aggregate attribute. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetCommunityAdditive

Enable/disable adding set-community to existing community. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetCommunityDelete

Delete communities matching community list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetDampeningMaxSuppress

Maximum duration to suppress a route (1 - 255 min, 0 = unset).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetDampeningReachabilityHalfLife

Reachability half-life time for the penalty (1 - 45 min, 0 = unset).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetDampeningReuse

Value to start reusing a route (1 - 20000, 0 = unset).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetDampeningSuppress

Value to start suppressing a route (1 - 20000, 0 = unset).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetDampeningUnreachabilityHalfLife

Unreachability Half-life time for the penalty (1 - 45 min, 0 = unset).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetFlags

BGP flags value (0 - 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetIp6Nexthop

IPv6 global address of next hop.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetIp6NexthopLocal

IPv6 local address of next hop.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetIpNexthop

IP address of next hop.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetLocalPreference

BGP local preference path attribute.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetMetric

Metric value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetMetricType

Metric type. Valid values: `1`, `2`, `none`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetOrigin

BGP origin code. Valid values: `none`, `egp`, `igp`, `incomplete`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetOriginatorId

BGP originator ID attribute.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetRouteTag

Route tag for routing table.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetTag

Tag value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetWeight

BGP weight for routing table.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetAspath

_Required_: No

_Type_: List of <a href="setaspathdefinition.md">SetAspathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetCommunity

_Required_: No

_Type_: List of <a href="setcommunitydefinition.md">SetCommunityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetExtcommunityRt

_Required_: No

_Type_: List of <a href="setextcommunityrtdefinition.md">SetExtcommunityRtDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetExtcommunitySoo

_Required_: No

_Type_: List of <a href="setextcommunitysoodefinition.md">SetExtcommunitySooDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

