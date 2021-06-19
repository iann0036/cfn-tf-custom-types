# TF::AVI::Serviceenginegroup

The ServiceEngineGroup resource allows the creation and management of Avi ServiceEngineGroup

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Serviceenginegroup",
    "Properties" : {
        "<a href="#acceleratednetworking" title="AcceleratedNetworking">AcceleratedNetworking</a>" : <i>Boolean</i>,
        "<a href="#activestandby" title="ActiveStandby">ActiveStandby</a>" : <i>Boolean</i>,
        "<a href="#aggressivefailuredetection" title="AggressiveFailureDetection">AggressiveFailureDetection</a>" : <i>Boolean</i>,
        "<a href="#algo" title="Algo">Algo</a>" : <i>String</i>,
        "<a href="#allowburst" title="AllowBurst">AllowBurst</a>" : <i>Boolean</i>,
        "<a href="#appcachepercent" title="AppCachePercent">AppCachePercent</a>" : <i>Double</i>,
        "<a href="#appcachethreshold" title="AppCacheThreshold">AppCacheThreshold</a>" : <i>Double</i>,
        "<a href="#applearningmemorypercent" title="AppLearningMemoryPercent">AppLearningMemoryPercent</a>" : <i>Double</i>,
        "<a href="#archiveshmlimit" title="ArchiveShmLimit">ArchiveShmLimit</a>" : <i>Double</i>,
        "<a href="#asyncssl" title="AsyncSsl">AsyncSsl</a>" : <i>Boolean</i>,
        "<a href="#asyncsslthreads" title="AsyncSslThreads">AsyncSslThreads</a>" : <i>Double</i>,
        "<a href="#autorebalance" title="AutoRebalance">AutoRebalance</a>" : <i>Boolean</i>,
        "<a href="#autorebalancecapacityperse" title="AutoRebalanceCapacityPerSe">AutoRebalanceCapacityPerSe</a>" : <i>[ Double, ... ]</i>,
        "<a href="#autorebalancecriteria" title="AutoRebalanceCriteria">AutoRebalanceCriteria</a>" : <i>[ String, ... ]</i>,
        "<a href="#autorebalanceinterval" title="AutoRebalanceInterval">AutoRebalanceInterval</a>" : <i>Double</i>,
        "<a href="#autoredistributeactivestandbyload" title="AutoRedistributeActiveStandbyLoad">AutoRedistributeActiveStandbyLoad</a>" : <i>Boolean</i>,
        "<a href="#availabilityzonerefs" title="AvailabilityZoneRefs">AvailabilityZoneRefs</a>" : <i>[ String, ... ]</i>,
        "<a href="#bgpstateupdateinterval" title="BgpStateUpdateInterval">BgpStateUpdateInterval</a>" : <i>Double</i>,
        "<a href="#bufferse" title="BufferSe">BufferSe</a>" : <i>Double</i>,
        "<a href="#cloudref" title="CloudRef">CloudRef</a>" : <i>String</i>,
        "<a href="#compressiprulesforeachnssubnet" title="CompressIpRulesForEachNsSubnet">CompressIpRulesForEachNsSubnet</a>" : <i>Boolean</i>,
        "<a href="#configdebugsonallcores" title="ConfigDebugsOnAllCores">ConfigDebugsOnAllCores</a>" : <i>Boolean</i>,
        "<a href="#connectionmemorypercentage" title="ConnectionMemoryPercentage">ConnectionMemoryPercentage</a>" : <i>Double</i>,
        "<a href="#coreshmappcache" title="CoreShmAppCache">CoreShmAppCache</a>" : <i>Boolean</i>,
        "<a href="#coreshmapplearning" title="CoreShmAppLearning">CoreShmAppLearning</a>" : <i>Boolean</i>,
        "<a href="#cpureserve" title="CpuReserve">CpuReserve</a>" : <i>Boolean</i>,
        "<a href="#cpusocketaffinity" title="CpuSocketAffinity">CpuSocketAffinity</a>" : <i>Boolean</i>,
        "<a href="#customsecuritygroupsdata" title="CustomSecuritygroupsData">CustomSecuritygroupsData</a>" : <i>[ String, ... ]</i>,
        "<a href="#customsecuritygroupsmgmt" title="CustomSecuritygroupsMgmt">CustomSecuritygroupsMgmt</a>" : <i>[ String, ... ]</i>,
        "<a href="#datanetworkid" title="DataNetworkId">DataNetworkId</a>" : <i>String</i>,
        "<a href="#datascripttimeout" title="DatascriptTimeout">DatascriptTimeout</a>" : <i>Double</i>,
        "<a href="#dedicateddispatchercore" title="DedicatedDispatcherCore">DedicatedDispatcherCore</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disableavisecuritygroups" title="DisableAviSecuritygroups">DisableAviSecuritygroups</a>" : <i>Boolean</i>,
        "<a href="#disablecsumoffloads" title="DisableCsumOffloads">DisableCsumOffloads</a>" : <i>Boolean</i>,
        "<a href="#disableflowprobes" title="DisableFlowProbes">DisableFlowProbes</a>" : <i>Boolean</i>,
        "<a href="#disablegro" title="DisableGro">DisableGro</a>" : <i>Boolean</i>,
        "<a href="#disablesememorycheck" title="DisableSeMemoryCheck">DisableSeMemoryCheck</a>" : <i>Boolean</i>,
        "<a href="#disabletso" title="DisableTso">DisableTso</a>" : <i>Boolean</i>,
        "<a href="#diskperse" title="DiskPerSe">DiskPerSe</a>" : <i>Double</i>,
        "<a href="#distributeloadactivestandby" title="DistributeLoadActiveStandby">DistributeLoadActiveStandby</a>" : <i>Boolean</i>,
        "<a href="#distributequeues" title="DistributeQueues">DistributeQueues</a>" : <i>Boolean</i>,
        "<a href="#distributevnics" title="DistributeVnics">DistributeVnics</a>" : <i>Boolean</i>,
        "<a href="#dpaggressivehbfrequency" title="DpAggressiveHbFrequency">DpAggressiveHbFrequency</a>" : <i>Double</i>,
        "<a href="#dpaggressivehbtimeoutcount" title="DpAggressiveHbTimeoutCount">DpAggressiveHbTimeoutCount</a>" : <i>Double</i>,
        "<a href="#dphbfrequency" title="DpHbFrequency">DpHbFrequency</a>" : <i>Double</i>,
        "<a href="#dphbtimeoutcount" title="DpHbTimeoutCount">DpHbTimeoutCount</a>" : <i>Double</i>,
        "<a href="#enablegratarppermanent" title="EnableGratarpPermanent">EnableGratarpPermanent</a>" : <i>Boolean</i>,
        "<a href="#enablehsmpriming" title="EnableHsmPriming">EnableHsmPriming</a>" : <i>Boolean</i>,
        "<a href="#enablemultilb" title="EnableMultiLb">EnableMultiLb</a>" : <i>Boolean</i>,
        "<a href="#enablepcaptxring" title="EnablePcapTxRing">EnablePcapTxRing</a>" : <i>Boolean</i>,
        "<a href="#ephemeralportrangeend" title="EphemeralPortrangeEnd">EphemeralPortrangeEnd</a>" : <i>Double</i>,
        "<a href="#ephemeralportrangestart" title="EphemeralPortrangeStart">EphemeralPortrangeStart</a>" : <i>Double</i>,
        "<a href="#extraconfigmultiplier" title="ExtraConfigMultiplier">ExtraConfigMultiplier</a>" : <i>Double</i>,
        "<a href="#extrasharedconfigmemory" title="ExtraSharedConfigMemory">ExtraSharedConfigMemory</a>" : <i>Double</i>,
        "<a href="#flowtablenewsynmaxentries" title="FlowTableNewSynMaxEntries">FlowTableNewSynMaxEntries</a>" : <i>Double</i>,
        "<a href="#freelistsize" title="FreeListSize">FreeListSize</a>" : <i>Double</i>,
        "<a href="#gratarppermanentperiodicity" title="GratarpPermanentPeriodicity">GratarpPermanentPeriodicity</a>" : <i>Double</i>,
        "<a href="#hamode" title="HaMode">HaMode</a>" : <i>String</i>,
        "<a href="#handleperpktattack" title="HandlePerPktAttack">HandlePerPktAttack</a>" : <i>Boolean</i>,
        "<a href="#hardwaresecuritymodulegroupref" title="HardwaresecuritymodulegroupRef">HardwaresecuritymodulegroupRef</a>" : <i>String</i>,
        "<a href="#heapminimumconfigmemory" title="HeapMinimumConfigMemory">HeapMinimumConfigMemory</a>" : <i>Double</i>,
        "<a href="#hmonstandby" title="HmOnStandby">HmOnStandby</a>" : <i>Boolean</i>,
        "<a href="#hostattributekey" title="HostAttributeKey">HostAttributeKey</a>" : <i>String</i>,
        "<a href="#hostattributevalue" title="HostAttributeValue">HostAttributeValue</a>" : <i>String</i>,
        "<a href="#hostgatewaymonitor" title="HostGatewayMonitor">HostGatewayMonitor</a>" : <i>Boolean</i>,
        "<a href="#hypervisor" title="Hypervisor">Hypervisor</a>" : <i>String</i>,
        "<a href="#ignorerttthreshold" title="IgnoreRttThreshold">IgnoreRttThreshold</a>" : <i>Double</i>,
        "<a href="#ingressaccessdata" title="IngressAccessData">IngressAccessData</a>" : <i>String</i>,
        "<a href="#ingressaccessmgmt" title="IngressAccessMgmt">IngressAccessMgmt</a>" : <i>String</i>,
        "<a href="#instanceflavor" title="InstanceFlavor">InstanceFlavor</a>" : <i>String</i>,
        "<a href="#leastloadcoreselection" title="LeastLoadCoreSelection">LeastLoadCoreSelection</a>" : <i>Boolean</i>,
        "<a href="#licensetier" title="LicenseTier">LicenseTier</a>" : <i>String</i>,
        "<a href="#licensetype" title="LicenseType">LicenseType</a>" : <i>String</i>,
        "<a href="#logdisksz" title="LogDisksz">LogDisksz</a>" : <i>Double</i>,
        "<a href="#logmallocfailure" title="LogMallocFailure">LogMallocFailure</a>" : <i>Boolean</i>,
        "<a href="#maxconcurrentexternalhm" title="MaxConcurrentExternalHm">MaxConcurrentExternalHm</a>" : <i>Double</i>,
        "<a href="#maxcpuusage" title="MaxCpuUsage">MaxCpuUsage</a>" : <i>Double</i>,
        "<a href="#maxmemorypermempool" title="MaxMemoryPerMempool">MaxMemoryPerMempool</a>" : <i>Double</i>,
        "<a href="#maxnumsedps" title="MaxNumSeDps">MaxNumSeDps</a>" : <i>Double</i>,
        "<a href="#maxpublicipsperlb" title="MaxPublicIpsPerLb">MaxPublicIpsPerLb</a>" : <i>Double</i>,
        "<a href="#maxqueuespervnic" title="MaxQueuesPerVnic">MaxQueuesPerVnic</a>" : <i>Double</i>,
        "<a href="#maxrulesperlb" title="MaxRulesPerLb">MaxRulesPerLb</a>" : <i>Double</i>,
        "<a href="#maxscaleoutpervs" title="MaxScaleoutPerVs">MaxScaleoutPerVs</a>" : <i>Double</i>,
        "<a href="#maxse" title="MaxSe">MaxSe</a>" : <i>Double</i>,
        "<a href="#maxvsperse" title="MaxVsPerSe">MaxVsPerSe</a>" : <i>Double</i>,
        "<a href="#memreserve" title="MemReserve">MemReserve</a>" : <i>Boolean</i>,
        "<a href="#memoryforconfigupdate" title="MemoryForConfigUpdate">MemoryForConfigUpdate</a>" : <i>Double</i>,
        "<a href="#memoryperse" title="MemoryPerSe">MemoryPerSe</a>" : <i>Double</i>,
        "<a href="#mgmtnetworkref" title="MgmtNetworkRef">MgmtNetworkRef</a>" : <i>String</i>,
        "<a href="#mincpuusage" title="MinCpuUsage">MinCpuUsage</a>" : <i>Double</i>,
        "<a href="#minscaleoutpervs" title="MinScaleoutPerVs">MinScaleoutPerVs</a>" : <i>Double</i>,
        "<a href="#minse" title="MinSe">MinSe</a>" : <i>Double</i>,
        "<a href="#minimumconnectionmemory" title="MinimumConnectionMemory">MinimumConnectionMemory</a>" : <i>Double</i>,
        "<a href="#nlogstreamingthreads" title="NLogStreamingThreads">NLogStreamingThreads</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nonsignificantlogthrottle" title="NonSignificantLogThrottle">NonSignificantLogThrottle</a>" : <i>Double</i>,
        "<a href="#numdispatchercores" title="NumDispatcherCores">NumDispatcherCores</a>" : <i>Double</i>,
        "<a href="#numflowcoressumchangestoignore" title="NumFlowCoresSumChangesToIgnore">NumFlowCoresSumChangesToIgnore</a>" : <i>Double</i>,
        "<a href="#objsyncport" title="ObjsyncPort">ObjsyncPort</a>" : <i>Double</i>,
        "<a href="#openstackavailabilityzones" title="OpenstackAvailabilityZones">OpenstackAvailabilityZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#openstackmgmtnetworkname" title="OpenstackMgmtNetworkName">OpenstackMgmtNetworkName</a>" : <i>String</i>,
        "<a href="#openstackmgmtnetworkuuid" title="OpenstackMgmtNetworkUuid">OpenstackMgmtNetworkUuid</a>" : <i>String</i>,
        "<a href="#osreservedmemory" title="OsReservedMemory">OsReservedMemory</a>" : <i>Double</i>,
        "<a href="#pcaptxmode" title="PcapTxMode">PcapTxMode</a>" : <i>String</i>,
        "<a href="#pcaptxringrdbalancingfactor" title="PcapTxRingRdBalancingFactor">PcapTxRingRdBalancingFactor</a>" : <i>Double</i>,
        "<a href="#perapp" title="PerApp">PerApp</a>" : <i>Boolean</i>,
        "<a href="#pervsadmissioncontrol" title="PerVsAdmissionControl">PerVsAdmissionControl</a>" : <i>Boolean</i>,
        "<a href="#placementmode" title="PlacementMode">PlacementMode</a>" : <i>String</i>,
        "<a href="#rebootonpanic" title="RebootOnPanic">RebootOnPanic</a>" : <i>Boolean</i>,
        "<a href="#resynctimeinterval" title="ResyncTimeInterval">ResyncTimeInterval</a>" : <i>Double</i>,
        "<a href="#sebandwidthtype" title="SeBandwidthType">SeBandwidthType</a>" : <i>String</i>,
        "<a href="#sedelayedflowdelete" title="SeDelayedFlowDelete">SeDelayedFlowDelete</a>" : <i>Boolean</i>,
        "<a href="#sedeprovisiondelay" title="SeDeprovisionDelay">SeDeprovisionDelay</a>" : <i>Double</i>,
        "<a href="#sedphmdrops" title="SeDpHmDrops">SeDpHmDrops</a>" : <i>Double</i>,
        "<a href="#sedpisolation" title="SeDpIsolation">SeDpIsolation</a>" : <i>Boolean</i>,
        "<a href="#sedpisolationnumnondpcpus" title="SeDpIsolationNumNonDpCpus">SeDpIsolationNumNonDpCpus</a>" : <i>Double</i>,
        "<a href="#sedpmaxhbversion" title="SeDpMaxHbVersion">SeDpMaxHbVersion</a>" : <i>Double</i>,
        "<a href="#sedpvnicqueuestalleventsleep" title="SeDpVnicQueueStallEventSleep">SeDpVnicQueueStallEventSleep</a>" : <i>Double</i>,
        "<a href="#sedpvnicqueuestallthreshold" title="SeDpVnicQueueStallThreshold">SeDpVnicQueueStallThreshold</a>" : <i>Double</i>,
        "<a href="#sedpvnicqueuestalltimeout" title="SeDpVnicQueueStallTimeout">SeDpVnicQueueStallTimeout</a>" : <i>Double</i>,
        "<a href="#sedpvnicrestartonqueuestallcount" title="SeDpVnicRestartOnQueueStallCount">SeDpVnicRestartOnQueueStallCount</a>" : <i>Double</i>,
        "<a href="#sedpvnicstallserestartwindow" title="SeDpVnicStallSeRestartWindow">SeDpVnicStallSeRestartWindow</a>" : <i>Double</i>,
        "<a href="#sedpdkpmd" title="SeDpdkPmd">SeDpdkPmd</a>" : <i>Double</i>,
        "<a href="#seflowproberetries" title="SeFlowProbeRetries">SeFlowProbeRetries</a>" : <i>Double</i>,
        "<a href="#seflowproberetrytimer" title="SeFlowProbeRetryTimer">SeFlowProbeRetryTimer</a>" : <i>Double</i>,
        "<a href="#sehyperthreadedmode" title="SeHyperthreadedMode">SeHyperthreadedMode</a>" : <i>String</i>,
        "<a href="#seipencapipc" title="SeIpEncapIpc">SeIpEncapIpc</a>" : <i>Double</i>,
        "<a href="#sekniburstfactor" title="SeKniBurstFactor">SeKniBurstFactor</a>" : <i>Double</i>,
        "<a href="#sel3encapipc" title="SeL3EncapIpc">SeL3EncapIpc</a>" : <i>Double</i>,
        "<a href="#selro" title="SeLro">SeLro</a>" : <i>Boolean</i>,
        "<a href="#sempringretrycount" title="SeMpRingRetryCount">SeMpRingRetryCount</a>" : <i>Double</i>,
        "<a href="#semtu" title="SeMtu">SeMtu</a>" : <i>Double</i>,
        "<a href="#senameprefix" title="SeNamePrefix">SeNamePrefix</a>" : <i>String</i>,
        "<a href="#sepcaplookahead" title="SePcapLookahead">SePcapLookahead</a>" : <i>Boolean</i>,
        "<a href="#sepcappktcount" title="SePcapPktCount">SePcapPktCount</a>" : <i>Double</i>,
        "<a href="#sepcappktsz" title="SePcapPktSz">SePcapPktSz</a>" : <i>Double</i>,
        "<a href="#sepcapqdiscbypass" title="SePcapQdiscBypass">SePcapQdiscBypass</a>" : <i>Boolean</i>,
        "<a href="#sepcapreinitfrequency" title="SePcapReinitFrequency">SePcapReinitFrequency</a>" : <i>Double</i>,
        "<a href="#sepcapreinitthreshold" title="SePcapReinitThreshold">SePcapReinitThreshold</a>" : <i>Double</i>,
        "<a href="#seprobeport" title="SeProbePort">SeProbePort</a>" : <i>Double</i>,
        "<a href="#serumsamplingnavinterval" title="SeRumSamplingNavInterval">SeRumSamplingNavInterval</a>" : <i>Double</i>,
        "<a href="#serumsamplingnavpercent" title="SeRumSamplingNavPercent">SeRumSamplingNavPercent</a>" : <i>Double</i>,
        "<a href="#serumsamplingresinterval" title="SeRumSamplingResInterval">SeRumSamplingResInterval</a>" : <i>Double</i>,
        "<a href="#serumsamplingrespercent" title="SeRumSamplingResPercent">SeRumSamplingResPercent</a>" : <i>Double</i>,
        "<a href="#sesbdedicatedcore" title="SeSbDedicatedCore">SeSbDedicatedCore</a>" : <i>Boolean</i>,
        "<a href="#sesbthreads" title="SeSbThreads">SeSbThreads</a>" : <i>Double</i>,
        "<a href="#sethreadmultiplier" title="SeThreadMultiplier">SeThreadMultiplier</a>" : <i>Double</i>,
        "<a href="#setunnelmode" title="SeTunnelMode">SeTunnelMode</a>" : <i>Double</i>,
        "<a href="#setunneludpport" title="SeTunnelUdpPort">SeTunnelUdpPort</a>" : <i>Double</i>,
        "<a href="#setxbatchsize" title="SeTxBatchSize">SeTxBatchSize</a>" : <i>Double</i>,
        "<a href="#setxqthreshold" title="SeTxqThreshold">SeTxqThreshold</a>" : <i>Double</i>,
        "<a href="#seudpencapipc" title="SeUdpEncapIpc">SeUdpEncapIpc</a>" : <i>Double</i>,
        "<a href="#seusedpdk" title="SeUseDpdk">SeUseDpdk</a>" : <i>Double</i>,
        "<a href="#sevnictxswqueueflushfrequency" title="SeVnicTxSwQueueFlushFrequency">SeVnicTxSwQueueFlushFrequency</a>" : <i>Double</i>,
        "<a href="#sevnictxswqueuesize" title="SeVnicTxSwQueueSize">SeVnicTxSwQueueSize</a>" : <i>Double</i>,
        "<a href="#sevshbmaxpktsinbatch" title="SeVsHbMaxPktsInBatch">SeVsHbMaxPktsInBatch</a>" : <i>Double</i>,
        "<a href="#sevshbmaxvsinpkt" title="SeVsHbMaxVsInPkt">SeVsHbMaxVsInPkt</a>" : <i>Double</i>,
        "<a href="#selfseelection" title="SelfSeElection">SelfSeElection</a>" : <i>Boolean</i>,
        "<a href="#shmminimumconfigmemory" title="ShmMinimumConfigMemory">ShmMinimumConfigMemory</a>" : <i>Double</i>,
        "<a href="#significantlogthrottle" title="SignificantLogThrottle">SignificantLogThrottle</a>" : <i>Double</i>,
        "<a href="#sslpreprocesssnihostname" title="SslPreprocessSniHostname">SslPreprocessSniHostname</a>" : <i>Boolean</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#transientsharedmemorymax" title="TransientSharedMemoryMax">TransientSharedMemoryMax</a>" : <i>Double</i>,
        "<a href="#udflogthrottle" title="UdfLogThrottle">UdfLogThrottle</a>" : <i>Double</i>,
        "<a href="#usehyperthreadedcores" title="UseHyperthreadedCores">UseHyperthreadedCores</a>" : <i>Boolean</i>,
        "<a href="#useobjsync" title="UseObjsync">UseObjsync</a>" : <i>Boolean</i>,
        "<a href="#usestandardalb" title="UseStandardAlb">UseStandardAlb</a>" : <i>Boolean</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vcenterdatastoremode" title="VcenterDatastoreMode">VcenterDatastoreMode</a>" : <i>String</i>,
        "<a href="#vcenterdatastoresinclude" title="VcenterDatastoresInclude">VcenterDatastoresInclude</a>" : <i>Boolean</i>,
        "<a href="#vcenterfolder" title="VcenterFolder">VcenterFolder</a>" : <i>String</i>,
        "<a href="#vcpusperse" title="VcpusPerSe">VcpusPerSe</a>" : <i>Double</i>,
        "<a href="#vshostredundancy" title="VsHostRedundancy">VsHostRedundancy</a>" : <i>Boolean</i>,
        "<a href="#vsscaleintimeout" title="VsScaleinTimeout">VsScaleinTimeout</a>" : <i>Double</i>,
        "<a href="#vsscaleintimeoutforupgrade" title="VsScaleinTimeoutForUpgrade">VsScaleinTimeoutForUpgrade</a>" : <i>Double</i>,
        "<a href="#vsscaleouttimeout" title="VsScaleoutTimeout">VsScaleoutTimeout</a>" : <i>Double</i>,
        "<a href="#vssescaleoutadditionalwaittime" title="VsSeScaleoutAdditionalWaitTime">VsSeScaleoutAdditionalWaitTime</a>" : <i>Double</i>,
        "<a href="#vssescaleoutreadytimeout" title="VsSeScaleoutReadyTimeout">VsSeScaleoutReadyTimeout</a>" : <i>Double</i>,
        "<a href="#vsswitchovertimeout" title="VsSwitchoverTimeout">VsSwitchoverTimeout</a>" : <i>Double</i>,
        "<a href="#vssplacementenabled" title="VssPlacementEnabled">VssPlacementEnabled</a>" : <i>Boolean</i>,
        "<a href="#wafmempool" title="WafMempool">WafMempool</a>" : <i>Boolean</i>,
        "<a href="#wafmempoolsize" title="WafMempoolSize">WafMempoolSize</a>" : <i>Double</i>,
        "<a href="#customtag" title="CustomTag">CustomTag</a>" : <i>[ <a href="customtagdefinition.md">CustomTagDefinition</a>, ... ]</i>,
        "<a href="#gcpconfig" title="GcpConfig">GcpConfig</a>" : <i>[ <a href="gcpconfigdefinition.md">GcpConfigDefinition</a>, ... ]</i>,
        "<a href="#instanceflavorinfo" title="InstanceFlavorInfo">InstanceFlavorInfo</a>" : <i>[ <a href="instanceflavorinfodefinition.md">InstanceFlavorInfoDefinition</a>, ... ]</i>,
        "<a href="#iptables" title="Iptables">Iptables</a>" : <i>[ <a href="iptablesdefinition.md">IptablesDefinition</a>, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#mgmtsubnet" title="MgmtSubnet">MgmtSubnet</a>" : <i>[ <a href="mgmtsubnetdefinition.md">MgmtSubnetDefinition</a>, ... ]</i>,
        "<a href="#objsyncconfig" title="ObjsyncConfig">ObjsyncConfig</a>" : <i>[ <a href="objsyncconfigdefinition.md">ObjsyncConfigDefinition</a>, ... ]</i>,
        "<a href="#realtimesemetrics" title="RealtimeSeMetrics">RealtimeSeMetrics</a>" : <i>[ <a href="realtimesemetricsdefinition.md">RealtimeSeMetricsDefinition</a>, ... ]</i>,
        "<a href="#sedosprofile" title="SeDosProfile">SeDosProfile</a>" : <i>[ <a href="sedosprofiledefinition.md">SeDosProfileDefinition</a>, ... ]</i>,
        "<a href="#segroupanalyticspolicy" title="SeGroupAnalyticsPolicy">SeGroupAnalyticsPolicy</a>" : <i>[ <a href="segroupanalyticspolicydefinition.md">SeGroupAnalyticsPolicyDefinition</a>, ... ]</i>,
        "<a href="#serlprop" title="SeRlProp">SeRlProp</a>" : <i>[ <a href="serlpropdefinition.md">SeRlPropDefinition</a>, ... ]</i>,
        "<a href="#setracertportrange" title="SeTracertPortRange">SeTracertPortRange</a>" : <i>[ <a href="setracertportrangedefinition.md">SeTracertPortRangeDefinition</a>, ... ]</i>,
        "<a href="#serviceip6subnets" title="ServiceIp6Subnets">ServiceIp6Subnets</a>" : <i>[ <a href="serviceip6subnetsdefinition.md">ServiceIp6SubnetsDefinition</a>, ... ]</i>,
        "<a href="#serviceipsubnets" title="ServiceIpSubnets">ServiceIpSubnets</a>" : <i>[ <a href="serviceipsubnetsdefinition.md">ServiceIpSubnetsDefinition</a>, ... ]</i>,
        "<a href="#vcenterclusters" title="VcenterClusters">VcenterClusters</a>" : <i>[ <a href="vcenterclustersdefinition.md">VcenterClustersDefinition</a>, ... ]</i>,
        "<a href="#vcenterdatastores" title="VcenterDatastores">VcenterDatastores</a>" : <i>[ <a href="vcenterdatastoresdefinition.md">VcenterDatastoresDefinition</a>, ... ]</i>,
        "<a href="#vcenterhosts" title="VcenterHosts">VcenterHosts</a>" : <i>[ <a href="vcenterhostsdefinition.md">VcenterHostsDefinition</a>, ... ]</i>,
        "<a href="#vcenters" title="Vcenters">Vcenters</a>" : <i>[ <a href="vcentersdefinition.md">VcentersDefinition</a>, ... ]</i>,
        "<a href="#vipasg" title="VipAsg">VipAsg</a>" : <i>[ <a href="vipasgdefinition.md">VipAsgDefinition</a>, ... ]</i>,
        "<a href="#vssplacement" title="VssPlacement">VssPlacement</a>" : <i>[ <a href="vssplacementdefinition.md">VssPlacementDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Serviceenginegroup
Properties:
    <a href="#acceleratednetworking" title="AcceleratedNetworking">AcceleratedNetworking</a>: <i>Boolean</i>
    <a href="#activestandby" title="ActiveStandby">ActiveStandby</a>: <i>Boolean</i>
    <a href="#aggressivefailuredetection" title="AggressiveFailureDetection">AggressiveFailureDetection</a>: <i>Boolean</i>
    <a href="#algo" title="Algo">Algo</a>: <i>String</i>
    <a href="#allowburst" title="AllowBurst">AllowBurst</a>: <i>Boolean</i>
    <a href="#appcachepercent" title="AppCachePercent">AppCachePercent</a>: <i>Double</i>
    <a href="#appcachethreshold" title="AppCacheThreshold">AppCacheThreshold</a>: <i>Double</i>
    <a href="#applearningmemorypercent" title="AppLearningMemoryPercent">AppLearningMemoryPercent</a>: <i>Double</i>
    <a href="#archiveshmlimit" title="ArchiveShmLimit">ArchiveShmLimit</a>: <i>Double</i>
    <a href="#asyncssl" title="AsyncSsl">AsyncSsl</a>: <i>Boolean</i>
    <a href="#asyncsslthreads" title="AsyncSslThreads">AsyncSslThreads</a>: <i>Double</i>
    <a href="#autorebalance" title="AutoRebalance">AutoRebalance</a>: <i>Boolean</i>
    <a href="#autorebalancecapacityperse" title="AutoRebalanceCapacityPerSe">AutoRebalanceCapacityPerSe</a>: <i>
      - Double</i>
    <a href="#autorebalancecriteria" title="AutoRebalanceCriteria">AutoRebalanceCriteria</a>: <i>
      - String</i>
    <a href="#autorebalanceinterval" title="AutoRebalanceInterval">AutoRebalanceInterval</a>: <i>Double</i>
    <a href="#autoredistributeactivestandbyload" title="AutoRedistributeActiveStandbyLoad">AutoRedistributeActiveStandbyLoad</a>: <i>Boolean</i>
    <a href="#availabilityzonerefs" title="AvailabilityZoneRefs">AvailabilityZoneRefs</a>: <i>
      - String</i>
    <a href="#bgpstateupdateinterval" title="BgpStateUpdateInterval">BgpStateUpdateInterval</a>: <i>Double</i>
    <a href="#bufferse" title="BufferSe">BufferSe</a>: <i>Double</i>
    <a href="#cloudref" title="CloudRef">CloudRef</a>: <i>String</i>
    <a href="#compressiprulesforeachnssubnet" title="CompressIpRulesForEachNsSubnet">CompressIpRulesForEachNsSubnet</a>: <i>Boolean</i>
    <a href="#configdebugsonallcores" title="ConfigDebugsOnAllCores">ConfigDebugsOnAllCores</a>: <i>Boolean</i>
    <a href="#connectionmemorypercentage" title="ConnectionMemoryPercentage">ConnectionMemoryPercentage</a>: <i>Double</i>
    <a href="#coreshmappcache" title="CoreShmAppCache">CoreShmAppCache</a>: <i>Boolean</i>
    <a href="#coreshmapplearning" title="CoreShmAppLearning">CoreShmAppLearning</a>: <i>Boolean</i>
    <a href="#cpureserve" title="CpuReserve">CpuReserve</a>: <i>Boolean</i>
    <a href="#cpusocketaffinity" title="CpuSocketAffinity">CpuSocketAffinity</a>: <i>Boolean</i>
    <a href="#customsecuritygroupsdata" title="CustomSecuritygroupsData">CustomSecuritygroupsData</a>: <i>
      - String</i>
    <a href="#customsecuritygroupsmgmt" title="CustomSecuritygroupsMgmt">CustomSecuritygroupsMgmt</a>: <i>
      - String</i>
    <a href="#datanetworkid" title="DataNetworkId">DataNetworkId</a>: <i>String</i>
    <a href="#datascripttimeout" title="DatascriptTimeout">DatascriptTimeout</a>: <i>Double</i>
    <a href="#dedicateddispatchercore" title="DedicatedDispatcherCore">DedicatedDispatcherCore</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disableavisecuritygroups" title="DisableAviSecuritygroups">DisableAviSecuritygroups</a>: <i>Boolean</i>
    <a href="#disablecsumoffloads" title="DisableCsumOffloads">DisableCsumOffloads</a>: <i>Boolean</i>
    <a href="#disableflowprobes" title="DisableFlowProbes">DisableFlowProbes</a>: <i>Boolean</i>
    <a href="#disablegro" title="DisableGro">DisableGro</a>: <i>Boolean</i>
    <a href="#disablesememorycheck" title="DisableSeMemoryCheck">DisableSeMemoryCheck</a>: <i>Boolean</i>
    <a href="#disabletso" title="DisableTso">DisableTso</a>: <i>Boolean</i>
    <a href="#diskperse" title="DiskPerSe">DiskPerSe</a>: <i>Double</i>
    <a href="#distributeloadactivestandby" title="DistributeLoadActiveStandby">DistributeLoadActiveStandby</a>: <i>Boolean</i>
    <a href="#distributequeues" title="DistributeQueues">DistributeQueues</a>: <i>Boolean</i>
    <a href="#distributevnics" title="DistributeVnics">DistributeVnics</a>: <i>Boolean</i>
    <a href="#dpaggressivehbfrequency" title="DpAggressiveHbFrequency">DpAggressiveHbFrequency</a>: <i>Double</i>
    <a href="#dpaggressivehbtimeoutcount" title="DpAggressiveHbTimeoutCount">DpAggressiveHbTimeoutCount</a>: <i>Double</i>
    <a href="#dphbfrequency" title="DpHbFrequency">DpHbFrequency</a>: <i>Double</i>
    <a href="#dphbtimeoutcount" title="DpHbTimeoutCount">DpHbTimeoutCount</a>: <i>Double</i>
    <a href="#enablegratarppermanent" title="EnableGratarpPermanent">EnableGratarpPermanent</a>: <i>Boolean</i>
    <a href="#enablehsmpriming" title="EnableHsmPriming">EnableHsmPriming</a>: <i>Boolean</i>
    <a href="#enablemultilb" title="EnableMultiLb">EnableMultiLb</a>: <i>Boolean</i>
    <a href="#enablepcaptxring" title="EnablePcapTxRing">EnablePcapTxRing</a>: <i>Boolean</i>
    <a href="#ephemeralportrangeend" title="EphemeralPortrangeEnd">EphemeralPortrangeEnd</a>: <i>Double</i>
    <a href="#ephemeralportrangestart" title="EphemeralPortrangeStart">EphemeralPortrangeStart</a>: <i>Double</i>
    <a href="#extraconfigmultiplier" title="ExtraConfigMultiplier">ExtraConfigMultiplier</a>: <i>Double</i>
    <a href="#extrasharedconfigmemory" title="ExtraSharedConfigMemory">ExtraSharedConfigMemory</a>: <i>Double</i>
    <a href="#flowtablenewsynmaxentries" title="FlowTableNewSynMaxEntries">FlowTableNewSynMaxEntries</a>: <i>Double</i>
    <a href="#freelistsize" title="FreeListSize">FreeListSize</a>: <i>Double</i>
    <a href="#gratarppermanentperiodicity" title="GratarpPermanentPeriodicity">GratarpPermanentPeriodicity</a>: <i>Double</i>
    <a href="#hamode" title="HaMode">HaMode</a>: <i>String</i>
    <a href="#handleperpktattack" title="HandlePerPktAttack">HandlePerPktAttack</a>: <i>Boolean</i>
    <a href="#hardwaresecuritymodulegroupref" title="HardwaresecuritymodulegroupRef">HardwaresecuritymodulegroupRef</a>: <i>String</i>
    <a href="#heapminimumconfigmemory" title="HeapMinimumConfigMemory">HeapMinimumConfigMemory</a>: <i>Double</i>
    <a href="#hmonstandby" title="HmOnStandby">HmOnStandby</a>: <i>Boolean</i>
    <a href="#hostattributekey" title="HostAttributeKey">HostAttributeKey</a>: <i>String</i>
    <a href="#hostattributevalue" title="HostAttributeValue">HostAttributeValue</a>: <i>String</i>
    <a href="#hostgatewaymonitor" title="HostGatewayMonitor">HostGatewayMonitor</a>: <i>Boolean</i>
    <a href="#hypervisor" title="Hypervisor">Hypervisor</a>: <i>String</i>
    <a href="#ignorerttthreshold" title="IgnoreRttThreshold">IgnoreRttThreshold</a>: <i>Double</i>
    <a href="#ingressaccessdata" title="IngressAccessData">IngressAccessData</a>: <i>String</i>
    <a href="#ingressaccessmgmt" title="IngressAccessMgmt">IngressAccessMgmt</a>: <i>String</i>
    <a href="#instanceflavor" title="InstanceFlavor">InstanceFlavor</a>: <i>String</i>
    <a href="#leastloadcoreselection" title="LeastLoadCoreSelection">LeastLoadCoreSelection</a>: <i>Boolean</i>
    <a href="#licensetier" title="LicenseTier">LicenseTier</a>: <i>String</i>
    <a href="#licensetype" title="LicenseType">LicenseType</a>: <i>String</i>
    <a href="#logdisksz" title="LogDisksz">LogDisksz</a>: <i>Double</i>
    <a href="#logmallocfailure" title="LogMallocFailure">LogMallocFailure</a>: <i>Boolean</i>
    <a href="#maxconcurrentexternalhm" title="MaxConcurrentExternalHm">MaxConcurrentExternalHm</a>: <i>Double</i>
    <a href="#maxcpuusage" title="MaxCpuUsage">MaxCpuUsage</a>: <i>Double</i>
    <a href="#maxmemorypermempool" title="MaxMemoryPerMempool">MaxMemoryPerMempool</a>: <i>Double</i>
    <a href="#maxnumsedps" title="MaxNumSeDps">MaxNumSeDps</a>: <i>Double</i>
    <a href="#maxpublicipsperlb" title="MaxPublicIpsPerLb">MaxPublicIpsPerLb</a>: <i>Double</i>
    <a href="#maxqueuespervnic" title="MaxQueuesPerVnic">MaxQueuesPerVnic</a>: <i>Double</i>
    <a href="#maxrulesperlb" title="MaxRulesPerLb">MaxRulesPerLb</a>: <i>Double</i>
    <a href="#maxscaleoutpervs" title="MaxScaleoutPerVs">MaxScaleoutPerVs</a>: <i>Double</i>
    <a href="#maxse" title="MaxSe">MaxSe</a>: <i>Double</i>
    <a href="#maxvsperse" title="MaxVsPerSe">MaxVsPerSe</a>: <i>Double</i>
    <a href="#memreserve" title="MemReserve">MemReserve</a>: <i>Boolean</i>
    <a href="#memoryforconfigupdate" title="MemoryForConfigUpdate">MemoryForConfigUpdate</a>: <i>Double</i>
    <a href="#memoryperse" title="MemoryPerSe">MemoryPerSe</a>: <i>Double</i>
    <a href="#mgmtnetworkref" title="MgmtNetworkRef">MgmtNetworkRef</a>: <i>String</i>
    <a href="#mincpuusage" title="MinCpuUsage">MinCpuUsage</a>: <i>Double</i>
    <a href="#minscaleoutpervs" title="MinScaleoutPerVs">MinScaleoutPerVs</a>: <i>Double</i>
    <a href="#minse" title="MinSe">MinSe</a>: <i>Double</i>
    <a href="#minimumconnectionmemory" title="MinimumConnectionMemory">MinimumConnectionMemory</a>: <i>Double</i>
    <a href="#nlogstreamingthreads" title="NLogStreamingThreads">NLogStreamingThreads</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nonsignificantlogthrottle" title="NonSignificantLogThrottle">NonSignificantLogThrottle</a>: <i>Double</i>
    <a href="#numdispatchercores" title="NumDispatcherCores">NumDispatcherCores</a>: <i>Double</i>
    <a href="#numflowcoressumchangestoignore" title="NumFlowCoresSumChangesToIgnore">NumFlowCoresSumChangesToIgnore</a>: <i>Double</i>
    <a href="#objsyncport" title="ObjsyncPort">ObjsyncPort</a>: <i>Double</i>
    <a href="#openstackavailabilityzones" title="OpenstackAvailabilityZones">OpenstackAvailabilityZones</a>: <i>
      - String</i>
    <a href="#openstackmgmtnetworkname" title="OpenstackMgmtNetworkName">OpenstackMgmtNetworkName</a>: <i>String</i>
    <a href="#openstackmgmtnetworkuuid" title="OpenstackMgmtNetworkUuid">OpenstackMgmtNetworkUuid</a>: <i>String</i>
    <a href="#osreservedmemory" title="OsReservedMemory">OsReservedMemory</a>: <i>Double</i>
    <a href="#pcaptxmode" title="PcapTxMode">PcapTxMode</a>: <i>String</i>
    <a href="#pcaptxringrdbalancingfactor" title="PcapTxRingRdBalancingFactor">PcapTxRingRdBalancingFactor</a>: <i>Double</i>
    <a href="#perapp" title="PerApp">PerApp</a>: <i>Boolean</i>
    <a href="#pervsadmissioncontrol" title="PerVsAdmissionControl">PerVsAdmissionControl</a>: <i>Boolean</i>
    <a href="#placementmode" title="PlacementMode">PlacementMode</a>: <i>String</i>
    <a href="#rebootonpanic" title="RebootOnPanic">RebootOnPanic</a>: <i>Boolean</i>
    <a href="#resynctimeinterval" title="ResyncTimeInterval">ResyncTimeInterval</a>: <i>Double</i>
    <a href="#sebandwidthtype" title="SeBandwidthType">SeBandwidthType</a>: <i>String</i>
    <a href="#sedelayedflowdelete" title="SeDelayedFlowDelete">SeDelayedFlowDelete</a>: <i>Boolean</i>
    <a href="#sedeprovisiondelay" title="SeDeprovisionDelay">SeDeprovisionDelay</a>: <i>Double</i>
    <a href="#sedphmdrops" title="SeDpHmDrops">SeDpHmDrops</a>: <i>Double</i>
    <a href="#sedpisolation" title="SeDpIsolation">SeDpIsolation</a>: <i>Boolean</i>
    <a href="#sedpisolationnumnondpcpus" title="SeDpIsolationNumNonDpCpus">SeDpIsolationNumNonDpCpus</a>: <i>Double</i>
    <a href="#sedpmaxhbversion" title="SeDpMaxHbVersion">SeDpMaxHbVersion</a>: <i>Double</i>
    <a href="#sedpvnicqueuestalleventsleep" title="SeDpVnicQueueStallEventSleep">SeDpVnicQueueStallEventSleep</a>: <i>Double</i>
    <a href="#sedpvnicqueuestallthreshold" title="SeDpVnicQueueStallThreshold">SeDpVnicQueueStallThreshold</a>: <i>Double</i>
    <a href="#sedpvnicqueuestalltimeout" title="SeDpVnicQueueStallTimeout">SeDpVnicQueueStallTimeout</a>: <i>Double</i>
    <a href="#sedpvnicrestartonqueuestallcount" title="SeDpVnicRestartOnQueueStallCount">SeDpVnicRestartOnQueueStallCount</a>: <i>Double</i>
    <a href="#sedpvnicstallserestartwindow" title="SeDpVnicStallSeRestartWindow">SeDpVnicStallSeRestartWindow</a>: <i>Double</i>
    <a href="#sedpdkpmd" title="SeDpdkPmd">SeDpdkPmd</a>: <i>Double</i>
    <a href="#seflowproberetries" title="SeFlowProbeRetries">SeFlowProbeRetries</a>: <i>Double</i>
    <a href="#seflowproberetrytimer" title="SeFlowProbeRetryTimer">SeFlowProbeRetryTimer</a>: <i>Double</i>
    <a href="#sehyperthreadedmode" title="SeHyperthreadedMode">SeHyperthreadedMode</a>: <i>String</i>
    <a href="#seipencapipc" title="SeIpEncapIpc">SeIpEncapIpc</a>: <i>Double</i>
    <a href="#sekniburstfactor" title="SeKniBurstFactor">SeKniBurstFactor</a>: <i>Double</i>
    <a href="#sel3encapipc" title="SeL3EncapIpc">SeL3EncapIpc</a>: <i>Double</i>
    <a href="#selro" title="SeLro">SeLro</a>: <i>Boolean</i>
    <a href="#sempringretrycount" title="SeMpRingRetryCount">SeMpRingRetryCount</a>: <i>Double</i>
    <a href="#semtu" title="SeMtu">SeMtu</a>: <i>Double</i>
    <a href="#senameprefix" title="SeNamePrefix">SeNamePrefix</a>: <i>String</i>
    <a href="#sepcaplookahead" title="SePcapLookahead">SePcapLookahead</a>: <i>Boolean</i>
    <a href="#sepcappktcount" title="SePcapPktCount">SePcapPktCount</a>: <i>Double</i>
    <a href="#sepcappktsz" title="SePcapPktSz">SePcapPktSz</a>: <i>Double</i>
    <a href="#sepcapqdiscbypass" title="SePcapQdiscBypass">SePcapQdiscBypass</a>: <i>Boolean</i>
    <a href="#sepcapreinitfrequency" title="SePcapReinitFrequency">SePcapReinitFrequency</a>: <i>Double</i>
    <a href="#sepcapreinitthreshold" title="SePcapReinitThreshold">SePcapReinitThreshold</a>: <i>Double</i>
    <a href="#seprobeport" title="SeProbePort">SeProbePort</a>: <i>Double</i>
    <a href="#serumsamplingnavinterval" title="SeRumSamplingNavInterval">SeRumSamplingNavInterval</a>: <i>Double</i>
    <a href="#serumsamplingnavpercent" title="SeRumSamplingNavPercent">SeRumSamplingNavPercent</a>: <i>Double</i>
    <a href="#serumsamplingresinterval" title="SeRumSamplingResInterval">SeRumSamplingResInterval</a>: <i>Double</i>
    <a href="#serumsamplingrespercent" title="SeRumSamplingResPercent">SeRumSamplingResPercent</a>: <i>Double</i>
    <a href="#sesbdedicatedcore" title="SeSbDedicatedCore">SeSbDedicatedCore</a>: <i>Boolean</i>
    <a href="#sesbthreads" title="SeSbThreads">SeSbThreads</a>: <i>Double</i>
    <a href="#sethreadmultiplier" title="SeThreadMultiplier">SeThreadMultiplier</a>: <i>Double</i>
    <a href="#setunnelmode" title="SeTunnelMode">SeTunnelMode</a>: <i>Double</i>
    <a href="#setunneludpport" title="SeTunnelUdpPort">SeTunnelUdpPort</a>: <i>Double</i>
    <a href="#setxbatchsize" title="SeTxBatchSize">SeTxBatchSize</a>: <i>Double</i>
    <a href="#setxqthreshold" title="SeTxqThreshold">SeTxqThreshold</a>: <i>Double</i>
    <a href="#seudpencapipc" title="SeUdpEncapIpc">SeUdpEncapIpc</a>: <i>Double</i>
    <a href="#seusedpdk" title="SeUseDpdk">SeUseDpdk</a>: <i>Double</i>
    <a href="#sevnictxswqueueflushfrequency" title="SeVnicTxSwQueueFlushFrequency">SeVnicTxSwQueueFlushFrequency</a>: <i>Double</i>
    <a href="#sevnictxswqueuesize" title="SeVnicTxSwQueueSize">SeVnicTxSwQueueSize</a>: <i>Double</i>
    <a href="#sevshbmaxpktsinbatch" title="SeVsHbMaxPktsInBatch">SeVsHbMaxPktsInBatch</a>: <i>Double</i>
    <a href="#sevshbmaxvsinpkt" title="SeVsHbMaxVsInPkt">SeVsHbMaxVsInPkt</a>: <i>Double</i>
    <a href="#selfseelection" title="SelfSeElection">SelfSeElection</a>: <i>Boolean</i>
    <a href="#shmminimumconfigmemory" title="ShmMinimumConfigMemory">ShmMinimumConfigMemory</a>: <i>Double</i>
    <a href="#significantlogthrottle" title="SignificantLogThrottle">SignificantLogThrottle</a>: <i>Double</i>
    <a href="#sslpreprocesssnihostname" title="SslPreprocessSniHostname">SslPreprocessSniHostname</a>: <i>Boolean</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#transientsharedmemorymax" title="TransientSharedMemoryMax">TransientSharedMemoryMax</a>: <i>Double</i>
    <a href="#udflogthrottle" title="UdfLogThrottle">UdfLogThrottle</a>: <i>Double</i>
    <a href="#usehyperthreadedcores" title="UseHyperthreadedCores">UseHyperthreadedCores</a>: <i>Boolean</i>
    <a href="#useobjsync" title="UseObjsync">UseObjsync</a>: <i>Boolean</i>
    <a href="#usestandardalb" title="UseStandardAlb">UseStandardAlb</a>: <i>Boolean</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vcenterdatastoremode" title="VcenterDatastoreMode">VcenterDatastoreMode</a>: <i>String</i>
    <a href="#vcenterdatastoresinclude" title="VcenterDatastoresInclude">VcenterDatastoresInclude</a>: <i>Boolean</i>
    <a href="#vcenterfolder" title="VcenterFolder">VcenterFolder</a>: <i>String</i>
    <a href="#vcpusperse" title="VcpusPerSe">VcpusPerSe</a>: <i>Double</i>
    <a href="#vshostredundancy" title="VsHostRedundancy">VsHostRedundancy</a>: <i>Boolean</i>
    <a href="#vsscaleintimeout" title="VsScaleinTimeout">VsScaleinTimeout</a>: <i>Double</i>
    <a href="#vsscaleintimeoutforupgrade" title="VsScaleinTimeoutForUpgrade">VsScaleinTimeoutForUpgrade</a>: <i>Double</i>
    <a href="#vsscaleouttimeout" title="VsScaleoutTimeout">VsScaleoutTimeout</a>: <i>Double</i>
    <a href="#vssescaleoutadditionalwaittime" title="VsSeScaleoutAdditionalWaitTime">VsSeScaleoutAdditionalWaitTime</a>: <i>Double</i>
    <a href="#vssescaleoutreadytimeout" title="VsSeScaleoutReadyTimeout">VsSeScaleoutReadyTimeout</a>: <i>Double</i>
    <a href="#vsswitchovertimeout" title="VsSwitchoverTimeout">VsSwitchoverTimeout</a>: <i>Double</i>
    <a href="#vssplacementenabled" title="VssPlacementEnabled">VssPlacementEnabled</a>: <i>Boolean</i>
    <a href="#wafmempool" title="WafMempool">WafMempool</a>: <i>Boolean</i>
    <a href="#wafmempoolsize" title="WafMempoolSize">WafMempoolSize</a>: <i>Double</i>
    <a href="#customtag" title="CustomTag">CustomTag</a>: <i>
      - <a href="customtagdefinition.md">CustomTagDefinition</a></i>
    <a href="#gcpconfig" title="GcpConfig">GcpConfig</a>: <i>
      - <a href="gcpconfigdefinition.md">GcpConfigDefinition</a></i>
    <a href="#instanceflavorinfo" title="InstanceFlavorInfo">InstanceFlavorInfo</a>: <i>
      - <a href="instanceflavorinfodefinition.md">InstanceFlavorInfoDefinition</a></i>
    <a href="#iptables" title="Iptables">Iptables</a>: <i>
      - <a href="iptablesdefinition.md">IptablesDefinition</a></i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#mgmtsubnet" title="MgmtSubnet">MgmtSubnet</a>: <i>
      - <a href="mgmtsubnetdefinition.md">MgmtSubnetDefinition</a></i>
    <a href="#objsyncconfig" title="ObjsyncConfig">ObjsyncConfig</a>: <i>
      - <a href="objsyncconfigdefinition.md">ObjsyncConfigDefinition</a></i>
    <a href="#realtimesemetrics" title="RealtimeSeMetrics">RealtimeSeMetrics</a>: <i>
      - <a href="realtimesemetricsdefinition.md">RealtimeSeMetricsDefinition</a></i>
    <a href="#sedosprofile" title="SeDosProfile">SeDosProfile</a>: <i>
      - <a href="sedosprofiledefinition.md">SeDosProfileDefinition</a></i>
    <a href="#segroupanalyticspolicy" title="SeGroupAnalyticsPolicy">SeGroupAnalyticsPolicy</a>: <i>
      - <a href="segroupanalyticspolicydefinition.md">SeGroupAnalyticsPolicyDefinition</a></i>
    <a href="#serlprop" title="SeRlProp">SeRlProp</a>: <i>
      - <a href="serlpropdefinition.md">SeRlPropDefinition</a></i>
    <a href="#setracertportrange" title="SeTracertPortRange">SeTracertPortRange</a>: <i>
      - <a href="setracertportrangedefinition.md">SeTracertPortRangeDefinition</a></i>
    <a href="#serviceip6subnets" title="ServiceIp6Subnets">ServiceIp6Subnets</a>: <i>
      - <a href="serviceip6subnetsdefinition.md">ServiceIp6SubnetsDefinition</a></i>
    <a href="#serviceipsubnets" title="ServiceIpSubnets">ServiceIpSubnets</a>: <i>
      - <a href="serviceipsubnetsdefinition.md">ServiceIpSubnetsDefinition</a></i>
    <a href="#vcenterclusters" title="VcenterClusters">VcenterClusters</a>: <i>
      - <a href="vcenterclustersdefinition.md">VcenterClustersDefinition</a></i>
    <a href="#vcenterdatastores" title="VcenterDatastores">VcenterDatastores</a>: <i>
      - <a href="vcenterdatastoresdefinition.md">VcenterDatastoresDefinition</a></i>
    <a href="#vcenterhosts" title="VcenterHosts">VcenterHosts</a>: <i>
      - <a href="vcenterhostsdefinition.md">VcenterHostsDefinition</a></i>
    <a href="#vcenters" title="Vcenters">Vcenters</a>: <i>
      - <a href="vcentersdefinition.md">VcentersDefinition</a></i>
    <a href="#vipasg" title="VipAsg">VipAsg</a>: <i>
      - <a href="vipasgdefinition.md">VipAsgDefinition</a></i>
    <a href="#vssplacement" title="VssPlacement">VssPlacement</a>: <i>
      - <a href="vssplacementdefinition.md">VssPlacementDefinition</a></i>
</pre>

## Properties

#### AcceleratedNetworking

Enable accelerated networking option for azure se. Accelerated networking enables single root i/o virtualization (sr-iov) to a se vm. This improves networking performance. Field introduced in 17.2.14,18.1.5,18.2.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveStandby

Service engines in active/standby mode for ha failover.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AggressiveFailureDetection

Enable aggressive failover configuration for ha. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Algo

In compact placement, virtual services are placed on existing ses until max_vs_per_se limit is reached. Enum options - PLACEMENT_ALGO_PACKED, PLACEMENT_ALGO_DISTRIBUTED.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowBurst

Allow ses to be created using burst license. Field introduced in 17.2.5.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppCachePercent

A percent value of total se memory reserved for applicationcaching. This is an se bootup property and requires se restart.requires se reboot. Allowed values are 0 - 100. Special values are 0- 'disable'. Field introduced in 18.2.3. Unit is percent. Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition. Special default for basic edition is 0, essentials edition is 0, enterprise is 10.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppCacheThreshold

The max memory that can be allocated for the app cache. This value will act as an upper bound on the cache size specified in app_cache_percent. Special values are 0- 'disable'. Field introduced in 20.1.1. Unit is gb.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppLearningMemoryPercent

A percent value of total se memory reserved for application learning. This is an se bootup property and requires se restart. Allowed values are 0 - 10. Field introduced in 18.2.3. Unit is percent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArchiveShmLimit

Amount of se memory in gb until which shared memory is collected in core archive. Field introduced in 17.1.3. Unit is gb.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsyncSsl

Ssl handshakes will be handled by dedicated ssl threads.requires se reboot. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsyncSslThreads

Number of async ssl threads per se_dp.requires se reboot. Allowed values are 1-16.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRebalance

If set, virtual services will be automatically migrated when load on an se is less than minimum or more than maximum thresholds. Only alerts are generated when the auto_rebalance is not set. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRebalanceCapacityPerSe

Capacities of se for auto rebalance for each criteria. Field introduced in 17.2.4.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRebalanceCriteria

Set of criteria for se auto rebalance. Enum options - SE_AUTO_REBALANCE_CPU, SE_AUTO_REBALANCE_PPS, SE_AUTO_REBALANCE_MBPS, SE_AUTO_REBALANCE_OPEN_CONNS, SE_AUTO_REBALANCE_CPS. Field introduced in 17.2.3.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRebalanceInterval

Frequency of rebalance, if 'auto rebalance' is enabled. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRedistributeActiveStandbyLoad

Redistribution of virtual services from the takeover se to the replacement se can cause momentary traffic loss. If the auto-redistribute load option is left in its default off state, any desired rebalancing requires calls to rest api. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZoneRefs

Availability zones for virtual service high availability. It is a reference to an object of type availabilityzone. Field introduced in 20.1.1.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpStateUpdateInterval

Bgp peer state update interval. Allowed values are 5-100. Field introduced in 17.2.14,18.1.5,18.2.1. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BufferSe

Excess service engine capacity provisioned for ha failover.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudRef

It is a reference to an object of type cloud.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressIpRulesForEachNsSubnet

Compress ip rules into a single subnet based ip rule for each north-south ipam subnet configured in pcap mode in openshift/kubernetes node. Field introduced in 18.2.9, 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigDebugsOnAllCores

Enable config debugs on all cores of se. Field introduced in 17.2.13,18.1.5,18.2.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionMemoryPercentage

Percentage of memory for connection state. This will come at the expense of memory used for http in-memory cache. Allowed values are 10-90. Unit is percent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreShmAppCache

Include shared memory for app cache in core file.requires se reboot. Field introduced in 18.2.8, 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreShmAppLearning

Include shared memory for app learning in core file.requires se reboot. Field introduced in 18.2.8, 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuReserve

Boolean flag to set cpu_reserve.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuSocketAffinity

Allocate all the cpu cores for the service engine virtual machines  on the same cpu socket. Applicable only for vcenter cloud.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomSecuritygroupsData

Custom security groups to be associated with data vnics for se instances in openstack and aws clouds. Field introduced in 17.1.3.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomSecuritygroupsMgmt

Custom security groups to be associated with management vnic for se instances in openstack and aws clouds. Field introduced in 17.1.3.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataNetworkId

Subnet used to spin up the data nic for service engines, used only for azure cloud. Overrides the cloud level setting for service engine subnet. Field introduced in 18.2.3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatascriptTimeout

Number of instructions before datascript times out. Allowed values are 0-100000000. Field introduced in 18.2.3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DedicatedDispatcherCore

Dedicate the core that handles packet receive/transmit from the network to just the dispatching function. Don't use it for tcp/ip and ssl functions.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

User defined description for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableAviSecuritygroups

By default, avi creates and manages security groups along with custom sg provided by user. Set this to true to disallow avi to create and manage new security groups. Avi will only make use of custom security groups provided by user. This option is supported for aws and openstack cloud types. Field introduced in 17.2.13,18.1.4,18.2.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableCsumOffloads

Stop using tcp/udp and ip checksum offload features of nics. Field introduced in 17.1.14, 17.2.5, 18.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableFlowProbes

Disable flow probes for scaled out vs'es. Field introduced in 20.1.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableGro

Disable generic receive offload (gro) in dpdk poll-mode driver packet receive path. Gro is on by default on nics that do not support lro (large receive offload) or do not gain performance boost from lro. Field introduced in 17.2.5, 18.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableSeMemoryCheck

If set, disable the config memory check done in service engine. Field introduced in 18.1.2.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableTso

Disable tcp segmentation offload (tso) in dpdk poll-mode driver packet transmit path. Tso is on by default on nics that support it. Field introduced in 17.2.5, 18.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskPerSe

Amount of disk space for each of the service engine virtual machines. Unit is gb.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributeLoadActiveStandby

Use both the active and standby service engines for virtual service placement in the legacy active standby ha mode. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributeQueues

Distributes queue ownership among cores so multiple cores handle dispatcher duties. Requires se reboot. Deprecated from 18.2.8, instead use max_queues_per_vnic. Field introduced in 17.2.8. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributeVnics

Distributes vnic ownership among cores so multiple cores handle dispatcher duties.requires se reboot. Field introduced in 18.2.5.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpAggressiveHbFrequency

Frequency of se - se hb messages when aggressive failure mode detection is enabled. Field introduced in 20.1.3. Unit is milliseconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpAggressiveHbTimeoutCount

Consecutive hb failures after which failure is reported to controller,when aggressive failure mode detection is enabled. Field introduced in 20.1.3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpHbFrequency

Frequency of se - se hb messages when aggressive failure mode detection is not enabled. Field introduced in 20.1.3. Unit is milliseconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpHbTimeoutCount

Consecutive hb failures after which failure is reported to controller, when aggressive failure mode detection is not enabled. Field introduced in 20.1.3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableGratarpPermanent

Enable gratarp for vip_ip. Field introduced in 18.2.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHsmPriming

(this is a beta feature). Enable hsm key priming. If enabled, key handles on the hsm will be synced to se before processing client connections. Field introduced in 17.2.7, 18.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMultiLb

Applicable only for azure cloud with basic sku lb. If set, additional azure lbs will be automatically created if resources in existing lb are exhausted. Field introduced in 17.2.10, 18.1.2.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePcapTxRing

Enable tx ring support in pcap mode of operation. Tso feature is not supported with tx ring enabled. Deprecated from 18.2.8, instead use pcap_tx_mode. Requires se reboot. Field introduced in 18.2.5.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EphemeralPortrangeEnd

End local ephemeral port number for outbound connections. Field introduced in 17.2.13, 18.1.5, 18.2.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EphemeralPortrangeStart

Start local ephemeral port number for outbound connections. Field introduced in 17.2.13, 18.1.5, 18.2.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraConfigMultiplier

Multiplier for extra config to support large vs/pool config.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraSharedConfigMemory

Extra config memory to support large geo db configuration. Field introduced in 17.1.1. Unit is mb.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlowTableNewSynMaxEntries

Maximum number of flow table entries that have not completed tcp three-way handshake yet. Field introduced in 17.2.5.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeListSize

Number of entries in the free list. Field introduced in 17.2.10, 18.1.2.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GratarpPermanentPeriodicity

Gratarp periodicity for vip-ip. Allowed values are 5-30. Field introduced in 18.2.3. Unit is min.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaMode

High availability mode for all the virtual services using this service engine group. Enum options - HA_MODE_SHARED_PAIR, HA_MODE_SHARED, HA_MODE_LEGACY_ACTIVE_STANDBY. Allowed in basic(allowed values- ha_mode_legacy_active_standby) edition, essentials(allowed values- ha_mode_legacy_active_standby) edition, enterprise edition. Special default for basic edition is ha_mode_legacy_active_standby, essentials edition is ha_mode_legacy_active_standby, enterprise is ha_mode_shared.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HandlePerPktAttack

Configuration to handle per packet attack handling.for example, dns reflection attack is a type of attack where a response packet is sent to the dns vs.this configuration tells if such packets should be dropped without further processing. Field introduced in 20.1.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HardwaresecuritymodulegroupRef

It is a reference to an object of type hardwaresecuritymodulegroup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeapMinimumConfigMemory

Minimum required heap memory to apply any configuration. Allowed values are 0-100. Field introduced in 18.1.2. Unit is mb.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HmOnStandby

Enable active health monitoring from the standby se for all placed virtual services. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition. Special default for basic edition is false, essentials edition is false, enterprise is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostAttributeKey

Key of a (key, value) pair identifying a label for a set of nodes usually in container clouds. Needs to be specified together with host_attribute_value. Ses can be configured differently including ha modes across different se groups. May also be used for isolation between different classes of virtualservices. Virtualservices' se group may be specified via annotations/labels. A openshift/kubernetes namespace maybe annotated with a matching se group label as openshift.io/node-selector  apptype=prod. When multiple se groups are used in a cloud with host attributes specified,just a single se group can exist as a match-all se group without a host_attribute_key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostAttributeValue

Value of a (key, value) pair identifying a label for a set of nodes usually in container clouds. Needs to be specified together with host_attribute_key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostGatewayMonitor

Enable the host gateway monitor when service engine is deployed as docker container. Disabled by default. Field introduced in 17.2.4.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hypervisor

Override default hypervisor. Enum options - DEFAULT, VMWARE_ESX, KVM, VMWARE_VSAN, XEN.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreRttThreshold

Ignore rtt samples if it is above threshold. Field introduced in 17.1.6,17.2.2. Unit is milliseconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressAccessData

Program se security group ingress rules to allow vip data access from remote cidr type. Enum options - SG_INGRESS_ACCESS_NONE, SG_INGRESS_ACCESS_ALL, SG_INGRESS_ACCESS_VPC. Field introduced in 17.1.5.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressAccessMgmt

Program se security group ingress rules to allow ssh/icmp management access from remote cidr type. Enum options - SG_INGRESS_ACCESS_NONE, SG_INGRESS_ACCESS_ALL, SG_INGRESS_ACCESS_VPC. Field introduced in 17.1.5.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceFlavor

Instance/flavor name for se instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeastLoadCoreSelection

Select core with least load for new flow.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseTier

Specifies the license tier which would be used. This field by default inherits the value from cloud. Enum options - ENTERPRISE_16, ENTERPRISE, ENTERPRISE_18, BASIC, ESSENTIALS. Field introduced in 17.2.5.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseType

If no license type is specified then default license enforcement for the cloud type is chosen. Enum options - LIC_BACKEND_SERVERS, LIC_SOCKETS, LIC_CORES, LIC_HOSTS, LIC_SE_BANDWIDTH, LIC_METERED_SE_BANDWIDTH. Field introduced in 17.2.5.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogDisksz

Maximum disk capacity (in mb) to be allocated to an se. This is exclusively used for debug and log data. Unit is mb.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogMallocFailure

Se will log memory allocation related failure to the se_trace file, wherever available. Field introduced in 20.1.2. Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentExternalHm

Maximum number of external health monitors that can run concurrently in a service engine. This helps control the cpu and memory use by external health monitors. Special values are 0- 'value will be internally calculated based on cpu and memory'. Field introduced in 18.2.7.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCpuUsage

When cpu usage on an se exceeds this threshold, virtual services hosted on this se may be rebalanced to other ses to reduce load. A new se may be created as part of this process. Allowed values are 40-90. Unit is percent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxMemoryPerMempool

Max bytes that can be allocated in a single mempool. Field introduced in 18.1.5. Unit is mb.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxNumSeDps

Configures the maximum number of se_dp processes created on the se, requires se reboot. If not configured, defaults to the number of cpus on the se. This should only be used if user wants to limit the number of se_dps to less than the available cpus on the se. Allowed values are 1-128. Field introduced in 20.1.1. Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPublicIpsPerLb

Applicable to azure platform only. Maximum number of public ips per azure lb. Field introduced in 17.2.12, 18.1.2.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxQueuesPerVnic

Maximum number of queues per vnic setting to '0' utilises all queues that are distributed across dispatcher cores. Allowed values are 0,1,2,4,8,16. Field introduced in 18.2.7, 20.1.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRulesPerLb

Applicable to azure platform only. Maximum number of rules per azure lb. Field introduced in 17.2.12, 18.1.2.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxScaleoutPerVs

Maximum number of active service engines for the virtual service. Allowed values are 1-64.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSe

Maximum number of services engines in this group. Allowed values are 0-1000.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxVsPerSe

Maximum number of virtual services that can be placed on a single service engine. Allowed values are 1-1000.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemReserve

Boolean flag to set mem_reserve.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryForConfigUpdate

Indicates the percent of memory reserved for config updates. Allowed values are 0-100. Field introduced in 18.1.2. Unit is percent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryPerSe

Amount of memory for each of the service engine virtual machines. Changes to this setting do not affect existing ses.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MgmtNetworkRef

Management network to use for avi service engines. It is a reference to an object of type network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCpuUsage

When cpu usage on an se falls below the minimum threshold, virtual services hosted on the se may be consolidated onto other underutilized ses. After consolidation, unused service engines may then be eligible for deletion. Allowed values are 20-60. Unit is percent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinScaleoutPerVs

Minimum number of active service engines for the virtual service. Allowed values are 1-64.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSe

Minimum number of services engines in this group (relevant for se autorebalance only). Allowed values are 0-1000. Field introduced in 17.2.13,18.1.3,18.2.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumConnectionMemory

Indicates the percent of memory reserved for connections. Allowed values are 0-100. Field introduced in 18.1.2. Unit is percent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NLogStreamingThreads

Number of threads to use for log streaming. Allowed values are 1-100. Field introduced in 17.2.12, 18.1.2.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NonSignificantLogThrottle

This setting limits the number of non-significant logs generated per second per core on this se. Default is 100 logs per second. Set it to zero (0) to deactivate throttling. Field introduced in 17.1.3. Unit is per_second.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumDispatcherCores

Number of dispatcher cores (0,1,2,4,8 or 16). If set to 0, then number of dispatcher cores is deduced automatically.requires se reboot. Allowed values are 0,1,2,4,8,16. Field introduced in 17.2.12, 18.1.3, 18.2.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumFlowCoresSumChangesToIgnore

Number of changes in num flow cores sum to ignore.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjsyncPort

Tcp port on se management interface for interse object distribution. Supported only for externally managed security groups. Not supported on full access deployments. Requires se reboot. Field introduced in 20.1.3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenstackAvailabilityZones

Field introduced in 17.1.1. Maximum of 5 items allowed.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenstackMgmtNetworkName

Avi management network name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenstackMgmtNetworkUuid

Management network uuid.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsReservedMemory

Amount of extra memory to be reserved for use by the operating system on a service engine. Unit is mb.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcapTxMode

Determines the pcap transmit mode of operation. Requires se reboot. Enum options - PCAP_TX_AUTO, PCAP_TX_SOCKET, PCAP_TX_RING. Field introduced in 18.2.8, 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcapTxRingRdBalancingFactor

In pcap mode, reserve a configured portion of tx ring resources for itself and the remaining portion for the rx ring to achieve better balance in terms of queue depth. Requires se reboot. Allowed values are 10-100. Field introduced in 20.1.3. Unit is percent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerApp

Per-app se mode is designed for deploying dedicated load balancers per app (vs). In this mode, each se is limited to a max of 2 vss. Vcpus in per-app ses count towards licensing usage at 25% rate. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerVsAdmissionControl

Enable/disable per vs level admission control.enabling this feature will cause the connection and packet throttling on a particular vs that has high packet buffer consumption. Field introduced in 20.1.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementMode

If placement mode is 'auto', virtual services are automatically placed on service engines. Enum options - PLACEMENT_MODE_AUTO.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RebootOnPanic

Reboot the vm or host on kernel panic. Field introduced in 18.2.5.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResyncTimeInterval

Time interval to re-sync se's time with wall clock time. Allowed values are 8-600000. Field introduced in 20.1.1. Unit is milliseconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeBandwidthType

Select the se bandwidth for the bandwidth license. Enum options - SE_BANDWIDTH_UNLIMITED, SE_BANDWIDTH_25M, SE_BANDWIDTH_200M, SE_BANDWIDTH_1000M, SE_BANDWIDTH_10000M. Field introduced in 17.2.5. Allowed in basic(allowed values- se_bandwidth_unlimited) edition, essentials(allowed values- se_bandwidth_unlimited) edition, enterprise edition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDelayedFlowDelete

Delay the cleanup of flowtable entry. To be used under surveillance of avi support. Field introduced in 20.1.2. Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDeprovisionDelay

Duration to preserve unused service engine virtual machines before deleting them. If traffic to a virtual service were to spike up abruptly, this se would still be available to be utilized again rather than creating a new se. If this value is set to 0, controller will never delete any ses and administrator has to manually cleanup unused ses. Allowed values are 0-525600. Unit is min.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDpHmDrops

Internal only. Used to simulate se - se hb failure. Field introduced in 20.1.3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDpIsolation

Toggle support to run se datapath instances in isolation on exclusive cpus. This improves latency and performance. However, this could reduce the total number of se_dp instances created on that se instance. Supported for >= 8 cpus. Requires se reboot. Field introduced in 20.1.4.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDpIsolationNumNonDpCpus

Number of cpus for non se-dp tasks in se datapath isolation mode. Translates total cpus minus 'num_non_dp_cpus' for datapath use. It is recommended to reserve an even number of cpus for hyper-threaded processors. Requires se reboot. Allowed values are 1-8. Special values are 0- 'auto'. Field introduced in 20.1.4.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDpMaxHbVersion

The highest supported se-se heartbeat protocol version. This version is reported by secondary se to primary se in heartbeat response messages. Allowed values are 1-3. Field introduced in 20.1.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDpVnicQueueStallEventSleep

Time (in seconds) service engine waits for after generating a vnic transmit queue stall event before resetting thenic. Field introduced in 18.2.5.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDpVnicQueueStallThreshold

Number of consecutive transmit failures to look for before generating a vnic transmit queue stall event. Field introduced in 18.2.5.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDpVnicQueueStallTimeout

Time (in milliseconds) to wait for network/nic recovery on detecting a transmit queue stall after which service engine resets the nic. Field introduced in 18.2.5.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDpVnicRestartOnQueueStallCount

Number of consecutive transmit queue stall events in se_dp_vnic_stall_se_restart_window to look for before restarting se. Field introduced in 18.2.5.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDpVnicStallSeRestartWindow

Window of time (in seconds) during which se_dp_vnic_restart_on_queue_stall_count number of consecutive stalls results in a se restart. Field introduced in 18.2.5.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDpdkPmd

Determines if dpdk pool mode driver should be used or not   0  automatically determine based on hypervisor/nic type 1  unconditionally use dpdk poll mode driver 2  don't use dpdk poll mode driver.requires se reboot. Allowed values are 0-2. Field introduced in 18.1.3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeFlowProbeRetries

Flow probe retry count if no replies are received.requires se reboot. Allowed values are 0-5. Field introduced in 18.1.4, 18.2.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeFlowProbeRetryTimer

Timeout in milliseconds for flow probe retries.requires se reboot. Allowed values are 20-50. Field introduced in 18.2.5. Unit is milliseconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeHyperthreadedMode

Controls the distribution of se data path processes on cpus which support hyper-threading. Requires hyper-threading to be enabled at host level. Requires se reboot. For more details please refer to se placement kb. Enum options - SE_CPU_HT_AUTO, SE_CPU_HT_SPARSE_DISPATCHER_PRIORITY, SE_CPU_HT_SPARSE_PROXY_PRIORITY, SE_CPU_HT_PACKED_CORES. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeIpEncapIpc

Determines if se-se ipc messages are encapsulated in an ip header       0        automatically determine based on hypervisor type    1        use ip encap unconditionally    ~[0,1]   don't use ip encaprequires se reboot. Field introduced in 20.1.3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeKniBurstFactor

This knob controls the resource availability and burst size used between se datapath and kni. This helps in minimising packet drops when there is higher kni traffic (non-vip traffic from and to linux). The factor takes the following values      0-default. 1-doubles the burst size and kni resources. 2-quadruples the burst size and kni resources. Allowed values are 0-2. Field introduced in 18.2.6.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeL3EncapIpc

Determines if se-se ipc messages use se interface ip instead of vip        0        automatically determine based on hypervisor type    1        use se interface ip unconditionally    ~[0,1]   don't use se interface iprequires se reboot. Field introduced in 20.1.3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLro

Enable or disable large receive optimization for vnics. Requires se reboot. Field introduced in 18.2.5.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeMpRingRetryCount

The retry count for the multi-producer enqueue before yielding the cpu. To be used under surveillance of avi support. Field introduced in 20.1.3. Allowed in basic(allowed values- 500) edition, essentials(allowed values- 500) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeMtu

Mtu for the vnics of ses in the se group. Allowed values are 512-9000. Field introduced in 18.2.8, 20.1.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeNamePrefix

Prefix to use for virtual machine name of service engines.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SePcapLookahead

Enables lookahead mode of packet receive in pcap mode. Introduced to overcome an issue with hv_netvsc driver. Lookahead mode attempts to ensure that application and kernel's view of the receive rings are consistent. Field introduced in 18.2.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SePcapPktCount

Max number of packets the pcap interface can hold and if the value is 0 the optimum value will be chosen. The optimum value will be chosen based on se-memory, cloud type and number of interfaces.requires se reboot. Field introduced in 18.2.5.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SePcapPktSz

Max size of each packet in the pcap interface. Requires se reboot. Field introduced in 18.2.5.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SePcapQdiscBypass

Bypass the kernel's traffic control layer, to deliver packets directly to the driver. Enabling this feature results in egress packets not being captured in host tcpdump. Note   brief packet reordering or loss may occur upon toggle. Field introduced in 18.2.6.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SePcapReinitFrequency

Frequency in seconds at which periodically a pcap reinit check is triggered. May be used in conjunction with the configuration pcap_reinit_threshold. (valid range   15 mins - 12 hours, 0 - disables). Allowed values are 900-43200. Special values are 0- 'disable'. Field introduced in 17.2.13, 18.1.3, 18.2.1. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SePcapReinitThreshold

Threshold for input packet receive errors in pcap mode exceeding which a pcap reinit is triggered. If not set, an unconditional reinit is performed. This value is checked every pcap_reinit_frequency interval. Field introduced in 17.2.13, 18.1.3, 18.2.1. Unit is metric_count.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeProbePort

Tcp port on se where echo service will be run. Field introduced in 17.2.2.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeRumSamplingNavInterval

Minimum time to wait on server between taking sampleswhen sampling the navigation timing data from the end user client. Field introduced in 18.2.6. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeRumSamplingNavPercent

Percentage of navigation timing data from the end user client, used for sampling to get client insights. Field introduced in 18.2.6.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeRumSamplingResInterval

Minimum time to wait on server between taking sampleswhen sampling the resource timing data from the end user client. Field introduced in 18.2.6. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeRumSamplingResPercent

Percentage of resource timing data from the end user client used for sampling to get client insight. Field introduced in 18.2.6.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeSbDedicatedCore

Sideband traffic will be handled by a dedicated core.requires se reboot. Field introduced in 16.5.2, 17.1.9, 17.2.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeSbThreads

Number of sideband threads per se.requires se reboot. Allowed values are 1-128. Field introduced in 16.5.2, 17.1.9, 17.2.3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeThreadMultiplier

Multiplier for se threads based on vcpu. Allowed values are 1-10. Allowed in basic(allowed values- 1) edition, essentials(allowed values- 1) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeTunnelMode

Determines if direct secondary return (dsr) from secondary se is active or not  0  automatically determine based on hypervisor type. 1  enable tunnel mode - dsr is unconditionally disabled. 2  disable tunnel mode - dsr is unconditionally enabled. Tunnel mode can be enabled or disabled at run-time. Allowed values are 0-2. Field introduced in 17.1.1. Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeTunnelUdpPort

Udp port for tunneled packets from secondary to primary se in docker bridge mode.requires se reboot. Field introduced in 17.1.3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeTxBatchSize

Number of packets to batch for transmit to the nic. Requires se reboot. Field introduced in 18.2.5.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeTxqThreshold

Once the tx queue of the dispatcher reaches this threshold, hardware queues are not polled for further packets. To be used under surveillance of avi support. Allowed values are 512-32768. Field introduced in 20.1.2. Allowed in basic(allowed values- 2048) edition, essentials(allowed values- 2048) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeUdpEncapIpc

Determines if se-se ipc messages are encapsulated in a udp header  0  automatically determine based on hypervisor type. 1  use udp encap unconditionally.requires se reboot. Allowed values are 0-1. Field introduced in 17.1.2.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeUseDpdk

Determines if dpdk library should be used or not   0  automatically determine based on hypervisor type 1  use dpdk if pcap is not enabled 2  don't use dpdk. Allowed values are 0-2. Field introduced in 18.1.3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeVnicTxSwQueueFlushFrequency

Configure the frequency in milliseconds of software transmit spillover queue flush when enabled. This is necessary to flush any packets in the spillover queue in the absence of a packet transmit in the normal course of operation. Allowed values are 50-500. Special values are 0- 'disable'. Field introduced in 20.1.1. Unit is milliseconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeVnicTxSwQueueSize

Configure the size of software transmit spillover queue when enabled. Requires se reboot. Allowed values are 128-2048. Field introduced in 20.1.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeVsHbMaxPktsInBatch

Maximum number of aggregated vs heartbeat packets to send in a batch. Allowed values are 1-256. Field introduced in 17.1.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeVsHbMaxVsInPkt

Maximum number of virtualservices for which heartbeat messages are aggregated in one packet. Allowed values are 1-1024. Field introduced in 17.1.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelfSeElection

Enable ses to elect a primary amongst themselves in the absence of a connectivity to controller. Field introduced in 18.1.2. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShmMinimumConfigMemory

Minimum required shared memory to apply any configuration. Allowed values are 0-100. Field introduced in 18.1.2. Unit is mb.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignificantLogThrottle

This setting limits the number of significant logs generated per second per core on this se. Default is 100 logs per second. Set it to zero (0) to deactivate throttling. Field introduced in 17.1.3. Unit is per_second.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslPreprocessSniHostname

(beta) preprocess ssl client hello for sni hostname extension.if set to true, this will apply sni child's ssl protocol(s), if they are different from sni parent's allowed ssl protocol(s). Field introduced in 17.2.12, 18.1.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransientSharedMemoryMax

The threshold for the transient shared config memory in the se. Allowed values are 0-100. Field introduced in 20.1.1. Unit is percent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdfLogThrottle

This setting limits the number of udf logs generated per second per core on this se. Udf logs are generated due to the configured client log filters or the rules with logging enabled. Default is 100 logs per second. Set it to zero (0) to deactivate throttling. Field introduced in 17.1.3. Unit is per_second.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseHyperthreadedCores

Enables the use of hyper-threaded cores on se. Requires se reboot. Field introduced in 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseObjsync

Enable interse objsyc distribution framework. Field introduced in 20.1.3. Allowed in basic edition, essentials edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseStandardAlb

Use standard sku azure load balancer. By default cloud level flag is set. If not set, it inherits/uses the use_standard_alb flag from the cloud. Field introduced in 18.2.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterDatastoreMode

Enum options - vcenter_datastore_any, vcenter_datastore_local, vcenter_datastore_shared.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterDatastoresInclude

Boolean flag to set vcenter_datastores_include.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterFolder

Folder to place all the service engine virtual machines in vcenter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcpusPerSe

Number of vcpus for each of the service engine virtual machines. Changes to this setting do not affect existing ses.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsHostRedundancy

Ensure primary and secondary service engines are deployed on different physical hosts. Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition. Special default for basic edition is true, essentials edition is true, enterprise is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsScaleinTimeout

Time to wait for the scaled in se to drain existing flows before marking the scalein done. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsScaleinTimeoutForUpgrade

During se upgrade, time to wait for the scaled-in se to drain existing flows before marking the scalein done. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsScaleoutTimeout

Time to wait for the scaled out se to become ready before marking the scaleout done. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsSeScaleoutAdditionalWaitTime

Wait time for sending scaleout ready notification after virtual service is marked up. In certain deployments, there may be an additional delay to accept traffic. For example, for bgp, some time is needed for route advertisement. Allowed values are 0-20. Field introduced in 18.1.5,18.2.1. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsSeScaleoutReadyTimeout

Timeout in seconds for service engine to sendscaleout ready notification of a virtual service. Allowed values are 0-90. Field introduced in 18.1.5,18.2.1. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsSwitchoverTimeout

During se upgrade in a legacy active/standby segroup, time to wait for the new primary se to accept flows before marking the switchover done. Field introduced in 17.2.13,18.1.4,18.2.1. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VssPlacementEnabled

If set, virtual services will be placed on only a subset of the cores of an se. Field introduced in 18.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafMempool

Enable memory pool for waf.requires se reboot. Field introduced in 17.2.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafMempoolSize

Memory pool size used for waf.requires se reboot. Field introduced in 17.2.3. Unit is kb.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomTag

_Required_: No

_Type_: List of <a href="customtagdefinition.md">CustomTagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpConfig

_Required_: No

_Type_: List of <a href="gcpconfigdefinition.md">GcpConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceFlavorInfo

_Required_: No

_Type_: List of <a href="instanceflavorinfodefinition.md">InstanceFlavorInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iptables

_Required_: No

_Type_: List of <a href="iptablesdefinition.md">IptablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MgmtSubnet

_Required_: No

_Type_: List of <a href="mgmtsubnetdefinition.md">MgmtSubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjsyncConfig

_Required_: No

_Type_: List of <a href="objsyncconfigdefinition.md">ObjsyncConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealtimeSeMetrics

_Required_: No

_Type_: List of <a href="realtimesemetricsdefinition.md">RealtimeSeMetricsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDosProfile

_Required_: No

_Type_: List of <a href="sedosprofiledefinition.md">SeDosProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeGroupAnalyticsPolicy

_Required_: No

_Type_: List of <a href="segroupanalyticspolicydefinition.md">SeGroupAnalyticsPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeRlProp

_Required_: No

_Type_: List of <a href="serlpropdefinition.md">SeRlPropDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeTracertPortRange

_Required_: No

_Type_: List of <a href="setracertportrangedefinition.md">SeTracertPortRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceIp6Subnets

_Required_: No

_Type_: List of <a href="serviceip6subnetsdefinition.md">ServiceIp6SubnetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceIpSubnets

_Required_: No

_Type_: List of <a href="serviceipsubnetsdefinition.md">ServiceIpSubnetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterClusters

_Required_: No

_Type_: List of <a href="vcenterclustersdefinition.md">VcenterClustersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterDatastores

_Required_: No

_Type_: List of <a href="vcenterdatastoresdefinition.md">VcenterDatastoresDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterHosts

_Required_: No

_Type_: List of <a href="vcenterhostsdefinition.md">VcenterHostsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vcenters

_Required_: No

_Type_: List of <a href="vcentersdefinition.md">VcentersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipAsg

_Required_: No

_Type_: List of <a href="vipasgdefinition.md">VipAsgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VssPlacement

_Required_: No

_Type_: List of <a href="vssplacementdefinition.md">VssPlacementDefinition</a>

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

