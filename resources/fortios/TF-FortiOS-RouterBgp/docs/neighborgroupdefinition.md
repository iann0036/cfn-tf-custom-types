# TF::FortiOS::RouterBgp NeighborGroupDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#activate" title="Activate">Activate</a>" : <i>String</i>,
    "<a href="#activate6" title="Activate6">Activate6</a>" : <i>String</i>,
    "<a href="#additionalpath" title="AdditionalPath">AdditionalPath</a>" : <i>String</i>,
    "<a href="#additionalpath6" title="AdditionalPath6">AdditionalPath6</a>" : <i>String</i>,
    "<a href="#advadditionalpath" title="AdvAdditionalPath">AdvAdditionalPath</a>" : <i>Double</i>,
    "<a href="#advadditionalpath6" title="AdvAdditionalPath6">AdvAdditionalPath6</a>" : <i>Double</i>,
    "<a href="#advertisementinterval" title="AdvertisementInterval">AdvertisementInterval</a>" : <i>Double</i>,
    "<a href="#allowasin" title="AllowasIn">AllowasIn</a>" : <i>Double</i>,
    "<a href="#allowasin6" title="AllowasIn6">AllowasIn6</a>" : <i>Double</i>,
    "<a href="#allowasinenable" title="AllowasInEnable">AllowasInEnable</a>" : <i>String</i>,
    "<a href="#allowasinenable6" title="AllowasInEnable6">AllowasInEnable6</a>" : <i>String</i>,
    "<a href="#asoverride" title="AsOverride">AsOverride</a>" : <i>String</i>,
    "<a href="#asoverride6" title="AsOverride6">AsOverride6</a>" : <i>String</i>,
    "<a href="#attributeunchanged" title="AttributeUnchanged">AttributeUnchanged</a>" : <i>String</i>,
    "<a href="#attributeunchanged6" title="AttributeUnchanged6">AttributeUnchanged6</a>" : <i>String</i>,
    "<a href="#bfd" title="Bfd">Bfd</a>" : <i>String</i>,
    "<a href="#capabilitydefaultoriginate" title="CapabilityDefaultOriginate">CapabilityDefaultOriginate</a>" : <i>String</i>,
    "<a href="#capabilitydefaultoriginate6" title="CapabilityDefaultOriginate6">CapabilityDefaultOriginate6</a>" : <i>String</i>,
    "<a href="#capabilitydynamic" title="CapabilityDynamic">CapabilityDynamic</a>" : <i>String</i>,
    "<a href="#capabilitygracefulrestart" title="CapabilityGracefulRestart">CapabilityGracefulRestart</a>" : <i>String</i>,
    "<a href="#capabilitygracefulrestart6" title="CapabilityGracefulRestart6">CapabilityGracefulRestart6</a>" : <i>String</i>,
    "<a href="#capabilityorf" title="CapabilityOrf">CapabilityOrf</a>" : <i>String</i>,
    "<a href="#capabilityorf6" title="CapabilityOrf6">CapabilityOrf6</a>" : <i>String</i>,
    "<a href="#capabilityrouterefresh" title="CapabilityRouteRefresh">CapabilityRouteRefresh</a>" : <i>String</i>,
    "<a href="#connecttimer" title="ConnectTimer">ConnectTimer</a>" : <i>Double</i>,
    "<a href="#defaultoriginateroutemap" title="DefaultOriginateRoutemap">DefaultOriginateRoutemap</a>" : <i>String</i>,
    "<a href="#defaultoriginateroutemap6" title="DefaultOriginateRoutemap6">DefaultOriginateRoutemap6</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#distributelistin" title="DistributeListIn">DistributeListIn</a>" : <i>String</i>,
    "<a href="#distributelistin6" title="DistributeListIn6">DistributeListIn6</a>" : <i>String</i>,
    "<a href="#distributelistout" title="DistributeListOut">DistributeListOut</a>" : <i>String</i>,
    "<a href="#distributelistout6" title="DistributeListOut6">DistributeListOut6</a>" : <i>String</i>,
    "<a href="#dontcapabilitynegotiate" title="DontCapabilityNegotiate">DontCapabilityNegotiate</a>" : <i>String</i>,
    "<a href="#ebgpenforcemultihop" title="EbgpEnforceMultihop">EbgpEnforceMultihop</a>" : <i>String</i>,
    "<a href="#ebgpmultihopttl" title="EbgpMultihopTtl">EbgpMultihopTtl</a>" : <i>Double</i>,
    "<a href="#filterlistin" title="FilterListIn">FilterListIn</a>" : <i>String</i>,
    "<a href="#filterlistin6" title="FilterListIn6">FilterListIn6</a>" : <i>String</i>,
    "<a href="#filterlistout" title="FilterListOut">FilterListOut</a>" : <i>String</i>,
    "<a href="#filterlistout6" title="FilterListOut6">FilterListOut6</a>" : <i>String</i>,
    "<a href="#holdtimetimer" title="HoldtimeTimer">HoldtimeTimer</a>" : <i>Double</i>,
    "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
    "<a href="#keepalivetimer" title="KeepAliveTimer">KeepAliveTimer</a>" : <i>Double</i>,
    "<a href="#linkdownfailover" title="LinkDownFailover">LinkDownFailover</a>" : <i>String</i>,
    "<a href="#localas" title="LocalAs">LocalAs</a>" : <i>Double</i>,
    "<a href="#localasnoprepend" title="LocalAsNoPrepend">LocalAsNoPrepend</a>" : <i>String</i>,
    "<a href="#localasreplaceas" title="LocalAsReplaceAs">LocalAsReplaceAs</a>" : <i>String</i>,
    "<a href="#maximumprefix" title="MaximumPrefix">MaximumPrefix</a>" : <i>Double</i>,
    "<a href="#maximumprefix6" title="MaximumPrefix6">MaximumPrefix6</a>" : <i>Double</i>,
    "<a href="#maximumprefixthreshold" title="MaximumPrefixThreshold">MaximumPrefixThreshold</a>" : <i>Double</i>,
    "<a href="#maximumprefixthreshold6" title="MaximumPrefixThreshold6">MaximumPrefixThreshold6</a>" : <i>Double</i>,
    "<a href="#maximumprefixwarningonly" title="MaximumPrefixWarningOnly">MaximumPrefixWarningOnly</a>" : <i>String</i>,
    "<a href="#maximumprefixwarningonly6" title="MaximumPrefixWarningOnly6">MaximumPrefixWarningOnly6</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#nexthopself" title="NextHopSelf">NextHopSelf</a>" : <i>String</i>,
    "<a href="#nexthopself6" title="NextHopSelf6">NextHopSelf6</a>" : <i>String</i>,
    "<a href="#nexthopselfrr" title="NextHopSelfRr">NextHopSelfRr</a>" : <i>String</i>,
    "<a href="#nexthopselfrr6" title="NextHopSelfRr6">NextHopSelfRr6</a>" : <i>String</i>,
    "<a href="#overridecapability" title="OverrideCapability">OverrideCapability</a>" : <i>String</i>,
    "<a href="#passive" title="Passive">Passive</a>" : <i>String</i>,
    "<a href="#prefixlistin" title="PrefixListIn">PrefixListIn</a>" : <i>String</i>,
    "<a href="#prefixlistin6" title="PrefixListIn6">PrefixListIn6</a>" : <i>String</i>,
    "<a href="#prefixlistout" title="PrefixListOut">PrefixListOut</a>" : <i>String</i>,
    "<a href="#prefixlistout6" title="PrefixListOut6">PrefixListOut6</a>" : <i>String</i>,
    "<a href="#remoteas" title="RemoteAs">RemoteAs</a>" : <i>Double</i>,
    "<a href="#removeprivateas" title="RemovePrivateAs">RemovePrivateAs</a>" : <i>String</i>,
    "<a href="#removeprivateas6" title="RemovePrivateAs6">RemovePrivateAs6</a>" : <i>String</i>,
    "<a href="#restarttime" title="RestartTime">RestartTime</a>" : <i>Double</i>,
    "<a href="#retainstaletime" title="RetainStaleTime">RetainStaleTime</a>" : <i>Double</i>,
    "<a href="#routemapin" title="RouteMapIn">RouteMapIn</a>" : <i>String</i>,
    "<a href="#routemapin6" title="RouteMapIn6">RouteMapIn6</a>" : <i>String</i>,
    "<a href="#routemapout" title="RouteMapOut">RouteMapOut</a>" : <i>String</i>,
    "<a href="#routemapout6" title="RouteMapOut6">RouteMapOut6</a>" : <i>String</i>,
    "<a href="#routemapout6preferable" title="RouteMapOut6Preferable">RouteMapOut6Preferable</a>" : <i>String</i>,
    "<a href="#routemapoutpreferable" title="RouteMapOutPreferable">RouteMapOutPreferable</a>" : <i>String</i>,
    "<a href="#routereflectorclient" title="RouteReflectorClient">RouteReflectorClient</a>" : <i>String</i>,
    "<a href="#routereflectorclient6" title="RouteReflectorClient6">RouteReflectorClient6</a>" : <i>String</i>,
    "<a href="#routeserverclient" title="RouteServerClient">RouteServerClient</a>" : <i>String</i>,
    "<a href="#routeserverclient6" title="RouteServerClient6">RouteServerClient6</a>" : <i>String</i>,
    "<a href="#sendcommunity" title="SendCommunity">SendCommunity</a>" : <i>String</i>,
    "<a href="#sendcommunity6" title="SendCommunity6">SendCommunity6</a>" : <i>String</i>,
    "<a href="#shutdown" title="Shutdown">Shutdown</a>" : <i>String</i>,
    "<a href="#softreconfiguration" title="SoftReconfiguration">SoftReconfiguration</a>" : <i>String</i>,
    "<a href="#softreconfiguration6" title="SoftReconfiguration6">SoftReconfiguration6</a>" : <i>String</i>,
    "<a href="#staleroute" title="StaleRoute">StaleRoute</a>" : <i>String</i>,
    "<a href="#strictcapabilitymatch" title="StrictCapabilityMatch">StrictCapabilityMatch</a>" : <i>String</i>,
    "<a href="#unsuppressmap" title="UnsuppressMap">UnsuppressMap</a>" : <i>String</i>,
    "<a href="#unsuppressmap6" title="UnsuppressMap6">UnsuppressMap6</a>" : <i>String</i>,
    "<a href="#updatesource" title="UpdateSource">UpdateSource</a>" : <i>String</i>,
    "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#activate" title="Activate">Activate</a>: <i>String</i>
