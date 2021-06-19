# TF::AVI::Virtualservice

The VirtualService resource allows the creation and management of Avi VirtualService

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Virtualservice",
    "Properties" : {
        "<a href="#activestandbysetag" title="ActiveStandbySeTag">ActiveStandbySeTag</a>" : <i>String</i>,
        "<a href="#advertisedownvs" title="AdvertiseDownVs">AdvertiseDownVs</a>" : <i>Boolean</i>,
        "<a href="#allowinvalidclientcert" title="AllowInvalidClientCert">AllowInvalidClientCert</a>" : <i>Boolean</i>,
        "<a href="#analyticsprofileref" title="AnalyticsProfileRef">AnalyticsProfileRef</a>" : <i>String</i>,
        "<a href="#apiccontractgraph" title="ApicContractGraph">ApicContractGraph</a>" : <i>String</i>,
        "<a href="#applicationprofileref" title="ApplicationProfileRef">ApplicationProfileRef</a>" : <i>String</i>,
        "<a href="#bgppeerlabels" title="BgpPeerLabels">BgpPeerLabels</a>" : <i>[ String, ... ]</i>,
        "<a href="#bulksynckvcache" title="BulkSyncKvcache">BulkSyncKvcache</a>" : <i>Boolean</i>,
        "<a href="#closeclientconnonconfigupdate" title="CloseClientConnOnConfigUpdate">CloseClientConnOnConfigUpdate</a>" : <i>Boolean</i>,
        "<a href="#cloudconfigcksum" title="CloudConfigCksum">CloudConfigCksum</a>" : <i>String</i>,
        "<a href="#cloudref" title="CloudRef">CloudRef</a>" : <i>String</i>,
        "<a href="#cloudtype" title="CloudType">CloudType</a>" : <i>String</i>,
        "<a href="#createdby" title="CreatedBy">CreatedBy</a>" : <i>String</i>,
        "<a href="#delayfairness" title="DelayFairness">DelayFairness</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#eastwestplacement" title="EastWestPlacement">EastWestPlacement</a>" : <i>Boolean</i>,
        "<a href="#enableautogw" title="EnableAutogw">EnableAutogw</a>" : <i>Boolean</i>,
        "<a href="#enablerhi" title="EnableRhi">EnableRhi</a>" : <i>Boolean</i>,
        "<a href="#enablerhisnat" title="EnableRhiSnat">EnableRhiSnat</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#errorpageprofileref" title="ErrorPageProfileRef">ErrorPageProfileRef</a>" : <i>String</i>,
        "<a href="#flowdist" title="FlowDist">FlowDist</a>" : <i>String</i>,
        "<a href="#flowlabeltype" title="FlowLabelType">FlowLabelType</a>" : <i>String</i>,
        "<a href="#fqdn" title="Fqdn">Fqdn</a>" : <i>String</i>,
        "<a href="#hostnamexlate" title="HostNameXlate">HostNameXlate</a>" : <i>String</i>,
        "<a href="#icaprequestprofilerefs" title="IcapRequestProfileRefs">IcapRequestProfileRefs</a>" : <i>[ String, ... ]</i>,
        "<a href="#ignpoolnetreach" title="IgnPoolNetReach">IgnPoolNetReach</a>" : <i>Boolean</i>,
        "<a href="#limitdoser" title="LimitDoser">LimitDoser</a>" : <i>Boolean</i>,
        "<a href="#maxcpsperclient" title="MaxCpsPerClient">MaxCpsPerClient</a>" : <i>Double</i>,
        "<a href="#microserviceref" title="MicroserviceRef">MicroserviceRef</a>" : <i>String</i>,
        "<a href="#minpoolsup" title="MinPoolsUp">MinPoolsUp</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkprofileref" title="NetworkProfileRef">NetworkProfileRef</a>" : <i>String</i>,
        "<a href="#networksecuritypolicyref" title="NetworkSecurityPolicyRef">NetworkSecurityPolicyRef</a>" : <i>String</i>,
        "<a href="#nsxsecuritygroup" title="NsxSecuritygroup">NsxSecuritygroup</a>" : <i>[ String, ... ]</i>,
        "<a href="#poolgroupref" title="PoolGroupRef">PoolGroupRef</a>" : <i>String</i>,
        "<a href="#poolref" title="PoolRef">PoolRef</a>" : <i>String</i>,
        "<a href="#removelisteningportonvsdown" title="RemoveListeningPortOnVsDown">RemoveListeningPortOnVsDown</a>" : <i>Boolean</i>,
        "<a href="#scaleoutecmp" title="ScaleoutEcmp">ScaleoutEcmp</a>" : <i>Boolean</i>,
        "<a href="#segroupref" title="SeGroupRef">SeGroupRef</a>" : <i>String</i>,
        "<a href="#securitypolicyref" title="SecurityPolicyRef">SecurityPolicyRef</a>" : <i>String</i>,
        "<a href="#servernetworkprofileref" title="ServerNetworkProfileRef">ServerNetworkProfileRef</a>" : <i>String</i>,
        "<a href="#servicemetadata" title="ServiceMetadata">ServiceMetadata</a>" : <i>String</i>,
        "<a href="#sslkeyandcertificaterefs" title="SslKeyAndCertificateRefs">SslKeyAndCertificateRefs</a>" : <i>[ String, ... ]</i>,
        "<a href="#sslprofileref" title="SslProfileRef">SslProfileRef</a>" : <i>String</i>,
        "<a href="#sslsesscacheavgsize" title="SslSessCacheAvgSize">SslSessCacheAvgSize</a>" : <i>Double</i>,
        "<a href="#ssopolicyref" title="SsoPolicyRef">SsoPolicyRef</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#testsedatastorelevel1ref" title="TestSeDatastoreLevel1Ref">TestSeDatastoreLevel1Ref</a>" : <i>String</i>,
        "<a href="#trafficcloneprofileref" title="TrafficCloneProfileRef">TrafficCloneProfileRef</a>" : <i>String</i>,
        "<a href="#trafficenabled" title="TrafficEnabled">TrafficEnabled</a>" : <i>Boolean</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#usebridgeipasvip" title="UseBridgeIpAsVip">UseBridgeIpAsVip</a>" : <i>Boolean</i>,
        "<a href="#usevipassnat" title="UseVipAsSnat">UseVipAsSnat</a>" : <i>Boolean</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vhdomainname" title="VhDomainName">VhDomainName</a>" : <i>[ String, ... ]</i>,
        "<a href="#vhparentvsuuid" title="VhParentVsUuid">VhParentVsUuid</a>" : <i>String</i>,
        "<a href="#vhtype" title="VhType">VhType</a>" : <i>String</i>,
        "<a href="#vrfcontextref" title="VrfContextRef">VrfContextRef</a>" : <i>String</i>,
        "<a href="#vsvipcloudconfigcksum" title="VsvipCloudConfigCksum">VsvipCloudConfigCksum</a>" : <i>String</i>,
        "<a href="#vsvipref" title="VsvipRef">VsvipRef</a>" : <i>String</i>,
        "<a href="#wafpolicyref" title="WafPolicyRef">WafPolicyRef</a>" : <i>String</i>,
        "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>,
        "<a href="#analyticspolicy" title="AnalyticsPolicy">AnalyticsPolicy</a>" : <i>[ <a href="analyticspolicydefinition.md">AnalyticsPolicyDefinition</a>, ... ]</i>,
        "<a href="#clientauth" title="ClientAuth">ClientAuth</a>" : <i>[ <a href="clientauthdefinition.md">ClientAuthDefinition</a>, ... ]</i>,
        "<a href="#connectionsratelimit" title="ConnectionsRateLimit">ConnectionsRateLimit</a>" : <i>[ <a href="connectionsratelimitdefinition.md">ConnectionsRateLimitDefinition</a>, ... ]</i>,
        "<a href="#contentrewrite" title="ContentRewrite">ContentRewrite</a>" : <i>[ <a href="contentrewritedefinition.md">ContentRewriteDefinition</a>, ... ]</i>,
        "<a href="#dnsinfo" title="DnsInfo">DnsInfo</a>" : <i>[ <a href="dnsinfodefinition.md">DnsInfoDefinition</a>, ... ]</i>,
        "<a href="#dnspolicies" title="DnsPolicies">DnsPolicies</a>" : <i>[ <a href="dnspoliciesdefinition.md">DnsPoliciesDefinition</a>, ... ]</i>,
        "<a href="#httppolicies" title="HttpPolicies">HttpPolicies</a>" : <i>[ <a href="httppoliciesdefinition.md">HttpPoliciesDefinition</a>, ... ]</i>,
        "<a href="#jwtconfig" title="JwtConfig">JwtConfig</a>" : <i>[ <a href="jwtconfigdefinition.md">JwtConfigDefinition</a>, ... ]</i>,
        "<a href="#l4policies" title="L4Policies">L4Policies</a>" : <i>[ <a href="l4policiesdefinition.md">L4PoliciesDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>,
        "<a href="#performancelimits" title="PerformanceLimits">PerformanceLimits</a>" : <i>[ <a href="performancelimitsdefinition.md">PerformanceLimitsDefinition</a>, ... ]</i>,
        "<a href="#requestsratelimit" title="RequestsRateLimit">RequestsRateLimit</a>" : <i>[ <a href="requestsratelimitdefinition.md">RequestsRateLimitDefinition</a>, ... ]</i>,
        "<a href="#samlspconfig" title="SamlSpConfig">SamlSpConfig</a>" : <i>[ <a href="samlspconfigdefinition.md">SamlSpConfigDefinition</a>, ... ]</i>,
        "<a href="#servicepoolselect" title="ServicePoolSelect">ServicePoolSelect</a>" : <i>[ <a href="servicepoolselectdefinition.md">ServicePoolSelectDefinition</a>, ... ]</i>,
        "<a href="#services" title="Services">Services</a>" : <i>[ <a href="servicesdefinition.md">ServicesDefinition</a>, ... ]</i>,
        "<a href="#sidebandprofile" title="SidebandProfile">SidebandProfile</a>" : <i>[ <a href="sidebandprofiledefinition.md">SidebandProfileDefinition</a>, ... ]</i>,
        "<a href="#snatip" title="SnatIp">SnatIp</a>" : <i>[ <a href="snatipdefinition.md">SnatIpDefinition</a>, ... ]</i>,
        "<a href="#sslprofileselectors" title="SslProfileSelectors">SslProfileSelectors</a>" : <i>[ <a href="sslprofileselectorsdefinition.md">SslProfileSelectorsDefinition</a>, ... ]</i>,
        "<a href="#staticdnsrecords" title="StaticDnsRecords">StaticDnsRecords</a>" : <i>[ <a href="staticdnsrecordsdefinition.md">StaticDnsRecordsDefinition</a>, ... ]</i>,
        "<a href="#topologypolicies" title="TopologyPolicies">TopologyPolicies</a>" : <i>[ <a href="topologypoliciesdefinition.md">TopologyPoliciesDefinition</a>, ... ]</i>,
        "<a href="#vhmatches" title="VhMatches">VhMatches</a>" : <i>[ <a href="vhmatchesdefinition.md">VhMatchesDefinition</a>, ... ]</i>,
        "<a href="#vip" title="Vip">Vip</a>" : <i>[ <a href="vipdefinition.md">VipDefinition</a>, ... ]</i>,
        "<a href="#vsdatascripts" title="VsDatascripts">VsDatascripts</a>" : <i>[ <a href="vsdatascriptsdefinition.md">VsDatascriptsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Virtualservice
Properties:
    <a href="#activestandbysetag" title="ActiveStandbySeTag">ActiveStandbySeTag</a>: <i>String</i>
    <a href="#advertisedownvs" title="AdvertiseDownVs">AdvertiseDownVs</a>: <i>Boolean</i>
    <a href="#allowinvalidclientcert" title="AllowInvalidClientCert">AllowInvalidClientCert</a>: <i>Boolean</i>
    <a href="#analyticsprofileref" title="AnalyticsProfileRef">AnalyticsProfileRef</a>: <i>String</i>
    <a href="#apiccontractgraph" title="ApicContractGraph">ApicContractGraph</a>: <i>String</i>
    <a href="#applicationprofileref" title="ApplicationProfileRef">ApplicationProfileRef</a>: <i>String</i>
    <a href="#bgppeerlabels" title="BgpPeerLabels">BgpPeerLabels</a>: <i>
      - String</i>
    <a href="#bulksynckvcache" title="BulkSyncKvcache">BulkSyncKvcache</a>: <i>Boolean</i>
    <a href="#closeclientconnonconfigupdate" title="CloseClientConnOnConfigUpdate">CloseClientConnOnConfigUpdate</a>: <i>Boolean</i>
    <a href="#cloudconfigcksum" title="CloudConfigCksum">CloudConfigCksum</a>: <i>String</i>
    <a href="#cloudref" title="CloudRef">CloudRef</a>: <i>String</i>
    <a href="#cloudtype" title="CloudType">CloudType</a>: <i>String</i>
    <a href="#createdby" title="CreatedBy">CreatedBy</a>: <i>String</i>
    <a href="#delayfairness" title="DelayFairness">DelayFairness</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#eastwestplacement" title="EastWestPlacement">EastWestPlacement</a>: <i>Boolean</i>
    <a href="#enableautogw" title="EnableAutogw">EnableAutogw</a>: <i>Boolean</i>
    <a href="#enablerhi" title="EnableRhi">EnableRhi</a>: <i>Boolean</i>
    <a href="#enablerhisnat" title="EnableRhiSnat">EnableRhiSnat</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#errorpageprofileref" title="ErrorPageProfileRef">ErrorPageProfileRef</a>: <i>String</i>
    <a href="#flowdist" title="FlowDist">FlowDist</a>: <i>String</i>
    <a href="#flowlabeltype" title="FlowLabelType">FlowLabelType</a>: <i>String</i>
    <a href="#fqdn" title="Fqdn">Fqdn</a>: <i>String</i>
    <a href="#hostnamexlate" title="HostNameXlate">HostNameXlate</a>: <i>String</i>
    <a href="#icaprequestprofilerefs" title="IcapRequestProfileRefs">IcapRequestProfileRefs</a>: <i>
      - String</i>
    <a href="#ignpoolnetreach" title="IgnPoolNetReach">IgnPoolNetReach</a>: <i>Boolean</i>
    <a href="#limitdoser" title="LimitDoser">LimitDoser</a>: <i>Boolean</i>
    <a href="#maxcpsperclient" title="MaxCpsPerClient">MaxCpsPerClient</a>: <i>Double</i>
    <a href="#microserviceref" title="MicroserviceRef">MicroserviceRef</a>: <i>String</i>
    <a href="#minpoolsup" title="MinPoolsUp">MinPoolsUp</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkprofileref" title="NetworkProfileRef">NetworkProfileRef</a>: <i>String</i>
    <a href="#networksecuritypolicyref" title="NetworkSecurityPolicyRef">NetworkSecurityPolicyRef</a>: <i>String</i>
    <a href="#nsxsecuritygroup" title="NsxSecuritygroup">NsxSecuritygroup</a>: <i>
      - String</i>
    <a href="#poolgroupref" title="PoolGroupRef">PoolGroupRef</a>: <i>String</i>
    <a href="#poolref" title="PoolRef">PoolRef</a>: <i>String</i>
    <a href="#removelisteningportonvsdown" title="RemoveListeningPortOnVsDown">RemoveListeningPortOnVsDown</a>: <i>Boolean</i>
    <a href="#scaleoutecmp" title="ScaleoutEcmp">ScaleoutEcmp</a>: <i>Boolean</i>
    <a href="#segroupref" title="SeGroupRef">SeGroupRef</a>: <i>String</i>
    <a href="#securitypolicyref" title="SecurityPolicyRef">SecurityPolicyRef</a>: <i>String</i>
    <a href="#servernetworkprofileref" title="ServerNetworkProfileRef">ServerNetworkProfileRef</a>: <i>String</i>
    <a href="#servicemetadata" title="ServiceMetadata">ServiceMetadata</a>: <i>String</i>
    <a href="#sslkeyandcertificaterefs" title="SslKeyAndCertificateRefs">SslKeyAndCertificateRefs</a>: <i>
      - String</i>
    <a href="#sslprofileref" title="SslProfileRef">SslProfileRef</a>: <i>String</i>
    <a href="#sslsesscacheavgsize" title="SslSessCacheAvgSize">SslSessCacheAvgSize</a>: <i>Double</i>
    <a href="#ssopolicyref" title="SsoPolicyRef">SsoPolicyRef</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#testsedatastorelevel1ref" title="TestSeDatastoreLevel1Ref">TestSeDatastoreLevel1Ref</a>: <i>String</i>
    <a href="#trafficcloneprofileref" title="TrafficCloneProfileRef">TrafficCloneProfileRef</a>: <i>String</i>
    <a href="#trafficenabled" title="TrafficEnabled">TrafficEnabled</a>: <i>Boolean</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#usebridgeipasvip" title="UseBridgeIpAsVip">UseBridgeIpAsVip</a>: <i>Boolean</i>
    <a href="#usevipassnat" title="UseVipAsSnat">UseVipAsSnat</a>: <i>Boolean</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vhdomainname" title="VhDomainName">VhDomainName</a>: <i>
      - String</i>
    <a href="#vhparentvsuuid" title="VhParentVsUuid">VhParentVsUuid</a>: <i>String</i>
    <a href="#vhtype" title="VhType">VhType</a>: <i>String</i>
    <a href="#vrfcontextref" title="VrfContextRef">VrfContextRef</a>: <i>String</i>
    <a href="#vsvipcloudconfigcksum" title="VsvipCloudConfigCksum">VsvipCloudConfigCksum</a>: <i>String</i>
    <a href="#vsvipref" title="VsvipRef">VsvipRef</a>: <i>String</i>
    <a href="#wafpolicyref" title="WafPolicyRef">WafPolicyRef</a>: <i>String</i>
    <a href="#weight" title="Weight">Weight</a>: <i>Double</i>
    <a href="#analyticspolicy" title="AnalyticsPolicy">AnalyticsPolicy</a>: <i>
      - <a href="analyticspolicydefinition.md">AnalyticsPolicyDefinition</a></i>
    <a href="#clientauth" title="ClientAuth">ClientAuth</a>: <i>
      - <a href="clientauthdefinition.md">ClientAuthDefinition</a></i>
    <a href="#connectionsratelimit" title="ConnectionsRateLimit">ConnectionsRateLimit</a>: <i>
      - <a href="connectionsratelimitdefinition.md">ConnectionsRateLimitDefinition</a></i>
    <a href="#contentrewrite" title="ContentRewrite">ContentRewrite</a>: <i>
      - <a href="contentrewritedefinition.md">ContentRewriteDefinition</a></i>
    <a href="#dnsinfo" title="DnsInfo">DnsInfo</a>: <i>
      - <a href="dnsinfodefinition.md">DnsInfoDefinition</a></i>
    <a href="#dnspolicies" title="DnsPolicies">DnsPolicies</a>: <i>
      - <a href="dnspoliciesdefinition.md">DnsPoliciesDefinition</a></i>
    <a href="#httppolicies" title="HttpPolicies">HttpPolicies</a>: <i>
      - <a href="httppoliciesdefinition.md">HttpPoliciesDefinition</a></i>
    <a href="#jwtconfig" title="JwtConfig">JwtConfig</a>: <i>
      - <a href="jwtconfigdefinition.md">JwtConfigDefinition</a></i>
    <a href="#l4policies" title="L4Policies">L4Policies</a>: <i>
      - <a href="l4policiesdefinition.md">L4PoliciesDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
    <a href="#performancelimits" title="PerformanceLimits">PerformanceLimits</a>: <i>
      - <a href="performancelimitsdefinition.md">PerformanceLimitsDefinition</a></i>
    <a href="#requestsratelimit" title="RequestsRateLimit">RequestsRateLimit</a>: <i>
      - <a href="requestsratelimitdefinition.md">RequestsRateLimitDefinition</a></i>
    <a href="#samlspconfig" title="SamlSpConfig">SamlSpConfig</a>: <i>
      - <a href="samlspconfigdefinition.md">SamlSpConfigDefinition</a></i>
    <a href="#servicepoolselect" title="ServicePoolSelect">ServicePoolSelect</a>: <i>
      - <a href="servicepoolselectdefinition.md">ServicePoolSelectDefinition</a></i>
    <a href="#services" title="Services">Services</a>: <i>
      - <a href="servicesdefinition.md">ServicesDefinition</a></i>
    <a href="#sidebandprofile" title="SidebandProfile">SidebandProfile</a>: <i>
      - <a href="sidebandprofiledefinition.md">SidebandProfileDefinition</a></i>
    <a href="#snatip" title="SnatIp">SnatIp</a>: <i>
      - <a href="snatipdefinition.md">SnatIpDefinition</a></i>
    <a href="#sslprofileselectors" title="SslProfileSelectors">SslProfileSelectors</a>: <i>
      - <a href="sslprofileselectorsdefinition.md">SslProfileSelectorsDefinition</a></i>
    <a href="#staticdnsrecords" title="StaticDnsRecords">StaticDnsRecords</a>: <i>
      - <a href="staticdnsrecordsdefinition.md">StaticDnsRecordsDefinition</a></i>
    <a href="#topologypolicies" title="TopologyPolicies">TopologyPolicies</a>: <i>
      - <a href="topologypoliciesdefinition.md">TopologyPoliciesDefinition</a></i>
    <a href="#vhmatches" title="VhMatches">VhMatches</a>: <i>
      - <a href="vhmatchesdefinition.md">VhMatchesDefinition</a></i>
    <a href="#vip" title="Vip">Vip</a>: <i>
      - <a href="vipdefinition.md">VipDefinition</a></i>
    <a href="#vsdatascripts" title="VsDatascripts">VsDatascripts</a>: <i>
      - <a href="vsdatascriptsdefinition.md">VsDatascriptsDefinition</a></i>
</pre>

## Properties

#### ActiveStandbySeTag

This configuration only applies if the virtualservice is in legacy active standby ha mode and load distribution among active standby is enabled. This field is used to tag the virtualservice so that virtualservices with the same tag will share the same active serviceengine. Virtualservices with different tags will have different active serviceengines. If one of the serviceengine's in the serviceenginegroup fails, all virtualservices will end up using the same active serviceengine. Redistribution of the virtualservices can be either manual or automated when the failed serviceengine recovers. Redistribution is based on the auto redistribute property of the serviceenginegroup. Enum options - ACTIVE_STANDBY_SE_1, ACTIVE_STANDBY_SE_2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseDownVs

Keep advertising virtual service via bgp even if it is marked down by health monitor. This setting takes effect for future virtual service flaps. To advertise current vses that are down, please disable and re-enable the virtual service. Field introduced in 20.1.1. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowInvalidClientCert

Process request even if invalid client certificate is presented. Datascript apis need to be used for processing of such requests. Field introduced in 18.2.3. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnalyticsProfileRef

Specifies settings related to analytics. It is a reference to an object of type analyticsprofile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApicContractGraph

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationProfileRef

Enable application layer specific features for the virtual service. It is a reference to an object of type applicationprofile. Special default for essentials edition is system-l4-application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpPeerLabels

Select bgp peers, using peer label, for vsvip advertisement. Field introduced in 20.1.5. Maximum of 128 items allowed.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BulkSyncKvcache

(this is a beta feature). Sync key-value cache to the new ses when vs is scaled out. For ex  ssl sessions are stored using vs's key-value cache. When the vs is scaled out, the ssl session information is synced to the new se, allowing existing ssl sessions to be reused on the new se. Field introduced in 17.2.7, 18.1.1. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloseClientConnOnConfigUpdate

Close client connection on vs config update. Field introduced in 17.2.4. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudConfigCksum

Checksum of cloud configuration for vs. Internally set by cloud connector.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudRef

It is a reference to an object of type cloud.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudType

Enum options - cloud_none, cloud_vcenter, cloud_openstack, cloud_aws, cloud_vca, cloud_apic, cloud_mesos, cloud_linuxserver, cloud_docker_ucp, cloud_rancher, cloud_oshift_k8s, cloud_azure, cloud_gcp, cloud_nsxt. Allowed in basic(allowed values- cloud_none,cloud_nsxt) edition, essentials(allowed values- cloud_none,cloud_vcenter) edition, enterprise edition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreatedBy

Creator name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelayFairness

Select the algorithm for qos fairness. This determines how multiple virtual services sharing the same service engines will prioritize traffic over a congested network. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

User defined description for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EastWestPlacement

Force placement on all se's in service group (mesos mode only). Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutogw

Response traffic to clients will be sent back to the source mac address of the connection, rather than statically sent to a default gateway. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition. Special default for basic edition is false, essentials edition is false, enterprise is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableRhi

Enable route health injection using the bgp config in the vrf context.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableRhiSnat

Enable route health injection for source nat'ted floating ip address using the bgp config in the vrf context.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Enable or disable the virtual service.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErrorPageProfileRef

Error page profile to be used for this virtualservice.this profile is used to send the custom error page to the client generated by the proxy. It is a reference to an object of type errorpageprofile. Field introduced in 17.2.4.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlowDist

Criteria for flow distribution among ses. Enum options - LOAD_AWARE, CONSISTENT_HASH_SOURCE_IP_ADDRESS, CONSISTENT_HASH_SOURCE_IP_ADDRESS_AND_PORT. Allowed in basic(allowed values- load_aware) edition, essentials(allowed values- load_aware) edition, enterprise edition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlowLabelType

Criteria for flow labelling. Enum options - NO_LABEL, APPLICATION_LABEL, SERVICE_LABEL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fqdn

Dns resolvable, fully qualified domain name of the virtualservice. Only one of 'fqdn' and 'dns_info' configuration is allowed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostNameXlate

Translate the host name sent to the servers to this value. Translate the host name sent from servers back to the value used by the client.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcapRequestProfileRefs

The config settings for the icap server when checking the http request. It is a reference to an object of type icapprofile. Field introduced in 20.1.1. Maximum of 1 items allowed. Allowed in basic edition, essentials edition, enterprise edition.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnPoolNetReach

Ignore pool servers network reachability constraints for virtual service placement.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitDoser

Limit potential dos attackers who exceed max_cps_per_client significantly to a fraction of max_cps_per_client for a while.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCpsPerClient

Maximum connections per second per client ip. Allowed values are 10-1000. Special values are 0- 'unlimited'.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MicroserviceRef

Microservice representing the virtual service. It is a reference to an object of type microservice.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinPoolsUp

Minimum number of up pools to mark vs up. Field introduced in 18.2.1, 17.2.12.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name for the virtual service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkProfileRef

Determines network settings such as protocol, tcp or udp, and related options for the protocol. It is a reference to an object of type networkprofile. Special default for essentials edition is system-tcp-fast-path.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkSecurityPolicyRef

Network security policies for the virtual service. It is a reference to an object of type networksecuritypolicy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxSecuritygroup

A list of nsx groups representing the clients which can access the virtual ip of the virtual service. Field introduced in 17.1.1.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolGroupRef

The pool group is an object that contains pools. It is a reference to an object of type poolgroup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolRef

The pool is an object that contains destination servers and related attributes such as load-balancing and persistence. It is a reference to an object of type pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoveListeningPortOnVsDown

Remove listening port if virtualservice is down.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleoutEcmp

Disable re-distribution of flows across service engines for a virtual service. Enable if the network itself performs flow hashing with ecmp in environments such as gcp.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeGroupRef

The service engine group to use for this virtual service. Moving to a new se group is disruptive to existing connections for this vs. It is a reference to an object of type serviceenginegroup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityPolicyRef

Security policy applied on the traffic of the virtual service. This policy is used to perform security actions such as distributed denial of service (ddos) attack mitigation, etc. It is a reference to an object of type securitypolicy. Field introduced in 18.2.1. Allowed in basic edition, essentials edition, enterprise edition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerNetworkProfileRef

Determines the network settings profile for the server side of tcp proxied connections. Leave blank to use the same settings as the client to vs side of the connection. It is a reference to an object of type networkprofile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceMetadata

Metadata pertaining to the service provided by this virtual service. In openshift/kubernetes environments, egress pod info is stored. Any user input to this field will be overwritten by avi vantage.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslKeyAndCertificateRefs

Select or create one or two certificates, ec and/or rsa, that will be presented to ssl/tls terminated connections. It is a reference to an object of type sslkeyandcertificate.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslProfileRef

Determines the set of ssl versions and ciphers to accept for ssl/tls terminated connections. It is a reference to an object of type sslprofile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslSessCacheAvgSize

Expected number of ssl session cache entries (may be exceeded). Allowed values are 1024-16383.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsoPolicyRef

The sso policy attached to the virtualservice. It is a reference to an object of type ssopolicy. Field introduced in 18.2.3. Allowed in basic edition, essentials edition, enterprise edition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestSeDatastoreLevel1Ref

Used for testing se datastore upgrade 2.0 functionality. It is a reference to an object of type testsedatastorelevel1. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficCloneProfileRef

Server network or list of servers for cloning traffic. It is a reference to an object of type trafficcloneprofile. Field introduced in 17.1.1. Allowed in basic edition, essentials edition, enterprise edition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficEnabled

Knob to enable the virtual service traffic on its assigned service engines. This setting is effective only when the enabled flag is set to true. Field introduced in 17.2.8.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Specify if this is a normal virtual service, or if it is the parent or child of an sni-enabled virtual hosted virtual service. Enum options - VS_TYPE_NORMAL, VS_TYPE_VH_PARENT, VS_TYPE_VH_CHILD. Allowed in basic(allowed values- vs_type_normal,vs_type_vh_parent) edition, essentials(allowed values- vs_type_normal) edition, enterprise edition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseBridgeIpAsVip

Use bridge ip as vip on each host in mesos deployments. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseVipAsSnat

Use the virtual ip as the snat ip for health monitoring and sending traffic to the backend servers instead of the service engine interface ip. The caveat of enabling this option is that the virtualservice cannot be configued in an active-active ha mode. Dns based multi vip solution has to be used for ha & non-disruptive upgrade purposes. Field introduced in 17.1.9,17.2.3. Allowed in essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VhDomainName

The exact name requested from the client's sni-enabled tls hello domain name field. If this is a match, the parent vs will forward the connection to this child vs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VhParentVsUuid

Specifies the virtual service acting as virtual hosting (sni) parent.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VhType

Specify if the virtual hosting vs is of type sni or enhanced. Enum options - VS_TYPE_VH_SNI, VS_TYPE_VH_ENHANCED. Field introduced in 20.1.3. Allowed in basic(allowed values- vs_type_vh_enhanced) edition, enterprise edition. Special default for basic edition is vs_type_vh_enhanced, enterprise is vs_type_vh_sni.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrfContextRef

Virtual routing context that the virtual service is bound to. This is used to provide the isolation of the set of networks the application is attached to. It is a reference to an object of type vrfcontext.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsvipCloudConfigCksum

Checksum of cloud configuration for vsvip. Internally set by cloud connector. Field introduced in 17.2.9, 18.1.2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsvipRef

Mostly used during the creation of shared vs, this field refers to entities that can be shared across virtual services. It is a reference to an object of type vsvip. Field introduced in 17.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafPolicyRef

Waf policy for the virtual service. It is a reference to an object of type wafpolicy. Field introduced in 17.2.1. Allowed in basic edition, essentials edition, enterprise edition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

The quality of service weight to assign to traffic transmitted from this virtual service. A higher weight will prioritize traffic versus other virtual services sharing the same service engines. Allowed values are 1-128. Allowed in basic(allowed values- 1) edition, essentials(allowed values- 1) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnalyticsPolicy

_Required_: No

_Type_: List of <a href="analyticspolicydefinition.md">AnalyticsPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAuth

_Required_: No

_Type_: List of <a href="clientauthdefinition.md">ClientAuthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionsRateLimit

_Required_: No

_Type_: List of <a href="connectionsratelimitdefinition.md">ConnectionsRateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentRewrite

_Required_: No

_Type_: List of <a href="contentrewritedefinition.md">ContentRewriteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsInfo

_Required_: No

_Type_: List of <a href="dnsinfodefinition.md">DnsInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsPolicies

_Required_: No

_Type_: List of <a href="dnspoliciesdefinition.md">DnsPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpPolicies

_Required_: No

_Type_: List of <a href="httppoliciesdefinition.md">HttpPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JwtConfig

_Required_: No

_Type_: List of <a href="jwtconfigdefinition.md">JwtConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L4Policies

_Required_: No

_Type_: List of <a href="l4policiesdefinition.md">L4PoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerformanceLimits

_Required_: No

_Type_: List of <a href="performancelimitsdefinition.md">PerformanceLimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestsRateLimit

_Required_: No

_Type_: List of <a href="requestsratelimitdefinition.md">RequestsRateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamlSpConfig

_Required_: No

_Type_: List of <a href="samlspconfigdefinition.md">SamlSpConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePoolSelect

_Required_: No

_Type_: List of <a href="servicepoolselectdefinition.md">ServicePoolSelectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

_Required_: No

_Type_: List of <a href="servicesdefinition.md">ServicesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SidebandProfile

_Required_: No

_Type_: List of <a href="sidebandprofiledefinition.md">SidebandProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnatIp

_Required_: No

_Type_: List of <a href="snatipdefinition.md">SnatIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslProfileSelectors

_Required_: No

_Type_: List of <a href="sslprofileselectorsdefinition.md">SslProfileSelectorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticDnsRecords

_Required_: No

_Type_: List of <a href="staticdnsrecordsdefinition.md">StaticDnsRecordsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopologyPolicies

_Required_: No

_Type_: List of <a href="topologypoliciesdefinition.md">TopologyPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VhMatches

_Required_: No

_Type_: List of <a href="vhmatchesdefinition.md">VhMatchesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vip

_Required_: No

_Type_: List of <a href="vipdefinition.md">VipDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsDatascripts

_Required_: No

_Type_: List of <a href="vsdatascriptsdefinition.md">VsDatascriptsDefinition</a>

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

