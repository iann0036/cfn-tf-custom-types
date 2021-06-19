# TF::AVI::Controllerproperties

The ControllerProperties resource allows the creation and management of Avi ControllerProperties

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Controllerproperties",
    "Properties" : {
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
}
</pre>

### YAML

<pre>
Type: TF::AVI::Controllerproperties
Properties:
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

Allow non-admin tenants to update admin vrfcontext and network objects. Field introduced in 18.2.7, 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowIpForwarding

Field introduced in 17.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowUnauthenticatedApis

Allow unauthenticated access for special apis.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowUnauthenticatedNodes

Boolean flag to set allow_unauthenticated_nodes.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiIdleTimeout

Allowed values are 0-1440. Unit is min.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiPerfLoggingThreshold

Threshold to log request timing in portal_performance.log and server-timing response header. Any stage taking longer than 1% of the threshold will be included in the server-timing header. Field introduced in 18.1.4, 18.2.1. Unit is milliseconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppviewxCompatMode

Export configuration in appviewx compatibility mode. Field introduced in 17.1.1. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsyncPatchMergePeriod

Period for which asynchronous patch requests are queued. Allowed values are 30-120. Special values are 0 - 'deactivated'. Field introduced in 18.2.11, 20.1.3. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsyncPatchRequestCleanupDuration

Duration for which asynchronous patch requests should be kept, after being marked as success or fail. Allowed values are 5-120. Field introduced in 18.2.11, 20.1.3. Unit is min.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachIpRetryInterval

Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachIpRetryLimit

Placeholder for description of property attach_ip_retry_limit of obj type controllerproperties field type integer  type int.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BmUseAnsible

Use ansible for se creation in baremetal. Field introduced in 17.2.2.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckVsvipFqdnSyntax

Enforce vsvip fqdn syntax checks. Field introduced in 20.1.6. Allowed in basic edition, essentials edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CleanupExpiredAuthtokenTimeoutPeriod

Period for auth token cleanup job. Field introduced in 18.1.1. Unit is min.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CleanupSessionsTimeoutPeriod

Period for sessions cleanup job. Field introduced in 18.1.1. Unit is min.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudReconcile

Enable/disable periodic reconcile for all the clouds. Field introduced in 17.2.14,18.1.5,18.2.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterIpGratuitousArpPeriod

Period for cluster ip gratuitous arp job. Unit is min.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsistencyCheckTimeoutPeriod

Period for consistency check job. Field introduced in 18.1.1. Unit is min.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerResourceInfoCollectionPeriod

Periodically collect stats. Field introduced in 20.1.3. Unit is min.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrashedSeReboot

Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeadSeDetectionTimer

Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultMinimumApiTimeout

Minimum api timeout value.if this value is not 60, it will be the default timeout for all apis that do not have a specific timeout.if an api has a specific timeout but is less than this value, this value will become the new timeout. Allowed values are 60-3600. Field introduced in 18.2.6. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelOfflineSeAfterRebootDelay

The amount of time the controller will wait before deleting an offline se after it has been rebooted. For unresponsive ses, the total time will be  unresponsive_se_reboot + del_offline_se_after_reboot_delay. For crashed ses, the total time will be crashed_se_reboot + del_offline_se_after_reboot_delay. Field introduced in 20.1.5. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsRefreshPeriod

Period for refresh pool and gslb dns job. Unit is min. Allowed in basic(allowed values- 60) edition, essentials(allowed values- 60) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dummy

Placeholder for description of property dummy of obj type controllerproperties field type integer  type int.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EditSystemLimits

Allow editing of system limits. Keep in mind that these system limits have been carefully selected based on rigorous testing in our testig environments. Modifying these limits could destabilize your cluster. Do this at your own risk!. Field introduced in 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableApiSharding

This setting enables the controller leader to shard api requests to the followers (if any). Field introduced in 18.1.5, 18.2.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMemoryBalancer

Enable/disable memory balancer. Field introduced in 17.2.8.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableResmgrLogCachePrint

Enable printing of cached logs inside resource manager. Used for debugging purposes only. Field introduced in 20.1.6.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FatalErrorLeaseTime

Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FederatedDatastoreCleanupDuration

Federated datastore will not cleanup diffs unless they are at least this duration in the past. Field introduced in 20.1.1. Unit is hours.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileObjectCleanupPeriod

Period for file object cleanup job. Field introduced in 20.1.1. Unit is min.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDeadSeInGrp

Placeholder for description of property max_dead_se_in_grp of obj type controllerproperties field type integer  type int.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPcapPerTenant

Maximum number of pcap files stored per tenant.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSeSpawnIntervalDelay

Maximum delay possible to add to se_spawn_retry_interval after successive se spawn failure. Field introduced in 20.1.1. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSeqAttachIpFailures

Maximum number of consecutive attach ip failures that halts vs placement. Field introduced in 17.2.2.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSeqVnicFailures

