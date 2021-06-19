# TF::FortiOS::WirelesscontrollerVap

Configure Virtual Access Points (VAPs).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WirelesscontrollerVap",
    "Properties" : {
        "<a href="#accesscontrollist" title="AccessControlList">AccessControlList</a>" : <i>String</i>,
        "<a href="#acctinteriminterval" title="AcctInterimInterval">AcctInterimInterval</a>" : <i>Double</i>,
        "<a href="#additionalakms" title="AdditionalAkms">AdditionalAkms</a>" : <i>String</i>,
        "<a href="#addressgroup" title="AddressGroup">AddressGroup</a>" : <i>String</i>,
        "<a href="#alias" title="Alias">Alias</a>" : <i>String</i>,
        "<a href="#atfweight" title="AtfWeight">AtfWeight</a>" : <i>Double</i>,
        "<a href="#auth" title="Auth">Auth</a>" : <i>String</i>,
        "<a href="#broadcastssid" title="BroadcastSsid">BroadcastSsid</a>" : <i>String</i>,
        "<a href="#broadcastsuppression" title="BroadcastSuppression">BroadcastSuppression</a>" : <i>String</i>,
        "<a href="#bsscolorpartial" title="BssColorPartial">BssColorPartial</a>" : <i>String</i>,
        "<a href="#captiveportalacname" title="CaptivePortalAcName">CaptivePortalAcName</a>" : <i>String</i>,
        "<a href="#captiveportalauthtimeout" title="CaptivePortalAuthTimeout">CaptivePortalAuthTimeout</a>" : <i>Double</i>,
        "<a href="#captiveportalmacauthradiussecret" title="CaptivePortalMacauthRadiusSecret">CaptivePortalMacauthRadiusSecret</a>" : <i>String</i>,
        "<a href="#captiveportalmacauthradiusserver" title="CaptivePortalMacauthRadiusServer">CaptivePortalMacauthRadiusServer</a>" : <i>String</i>,
        "<a href="#captiveportalradiussecret" title="CaptivePortalRadiusSecret">CaptivePortalRadiusSecret</a>" : <i>String</i>,
        "<a href="#captiveportalradiusserver" title="CaptivePortalRadiusServer">CaptivePortalRadiusServer</a>" : <i>String</i>,
        "<a href="#captiveportalsessiontimeoutinterval" title="CaptivePortalSessionTimeoutInterval">CaptivePortalSessionTimeoutInterval</a>" : <i>Double</i>,
        "<a href="#dhcpleasetime" title="DhcpLeaseTime">DhcpLeaseTime</a>" : <i>Double</i>,
        "<a href="#dhcpoption43insertion" title="DhcpOption43Insertion">DhcpOption43Insertion</a>" : <i>String</i>,
        "<a href="#dhcpoption82circuitidinsertion" title="DhcpOption82CircuitIdInsertion">DhcpOption82CircuitIdInsertion</a>" : <i>String</i>,
        "<a href="#dhcpoption82insertion" title="DhcpOption82Insertion">DhcpOption82Insertion</a>" : <i>String</i>,
        "<a href="#dhcpoption82remoteidinsertion" title="DhcpOption82RemoteIdInsertion">DhcpOption82RemoteIdInsertion</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#dynamicvlan" title="DynamicVlan">DynamicVlan</a>" : <i>String</i>,
        "<a href="#eapreauth" title="EapReauth">EapReauth</a>" : <i>String</i>,
        "<a href="#eapreauthintv" title="EapReauthIntv">EapReauthIntv</a>" : <i>Double</i>,
        "<a href="#eapolkeyretries" title="EapolKeyRetries">EapolKeyRetries</a>" : <i>String</i>,
        "<a href="#encrypt" title="Encrypt">Encrypt</a>" : <i>String</i>,
        "<a href="#externalfastroaming" title="ExternalFastRoaming">ExternalFastRoaming</a>" : <i>String</i>,
        "<a href="#externallogout" title="ExternalLogout">ExternalLogout</a>" : <i>String</i>,
        "<a href="#externalweb" title="ExternalWeb">ExternalWeb</a>" : <i>String</i>,
        "<a href="#externalwebformat" title="ExternalWebFormat">ExternalWebFormat</a>" : <i>String</i>,
        "<a href="#fastbsstransition" title="FastBssTransition">FastBssTransition</a>" : <i>String</i>,
        "<a href="#fastroaming" title="FastRoaming">FastRoaming</a>" : <i>String</i>,
        "<a href="#ftmobilitydomain" title="FtMobilityDomain">FtMobilityDomain</a>" : <i>Double</i>,
        "<a href="#ftoverds" title="FtOverDs">FtOverDs</a>" : <i>String</i>,
        "<a href="#ftr0keylifetime" title="FtR0KeyLifetime">FtR0KeyLifetime</a>" : <i>Double</i>,
        "<a href="#gtkrekey" title="GtkRekey">GtkRekey</a>" : <i>String</i>,
        "<a href="#gtkrekeyintv" title="GtkRekeyIntv">GtkRekeyIntv</a>" : <i>Double</i>,
        "<a href="#highefficiency" title="HighEfficiency">HighEfficiency</a>" : <i>String</i>,
        "<a href="#hotspot20profile" title="Hotspot20Profile">Hotspot20Profile</a>" : <i>String</i>,
        "<a href="#igmpsnooping" title="IgmpSnooping">IgmpSnooping</a>" : <i>String</i>,
        "<a href="#intravapprivacy" title="IntraVapPrivacy">IntraVapPrivacy</a>" : <i>String</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#ipv6rules" title="Ipv6Rules">Ipv6Rules</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#keyindex" title="Keyindex">Keyindex</a>" : <i>Double</i>,
        "<a href="#ldpc" title="Ldpc">Ldpc</a>" : <i>String</i>,
        "<a href="#localauthentication" title="LocalAuthentication">LocalAuthentication</a>" : <i>String</i>,
        "<a href="#localbridging" title="LocalBridging">LocalBridging</a>" : <i>String</i>,
        "<a href="#locallan" title="LocalLan">LocalLan</a>" : <i>String</i>,
        "<a href="#localstandalone" title="LocalStandalone">LocalStandalone</a>" : <i>String</i>,
        "<a href="#localstandalonenat" title="LocalStandaloneNat">LocalStandaloneNat</a>" : <i>String</i>,
        "<a href="#macauthbypass" title="MacAuthBypass">MacAuthBypass</a>" : <i>String</i>,
        "<a href="#macfilter" title="MacFilter">MacFilter</a>" : <i>String</i>,
        "<a href="#macfilterpolicyother" title="MacFilterPolicyOther">MacFilterPolicyOther</a>" : <i>String</i>,
        "<a href="#maxclients" title="MaxClients">MaxClients</a>" : <i>Double</i>,
        "<a href="#maxclientsap" title="MaxClientsAp">MaxClientsAp</a>" : <i>Double</i>,
        "<a href="#medisablethresh" title="MeDisableThresh">MeDisableThresh</a>" : <i>Double</i>,
        "<a href="#meshbackhaul" title="MeshBackhaul">MeshBackhaul</a>" : <i>String</i>,
        "<a href="#mpsk" title="Mpsk">Mpsk</a>" : <i>String</i>,
        "<a href="#mpskconcurrentclients" title="MpskConcurrentClients">MpskConcurrentClients</a>" : <i>Double</i>,
        "<a href="#mpskprofile" title="MpskProfile">MpskProfile</a>" : <i>String</i>,
        "<a href="#mumimo" title="MuMimo">MuMimo</a>" : <i>String</i>,
        "<a href="#multicastenhance" title="MulticastEnhance">MulticastEnhance</a>" : <i>String</i>,
        "<a href="#multicastrate" title="MulticastRate">MulticastRate</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#okc" title="Okc">Okc</a>" : <i>String</i>,
        "<a href="#owegroups" title="OweGroups">OweGroups</a>" : <i>String</i>,
        "<a href="#owetransition" title="OweTransition">OweTransition</a>" : <i>String</i>,
        "<a href="#owetransitionssid" title="OweTransitionSsid">OweTransitionSsid</a>" : <i>String</i>,
        "<a href="#passphrase" title="Passphrase">Passphrase</a>" : <i>String</i>,
        "<a href="#pmf" title="Pmf">Pmf</a>" : <i>String</i>,
        "<a href="#pmfassoccomebacktimeout" title="PmfAssocComebackTimeout">PmfAssocComebackTimeout</a>" : <i>Double</i>,
        "<a href="#pmfsaqueryretrytimeout" title="PmfSaQueryRetryTimeout">PmfSaQueryRetryTimeout</a>" : <i>Double</i>,
        "<a href="#portmacauth" title="PortMacauth">PortMacauth</a>" : <i>String</i>,
        "<a href="#portmacauthreauthtimeout" title="PortMacauthReauthTimeout">PortMacauthReauthTimeout</a>" : <i>Double</i>,
        "<a href="#portmacauthtimeout" title="PortMacauthTimeout">PortMacauthTimeout</a>" : <i>Double</i>,
        "<a href="#portalmessageoverridegroup" title="PortalMessageOverrideGroup">PortalMessageOverrideGroup</a>" : <i>String</i>,
        "<a href="#portaltype" title="PortalType">PortalType</a>" : <i>String</i>,
        "<a href="#primarywagprofile" title="PrimaryWagProfile">PrimaryWagProfile</a>" : <i>String</i>,
        "<a href="#proberespsuppression" title="ProbeRespSuppression">ProbeRespSuppression</a>" : <i>String</i>,
        "<a href="#proberespthreshold" title="ProbeRespThreshold">ProbeRespThreshold</a>" : <i>String</i>,
        "<a href="#ptkrekey" title="PtkRekey">PtkRekey</a>" : <i>String</i>,
        "<a href="#ptkrekeyintv" title="PtkRekeyIntv">PtkRekeyIntv</a>" : <i>Double</i>,
        "<a href="#qosprofile" title="QosProfile">QosProfile</a>" : <i>String</i>,
        "<a href="#quarantine" title="Quarantine">Quarantine</a>" : <i>String</i>,
        "<a href="#radio2gthreshold" title="Radio2gThreshold">Radio2gThreshold</a>" : <i>String</i>,
        "<a href="#radio5gthreshold" title="Radio5gThreshold">Radio5gThreshold</a>" : <i>String</i>,
        "<a href="#radiosensitivity" title="RadioSensitivity">RadioSensitivity</a>" : <i>String</i>,
        "<a href="#radiusmacauth" title="RadiusMacAuth">RadiusMacAuth</a>" : <i>String</i>,
        "<a href="#radiusmacauthserver" title="RadiusMacAuthServer">RadiusMacAuthServer</a>" : <i>String</i>,
        "<a href="#radiusserver" title="RadiusServer">RadiusServer</a>" : <i>String</i>,
        "<a href="#rates11a" title="Rates11a">Rates11a</a>" : <i>String</i>,
        "<a href="#rates11acss12" title="Rates11acSs12">Rates11acSs12</a>" : <i>String</i>,
        "<a href="#rates11acss34" title="Rates11acSs34">Rates11acSs34</a>" : <i>String</i>,
        "<a href="#rates11bg" title="Rates11bg">Rates11bg</a>" : <i>String</i>,
        "<a href="#rates11nss12" title="Rates11nSs12">Rates11nSs12</a>" : <i>String</i>,
        "<a href="#rates11nss34" title="Rates11nSs34">Rates11nSs34</a>" : <i>String</i>,
        "<a href="#saegroups" title="SaeGroups">SaeGroups</a>" : <i>String</i>,
        "<a href="#saepassword" title="SaePassword">SaePassword</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
        "<a href="#secondarywagprofile" title="SecondaryWagProfile">SecondaryWagProfile</a>" : <i>String</i>,
        "<a href="#security" title="Security">Security</a>" : <i>String</i>,
        "<a href="#securityexemptlist" title="SecurityExemptList">SecurityExemptList</a>" : <i>String</i>,
        "<a href="#securityobsoleteoption" title="SecurityObsoleteOption">SecurityObsoleteOption</a>" : <i>String</i>,
        "<a href="#securityredirecturl" title="SecurityRedirectUrl">SecurityRedirectUrl</a>" : <i>String</i>,
        "<a href="#splittunneling" title="SplitTunneling">SplitTunneling</a>" : <i>String</i>,
        "<a href="#ssid" title="Ssid">Ssid</a>" : <i>String</i>,
        "<a href="#stickyclientremove" title="StickyClientRemove">StickyClientRemove</a>" : <i>String</i>,
        "<a href="#stickyclientthreshold2g" title="StickyClientThreshold2g">StickyClientThreshold2g</a>" : <i>String</i>,
        "<a href="#stickyclientthreshold5g" title="StickyClientThreshold5g">StickyClientThreshold5g</a>" : <i>String</i>,
        "<a href="#targetwaketime" title="TargetWakeTime">TargetWakeTime</a>" : <i>String</i>,
        "<a href="#tkipcountermeasure" title="TkipCounterMeasure">TkipCounterMeasure</a>" : <i>String</i>,
        "<a href="#tunnelechointerval" title="TunnelEchoInterval">TunnelEchoInterval</a>" : <i>Double</i>,
        "<a href="#tunnelfallbackinterval" title="TunnelFallbackInterval">TunnelFallbackInterval</a>" : <i>Double</i>,
        "<a href="#utmprofile" title="UtmProfile">UtmProfile</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#vlanauto" title="VlanAuto">VlanAuto</a>" : <i>String</i>,
        "<a href="#vlanpooling" title="VlanPooling">VlanPooling</a>" : <i>String</i>,
        "<a href="#vlanid" title="Vlanid">Vlanid</a>" : <i>Double</i>,
        "<a href="#voiceenterprise" title="VoiceEnterprise">VoiceEnterprise</a>" : <i>String</i>,
        "<a href="#macfilterlist" title="MacFilterList">MacFilterList</a>" : <i>[ <a href="macfilterlistdefinition.md">MacFilterListDefinition</a>, ... ]</i>,
        "<a href="#mpskkey" title="MpskKey">MpskKey</a>" : <i>[ <a href="mpskkeydefinition.md">MpskKeyDefinition</a>, ... ]</i>,
        "<a href="#portalmessageoverrides" title="PortalMessageOverrides">PortalMessageOverrides</a>" : <i>[ <a href="portalmessageoverridesdefinition.md">PortalMessageOverridesDefinition</a>, ... ]</i>,
        "<a href="#radiusmacauthusergroups" title="RadiusMacAuthUsergroups">RadiusMacAuthUsergroups</a>" : <i>[ <a href="radiusmacauthusergroupsdefinition.md">RadiusMacAuthUsergroupsDefinition</a>, ... ]</i>,
        "<a href="#selectedusergroups" title="SelectedUsergroups">SelectedUsergroups</a>" : <i>[ <a href="selectedusergroupsdefinition.md">SelectedUsergroupsDefinition</a>, ... ]</i>,
        "<a href="#usergroup" title="Usergroup">Usergroup</a>" : <i>[ <a href="usergroupdefinition.md">UsergroupDefinition</a>, ... ]</i>,
        "<a href="#vlanpool" title="VlanPool">VlanPool</a>" : <i>[ <a href="vlanpooldefinition.md">VlanPoolDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WirelesscontrollerVap
Properties:
    <a href="#accesscontrollist" title="AccessControlList">AccessControlList</a>: <i>String</i>
    <a href="#acctinteriminterval" title="AcctInterimInterval">AcctInterimInterval</a>: <i>Double</i>
    <a href="#additionalakms" title="AdditionalAkms">AdditionalAkms</a>: <i>String</i>
    <a href="#addressgroup" title="AddressGroup">AddressGroup</a>: <i>String</i>
    <a href="#alias" title="Alias">Alias</a>: <i>String</i>
    <a href="#atfweight" title="AtfWeight">AtfWeight</a>: <i>Double</i>
    <a href="#auth" title="Auth">Auth</a>: <i>String</i>
    <a href="#broadcastssid" title="BroadcastSsid">BroadcastSsid</a>: <i>String</i>
    <a href="#broadcastsuppression" title="BroadcastSuppression">BroadcastSuppression</a>: <i>String</i>
    <a href="#bsscolorpartial" title="BssColorPartial">BssColorPartial</a>: <i>String</i>
    <a href="#captiveportalacname" title="CaptivePortalAcName">CaptivePortalAcName</a>: <i>String</i>
    <a href="#captiveportalauthtimeout" title="CaptivePortalAuthTimeout">CaptivePortalAuthTimeout</a>: <i>Double</i>
    <a href="#captiveportalmacauthradiussecret" title="CaptivePortalMacauthRadiusSecret">CaptivePortalMacauthRadiusSecret</a>: <i>String</i>
    <a href="#captiveportalmacauthradiusserver" title="CaptivePortalMacauthRadiusServer">CaptivePortalMacauthRadiusServer</a>: <i>String</i>
    <a href="#captiveportalradiussecret" title="CaptivePortalRadiusSecret">CaptivePortalRadiusSecret</a>: <i>String</i>
    <a href="#captiveportalradiusserver" title="CaptivePortalRadiusServer">CaptivePortalRadiusServer</a>: <i>String</i>
    <a href="#captiveportalsessiontimeoutinterval" title="CaptivePortalSessionTimeoutInterval">CaptivePortalSessionTimeoutInterval</a>: <i>Double</i>
    <a href="#dhcpleasetime" title="DhcpLeaseTime">DhcpLeaseTime</a>: <i>Double</i>
    <a href="#dhcpoption43insertion" title="DhcpOption43Insertion">DhcpOption43Insertion</a>: <i>String</i>
    <a href="#dhcpoption82circuitidinsertion" title="DhcpOption82CircuitIdInsertion">DhcpOption82CircuitIdInsertion</a>: <i>String</i>
    <a href="#dhcpoption82insertion" title="DhcpOption82Insertion">DhcpOption82Insertion</a>: <i>String</i>
    <a href="#dhcpoption82remoteidinsertion" title="DhcpOption82RemoteIdInsertion">DhcpOption82RemoteIdInsertion</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#dynamicvlan" title="DynamicVlan">DynamicVlan</a>: <i>String</i>
    <a href="#eapreauth" title="EapReauth">EapReauth</a>: <i>String</i>
    <a href="#eapreauthintv" title="EapReauthIntv">EapReauthIntv</a>: <i>Double</i>
    <a href="#eapolkeyretries" title="EapolKeyRetries">EapolKeyRetries</a>: <i>String</i>
    <a href="#encrypt" title="Encrypt">Encrypt</a>: <i>String</i>
    <a href="#externalfastroaming" title="ExternalFastRoaming">ExternalFastRoaming</a>: <i>String</i>
    <a href="#externallogout" title="ExternalLogout">ExternalLogout</a>: <i>String</i>
    <a href="#externalweb" title="ExternalWeb">ExternalWeb</a>: <i>String</i>
    <a href="#externalwebformat" title="ExternalWebFormat">ExternalWebFormat</a>: <i>String</i>
    <a href="#fastbsstransition" title="FastBssTransition">FastBssTransition</a>: <i>String</i>
    <a href="#fastroaming" title="FastRoaming">FastRoaming</a>: <i>String</i>
    <a href="#ftmobilitydomain" title="FtMobilityDomain">FtMobilityDomain</a>: <i>Double</i>
    <a href="#ftoverds" title="FtOverDs">FtOverDs</a>: <i>String</i>
    <a href="#ftr0keylifetime" title="FtR0KeyLifetime">FtR0KeyLifetime</a>: <i>Double</i>
    <a href="#gtkrekey" title="GtkRekey">GtkRekey</a>: <i>String</i>
    <a href="#gtkrekeyintv" title="GtkRekeyIntv">GtkRekeyIntv</a>: <i>Double</i>
    <a href="#highefficiency" title="HighEfficiency">HighEfficiency</a>: <i>String</i>
    <a href="#hotspot20profile" title="Hotspot20Profile">Hotspot20Profile</a>: <i>String</i>
    <a href="#igmpsnooping" title="IgmpSnooping">IgmpSnooping</a>: <i>String</i>
    <a href="#intravapprivacy" title="IntraVapPrivacy">IntraVapPrivacy</a>: <i>String</i>
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#ipv6rules" title="Ipv6Rules">Ipv6Rules</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#keyindex" title="Keyindex">Keyindex</a>: <i>Double</i>
    <a href="#ldpc" title="Ldpc">Ldpc</a>: <i>String</i>
    <a href="#localauthentication" title="LocalAuthentication">LocalAuthentication</a>: <i>String</i>
    <a href="#localbridging" title="LocalBridging">LocalBridging</a>: <i>String</i>
    <a href="#locallan" title="LocalLan">LocalLan</a>: <i>String</i>
    <a href="#localstandalone" title="LocalStandalone">LocalStandalone</a>: <i>String</i>
    <a href="#localstandalonenat" title="LocalStandaloneNat">LocalStandaloneNat</a>: <i>String</i>
    <a href="#macauthbypass" title="MacAuthBypass">MacAuthBypass</a>: <i>String</i>
    <a href="#macfilter" title="MacFilter">MacFilter</a>: <i>String</i>
    <a href="#macfilterpolicyother" title="MacFilterPolicyOther">MacFilterPolicyOther</a>: <i>String</i>
    <a href="#maxclients" title="MaxClients">MaxClients</a>: <i>Double</i>
    <a href="#maxclientsap" title="MaxClientsAp">MaxClientsAp</a>: <i>Double</i>
    <a href="#medisablethresh" title="MeDisableThresh">MeDisableThresh</a>: <i>Double</i>
    <a href="#meshbackhaul" title="MeshBackhaul">MeshBackhaul</a>: <i>String</i>
    <a href="#mpsk" title="Mpsk">Mpsk</a>: <i>String</i>
    <a href="#mpskconcurrentclients" title="MpskConcurrentClients">MpskConcurrentClients</a>: <i>Double</i>
    <a href="#mpskprofile" title="MpskProfile">MpskProfile</a>: <i>String</i>
    <a href="#mumimo" title="MuMimo">MuMimo</a>: <i>String</i>
    <a href="#multicastenhance" title="MulticastEnhance">MulticastEnhance</a>: <i>String</i>
    <a href="#multicastrate" title="MulticastRate">MulticastRate</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#okc" title="Okc">Okc</a>: <i>String</i>
    <a href="#owegroups" title="OweGroups">OweGroups</a>: <i>String</i>
    <a href="#owetransition" title="OweTransition">OweTransition</a>: <i>String</i>
    <a href="#owetransitionssid" title="OweTransitionSsid">OweTransitionSsid</a>: <i>String</i>
    <a href="#passphrase" title="Passphrase">Passphrase</a>: <i>String</i>
    <a href="#pmf" title="Pmf">Pmf</a>: <i>String</i>
    <a href="#pmfassoccomebacktimeout" title="PmfAssocComebackTimeout">PmfAssocComebackTimeout</a>: <i>Double</i>
    <a href="#pmfsaqueryretrytimeout" title="PmfSaQueryRetryTimeout">PmfSaQueryRetryTimeout</a>: <i>Double</i>
    <a href="#portmacauth" title="PortMacauth">PortMacauth</a>: <i>String</i>
    <a href="#portmacauthreauthtimeout" title="PortMacauthReauthTimeout">PortMacauthReauthTimeout</a>: <i>Double</i>
    <a href="#portmacauthtimeout" title="PortMacauthTimeout">PortMacauthTimeout</a>: <i>Double</i>
    <a href="#portalmessageoverridegroup" title="PortalMessageOverrideGroup">PortalMessageOverrideGroup</a>: <i>String</i>
    <a href="#portaltype" title="PortalType">PortalType</a>: <i>String</i>
    <a href="#primarywagprofile" title="PrimaryWagProfile">PrimaryWagProfile</a>: <i>String</i>
    <a href="#proberespsuppression" title="ProbeRespSuppression">ProbeRespSuppression</a>: <i>String</i>
    <a href="#proberespthreshold" title="ProbeRespThreshold">ProbeRespThreshold</a>: <i>String</i>
    <a href="#ptkrekey" title="PtkRekey">PtkRekey</a>: <i>String</i>
    <a href="#ptkrekeyintv" title="PtkRekeyIntv">PtkRekeyIntv</a>: <i>Double</i>
    <a href="#qosprofile" title="QosProfile">QosProfile</a>: <i>String</i>
    <a href="#quarantine" title="Quarantine">Quarantine</a>: <i>String</i>
    <a href="#radio2gthreshold" title="Radio2gThreshold">Radio2gThreshold</a>: <i>String</i>
    <a href="#radio5gthreshold" title="Radio5gThreshold">Radio5gThreshold</a>: <i>String</i>
    <a href="#radiosensitivity" title="RadioSensitivity">RadioSensitivity</a>: <i>String</i>
    <a href="#radiusmacauth" title="RadiusMacAuth">RadiusMacAuth</a>: <i>String</i>
    <a href="#radiusmacauthserver" title="RadiusMacAuthServer">RadiusMacAuthServer</a>: <i>String</i>
    <a href="#radiusserver" title="RadiusServer">RadiusServer</a>: <i>String</i>
    <a href="#rates11a" title="Rates11a">Rates11a</a>: <i>String</i>
    <a href="#rates11acss12" title="Rates11acSs12">Rates11acSs12</a>: <i>String</i>
    <a href="#rates11acss34" title="Rates11acSs34">Rates11acSs34</a>: <i>String</i>
    <a href="#rates11bg" title="Rates11bg">Rates11bg</a>: <i>String</i>
    <a href="#rates11nss12" title="Rates11nSs12">Rates11nSs12</a>: <i>String</i>
    <a href="#rates11nss34" title="Rates11nSs34">Rates11nSs34</a>: <i>String</i>
    <a href="#saegroups" title="SaeGroups">SaeGroups</a>: <i>String</i>
    <a href="#saepassword" title="SaePassword">SaePassword</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
    <a href="#secondarywagprofile" title="SecondaryWagProfile">SecondaryWagProfile</a>: <i>String</i>
    <a href="#security" title="Security">Security</a>: <i>String</i>
    <a href="#securityexemptlist" title="SecurityExemptList">SecurityExemptList</a>: <i>String</i>
    <a href="#securityobsoleteoption" title="SecurityObsoleteOption">SecurityObsoleteOption</a>: <i>String</i>
    <a href="#securityredirecturl" title="SecurityRedirectUrl">SecurityRedirectUrl</a>: <i>String</i>
    <a href="#splittunneling" title="SplitTunneling">SplitTunneling</a>: <i>String</i>
    <a href="#ssid" title="Ssid">Ssid</a>: <i>String</i>
    <a href="#stickyclientremove" title="StickyClientRemove">StickyClientRemove</a>: <i>String</i>
    <a href="#stickyclientthreshold2g" title="StickyClientThreshold2g">StickyClientThreshold2g</a>: <i>String</i>
    <a href="#stickyclientthreshold5g" title="StickyClientThreshold5g">StickyClientThreshold5g</a>: <i>String</i>
    <a href="#targetwaketime" title="TargetWakeTime">TargetWakeTime</a>: <i>String</i>
    <a href="#tkipcountermeasure" title="TkipCounterMeasure">TkipCounterMeasure</a>: <i>String</i>
    <a href="#tunnelechointerval" title="TunnelEchoInterval">TunnelEchoInterval</a>: <i>Double</i>
    <a href="#tunnelfallbackinterval" title="TunnelFallbackInterval">TunnelFallbackInterval</a>: <i>Double</i>
    <a href="#utmprofile" title="UtmProfile">UtmProfile</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#vlanauto" title="VlanAuto">VlanAuto</a>: <i>String</i>
    <a href="#vlanpooling" title="VlanPooling">VlanPooling</a>: <i>String</i>
    <a href="#vlanid" title="Vlanid">Vlanid</a>: <i>Double</i>
    <a href="#voiceenterprise" title="VoiceEnterprise">VoiceEnterprise</a>: <i>String</i>
    <a href="#macfilterlist" title="MacFilterList">MacFilterList</a>: <i>
      - <a href="macfilterlistdefinition.md">MacFilterListDefinition</a></i>
    <a href="#mpskkey" title="MpskKey">MpskKey</a>: <i>
      - <a href="mpskkeydefinition.md">MpskKeyDefinition</a></i>
    <a href="#portalmessageoverrides" title="PortalMessageOverrides">PortalMessageOverrides</a>: <i>
      - <a href="portalmessageoverridesdefinition.md">PortalMessageOverridesDefinition</a></i>
    <a href="#radiusmacauthusergroups" title="RadiusMacAuthUsergroups">RadiusMacAuthUsergroups</a>: <i>
      - <a href="radiusmacauthusergroupsdefinition.md">RadiusMacAuthUsergroupsDefinition</a></i>
    <a href="#selectedusergroups" title="SelectedUsergroups">SelectedUsergroups</a>: <i>
      - <a href="selectedusergroupsdefinition.md">SelectedUsergroupsDefinition</a></i>
    <a href="#usergroup" title="Usergroup">Usergroup</a>: <i>
      - <a href="usergroupdefinition.md">UsergroupDefinition</a></i>
    <a href="#vlanpool" title="VlanPool">VlanPool</a>: <i>
      - <a href="vlanpooldefinition.md">VlanPoolDefinition</a></i>
</pre>

## Properties

#### AccessControlList

access-control-list profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcctInterimInterval

WiFi RADIUS accounting interim interval (60 - 86400 sec, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalAkms

Additional AKMs. Valid values: `akm6`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddressGroup

Address group ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Alias

Alias.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AtfWeight

Airtime weight in percentage (default = 20).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Auth

Authentication protocol. Valid values: `psk`, `radius`, `usergroup`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BroadcastSsid

Enable/disable broadcasting the SSID (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BroadcastSuppression

Optional suppression of broadcast messages. For example, you can keep DHCP messages, ARP broadcasts, and so on off of the wireless network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BssColorPartial

Enable/disable 802.11ax partial BSS color (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptivePortalAcName

Local-bridging captive portal ac-name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptivePortalAuthTimeout

Hard timeout - AP will always clear the session after timeout regardless of traffic (0 - 864000 sec, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptivePortalMacauthRadiusSecret

Secret key to access the macauth RADIUS server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptivePortalMacauthRadiusServer

Captive portal external RADIUS server domain name or IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptivePortalRadiusSecret

Secret key to access the RADIUS server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptivePortalRadiusServer

Captive portal RADIUS server domain name or IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptivePortalSessionTimeoutInterval

Session timeout interval (0 - 864000 sec, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpLeaseTime

DHCP lease time in seconds for NAT IP address.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpOption43Insertion

Enable/disable insertion of DHCP option 43 (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpOption82CircuitIdInsertion

Enable/disable DHCP option 82 circuit-id insert (default = disable).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpOption82Insertion

Enable/disable DHCP option 82 insert (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpOption82RemoteIdInsertion

Enable/disable DHCP option 82 remote-id insert (default = disable). Valid values: `style-1`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicVlan

Enable/disable dynamic VLAN assignment. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapReauth

Enable/disable EAP re-authentication for WPA-Enterprise security. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapReauthIntv

EAP re-authentication interval (1800 - 864000 sec, default = 86400).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolKeyRetries

Enable/disable retransmission of EAPOL-Key frames (message 3/4 and group message 1/2) (default = enable). Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encrypt

Encryption protocol to use (only available when security is set to a WPA type). Valid values: `TKIP`, `AES`, `TKIP-AES`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalFastRoaming

Enable/disable fast roaming or pre-authentication with external APs not managed by the FortiGate (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalLogout

URL of external authentication logout server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalWeb

URL of external authentication web server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalWebFormat

URL query parameter detection (default = auto-detect). Valid values: `auto-detect`, `no-query-string`, `partial-query-string`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FastBssTransition

Enable/disable 802.11r Fast BSS Transition (FT) (default = disable). Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FastRoaming

Enable/disable fast-roaming, or pre-authentication, where supported by clients (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtMobilityDomain

Mobility domain identifier in FT (1 - 65535, default = 1000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtOverDs

Enable/disable FT over the Distribution System (DS). Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtR0KeyLifetime

Lifetime of the PMK-R0 key in FT, 1-65535 minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GtkRekey

Enable/disable GTK rekey for WPA security. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GtkRekeyIntv

GTK rekey interval (1800 - 864000 sec, default = 86400).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HighEfficiency

Enable/disable 802.11ax high efficiency (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hotspot20Profile

Hotspot 2.0 profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgmpSnooping

Enable/disable IGMP snooping. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntraVapPrivacy

Enable/disable blocking communication between clients on the same SSID (called intra-SSID privacy) (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

IP address and subnet mask for the local standalone NAT subnet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Rules

Optional rules of IPv6 packets. For example, you can keep RA, RS and so on off of the wireless network. Valid values: `drop-icmp6ra`, `drop-icmp6rs`, `drop-llmnr6`, `drop-icmp6mld2`, `drop-dhcp6s`, `drop-dhcp6c`, `ndp-proxy`, `drop-ns-dad`, `drop-ns-nondad`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

WEP Key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keyindex

WEP key index (1 - 4).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ldpc

VAP low-density parity-check (LDPC) coding configuration. Valid values: `disable`, `rx`, `tx`, `rxtx`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAuthentication

Enable/disable AP local authentication. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalBridging

Enable/disable bridging of wireless and Ethernet interfaces on the FortiAP (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalLan

Allow/deny traffic destined for a Class A, B, or C private IP address (default = allow). Valid values: `allow`, `deny`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalStandalone

Enable/disable AP local standalone (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalStandaloneNat

Enable/disable AP local standalone NAT mode. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAuthBypass

Enable/disable MAC authentication bypass. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacFilter

Enable/disable MAC filtering to block wireless clients by mac address. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacFilterPolicyOther

Allow or block clients with MAC addresses that are not in the filter list. Valid values: `allow`, `deny`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxClients

Maximum number of clients that can connect simultaneously to the VAP (default = 0, meaning no limitation).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxClientsAp

Maximum number of clients that can connect simultaneously to each radio (default = 0, meaning no limitation).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MeDisableThresh

Disable multicast enhancement when this many clients are receiving multicast traffic.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MeshBackhaul

Enable/disable using this VAP as a WiFi mesh backhaul (default = disable). This entry is only available when security is set to a WPA type or open. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mpsk

Enable/disable multiple pre-shared keys (PSKs.) Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MpskConcurrentClients

Number of pre-shared keys (PSKs) to allow if multiple pre-shared keys are enabled.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MpskProfile

MPSK profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MuMimo

Enable/disable Multi-user MIMO (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MulticastEnhance

Enable/disable converting multicast to unicast to improve performance (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MulticastRate

Multicast rate (0, 6000, 12000, or 24000 kbps, default = 0). Valid values: `0`, `6000`, `12000`, `24000`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Virtual AP name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Okc

Enable/disable Opportunistic Key Caching (OKC) (default = enable). Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OweGroups

OWE-Groups. Valid values: `19`, `20`, `21`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OweTransition

Enable/disable OWE transition mode support. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OweTransitionSsid

OWE transition mode peer SSID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Passphrase

WPA pre-shard key (PSK) to be used to authenticate WiFi users.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pmf

Protected Management Frames (PMF) support (default = disable). Valid values: `disable`, `enable`, `optional`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PmfAssocComebackTimeout

Protected Management Frames (PMF) comeback maximum timeout (1-20 sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PmfSaQueryRetryTimeout

Protected Management Frames (PMF) SA query retry timeout interval (1 - 5 100s of msec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortMacauth

Enable/disable LAN port MAC authentication (default = disable). Valid values: `disable`, `radius`, `address-group`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortMacauthReauthTimeout

LAN port MAC authentication re-authentication timeout value (default = 7200 sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortMacauthTimeout

LAN port MAC authentication idle timeout value (default = 600 sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortalMessageOverrideGroup

Replacement message group for this VAP (only available when security is set to a captive portal type).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortalType

Captive portal functionality. Configure how the captive portal authenticates users and whether it includes a disclaimer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryWagProfile

Primary wireless access gateway profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProbeRespSuppression

Enable/disable probe response suppression (to ignore weak signals) (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProbeRespThreshold

Minimum signal level/threshold in dBm required for the AP response to probe requests (-95 to -20, default = -80).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PtkRekey

Enable/disable PTK rekey for WPA-Enterprise security. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PtkRekeyIntv

PTK rekey interval (1800 - 864000 sec, default = 86400).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QosProfile

Quality of service profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quarantine

Enable/disable station quarantine (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Radio2gThreshold

Minimum signal level/threshold in dBm required for the AP response to receive a packet in 2.4G band (-95 to -20, default = -79).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Radio5gThreshold

Minimum signal level/threshold in dBm required for the AP response to receive a packet in 5G band(-95 to -20, default = -76).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadioSensitivity

Enable/disable software radio sensitivity (to ignore weak signals) (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusMacAuth

Enable/disable RADIUS-based MAC authentication of clients (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusMacAuthServer

RADIUS-based MAC authentication server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusServer

RADIUS server to be used to authenticate WiFi users.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rates11a

Allowed data rates for 802.11a. Valid values: `1`, `1-basic`, `2`, `2-basic`, `5.5`, `5.5-basic`, `11`, `11-basic`, `6`, `6-basic`, `9`, `9-basic`, `12`, `12-basic`, `18`, `18-basic`, `24`, `24-basic`, `36`, `36-basic`, `48`, `48-basic`, `54`, `54-basic`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rates11acSs12

Allowed data rates for 802.11ac with 1 or 2 spatial streams. Valid values: `mcs0/1`, `mcs1/1`, `mcs2/1`, `mcs3/1`, `mcs4/1`, `mcs5/1`, `mcs6/1`, `mcs7/1`, `mcs8/1`, `mcs9/1`, `mcs10/1`, `mcs11/1`, `mcs0/2`, `mcs1/2`, `mcs2/2`, `mcs3/2`, `mcs4/2`, `mcs5/2`, `mcs6/2`, `mcs7/2`, `mcs8/2`, `mcs9/2`, `mcs10/2`, `mcs11/2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rates11acSs34

Allowed data rates for 802.11ac with 3 or 4 spatial streams. Valid values: `mcs0/3`, `mcs1/3`, `mcs2/3`, `mcs3/3`, `mcs4/3`, `mcs5/3`, `mcs6/3`, `mcs7/3`, `mcs8/3`, `mcs9/3`, `mcs10/3`, `mcs11/3`, `mcs0/4`, `mcs1/4`, `mcs2/4`, `mcs3/4`, `mcs4/4`, `mcs5/4`, `mcs6/4`, `mcs7/4`, `mcs8/4`, `mcs9/4`, `mcs10/4`, `mcs11/4`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rates11bg

Allowed data rates for 802.11b/g. Valid values: `1`, `1-basic`, `2`, `2-basic`, `5.5`, `5.5-basic`, `11`, `11-basic`, `6`, `6-basic`, `9`, `9-basic`, `12`, `12-basic`, `18`, `18-basic`, `24`, `24-basic`, `36`, `36-basic`, `48`, `48-basic`, `54`, `54-basic`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rates11nSs12

Allowed data rates for 802.11n with 1 or 2 spatial streams. Valid values: `mcs0/1`, `mcs1/1`, `mcs2/1`, `mcs3/1`, `mcs4/1`, `mcs5/1`, `mcs6/1`, `mcs7/1`, `mcs8/2`, `mcs9/2`, `mcs10/2`, `mcs11/2`, `mcs12/2`, `mcs13/2`, `mcs14/2`, `mcs15/2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rates11nSs34

Allowed data rates for 802.11n with 3 or 4 spatial streams. Valid values: `mcs16/3`, `mcs17/3`, `mcs18/3`, `mcs19/3`, `mcs20/3`, `mcs21/3`, `mcs22/3`, `mcs23/3`, `mcs24/4`, `mcs25/4`, `mcs26/4`, `mcs27/4`, `mcs28/4`, `mcs29/4`, `mcs30/4`, `mcs31/4`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaeGroups

SAE-Groups. Valid values: `19`, `20`, `21`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaePassword

WPA3 SAE password to be used to authenticate WiFi users.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

VAP schedule name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryWagProfile

Secondary wireless access gateway profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Security

Security mode for the wireless interface (default = wpa2-only-personal).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityExemptList

Optional security exempt list for captive portal authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityObsoleteOption

Enable/disable obsolete security options. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityRedirectUrl

Optional URL for redirecting users after they pass captive portal authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitTunneling

Enable/disable split tunneling (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ssid

IEEE 802.11 service set identifier (SSID) for the wireless interface. Users who wish to use the wireless network must configure their computers to access this SSID name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StickyClientRemove

Enable/disable sticky client remove to maintain good signal level clients in SSID. (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StickyClientThreshold2g

Minimum signal level/threshold in dBm required for the 2G client to be serviced by the AP (-95 to -20, default = -79).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StickyClientThreshold5g

Minimum signal level/threshold in dBm required for the 5G client to be serviced by the AP (-95 to -20, default = -76).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetWakeTime

Enable/disable 802.11ax target wake time (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TkipCounterMeasure

Enable/disable TKIP counter measure. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelEchoInterval

The time interval to send echo to both primary and secondary tunnel peers (1 - 65535 sec, default = 300).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelFallbackInterval

The time interval for secondary tunnel to fall back to primary tunnel (0 - 65535 sec, default = 7200).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UtmProfile

UTM profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanAuto

Enable/disable automatic management of SSID VLAN interface. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanPooling

Enable/disable VLAN pooling, to allow grouping of multiple wireless controller VLANs into VLAN pools (default = disable). When set to wtp-group, VLAN pooling occurs with VLAN assignment by wtp-group. Valid values: `wtp-group`, `round-robin`, `hash`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vlanid

Optional VLAN ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VoiceEnterprise

Enable/disable 802.11k and 802.11v assisted Voice-Enterprise roaming (default = disable). Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacFilterList

_Required_: No

_Type_: List of <a href="macfilterlistdefinition.md">MacFilterListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MpskKey

_Required_: No

_Type_: List of <a href="mpskkeydefinition.md">MpskKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortalMessageOverrides

_Required_: No

_Type_: List of <a href="portalmessageoverridesdefinition.md">PortalMessageOverridesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusMacAuthUsergroups

_Required_: No

_Type_: List of <a href="radiusmacauthusergroupsdefinition.md">RadiusMacAuthUsergroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectedUsergroups

_Required_: No

_Type_: List of <a href="selectedusergroupsdefinition.md">SelectedUsergroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Usergroup

_Required_: No

_Type_: List of <a href="usergroupdefinition.md">UsergroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanPool

_Required_: No

_Type_: List of <a href="vlanpooldefinition.md">VlanPoolDefinition</a>

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

