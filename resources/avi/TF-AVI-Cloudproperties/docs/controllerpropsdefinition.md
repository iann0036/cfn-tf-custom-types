# TF::AVI::Cloudproperties ControllerPropsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowadminnetworkupdates" title="AllowAdminNetworkUpdates">AllowAdminNetworkUpdates</a>" : <i>Boolean</i>,
    "<a href="#allowipforwarding" title="AllowIpForwarding">AllowIpForwarding</a>" : <i>Boolean</i>,
    "<a href="#allowunauthenticatedapis" title="AllowUnauthenticatedApis">AllowUnauthenticatedApis</a>" : <i>Boolean</i>,
    "<a href="#allowunauthenticatednodes" title="AllowUnauthenticatedNodes">AllowUnauthenticatedNodes</a>" : <i>Boolean</i>,
    "<a href="#apiidletimeout" title="ApiIdleTimeout">ApiIdleTimeout</a>" : <i>Double</i>,
    "<a href="#apiperfloggingthreshold" title="ApiPerfLoggingThreshold">ApiPerfLoggingThreshold</a>" : <i>Double</i>,
    "<a href="#appviewxcompatmode" title="AppviewxCompatMode">AppviewxCompatMode</a>" : <i>Boolean</i>,
    "<a href="#asyncpatchmergeperiod" title="AsyncPatchMergePeriod">AsyncPatchMergePeriod</a>" : <i>Double</i>,
    "<a href="#asyncpatchrequestcleanupduration" title="AsyncPatchRequestCleanupDuration">AsyncPatchRequestCleanupDuration</a>" : <i>Double</i>,
    "<a href="#attachipretryinterval" title="AttachIpRetryInterval">AttachIpRetryInterval</a>" : <i>Double</i>,
    "<a href="#attachipretrylimit" title="AttachIpRetryLimit">AttachIpRetryLimit</a>" : <i>Double</i>,
    "<a href="#bmuseansible" title="BmUseAnsible">BmUseAnsible</a>" : <i>Boolean</i>,
    "<a href="#checkvsvipfqdnsyntax" title="CheckVsvipFqdnSyntax">CheckVsvipFqdnSyntax</a>" : <i>Boolean</i>,
    "<a href="#cleanupexpiredauthtokentimeoutperiod" title="CleanupExpiredAuthtokenTimeoutPeriod">CleanupExpiredAuthtokenTimeoutPeriod</a>" : <i>Double</i>,
    "<a href="#cleanupsessionstimeoutperiod" title="CleanupSessionsTimeoutPeriod">CleanupSessionsTimeoutPeriod</a>" : <i>Double</i>,
    "<a href="#cloudreconcile" title="CloudReconcile">CloudReconcile</a>" : <i>Boolean</i>,
    "<a href="#clusteripgratuitousarpperiod" title="ClusterIpGratuitousArpPeriod">ClusterIpGratuitousArpPeriod</a>" : <i>Double</i>,
    "<a href="#consistencychecktimeoutperiod" title="ConsistencyCheckTimeoutPeriod">ConsistencyCheckTimeoutPeriod</a>" : <i>Double</i>,
    "<a href="#controllerresourceinfocollectionperiod" title="ControllerResourceInfoCollectionPeriod">ControllerResourceInfoCollectionPeriod</a>" : <i>Double</i>,
    "<a href="#crashedsereboot" title="CrashedSeReboot">CrashedSeReboot</a>" : <i>Double</i>,
    "<a href="#deadsedetectiontimer" title="DeadSeDetectionTimer">DeadSeDetectionTimer</a>" : <i>Double</i>,
    "<a href="#defaultminimumapitimeout" title="DefaultMinimumApiTimeout">DefaultMinimumApiTimeout</a>" : <i>Double</i>,
    "<a href="#delofflineseafterrebootdelay" title="DelOfflineSeAfterRebootDelay">DelOfflineSeAfterRebootDelay</a>" : <i>Double</i>,
    "<a href="#dnsrefreshperiod" title="DnsRefreshPeriod">DnsRefreshPeriod</a>" : <i>Double</i>,
    "<a href="#dummy" title="Dummy">Dummy</a>" : <i>Double</i>,
    "<a href="#editsystemlimits" title="EditSystemLimits">EditSystemLimits</a>" : <i>Boolean</i>,
    "<a href="#enableapisharding" title="EnableApiSharding">EnableApiSharding</a>" : <i>Boolean</i>,
    "<a href="#enablememorybalancer" title="EnableMemoryBalancer">EnableMemoryBalancer</a>" : <i>Boolean</i>,
    "<a href="#enableresmgrlogcacheprint" title="EnableResmgrLogCachePrint">EnableResmgrLogCachePrint</a>" : <i>Boolean</i>,
    "<a href="#fatalerrorleasetime" title="FatalErrorLeaseTime">FatalErrorLeaseTime</a>" : <i>Double</i>,
    "<a href="#federateddatastorecleanupduration" title="FederatedDatastoreCleanupDuration">FederatedDatastoreCleanupDuration</a>" : <i>Double</i>,
    "<a href="#fileobjectcleanupperiod" title="FileObjectCleanupPeriod">FileObjectCleanupPeriod</a>" : <i>Double</i>,
    "<a href="#maxdeadseingrp" title="MaxDeadSeInGrp">MaxDeadSeInGrp</a>" : <i>Double</i>,
    "<a href="#maxpcappertenant" title="MaxPcapPerTenant">MaxPcapPerTenant</a>" : <i>Double</i>,
    "<a href="#maxsespawnintervaldelay" title="MaxSeSpawnIntervalDelay">MaxSeSpawnIntervalDelay</a>" : <i>Double</i>,
    "<a href="#maxseqattachipfailures" title="MaxSeqAttachIpFailures">MaxSeqAttachIpFailures</a>" : <i>Double</i>,
    "<a href="#maxseqvnicfailures" title="MaxSeqVnicFailures">MaxSeqVnicFailures</a>" : <i>Double</i>,
    "<a href="#maxthreadsccvipbgworker" title="MaxThreadsCcVipBgWorker">MaxThreadsCcVipBgWorker</a>" : <i>Double</i>,
    "<a href="#permissionscopedsharedadminnetworks" title="PermissionScopedSharedAdminNetworks">PermissionScopedSharedAdminNetworks</a>" : <i>Boolean</i>,
    "<a href="#persistencekeyrotateperiod" title="PersistenceKeyRotatePeriod">PersistenceKeyRotatePeriod</a>" : <i>Double</i>,
    "<a href="#portalrequestburstlimit" title="PortalRequestBurstLimit">PortalRequestBurstLimit</a>" : <i>Double</i>,
    "<a href="#portalrequestratelimit" title="PortalRequestRateLimit">PortalRequestRateLimit</a>" : <i>Double</i>,
    "<a href="#portaltoken" title="PortalToken">PortalToken</a>" : <i>String</i>,
    "<a href="#processlockeduseraccountstimeoutperiod" title="ProcessLockedUseraccountsTimeoutPeriod">ProcessLockedUseraccountsTimeoutPeriod</a>" : <i>Double</i>,
    "<a href="#processpkiprofiletimeoutperiod" title="ProcessPkiProfileTimeoutPeriod">ProcessPkiProfileTimeoutPeriod</a>" : <i>Double</i>,
    "<a href="#queryhostfail" title="QueryHostFail">QueryHostFail</a>" : <i>Double</i>,
    "<a href="#resmgrlogcachingperiod" title="ResmgrLogCachingPeriod">ResmgrLogCachingPeriod</a>" : <i>Double</i>,
    "<a href="#safenethsmversion" title="SafenetHsmVersion">SafenetHsmVersion</a>" : <i>String</i>,
    "<a href="#secreatetimeout" title="SeCreateTimeout">SeCreateTimeout</a>" : <i>Double</i>,
    "<a href="#sefailoverattemptinterval" title="SeFailoverAttemptInterval">SeFailoverAttemptInterval</a>" : <i>Double</i>,
    "<a href="#sefrommarketplace" title="SeFromMarketplace">SeFromMarketplace</a>" : <i>String</i>,
    "<a href="#seofflinedel" title="SeOfflineDel">SeOfflineDel</a>" : <i>Double</i>,
    "<a href="#sespawnretryinterval" title="SeSpawnRetryInterval">SeSpawnRetryInterval</a>" : <i>Double</i>,
    "<a href="#sevniccooldown" title="SeVnicCooldown">SeVnicCooldown</a>" : <i>Double</i>,
    "<a href="#sevnicgcwaittime" title="SeVnicGcWaitTime">SeVnicGcWaitTime</a>" : <i>Double</i>,
    "<a href="#securechannelcleanuptimeout" title="SecureChannelCleanupTimeout">SecureChannelCleanupTimeout</a>" : <i>Double</i>,
    "<a href="#securechannelcontrollertokentimeout" title="SecureChannelControllerTokenTimeout">SecureChannelControllerTokenTimeout</a>" : <i>Double</i>,
    "<a href="#securechannelsetokentimeout" title="SecureChannelSeTokenTimeout">SecureChannelSeTokenTimeout</a>" : <i>Double</i>,
    "<a href="#seupgradecopypoolsize" title="SeupgradeCopyPoolSize">SeupgradeCopyPoolSize</a>" : <i>Double</i>,
    "<a href="#seupgradefabricpoolsize" title="SeupgradeFabricPoolSize">SeupgradeFabricPoolSize</a>" : <i>Double</i>,
    "<a href="#seupgradesegroupmindeadtimeout" title="SeupgradeSegroupMinDeadTimeout">SeupgradeSegroupMinDeadTimeout</a>" : <i>Double</i>,
    "<a href="#sharedsslcertificates" title="SharedSslCertificates">SharedSslCertificates</a>" : <i>Boolean</i>,
    "<a href="#sslcertificateexpirywarningdays" title="SslCertificateExpiryWarningDays">SslCertificateExpiryWarningDays</a>" : <i>[ Double, ... ]</i>,
    "<a href="#unresponsivesereboot" title="UnresponsiveSeReboot">UnresponsiveSeReboot</a>" : <i>Double</i>,
    "<a href="#upgradednsttl" title="UpgradeDnsTtl">UpgradeDnsTtl</a>" : <i>Double</i>,
    "<a href="#upgradefatseleasetime" title="UpgradeFatSeLeaseTime">UpgradeFatSeLeaseTime</a>" : <i>Double</i>,
    "<a href="#upgradeleasetime" title="UpgradeLeaseTime">UpgradeLeaseTime</a>" : <i>Double</i>,
    "<a href="#upgradesepervsscaleopstxntime" title="UpgradeSePerVsScaleOpsTxnTime">UpgradeSePerVsScaleOpsTxnTime</a>" : <i>Double</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#vnicopfailtime" title="VnicOpFailTime">VnicOpFailTime</a>" : <i>Double</i>,
    "<a href="#vsapicscaleouttimeout" title="VsApicScaleoutTimeout">VsApicScaleoutTimeout</a>" : <i>Double</i>,
    "<a href="#vsawaitingsetimeout" title="VsAwaitingSeTimeout">VsAwaitingSeTimeout</a>" : <i>Double</i>,
    "<a href="#vskeyrotateperiod" title="VsKeyRotatePeriod">VsKeyRotatePeriod</a>" : <i>Double</i>,
    "<a href="#vsscaleoutreadycheckinterval" title="VsScaleoutReadyCheckInterval">VsScaleoutReadyCheckInterval</a>" : <i>Double</i>,
    "<a href="#vsseattachipfail" title="VsSeAttachIpFail">VsSeAttachIpFail</a>" : <i>Double</i>,
    "<a href="#vssebootupfail" title="VsSeBootupFail">VsSeBootupFail</a>" : <i>Double</i>,
    "<a href="#vssecreatefail" title="VsSeCreateFail">VsSeCreateFail</a>" : <i>Double</i>,
    "<a href="#vssepingfail" title="VsSePingFail">VsSePingFail</a>" : <i>Double</i>,
    "<a href="#vssevnicfail" title="VsSeVnicFail">VsSeVnicFail</a>" : <i>Double</i>,
    "<a href="#vssevnicipfail" title="VsSeVnicIpFail">VsSeVnicIpFail</a>" : <i>Double</i>,
    "<a href="#warmstartsereconnectwaittime" title="WarmstartSeReconnectWaitTime">WarmstartSeReconnectWaitTime</a>" : <i>Double</i>,
    "<a href="#warmstartvsresyncwaittime" title="WarmstartVsResyncWaitTime">WarmstartVsResyncWaitTime</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#allowadminnetworkupdates" title="AllowAdminNetworkUpdates">AllowAdminNetworkUpdates</a>: <i>Boolean</i>
