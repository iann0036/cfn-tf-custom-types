# TF::Thunder::SlbVirtualServerPort

`thunder_slb_virtual_server_port` Provides details about thunder slb virtual server port

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbVirtualServerPort",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#altprotocol1" title="AltProtocol1">AltProtocol1</a>" : <i>String</i>,
        "<a href="#altprotocol2" title="AltProtocol2">AltProtocol2</a>" : <i>String</i>,
        "<a href="#alternateport" title="AlternatePort">AlternatePort</a>" : <i>Double</i>,
        "<a href="#alternateportnumber" title="AlternatePortNumber">AlternatePortNumber</a>" : <i>Double</i>,
        "<a href="#auto" title="Auto">Auto</a>" : <i>Double</i>,
        "<a href="#clientipstickynat" title="ClientipStickyNat">ClientipStickyNat</a>" : <i>Double</i>,
        "<a href="#connlimit" title="ConnLimit">ConnLimit</a>" : <i>Double</i>,
        "<a href="#cpucompute" title="CpuCompute">CpuCompute</a>" : <i>Double</i>,
        "<a href="#defselectionifpreffailed" title="DefSelectionIfPrefFailed">DefSelectionIfPrefFailed</a>" : <i>String</i>,
        "<a href="#enableplayeridcheck" title="EnablePlayeridCheck">EnablePlayeridCheck</a>" : <i>Double</i>,
        "<a href="#ethfwd" title="EthFwd">EthFwd</a>" : <i>Double</i>,
        "<a href="#ethrev" title="EthRev">EthRev</a>" : <i>Double</i>,
        "<a href="#expand" title="Expand">Expand</a>" : <i>Double</i>,
        "<a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>" : <i>Double</i>,
        "<a href="#forceroutingmode" title="ForceRoutingMode">ForceRoutingMode</a>" : <i>Double</i>,
        "<a href="#gslbenable" title="GslbEnable">GslbEnable</a>" : <i>Double</i>,
        "<a href="#gtpsessionlb" title="GtpSessionLb">GtpSessionLb</a>" : <i>Double</i>,
        "<a href="#haconnmirror" title="HaConnMirror">HaConnMirror</a>" : <i>Double</i>,
        "<a href="#ignoreglobal" title="IgnoreGlobal">IgnoreGlobal</a>" : <i>Double</i>,
        "<a href="#ipmaplist" title="IpMapList">IpMapList</a>" : <i>String</i>,
        "<a href="#ipinip" title="Ipinip">Ipinip</a>" : <i>Double</i>,
        "<a href="#l7hardwareassist" title="L7HardwareAssist">L7HardwareAssist</a>" : <i>Double</i>,
        "<a href="#memorycompute" title="MemoryCompute">MemoryCompute</a>" : <i>Double</i>,
        "<a href="#messageswitching" title="MessageSwitching">MessageSwitching</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#noautouponaflex" title="NoAutoUpOnAflex">NoAutoUpOnAflex</a>" : <i>Double</i>,
        "<a href="#nodestnat" title="NoDestNat">NoDestNat</a>" : <i>Double</i>,
        "<a href="#nologging" title="NoLogging">NoLogging</a>" : <i>Double</i>,
        "<a href="#onsyn" title="OnSyn">OnSyn</a>" : <i>Double</i>,
        "<a href="#optimizationlevel" title="OptimizationLevel">OptimizationLevel</a>" : <i>String</i>,
        "<a href="#ptemplatesipshared" title="PTemplateSipShared">PTemplateSipShared</a>" : <i>Double</i>,
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
        "<a href="#sharedpartitiondblbtemplate" title="SharedPartitionDblbTemplate">SharedPartitionDblbTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitiondiametertemplate" title="SharedPartitionDiameterTemplate">SharedPartitionDiameterTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitiondnstemplate" title="SharedPartitionDnsTemplate">SharedPartitionDnsTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitiondohtemplate" title="SharedPartitionDohTemplate">SharedPartitionDohTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitiondynamicservicetemplate" title="SharedPartitionDynamicServiceTemplate">SharedPartitionDynamicServiceTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitionexternalservicetemplate" title="SharedPartitionExternalServiceTemplate">SharedPartitionExternalServiceTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitionfixtemplate" title="SharedPartitionFixTemplate">SharedPartitionFixTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitionhttppolicytemplate" title="SharedPartitionHttpPolicyTemplate">SharedPartitionHttpPolicyTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitionhttptemplate" title="SharedPartitionHttpTemplate">SharedPartitionHttpTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitionimappop3template" title="SharedPartitionImapPop3Template">SharedPartitionImapPop3Template</a>" : <i>Double</i>,
        "<a href="#sharedpartitionpersistcookietemplate" title="SharedPartitionPersistCookieTemplate">SharedPartitionPersistCookieTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitionpersistdestinationiptemplate" title="SharedPartitionPersistDestinationIpTemplate">SharedPartitionPersistDestinationIpTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitionpersistsourceiptemplate" title="SharedPartitionPersistSourceIpTemplate">SharedPartitionPersistSourceIpTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitionpersistsslsidtemplate" title="SharedPartitionPersistSslSidTemplate">SharedPartitionPersistSslSidTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitionpolicytemplate" title="SharedPartitionPolicyTemplate">SharedPartitionPolicyTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitionpool" title="SharedPartitionPool">SharedPartitionPool</a>" : <i>Double</i>,
        "<a href="#sharedpartitionserverssltemplate" title="SharedPartitionServerSslTemplate">SharedPartitionServerSslTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitionsmpptemplate" title="SharedPartitionSmppTemplate">SharedPartitionSmppTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitionsmtptemplate" title="SharedPartitionSmtpTemplate">SharedPartitionSmtpTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitiontcp" title="SharedPartitionTcp">SharedPartitionTcp</a>" : <i>Double</i>,
        "<a href="#sharedpartitiontcpproxytemplate" title="SharedPartitionTcpProxyTemplate">SharedPartitionTcpProxyTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitionudp" title="SharedPartitionUdp">SharedPartitionUdp</a>" : <i>Double</i>,
        "<a href="#sharedpartitionvirtualporttemplate" title="SharedPartitionVirtualPortTemplate">SharedPartitionVirtualPortTemplate</a>" : <i>Double</i>,
        "<a href="#skiprevhash" title="SkipRevHash">SkipRevHash</a>" : <i>Double</i>,
        "<a href="#snatonvip" title="SnatOnVip">SnatOnVip</a>" : <i>Double</i>,
        "<a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>" : <i>String</i>,
        "<a href="#substitutesourcemac" title="SubstituteSourceMac">SubstituteSourceMac</a>" : <i>Double</i>,
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
        "<a href="#templatedblbshared" title="TemplateDblbShared">TemplateDblbShared</a>" : <i>String</i>,
        "<a href="#templatediameter" title="TemplateDiameter">TemplateDiameter</a>" : <i>String</i>,
        "<a href="#templatediametershared" title="TemplateDiameterShared">TemplateDiameterShared</a>" : <i>String</i>,
        "<a href="#templatedns" title="TemplateDns">TemplateDns</a>" : <i>String</i>,
        "<a href="#templatednsshared" title="TemplateDnsShared">TemplateDnsShared</a>" : <i>String</i>,
        "<a href="#templatedoh" title="TemplateDoh">TemplateDoh</a>" : <i>String</i>,
        "<a href="#templatedohshared" title="TemplateDohShared">TemplateDohShared</a>" : <i>String</i>,
        "<a href="#templatedynamicservice" title="TemplateDynamicService">TemplateDynamicService</a>" : <i>String</i>,
        "<a href="#templatedynamicserviceshared" title="TemplateDynamicServiceShared">TemplateDynamicServiceShared</a>" : <i>String</i>,
        "<a href="#templateexternalservice" title="TemplateExternalService">TemplateExternalService</a>" : <i>String</i>,
        "<a href="#templateexternalserviceshared" title="TemplateExternalServiceShared">TemplateExternalServiceShared</a>" : <i>String</i>,
        "<a href="#templatefileinspection" title="TemplateFileInspection">TemplateFileInspection</a>" : <i>String</i>,
        "<a href="#templatefix" title="TemplateFix">TemplateFix</a>" : <i>String</i>,
        "<a href="#templatefixshared" title="TemplateFixShared">TemplateFixShared</a>" : <i>String</i>,
        "<a href="#templateftp" title="TemplateFtp">TemplateFtp</a>" : <i>String</i>,
        "<a href="#templatehttp" title="TemplateHttp">TemplateHttp</a>" : <i>String</i>,
        "<a href="#templatehttppolicy" title="TemplateHttpPolicy">TemplateHttpPolicy</a>" : <i>String</i>,
        "<a href="#templatehttppolicyshared" title="TemplateHttpPolicyShared">TemplateHttpPolicyShared</a>" : <i>String</i>,
        "<a href="#templatehttpshared" title="TemplateHttpShared">TemplateHttpShared</a>" : <i>String</i>,
        "<a href="#templateimappop3" title="TemplateImapPop3">TemplateImapPop3</a>" : <i>String</i>,
        "<a href="#templateimappop3shared" title="TemplateImapPop3Shared">TemplateImapPop3Shared</a>" : <i>String</i>,
        "<a href="#templatemqtt" title="TemplateMqtt">TemplateMqtt</a>" : <i>String</i>,
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
        "<a href="#templatesipshared" title="TemplateSipShared">TemplateSipShared</a>" : <i>String</i>,
        "<a href="#templatesmpp" title="TemplateSmpp">TemplateSmpp</a>" : <i>String</i>,
        "<a href="#templatesmppshared" title="TemplateSmppShared">TemplateSmppShared</a>" : <i>String</i>,
        "<a href="#templatesmtp" title="TemplateSmtp">TemplateSmtp</a>" : <i>String</i>,
        "<a href="#templatesmtpshared" title="TemplateSmtpShared">TemplateSmtpShared</a>" : <i>String</i>,
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
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbVirtualServerPort
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#altprotocol1" title="AltProtocol1">AltProtocol1</a>: <i>String</i>
    <a href="#altprotocol2" title="AltProtocol2">AltProtocol2</a>: <i>String</i>
    <a href="#alternateport" title="AlternatePort">AlternatePort</a>: <i>Double</i>
    <a href="#alternateportnumber" title="AlternatePortNumber">AlternatePortNumber</a>: <i>Double</i>
    <a href="#auto" title="Auto">Auto</a>: <i>Double</i>
    <a href="#clientipstickynat" title="ClientipStickyNat">ClientipStickyNat</a>: <i>Double</i>
    <a href="#connlimit" title="ConnLimit">ConnLimit</a>: <i>Double</i>
    <a href="#cpucompute" title="CpuCompute">CpuCompute</a>: <i>Double</i>
    <a href="#defselectionifpreffailed" title="DefSelectionIfPrefFailed">DefSelectionIfPrefFailed</a>: <i>String</i>
    <a href="#enableplayeridcheck" title="EnablePlayeridCheck">EnablePlayeridCheck</a>: <i>Double</i>
    <a href="#ethfwd" title="EthFwd">EthFwd</a>: <i>Double</i>
    <a href="#ethrev" title="EthRev">EthRev</a>: <i>Double</i>
    <a href="#expand" title="Expand">Expand</a>: <i>Double</i>
    <a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>: <i>Double</i>
    <a href="#forceroutingmode" title="ForceRoutingMode">ForceRoutingMode</a>: <i>Double</i>
    <a href="#gslbenable" title="GslbEnable">GslbEnable</a>: <i>Double</i>
    <a href="#gtpsessionlb" title="GtpSessionLb">GtpSessionLb</a>: <i>Double</i>
    <a href="#haconnmirror" title="HaConnMirror">HaConnMirror</a>: <i>Double</i>
    <a href="#ignoreglobal" title="IgnoreGlobal">IgnoreGlobal</a>: <i>Double</i>
    <a href="#ipmaplist" title="IpMapList">IpMapList</a>: <i>String</i>
    <a href="#ipinip" title="Ipinip">Ipinip</a>: <i>Double</i>
    <a href="#l7hardwareassist" title="L7HardwareAssist">L7HardwareAssist</a>: <i>Double</i>
    <a href="#memorycompute" title="MemoryCompute">MemoryCompute</a>: <i>Double</i>
    <a href="#messageswitching" title="MessageSwitching">MessageSwitching</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#noautouponaflex" title="NoAutoUpOnAflex">NoAutoUpOnAflex</a>: <i>Double</i>
    <a href="#nodestnat" title="NoDestNat">NoDestNat</a>: <i>Double</i>
    <a href="#nologging" title="NoLogging">NoLogging</a>: <i>Double</i>
    <a href="#onsyn" title="OnSyn">OnSyn</a>: <i>Double</i>
    <a href="#optimizationlevel" title="OptimizationLevel">OptimizationLevel</a>: <i>String</i>
    <a href="#ptemplatesipshared" title="PTemplateSipShared">PTemplateSipShared</a>: <i>Double</i>
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
    <a href="#sharedpartitiondblbtemplate" title="SharedPartitionDblbTemplate">SharedPartitionDblbTemplate</a>: <i>Double</i>
    <a href="#sharedpartitiondiametertemplate" title="SharedPartitionDiameterTemplate">SharedPartitionDiameterTemplate</a>: <i>Double</i>
    <a href="#sharedpartitiondnstemplate" title="SharedPartitionDnsTemplate">SharedPartitionDnsTemplate</a>: <i>Double</i>
    <a href="#sharedpartitiondohtemplate" title="SharedPartitionDohTemplate">SharedPartitionDohTemplate</a>: <i>Double</i>
    <a href="#sharedpartitiondynamicservicetemplate" title="SharedPartitionDynamicServiceTemplate">SharedPartitionDynamicServiceTemplate</a>: <i>Double</i>
    <a href="#sharedpartitionexternalservicetemplate" title="SharedPartitionExternalServiceTemplate">SharedPartitionExternalServiceTemplate</a>: <i>Double</i>
    <a href="#sharedpartitionfixtemplate" title="SharedPartitionFixTemplate">SharedPartitionFixTemplate</a>: <i>Double</i>
    <a href="#sharedpartitionhttppolicytemplate" title="SharedPartitionHttpPolicyTemplate">SharedPartitionHttpPolicyTemplate</a>: <i>Double</i>
    <a href="#sharedpartitionhttptemplate" title="SharedPartitionHttpTemplate">SharedPartitionHttpTemplate</a>: <i>Double</i>
    <a href="#sharedpartitionimappop3template" title="SharedPartitionImapPop3Template">SharedPartitionImapPop3Template</a>: <i>Double</i>
    <a href="#sharedpartitionpersistcookietemplate" title="SharedPartitionPersistCookieTemplate">SharedPartitionPersistCookieTemplate</a>: <i>Double</i>
    <a href="#sharedpartitionpersistdestinationiptemplate" title="SharedPartitionPersistDestinationIpTemplate">SharedPartitionPersistDestinationIpTemplate</a>: <i>Double</i>
    <a href="#sharedpartitionpersistsourceiptemplate" title="SharedPartitionPersistSourceIpTemplate">SharedPartitionPersistSourceIpTemplate</a>: <i>Double</i>
    <a href="#sharedpartitionpersistsslsidtemplate" title="SharedPartitionPersistSslSidTemplate">SharedPartitionPersistSslSidTemplate</a>: <i>Double</i>
    <a href="#sharedpartitionpolicytemplate" title="SharedPartitionPolicyTemplate">SharedPartitionPolicyTemplate</a>: <i>Double</i>
    <a href="#sharedpartitionpool" title="SharedPartitionPool">SharedPartitionPool</a>: <i>Double</i>
    <a href="#sharedpartitionserverssltemplate" title="SharedPartitionServerSslTemplate">SharedPartitionServerSslTemplate</a>: <i>Double</i>
    <a href="#sharedpartitionsmpptemplate" title="SharedPartitionSmppTemplate">SharedPartitionSmppTemplate</a>: <i>Double</i>
    <a href="#sharedpartitionsmtptemplate" title="SharedPartitionSmtpTemplate">SharedPartitionSmtpTemplate</a>: <i>Double</i>
    <a href="#sharedpartitiontcp" title="SharedPartitionTcp">SharedPartitionTcp</a>: <i>Double</i>
    <a href="#sharedpartitiontcpproxytemplate" title="SharedPartitionTcpProxyTemplate">SharedPartitionTcpProxyTemplate</a>: <i>Double</i>
    <a href="#sharedpartitionudp" title="SharedPartitionUdp">SharedPartitionUdp</a>: <i>Double</i>
    <a href="#sharedpartitionvirtualporttemplate" title="SharedPartitionVirtualPortTemplate">SharedPartitionVirtualPortTemplate</a>: <i>Double</i>
    <a href="#skiprevhash" title="SkipRevHash">SkipRevHash</a>: <i>Double</i>
    <a href="#snatonvip" title="SnatOnVip">SnatOnVip</a>: <i>Double</i>
    <a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>: <i>String</i>
    <a href="#substitutesourcemac" title="SubstituteSourceMac">SubstituteSourceMac</a>: <i>Double</i>
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
    <a href="#templatedblbshared" title="TemplateDblbShared">TemplateDblbShared</a>: <i>String</i>
    <a href="#templatediameter" title="TemplateDiameter">TemplateDiameter</a>: <i>String</i>
    <a href="#templatediametershared" title="TemplateDiameterShared">TemplateDiameterShared</a>: <i>String</i>
    <a href="#templatedns" title="TemplateDns">TemplateDns</a>: <i>String</i>
    <a href="#templatednsshared" title="TemplateDnsShared">TemplateDnsShared</a>: <i>String</i>
    <a href="#templatedoh" title="TemplateDoh">TemplateDoh</a>: <i>String</i>
    <a href="#templatedohshared" title="TemplateDohShared">TemplateDohShared</a>: <i>String</i>
    <a href="#templatedynamicservice" title="TemplateDynamicService">TemplateDynamicService</a>: <i>String</i>
    <a href="#templatedynamicserviceshared" title="TemplateDynamicServiceShared">TemplateDynamicServiceShared</a>: <i>String</i>
    <a href="#templateexternalservice" title="TemplateExternalService">TemplateExternalService</a>: <i>String</i>
    <a href="#templateexternalserviceshared" title="TemplateExternalServiceShared">TemplateExternalServiceShared</a>: <i>String</i>
    <a href="#templatefileinspection" title="TemplateFileInspection">TemplateFileInspection</a>: <i>String</i>
    <a href="#templatefix" title="TemplateFix">TemplateFix</a>: <i>String</i>
    <a href="#templatefixshared" title="TemplateFixShared">TemplateFixShared</a>: <i>String</i>
    <a href="#templateftp" title="TemplateFtp">TemplateFtp</a>: <i>String</i>
    <a href="#templatehttp" title="TemplateHttp">TemplateHttp</a>: <i>String</i>
    <a href="#templatehttppolicy" title="TemplateHttpPolicy">TemplateHttpPolicy</a>: <i>String</i>
    <a href="#templatehttppolicyshared" title="TemplateHttpPolicyShared">TemplateHttpPolicyShared</a>: <i>String</i>
    <a href="#templatehttpshared" title="TemplateHttpShared">TemplateHttpShared</a>: <i>String</i>
    <a href="#templateimappop3" title="TemplateImapPop3">TemplateImapPop3</a>: <i>String</i>
    <a href="#templateimappop3shared" title="TemplateImapPop3Shared">TemplateImapPop3Shared</a>: <i>String</i>
    <a href="#templatemqtt" title="TemplateMqtt">TemplateMqtt</a>: <i>String</i>
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
    <a href="#templatesipshared" title="TemplateSipShared">TemplateSipShared</a>: <i>String</i>
    <a href="#templatesmpp" title="TemplateSmpp">TemplateSmpp</a>: <i>String</i>
    <a href="#templatesmppshared" title="TemplateSmppShared">TemplateSmppShared</a>: <i>String</i>
    <a href="#templatesmtp" title="TemplateSmtp">TemplateSmtp</a>: <i>String</i>
    <a href="#templatesmtpshared" title="TemplateSmtpShared">TemplateSmtpShared</a>: <i>String</i>
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