<a href="#activate6" title="Activate6">Activate6</a>: <i>String</i>
<a href="#additionalpath" title="AdditionalPath">AdditionalPath</a>: <i>String</i>
<a href="#additionalpath6" title="AdditionalPath6">AdditionalPath6</a>: <i>String</i>
<a href="#advadditionalpath" title="AdvAdditionalPath">AdvAdditionalPath</a>: <i>Double</i>
<a href="#advadditionalpath6" title="AdvAdditionalPath6">AdvAdditionalPath6</a>: <i>Double</i>
<a href="#advertisementinterval" title="AdvertisementInterval">AdvertisementInterval</a>: <i>Double</i>
<a href="#allowasin" title="AllowasIn">AllowasIn</a>: <i>Double</i>
<a href="#allowasin6" title="AllowasIn6">AllowasIn6</a>: <i>Double</i>
<a href="#allowasinenable" title="AllowasInEnable">AllowasInEnable</a>: <i>String</i>
<a href="#allowasinenable6" title="AllowasInEnable6">AllowasInEnable6</a>: <i>String</i>
<a href="#asoverride" title="AsOverride">AsOverride</a>: <i>String</i>
<a href="#asoverride6" title="AsOverride6">AsOverride6</a>: <i>String</i>
<a href="#attributeunchanged" title="AttributeUnchanged">AttributeUnchanged</a>: <i>String</i>
<a href="#attributeunchanged6" title="AttributeUnchanged6">AttributeUnchanged6</a>: <i>String</i>
<a href="#bfd" title="Bfd">Bfd</a>: <i>String</i>
<a href="#capabilitydefaultoriginate" title="CapabilityDefaultOriginate">CapabilityDefaultOriginate</a>: <i>String</i>
<a href="#capabilitydefaultoriginate6" title="CapabilityDefaultOriginate6">CapabilityDefaultOriginate6</a>: <i>String</i>
<a href="#capabilitydynamic" title="CapabilityDynamic">CapabilityDynamic</a>: <i>String</i>
<a href="#capabilitygracefulrestart" title="CapabilityGracefulRestart">CapabilityGracefulRestart</a>: <i>String</i>
<a href="#capabilitygracefulrestart6" title="CapabilityGracefulRestart6">CapabilityGracefulRestart6</a>: <i>String</i>
<a href="#capabilityorf" title="CapabilityOrf">CapabilityOrf</a>: <i>String</i>
<a href="#capabilityorf6" title="CapabilityOrf6">CapabilityOrf6</a>: <i>String</i>
<a href="#capabilityrouterefresh" title="CapabilityRouteRefresh">CapabilityRouteRefresh</a>: <i>String</i>
<a href="#connecttimer" title="ConnectTimer">ConnectTimer</a>: <i>Double</i>
<a href="#defaultoriginateroutemap" title="DefaultOriginateRoutemap">DefaultOriginateRoutemap</a>: <i>String</i>
<a href="#defaultoriginateroutemap6" title="DefaultOriginateRoutemap6">DefaultOriginateRoutemap6</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#distributelistin" title="DistributeListIn">DistributeListIn</a>: <i>String</i>
<a href="#distributelistin6" title="DistributeListIn6">DistributeListIn6</a>: <i>String</i>
<a href="#distributelistout" title="DistributeListOut">DistributeListOut</a>: <i>String</i>
<a href="#distributelistout6" title="DistributeListOut6">DistributeListOut6</a>: <i>String</i>
<a href="#dontcapabilitynegotiate" title="DontCapabilityNegotiate">DontCapabilityNegotiate</a>: <i>String</i>
<a href="#ebgpenforcemultihop" title="EbgpEnforceMultihop">EbgpEnforceMultihop</a>: <i>String</i>
<a href="#ebgpmultihopttl" title="EbgpMultihopTtl">EbgpMultihopTtl</a>: <i>Double</i>
<a href="#filterlistin" title="FilterListIn">FilterListIn</a>: <i>String</i>
<a href="#filterlistin6" title="FilterListIn6">FilterListIn6</a>: <i>String</i>
<a href="#filterlistout" title="FilterListOut">FilterListOut</a>: <i>String</i>
<a href="#filterlistout6" title="FilterListOut6">FilterListOut6</a>: <i>String</i>
<a href="#holdtimetimer" title="HoldtimeTimer">HoldtimeTimer</a>: <i>Double</i>
<a href="#interface" title="Interface">Interface</a>: <i>String</i>
<a href="#keepalivetimer" title="KeepAliveTimer">KeepAliveTimer</a>: <i>Double</i>
<a href="#linkdownfailover" title="LinkDownFailover">LinkDownFailover</a>: <i>String</i>
<a href="#localas" title="LocalAs">LocalAs</a>: <i>Double</i>
<a href="#localasnoprepend" title="LocalAsNoPrepend">LocalAsNoPrepend</a>: <i>String</i>
<a href="#localasreplaceas" title="LocalAsReplaceAs">LocalAsReplaceAs</a>: <i>String</i>
<a href="#maximumprefix" title="MaximumPrefix">MaximumPrefix</a>: <i>Double</i>
<a href="#maximumprefix6" title="MaximumPrefix6">MaximumPrefix6</a>: <i>Double</i>
<a href="#maximumprefixthreshold" title="MaximumPrefixThreshold">MaximumPrefixThreshold</a>: <i>Double</i>
<a href="#maximumprefixthreshold6" title="MaximumPrefixThreshold6">MaximumPrefixThreshold6</a>: <i>Double</i>
<a href="#maximumprefixwarningonly" title="MaximumPrefixWarningOnly">MaximumPrefixWarningOnly</a>: <i>String</i>
<a href="#maximumprefixwarningonly6" title="MaximumPrefixWarningOnly6">MaximumPrefixWarningOnly6</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#nexthopself" title="NextHopSelf">NextHopSelf</a>: <i>String</i>
<a href="#nexthopself6" title="NextHopSelf6">NextHopSelf6</a>: <i>String</i>
<a href="#nexthopselfrr" title="NextHopSelfRr">NextHopSelfRr</a>: <i>String</i>
<a href="#nexthopselfrr6" title="NextHopSelfRr6">NextHopSelfRr6</a>: <i>String</i>
<a href="#overridecapability" title="OverrideCapability">OverrideCapability</a>: <i>String</i>
<a href="#passive" title="Passive">Passive</a>: <i>String</i>
<a href="#prefixlistin" title="PrefixListIn">PrefixListIn</a>: <i>String</i>
<a href="#prefixlistin6" title="PrefixListIn6">PrefixListIn6</a>: <i>String</i>
<a href="#prefixlistout" title="PrefixListOut">PrefixListOut</a>: <i>String</i>
<a href="#prefixlistout6" title="PrefixListOut6">PrefixListOut6</a>: <i>String</i>
<a href="#remoteas" title="RemoteAs">RemoteAs</a>: <i>Double</i>
<a href="#removeprivateas" title="RemovePrivateAs">RemovePrivateAs</a>: <i>String</i>
<a href="#removeprivateas6" title="RemovePrivateAs6">RemovePrivateAs6</a>: <i>String</i>
<a href="#restarttime" title="RestartTime">RestartTime</a>: <i>Double</i>
<a href="#retainstaletime" title="RetainStaleTime">RetainStaleTime</a>: <i>Double</i>
<a href="#routemapin" title="RouteMapIn">RouteMapIn</a>: <i>String</i>
<a href="#routemapin6" title="RouteMapIn6">RouteMapIn6</a>: <i>String</i>
<a href="#routemapout" title="RouteMapOut">RouteMapOut</a>: <i>String</i>
<a href="#routemapout6" title="RouteMapOut6">RouteMapOut6</a>: <i>String</i>
<a href="#routemapout6preferable" title="RouteMapOut6Preferable">RouteMapOut6Preferable</a>: <i>String</i>
<a href="#routemapoutpreferable" title="RouteMapOutPreferable">RouteMapOutPreferable</a>: <i>String</i>
<a href="#routereflectorclient" title="RouteReflectorClient">RouteReflectorClient</a>: <i>String</i>
<a href="#routereflectorclient6" title="RouteReflectorClient6">RouteReflectorClient6</a>: <i>String</i>
<a href="#routeserverclient" title="RouteServerClient">RouteServerClient</a>: <i>String</i>
<a href="#routeserverclient6" title="RouteServerClient6">RouteServerClient6</a>: <i>String</i>
<a href="#sendcommunity" title="SendCommunity">SendCommunity</a>: <i>String</i>
<a href="#sendcommunity6" title="SendCommunity6">SendCommunity6</a>: <i>String</i>
<a href="#shutdown" title="Shutdown">Shutdown</a>: <i>String</i>
<a href="#softreconfiguration" title="SoftReconfiguration">SoftReconfiguration</a>: <i>String</i>
<a href="#softreconfiguration6" title="SoftReconfiguration6">SoftReconfiguration6</a>: <i>String</i>
<a href="#staleroute" title="StaleRoute">StaleRoute</a>: <i>String</i>
<a href="#strictcapabilitymatch" title="StrictCapabilityMatch">StrictCapabilityMatch</a>: <i>String</i>
<a href="#unsuppressmap" title="UnsuppressMap">UnsuppressMap</a>: <i>String</i>
<a href="#unsuppressmap6" title="UnsuppressMap6">UnsuppressMap6</a>: <i>String</i>
<a href="#updatesource" title="UpdateSource">UpdateSource</a>: <i>String</i>
<a href="#weight" title="Weight">Weight</a>: <i>Double</i>
</pre>

