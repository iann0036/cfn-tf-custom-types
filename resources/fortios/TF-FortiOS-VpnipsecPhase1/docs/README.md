# TF::FortiOS::VpnipsecPhase1

Configure VPN remote gateway.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::VpnipsecPhase1",
    "Properties" : {
        "<a href="#acctverify" title="AcctVerify">AcctVerify</a>" : <i>String</i>,
        "<a href="#addgwroute" title="AddGwRoute">AddGwRoute</a>" : <i>String</i>,
        "<a href="#addroute" title="AddRoute">AddRoute</a>" : <i>String</i>,
        "<a href="#assignip" title="AssignIp">AssignIp</a>" : <i>String</i>,
        "<a href="#assignipfrom" title="AssignIpFrom">AssignIpFrom</a>" : <i>String</i>,
        "<a href="#authmethod" title="Authmethod">Authmethod</a>" : <i>String</i>,
        "<a href="#authmethodremote" title="AuthmethodRemote">AuthmethodRemote</a>" : <i>String</i>,
        "<a href="#authpasswd" title="Authpasswd">Authpasswd</a>" : <i>String</i>,
        "<a href="#authusr" title="Authusr">Authusr</a>" : <i>String</i>,
        "<a href="#authusrgrp" title="Authusrgrp">Authusrgrp</a>" : <i>String</i>,
        "<a href="#autonegotiate" title="AutoNegotiate">AutoNegotiate</a>" : <i>String</i>,
        "<a href="#banner" title="Banner">Banner</a>" : <i>String</i>,
        "<a href="#certidvalidation" title="CertIdValidation">CertIdValidation</a>" : <i>String</i>,
        "<a href="#childlessike" title="ChildlessIke">ChildlessIke</a>" : <i>String</i>,
        "<a href="#clientautonegotiate" title="ClientAutoNegotiate">ClientAutoNegotiate</a>" : <i>String</i>,
        "<a href="#clientkeepalive" title="ClientKeepAlive">ClientKeepAlive</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#dhcp6ralinkaddr" title="Dhcp6RaLinkaddr">Dhcp6RaLinkaddr</a>" : <i>String</i>,
        "<a href="#dhcpragiaddr" title="DhcpRaGiaddr">DhcpRaGiaddr</a>" : <i>String</i>,
        "<a href="#dhgrp" title="Dhgrp">Dhgrp</a>" : <i>String</i>,
        "<a href="#digitalsignatureauth" title="DigitalSignatureAuth">DigitalSignatureAuth</a>" : <i>String</i>,
        "<a href="#distance" title="Distance">Distance</a>" : <i>Double</i>,
        "<a href="#dnsmode" title="DnsMode">DnsMode</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#dpd" title="Dpd">Dpd</a>" : <i>String</i>,
        "<a href="#dpdretrycount" title="DpdRetrycount">DpdRetrycount</a>" : <i>Double</i>,
        "<a href="#dpdretryinterval" title="DpdRetryinterval">DpdRetryinterval</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#eap" title="Eap">Eap</a>" : <i>String</i>,
        "<a href="#eapexcludepeergrp" title="EapExcludePeergrp">EapExcludePeergrp</a>" : <i>String</i>,
        "<a href="#eapidentity" title="EapIdentity">EapIdentity</a>" : <i>String</i>,
        "<a href="#enforceuniqueid" title="EnforceUniqueId">EnforceUniqueId</a>" : <i>String</i>,
        "<a href="#fecbase" title="FecBase">FecBase</a>" : <i>Double</i>,
        "<a href="#feccodec" title="FecCodec">FecCodec</a>" : <i>Double</i>,
        "<a href="#fecegress" title="FecEgress">FecEgress</a>" : <i>String</i>,
        "<a href="#fecingress" title="FecIngress">FecIngress</a>" : <i>String</i>,
        "<a href="#fecreceivetimeout" title="FecReceiveTimeout">FecReceiveTimeout</a>" : <i>Double</i>,
        "<a href="#fecredundant" title="FecRedundant">FecRedundant</a>" : <i>Double</i>,
        "<a href="#fecsendtimeout" title="FecSendTimeout">FecSendTimeout</a>" : <i>Double</i>,
        "<a href="#forticlientenforcement" title="ForticlientEnforcement">ForticlientEnforcement</a>" : <i>String</i>,
        "<a href="#fragmentation" title="Fragmentation">Fragmentation</a>" : <i>String</i>,
        "<a href="#fragmentationmtu" title="FragmentationMtu">FragmentationMtu</a>" : <i>Double</i>,
        "<a href="#groupauthentication" title="GroupAuthentication">GroupAuthentication</a>" : <i>String</i>,
        "<a href="#groupauthenticationsecret" title="GroupAuthenticationSecret">GroupAuthenticationSecret</a>" : <i>String</i>,
        "<a href="#hasyncespseqno" title="HaSyncEspSeqno">HaSyncEspSeqno</a>" : <i>String</i>,
        "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>String</i>,
        "<a href="#idletimeoutinterval" title="IdleTimeoutinterval">IdleTimeoutinterval</a>" : <i>Double</i>,
        "<a href="#ikeversion" title="IkeVersion">IkeVersion</a>" : <i>String</i>,
        "<a href="#includelocallan" title="IncludeLocalLan">IncludeLocalLan</a>" : <i>String</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#ipv4dnsserver1" title="Ipv4DnsServer1">Ipv4DnsServer1</a>" : <i>String</i>,
        "<a href="#ipv4dnsserver2" title="Ipv4DnsServer2">Ipv4DnsServer2</a>" : <i>String</i>,
        "<a href="#ipv4dnsserver3" title="Ipv4DnsServer3">Ipv4DnsServer3</a>" : <i>String</i>,
        "<a href="#ipv4endip" title="Ipv4EndIp">Ipv4EndIp</a>" : <i>String</i>,
        "<a href="#ipv4name" title="Ipv4Name">Ipv4Name</a>" : <i>String</i>,
        "<a href="#ipv4netmask" title="Ipv4Netmask">Ipv4Netmask</a>" : <i>String</i>,
        "<a href="#ipv4splitexclude" title="Ipv4SplitExclude">Ipv4SplitExclude</a>" : <i>String</i>,
        "<a href="#ipv4splitinclude" title="Ipv4SplitInclude">Ipv4SplitInclude</a>" : <i>String</i>,
        "<a href="#ipv4startip" title="Ipv4StartIp">Ipv4StartIp</a>" : <i>String</i>,
        "<a href="#ipv4winsserver1" title="Ipv4WinsServer1">Ipv4WinsServer1</a>" : <i>String</i>,
        "<a href="#ipv4winsserver2" title="Ipv4WinsServer2">Ipv4WinsServer2</a>" : <i>String</i>,
        "<a href="#ipv6dnsserver1" title="Ipv6DnsServer1">Ipv6DnsServer1</a>" : <i>String</i>,
        "<a href="#ipv6dnsserver2" title="Ipv6DnsServer2">Ipv6DnsServer2</a>" : <i>String</i>,
        "<a href="#ipv6dnsserver3" title="Ipv6DnsServer3">Ipv6DnsServer3</a>" : <i>String</i>,
        "<a href="#ipv6endip" title="Ipv6EndIp">Ipv6EndIp</a>" : <i>String</i>,
        "<a href="#ipv6name" title="Ipv6Name">Ipv6Name</a>" : <i>String</i>,
        "<a href="#ipv6prefix" title="Ipv6Prefix">Ipv6Prefix</a>" : <i>Double</i>,
        "<a href="#ipv6splitexclude" title="Ipv6SplitExclude">Ipv6SplitExclude</a>" : <i>String</i>,
        "<a href="#ipv6splitinclude" title="Ipv6SplitInclude">Ipv6SplitInclude</a>" : <i>String</i>,
        "<a href="#ipv6startip" title="Ipv6StartIp">Ipv6StartIp</a>" : <i>String</i>,
        "<a href="#keepalive" title="Keepalive">Keepalive</a>" : <i>Double</i>,
        "<a href="#keylife" title="Keylife">Keylife</a>" : <i>Double</i>,
        "<a href="#localgw" title="LocalGw">LocalGw</a>" : <i>String</i>,
        "<a href="#localid" title="Localid">Localid</a>" : <i>String</i>,
        "<a href="#localidtype" title="LocalidType">LocalidType</a>" : <i>String</i>,
        "<a href="#meshselectortype" title="MeshSelectorType">MeshSelectorType</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#modecfg" title="ModeCfg">ModeCfg</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nattraversal" title="Nattraversal">Nattraversal</a>" : <i>String</i>,
        "<a href="#negotiatetimeout" title="NegotiateTimeout">NegotiateTimeout</a>" : <i>Double</i>,
        "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>Double</i>,
        "<a href="#networkoverlay" title="NetworkOverlay">NetworkOverlay</a>" : <i>String</i>,
        "<a href="#peer" title="Peer">Peer</a>" : <i>String</i>,
        "<a href="#peergrp" title="Peergrp">Peergrp</a>" : <i>String</i>,
        "<a href="#peerid" title="Peerid">Peerid</a>" : <i>String</i>,
        "<a href="#peertype" title="Peertype">Peertype</a>" : <i>String</i>,
        "<a href="#ppk" title="Ppk">Ppk</a>" : <i>String</i>,
        "<a href="#ppkidentity" title="PpkIdentity">PpkIdentity</a>" : <i>String</i>,
        "<a href="#ppksecret" title="PpkSecret">PpkSecret</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#proposal" title="Proposal">Proposal</a>" : <i>String</i>,
        "<a href="#psksecret" title="Psksecret">Psksecret</a>" : <i>String</i>,
        "<a href="#psksecretremote" title="PsksecretRemote">PsksecretRemote</a>" : <i>String</i>,
        "<a href="#reauth" title="Reauth">Reauth</a>" : <i>String</i>,
        "<a href="#rekey" title="Rekey">Rekey</a>" : <i>String</i>,
        "<a href="#remotegw" title="RemoteGw">RemoteGw</a>" : <i>String</i>,
        "<a href="#remotegwddns" title="RemotegwDdns">RemotegwDdns</a>" : <i>String</i>,
        "<a href="#rsasignatureformat" title="RsaSignatureFormat">RsaSignatureFormat</a>" : <i>String</i>,
        "<a href="#savepassword" title="SavePassword">SavePassword</a>" : <i>String</i>,
        "<a href="#sendcertchain" title="SendCertChain">SendCertChain</a>" : <i>String</i>,
        "<a href="#signaturehashalg" title="SignatureHashAlg">SignatureHashAlg</a>" : <i>String</i>,
        "<a href="#splitincludeservice" title="SplitIncludeService">SplitIncludeService</a>" : <i>String</i>,
        "<a href="#suiteb" title="SuiteB">SuiteB</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#unitysupport" title="UnitySupport">UnitySupport</a>" : <i>String</i>,
        "<a href="#usrgrp" title="Usrgrp">Usrgrp</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#wizardtype" title="WizardType">WizardType</a>" : <i>String</i>,
        "<a href="#xauthtype" title="Xauthtype">Xauthtype</a>" : <i>String</i>,
        "<a href="#backupgateway" title="BackupGateway">BackupGateway</a>" : <i>[ <a href="backupgatewaydefinition.md">BackupGatewayDefinition</a>, ... ]</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ <a href="certificatedefinition.md">CertificateDefinition</a>, ... ]</i>,
        "<a href="#ipv4excluderange" title="Ipv4ExcludeRange">Ipv4ExcludeRange</a>" : <i>[ <a href="ipv4excluderangedefinition.md">Ipv4ExcludeRangeDefinition</a>, ... ]</i>,
        "<a href="#ipv6excluderange" title="Ipv6ExcludeRange">Ipv6ExcludeRange</a>" : <i>[ <a href="ipv6excluderangedefinition.md">Ipv6ExcludeRangeDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::VpnipsecPhase1
Properties:
    <a href="#acctverify" title="AcctVerify">AcctVerify</a>: <i>String</i>
    <a href="#addgwroute" title="AddGwRoute">AddGwRoute</a>: <i>String</i>
    <a href="#addroute" title="AddRoute">AddRoute</a>: <i>String</i>
    <a href="#assignip" title="AssignIp">AssignIp</a>: <i>String</i>
    <a href="#assignipfrom" title="AssignIpFrom">AssignIpFrom</a>: <i>String</i>
    <a href="#authmethod" title="Authmethod">Authmethod</a>: <i>String</i>
    <a href="#authmethodremote" title="AuthmethodRemote">AuthmethodRemote</a>: <i>String</i>
    <a href="#authpasswd" title="Authpasswd">Authpasswd</a>: <i>String</i>
    <a href="#authusr" title="Authusr">Authusr</a>: <i>String</i>
    <a href="#authusrgrp" title="Authusrgrp">Authusrgrp</a>: <i>String</i>
    <a href="#autonegotiate" title="AutoNegotiate">AutoNegotiate</a>: <i>String</i>
    <a href="#banner" title="Banner">Banner</a>: <i>String</i>
    <a href="#certidvalidation" title="CertIdValidation">CertIdValidation</a>: <i>String</i>
    <a href="#childlessike" title="ChildlessIke">ChildlessIke</a>: <i>String</i>
    <a href="#clientautonegotiate" title="ClientAutoNegotiate">ClientAutoNegotiate</a>: <i>String</i>
    <a href="#clientkeepalive" title="ClientKeepAlive">ClientKeepAlive</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#dhcp6ralinkaddr" title="Dhcp6RaLinkaddr">Dhcp6RaLinkaddr</a>: <i>String</i>
    <a href="#dhcpragiaddr" title="DhcpRaGiaddr">DhcpRaGiaddr</a>: <i>String</i>
    <a href="#dhgrp" title="Dhgrp">Dhgrp</a>: <i>String</i>
    <a href="#digitalsignatureauth" title="DigitalSignatureAuth">DigitalSignatureAuth</a>: <i>String</i>
    <a href="#distance" title="Distance">Distance</a>: <i>Double</i>
    <a href="#dnsmode" title="DnsMode">DnsMode</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#dpd" title="Dpd">Dpd</a>: <i>String</i>
    <a href="#dpdretrycount" title="DpdRetrycount">DpdRetrycount</a>: <i>Double</i>
    <a href="#dpdretryinterval" title="DpdRetryinterval">DpdRetryinterval</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#eap" title="Eap">Eap</a>: <i>String</i>
    <a href="#eapexcludepeergrp" title="EapExcludePeergrp">EapExcludePeergrp</a>: <i>String</i>
    <a href="#eapidentity" title="EapIdentity">EapIdentity</a>: <i>String</i>
    <a href="#enforceuniqueid" title="EnforceUniqueId">EnforceUniqueId</a>: <i>String</i>
    <a href="#fecbase" title="FecBase">FecBase</a>: <i>Double</i>
    <a href="#feccodec" title="FecCodec">FecCodec</a>: <i>Double</i>
    <a href="#fecegress" title="FecEgress">FecEgress</a>: <i>String</i>
    <a href="#fecingress" title="FecIngress">FecIngress</a>: <i>String</i>
    <a href="#fecreceivetimeout" title="FecReceiveTimeout">FecReceiveTimeout</a>: <i>Double</i>
    <a href="#fecredundant" title="FecRedundant">FecRedundant</a>: <i>Double</i>
    <a href="#fecsendtimeout" title="FecSendTimeout">FecSendTimeout</a>: <i>Double</i>
    <a href="#forticlientenforcement" title="ForticlientEnforcement">ForticlientEnforcement</a>: <i>String</i>
    <a href="#fragmentation" title="Fragmentation">Fragmentation</a>: <i>String</i>
    <a href="#fragmentationmtu" title="FragmentationMtu">FragmentationMtu</a>: <i>Double</i>
    <a href="#groupauthentication" title="GroupAuthentication">GroupAuthentication</a>: <i>String</i>
    <a href="#groupauthenticationsecret" title="GroupAuthenticationSecret">GroupAuthenticationSecret</a>: <i>String</i>
    <a href="#hasyncespseqno" title="HaSyncEspSeqno">HaSyncEspSeqno</a>: <i>String</i>
    <a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>String</i>
    <a href="#idletimeoutinterval" title="IdleTimeoutinterval">IdleTimeoutinterval</a>: <i>Double</i>
    <a href="#ikeversion" title="IkeVersion">IkeVersion</a>: <i>String</i>
    <a href="#includelocallan" title="IncludeLocalLan">IncludeLocalLan</a>: <i>String</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#ipv4dnsserver1" title="Ipv4DnsServer1">Ipv4DnsServer1</a>: <i>String</i>
    <a href="#ipv4dnsserver2" title="Ipv4DnsServer2">Ipv4DnsServer2</a>: <i>String</i>
    <a href="#ipv4dnsserver3" title="Ipv4DnsServer3">Ipv4DnsServer3</a>: <i>String</i>
    <a href="#ipv4endip" title="Ipv4EndIp">Ipv4EndIp</a>: <i>String</i>
    <a href="#ipv4name" title="Ipv4Name">Ipv4Name</a>: <i>String</i>
    <a href="#ipv4netmask" title="Ipv4Netmask">Ipv4Netmask</a>: <i>String</i>
    <a href="#ipv4splitexclude" title="Ipv4SplitExclude">Ipv4SplitExclude</a>: <i>String</i>
    <a href="#ipv4splitinclude" title="Ipv4SplitInclude">Ipv4SplitInclude</a>: <i>String</i>
    <a href="#ipv4startip" title="Ipv4StartIp">Ipv4StartIp</a>: <i>String</i>
    <a href="#ipv4winsserver1" title="Ipv4WinsServer1">Ipv4WinsServer1</a>: <i>String</i>
    <a href="#ipv4winsserver2" title="Ipv4WinsServer2">Ipv4WinsServer2</a>: <i>String</i>
    <a href="#ipv6dnsserver1" title="Ipv6DnsServer1">Ipv6DnsServer1</a>: <i>String</i>
    <a href="#ipv6dnsserver2" title="Ipv6DnsServer2">Ipv6DnsServer2</a>: <i>String</i>
    <a href="#ipv6dnsserver3" title="Ipv6DnsServer3">Ipv6DnsServer3</a>: <i>String</i>
    <a href="#ipv6endip" title="Ipv6EndIp">Ipv6EndIp</a>: <i>String</i>
    <a href="#ipv6name" title="Ipv6Name">Ipv6Name</a>: <i>String</i>
    <a href="#ipv6prefix" title="Ipv6Prefix">Ipv6Prefix</a>: <i>Double</i>
    <a href="#ipv6splitexclude" title="Ipv6SplitExclude">Ipv6SplitExclude</a>: <i>String</i>
    <a href="#ipv6splitinclude" title="Ipv6SplitInclude">Ipv6SplitInclude</a>: <i>String</i>
    <a href="#ipv6startip" title="Ipv6StartIp">Ipv6StartIp</a>: <i>String</i>
    <a href="#keepalive" title="Keepalive">Keepalive</a>: <i>Double</i>
    <a href="#keylife" title="Keylife">Keylife</a>: <i>Double</i>
    <a href="#localgw" title="LocalGw">LocalGw</a>: <i>String</i>
    <a href="#localid" title="Localid">Localid</a>: <i>String</i>
    <a href="#localidtype" title="LocalidType">LocalidType</a>: <i>String</i>
    <a href="#meshselectortype" title="MeshSelectorType">MeshSelectorType</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#modecfg" title="ModeCfg">ModeCfg</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nattraversal" title="Nattraversal">Nattraversal</a>: <i>String</i>
    <a href="#negotiatetimeout" title="NegotiateTimeout">NegotiateTimeout</a>: <i>Double</i>
    <a href="#networkid" title="NetworkId">NetworkId</a>: <i>Double</i>
    <a href="#networkoverlay" title="NetworkOverlay">NetworkOverlay</a>: <i>String</i>
    <a href="#peer" title="Peer">Peer</a>: <i>String</i>
    <a href="#peergrp" title="Peergrp">Peergrp</a>: <i>String</i>
    <a href="#peerid" title="Peerid">Peerid</a>: <i>String</i>
    <a href="#peertype" title="Peertype">Peertype</a>: <i>String</i>
    <a href="#ppk" title="Ppk">Ppk</a>: <i>String</i>
    <a href="#ppkidentity" title="PpkIdentity">PpkIdentity</a>: <i>String</i>
    <a href="#ppksecret" title="PpkSecret">PpkSecret</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#proposal" title="Proposal">Proposal</a>: <i>String</i>
    <a href="#psksecret" title="Psksecret">Psksecret</a>: <i>String</i>
    <a href="#psksecretremote" title="PsksecretRemote">PsksecretRemote</a>: <i>String</i>
    <a href="#reauth" title="Reauth">Reauth</a>: <i>String</i>
    <a href="#rekey" title="Rekey">Rekey</a>: <i>String</i>
    <a href="#remotegw" title="RemoteGw">RemoteGw</a>: <i>String</i>
    <a href="#remotegwddns" title="RemotegwDdns">RemotegwDdns</a>: <i>String</i>
    <a href="#rsasignatureformat" title="RsaSignatureFormat">RsaSignatureFormat</a>: <i>String</i>
    <a href="#savepassword" title="SavePassword">SavePassword</a>: <i>String</i>
    <a href="#sendcertchain" title="SendCertChain">SendCertChain</a>: <i>String</i>
    <a href="#signaturehashalg" title="SignatureHashAlg">SignatureHashAlg</a>: <i>String</i>
    <a href="#splitincludeservice" title="SplitIncludeService">SplitIncludeService</a>: <i>String</i>
    <a href="#suiteb" title="SuiteB">SuiteB</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#unitysupport" title="UnitySupport">UnitySupport</a>: <i>String</i>
    <a href="#usrgrp" title="Usrgrp">Usrgrp</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#wizardtype" title="WizardType">WizardType</a>: <i>String</i>
    <a href="#xauthtype" title="Xauthtype">Xauthtype</a>: <i>String</i>
    <a href="#backupgateway" title="BackupGateway">BackupGateway</a>: <i>
      - <a href="backupgatewaydefinition.md">BackupGatewayDefinition</a></i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>
      - <a href="certificatedefinition.md">CertificateDefinition</a></i>
    <a href="#ipv4excluderange" title="Ipv4ExcludeRange">Ipv4ExcludeRange</a>: <i>
      - <a href="ipv4excluderangedefinition.md">Ipv4ExcludeRangeDefinition</a></i>
    <a href="#ipv6excluderange" title="Ipv6ExcludeRange">Ipv6ExcludeRange</a>: <i>
      - <a href="ipv6excluderangedefinition.md">Ipv6ExcludeRangeDefinition</a></i>
</pre>

## Properties

#### AcctVerify

Enable/disable verification of RADIUS accounting record. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddGwRoute

Enable/disable automatically add a route to the remote gateway. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddRoute

Enable/disable control addition of a route to peer destination selector. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssignIp

Enable/disable assignment of IP to IPsec interface via configuration method. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssignIpFrom

Method by which the IP address will be assigned. Valid values: `range`, `usrgrp`, `dhcp`, `name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authmethod

Authentication method. Valid values: `psk`, `signature`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthmethodRemote

Authentication method (remote side). Valid values: `psk`, `signature`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authpasswd

XAuth password (max 35 characters).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authusr

XAuth user name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authusrgrp

Authentication user group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoNegotiate

Enable/disable automatic initiation of IKE SA negotiation. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Banner

Message that unity client should display after connecting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertIdValidation

Enable/disable cross validation of peer ID and the identity in the peer's certificate as specified in RFC 4945. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChildlessIke

Enable/disable childless IKEv2 initiation (RFC 6023). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAutoNegotiate

Enable/disable allowing the VPN client to bring up the tunnel when there is no traffic. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientKeepAlive

Enable/disable allowing the VPN client to keep the tunnel up when there is no traffic. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhcp6RaLinkaddr

Relay agent IPv6 link address to use in DHCP6 requests.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpRaGiaddr

Relay agent gateway IP address to use in the giaddr field of DHCP requests.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhgrp

DH group. Valid values: `1`, `2`, `5`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `27`, `28`, `29`, `30`, `31`, `32`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DigitalSignatureAuth

Enable/disable IKEv2 Digital Signature Authentication (RFC 7427). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Distance

Distance for routes added by IKE (1 - 255).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsMode

DNS server mode. Valid values: `manual`, `auto`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

Instruct unity clients about the default DNS domain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dpd

Dead Peer Detection mode. Valid values: `disable`, `on-idle`, `on-demand`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpdRetrycount

Number of DPD retry attempts.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpdRetryinterval

DPD retry interval.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Eap

Enable/disable IKEv2 EAP authentication. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapExcludePeergrp

Peer group excluded from EAP authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapIdentity

IKEv2 EAP peer identity type. Valid values: `use-id-payload`, `send-request`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforceUniqueId

Enable/disable peer ID uniqueness check. Valid values: `disable`, `keep-new`, `keep-old`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FecBase

Number of base Forward Error Correction packets (1 - 100).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FecCodec

ipsec fec encoding/decoding algorithm (0: reed-solomon, 1: xor).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FecEgress

Enable/disable Forward Error Correction for egress IPsec traffic. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FecIngress

Enable/disable Forward Error Correction for ingress IPsec traffic. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FecReceiveTimeout

Timeout in milliseconds before dropping Forward Error Correction packets (1 - 10000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FecRedundant

Number of redundant Forward Error Correction packets (1 - 100).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FecSendTimeout

Timeout in milliseconds before sending Forward Error Correction packets (1 - 1000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientEnforcement

Enable/disable FortiClient enforcement. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fragmentation

Enable/disable fragment IKE message on re-transmission. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FragmentationMtu

IKE fragmentation MTU (500 - 16000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupAuthentication

Enable/disable IKEv2 IDi group authentication. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupAuthenticationSecret

Password for IKEv2 IDi group authentication.  (ASCII string or hexadecimal indicated by a leading 0x.).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaSyncEspSeqno

Enable/disable sequence number jump ahead for IPsec HA. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

Enable/disable IPsec tunnel idle timeout. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeoutinterval

IPsec tunnel idle timeout in minutes (5 - 43200).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeVersion

IKE protocol version. Valid values: `1`, `2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeLocalLan

Enable/disable allow local LAN access on unity clients. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Local physical, aggregate, or VLAN outgoing interface.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4DnsServer1

IPv4 DNS server 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4DnsServer2

IPv4 DNS server 2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4DnsServer3

IPv4 DNS server 3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4EndIp

End of IPv4 range.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4Name

IPv4 address name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4Netmask

IPv4 Netmask.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4SplitExclude

IPv4 subnets that should not be sent over the IPsec tunnel.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4SplitInclude

IPv4 split-include subnets.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4StartIp

Start of IPv4 range.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4WinsServer1

WINS server 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4WinsServer2

WINS server 2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6DnsServer1

IPv6 DNS server 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6DnsServer2

IPv6 DNS server 2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6DnsServer3

IPv6 DNS server 3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6EndIp

End of IPv6 range.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Name

IPv6 address name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Prefix

IPv6 prefix.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6SplitExclude

IPv6 subnets that should not be sent over the IPsec tunnel.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6SplitInclude

IPv6 split-include subnets.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6StartIp

Start of IPv6 range.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keepalive

NAT-T keep alive interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keylife

Time to wait in seconds before phase 1 encryption key expires.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalGw

Local VPN gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Localid

Local ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalidType

Local ID type. Valid values: `auto`, `fqdn`, `user-fqdn`, `keyid`, `address`, `asn1dn`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MeshSelectorType

Add selectors containing subsets of the configuration depending on traffic. Valid values: `disable`, `subnet`, `host`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

ID protection mode used to establish a secure channel. Valid values: `aggressive`, `main`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModeCfg

Enable/disable configuration method. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

IPsec remote gateway name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nattraversal

Enable/disable NAT traversal. Valid values: `enable`, `disable`, `forced`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegotiateTimeout

IKE SA negotiation timeout in seconds (1 - 300).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

VPN gateway network ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkOverlay

Enable/disable network overlays. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Peer

Accept this peer certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Peergrp

Accept this peer certificate group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Peerid

Accept this peer identity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Peertype

Accept this peer type. Valid values: `any`, `one`, `dialup`, `peer`, `peergrp`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ppk

Enable/disable IKEv2 Postquantum Preshared Key (PPK). Valid values: `disable`, `allow`, `require`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PpkIdentity

IKEv2 Postquantum Preshared Key Identity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PpkSecret

IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal encoded with a leading 0x).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Priority for routes added by IKE (0 - 4294967295).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proposal