<a href="#allowipforwarding" title="AllowIpForwarding">AllowIpForwarding</a>: <i>Boolean</i>
<a href="#allowunauthenticatedapis" title="AllowUnauthenticatedApis">AllowUnauthenticatedApis</a>: <i>Boolean</i>
<a href="#allowunauthenticatednodes" title="AllowUnauthenticatedNodes">AllowUnauthenticatedNodes</a>: <i>Boolean</i>
<a href="#apiidletimeout" title="ApiIdleTimeout">ApiIdleTimeout</a>: <i>Double</i>
<a href="#apiperfloggingthreshold" title="ApiPerfLoggingThreshold">ApiPerfLoggingThreshold</a>: <i>Double</i>
<a href="#appviewxcompatmode" title="AppviewxCompatMode">AppviewxCompatMode</a>: <i>Boolean</i>
<a href="#asyncpatchmergeperiod" title="AsyncPatchMergePeriod">AsyncPatchMergePeriod</a>: <i>Double</i>
<a href="#asyncpatchrequestcleanupduration" title="AsyncPatchRequestCleanupDuration">AsyncPatchRequestCleanupDuration</a>: <i>Double</i>
<a href="#attachipretryinterval" title="AttachIpRetryInterval">AttachIpRetryInterval</a>: <i>Double</i>
<a href="#attachipretrylimit" title="AttachIpRetryLimit">AttachIpRetryLimit</a>: <i>Double</i>
<a href="#bmuseansible" title="BmUseAnsible">BmUseAnsible</a>: <i>Boolean</i>
<a href="#checkvsvipfqdnsyntax" title="CheckVsvipFqdnSyntax">CheckVsvipFqdnSyntax</a>: <i>Boolean</i>
<a href="#cleanupexpiredauthtokentimeoutperiod" title="CleanupExpiredAuthtokenTimeoutPeriod">CleanupExpiredAuthtokenTimeoutPeriod</a>: <i>Double</i>
<a href="#cleanupsessionstimeoutperiod" title="CleanupSessionsTimeoutPeriod">CleanupSessionsTimeoutPeriod</a>: <i>Double</i>
<a href="#cloudreconcile" title="CloudReconcile">CloudReconcile</a>: <i>Boolean</i>
<a href="#clusteripgratuitousarpperiod" title="ClusterIpGratuitousArpPeriod">ClusterIpGratuitousArpPeriod</a>: <i>Double</i>
<a href="#consistencychecktimeoutperiod" title="ConsistencyCheckTimeoutPeriod">ConsistencyCheckTimeoutPeriod</a>: <i>Double</i>
<a href="#controllerresourceinfocollectionperiod" title="ControllerResourceInfoCollectionPeriod">ControllerResourceInfoCollectionPeriod</a>: <i>Double</i>
<a href="#crashedsereboot" title="CrashedSeReboot">CrashedSeReboot</a>: <i>Double</i>
<a href="#deadsedetectiontimer" title="DeadSeDetectionTimer">DeadSeDetectionTimer</a>: <i>Double</i>
<a href="#defaultminimumapitimeout" title="DefaultMinimumApiTimeout">DefaultMinimumApiTimeout</a>: <i>Double</i>
<a href="#delofflineseafterrebootdelay" title="DelOfflineSeAfterRebootDelay">DelOfflineSeAfterRebootDelay</a>: <i>Double</i>
<a href="#dnsrefreshperiod" title="DnsRefreshPeriod">DnsRefreshPeriod</a>: <i>Double</i>
<a href="#dummy" title="Dummy">Dummy</a>: <i>Double</i>
<a href="#editsystemlimits" title="EditSystemLimits">EditSystemLimits</a>: <i>Boolean</i>
<a href="#enableapisharding" title="EnableApiSharding">EnableApiSharding</a>: <i>Boolean</i>
<a href="#enablememorybalancer" title="EnableMemoryBalancer">EnableMemoryBalancer</a>: <i>Boolean</i>
<a href="#enableresmgrlogcacheprint" title="EnableResmgrLogCachePrint">EnableResmgrLogCachePrint</a>: <i>Boolean</i>
<a href="#fatalerrorleasetime" title="FatalErrorLeaseTime">FatalErrorLeaseTime</a>: <i>Double</i>
<a href="#federateddatastorecleanupduration" title="FederatedDatastoreCleanupDuration">FederatedDatastoreCleanupDuration</a>: <i>Double</i>
<a href="#fileobjectcleanupperiod" title="FileObjectCleanupPeriod">FileObjectCleanupPeriod</a>: <i>Double</i>
<a href="#maxdeadseingrp" title="MaxDeadSeInGrp">MaxDeadSeInGrp</a>: <i>Double</i>
<a href="#maxpcappertenant" title="MaxPcapPerTenant">MaxPcapPerTenant</a>: <i>Double</i>
<a href="#maxsespawnintervaldelay" title="MaxSeSpawnIntervalDelay">MaxSeSpawnIntervalDelay</a>: <i>Double</i>
<a href="#maxseqattachipfailures" title="MaxSeqAttachIpFailures">MaxSeqAttachIpFailures</a>: <i>Double</i>
<a href="#maxseqvnicfailures" title="MaxSeqVnicFailures">MaxSeqVnicFailures</a>: <i>Double</i>
<a href="#maxthreadsccvipbgworker" title="MaxThreadsCcVipBgWorker">MaxThreadsCcVipBgWorker</a>: <i>Double</i>
<a href="#permissionscopedsharedadminnetworks" title="PermissionScopedSharedAdminNetworks">PermissionScopedSharedAdminNetworks</a>: <i>Boolean</i>
<a href="#persistencekeyrotateperiod" title="PersistenceKeyRotatePeriod">PersistenceKeyRotatePeriod</a>: <i>Double</i>
<a href="#portalrequestburstlimit" title="PortalRequestBurstLimit">PortalRequestBurstLimit</a>: <i>Double</i>
<a href="#portalrequestratelimit" title="PortalRequestRateLimit">PortalRequestRateLimit</a>: <i>Double</i>
<a href="#portaltoken" title="PortalToken">PortalToken</a>: <i>String</i>
<a href="#processlockeduseraccountstimeoutperiod" title="ProcessLockedUseraccountsTimeoutPeriod">ProcessLockedUseraccountsTimeoutPeriod</a>: <i>Double</i>
<a href="#processpkiprofiletimeoutperiod" title="ProcessPkiProfileTimeoutPeriod">ProcessPkiProfileTimeoutPeriod</a>: <i>Double</i>
<a href="#queryhostfail" title="QueryHostFail">QueryHostFail</a>: <i>Double</i>
<a href="#resmgrlogcachingperiod" title="ResmgrLogCachingPeriod">ResmgrLogCachingPeriod</a>: <i>Double</i>
<a href="#safenethsmversion" title="SafenetHsmVersion">SafenetHsmVersion</a>: <i>String</i>
<a href="#secreatetimeout" title="SeCreateTimeout">SeCreateTimeout</a>: <i>Double</i>
<a href="#sefailoverattemptinterval" title="SeFailoverAttemptInterval">SeFailoverAttemptInterval</a>: <i>Double</i>
<a href="#sefrommarketplace" title="SeFromMarketplace">SeFromMarketplace</a>: <i>String</i>
<a href="#seofflinedel" title="SeOfflineDel">SeOfflineDel</a>: <i>Double</i>
<a href="#sespawnretryinterval" title="SeSpawnRetryInterval">SeSpawnRetryInterval</a>: <i>Double</i>
<a href="#sevniccooldown" title="SeVnicCooldown">SeVnicCooldown</a>: <i>Double</i>
<a href="#sevnicgcwaittime" title="SeVnicGcWaitTime">SeVnicGcWaitTime</a>: <i>Double</i>
<a href="#securechannelcleanuptimeout" title="SecureChannelCleanupTimeout">SecureChannelCleanupTimeout</a>: <i>Double</i>
<a href="#securechannelcontrollertokentimeout" title="SecureChannelControllerTokenTimeout">SecureChannelControllerTokenTimeout</a>: <i>Double</i>
<a href="#securechannelsetokentimeout" title="SecureChannelSeTokenTimeout">SecureChannelSeTokenTimeout</a>: <i>Double</i>
<a href="#seupgradecopypoolsize" title="SeupgradeCopyPoolSize">SeupgradeCopyPoolSize</a>: <i>Double</i>
<a href="#seupgradefabricpoolsize" title="SeupgradeFabricPoolSize">SeupgradeFabricPoolSize</a>: <i>Double</i>
<a href="#seupgradesegroupmindeadtimeout" title="SeupgradeSegroupMinDeadTimeout">SeupgradeSegroupMinDeadTimeout</a>: <i>Double</i>
<a href="#sharedsslcertificates" title="SharedSslCertificates">SharedSslCertificates</a>: <i>Boolean</i>
<a href="#sslcertificateexpirywarningdays" title="SslCertificateExpiryWarningDays">SslCertificateExpiryWarningDays</a>: <i>
      - Double</i>
