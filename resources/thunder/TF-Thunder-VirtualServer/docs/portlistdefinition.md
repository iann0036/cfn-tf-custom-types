# TF::Thunder::VirtualServer PortListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#altprotocol1" title="AltProtocol1">AltProtocol1</a>" : <i>String</i>,
    "<a href="#altprotocol2" title="AltProtocol2">AltProtocol2</a>" : <i>String</i>,
    "<a href="#alternateport" title="AlternatePort">AlternatePort</a>" : <i>Double</i>,
    "<a href="#alternateportnumber" title="AlternatePortNumber">AlternatePortNumber</a>" : <i>Double</i>,
    "<a href="#auto" title="Auto">Auto</a>" : <i>Double</i>,
    "<a href="#clientipstickynat" title="ClientipStickyNat">ClientipStickyNat</a>" : <i>Double</i>,
    "<a href="#connlimit" title="ConnLimit">ConnLimit</a>" : <i>Double</i>,
    "<a href="#defselectionifpreffailed" title="DefSelectionIfPrefFailed">DefSelectionIfPrefFailed</a>" : <i>String</i>,
    "<a href="#enableplayeridcheck" title="EnablePlayeridCheck">EnablePlayeridCheck</a>" : <i>Double</i>,
    "<a href="#ethfwd" title="EthFwd">EthFwd</a>" : <i>Double</i>,
    "<a href="#ethrev" title="EthRev">EthRev</a>" : <i>Double</i>,
    "<a href="#expand" title="Expand">Expand</a>" : <i>Double</i>,
    "<a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>" : <i>Double</i>,
    "<a href="#forceroutingmode" title="ForceRoutingMode">ForceRoutingMode</a>" : <i>Double</i>,
    "<a href="#gslbenable" title="GslbEnable">GslbEnable</a>" : <i>Double</i>,
    "<a href="#haconnmirror" title="HaConnMirror">HaConnMirror</a>" : <i>Double</i>,
    "<a href="#ipmaplist" title="IpMapList">IpMapList</a>" : <i>String</i>,
    "<a href="#ipinip" title="Ipinip">Ipinip</a>" : <i>Double</i>,
    "<a href="#ipv6acl" title="Ipv6Acl">Ipv6Acl</a>" : <i>String</i>,
    "<a href="#l7hardwareassist" title="L7HardwareAssist">L7HardwareAssist</a>" : <i>Double</i>,
    "<a href="#messageswitching" title="MessageSwitching">MessageSwitching</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#noautouponaflex" title="NoAutoUpOnAflex">NoAutoUpOnAflex</a>" : <i>Double</i>,
    "<a href="#nodestnat" title="NoDestNat">NoDestNat</a>" : <i>Double</i>,
    "<a href="#nologging" title="NoLogging">NoLogging</a>" : <i>Double</i>,
    "<a href="#onsyn" title="OnSyn">OnSyn</a>" : <i>Double</i>,
    "<a href="#optimizationlevel" title="OptimizationLevel">OptimizationLevel</a>" : <i>String</i>,
    "<a href="#persisttype" title="PersistType">PersistType</a>" : <i>String</i>,
    "<a href="#pool" title="Pool">Pool</a>" : <i>String</i>,
    "<a href="#poolshared" title="PoolShared">PoolShared</a>" : <i>String</i>,
    "<a href="#portnumber" title="PortNumber">PortNumber</a>" : <i>Double</i>,
    "<a href="#porttranslation" title="PortTranslation">PortTranslation</a>" : <i>Double</i>,
    "<a href="#precedence" title="Precedence">Precedence</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#range" title="Range">Range</a>" : <i>Double</i>,
    "<a href="#rate" title="Rate">Rate</a>" : <i>Double</i>,
    "<a href="#redirecttohttps" title="RedirectToHttps">RedirectToHttps</a>" : <i>Double</i>,
    "<a href="#reqfail" title="ReqFail">ReqFail</a>" : <i>Double</i>,
    "<a href="#reset" title="Reset">Reset</a>" : <i>Double</i>,
    "<a href="#resetonserverselectionfail" title="ResetOnServerSelectionFail">ResetOnServerSelectionFail</a>" : <i>Double</i>,
    "<a href="#rtpsipcallidmatch" title="RtpSipCallIdMatch">RtpSipCallIdMatch</a>" : <i>Double</i>,
    "<a href="#scaleoutbucketcount" title="ScaleoutBucketCount">ScaleoutBucketCount</a>" : <i>Double</i>,
    "<a href="#scaleoutdevicegroup" title="ScaleoutDeviceGroup">ScaleoutDeviceGroup</a>" : <i>Double</i>,
    "<a href="#secs" title="Secs">Secs</a>" : <i>Double</i>,
    "<a href="#servselfail" title="ServSelFail">ServSelFail</a>" : <i>Double</i>,
    "<a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>" : <i>String</i>,
    "<a href="#sharedpartitioncachetemplate" title="SharedPartitionCacheTemplate">SharedPartitionCacheTemplate</a>" : <i>Double</i>,
    "<a href="#sharedpartitionclientssltemplate" title="SharedPartitionClientSslTemplate">SharedPartitionClientSslTemplate</a>" : <i>Double</i>,
    "<a href="#sharedpartitionconnectionreusetemplate" title="SharedPartitionConnectionReuseTemplate">SharedPartitionConnectionReuseTemplate</a>" : <i>Double</i>,
    "<a href="#sharedpartitiondiametertemplate" title="SharedPartitionDiameterTemplate">SharedPartitionDiameterTemplate</a>" : <i>Double</i>,
    "<a href="#sharedpartitiondnstemplate" title="SharedPartitionDnsTemplate">SharedPartitionDnsTemplate</a>" : <i>Double</i>,
    "<a href="#sharedpartitiondynamicservicetemplate" title="SharedPartitionDynamicServiceTemplate">SharedPartitionDynamicServiceTemplate</a>" : <i>Double</i>,
    "<a href="#sharedpartitionexternalservicetemplate" title="SharedPartitionExternalServiceTemplate">SharedPartitionExternalServiceTemplate</a>" : <i>Double</i>,
    "<a href="#sharedpartitionhttppolicytemplate" title="SharedPartitionHttpPolicyTemplate">SharedPartitionHttpPolicyTemplate</a>" : <i>Double</i>,
    "<a href="#sharedpartitionhttptemplate" title="SharedPartitionHttpTemplate">SharedPartitionHttpTemplate</a>" : <i>Double</i>,
    "<a href="#sharedpartitionpersistcookietemplate" title="SharedPartitionPersistCookieTemplate">SharedPartitionPersistCookieTemplate</a>" : <i>Double</i>,
    "<a href="#sharedpartitionpersistdestinationiptemplate" title="SharedPartitionPersistDestinationIpTemplate">SharedPartitionPersistDestinationIpTemplate</a>" : <i>Double</i>,
    "<a href="#sharedpartitionpersistsourceiptemplate" title="SharedPartitionPersistSourceIpTemplate">SharedPartitionPersistSourceIpTemplate</a>" : <i>Double</i>,
    "<a href="#sharedpartitionpersistsslsidtemplate" title="SharedPartitionPersistSslSidTemplate">SharedPartitionPersistSslSidTemplate</a>" : <i>Double</i>,
    "<a href="#sharedpartitionpolicytemplate" title="SharedPartitionPolicyTemplate">SharedPartitionPolicyTemplate</a>" : <i>Double</i>,
    "<a href="#sharedpartitionpool" title="SharedPartitionPool">SharedPartitionPool</a>" : <i>Double</i>,
    "<a href="#sharedpartitionserverssltemplate" title="SharedPartitionServerSslTemplate">SharedPartitionServerSslTemplate</a>" : <i>Double</i>,
    "<a href="#sharedpartitiontcp" title="SharedPartitionTcp">SharedPartitionTcp</a>" : <i>Double</i>,
    "<a href="#sharedpartitiontcpproxytemplate" title="SharedPartitionTcpProxyTemplate">SharedPartitionTcpProxyTemplate</a>" : <i>Double</i>,
    "<a href="#sharedpartitionudp" title="SharedPartitionUdp">SharedPartitionUdp</a>" : <i>Double</i>,
    "<a href="#sharedpartitionvirtualporttemplate" title="SharedPartitionVirtualPortTemplate">SharedPartitionVirtualPortTemplate</a>" : <i>Double</i>,
    "<a href="#skiprevhash" title="SkipRevHash">SkipRevHash</a>" : <i>Double</i>,
    "<a href="#snatonvip" title="SnatOnVip">SnatOnVip</a>" : <i>Double</i>,
    "<a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>" : <i>String</i>,
    "<a href="#supporthttp2" title="SupportHttp2">SupportHttp2</a>" : <i>Double</i>,
    "<a href="#syncookie" title="SynCookie">SynCookie</a>" : <i>Double</i>,
    "<a href="#templatecache" title="TemplateCache">TemplateCache</a>" : <i>String</i>,
    "<a href="#templatecacheshared" title="TemplateCacheShared">TemplateCacheShared</a>" : <i>String</i>,
    "<a href="#templateclientssh" title="TemplateClientSsh">TemplateClientSsh</a>" : <i>String</i>,
    "<a href="#templateclientssl" title="TemplateClientSsl">TemplateClientSsl</a>" : <i>String</i>,
    "<a href="#templateclientsslshared" title="TemplateClientSslShared">TemplateClientSslShared</a>" : <i>String</i>,
    "<a href="#templateconnectionreuse" title="TemplateConnectionReuse">TemplateConnectionReuse</a>" : <i>String</i>,
    "<a href="#templateconnectionreuseshared" title="TemplateConnectionReuseShared">TemplateConnectionReuseShared</a>" : <i>String</i>,
    "<a href="#templatedblb" title="TemplateDblb">TemplateDblb</a>" : <i>String</i>,
    "<a href="#templatediameter" title="TemplateDiameter">TemplateDiameter</a>" : <i>String</i>,
    "<a href="#templatediametershared" title="TemplateDiameterShared">TemplateDiameterShared</a>" : <i>String</i>,
    "<a href="#templatedns" title="TemplateDns">TemplateDns</a>" : <i>String</i>,
    "<a href="#templatednsshared" title="TemplateDnsShared">TemplateDnsShared</a>" : <i>String</i>,
    "<a href="#templatedynamicservice" title="TemplateDynamicService">TemplateDynamicService</a>" : <i>String</i>,
    "<a href="#templatedynamicserviceshared" title="TemplateDynamicServiceShared">TemplateDynamicServiceShared</a>" : <i>String</i>,
    "<a href="#templateexternalservice" title="TemplateExternalService">TemplateExternalService</a>" : <i>String</i>,
    "<a href="#templateexternalserviceshared" title="TemplateExternalServiceShared">TemplateExternalServiceShared</a>" : <i>String</i>,
    "<a href="#templatefileinspection" title="TemplateFileInspection">TemplateFileInspection</a>" : <i>String</i>,
    "<a href="#templatefix" title="TemplateFix">TemplateFix</a>" : <i>String</i>,
    "<a href="#templateftp" title="TemplateFtp">TemplateFtp</a>" : <i>String</i>,
    "<a href="#templatehttp" title="TemplateHttp">TemplateHttp</a>" : <i>String</i>,
    "<a href="#templatehttppolicy" title="TemplateHttpPolicy">TemplateHttpPolicy</a>" : <i>String</i>,
    "<a href="#templatehttppolicyshared" title="TemplateHttpPolicyShared">TemplateHttpPolicyShared</a>" : <i>String</i>,
    "<a href="#templatehttpshared" title="TemplateHttpShared">TemplateHttpShared</a>" : <i>String</i>,
    "<a href="#templateimappop3" title="TemplateImapPop3">TemplateImapPop3</a>" : <i>String</i>,
    "<a href="#templatepersistcookie" title="TemplatePersistCookie">TemplatePersistCookie</a>" : <i>String</i>,
    "<a href="#templatepersistcookieshared" title="TemplatePersistCookieShared">TemplatePersistCookieShared</a>" : <i>String</i>,
    "<a href="#templatepersistdestinationip" title="TemplatePersistDestinationIp">TemplatePersistDestinationIp</a>" : <i>String</i>,
    "<a href="#templatepersistdestinationipshared" title="TemplatePersistDestinationIpShared">TemplatePersistDestinationIpShared</a>" : <i>String</i>,
    "<a href="#templatepersistsourceip" title="TemplatePersistSourceIp">TemplatePersistSourceIp</a>" : <i>String</i>,
    "<a href="#templatepersistsourceipshared" title="TemplatePersistSourceIpShared">TemplatePersistSourceIpShared</a>" : <i>String</i>,
    "<a href="#templatepersistsslsid" title="TemplatePersistSslSid">TemplatePersistSslSid</a>" : <i>String</i>,
    "<a href="#templatepersistsslsidshared" title="TemplatePersistSslSidShared">TemplatePersistSslSidShared</a>" : <i>String</i>,
    "<a href="#templatepolicy" title="TemplatePolicy">TemplatePolicy</a>" : <i>String</i>,
    "<a href="#templatepolicyshared" title="TemplatePolicyShared">TemplatePolicyShared</a>" : <i>String</i>,
    "<a href="#templatereqmodicap" title="TemplateReqmodIcap">TemplateReqmodIcap</a>" : <i>String</i>,
    "<a href="#templaterespmodicap" title="TemplateRespmodIcap">TemplateRespmodIcap</a>" : <i>String</i>,
    "<a href="#templatescaleout" title="TemplateScaleout">TemplateScaleout</a>" : <i>String</i>,
    "<a href="#templateserverssh" title="TemplateServerSsh">TemplateServerSsh</a>" : <i>String</i>,
    "<a href="#templateserverssl" title="TemplateServerSsl">TemplateServerSsl</a>" : <i>String</i>,
    "<a href="#templateserversslshared" title="TemplateServerSslShared">TemplateServerSslShared</a>" : <i>String</i>,
    "<a href="#templatesip" title="TemplateSip">TemplateSip</a>" : <i>String</i>,
    "<a href="#templatesmpp" title="TemplateSmpp">TemplateSmpp</a>" : <i>String</i>,
    "<a href="#templatesmtp" title="TemplateSmtp">TemplateSmtp</a>" : <i>String</i>,
    "<a href="#templatessli" title="TemplateSsli">TemplateSsli</a>" : <i>String</i>,
    "<a href="#templatetcp" title="TemplateTcp">TemplateTcp</a>" : <i>String</i>,
    "<a href="#templatetcpproxy" title="TemplateTcpProxy">TemplateTcpProxy</a>" : <i>String</i>,
    "<a href="#templatetcpproxyclient" title="TemplateTcpProxyClient">TemplateTcpProxyClient</a>" : <i>String</i>,
    "<a href="#templatetcpproxyserver" title="TemplateTcpProxyServer">TemplateTcpProxyServer</a>" : <i>String</i>,
    "<a href="#templatetcpproxyshared" title="TemplateTcpProxyShared">TemplateTcpProxyShared</a>" : <i>String</i>,
    "<a href="#templatetcpshared" title="TemplateTcpShared">TemplateTcpShared</a>" : <i>String</i>,
    "<a href="#templateudp" title="TemplateUdp">TemplateUdp</a>" : <i>String</i>,
    "<a href="#templateudpshared" title="TemplateUdpShared">TemplateUdpShared</a>" : <i>String</i>,
    "<a href="#templatevirtualport" title="TemplateVirtualPort">TemplateVirtualPort</a>" : <i>String</i>,
    "<a href="#templatevirtualportshared" title="TemplateVirtualPortShared">TemplateVirtualPortShared</a>" : <i>String</i>,
    "<a href="#trunkfwd" title="TrunkFwd">TrunkFwd</a>" : <i>Double</i>,
    "<a href="#trunkrev" title="TrunkRev">TrunkRev</a>" : <i>Double</i>,
    "<a href="#usealternateport" title="UseAlternatePort">UseAlternatePort</a>" : <i>Double</i>,
    "<a href="#usecgnv6" title="UseCgnv6">UseCgnv6</a>" : <i>Double</i>,
    "<a href="#usedefaultifnoserver" title="UseDefaultIfNoServer">UseDefaultIfNoServer</a>" : <i>Double</i>,
    "<a href="#usercvhopforresp" title="UseRcvHopForResp">UseRcvHopForResp</a>" : <i>Double</i>,
    "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#view" title="View">View</a>" : <i>Double</i>,
    "<a href="#waftemplate" title="WafTemplate">WafTemplate</a>" : <i>String</i>,
    "<a href="#whendown" title="WhenDown">WhenDown</a>" : <i>Double</i>,
    "<a href="#whendownprotocol2" title="WhenDownProtocol2">WhenDownProtocol2</a>" : <i>Double</i>,
    "<a href="#aclidlist" title="AclIdList">AclIdList</a>" : <i>[ <a href="aclidlistdefinition.md">AclIdListDefinition</a>, ... ]</i>,
    "<a href="#aclnamelist" title="AclNameList">AclNameList</a>" : <i>[ <a href="aclnamelistdefinition.md">AclNameListDefinition</a>, ... ]</i>,
    "<a href="#aflexscripts" title="AflexScripts">AflexScripts</a>" : <i>[ <a href="aflexscriptsdefinition.md">AflexScriptsDefinition</a>, ... ]</i>,
    "<a href="#authcfg" title="AuthCfg">AuthCfg</a>" : <i>[ <a href="authcfgdefinition.md">AuthCfgDefinition</a>, ... ]</i>,
    "<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>" : <i>[ <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#altprotocol1" title="AltProtocol1">AltProtocol1</a>: <i>String</i>
<a href="#altprotocol2" title="AltProtocol2">AltProtocol2</a>: <i>String</i>
<a href="#alternateport" title="AlternatePort">AlternatePort</a>: <i>Double</i>
<a href="#alternateportnumber" title="AlternatePortNumber">AlternatePortNumber</a>: <i>Double</i>
<a href="#auto" title="Auto">Auto</a>: <i>Double</i>
<a href="#clientipstickynat" title="ClientipStickyNat">ClientipStickyNat</a>: <i>Double</i>
<a href="#connlimit" title="ConnLimit">ConnLimit</a>: <i>Double</i>
<a href="#defselectionifpreffailed" title="DefSelectionIfPrefFailed">DefSelectionIfPrefFailed</a>: <i>String</i>
<a href="#enableplayeridcheck" title="EnablePlayeridCheck">EnablePlayeridCheck</a>: <i>Double</i>
<a href="#ethfwd" title="EthFwd">EthFwd</a>: <i>Double</i>
<a href="#ethrev" title="EthRev">EthRev</a>: <i>Double</i>
<a href="#expand" title="Expand">Expand</a>: <i>Double</i>
<a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>: <i>Double</i>
<a href="#forceroutingmode" title="ForceRoutingMode">ForceRoutingMode</a>: <i>Double</i>
<a href="#gslbenable" title="GslbEnable">GslbEnable</a>: <i>Double</i>
<a href="#haconnmirror" title="HaConnMirror">HaConnMirror</a>: <i>Double</i>
<a href="#ipmaplist" title="IpMapList">IpMapList</a>: <i>String</i>
<a href="#ipinip" title="Ipinip">Ipinip</a>: <i>Double</i>
<a href="#ipv6acl" title="Ipv6Acl">Ipv6Acl</a>: <i>String</i>
<a href="#l7hardwareassist" title="L7HardwareAssist">L7HardwareAssist</a>: <i>Double</i>
<a href="#messageswitching" title="MessageSwitching">MessageSwitching</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#noautouponaflex" title="NoAutoUpOnAflex">NoAutoUpOnAflex</a>: <i>Double</i>
<a href="#nodestnat" title="NoDestNat">NoDestNat</a>: <i>Double</i>
<a href="#nologging" title="NoLogging">NoLogging</a>: <i>Double</i>
<a href="#onsyn" title="OnSyn">OnSyn</a>: <i>Double</i>
<a href="#optimizationlevel" title="OptimizationLevel">OptimizationLevel</a>: <i>String</i>
<a href="#persisttype" title="PersistType">PersistType</a>: <i>String</i>
<a href="#pool" title="Pool">Pool</a>: <i>String</i>
<a href="#poolshared" title="PoolShared">PoolShared</a>: <i>String</i>
<a href="#portnumber" title="PortNumber">PortNumber</a>: <i>Double</i>
<a href="#porttranslation" title="PortTranslation">PortTranslation</a>: <i>Double</i>
<a href="#precedence" title="Precedence">Precedence</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#range" title="Range">Range</a>: <i>Double</i>
<a href="#rate" title="Rate">Rate</a>: <i>Double</i>
<a href="#redirecttohttps" title="RedirectToHttps">RedirectToHttps</a>: <i>Double</i>
<a href="#reqfail" title="ReqFail">ReqFail</a>: <i>Double</i>
<a href="#reset" title="Reset">Reset</a>: <i>Double</i>
<a href="#resetonserverselectionfail" title="ResetOnServerSelectionFail">ResetOnServerSelectionFail</a>: <i>Double</i>
<a href="#rtpsipcallidmatch" title="RtpSipCallIdMatch">RtpSipCallIdMatch</a>: <i>Double</i>
<a href="#scaleoutbucketcount" title="ScaleoutBucketCount">ScaleoutBucketCount</a>: <i>Double</i>
<a href="#scaleoutdevicegroup" title="ScaleoutDeviceGroup">ScaleoutDeviceGroup</a>: <i>Double</i>
<a href="#secs" title="Secs">Secs</a>: <i>Double</i>
<a href="#servselfail" title="ServSelFail">ServSelFail</a>: <i>Double</i>
<a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>: <i>String</i>
<a href="#sharedpartitioncachetemplate" title="SharedPartitionCacheTemplate">SharedPartitionCacheTemplate</a>: <i>Double</i>
<a href="#sharedpartitionclientssltemplate" title="SharedPartitionClientSslTemplate">SharedPartitionClientSslTemplate</a>: <i>Double</i>
<a href="#sharedpartitionconnectionreusetemplate" title="SharedPartitionConnectionReuseTemplate">SharedPartitionConnectionReuseTemplate</a>: <i>Double</i>
<a href="#sharedpartitiondiametertemplate" title="SharedPartitionDiameterTemplate">SharedPartitionDiameterTemplate</a>: <i>Double</i>
<a href="#sharedpartitiondnstemplate" title="SharedPartitionDnsTemplate">SharedPartitionDnsTemplate</a>: <i>Double</i>
<a href="#sharedpartitiondynamicservicetemplate" title="SharedPartitionDynamicServiceTemplate">SharedPartitionDynamicServiceTemplate</a>: <i>Double</i>
<a href="#sharedpartitionexternalservicetemplate" title="SharedPartitionExternalServiceTemplate">SharedPartitionExternalServiceTemplate</a>: <i>Double</i>
<a href="#sharedpartitionhttppolicytemplate" title="SharedPartitionHttpPolicyTemplate">SharedPartitionHttpPolicyTemplate</a>: <i>Double</i>
<a href="#sharedpartitionhttptemplate" title="SharedPartitionHttpTemplate">SharedPartitionHttpTemplate</a>: <i>Double</i>
<a href="#sharedpartitionpersistcookietemplate" title="SharedPartitionPersistCookieTemplate">SharedPartitionPersistCookieTemplate</a>: <i>Double</i>
<a href="#sharedpartitionpersistdestinationiptemplate" title="SharedPartitionPersistDestinationIpTemplate">SharedPartitionPersistDestinationIpTemplate</a>: <i>Double</i>
<a href="#sharedpartitionpersistsourceiptemplate" title="SharedPartitionPersistSourceIpTemplate">SharedPartitionPersistSourceIpTemplate</a>: <i>Double</i>
<a href="#sharedpartitionpersistsslsidtemplate" title="SharedPartitionPersistSslSidTemplate">SharedPartitionPersistSslSidTemplate</a>: <i>Double</i>
<a href="#sharedpartitionpolicytemplate" title="SharedPartitionPolicyTemplate">SharedPartitionPolicyTemplate</a>: <i>Double</i>
<a href="#sharedpartitionpool" title="SharedPartitionPool">SharedPartitionPool</a>: <i>Double</i>
<a href="#sharedpartitionserverssltemplate" title="SharedPartitionServerSslTemplate">SharedPartitionServerSslTemplate</a>: <i>Double</i>
<a href="#sharedpartitiontcp" title="SharedPartitionTcp">SharedPartitionTcp</a>: <i>Double</i>
<a href="#sharedpartitiontcpproxytemplate" title="SharedPartitionTcpProxyTemplate">SharedPartitionTcpProxyTemplate</a>: <i>Double</i>
<a href="#sharedpartitionudp" title="SharedPartitionUdp">SharedPartitionUdp</a>: <i>Double</i>
<a href="#sharedpartitionvirtualporttemplate" title="SharedPartitionVirtualPortTemplate">SharedPartitionVirtualPortTemplate</a>: <i>Double</i>
<a href="#skiprevhash" title="SkipRevHash">SkipRevHash</a>: <i>Double</i>
<a href="#snatonvip" title="SnatOnVip">SnatOnVip</a>: <i>Double</i>
<a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>: <i>String</i>
<a href="#supporthttp2" title="SupportHttp2">SupportHttp2</a>: <i>Double</i>
<a href="#syncookie" title="SynCookie">SynCookie</a>: <i>Double</i>
<a href="#templatecache" title="TemplateCache">TemplateCache</a>: <i>String</i>
<a href="#templatecacheshared" title="TemplateCacheShared">TemplateCacheShared</a>: <i>String</i>
<a href="#templateclientssh" title="TemplateClientSsh">TemplateClientSsh</a>: <i>String</i>
<a href="#templateclientssl" title="TemplateClientSsl">TemplateClientSsl</a>: <i>String</i>
<a href="#templateclientsslshared" title="TemplateClientSslShared">TemplateClientSslShared</a>: <i>String</i>
<a href="#templateconnectionreuse" title="TemplateConnectionReuse">TemplateConnectionReuse</a>: <i>String</i>
<a href="#templateconnectionreuseshared" title="TemplateConnectionReuseShared">TemplateConnectionReuseShared</a>: <i>String</i>
<a href="#templatedblb" title="TemplateDblb">TemplateDblb</a>: <i>String</i>
<a href="#templatediameter" title="TemplateDiameter">TemplateDiameter</a>: <i>String</i>
<a href="#templatediametershared" title="TemplateDiameterShared">TemplateDiameterShared</a>: <i>String</i>
<a href="#templatedns" title="TemplateDns">TemplateDns</a>: <i>String</i>
<a href="#templatednsshared" title="TemplateDnsShared">TemplateDnsShared</a>: <i>String</i>
<a href="#templatedynamicservice" title="TemplateDynamicService">TemplateDynamicService</a>: <i>String</i>
<a href="#templatedynamicserviceshared" title="TemplateDynamicServiceShared">TemplateDynamicServiceShared</a>: <i>String</i>
<a href="#templateexternalservice" title="TemplateExternalService">TemplateExternalService</a>: <i>String</i>
<a href="#templateexternalserviceshared" title="TemplateExternalServiceShared">TemplateExternalServiceShared</a>: <i>String</i>
<a href="#templatefileinspection" title="TemplateFileInspection">TemplateFileInspection</a>: <i>String</i>
<a href="#templatefix" title="TemplateFix">TemplateFix</a>: <i>String</i>
<a href="#templateftp" title="TemplateFtp">TemplateFtp</a>: <i>String</i>
<a href="#templatehttp" title="TemplateHttp">TemplateHttp</a>: <i>String</i>
<a href="#templatehttppolicy" title="TemplateHttpPolicy">TemplateHttpPolicy</a>: <i>String</i>
<a href="#templatehttppolicyshared" title="TemplateHttpPolicyShared">TemplateHttpPolicyShared</a>: <i>String</i>
<a href="#templatehttpshared" title="TemplateHttpShared">TemplateHttpShared</a>: <i>String</i>
<a href="#templateimappop3" title="TemplateImapPop3">TemplateImapPop3</a>: <i>String</i>
<a href="#templatepersistcookie" title="TemplatePersistCookie">TemplatePersistCookie</a>: <i>String</i>
<a href="#templatepersistcookieshared" title="TemplatePersistCookieShared">TemplatePersistCookieShared</a>: <i>String</i>
<a href="#templatepersistdestinationip" title="TemplatePersistDestinationIp">TemplatePersistDestinationIp</a>: <i>String</i>
<a href="#templatepersistdestinationipshared" title="TemplatePersistDestinationIpShared">TemplatePersistDestinationIpShared</a>: <i>String</i>
<a href="#templatepersistsourceip" title="TemplatePersistSourceIp">TemplatePersistSourceIp</a>: <i>String</i>
<a href="#templatepersistsourceipshared" title="TemplatePersistSourceIpShared">TemplatePersistSourceIpShared</a>: <i>String</i>
<a href="#templatepersistsslsid" title="TemplatePersistSslSid">TemplatePersistSslSid</a>: <i>String</i>
<a href="#templatepersistsslsidshared" title="TemplatePersistSslSidShared">TemplatePersistSslSidShared</a>: <i>String</i>
<a href="#templatepolicy" title="TemplatePolicy">TemplatePolicy</a>: <i>String</i>
<a href="#templatepolicyshared" title="TemplatePolicyShared">TemplatePolicyShared</a>: <i>String</i>
<a href="#templatereqmodicap" title="TemplateReqmodIcap">TemplateReqmodIcap</a>: <i>String</i>
<a href="#templaterespmodicap" title="TemplateRespmodIcap">TemplateRespmodIcap</a>: <i>String</i>
<a href="#templatescaleout" title="TemplateScaleout">TemplateScaleout</a>: <i>String</i>
<a href="#templateserverssh" title="TemplateServerSsh">TemplateServerSsh</a>: <i>String</i>
<a href="#templateserverssl" title="TemplateServerSsl">TemplateServerSsl</a>: <i>String</i>
<a href="#templateserversslshared" title="TemplateServerSslShared">TemplateServerSslShared</a>: <i>String</i>
<a href="#templatesip" title="TemplateSip">TemplateSip</a>: <i>String</i>
<a href="#templatesmpp" title="TemplateSmpp">TemplateSmpp</a>: <i>String</i>
<a href="#templatesmtp" title="TemplateSmtp">TemplateSmtp</a>: <i>String</i>
<a href="#templatessli" title="TemplateSsli">TemplateSsli</a>: <i>String</i>
<a href="#templatetcp" title="TemplateTcp">TemplateTcp</a>: <i>String</i>
<a href="#templatetcpproxy" title="TemplateTcpProxy">TemplateTcpProxy</a>: <i>String</i>
<a href="#templatetcpproxyclient" title="TemplateTcpProxyClient">TemplateTcpProxyClient</a>: <i>String</i>
<a href="#templatetcpproxyserver" title="TemplateTcpProxyServer">TemplateTcpProxyServer</a>: <i>String</i>
<a href="#templatetcpproxyshared" title="TemplateTcpProxyShared">TemplateTcpProxyShared</a>: <i>String</i>
<a href="#templatetcpshared" title="TemplateTcpShared">TemplateTcpShared</a>: <i>String</i>
<a href="#templateudp" title="TemplateUdp">TemplateUdp</a>: <i>String</i>
<a href="#templateudpshared" title="TemplateUdpShared">TemplateUdpShared</a>: <i>String</i>
<a href="#templatevirtualport" title="TemplateVirtualPort">TemplateVirtualPort</a>: <i>String</i>
<a href="#templatevirtualportshared" title="TemplateVirtualPortShared">TemplateVirtualPortShared</a>: <i>String</i>
<a href="#trunkfwd" title="TrunkFwd">TrunkFwd</a>: <i>Double</i>
<a href="#trunkrev" title="TrunkRev">TrunkRev</a>: <i>Double</i>
<a href="#usealternateport" title="UseAlternatePort">UseAlternatePort</a>: <i>Double</i>
<a href="#usecgnv6" title="UseCgnv6">UseCgnv6</a>: <i>Double</i>
<a href="#usedefaultifnoserver" title="UseDefaultIfNoServer">UseDefaultIfNoServer</a>: <i>Double</i>
<a href="#usercvhopforresp" title="UseRcvHopForResp">UseRcvHopForResp</a>: <i>Double</i>
<a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#view" title="View">View</a>: <i>Double</i>
<a href="#waftemplate" title="WafTemplate">WafTemplate</a>: <i>String</i>
<a href="#whendown" title="WhenDown">WhenDown</a>: <i>Double</i>
<a href="#whendownprotocol2" title="WhenDownProtocol2">WhenDownProtocol2</a>: <i>Double</i>
<a href="#aclidlist" title="AclIdList">AclIdList</a>: <i>
      - <a href="aclidlistdefinition.md">AclIdListDefinition</a></i>
<a href="#aclnamelist" title="AclNameList">AclNameList</a>: <i>
      - <a href="aclnamelistdefinition.md">AclNameListDefinition</a></i>
<a href="#aflexscripts" title="AflexScripts">AflexScripts</a>: <i>
      - <a href="aflexscriptsdefinition.md">AflexScriptsDefinition</a></i>
<a href="#authcfg" title="AuthCfg">AuthCfg</a>: <i>
      - <a href="authcfgdefinition.md">AuthCfgDefinition</a></i>
<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>: <i>
      - <a href="samplingenabledefinition.md">SamplingEnableDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AltProtocol1

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AltProtocol2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlternatePort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlternatePortNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Auto

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientipStickyNat

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefSelectionIfPrefFailed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePlayeridCheck

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EthFwd

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EthRev

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expand

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedStats

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceRoutingMode

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GslbEnable

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaConnMirror

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpMapList

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipinip

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Acl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L7HardwareAssist

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageSwitching

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoAutoUpOnAflex

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoDestNat

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoLogging

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnSyn

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptimizationLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pool

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortTranslation

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Precedence

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Range

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectToHttps

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReqFail

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reset

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetOnServerSelectionFail

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RtpSipCallIdMatch

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleoutBucketCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleoutDeviceGroup

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServSelFail

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionCacheTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionClientSslTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionConnectionReuseTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionDiameterTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionDnsTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionDynamicServiceTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionExternalServiceTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionHttpPolicyTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionHttpTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPersistCookieTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPersistDestinationIpTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPersistSourceIpTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPersistSslSidTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPolicyTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPool

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionServerSslTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionTcp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionTcpProxyTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionUdp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionVirtualPortTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipRevHash

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnatOnVip

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatsDataAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportHttp2

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SynCookie

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateCache

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateCacheShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateClientSsh

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateClientSsl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateClientSslShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateConnectionReuse

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateConnectionReuseShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDblb

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDiameter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDiameterShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDnsShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDynamicService

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDynamicServiceShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateExternalService

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateExternalServiceShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateFileInspection

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateFix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateFtp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateHttp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateHttpPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateHttpPolicyShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateHttpShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateImapPop3

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePersistCookie

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePersistCookieShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePersistDestinationIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePersistDestinationIpShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePersistSourceIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePersistSourceIpShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePersistSslSid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePersistSslSidShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePolicyShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateReqmodIcap

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateRespmodIcap

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateScaleout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateServerSsh

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateServerSsl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateServerSslShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateSip

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateSmpp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateSmtp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateSsli

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateTcp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateTcpProxy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateTcpProxyClient

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateTcpProxyServer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateTcpProxyShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateTcpShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateUdp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateUdpShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateVirtualPort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateVirtualPortShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrunkFwd

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrunkRev

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseAlternatePort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCgnv6

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseDefaultIfNoServer

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseRcvHopForResp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### View

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WhenDown

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WhenDownProtocol2

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AclIdList

_Required_: No

_Type_: List of <a href="aclidlistdefinition.md">AclIdListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AclNameList

_Required_: No

_Type_: List of <a href="aclnamelistdefinition.md">AclNameListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AflexScripts

_Required_: No

_Type_: List of <a href="aflexscriptsdefinition.md">AflexScriptsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthCfg

_Required_: No

_Type_: List of <a href="authcfgdefinition.md">AuthCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamplingEnable

_Required_: No

_Type_: List of <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

