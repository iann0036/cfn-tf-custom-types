# TF::FortiOS::RouterBgp

Configure BGP.

~> The provider supports the definition of Neighbor in Router Bgp `fortios_router_bgp`, and also allows the definition of separate Neighbor resources `fortios_routerbgp_neighbor`, but do not use a `fortios_router_bgp` with in-line Neighbor in conjunction with any `fortios_routerbgp_neighbor` resources, otherwise conflicts and overwrite will occur.

~> The provider supports the definition of Network in Router Bgp `fortios_router_bgp`, and also allows the definition of separate Network resources `fortios_routerbgp_network`, but do not use a `fortios_router_bgp` with in-line Network in conjunction with any `fortios_routerbgp_network` resources, otherwise conflicts and overwrite will occur.

~> The provider supports the definition of Network6 in Router Bgp `fortios_router_bgp`, and also allows the definition of separate Network6 resources `fortios_routerbgp_network6`, but do not use a `fortios_router_bgp` with in-line Network6 in conjunction with any `fortios_routerbgp_network6` resources, oth...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::RouterBgp",
    "Properties" : {
        "<a href="#additionalpath" title="AdditionalPath">AdditionalPath</a>" : <i>String</i>,
        "<a href="#additionalpath6" title="AdditionalPath6">AdditionalPath6</a>" : <i>String</i>,
        "<a href="#additionalpathselect" title="AdditionalPathSelect">AdditionalPathSelect</a>" : <i>Double</i>,
        "<a href="#additionalpathselect6" title="AdditionalPathSelect6">AdditionalPathSelect6</a>" : <i>Double</i>,
        "<a href="#alwayscomparemed" title="AlwaysCompareMed">AlwaysCompareMed</a>" : <i>String</i>,
        "<a href="#as" title="As">As</a>" : <i>Double</i>,
        "<a href="#bestpathaspathignore" title="BestpathAsPathIgnore">BestpathAsPathIgnore</a>" : <i>String</i>,
        "<a href="#bestpathcmpconfedaspath" title="BestpathCmpConfedAspath">BestpathCmpConfedAspath</a>" : <i>String</i>,
        "<a href="#bestpathcmprouterid" title="BestpathCmpRouterid">BestpathCmpRouterid</a>" : <i>String</i>,
        "<a href="#bestpathmedconfed" title="BestpathMedConfed">BestpathMedConfed</a>" : <i>String</i>,
        "<a href="#bestpathmedmissingasworst" title="BestpathMedMissingAsWorst">BestpathMedMissingAsWorst</a>" : <i>String</i>,
        "<a href="#clienttoclientreflection" title="ClientToClientReflection">ClientToClientReflection</a>" : <i>String</i>,
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#confederationidentifier" title="ConfederationIdentifier">ConfederationIdentifier</a>" : <i>Double</i>,
        "<a href="#dampening" title="Dampening">Dampening</a>" : <i>String</i>,
        "<a href="#dampeningmaxsuppresstime" title="DampeningMaxSuppressTime">DampeningMaxSuppressTime</a>" : <i>Double</i>,
        "<a href="#dampeningreachabilityhalflife" title="DampeningReachabilityHalfLife">DampeningReachabilityHalfLife</a>" : <i>Double</i>,
        "<a href="#dampeningreuse" title="DampeningReuse">DampeningReuse</a>" : <i>Double</i>,
        "<a href="#dampeningroutemap" title="DampeningRouteMap">DampeningRouteMap</a>" : <i>String</i>,
        "<a href="#dampeningsuppress" title="DampeningSuppress">DampeningSuppress</a>" : <i>Double</i>,
        "<a href="#dampeningunreachabilityhalflife" title="DampeningUnreachabilityHalfLife">DampeningUnreachabilityHalfLife</a>" : <i>Double</i>,
        "<a href="#defaultlocalpreference" title="DefaultLocalPreference">DefaultLocalPreference</a>" : <i>Double</i>,
        "<a href="#deterministicmed" title="DeterministicMed">DeterministicMed</a>" : <i>String</i>,
        "<a href="#distanceexternal" title="DistanceExternal">DistanceExternal</a>" : <i>Double</i>,
        "<a href="#distanceinternal" title="DistanceInternal">DistanceInternal</a>" : <i>Double</i>,
        "<a href="#distancelocal" title="DistanceLocal">DistanceLocal</a>" : <i>Double</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#ebgpmultipath" title="EbgpMultipath">EbgpMultipath</a>" : <i>String</i>,
        "<a href="#enforcefirstas" title="EnforceFirstAs">EnforceFirstAs</a>" : <i>String</i>,
        "<a href="#fastexternalfailover" title="FastExternalFailover">FastExternalFailover</a>" : <i>String</i>,
        "<a href="#gracefulendontimer" title="GracefulEndOnTimer">GracefulEndOnTimer</a>" : <i>String</i>,
        "<a href="#gracefulrestart" title="GracefulRestart">GracefulRestart</a>" : <i>String</i>,
        "<a href="#gracefulrestarttime" title="GracefulRestartTime">GracefulRestartTime</a>" : <i>Double</i>,
        "<a href="#gracefulstalepathtime" title="GracefulStalepathTime">GracefulStalepathTime</a>" : <i>Double</i>,
        "<a href="#gracefulupdatedelay" title="GracefulUpdateDelay">GracefulUpdateDelay</a>" : <i>Double</i>,
        "<a href="#holdtimetimer" title="HoldtimeTimer">HoldtimeTimer</a>" : <i>Double</i>,
        "<a href="#ibgpmultipath" title="IbgpMultipath">IbgpMultipath</a>" : <i>String</i>,
        "<a href="#ignoreoptionalcapability" title="IgnoreOptionalCapability">IgnoreOptionalCapability</a>" : <i>String</i>,
        "<a href="#keepalivetimer" title="KeepaliveTimer">KeepaliveTimer</a>" : <i>Double</i>,
        "<a href="#logneighbourchanges" title="LogNeighbourChanges">LogNeighbourChanges</a>" : <i>String</i>,
        "<a href="#multipathrecursivedistance" title="MultipathRecursiveDistance">MultipathRecursiveDistance</a>" : <i>String</i>,
        "<a href="#networkimportcheck" title="NetworkImportCheck">NetworkImportCheck</a>" : <i>String</i>,
        "<a href="#recursivenexthop" title="RecursiveNextHop">RecursiveNextHop</a>" : <i>String</i>,
        "<a href="#routerid" title="RouterId">RouterId</a>" : <i>String</i>,
        "<a href="#scantime" title="ScanTime">ScanTime</a>" : <i>Double</i>,
        "<a href="#synchronization" title="Synchronization">Synchronization</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#admindistance" title="AdminDistance">AdminDistance</a>" : <i>[ <a href="admindistancedefinition.md">AdminDistanceDefinition</a>, ... ]</i>,
        "<a href="#aggregateaddress" title="AggregateAddress">AggregateAddress</a>" : <i>[ <a href="aggregateaddressdefinition.md">AggregateAddressDefinition</a>, ... ]</i>,
        "<a href="#aggregateaddress6" title="AggregateAddress6">AggregateAddress6</a>" : <i>[ <a href="aggregateaddress6definition.md">AggregateAddress6Definition</a>, ... ]</i>,
        "<a href="#confederationpeers" title="ConfederationPeers">ConfederationPeers</a>" : <i>[ <a href="confederationpeersdefinition.md">ConfederationPeersDefinition</a>, ... ]</i>,
        "<a href="#neighbor" title="Neighbor">Neighbor</a>" : <i>[ <a href="neighbordefinition.md">NeighborDefinition</a>, ... ]</i>,
        "<a href="#neighborgroup" title="NeighborGroup">NeighborGroup</a>" : <i>[ <a href="neighborgroupdefinition.md">NeighborGroupDefinition</a>, ... ]</i>,
        "<a href="#neighborrange" title="NeighborRange">NeighborRange</a>" : <i>[ <a href="neighborrangedefinition.md">NeighborRangeDefinition</a>, ... ]</i>,
        "<a href="#neighborrange6" title="NeighborRange6">NeighborRange6</a>" : <i>[ <a href="neighborrange6definition.md">NeighborRange6Definition</a>, ... ]</i>,
        "<a href="#network" title="Network">Network</a>" : <i>[ <a href="networkdefinition.md">NetworkDefinition</a>, ... ]</i>,
        "<a href="#network6" title="Network6">Network6</a>" : <i>[ <a href="network6definition.md">Network6Definition</a>, ... ]</i>,
        "<a href="#redistribute" title="Redistribute">Redistribute</a>" : <i>[ <a href="redistributedefinition.md">RedistributeDefinition</a>, ... ]</i>,
        "<a href="#redistribute6" title="Redistribute6">Redistribute6</a>" : <i>[ <a href="redistribute6definition.md">Redistribute6Definition</a>, ... ]</i>,
        "<a href="#vrfleak" title="VrfLeak">VrfLeak</a>" : <i>[ <a href="vrfleakdefinition.md">VrfLeakDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::RouterBgp
Properties:
    <a href="#additionalpath" title="AdditionalPath">AdditionalPath</a>: <i>String</i>
    <a href="#additionalpath6" title="AdditionalPath6">AdditionalPath6</a>: <i>String</i>
    <a href="#additionalpathselect" title="AdditionalPathSelect">AdditionalPathSelect</a>: <i>Double</i>
    <a href="#additionalpathselect6" title="AdditionalPathSelect6">AdditionalPathSelect6</a>: <i>Double</i>
    <a href="#alwayscomparemed" title="AlwaysCompareMed">AlwaysCompareMed</a>: <i>String</i>
    <a href="#as" title="As">As</a>: <i>Double</i>
    <a href="#bestpathaspathignore" title="BestpathAsPathIgnore">BestpathAsPathIgnore</a>: <i>String</i>
    <a href="#bestpathcmpconfedaspath" title="BestpathCmpConfedAspath">BestpathCmpConfedAspath</a>: <i>String</i>
    <a href="#bestpathcmprouterid" title="BestpathCmpRouterid">BestpathCmpRouterid</a>: <i>String</i>
    <a href="#bestpathmedconfed" title="BestpathMedConfed">BestpathMedConfed</a>: <i>String</i>
    <a href="#bestpathmedmissingasworst" title="BestpathMedMissingAsWorst">BestpathMedMissingAsWorst</a>: <i>String</i>
    <a href="#clienttoclientreflection" title="ClientToClientReflection">ClientToClientReflection</a>: <i>String</i>
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#confederationidentifier" title="ConfederationIdentifier">ConfederationIdentifier</a>: <i>Double</i>
    <a href="#dampening" title="Dampening">Dampening</a>: <i>String</i>
    <a href="#dampeningmaxsuppresstime" title="DampeningMaxSuppressTime">DampeningMaxSuppressTime</a>: <i>Double</i>
    <a href="#dampeningreachabilityhalflife" title="DampeningReachabilityHalfLife">DampeningReachabilityHalfLife</a>: <i>Double</i>
    <a href="#dampeningreuse" title="DampeningReuse">DampeningReuse</a>: <i>Double</i>
    <a href="#dampeningroutemap" title="DampeningRouteMap">DampeningRouteMap</a>: <i>String</i>
    <a href="#dampeningsuppress" title="DampeningSuppress">DampeningSuppress</a>: <i>Double</i>
    <a href="#dampeningunreachabilityhalflife" title="DampeningUnreachabilityHalfLife">DampeningUnreachabilityHalfLife</a>: <i>Double</i>
    <a href="#defaultlocalpreference" title="DefaultLocalPreference">DefaultLocalPreference</a>: <i>Double</i>
    <a href="#deterministicmed" title="DeterministicMed">DeterministicMed</a>: <i>String</i>
    <a href="#distanceexternal" title="DistanceExternal">DistanceExternal</a>: <i>Double</i>
    <a href="#distanceinternal" title="DistanceInternal">DistanceInternal</a>: <i>Double</i>
    <a href="#distancelocal" title="DistanceLocal">DistanceLocal</a>: <i>Double</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#ebgpmultipath" title="EbgpMultipath">EbgpMultipath</a>: <i>String</i>
    <a href="#enforcefirstas" title="EnforceFirstAs">EnforceFirstAs</a>: <i>String</i>
    <a href="#fastexternalfailover" title="FastExternalFailover">FastExternalFailover</a>: <i>String</i>
    <a href="#gracefulendontimer" title="GracefulEndOnTimer">GracefulEndOnTimer</a>: <i>String</i>
    <a href="#gracefulrestart" title="GracefulRestart">GracefulRestart</a>: <i>String</i>
    <a href="#gracefulrestarttime" title="GracefulRestartTime">GracefulRestartTime</a>: <i>Double</i>
    <a href="#gracefulstalepathtime" title="GracefulStalepathTime">GracefulStalepathTime</a>: <i>Double</i>
    <a href="#gracefulupdatedelay" title="GracefulUpdateDelay">GracefulUpdateDelay</a>: <i>Double</i>
    <a href="#holdtimetimer" title="HoldtimeTimer">HoldtimeTimer</a>: <i>Double</i>
    <a href="#ibgpmultipath" title="IbgpMultipath">IbgpMultipath</a>: <i>String</i>
    <a href="#ignoreoptionalcapability" title="IgnoreOptionalCapability">IgnoreOptionalCapability</a>: <i>String</i>
    <a href="#keepalivetimer" title="KeepaliveTimer">KeepaliveTimer</a>: <i>Double</i>
    <a href="#logneighbourchanges" title="LogNeighbourChanges">LogNeighbourChanges</a>: <i>String</i>
    <a href="#multipathrecursivedistance" title="MultipathRecursiveDistance">MultipathRecursiveDistance</a>: <i>String</i>
    <a href="#networkimportcheck" title="NetworkImportCheck">NetworkImportCheck</a>: <i>String</i>
    <a href="#recursivenexthop" title="RecursiveNextHop">RecursiveNextHop</a>: <i>String</i>
    <a href="#routerid" title="RouterId">RouterId</a>: <i>String</i>
    <a href="#scantime" title="ScanTime">ScanTime</a>: <i>Double</i>
    <a href="#synchronization" title="Synchronization">Synchronization</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#admindistance" title="AdminDistance">AdminDistance</a>: <i>
      - <a href="admindistancedefinition.md">AdminDistanceDefinition</a></i>
    <a href="#aggregateaddress" title="AggregateAddress">AggregateAddress</a>: <i>
      - <a href="aggregateaddressdefinition.md">AggregateAddressDefinition</a></i>
    <a href="#aggregateaddress6" title="AggregateAddress6">AggregateAddress6</a>: <i>
      - <a href="aggregateaddress6definition.md">AggregateAddress6Definition</a></i>
    <a href="#confederationpeers" title="ConfederationPeers">ConfederationPeers</a>: <i>
      - <a href="confederationpeersdefinition.md">ConfederationPeersDefinition</a></i>
    <a href="#neighbor" title="Neighbor">Neighbor</a>: <i>
      - <a href="neighbordefinition.md">NeighborDefinition</a></i>
    <a href="#neighborgroup" title="NeighborGroup">NeighborGroup</a>: <i>
      - <a href="neighborgroupdefinition.md">NeighborGroupDefinition</a></i>
    <a href="#neighborrange" title="NeighborRange">NeighborRange</a>: <i>
      - <a href="neighborrangedefinition.md">NeighborRangeDefinition</a></i>
    <a href="#neighborrange6" title="NeighborRange6">NeighborRange6</a>: <i>
      - <a href="neighborrange6definition.md">NeighborRange6Definition</a></i>
    <a href="#network" title="Network">Network</a>: <i>
      - <a href="networkdefinition.md">NetworkDefinition</a></i>
    <a href="#network6" title="Network6">Network6</a>: <i>
      - <a href="network6definition.md">Network6Definition</a></i>
    <a href="#redistribute" title="Redistribute">Redistribute</a>: <i>
      - <a href="redistributedefinition.md">RedistributeDefinition</a></i>
    <a href="#redistribute6" title="Redistribute6">Redistribute6</a>: <i>
      - <a href="redistribute6definition.md">Redistribute6Definition</a></i>
    <a href="#vrfleak" title="VrfLeak">VrfLeak</a>: <i>
      - <a href="vrfleakdefinition.md">VrfLeakDefinition</a></i>
</pre>

## Properties

#### AdditionalPath

Enable/disable selection of BGP IPv4 additional paths. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalPath6

Enable/disable selection of BGP IPv6 additional paths. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalPathSelect

Number of additional paths to be selected for each IPv4 NLRI.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalPathSelect6

Number of additional paths to be selected for each IPv6 NLRI.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlwaysCompareMed

Enable/disable always compare MED. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### As

Router AS number, valid from 1 to 4294967295, 0 to disable BGP.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BestpathAsPathIgnore

Enable/disable ignore AS path. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BestpathCmpConfedAspath

Enable/disable compare federation AS path length. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BestpathCmpRouterid

Enable/disable compare router ID for identical EBGP paths. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BestpathMedConfed

Enable/disable compare MED among confederation paths. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BestpathMedMissingAsWorst

Enable/disable treat missing MED as least preferred. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientToClientReflection

Enable/disable client-to-client route reflection. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterId

Route reflector cluster ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfederationIdentifier

Confederation identifier.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dampening

Enable/disable route-flap dampening. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DampeningMaxSuppressTime

Maximum minutes a route can be suppressed.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DampeningReachabilityHalfLife

Reachability half-life time for penalty (min).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DampeningReuse

Threshold to reuse routes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DampeningRouteMap

Criteria for dampening.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DampeningSuppress

Threshold to suppress routes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DampeningUnreachabilityHalfLife

Unreachability half-life time for penalty (min).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultLocalPreference

Default local preference.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeterministicMed

Enable/disable enforce deterministic comparison of MED. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistanceExternal

Distance for routes external to the AS.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistanceInternal

Distance for routes internal to the AS.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistanceLocal

Distance for routes local to the AS.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbgpMultipath

Enable/disable EBGP multi-path. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforceFirstAs

Enable/disable enforce first AS for EBGP routes. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FastExternalFailover

Enable/disable reset peer BGP session if link goes down. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulEndOnTimer

Enable/disable to exit graceful restart on timer only. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulRestart

Enable/disable BGP graceful restart capabilities. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulRestartTime

Time needed for neighbors to restart (sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulStalepathTime

Time to hold stale paths of restarting neighbor (sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulUpdateDelay

Route advertisement/selection delay after restart (sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HoldtimeTimer

Number of seconds to mark peer as dead.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IbgpMultipath

Enable/disable IBGP multi-path. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreOptionalCapability

Don't send unknown optional capability notification message Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepaliveTimer

Frequency to send keep alive requests.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogNeighbourChanges

Enable logging of BGP neighbour's changes Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultipathRecursiveDistance

Enable/disable use of recursive distance to select multipath. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkImportCheck

Enable/disable ensure BGP network route exists in IGP. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecursiveNextHop

Enable/disable recursive resolution of next-hop using BGP route. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouterId

Router ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanTime

Background scanner interval (sec), 0 to disable it.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Synchronization

Enable/disable only advertise routes from iBGP if routes present in an IGP. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminDistance

_Required_: No

_Type_: List of <a href="admindistancedefinition.md">AdminDistanceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AggregateAddress

_Required_: No

_Type_: List of <a href="aggregateaddressdefinition.md">AggregateAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AggregateAddress6

_Required_: No

_Type_: List of <a href="aggregateaddress6definition.md">AggregateAddress6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfederationPeers

_Required_: No

_Type_: List of <a href="confederationpeersdefinition.md">ConfederationPeersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Neighbor

_Required_: No

_Type_: List of <a href="neighbordefinition.md">NeighborDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeighborGroup

_Required_: No

_Type_: List of <a href="neighborgroupdefinition.md">NeighborGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeighborRange

_Required_: No

_Type_: List of <a href="neighborrangedefinition.md">NeighborRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeighborRange6

_Required_: No

_Type_: List of <a href="neighborrange6definition.md">NeighborRange6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="networkdefinition.md">NetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network6

_Required_: No

_Type_: List of <a href="network6definition.md">Network6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redistribute

_Required_: No

_Type_: List of <a href="redistributedefinition.md">RedistributeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redistribute6

_Required_: No

_Type_: List of <a href="redistribute6definition.md">Redistribute6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrfLeak

_Required_: No

_Type_: List of <a href="vrfleakdefinition.md">VrfLeakDefinition</a>

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