Phase1 proposal. Valid values: `des-md5`, `des-sha1`, `des-sha256`, `des-sha384`, `des-sha512`, `3des-md5`, `3des-sha1`, `3des-sha256`, `3des-sha384`, `3des-sha512`, `aes128-md5`, `aes128-sha1`, `aes128-sha256`, `aes128-sha384`, `aes128-sha512`, `aes128gcm-prfsha1`, `aes128gcm-prfsha256`, `aes128gcm-prfsha384`, `aes128gcm-prfsha512`, `aes192-md5`, `aes192-sha1`, `aes192-sha256`, `aes192-sha384`, `aes192-sha512`, `aes256-md5`, `aes256-sha1`, `aes256-sha256`, `aes256-sha384`, `aes256-sha512`, `aes256gcm-prfsha1`, `aes256gcm-prfsha256`, `aes256gcm-prfsha384`, `aes256gcm-prfsha512`, `chacha20poly1305-prfsha1`, `chacha20poly1305-prfsha256`, `chacha20poly1305-prfsha384`, `chacha20poly1305-prfsha512`, `aria128-md5`, `aria128-sha1`, `aria128-sha256`, `aria128-sha384`, `aria128-sha512`, `aria192-md5`, `aria192-sha1`, `aria192-sha256`, `aria192-sha384`, `aria192-sha512`, `aria256-md5`, `aria256-sha1`, `aria256-sha256`, `aria256-sha384`, `aria256-sha512`, `seed-md5`, `seed-sha1`, `seed-sha256`, `seed-sha384`, `seed-sha512`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Psksecret