<a href="#unresponsivesereboot" title="UnresponsiveSeReboot">UnresponsiveSeReboot</a>: <i>Double</i>
<a href="#upgradednsttl" title="UpgradeDnsTtl">UpgradeDnsTtl</a>: <i>Double</i>
<a href="#upgradefatseleasetime" title="UpgradeFatSeLeaseTime">UpgradeFatSeLeaseTime</a>: <i>Double</i>
<a href="#upgradeleasetime" title="UpgradeLeaseTime">UpgradeLeaseTime</a>: <i>Double</i>
<a href="#upgradesepervsscaleopstxntime" title="UpgradeSePerVsScaleOpsTxnTime">UpgradeSePerVsScaleOpsTxnTime</a>: <i>Double</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#vnicopfailtime" title="VnicOpFailTime">VnicOpFailTime</a>: <i>Double</i>
<a href="#vsapicscaleouttimeout" title="VsApicScaleoutTimeout">VsApicScaleoutTimeout</a>: <i>Double</i>
<a href="#vsawaitingsetimeout" title="VsAwaitingSeTimeout">VsAwaitingSeTimeout</a>: <i>Double</i>
<a href="#vskeyrotateperiod" title="VsKeyRotatePeriod">VsKeyRotatePeriod</a>: <i>Double</i>
<a href="#vsscaleoutreadycheckinterval" title="VsScaleoutReadyCheckInterval">VsScaleoutReadyCheckInterval</a>: <i>Double</i>
<a href="#vsseattachipfail" title="VsSeAttachIpFail">VsSeAttachIpFail</a>: <i>Double</i>
<a href="#vssebootupfail" title="VsSeBootupFail">VsSeBootupFail</a>: <i>Double</i>
<a href="#vssecreatefail" title="VsSeCreateFail">VsSeCreateFail</a>: <i>Double</i>
<a href="#vssepingfail" title="VsSePingFail">VsSePingFail</a>: <i>Double</i>
<a href="#vssevnicfail" title="VsSeVnicFail">VsSeVnicFail</a>: <i>Double</i>
<a href="#vssevnicipfail" title="VsSeVnicIpFail">VsSeVnicIpFail</a>: <i>Double</i>
<a href="#warmstartsereconnectwaittime" title="WarmstartSeReconnectWaitTime">WarmstartSeReconnectWaitTime</a>: <i>Double</i>
<a href="#warmstartvsresyncwaittime" title="WarmstartVsResyncWaitTime">WarmstartVsResyncWaitTime</a>: <i>Double</i>
</pre>