## Properties

#### Activate

Enable/disable address family IPv4 for this neighbor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Activate6

Enable/disable address family IPv6 for this neighbor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalPath

Enable/disable IPv4 additional-path capability. Valid values: `send`, `receive`, `both`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalPath6

Enable/disable IPv6 additional-path capability. Valid values: `send`, `receive`, `both`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvAdditionalPath

Number of IPv4 additional paths that can be advertised to this neighbor.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvAdditionalPath6

Number of IPv6 additional paths that can be advertised to this neighbor.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertisementInterval

Minimum interval (sec) between sending updates.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowasIn

IPv4 The maximum number of occurrence of my AS number allowed.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowasIn6

IPv6 The maximum number of occurrence of my AS number allowed.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowasInEnable

Enable/disable IPv4 Enable to allow my AS in AS path. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowasInEnable6

Enable/disable IPv6 Enable to allow my AS in AS path. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsOverride

Enable/disable replace peer AS with own AS for IPv4. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsOverride6

Enable/disable replace peer AS with own AS for IPv6. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttributeUnchanged

IPv4 List of attributes that should be unchanged. Valid values: `as-path`, `med`, `next-hop`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttributeUnchanged6

IPv6 List of attributes that should be unchanged. Valid values: `as-path`, `med`, `next-hop`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bfd