‘enable’: Enable; ‘disable’: Disable;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AltProtocol1

‘http’: HTTP Port;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AltProtocol2

‘tcp’: TCP LB service;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlternatePort

Alternate Virtual Port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlternatePortNumber

Virtual Port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Auto

Configure auto NAT for the vport.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientipStickyNat

Prefer to use same source NAT address for a client.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnLimit

Connection Limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuCompute

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefSelectionIfPrefFailed

‘def-selection-if-pref-failed’: Use default server selection method if prefer method failed; ‘def-selection-if-pref-failed-disable’: Stop using default server selection method if prefer method failed;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePlayeridCheck

Enable playerid checks on UDP packets once the AX is in active mode.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EthFwd

Ethernet interface number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EthRev

Ethernet interface number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expand

expand syn-cookie with timestamp and wscale.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedStats

Enable extended statistics on virtual port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceRoutingMode

Force routing mode.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GslbEnable

Enable Global Server Load Balancing.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GtpSessionLb

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaConnMirror

Enable for HA Conn sync.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreGlobal

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpMapList

Enter name of IP Map List to be bound (IP Map List Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipinip

Enable IP in IP.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L7HardwareAssist

FPGA assist L7 packet parsing.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryCompute

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageSwitching

Message switching.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

SLB Virtual Service Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoAutoUpOnAflex

Don’t automatically mark vport up when aFleX is bound.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoDestNat

Disable destination NAT, this option only supports in wildcard VIP or when a connection is operated in SSLi + EP mode.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoLogging

Do not log connection over limit event.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnSyn

Enable for HA Conn sync for l4 tcp sessions on SYN.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptimizationLevel

‘0’: No optimization; ‘1’: Optimization level 1 (Experimental);.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PTemplateSipShared

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistType

‘src-dst-ip-swap-persist’: Create persist session after source IP and destination IP swap; ‘use-src-ip-for-dst-persist’: Use the source IP to create a destination persist session; ‘use-dst-ip-for-src-persist’: Use the destination IP to create source IP persist session;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pool

Specify NAT pool or pool group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolShared

Specify NAT pool or pool group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortNumber

Port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortTranslation

Enable port translation under no-dest-nat.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Precedence

Set auto NAT pool as higher precedence for source NAT.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

‘tcp’: TCP LB service; ‘udp’: UDP Port; ‘others’: for no tcp/udp protocol, do IP load balancing; ‘diameter’: diameter port; ‘dns-tcp’: DNS service over TCP; ‘dns-udp’: DNS service over UDP; ‘fast-http’: Fast HTTP Port; ‘fix’: FIX Port; ‘ftp’: File Transfer Protocol Port; ‘ftp-proxy’: ftp proxy port; ‘http’: HTTP Port; ‘https’: HTTPS port; ‘imap’: imap proxy port; ‘mlb’: Message based load balancing; ‘mms’: Microsoft Multimedia Service Port; ‘mysql’: mssql port; ‘mssql’: mssql; ‘pop3’: pop3 proxy port; ‘radius’: RADIUS Port; ‘rtsp’: Real Time Streaming Protocol Port; ‘sip’: Session initiation protocol over UDP; ‘sip-tcp’: Session initiation protocol over TCP; ‘sips’: Session initiation protocol over TLS; ‘smpp-tcp’: SMPP service over TCP; ‘spdy’: spdy port; ‘spdys’: spdys port; ‘smtp’: SMTP Port; ‘ssl-proxy’: Generic SSL proxy; ‘ssli’: SSL insight; ‘tcp-proxy’: Generic TCP proxy; ‘tftp’: TFTP Port;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Range

Virtual Port range (Virtual Port range value).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rate

Specify the log message rate.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectToHttps

Redirect HTTP to HTTPS.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReqFail

Use alternate virtual port when L7 request fail.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reset

Send client reset when connection number over limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetOnServerSelectionFail

Send client reset when server selection fails.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RtpSipCallIdMatch

rtp traffic try to match the real server of sip smp call-id session.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleoutBucketCount

Number of traffic buckets.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleoutDeviceGroup

Device group id.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secs

Specify the interval in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServSelFail

Use alternate virtual port when server selection failure.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroup

Bind a Service Group to this Virtual Server (Service Group Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionCacheTemplate

Reference a Cache template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionClientSslTemplate

Reference a Client SSL template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionConnectionReuseTemplate

Reference a connection reuse template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionDblbTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionDiameterTemplate

Reference a Diameter template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionDnsTemplate

Reference a dns template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionDohTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionDynamicServiceTemplate

Reference a dynamic service template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionExternalServiceTemplate

Reference a external service template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionFixTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionHttpPolicyTemplate

Reference a http policy template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionHttpTemplate

Reference a HTTP template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionImapPop3Template

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPersistCookieTemplate

Reference a persist cookie template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPersistDestinationIpTemplate

Reference a persist destination ip template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPersistSourceIpTemplate

Reference a persist source ip template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPersistSslSidTemplate

Reference a persist SSL SID template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPolicyTemplate

Reference a policy template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPool

Specify NAT pool or pool group from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionServerSslTemplate

Reference a SSL Server template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionSmppTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionSmtpTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionTcp

Reference a tcp template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionTcpProxyTemplate

Reference a TCP Proxy template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionUdp

Reference a UDP template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionVirtualPortTemplate

Reference a Virtual Port template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipRevHash

Skip rev tuple hash insertion.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnatOnVip

Enable source NAT traffic against VIP.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatsDataAction

‘stats-data-enable’: Enable statistical data collection for virtual port; ‘stats-data-disable’: Disable statistical data collection for virtual port;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubstituteSourceMac

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportHttp2

Support HTTP2.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SynCookie

Enable syn-cookie.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateCache

RAM caching template (Cache Template Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateCacheShared

Cache Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateClientSsh

Client SSH Template (Client SSH Config Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateClientSsl

Client SSL Template (Client SSL Config Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateClientSslShared

Client SSL Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateConnectionReuse

Connection Reuse Template (Connection Reuse Template Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateConnectionReuseShared

Connection Reuse Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDblb

DBLB Template (DBLB template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDblbShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDiameter

Diameter Template (diameter template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDiameterShared

Diameter Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDns

DNS template (DNS template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDnsShared

DNS Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDoh

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDohShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDynamicService

Dynamic Service Template (dynamic-service template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDynamicServiceShared

Dynamic Service Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateExternalService

External service template (external-service template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateExternalServiceShared

External Service Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateFileInspection

File Inspection service template (file-inspection template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateFix

FIX template (FIX Template Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateFixShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateFtp

FTP port template (Ftp template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateHttp

HTTP Template (HTTP Config Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateHttpPolicy

http-policy template (http-policy template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateHttpPolicyShared

Http Policy Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateHttpShared

HTTP Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateImapPop3

IMAP/POP3 Template (IMAP/POP3 Config Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateImapPop3Shared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateMqtt

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePersistCookie

Cookie persistence (Cookie persistence template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePersistCookieShared

Cookie Persistence Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePersistDestinationIp

Destination IP persistence (Destination IP persistence template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePersistDestinationIpShared

Destination IP Persistence Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePersistSourceIp

Source IP persistence (Source IP persistence template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePersistSourceIpShared

Source IP Persistence Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePersistSslSid

SSL session ID persistence (Source IP Persistence Config name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePersistSslSidShared

SSL SID Persistence Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePolicy

Policy Template (Policy template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePolicyShared

Policy Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateReqmodIcap

ICAP reqmod template (reqmod-icap template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateRespmodIcap

ICAP respmod service template (respmod-icap template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateScaleout

Scaleout template (Scaleout template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateServerSsh

Server SSH Template (Server SSH Config Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateServerSsl

Server Side SSL Template (Server SSL Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateServerSslShared

Server SSL Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateSip

SIP template.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateSipShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateSmpp

SMPP template.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateSmppShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateSmtp

SMTP Template (SMTP Config Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateSmtpShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateSsli

SSLi template (SSLi Template Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateTcp

L4 TCP Template (TCP Config Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateTcpProxy

TCP Proxy Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateTcpProxyClient

TCP Proxy Config Client (TCP Proxy Config name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateTcpProxyServer

TCP Proxy Config Server (TCP Proxy Config name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateTcpProxyShared

TCP Proxy Template name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateTcpShared

TCP Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateUdp

L4 UDP Template (UDP Config Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateUdpShared

UDP Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateVirtualPort

Virtual port template (Virtual port template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateVirtualPortShared

Virtual Port Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrunkFwd

Trunk interface number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrunkRev

Trunk interface number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseAlternatePort

Use alternate virtual port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCgnv6

Follow CGNv6 source NAT configuration.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseDefaultIfNoServer

Use default forwarding if server selection failed.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseRcvHopForResp

Use receive hop for response to client(For packets on default-vlan, also config “vlan-global enable-def-vlan-l2-forwarding”.).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### View

Specify a GSLB View (ID).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafTemplate

WAF template (WAF Template Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WhenDown

Use alternate virtual port when down.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WhenDownProtocol2

Use alternate virtual port when down.

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

