# TF::AVI::Seproperties SeRuntimePropertiesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adminsshenabled" title="AdminSshEnabled">AdminSshEnabled</a>" : <i>Boolean</i>,
    "<a href="#baremetaldispatcherhandlesflows" title="BaremetalDispatcherHandlesFlows">BaremetalDispatcherHandlesFlows</a>" : <i>Boolean</i>,
    "<a href="#connectionslossylogratelimiterthreshold" title="ConnectionsLossyLogRateLimiterThreshold">ConnectionsLossyLogRateLimiterThreshold</a>" : <i>Double</i>,
    "<a href="#connectionsudfnflogratelimiterthreshold" title="ConnectionsUdfnfLogRateLimiterThreshold">ConnectionsUdfnfLogRateLimiterThreshold</a>" : <i>Double</i>,
    "<a href="#disableflowprobes" title="DisableFlowProbes">DisableFlowProbes</a>" : <i>Boolean</i>,
    "<a href="#downstreamsendtimeout" title="DownstreamSendTimeout">DownstreamSendTimeout</a>" : <i>Double</i>,
    "<a href="#dpaggressivehbfrequency" title="DpAggressiveHbFrequency">DpAggressiveHbFrequency</a>" : <i>Double</i>,
    "<a href="#dpaggressivehbtimeoutcount" title="DpAggressiveHbTimeoutCount">DpAggressiveHbTimeoutCount</a>" : <i>Double</i>,
    "<a href="#dphbfrequency" title="DpHbFrequency">DpHbFrequency</a>" : <i>Double</i>,
    "<a href="#dphbtimeoutcount" title="DpHbTimeoutCount">DpHbTimeoutCount</a>" : <i>Double</i>,
    "<a href="#dupipfrequency" title="DupipFrequency">DupipFrequency</a>" : <i>Double</i>,
    "<a href="#dupiptimeoutcount" title="DupipTimeoutCount">DupipTimeoutCount</a>" : <i>Double</i>,
    "<a href="#enablehsmlog" title="EnableHsmLog">EnableHsmLog</a>" : <i>Boolean</i>,
    "<a href="#feproxyvipsenableproxyarp" title="FeproxyVipsEnableProxyArp">FeproxyVipsEnableProxyArp</a>" : <i>Boolean</i>,
    "<a href="#flowtablebatchpushfrequency" title="FlowTableBatchPushFrequency">FlowTableBatchPushFrequency</a>" : <i>Double</i>,
    "<a href="#globalmtu" title="GlobalMtu">GlobalMtu</a>" : <i>Double</i>,
    "<a href="#httprumconsolelog" title="HttpRumConsoleLog">HttpRumConsoleLog</a>" : <i>Boolean</i>,
    "<a href="#httprummincontentlength" title="HttpRumMinContentLength">HttpRumMinContentLength</a>" : <i>Double</i>,
    "<a href="#lbactionnumrequeststodispatch" title="LbactionNumRequestsToDispatch">LbactionNumRequestsToDispatch</a>" : <i>Double</i>,
    "<a href="#lbactionrqperrequestmaxretries" title="LbactionRqPerRequestMaxRetries">LbactionRqPerRequestMaxRetries</a>" : <i>Double</i>,
    "<a href="#logagentcompresslogs" title="LogAgentCompressLogs">LogAgentCompressLogs</a>" : <i>Boolean</i>,
    "<a href="#logagentconnsendbuffersize" title="LogAgentConnSendBufferSize">LogAgentConnSendBufferSize</a>" : <i>Double</i>,
    "<a href="#logagentexportmsgbuffersize" title="LogAgentExportMsgBufferSize">LogAgentExportMsgBufferSize</a>" : <i>Double</i>,
    "<a href="#logagentexportwaittime" title="LogAgentExportWaitTime">LogAgentExportWaitTime</a>" : <i>Double</i>,
    "<a href="#logagentfileszappl" title="LogAgentFileSzAppl">LogAgentFileSzAppl</a>" : <i>Double</i>,
    "<a href="#logagentfileszconn" title="LogAgentFileSzConn">LogAgentFileSzConn</a>" : <i>Double</i>,
    "<a href="#logagentfileszdebug" title="LogAgentFileSzDebug">LogAgentFileSzDebug</a>" : <i>Double</i>,
    "<a href="#logagentfileszevent" title="LogAgentFileSzEvent">LogAgentFileSzEvent</a>" : <i>Double</i>,
    "<a href="#logagentlogstorageminsz" title="LogAgentLogStorageMinSz">LogAgentLogStorageMinSz</a>" : <i>Double</i>,
    "<a href="#logagentmaxactiveadffilespervs" title="LogAgentMaxActiveAdfFilesPerVs">LogAgentMaxActiveAdfFilesPerVs</a>" : <i>Double</i>,
    "<a href="#logagentmaxconcurrentrsync" title="LogAgentMaxConcurrentRsync">LogAgentMaxConcurrentRsync</a>" : <i>Double</i>,
    "<a href="#logagentmaxlogmessageprotosz" title="LogAgentMaxLogmessageProtoSz">LogAgentMaxLogmessageProtoSz</a>" : <i>Double</i>,
    "<a href="#logagentmaxstorageexcesspercent" title="LogAgentMaxStorageExcessPercent">LogAgentMaxStorageExcessPercent</a>" : <i>Double</i>,
    "<a href="#logagentmaxstorageignorepercent" title="LogAgentMaxStorageIgnorePercent">LogAgentMaxStorageIgnorePercent</a>" : <i>Double</i>,
    "<a href="#logagentminstoragepervs" title="LogAgentMinStoragePerVs">LogAgentMinStoragePerVs</a>" : <i>Double</i>,
    "<a href="#logagentpauseinterval" title="LogAgentPauseInterval">LogAgentPauseInterval</a>" : <i>Double</i>,
    "<a href="#logagentsleepinterval" title="LogAgentSleepInterval">LogAgentSleepInterval</a>" : <i>Double</i>,
    "<a href="#logagentunknownvstimer" title="LogAgentUnknownVsTimer">LogAgentUnknownVsTimer</a>" : <i>Double</i>,
    "<a href="#logmessagemaxfilelistsize" title="LogMessageMaxFileListSize">LogMessageMaxFileListSize</a>" : <i>Double</i>,
    "<a href="#mcacheenabled" title="McacheEnabled">McacheEnabled</a>" : <i>Boolean</i>,
    "<a href="#mcachefetchenabled" title="McacheFetchEnabled">McacheFetchEnabled</a>" : <i>Boolean</i>,
    "<a href="#mcachestoreinenabled" title="McacheStoreInEnabled">McacheStoreInEnabled</a>" : <i>Boolean</i>,
    "<a href="#mcachestoreinmaxsize" title="McacheStoreInMaxSize">McacheStoreInMaxSize</a>" : <i>Double</i>,
    "<a href="#mcachestoreinminsize" title="McacheStoreInMinSize">McacheStoreInMinSize</a>" : <i>Double</i>,
    "<a href="#mcachestoreoutenabled" title="McacheStoreOutEnabled">McacheStoreOutEnabled</a>" : <i>Boolean</i>,
    "<a href="#ngxfreeconnectionstack" title="NgxFreeConnectionStack">NgxFreeConnectionStack</a>" : <i>Boolean</i>,
    "<a href="#persistencememmax" title="PersistenceMemMax">PersistenceMemMax</a>" : <i>Double</i>,
    "<a href="#scaleoutudpperpkt" title="ScaleoutUdpPerPkt">ScaleoutUdpPerPkt</a>" : <i>Boolean</i>,
    "<a href="#seauthldapbindtimeout" title="SeAuthLdapBindTimeout">SeAuthLdapBindTimeout</a>" : <i>Double</i>,
    "<a href="#seauthldapcachesize" title="SeAuthLdapCacheSize">SeAuthLdapCacheSize</a>" : <i>Double</i>,
    "<a href="#seauthldapconnecttimeout" title="SeAuthLdapConnectTimeout">SeAuthLdapConnectTimeout</a>" : <i>Double</i>,
    "<a href="#seauthldapconnsperserver" title="SeAuthLdapConnsPerServer">SeAuthLdapConnsPerServer</a>" : <i>Double</i>,
    "<a href="#seauthldapreconnecttimeout" title="SeAuthLdapReconnectTimeout">SeAuthLdapReconnectTimeout</a>" : <i>Double</i>,
    "<a href="#seauthldaprequesttimeout" title="SeAuthLdapRequestTimeout">SeAuthLdapRequestTimeout</a>" : <i>Double</i>,
    "<a href="#seauthldapserversfailoveronly" title="SeAuthLdapServersFailoverOnly">SeAuthLdapServersFailoverOnly</a>" : <i>Boolean</i>,
    "<a href="#sedphmdrops" title="SeDpHmDrops">SeDpHmDrops</a>" : <i>Double</i>,
    "<a href="#sedpifstatepollinterval" title="SeDpIfStatePollInterval">SeDpIfStatePollInterval</a>" : <i>Double</i>,
    "<a href="#sedplognfenqueuepercent" title="SeDpLogNfEnqueuePercent">SeDpLogNfEnqueuePercent</a>" : <i>Double</i>,
    "<a href="#sedplogudfenqueuepercent" title="SeDpLogUdfEnqueuePercent">SeDpLogUdfEnqueuePercent</a>" : <i>Double</i>,
    "<a href="#sedumpcoreonassert" title="SeDumpCoreOnAssert">SeDumpCoreOnAssert</a>" : <i>Boolean</i>,
    "<a href="#sehandleinterfaceroutes" title="SeHandleInterfaceRoutes">SeHandleInterfaceRoutes</a>" : <i>Boolean</i>,
    "<a href="#sehbpersistfudgebits" title="SeHbPersistFudgeBits">SeHbPersistFudgeBits</a>" : <i>Double</i>,
    "<a href="#semacerrorthresholdtodisablepromiscious" title="SeMacErrorThresholdToDisablePromiscious">SeMacErrorThresholdToDisablePromiscious</a>" : <i>Double</i>,
    "<a href="#sememorypoison" title="SeMemoryPoison">SeMemoryPoison</a>" : <i>Boolean</i>,
    "<a href="#semetricsinterval" title="SeMetricsInterval">SeMetricsInterval</a>" : <i>Double</i>,
    "<a href="#semetricsrtenabled" title="SeMetricsRtEnabled">SeMetricsRtEnabled</a>" : <i>Boolean</i>,
    "<a href="#semetricsrtinterval" title="SeMetricsRtInterval">SeMetricsRtInterval</a>" : <i>Double</i>,
    "<a href="#sepacketbuffermax" title="SePacketBufferMax">SePacketBufferMax</a>" : <i>Double</i>,
    "<a href="#serandomtcpdrops" title="SeRandomTcpDrops">SeRandomTcpDrops</a>" : <i>Boolean</i>,
    "<a href="#servicesaccessibleallinterfaces" title="ServicesAccessibleAllInterfaces">ServicesAccessibleAllInterfaces</a>" : <i>Boolean</i>,
    "<a href="#spdyfwdproxyparseenable" title="SpdyFwdProxyParseEnable">SpdyFwdProxyParseEnable</a>" : <i>Boolean</i>,
    "<a href="#tcpsyncachemaxretransmitdefault" title="TcpSyncacheMaxRetransmitDefault">TcpSyncacheMaxRetransmitDefault</a>" : <i>Double</i>,
    "<a href="#upstreamconnecttimeout" title="UpstreamConnectTimeout">UpstreamConnectTimeout</a>" : <i>Double</i>,
    "<a href="#upstreamconnpoolcachethresh" title="UpstreamConnpoolCacheThresh">UpstreamConnpoolCacheThresh</a>" : <i>Double</i>,
    "<a href="#upstreamconnpoolconnidlethreshtmo" title="UpstreamConnpoolConnIdleThreshTmo">UpstreamConnpoolConnIdleThreshTmo</a>" : <i>Double</i>,
    "<a href="#upstreamconnpoolcoremaxcache" title="UpstreamConnpoolCoreMaxCache">UpstreamConnpoolCoreMaxCache</a>" : <i>Double</i>,
    "<a href="#upstreamconnpoolenable" title="UpstreamConnpoolEnable">UpstreamConnpoolEnable</a>" : <i>Boolean</i>,
    "<a href="#upstreamconnpoolstrategy" title="UpstreamConnpoolStrategy">UpstreamConnpoolStrategy</a>" : <i>Double</i>,
    "<a href="#upstreamkeepalive" title="UpstreamKeepalive">UpstreamKeepalive</a>" : <i>Boolean</i>,
    "<a href="#upstreamreadtimeout" title="UpstreamReadTimeout">UpstreamReadTimeout</a>" : <i>Double</i>,
    "<a href="#upstreamsendtimeout" title="UpstreamSendTimeout">UpstreamSendTimeout</a>" : <i>Double</i>,
    "<a href="#userdefinedmetricage" title="UserDefinedMetricAge">UserDefinedMetricAge</a>" : <i>Double</i>,
    "<a href="#appheaders" title="AppHeaders">AppHeaders</a>" : <i>[ <a href="appheadersdefinition.md">AppHeadersDefinition</a>, ... ]</i>,
    "<a href="#dosprofile" title="DosProfile">DosProfile</a>" : <i>[ <a href="dosprofiledefinition.md">DosProfileDefinition</a>, ... ]</i>,
    "<a href="#sedpcompression" title="SeDpCompression">SeDpCompression</a>" : <i>[ <a href="sedpcompressiondefinition.md">SeDpCompressionDefinition</a>, ... ]</i>,
    "<a href="#seratelimiters" title="SeRateLimiters">SeRateLimiters</a>" : <i>[ <a href="seratelimitersdefinition.md">SeRateLimitersDefinition</a>, ... ]</i>,
    "<a href="#serviceipsubnets" title="ServiceIpSubnets">ServiceIpSubnets</a>" : <i>[ <a href="serviceipsubnetsdefinition.md">ServiceIpSubnetsDefinition</a>, ... ]</i>,
    "<a href="#serviceportranges" title="ServicePortRanges">ServicePortRanges</a>" : <i>[ <a href="serviceportrangesdefinition.md">ServicePortRangesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#adminsshenabled" title="AdminSshEnabled">AdminSshEnabled</a>: <i>Boolean</i>