Enable/disable BFD for this neighbor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapabilityDefaultOriginate

Enable/disable advertise default IPv4 route to this neighbor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapabilityDefaultOriginate6

Enable/disable advertise default IPv6 route to this neighbor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapabilityDynamic

Enable/disable advertise dynamic capability to this neighbor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapabilityGracefulRestart

Enable/disable advertise IPv4 graceful restart capability to this neighbor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapabilityGracefulRestart6

Enable/disable advertise IPv6 graceful restart capability to this neighbor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapabilityOrf

Accept/Send IPv4 ORF lists to/from this neighbor. Valid values: `none`, `receive`, `send`, `both`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapabilityOrf6

Accept/Send IPv6 ORF lists to/from this neighbor. Valid values: `none`, `receive`, `send`, `both`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapabilityRouteRefresh

Enable/disable advertise route refresh capability to this neighbor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectTimer

Interval (sec) for connect timer.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultOriginateRoutemap

Route map to specify criteria to originate IPv4 default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultOriginateRoutemap6

Route map to specify criteria to originate IPv6 default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributeListIn

Filter for IPv4 updates from this neighbor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributeListIn6

Filter for IPv6 updates from this neighbor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributeListOut

Filter for IPv4 updates to this neighbor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributeListOut6