Pre-shared secret for PSK authentication (ASCII string or hexadecimal encoded with a leading 0x).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PsksecretRemote

Pre-shared secret for remote side PSK authentication (ASCII string or hexadecimal encoded with a leading 0x).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reauth

Enable/disable re-authentication upon IKE SA lifetime expiration. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rekey

Enable/disable phase1 rekey. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteGw

Remote VPN gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemotegwDdns

Domain name of remote gateway (eg. name.DDNS.com).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RsaSignatureFormat

Digital Signature Authentication RSA signature format. Valid values: `pkcs1`, `pss`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SavePassword

Enable/disable saving XAuth username and password on VPN clients. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendCertChain

Enable/disable sending certificate chain. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignatureHashAlg

Digital Signature Authentication hash algorithms. Valid values: `sha1`, `sha2-256`, `sha2-384`, `sha2-512`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitIncludeService

Split-include services.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuiteB

Use Suite-B. Valid values: `disable`, `suite-b-gcm-128`, `suite-b-gcm-256`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Remote gateway type. Valid values: `static`, `dynamic`, `ddns`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnitySupport

Enable/disable support for Cisco UNITY Configuration Method extensions. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Usrgrp

User group name for dialup peers.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WizardType

GUI VPN Wizard Type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Xauthtype

XAuth type. Valid values: `disable`, `client`, `pap`, `chap`, `auto`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupGateway

_Required_: No

_Type_: List of <a href="backupgatewaydefinition.md">BackupGatewayDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: List of <a href="certificatedefinition.md">CertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4ExcludeRange

_Required_: No

_Type_: List of <a href="ipv4excluderangedefinition.md">Ipv4ExcludeRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6ExcludeRange

_Required_: No

_Type_: List of <a href="ipv6excluderangedefinition.md">Ipv6ExcludeRangeDefinition</a>

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