<a href="#baremetaldispatcherhandlesflows" title="BaremetalDispatcherHandlesFlows">BaremetalDispatcherHandlesFlows</a>: <i>Boolean</i>
<a href="#connectionslossylogratelimiterthreshold" title="ConnectionsLossyLogRateLimiterThreshold">ConnectionsLossyLogRateLimiterThreshold</a>: <i>Double</i>
<a href="#connectionsudfnflogratelimiterthreshold" title="ConnectionsUdfnfLogRateLimiterThreshold">ConnectionsUdfnfLogRateLimiterThreshold</a>: <i>Double</i>
<a href="#disableflowprobes" title="DisableFlowProbes">DisableFlowProbes</a>: <i>Boolean</i>
<a href="#downstreamsendtimeout" title="DownstreamSendTimeout">DownstreamSendTimeout</a>: <i>Double</i>
<a href="#dpaggressivehbfrequency" title="DpAggressiveHbFrequency">DpAggressiveHbFrequency</a>: <i>Double</i>
<a href="#dpaggressivehbtimeoutcount" title="DpAggressiveHbTimeoutCount">DpAggressiveHbTimeoutCount</a>: <i>Double</i>
<a href="#dphbfrequency" title="DpHbFrequency">DpHbFrequency</a>: <i>Double</i>
<a href="#dphbtimeoutcount" title="DpHbTimeoutCount">DpHbTimeoutCount</a>: <i>Double</i>
<a href="#dupipfrequency" title="DupipFrequency">DupipFrequency</a>: <i>Double</i>
<a href="#dupiptimeoutcount" title="DupipTimeoutCount">DupipTimeoutCount</a>: <i>Double</i>
<a href="#enablehsmlog" title="EnableHsmLog">EnableHsmLog</a>: <i>Boolean</i>
<a href="#feproxyvipsenableproxyarp" title="FeproxyVipsEnableProxyArp">FeproxyVipsEnableProxyArp</a>: <i>Boolean</i>
<a href="#flowtablebatchpushfrequency" title="FlowTableBatchPushFrequency">FlowTableBatchPushFrequency</a>: <i>Double</i>
<a href="#globalmtu" title="GlobalMtu">GlobalMtu</a>: <i>Double</i>
<a href="#httprumconsolelog" title="HttpRumConsoleLog">HttpRumConsoleLog</a>: <i>Boolean</i>
<a href="#httprummincontentlength" title="HttpRumMinContentLength">HttpRumMinContentLength</a>: <i>Double</i>
<a href="#lbactionnumrequeststodispatch" title="LbactionNumRequestsToDispatch">LbactionNumRequestsToDispatch</a>: <i>Double</i>
<a href="#lbactionrqperrequestmaxretries" title="LbactionRqPerRequestMaxRetries">LbactionRqPerRequestMaxRetries</a>: <i>Double</i>
<a href="#logagentcompresslogs" title="LogAgentCompressLogs">LogAgentCompressLogs</a>: <i>Boolean</i>
<a href="#logagentconnsendbuffersize" title="LogAgentConnSendBufferSize">LogAgentConnSendBufferSize</a>: <i>Double</i>
<a href="#logagentexportmsgbuffersize" title="LogAgentExportMsgBufferSize">LogAgentExportMsgBufferSize</a>: <i>Double</i>
<a href="#logagentexportwaittime" title="LogAgentExportWaitTime">LogAgentExportWaitTime</a>: <i>Double</i>
<a href="#logagentfileszappl" title="LogAgentFileSzAppl">LogAgentFileSzAppl</a>: <i>Double</i>
<a href="#logagentfileszconn" title="LogAgentFileSzConn">LogAgentFileSzConn</a>: <i>Double</i>
<a href="#logagentfileszdebug" title="LogAgentFileSzDebug">LogAgentFileSzDebug</a>: <i>Double</i>
<a href="#logagentfileszevent" title="LogAgentFileSzEvent">LogAgentFileSzEvent</a>: <i>Double</i>
<a href="#logagentlogstorageminsz" title="LogAgentLogStorageMinSz">LogAgentLogStorageMinSz</a>: <i>Double</i>
<a href="#logagentmaxactiveadffilespervs" title="LogAgentMaxActiveAdfFilesPerVs">LogAgentMaxActiveAdfFilesPerVs</a>: <i>Double</i>
<a href="#logagentmaxconcurrentrsync" title="LogAgentMaxConcurrentRsync">LogAgentMaxConcurrentRsync</a>: <i>Double</i>
<a href="#logagentmaxlogmessageprotosz" title="LogAgentMaxLogmessageProtoSz">LogAgentMaxLogmessageProtoSz</a>: <i>Double</i>
<a href="#logagentmaxstorageexcesspercent" title="LogAgentMaxStorageExcessPercent">LogAgentMaxStorageExcessPercent</a>: <i>Double</i>
<a href="#logagentmaxstorageignorepercent" title="LogAgentMaxStorageIgnorePercent">LogAgentMaxStorageIgnorePercent</a>: <i>Double</i>
<a href="#logagentminstoragepervs" title="LogAgentMinStoragePerVs">LogAgentMinStoragePerVs</a>: <i>Double</i>
<a href="#logagentpauseinterval" title="LogAgentPauseInterval">LogAgentPauseInterval</a>: <i>Double</i>
<a href="#logagentsleepinterval" title="LogAgentSleepInterval">LogAgentSleepInterval</a>: <i>Double</i>
<a href="#logagentunknownvstimer" title="LogAgentUnknownVsTimer">LogAgentUnknownVsTimer</a>: <i>Double</i>
<a href="#logmessagemaxfilelistsize" title="LogMessageMaxFileListSize">LogMessageMaxFileListSize</a>: <i>Double</i>
<a href="#mcacheenabled" title="McacheEnabled">McacheEnabled</a>: <i>Boolean</i>
<a href="#mcachefetchenabled" title="McacheFetchEnabled">McacheFetchEnabled</a>: <i>Boolean</i>
<a href="#mcachestoreinenabled" title="McacheStoreInEnabled">McacheStoreInEnabled</a>: <i>Boolean</i>
<a href="#mcachestoreinmaxsize" title="McacheStoreInMaxSize">McacheStoreInMaxSize</a>: <i>Double</i>
<a href="#mcachestoreinminsize" title="McacheStoreInMinSize">McacheStoreInMinSize</a>: <i>Double</i>
<a href="#mcachestoreoutenabled" title="McacheStoreOutEnabled">McacheStoreOutEnabled</a>: <i>Boolean</i>
<a href="#ngxfreeconnectionstack" title="NgxFreeConnectionStack">NgxFreeConnectionStack</a>: <i>Boolean</i>
<a href="#persistencememmax" title="PersistenceMemMax">PersistenceMemMax</a>: <i>Double</i>
<a href="#scaleoutudpperpkt" title="ScaleoutUdpPerPkt">ScaleoutUdpPerPkt</a>: <i>Boolean</i>
<a href="#seauthldapbindtimeout" title="SeAuthLdapBindTimeout">SeAuthLdapBindTimeout</a>: <i>Double</i>
<a href="#seauthldapcachesize" title="SeAuthLdapCacheSize">SeAuthLdapCacheSize</a>: <i>Double</i>
<a href="#seauthldapconnecttimeout" title="SeAuthLdapConnectTimeout">SeAuthLdapConnectTimeout</a>: <i>Double</i>
<a href="#seauthldapconnsperserver" title="SeAuthLdapConnsPerServer">SeAuthLdapConnsPerServer</a>: <i>Double</i>
<a href="#seauthldapreconnecttimeout" title="SeAuthLdapReconnectTimeout">SeAuthLdapReconnectTimeout</a>: <i>Double</i>
<a href="#seauthldaprequesttimeout" title="SeAuthLdapRequestTimeout">SeAuthLdapRequestTimeout</a>: <i>Double</i>
<a href="#seauthldapserversfailoveronly" title="SeAuthLdapServersFailoverOnly">SeAuthLdapServersFailoverOnly</a>: <i>Boolean</i>
<a href="#sedphmdrops" title="SeDpHmDrops">SeDpHmDrops</a>: <i>Double</i>
<a href="#sedpifstatepollinterval" title="SeDpIfStatePollInterval">SeDpIfStatePollInterval</a>: <i>Double</i>
<a href="#sedplognfenqueuepercent" title="SeDpLogNfEnqueuePercent">SeDpLogNfEnqueuePercent</a>: <i>Double</i>
<a href="#sedplogudfenqueuepercent" title="SeDpLogUdfEnqueuePercent">SeDpLogUdfEnqueuePercent</a>: <i>Double</i>
<a href="#sedumpcoreonassert" title="SeDumpCoreOnAssert">SeDumpCoreOnAssert</a>: <i>Boolean</i>
<a href="#sehandleinterfaceroutes" title="SeHandleInterfaceRoutes">SeHandleInterfaceRoutes</a>: <i>Boolean</i>
<a href="#sehbpersistfudgebits" title="SeHbPersistFudgeBits">SeHbPersistFudgeBits</a>: <i>Double</i>
<a href="#semacerrorthresholdtodisablepromiscious" title="SeMacErrorThresholdToDisablePromiscious">SeMacErrorThresholdToDisablePromiscious</a>: <i>Double</i>
<a href="#sememorypoison" title="SeMemoryPoison">SeMemoryPoison</a>: <i>Boolean</i>
<a href="#semetricsinterval" title="SeMetricsInterval">SeMetricsInterval</a>: <i>Double</i>
<a href="#semetricsrtenabled" title="SeMetricsRtEnabled">SeMetricsRtEnabled</a>: <i>Boolean</i>
<a href="#semetricsrtinterval" title="SeMetricsRtInterval">SeMetricsRtInterval</a>: <i>Double</i>
<a href="#sepacketbuffermax" title="SePacketBufferMax">SePacketBufferMax</a>: <i>Double</i>
<a href="#serandomtcpdrops" title="SeRandomTcpDrops">SeRandomTcpDrops</a>: <i>Boolean</i>
<a href="#servicesaccessibleallinterfaces" title="ServicesAccessibleAllInterfaces">ServicesAccessibleAllInterfaces</a>: <i>Boolean</i>
<a href="#spdyfwdproxyparseenable" title="SpdyFwdProxyParseEnable">SpdyFwdProxyParseEnable</a>: <i>Boolean</i>
<a href="#tcpsyncachemaxretransmitdefault" title="TcpSyncacheMaxRetransmitDefault">TcpSyncacheMaxRetransmitDefault</a>: <i>Double</i>
<a href="#upstreamconnecttimeout" title="UpstreamConnectTimeout">UpstreamConnectTimeout</a>: <i>Double</i>
<a href="#upstreamconnpoolcachethresh" title="UpstreamConnpoolCacheThresh">UpstreamConnpoolCacheThresh</a>: <i>Double</i>
<a href="#upstreamconnpoolconnidlethreshtmo" title="UpstreamConnpoolConnIdleThreshTmo">UpstreamConnpoolConnIdleThreshTmo</a>: <i>Double</i>
<a href="#upstreamconnpoolcoremaxcache" title="UpstreamConnpoolCoreMaxCache">UpstreamConnpoolCoreMaxCache</a>: <i>Double</i>
<a href="#upstreamconnpoolenable" title="UpstreamConnpoolEnable">UpstreamConnpoolEnable</a>: <i>Boolean</i>
<a href="#upstreamconnpoolstrategy" title="UpstreamConnpoolStrategy">UpstreamConnpoolStrategy</a>: <i>Double</i>
<a href="#upstreamkeepalive" title="UpstreamKeepalive">UpstreamKeepalive</a>: <i>Boolean</i>
<a href="#upstreamreadtimeout" title="UpstreamReadTimeout">UpstreamReadTimeout</a>: <i>Double</i>
<a href="#upstreamsendtimeout" title="UpstreamSendTimeout">UpstreamSendTimeout</a>: <i>Double</i>
<a href="#userdefinedmetricage" title="UserDefinedMetricAge">UserDefinedMetricAge</a>: <i>Double</i>
<a href="#appheaders" title="AppHeaders">AppHeaders</a>: <i>
      - <a href="appheadersdefinition.md">AppHeadersDefinition</a></i>
