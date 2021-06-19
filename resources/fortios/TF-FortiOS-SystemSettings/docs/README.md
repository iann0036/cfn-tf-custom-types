# TF::FortiOS::SystemSettings

Configure VDOM settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemSettings",
    "Properties" : {
        "<a href="#allowlinkdownpath" title="AllowLinkdownPath">AllowLinkdownPath</a>" : <i>String</i>,
        "<a href="#allowsubnetoverlap" title="AllowSubnetOverlap">AllowSubnetOverlap</a>" : <i>String</i>,
        "<a href="#asymroute" title="Asymroute">Asymroute</a>" : <i>String</i>,
        "<a href="#asymroute6" title="Asymroute6">Asymroute6</a>" : <i>String</i>,
        "<a href="#asymroute6icmp" title="Asymroute6Icmp">Asymroute6Icmp</a>" : <i>String</i>,
        "<a href="#asymrouteicmp" title="AsymrouteIcmp">AsymrouteIcmp</a>" : <i>String</i>,
        "<a href="#auxiliarysession" title="AuxiliarySession">AuxiliarySession</a>" : <i>String</i>,
        "<a href="#bfd" title="Bfd">Bfd</a>" : <i>String</i>,
        "<a href="#bfddesiredmintx" title="BfdDesiredMinTx">BfdDesiredMinTx</a>" : <i>Double</i>,
        "<a href="#bfddetectmult" title="BfdDetectMult">BfdDetectMult</a>" : <i>Double</i>,
        "<a href="#bfddontenforcesrcport" title="BfdDontEnforceSrcPort">BfdDontEnforceSrcPort</a>" : <i>String</i>,
        "<a href="#bfdrequiredminrx" title="BfdRequiredMinRx">BfdRequiredMinRx</a>" : <i>Double</i>,
        "<a href="#blocklandattack" title="BlockLandAttack">BlockLandAttack</a>" : <i>String</i>,
        "<a href="#centralnat" title="CentralNat">CentralNat</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#compliancecheck" title="ComplianceCheck">ComplianceCheck</a>" : <i>String</i>,
        "<a href="#consolidatedfirewallmode" title="ConsolidatedFirewallMode">ConsolidatedFirewallMode</a>" : <i>String</i>,
        "<a href="#defaultvoipalgmode" title="DefaultVoipAlgMode">DefaultVoipAlgMode</a>" : <i>String</i>,
        "<a href="#denytcpwithicmp" title="DenyTcpWithIcmp">DenyTcpWithIcmp</a>" : <i>String</i>,
        "<a href="#device" title="Device">Device</a>" : <i>String</i>,
        "<a href="#dhcp6serverip" title="Dhcp6ServerIp">Dhcp6ServerIp</a>" : <i>String</i>,
        "<a href="#dhcpproxy" title="DhcpProxy">DhcpProxy</a>" : <i>String</i>,
        "<a href="#dhcpproxyinterface" title="DhcpProxyInterface">DhcpProxyInterface</a>" : <i>String</i>,
        "<a href="#dhcpproxyinterfaceselectmethod" title="DhcpProxyInterfaceSelectMethod">DhcpProxyInterfaceSelectMethod</a>" : <i>String</i>,
        "<a href="#dhcpserverip" title="DhcpServerIp">DhcpServerIp</a>" : <i>String</i>,
        "<a href="#discovereddevicetimeout" title="DiscoveredDeviceTimeout">DiscoveredDeviceTimeout</a>" : <i>Double</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#ecmpmaxpaths" title="EcmpMaxPaths">EcmpMaxPaths</a>" : <i>Double</i>,
        "<a href="#emailportalcheckdns" title="EmailPortalCheckDns">EmailPortalCheckDns</a>" : <i>String</i>,
        "<a href="#firewallsessiondirty" title="FirewallSessionDirty">FirewallSessionDirty</a>" : <i>String</i>,
        "<a href="#fwsessionhairpin" title="FwSessionHairpin">FwSessionHairpin</a>" : <i>String</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
        "<a href="#gateway6" title="Gateway6">Gateway6</a>" : <i>String</i>,
        "<a href="#guiadvancedpolicy" title="GuiAdvancedPolicy">GuiAdvancedPolicy</a>" : <i>String</i>,
        "<a href="#guiallowunnamedpolicy" title="GuiAllowUnnamedPolicy">GuiAllowUnnamedPolicy</a>" : <i>String</i>,
        "<a href="#guiantivirus" title="GuiAntivirus">GuiAntivirus</a>" : <i>String</i>,
        "<a href="#guiapprofile" title="GuiApProfile">GuiApProfile</a>" : <i>String</i>,
        "<a href="#guiapplicationcontrol" title="GuiApplicationControl">GuiApplicationControl</a>" : <i>String</i>,
        "<a href="#guidhcpadvanced" title="GuiDhcpAdvanced">GuiDhcpAdvanced</a>" : <i>String</i>,
        "<a href="#guidlp" title="GuiDlp">GuiDlp</a>" : <i>String</i>,
        "<a href="#guidnsdatabase" title="GuiDnsDatabase">GuiDnsDatabase</a>" : <i>String</i>,
        "<a href="#guidnsfilter" title="GuiDnsfilter">GuiDnsfilter</a>" : <i>String</i>,
        "<a href="#guidomainipreputation" title="GuiDomainIpReputation">GuiDomainIpReputation</a>" : <i>String</i>,
        "<a href="#guidospolicy" title="GuiDosPolicy">GuiDosPolicy</a>" : <i>String</i>,
        "<a href="#guidynamicprofiledisplay" title="GuiDynamicProfileDisplay">GuiDynamicProfileDisplay</a>" : <i>String</i>,
        "<a href="#guidynamicrouting" title="GuiDynamicRouting">GuiDynamicRouting</a>" : <i>String</i>,
        "<a href="#guiemailcollection" title="GuiEmailCollection">GuiEmailCollection</a>" : <i>String</i>,
        "<a href="#guiendpointcontrol" title="GuiEndpointControl">GuiEndpointControl</a>" : <i>String</i>,
        "<a href="#guiendpointcontroladvanced" title="GuiEndpointControlAdvanced">GuiEndpointControlAdvanced</a>" : <i>String</i>,
        "<a href="#guiexplicitproxy" title="GuiExplicitProxy">GuiExplicitProxy</a>" : <i>String</i>,
        "<a href="#guifilefilter" title="GuiFileFilter">GuiFileFilter</a>" : <i>String</i>,
        "<a href="#guifortiapsplittunneling" title="GuiFortiapSplitTunneling">GuiFortiapSplitTunneling</a>" : <i>String</i>,
        "<a href="#guifortiextendercontroller" title="GuiFortiextenderController">GuiFortiextenderController</a>" : <i>String</i>,
        "<a href="#guiicap" title="GuiIcap">GuiIcap</a>" : <i>String</i>,
        "<a href="#guiimplicitpolicy" title="GuiImplicitPolicy">GuiImplicitPolicy</a>" : <i>String</i>,
        "<a href="#guiips" title="GuiIps">GuiIps</a>" : <i>String</i>,
        "<a href="#guiloadbalance" title="GuiLoadBalance">GuiLoadBalance</a>" : <i>String</i>,
        "<a href="#guilocalinpolicy" title="GuiLocalInPolicy">GuiLocalInPolicy</a>" : <i>String</i>,
        "<a href="#guilocalreports" title="GuiLocalReports">GuiLocalReports</a>" : <i>String</i>,
        "<a href="#guimulticastpolicy" title="GuiMulticastPolicy">GuiMulticastPolicy</a>" : <i>String</i>,
        "<a href="#guimultipleinterfacepolicy" title="GuiMultipleInterfacePolicy">GuiMultipleInterfacePolicy</a>" : <i>String</i>,
        "<a href="#guimultipleutmprofiles" title="GuiMultipleUtmProfiles">GuiMultipleUtmProfiles</a>" : <i>String</i>,
        "<a href="#guinat4664" title="GuiNat4664">GuiNat4664</a>" : <i>String</i>,
        "<a href="#guiobjectcolors" title="GuiObjectColors">GuiObjectColors</a>" : <i>String</i>,
        "<a href="#guiperpolicydisclaimer" title="GuiPerPolicyDisclaimer">GuiPerPolicyDisclaimer</a>" : <i>String</i>,
        "<a href="#guipolicybasedipsec" title="GuiPolicyBasedIpsec">GuiPolicyBasedIpsec</a>" : <i>String</i>,
        "<a href="#guipolicydisclaimer" title="GuiPolicyDisclaimer">GuiPolicyDisclaimer</a>" : <i>String</i>,
        "<a href="#guipolicylearning" title="GuiPolicyLearning">GuiPolicyLearning</a>" : <i>String</i>,
        "<a href="#guireplacementmessagegroups" title="GuiReplacementMessageGroups">GuiReplacementMessageGroups</a>" : <i>String</i>,
        "<a href="#guisecurityprofilegroup" title="GuiSecurityProfileGroup">GuiSecurityProfileGroup</a>" : <i>String</i>,
        "<a href="#guispamfilter" title="GuiSpamfilter">GuiSpamfilter</a>" : <i>String</i>,
        "<a href="#guisslvpnpersonalbookmarks" title="GuiSslvpnPersonalBookmarks">GuiSslvpnPersonalBookmarks</a>" : <i>String</i>,
        "<a href="#guisslvpnrealms" title="GuiSslvpnRealms">GuiSslvpnRealms</a>" : <i>String</i>,
        "<a href="#guiswitchcontroller" title="GuiSwitchController">GuiSwitchController</a>" : <i>String</i>,
        "<a href="#guithreatweight" title="GuiThreatWeight">GuiThreatWeight</a>" : <i>String</i>,
        "<a href="#guitrafficshaping" title="GuiTrafficShaping">GuiTrafficShaping</a>" : <i>String</i>,
        "<a href="#guivoipprofile" title="GuiVoipProfile">GuiVoipProfile</a>" : <i>String</i>,
        "<a href="#guivpn" title="GuiVpn">GuiVpn</a>" : <i>String</i>,
        "<a href="#guiwafprofile" title="GuiWafProfile">GuiWafProfile</a>" : <i>String</i>,
        "<a href="#guiwanloadbalancing" title="GuiWanLoadBalancing">GuiWanLoadBalancing</a>" : <i>String</i>,
        "<a href="#guiwanoptcache" title="GuiWanoptCache">GuiWanoptCache</a>" : <i>String</i>,
        "<a href="#guiwebfilter" title="GuiWebfilter">GuiWebfilter</a>" : <i>String</i>,
        "<a href="#guiwebfilteradvanced" title="GuiWebfilterAdvanced">GuiWebfilterAdvanced</a>" : <i>String</i>,
        "<a href="#guiwirelesscontroller" title="GuiWirelessController">GuiWirelessController</a>" : <i>String</i>,
        "<a href="#httpexternaldest" title="HttpExternalDest">HttpExternalDest</a>" : <i>String</i>,
        "<a href="#ikednformat" title="IkeDnFormat">IkeDnFormat</a>" : <i>String</i>,
        "<a href="#ikenattport" title="IkeNattPort">IkeNattPort</a>" : <i>Double</i>,
        "<a href="#ikeport" title="IkePort">IkePort</a>" : <i>Double</i>,
        "<a href="#ikequickcrashdetect" title="IkeQuickCrashDetect">IkeQuickCrashDetect</a>" : <i>String</i>,
        "<a href="#ikesessionresume" title="IkeSessionResume">IkeSessionResume</a>" : <i>String</i>,
        "<a href="#implicitallowdns" title="ImplicitAllowDns">ImplicitAllowDns</a>" : <i>String</i>,
        "<a href="#inspectionmode" title="InspectionMode">InspectionMode</a>" : <i>String</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#ip6" title="Ip6">Ip6</a>" : <i>String</i>,
        "<a href="#linkdownaccess" title="LinkDownAccess">LinkDownAccess</a>" : <i>String</i>,
        "<a href="#lldpreception" title="LldpReception">LldpReception</a>" : <i>String</i>,
        "<a href="#lldptransmission" title="LldpTransmission">LldpTransmission</a>" : <i>String</i>,
        "<a href="#macttl" title="MacTtl">MacTtl</a>" : <i>Double</i>,
        "<a href="#manageip" title="Manageip">Manageip</a>" : <i>String</i>,
        "<a href="#manageip6" title="Manageip6">Manageip6</a>" : <i>String</i>,
        "<a href="#multicastforward" title="MulticastForward">MulticastForward</a>" : <i>String</i>,
        "<a href="#multicastskippolicy" title="MulticastSkipPolicy">MulticastSkipPolicy</a>" : <i>String</i>,
        "<a href="#multicastttlnotchange" title="MulticastTtlNotchange">MulticastTtlNotchange</a>" : <i>String</i>,
        "<a href="#ngfwmode" title="NgfwMode">NgfwMode</a>" : <i>String</i>,
        "<a href="#opmode" title="Opmode">Opmode</a>" : <i>String</i>,
        "<a href="#prptraileraction" title="PrpTrailerAction">PrpTrailerAction</a>" : <i>String</i>,
        "<a href="#sccpport" title="SccpPort">SccpPort</a>" : <i>Double</i>,
        "<a href="#sctpsessionwithoutinit" title="SctpSessionWithoutInit">SctpSessionWithoutInit</a>" : <i>String</i>,
        "<a href="#sesdeniedtraffic" title="SesDeniedTraffic">SesDeniedTraffic</a>" : <i>String</i>,
        "<a href="#sipexpectation" title="SipExpectation">SipExpectation</a>" : <i>String</i>,
        "<a href="#siphelper" title="SipHelper">SipHelper</a>" : <i>String</i>,
        "<a href="#sipnattrace" title="SipNatTrace">SipNatTrace</a>" : <i>String</i>,
        "<a href="#sipsslport" title="SipSslPort">SipSslPort</a>" : <i>Double</i>,
        "<a href="#siptcpport" title="SipTcpPort">SipTcpPort</a>" : <i>Double</i>,
        "<a href="#sipudpport" title="SipUdpPort">SipUdpPort</a>" : <i>Double</i>,
        "<a href="#snathairpintraffic" title="SnatHairpinTraffic">SnatHairpinTraffic</a>" : <i>String</i>,
        "<a href="#sslsshprofile" title="SslSshProfile">SslSshProfile</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#strictsrccheck" title="StrictSrcCheck">StrictSrcCheck</a>" : <i>String</i>,
        "<a href="#tcpsessionwithoutsyn" title="TcpSessionWithoutSyn">TcpSessionWithoutSyn</a>" : <i>String</i>,
        "<a href="#utf8spamtagging" title="Utf8SpamTagging">Utf8SpamTagging</a>" : <i>String</i>,
        "<a href="#v4ecmpmode" title="V4EcmpMode">V4EcmpMode</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#vpnstatslog" title="VpnStatsLog">VpnStatsLog</a>" : <i>String</i>,
        "<a href="#vpnstatsperiod" title="VpnStatsPeriod">VpnStatsPeriod</a>" : <i>Double</i>,
        "<a href="#wccpcacheengine" title="WccpCacheEngine">WccpCacheEngine</a>" : <i>String</i>,
        "<a href="#guidefaultpolicycolumns" title="GuiDefaultPolicyColumns">GuiDefaultPolicyColumns</a>" : <i>[ <a href="guidefaultpolicycolumnsdefinition.md">GuiDefaultPolicyColumnsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemSettings
Properties:
    <a href="#allowlinkdownpath" title="AllowLinkdownPath">AllowLinkdownPath</a>: <i>String</i>
    <a href="#allowsubnetoverlap" title="AllowSubnetOverlap">AllowSubnetOverlap</a>: <i>String</i>
    <a href="#asymroute" title="Asymroute">Asymroute</a>: <i>String</i>
    <a href="#asymroute6" title="Asymroute6">Asymroute6</a>: <i>String</i>
    <a href="#asymroute6icmp" title="Asymroute6Icmp">Asymroute6Icmp</a>: <i>String</i>
    <a href="#asymrouteicmp" title="AsymrouteIcmp">AsymrouteIcmp</a>: <i>String</i>
    <a href="#auxiliarysession" title="AuxiliarySession">AuxiliarySession</a>: <i>String</i>
    <a href="#bfd" title="Bfd">Bfd</a>: <i>String</i>
    <a href="#bfddesiredmintx" title="BfdDesiredMinTx">BfdDesiredMinTx</a>: <i>Double</i>
    <a href="#bfddetectmult" title="BfdDetectMult">BfdDetectMult</a>: <i>Double</i>
    <a href="#bfddontenforcesrcport" title="BfdDontEnforceSrcPort">BfdDontEnforceSrcPort</a>: <i>String</i>
    <a href="#bfdrequiredminrx" title="BfdRequiredMinRx">BfdRequiredMinRx</a>: <i>Double</i>
    <a href="#blocklandattack" title="BlockLandAttack">BlockLandAttack</a>: <i>String</i>
    <a href="#centralnat" title="CentralNat">CentralNat</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#compliancecheck" title="ComplianceCheck">ComplianceCheck</a>: <i>String</i>
    <a href="#consolidatedfirewallmode" title="ConsolidatedFirewallMode">ConsolidatedFirewallMode</a>: <i>String</i>
    <a href="#defaultvoipalgmode" title="DefaultVoipAlgMode">DefaultVoipAlgMode</a>: <i>String</i>
    <a href="#denytcpwithicmp" title="DenyTcpWithIcmp">DenyTcpWithIcmp</a>: <i>String</i>
    <a href="#device" title="Device">Device</a>: <i>String</i>
    <a href="#dhcp6serverip" title="Dhcp6ServerIp">Dhcp6ServerIp</a>: <i>String</i>
    <a href="#dhcpproxy" title="DhcpProxy">DhcpProxy</a>: <i>String</i>
    <a href="#dhcpproxyinterface" title="DhcpProxyInterface">DhcpProxyInterface</a>: <i>String</i>
    <a href="#dhcpproxyinterfaceselectmethod" title="DhcpProxyInterfaceSelectMethod">DhcpProxyInterfaceSelectMethod</a>: <i>String</i>
    <a href="#dhcpserverip" title="DhcpServerIp">DhcpServerIp</a>: <i>String</i>
    <a href="#discovereddevicetimeout" title="DiscoveredDeviceTimeout">DiscoveredDeviceTimeout</a>: <i>Double</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#ecmpmaxpaths" title="EcmpMaxPaths">EcmpMaxPaths</a>: <i>Double</i>
    <a href="#emailportalcheckdns" title="EmailPortalCheckDns">EmailPortalCheckDns</a>: <i>String</i>
    <a href="#firewallsessiondirty" title="FirewallSessionDirty">FirewallSessionDirty</a>: <i>String</i>
    <a href="#fwsessionhairpin" title="FwSessionHairpin">FwSessionHairpin</a>: <i>String</i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
    <a href="#gateway6" title="Gateway6">Gateway6</a>: <i>String</i>
    <a href="#guiadvancedpolicy" title="GuiAdvancedPolicy">GuiAdvancedPolicy</a>: <i>String</i>
    <a href="#guiallowunnamedpolicy" title="GuiAllowUnnamedPolicy">GuiAllowUnnamedPolicy</a>: <i>String</i>
    <a href="#guiantivirus" title="GuiAntivirus">GuiAntivirus</a>: <i>String</i>
    <a href="#guiapprofile" title="GuiApProfile">GuiApProfile</a>: <i>String</i>
    <a href="#guiapplicationcontrol" title="GuiApplicationControl">GuiApplicationControl</a>: <i>String</i>
    <a href="#guidhcpadvanced" title="GuiDhcpAdvanced">GuiDhcpAdvanced</a>: <i>String</i>
    <a href="#guidlp" title="GuiDlp">GuiDlp</a>: <i>String</i>
    <a href="#guidnsdatabase" title="GuiDnsDatabase">GuiDnsDatabase</a>: <i>String</i>
    <a href="#guidnsfilter" title="GuiDnsfilter">GuiDnsfilter</a>: <i>String</i>
    <a href="#guidomainipreputation" title="GuiDomainIpReputation">GuiDomainIpReputation</a>: <i>String</i>
    <a href="#guidospolicy" title="GuiDosPolicy">GuiDosPolicy</a>: <i>String</i>
    <a href="#guidynamicprofiledisplay" title="GuiDynamicProfileDisplay">GuiDynamicProfileDisplay</a>: <i>String</i>
    <a href="#guidynamicrouting" title="GuiDynamicRouting">GuiDynamicRouting</a>: <i>String</i>
    <a href="#guiemailcollection" title="GuiEmailCollection">GuiEmailCollection</a>: <i>String</i>
    <a href="#guiendpointcontrol" title="GuiEndpointControl">GuiEndpointControl</a>: <i>String</i>
    <a href="#guiendpointcontroladvanced" title="GuiEndpointControlAdvanced">GuiEndpointControlAdvanced</a>: <i>String</i>
    <a href="#guiexplicitproxy" title="GuiExplicitProxy">GuiExplicitProxy</a>: <i>String</i>
    <a href="#guifilefilter" title="GuiFileFilter">GuiFileFilter</a>: <i>String</i>
    <a href="#guifortiapsplittunneling" title="GuiFortiapSplitTunneling">GuiFortiapSplitTunneling</a>: <i>String</i>
    <a href="#guifortiextendercontroller" title="GuiFortiextenderController">GuiFortiextenderController</a>: <i>String</i>
    <a href="#guiicap" title="GuiIcap">GuiIcap</a>: <i>String</i>
    <a href="#guiimplicitpolicy" title="GuiImplicitPolicy">GuiImplicitPolicy</a>: <i>String</i>
    <a href="#guiips" title="GuiIps">GuiIps</a>: <i>String</i>
    <a href="#guiloadbalance" title="GuiLoadBalance">GuiLoadBalance</a>: <i>String</i>
    <a href="#guilocalinpolicy" title="GuiLocalInPolicy">GuiLocalInPolicy</a>: <i>String</i>
    <a href="#guilocalreports" title="GuiLocalReports">GuiLocalReports</a>: <i>String</i>
    <a href="#guimulticastpolicy" title="GuiMulticastPolicy">GuiMulticastPolicy</a>: <i>String</i>
    <a href="#guimultipleinterfacepolicy" title="GuiMultipleInterfacePolicy">GuiMultipleInterfacePolicy</a>: <i>String</i>
    <a href="#guimultipleutmprofiles" title="GuiMultipleUtmProfiles">GuiMultipleUtmProfiles</a>: <i>String</i>
    <a href="#guinat4664" title="GuiNat4664">GuiNat4664</a>: <i>String</i>
    <a href="#guiobjectcolors" title="GuiObjectColors">GuiObjectColors</a>: <i>String</i>
    <a href="#guiperpolicydisclaimer" title="GuiPerPolicyDisclaimer">GuiPerPolicyDisclaimer</a>: <i>String</i>
    <a href="#guipolicybasedipsec" title="GuiPolicyBasedIpsec">GuiPolicyBasedIpsec</a>: <i>String</i>
    <a href="#guipolicydisclaimer" title="GuiPolicyDisclaimer">GuiPolicyDisclaimer</a>: <i>String</i>
    <a href="#guipolicylearning" title="GuiPolicyLearning">GuiPolicyLearning</a>: <i>String</i>
    <a href="#guireplacementmessagegroups" title="GuiReplacementMessageGroups">GuiReplacementMessageGroups</a>: <i>String</i>
    <a href="#guisecurityprofilegroup" title="GuiSecurityProfileGroup">GuiSecurityProfileGroup</a>: <i>String</i>
    <a href="#guispamfilter" title="GuiSpamfilter">GuiSpamfilter</a>: <i>String</i>
    <a href="#guisslvpnpersonalbookmarks" title="GuiSslvpnPersonalBookmarks">GuiSslvpnPersonalBookmarks</a>: <i>String</i>
    <a href="#guisslvpnrealms" title="GuiSslvpnRealms">GuiSslvpnRealms</a>: <i>String</i>
    <a href="#guiswitchcontroller" title="GuiSwitchController">GuiSwitchController</a>: <i>String</i>
    <a href="#guithreatweight" title="GuiThreatWeight">GuiThreatWeight</a>: <i>String</i>
    <a href="#guitrafficshaping" title="GuiTrafficShaping">GuiTrafficShaping</a>: <i>String</i>
    <a href="#guivoipprofile" title="GuiVoipProfile">GuiVoipProfile</a>: <i>String</i>
    <a href="#guivpn" title="GuiVpn">GuiVpn</a>: <i>String</i>
    <a href="#guiwafprofile" title="GuiWafProfile">GuiWafProfile</a>: <i>String</i>
    <a href="#guiwanloadbalancing" title="GuiWanLoadBalancing">GuiWanLoadBalancing</a>: <i>String</i>
    <a href="#guiwanoptcache" title="GuiWanoptCache">GuiWanoptCache</a>: <i>String</i>
    <a href="#guiwebfilter" title="GuiWebfilter">GuiWebfilter</a>: <i>String</i>
    <a href="#guiwebfilteradvanced" title="GuiWebfilterAdvanced">GuiWebfilterAdvanced</a>: <i>String</i>
    <a href="#guiwirelesscontroller" title="GuiWirelessController">GuiWirelessController</a>: <i>String</i>
    <a href="#httpexternaldest" title="HttpExternalDest">HttpExternalDest</a>: <i>String</i>
    <a href="#ikednformat" title="IkeDnFormat">IkeDnFormat</a>: <i>String</i>
    <a href="#ikenattport" title="IkeNattPort">IkeNattPort</a>: <i>Double</i>
    <a href="#ikeport" title="IkePort">IkePort</a>: <i>Double</i>
    <a href="#ikequickcrashdetect" title="IkeQuickCrashDetect">IkeQuickCrashDetect</a>: <i>String</i>
    <a href="#ikesessionresume" title="IkeSessionResume">IkeSessionResume</a>: <i>String</i>
    <a href="#implicitallowdns" title="ImplicitAllowDns">ImplicitAllowDns</a>: <i>String</i>
    <a href="#inspectionmode" title="InspectionMode">InspectionMode</a>: <i>String</i>
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#ip6" title="Ip6">Ip6</a>: <i>String</i>
    <a href="#linkdownaccess" title="LinkDownAccess">LinkDownAccess</a>: <i>String</i>
    <a href="#lldpreception" title="LldpReception">LldpReception</a>: <i>String</i>
    <a href="#lldptransmission" title="LldpTransmission">LldpTransmission</a>: <i>String</i>
    <a href="#macttl" title="MacTtl">MacTtl</a>: <i>Double</i>
    <a href="#manageip" title="Manageip">Manageip</a>: <i>String</i>
    <a href="#manageip6" title="Manageip6">Manageip6</a>: <i>String</i>
    <a href="#multicastforward" title="MulticastForward">MulticastForward</a>: <i>String</i>
    <a href="#multicastskippolicy" title="MulticastSkipPolicy">MulticastSkipPolicy</a>: <i>String</i>
    <a href="#multicastttlnotchange" title="MulticastTtlNotchange">MulticastTtlNotchange</a>: <i>String</i>
    <a href="#ngfwmode" title="NgfwMode">NgfwMode</a>: <i>String</i>
    <a href="#opmode" title="Opmode">Opmode</a>: <i>String</i>
    <a href="#prptraileraction" title="PrpTrailerAction">PrpTrailerAction</a>: <i>String</i>
    <a href="#sccpport" title="SccpPort">SccpPort</a>: <i>Double</i>
    <a href="#sctpsessionwithoutinit" title="SctpSessionWithoutInit">SctpSessionWithoutInit</a>: <i>String</i>
    <a href="#sesdeniedtraffic" title="SesDeniedTraffic">SesDeniedTraffic</a>: <i>String</i>
    <a href="#sipexpectation" title="SipExpectation">SipExpectation</a>: <i>String</i>
    <a href="#siphelper" title="SipHelper">SipHelper</a>: <i>String</i>
    <a href="#sipnattrace" title="SipNatTrace">SipNatTrace</a>: <i>String</i>
    <a href="#sipsslport" title="SipSslPort">SipSslPort</a>: <i>Double</i>
    <a href="#siptcpport" title="SipTcpPort">SipTcpPort</a>: <i>Double</i>
    <a href="#sipudpport" title="SipUdpPort">SipUdpPort</a>: <i>Double</i>
    <a href="#snathairpintraffic" title="SnatHairpinTraffic">SnatHairpinTraffic</a>: <i>String</i>
    <a href="#sslsshprofile" title="SslSshProfile">SslSshProfile</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#strictsrccheck" title="StrictSrcCheck">StrictSrcCheck</a>: <i>String</i>
    <a href="#tcpsessionwithoutsyn" title="TcpSessionWithoutSyn">TcpSessionWithoutSyn</a>: <i>String</i>
    <a href="#utf8spamtagging" title="Utf8SpamTagging">Utf8SpamTagging</a>: <i>String</i>
    <a href="#v4ecmpmode" title="V4EcmpMode">V4EcmpMode</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#vpnstatslog" title="VpnStatsLog">VpnStatsLog</a>: <i>String</i>
    <a href="#vpnstatsperiod" title="VpnStatsPeriod">VpnStatsPeriod</a>: <i>Double</i>
    <a href="#wccpcacheengine" title="WccpCacheEngine">WccpCacheEngine</a>: <i>String</i>
    <a href="#guidefaultpolicycolumns" title="GuiDefaultPolicyColumns">GuiDefaultPolicyColumns</a>: <i>
      - <a href="guidefaultpolicycolumnsdefinition.md">GuiDefaultPolicyColumnsDefinition</a></i>
</pre>

## Properties

#### AllowLinkdownPath

Enable/disable link down path. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowSubnetOverlap

Enable/disable allowing interface subnets to use overlapping IP addresses. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Asymroute

Enable/disable IPv4 asymmetric routing. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Asymroute6

Enable/disable asymmetric IPv6 routing. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Asymroute6Icmp

Enable/disable asymmetric ICMPv6 routing. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsymrouteIcmp

Enable/disable ICMP asymmetric routing. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuxiliarySession

Enable/disable auxiliary session. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bfd

Enable/disable Bi-directional Forwarding Detection (BFD) on all interfaces. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BfdDesiredMinTx

BFD desired minimal transmit interval (1 - 100000 ms, default = 50).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BfdDetectMult

BFD detection multiplier (1 - 50, default = 3).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BfdDontEnforceSrcPort

Enable to not enforce verifying the source port of BFD Packets. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BfdRequiredMinRx

BFD required minimal receive interval (1 - 100000 ms, default = 50).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockLandAttack

Enable/disable blocking of land attacks. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CentralNat

Enable/disable central NAT. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

VDOM comments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComplianceCheck

Enable/disable PCI DSS compliance checking. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsolidatedFirewallMode

Consolidated firewall mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultVoipAlgMode

Configure how the FortiGate handles VoIP traffic when a policy that accepts the traffic doesn't include a VoIP profile. Valid values: `proxy-based`, `kernel-helper-based`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DenyTcpWithIcmp

Enable/disable denying TCP by sending an ICMP communication prohibited packet. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Device

Interface to use for management access for NAT mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhcp6ServerIp

DHCPv6 server IPv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpProxy

Enable/disable the DHCP Proxy. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpProxyInterface

Specify outgoing interface to reach server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpProxyInterfaceSelectMethod

Specify how to select outgoing interface to reach server. Valid values: `auto`, `sdwan`, `specify`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpServerIp

DHCP Server IPv4 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiscoveredDeviceTimeout

Timeout for discovered devices (1 - 365 days, default = 28).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcmpMaxPaths

Maximum number of Equal Cost Multi-Path (ECMP) next-hops. Set to 1 to disable ECMP routing (1 - 100, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailPortalCheckDns

Enable/disable using DNS to validate email addresses collected by a captive portal. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallSessionDirty

Select how to manage sessions affected by firewall policy configuration changes. Valid values: `check-all`, `check-new`, `check-policy-option`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FwSessionHairpin

Enable/disable checking for a matching policy each time hairpin traffic goes through the FortiGate. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

Transparent mode IPv4 default gateway IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway6

Transparent mode IPv4 default gateway IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiAdvancedPolicy

Enable/disable advanced policy configuration on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiAllowUnnamedPolicy

Enable/disable the requirement for policy naming on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiAntivirus

Enable/disable AntiVirus on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiApProfile

Enable/disable FortiAP profiles on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiApplicationControl

Enable/disable application control on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiDhcpAdvanced

Enable/disable advanced DHCP options on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiDlp

Enable/disable DLP on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiDnsDatabase

Enable/disable DNS database settings on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiDnsfilter

Enable/disable DNS Filtering on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiDomainIpReputation

Enable/disable Domain and IP Reputation on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiDosPolicy

Enable/disable DoS policies on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiDynamicProfileDisplay

Enable/disable RADIUS Single Sign On (RSSO) on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiDynamicRouting

Enable/disable dynamic routing on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiEmailCollection

Enable/disable email collection on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiEndpointControl

Enable/disable endpoint control on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiEndpointControlAdvanced

Enable/disable advanced endpoint control options on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiExplicitProxy

Enable/disable the explicit proxy on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiFileFilter

Enable/disable File-filter on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiFortiapSplitTunneling

Enable/disable FortiAP split tunneling on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiFortiextenderController

Enable/disable FortiExtender on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiIcap

Enable/disable ICAP on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiImplicitPolicy

Enable/disable implicit firewall policies on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiIps

Enable/disable IPS on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiLoadBalance

Enable/disable server load balancing on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiLocalInPolicy

Enable/disable Local-In policies on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiLocalReports

Enable/disable local reports on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiMulticastPolicy

Enable/disable multicast firewall policies on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiMultipleInterfacePolicy

Enable/disable adding multiple interfaces to a policy on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiMultipleUtmProfiles

Enable/disable multiple UTM profiles on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiNat4664

Enable/disable NAT46 and NAT64 settings on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiObjectColors

Enable/disable object colors on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiPerPolicyDisclaimer

Enable/disable policy disclaimer on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiPolicyBasedIpsec

Enable/disable policy-based IPsec VPN on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiPolicyDisclaimer

Enable/disable policy disclaimer on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiPolicyLearning

Enable/disable firewall policy learning mode on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiReplacementMessageGroups

Enable/disable replacement message groups on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiSecurityProfileGroup

Enable/disable Security Profile Groups on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiSpamfilter

Enable/disable Antispam on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiSslvpnPersonalBookmarks

Enable/disable SSL-VPN personal bookmark management on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiSslvpnRealms

Enable/disable SSL-VPN realms on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiSwitchController

Enable/disable the switch controller on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiThreatWeight

Enable/disable threat weight on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiTrafficShaping

Enable/disable traffic shaping on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiVoipProfile

Enable/disable VoIP profiles on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiVpn

Enable/disable VPN tunnels on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiWafProfile

Enable/disable Web Application Firewall on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiWanLoadBalancing

Enable/disable SD-WAN on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiWanoptCache

Enable/disable WAN Optimization and Web Caching on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiWebfilter

Enable/disable Web filtering on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiWebfilterAdvanced

Enable/disable advanced web filtering on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiWirelessController

Enable/disable the wireless controller on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpExternalDest

Offload HTTP traffic to FortiWeb or FortiCache. Valid values: `fortiweb`, `forticache`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeDnFormat

Configure IKE ASN.1 Distinguished Name format conventions. Valid values: `with-space`, `no-space`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeNattPort

UDP port for IKE/IPsec traffic in NAT-T mode (default 4500).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkePort

UDP port for IKE/IPsec traffic (default 500).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeQuickCrashDetect

Enable/disable IKE quick crash detection (RFC 6290). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeSessionResume

Enable/disable IKEv2 session resumption (RFC 5723). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImplicitAllowDns

Enable/disable implicitly allowing DNS traffic. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InspectionMode

Inspection mode (proxy-based or flow-based). Valid values: `proxy`, `flow`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

IP address and netmask.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6

IPv6 address prefix for NAT mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkDownAccess

Enable/disable link down access traffic. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LldpReception

Enable/disable Link Layer Discovery Protocol (LLDP) reception for this VDOM or apply global settings to this VDOM. Valid values: `enable`, `disable`, `global`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LldpTransmission

Enable/disable Link Layer Discovery Protocol (LLDP) transmission for this VDOM or apply global settings to this VDOM. Valid values: `enable`, `disable`, `global`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacTtl

Duration of MAC addresses in Transparent mode (300 - 8640000 sec, default = 300).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Manageip

Transparent mode IPv4 management IP address and netmask.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Manageip6

Transparent mode IPv6 management IP address and netmask.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MulticastForward

Enable/disable multicast forwarding. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MulticastSkipPolicy

Enable/disable allowing multicast traffic through the FortiGate without a policy check. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MulticastTtlNotchange

Enable/disable preventing the FortiGate from changing the TTL for forwarded multicast packets. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NgfwMode

Next Generation Firewall (NGFW) mode. Valid values: `profile-based`, `policy-based`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Opmode

Firewall operation mode (NAT or Transparent). Valid values: `nat`, `transparent`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrpTrailerAction

Enable/disable action to take on PRP trailer. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SccpPort

TCP port the SCCP proxy monitors for SCCP traffic (0 - 65535, default = 2000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SctpSessionWithoutInit

Enable/disable SCTP session creation without SCTP INIT. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SesDeniedTraffic

Enable/disable including denied session in the session table. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SipExpectation

Enable/disable the SIP kernel session helper to create an expectation for port 5060. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SipHelper

Enable/disable the SIP session helper to process SIP sessions unless SIP sessions are accepted by the SIP application layer gateway (ALG). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SipNatTrace

Enable/disable recording the original SIP source IP address when NAT is used. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SipSslPort

TCP port the SIP proxy monitors for SIP SSL/TLS traffic (0 - 65535, default = 5061).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SipTcpPort

TCP port the SIP proxy monitors for SIP traffic (0 - 65535, default = 5060).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SipUdpPort

UDP port the SIP proxy monitors for SIP traffic (0 - 65535, default = 5060).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnatHairpinTraffic

Enable/disable source NAT (SNAT) for hairpin traffic. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslSshProfile

Profile for SSL/SSH inspection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable this VDOM. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrictSrcCheck

Enable/disable strict source verification. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpSessionWithoutSyn

Enable/disable allowing TCP session without SYN flags. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Utf8SpamTagging

Enable/disable converting antispam tags to UTF-8 for better non-ASCII character support. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### V4EcmpMode

IPv4 Equal-cost multi-path (ECMP) routing and load balancing mode. Valid values: `source-ip-based`, `weight-based`, `usage-based`, `source-dest-ip-based`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnStatsLog

Enable/disable periodic VPN log statistics for one or more types of VPN. Separate names with a space. Valid values: `ipsec`, `pptp`, `l2tp`, `ssl`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnStatsPeriod

Period to send VPN log statistics (0 or 60 - 86400 sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WccpCacheEngine

Enable/disable WCCP cache engine. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiDefaultPolicyColumns

_Required_: No

_Type_: List of <a href="guidefaultpolicycolumnsdefinition.md">GuiDefaultPolicyColumnsDefinition</a>

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