## Properties

#### AllowAdminNetworkUpdates

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowIpForwarding

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowUnauthenticatedApis

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowUnauthenticatedNodes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiIdleTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiPerfLoggingThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppviewxCompatMode

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsyncPatchMergePeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsyncPatchRequestCleanupDuration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachIpRetryInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachIpRetryLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BmUseAnsible

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckVsvipFqdnSyntax

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CleanupExpiredAuthtokenTimeoutPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CleanupSessionsTimeoutPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudReconcile

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterIpGratuitousArpPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsistencyCheckTimeoutPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerResourceInfoCollectionPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrashedSeReboot

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeadSeDetectionTimer

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultMinimumApiTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelOfflineSeAfterRebootDelay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsRefreshPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dummy

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EditSystemLimits

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableApiSharding

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMemoryBalancer

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableResmgrLogCachePrint

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FatalErrorLeaseTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FederatedDatastoreCleanupDuration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileObjectCleanupPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDeadSeInGrp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPcapPerTenant

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSeSpawnIntervalDelay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSeqAttachIpFailures

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSeqVnicFailures

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxThreadsCcVipBgWorker

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissionScopedSharedAdminNetworks

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistenceKeyRotatePeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortalRequestBurstLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortalRequestRateLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortalToken

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessLockedUseraccountsTimeoutPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessPkiProfileTimeoutPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryHostFail

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResmgrLogCachingPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SafenetHsmVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeCreateTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeFailoverAttemptInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeFromMarketplace

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeOfflineDel

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeSpawnRetryInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeVnicCooldown

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeVnicGcWaitTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureChannelCleanupTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureChannelControllerTokenTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureChannelSeTokenTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeupgradeCopyPoolSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeupgradeFabricPoolSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeupgradeSegroupMinDeadTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedSslCertificates

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertificateExpiryWarningDays

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnresponsiveSeReboot

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeDnsTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeFatSeLeaseTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeLeaseTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeSePerVsScaleOpsTxnTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnicOpFailTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsApicScaleoutTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsAwaitingSeTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsKeyRotatePeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsScaleoutReadyCheckInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsSeAttachIpFail

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsSeBootupFail

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsSeCreateFail

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsSePingFail

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsSeVnicFail

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsSeVnicIpFail

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarmstartSeReconnectWaitTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarmstartVsResyncWaitTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