Placeholder for description of property max_seq_vnic_failures of obj type controllerproperties field type integer  type int.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxThreadsCcVipBgWorker

Maximum number of threads in threadpool used by cloud connector ccvipbgworker. Allowed values are 1-100. Field introduced in 20.1.3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissionScopedSharedAdminNetworks

Network and vrfcontext objects from the admin tenant will not be shared to non-admin tenants unless admin permissions are granted. Field introduced in 18.2.7, 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistenceKeyRotatePeriod

Period for rotate app persistence keys job. Allowed values are 1-1051200. Special values are 0 - 'disabled'. Unit is min. Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortalRequestBurstLimit

Burst limit on number of incoming requests. 0 to disable. Field introduced in 20.1.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortalRequestRateLimit

Maximum average number of requests allowed per second. 0 to disable. Field introduced in 20.1.1. Unit is per_second.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortalToken

Token used for uploading tech-support to portal. Field introduced in 16.4.6,17.1.2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessLockedUseraccountsTimeoutPeriod

Period for process locked user accounts job. Field introduced in 18.1.1. Unit is min.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessPkiProfileTimeoutPeriod

Period for process pki profile job. Field introduced in 18.1.1. Unit is min.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryHostFail

Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResmgrLogCachingPeriod

Period for each cycle of log caching in resource manager. At the end of each cycle, the in memory cached log history will be cleared. Field introduced in 20.1.5. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SafenetHsmVersion

Version of the safenet package installed on the controller. Field introduced in 16.5.2,17.2.3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeCreateTimeout

Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeFailoverAttemptInterval

Interval between attempting failovers to an se. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeFromMarketplace

This setting decides whether se is to be deployed from the cloud marketplace or to be created by the controller. The setting is applicable only when byol license is selected. Enum options - MARKETPLACE, IMAGE. Field introduced in 18.1.4, 18.2.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeOfflineDel

Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeSpawnRetryInterval

Default retry period before attempting another service engine spawn in se group. Field introduced in 20.1.1. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeVnicCooldown

Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeVnicGcWaitTime

Duration to wait after last vnic addition before proceeding with vnic garbage collection. Used for testing purposes. Field introduced in 20.1.4. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureChannelCleanupTimeout

Period for secure channel cleanup job. Unit is min.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureChannelControllerTokenTimeout

Unit is min.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureChannelSeTokenTimeout

Unit is min.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeupgradeCopyPoolSize

This parameter defines the number of simultaneous se image downloads in a segroup. It is used to pace the se downloads so that controller network/cpu bandwidth is a bounded operation. A value of 0 will disable the pacing scheme and all the se(s) in the segroup will attempt to download the image. Field introduced in 18.2.6.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeupgradeFabricPoolSize

Pool size used for all fabric commands during se upgrade.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeupgradeSegroupMinDeadTimeout

Time to wait before marking segroup upgrade as stuck. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedSslCertificates

Ssl certificates in the admin tenant can be used in non-admin tenants. Field introduced in 18.2.5.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertificateExpiryWarningDays

Number of days for ssl certificate expiry warning. Unit is days.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnresponsiveSeReboot

Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeDnsTtl

Time to account for dns ttl during upgrade. This is in addition to vs_scalein_timeout_for_upgrade in se_group. Field introduced in 17.1.1. Unit is sec. Allowed in basic(allowed values- 5) edition, essentials(allowed values- 5) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeFatSeLeaseTime

Amount of time controller waits for a large-sized se (>=128gb memory) to reconnect after it is rebooted during upgrade. Field introduced in 18.2.10, 20.1.1. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeLeaseTime

Amount of time controller waits for a regular-sized se (<128gb memory) to reconnect after it is rebooted during upgrade. Starting 18.2.10/20.1.1, the default time has increased from 360 seconds to 600 seconds. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeSePerVsScaleOpsTxnTime

This parameter defines the upper-bound value of the vs scale-in or vs scale-out operation executed in the sescalein and sescale context. User can tweak this parameter to a higher value if the segroup gets suspended due to sescalein or sescaleout timeout failure typically associated with high number of vs(es) scaled out. Field introduced in 18.2.10, 20.1.1. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnicOpFailTime

Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsApicScaleoutTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsAwaitingSeTimeout

Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsKeyRotatePeriod

Period for rotate vs keys job. Allowed values are 1-1051200. Special values are 0 - 'disabled'. Unit is min.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsScaleoutReadyCheckInterval

Interval for checking scaleout_ready status while controller is waiting for scaleoutready rpc from the service engine. Field introduced in 18.2.2. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsSeAttachIpFail

Time to wait before marking attach ip operation on an se as failed. Field introduced in 17.2.2. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsSeBootupFail

Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsSeCreateFail

Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsSePingFail

Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsSeVnicFail

Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsSeVnicIpFail

Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarmstartSeReconnectWaitTime

Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarmstartVsResyncWaitTime

Timeout for warmstart vs resync. Field introduced in 18.1.4, 18.2.1. Unit is sec.

_Required_: No

_Type_: Double

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