<a href="#dosprofile" title="DosProfile">DosProfile</a>: <i>
      - <a href="dosprofiledefinition.md">DosProfileDefinition</a></i>
<a href="#sedpcompression" title="SeDpCompression">SeDpCompression</a>: <i>
      - <a href="sedpcompressiondefinition.md">SeDpCompressionDefinition</a></i>
<a href="#seratelimiters" title="SeRateLimiters">SeRateLimiters</a>: <i>
      - <a href="seratelimitersdefinition.md">SeRateLimitersDefinition</a></i>
<a href="#serviceipsubnets" title="ServiceIpSubnets">ServiceIpSubnets</a>: <i>
      - <a href="serviceipsubnetsdefinition.md">ServiceIpSubnetsDefinition</a></i>
<a href="#serviceportranges" title="ServicePortRanges">ServicePortRanges</a>: <i>
      - <a href="serviceportrangesdefinition.md">ServicePortRangesDefinition</a></i>
</pre>

## Properties

#### AdminSshEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BaremetalDispatcherHandlesFlows

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionsLossyLogRateLimiterThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionsUdfnfLogRateLimiterThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableFlowProbes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownstreamSendTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpAggressiveHbFrequency

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpAggressiveHbTimeoutCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpHbFrequency

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpHbTimeoutCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DupipFrequency

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DupipTimeoutCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHsmLog

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeproxyVipsEnableProxyArp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlowTableBatchPushFrequency

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalMtu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRumConsoleLog

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRumMinContentLength

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbactionNumRequestsToDispatch

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbactionRqPerRequestMaxRetries

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentCompressLogs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentConnSendBufferSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentExportMsgBufferSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentExportWaitTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentFileSzAppl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentFileSzConn

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentFileSzDebug

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentFileSzEvent

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentLogStorageMinSz

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentMaxActiveAdfFilesPerVs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentMaxConcurrentRsync

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentMaxLogmessageProtoSz

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentMaxStorageExcessPercent

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentMaxStorageIgnorePercent

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentMinStoragePerVs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentPauseInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentSleepInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentUnknownVsTimer

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogMessageMaxFileListSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### McacheEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### McacheFetchEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### McacheStoreInEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### McacheStoreInMaxSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### McacheStoreInMinSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### McacheStoreOutEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NgxFreeConnectionStack

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistenceMemMax

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleoutUdpPerPkt

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeAuthLdapBindTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeAuthLdapCacheSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeAuthLdapConnectTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeAuthLdapConnsPerServer

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeAuthLdapReconnectTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeAuthLdapRequestTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeAuthLdapServersFailoverOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDpHmDrops

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDpIfStatePollInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDpLogNfEnqueuePercent

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDpLogUdfEnqueuePercent

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDumpCoreOnAssert

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeHandleInterfaceRoutes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeHbPersistFudgeBits

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeMacErrorThresholdToDisablePromiscious

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeMemoryPoison

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeMetricsInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeMetricsRtEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeMetricsRtInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SePacketBufferMax

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeRandomTcpDrops

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicesAccessibleAllInterfaces

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpdyFwdProxyParseEnable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpSyncacheMaxRetransmitDefault

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpstreamConnectTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpstreamConnpoolCacheThresh

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpstreamConnpoolConnIdleThreshTmo

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpstreamConnpoolCoreMaxCache

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpstreamConnpoolEnable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpstreamConnpoolStrategy

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpstreamKeepalive

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpstreamReadTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpstreamSendTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserDefinedMetricAge

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppHeaders

_Required_: No

_Type_: List of <a href="appheadersdefinition.md">AppHeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DosProfile

_Required_: No

_Type_: List of <a href="dosprofiledefinition.md">DosProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDpCompression

_Required_: No

_Type_: List of <a href="sedpcompressiondefinition.md">SeDpCompressionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeRateLimiters

_Required_: No

_Type_: List of <a href="seratelimitersdefinition.md">SeRateLimitersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceIpSubnets

_Required_: No

_Type_: List of <a href="serviceipsubnetsdefinition.md">ServiceIpSubnetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePortRanges

_Required_: No

_Type_: List of <a href="serviceportrangesdefinition.md">ServicePortRangesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