Filter for IPv6 updates to this neighbor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DontCapabilityNegotiate

Don't negotiate capabilities with this neighbor Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbgpEnforceMultihop

Enable/disable allow multi-hop EBGP neighbors. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbgpMultihopTtl

EBGP multihop TTL for this peer.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterListIn

BGP filter for IPv4 inbound routes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterListIn6

BGP filter for IPv6 inbound routes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterListOut

BGP filter for IPv4 outbound routes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterListOut6

BGP filter for IPv6 outbound routes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HoldtimeTimer

Interval (sec) before peer considered dead.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepAliveTimer

Keep alive timer interval (sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkDownFailover

Enable/disable failover upon link down. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAs

Local AS number of neighbor.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAsNoPrepend

Do not prepend local-as to incoming updates. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAsReplaceAs

Replace real AS with local-as in outgoing updates. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumPrefix

Maximum number of IPv4 prefixes to accept from this peer.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumPrefix6

Maximum number of IPv6 prefixes to accept from this peer.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumPrefixThreshold

Maximum IPv4 prefix threshold value (1 - 100 percent).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumPrefixThreshold6

Maximum IPv6 prefix threshold value (1 - 100 percent).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumPrefixWarningOnly

Enable/disable IPv4 Only give warning message when limit is exceeded. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumPrefixWarningOnly6

Enable/disable IPv6 Only give warning message when limit is exceeded. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Neighbor group name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHopSelf

Enable/disable IPv4 next-hop calculation for this neighbor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHopSelf6

Enable/disable IPv6 next-hop calculation for this neighbor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHopSelfRr

Enable/disable setting nexthop's address to interface's IPv4 address for route-reflector routes. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHopSelfRr6

Enable/disable setting nexthop's address to interface's IPv6 address for route-reflector routes. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideCapability

Enable/disable override result of capability negotiation. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Passive

Enable/disable sending of open messages to this neighbor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixListIn

IPv4 Inbound filter for updates from this neighbor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixListIn6

IPv6 Inbound filter for updates from this neighbor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixListOut

IPv4 Outbound filter for updates to this neighbor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixListOut6

IPv6 Outbound filter for updates to this neighbor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteAs

AS number of neighbor.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemovePrivateAs

Enable/disable remove private AS number from IPv4 outbound updates. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemovePrivateAs6

Enable/disable remove private AS number from IPv6 outbound updates. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestartTime

Graceful restart delay time (sec, 0 = global default).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetainStaleTime

Time to retain stale routes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteMapIn

IPv4 Inbound route map filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteMapIn6

IPv6 Inbound route map filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteMapOut

IPv4 Outbound route map filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteMapOut6

IPv6 Outbound route map filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteMapOut6Preferable

IPv6 outbound route map filter if the peer is preferred.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteMapOutPreferable

IPv4 outbound route map filter if the peer is preferred.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteReflectorClient

Enable/disable IPv4 AS route reflector client. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteReflectorClient6

Enable/disable IPv6 AS route reflector client. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteServerClient

Enable/disable IPv4 AS route server client. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteServerClient6

Enable/disable IPv6 AS route server client. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendCommunity

IPv4 Send community attribute to neighbor. Valid values: `standard`, `extended`, `both`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendCommunity6

IPv6 Send community attribute to neighbor. Valid values: `standard`, `extended`, `both`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shutdown

Enable/disable shutdown this neighbor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftReconfiguration

Enable/disable allow IPv4 inbound soft reconfiguration. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftReconfiguration6

Enable/disable allow IPv6 inbound soft reconfiguration. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaleRoute

Enable/disable stale route after neighbor down. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrictCapabilityMatch

Enable/disable strict capability matching. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnsuppressMap

IPv4 Route map to selectively unsuppress suppressed routes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnsuppressMap6

IPv6 Route map to selectively unsuppress suppressed routes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateSource

Interface to use as source IP/IPv6 address of TCP connections.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

Neighbor weight.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

