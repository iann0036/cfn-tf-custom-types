# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    AllowAdminNetworkUpdates: Optional[bool]
    AllowIpForwarding: Optional[bool]
    AllowUnauthenticatedApis: Optional[bool]
    AllowUnauthenticatedNodes: Optional[bool]
    ApiIdleTimeout: Optional[float]
    ApiPerfLoggingThreshold: Optional[float]
    AppviewxCompatMode: Optional[bool]
    AsyncPatchMergePeriod: Optional[float]
    AsyncPatchRequestCleanupDuration: Optional[float]
    AttachIpRetryInterval: Optional[float]
    AttachIpRetryLimit: Optional[float]
    BmUseAnsible: Optional[bool]
    CheckVsvipFqdnSyntax: Optional[bool]
    CleanupExpiredAuthtokenTimeoutPeriod: Optional[float]
    CleanupSessionsTimeoutPeriod: Optional[float]
    CloudReconcile: Optional[bool]
    ClusterIpGratuitousArpPeriod: Optional[float]
    ConsistencyCheckTimeoutPeriod: Optional[float]
    ControllerResourceInfoCollectionPeriod: Optional[float]
    CrashedSeReboot: Optional[float]
    DeadSeDetectionTimer: Optional[float]
    DefaultMinimumApiTimeout: Optional[float]
    DelOfflineSeAfterRebootDelay: Optional[float]
    DnsRefreshPeriod: Optional[float]
    Dummy: Optional[float]
    EditSystemLimits: Optional[bool]
    EnableApiSharding: Optional[bool]
    EnableMemoryBalancer: Optional[bool]
    EnableResmgrLogCachePrint: Optional[bool]
    FatalErrorLeaseTime: Optional[float]
    FederatedDatastoreCleanupDuration: Optional[float]
    FileObjectCleanupPeriod: Optional[float]
    Id: Optional[str]
    MaxDeadSeInGrp: Optional[float]
    MaxPcapPerTenant: Optional[float]
    MaxSeSpawnIntervalDelay: Optional[float]
    MaxSeqAttachIpFailures: Optional[float]
    MaxSeqVnicFailures: Optional[float]
    MaxThreadsCcVipBgWorker: Optional[float]
    PermissionScopedSharedAdminNetworks: Optional[bool]
    PersistenceKeyRotatePeriod: Optional[float]
    PortalRequestBurstLimit: Optional[float]
    PortalRequestRateLimit: Optional[float]
    PortalToken: Optional[str]
    ProcessLockedUseraccountsTimeoutPeriod: Optional[float]
    ProcessPkiProfileTimeoutPeriod: Optional[float]
    QueryHostFail: Optional[float]
    ResmgrLogCachingPeriod: Optional[float]
    SafenetHsmVersion: Optional[str]
    SeCreateTimeout: Optional[float]
    SeFailoverAttemptInterval: Optional[float]
    SeFromMarketplace: Optional[str]
    SeOfflineDel: Optional[float]
    SeSpawnRetryInterval: Optional[float]
    SeVnicCooldown: Optional[float]
    SeVnicGcWaitTime: Optional[float]
    SecureChannelCleanupTimeout: Optional[float]
    SecureChannelControllerTokenTimeout: Optional[float]
    SecureChannelSeTokenTimeout: Optional[float]
    SeupgradeCopyPoolSize: Optional[float]
    SeupgradeFabricPoolSize: Optional[float]
    SeupgradeSegroupMinDeadTimeout: Optional[float]
    SharedSslCertificates: Optional[bool]
    SslCertificateExpiryWarningDays: Optional[Sequence[float]]
    UnresponsiveSeReboot: Optional[float]
    UpgradeDnsTtl: Optional[float]
    UpgradeFatSeLeaseTime: Optional[float]
    UpgradeLeaseTime: Optional[float]
    UpgradeSePerVsScaleOpsTxnTime: Optional[float]
    Uuid: Optional[str]
    VnicOpFailTime: Optional[float]
    VsApicScaleoutTimeout: Optional[float]
    VsAwaitingSeTimeout: Optional[float]
    VsKeyRotatePeriod: Optional[float]
    VsScaleoutReadyCheckInterval: Optional[float]
    VsSeAttachIpFail: Optional[float]
    VsSeBootupFail: Optional[float]
    VsSeCreateFail: Optional[float]
    VsSePingFail: Optional[float]
    VsSeVnicFail: Optional[float]
    VsSeVnicIpFail: Optional[float]
    WarmstartSeReconnectWaitTime: Optional[float]
    WarmstartVsResyncWaitTime: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowAdminNetworkUpdates=json_data.get("AllowAdminNetworkUpdates"),
            AllowIpForwarding=json_data.get("AllowIpForwarding"),
            AllowUnauthenticatedApis=json_data.get("AllowUnauthenticatedApis"),
            AllowUnauthenticatedNodes=json_data.get("AllowUnauthenticatedNodes"),
            ApiIdleTimeout=json_data.get("ApiIdleTimeout"),
            ApiPerfLoggingThreshold=json_data.get("ApiPerfLoggingThreshold"),
            AppviewxCompatMode=json_data.get("AppviewxCompatMode"),
            AsyncPatchMergePeriod=json_data.get("AsyncPatchMergePeriod"),
            AsyncPatchRequestCleanupDuration=json_data.get("AsyncPatchRequestCleanupDuration"),
            AttachIpRetryInterval=json_data.get("AttachIpRetryInterval"),
            AttachIpRetryLimit=json_data.get("AttachIpRetryLimit"),
            BmUseAnsible=json_data.get("BmUseAnsible"),
            CheckVsvipFqdnSyntax=json_data.get("CheckVsvipFqdnSyntax"),
            CleanupExpiredAuthtokenTimeoutPeriod=json_data.get("CleanupExpiredAuthtokenTimeoutPeriod"),
            CleanupSessionsTimeoutPeriod=json_data.get("CleanupSessionsTimeoutPeriod"),
            CloudReconcile=json_data.get("CloudReconcile"),
            ClusterIpGratuitousArpPeriod=json_data.get("ClusterIpGratuitousArpPeriod"),
            ConsistencyCheckTimeoutPeriod=json_data.get("ConsistencyCheckTimeoutPeriod"),
            ControllerResourceInfoCollectionPeriod=json_data.get("ControllerResourceInfoCollectionPeriod"),
            CrashedSeReboot=json_data.get("CrashedSeReboot"),
            DeadSeDetectionTimer=json_data.get("DeadSeDetectionTimer"),
            DefaultMinimumApiTimeout=json_data.get("DefaultMinimumApiTimeout"),
            DelOfflineSeAfterRebootDelay=json_data.get("DelOfflineSeAfterRebootDelay"),
            DnsRefreshPeriod=json_data.get("DnsRefreshPeriod"),
            Dummy=json_data.get("Dummy"),
            EditSystemLimits=json_data.get("EditSystemLimits"),
            EnableApiSharding=json_data.get("EnableApiSharding"),
            EnableMemoryBalancer=json_data.get("EnableMemoryBalancer"),
            EnableResmgrLogCachePrint=json_data.get("EnableResmgrLogCachePrint"),
            FatalErrorLeaseTime=json_data.get("FatalErrorLeaseTime"),
            FederatedDatastoreCleanupDuration=json_data.get("FederatedDatastoreCleanupDuration"),
            FileObjectCleanupPeriod=json_data.get("FileObjectCleanupPeriod"),
            Id=json_data.get("Id"),
            MaxDeadSeInGrp=json_data.get("MaxDeadSeInGrp"),
            MaxPcapPerTenant=json_data.get("MaxPcapPerTenant"),
            MaxSeSpawnIntervalDelay=json_data.get("MaxSeSpawnIntervalDelay"),
            MaxSeqAttachIpFailures=json_data.get("MaxSeqAttachIpFailures"),
            MaxSeqVnicFailures=json_data.get("MaxSeqVnicFailures"),
            MaxThreadsCcVipBgWorker=json_data.get("MaxThreadsCcVipBgWorker"),
            PermissionScopedSharedAdminNetworks=json_data.get("PermissionScopedSharedAdminNetworks"),
            PersistenceKeyRotatePeriod=json_data.get("PersistenceKeyRotatePeriod"),
            PortalRequestBurstLimit=json_data.get("PortalRequestBurstLimit"),
            PortalRequestRateLimit=json_data.get("PortalRequestRateLimit"),
            PortalToken=json_data.get("PortalToken"),
            ProcessLockedUseraccountsTimeoutPeriod=json_data.get("ProcessLockedUseraccountsTimeoutPeriod"),
            ProcessPkiProfileTimeoutPeriod=json_data.get("ProcessPkiProfileTimeoutPeriod"),
            QueryHostFail=json_data.get("QueryHostFail"),
            ResmgrLogCachingPeriod=json_data.get("ResmgrLogCachingPeriod"),
            SafenetHsmVersion=json_data.get("SafenetHsmVersion"),
            SeCreateTimeout=json_data.get("SeCreateTimeout"),
            SeFailoverAttemptInterval=json_data.get("SeFailoverAttemptInterval"),
            SeFromMarketplace=json_data.get("SeFromMarketplace"),
            SeOfflineDel=json_data.get("SeOfflineDel"),
            SeSpawnRetryInterval=json_data.get("SeSpawnRetryInterval"),
            SeVnicCooldown=json_data.get("SeVnicCooldown"),
            SeVnicGcWaitTime=json_data.get("SeVnicGcWaitTime"),
            SecureChannelCleanupTimeout=json_data.get("SecureChannelCleanupTimeout"),
            SecureChannelControllerTokenTimeout=json_data.get("SecureChannelControllerTokenTimeout"),
            SecureChannelSeTokenTimeout=json_data.get("SecureChannelSeTokenTimeout"),
            SeupgradeCopyPoolSize=json_data.get("SeupgradeCopyPoolSize"),
            SeupgradeFabricPoolSize=json_data.get("SeupgradeFabricPoolSize"),
            SeupgradeSegroupMinDeadTimeout=json_data.get("SeupgradeSegroupMinDeadTimeout"),
            SharedSslCertificates=json_data.get("SharedSslCertificates"),
            SslCertificateExpiryWarningDays=json_data.get("SslCertificateExpiryWarningDays"),
            UnresponsiveSeReboot=json_data.get("UnresponsiveSeReboot"),
            UpgradeDnsTtl=json_data.get("UpgradeDnsTtl"),
            UpgradeFatSeLeaseTime=json_data.get("UpgradeFatSeLeaseTime"),
            UpgradeLeaseTime=json_data.get("UpgradeLeaseTime"),
            UpgradeSePerVsScaleOpsTxnTime=json_data.get("UpgradeSePerVsScaleOpsTxnTime"),
            Uuid=json_data.get("Uuid"),
            VnicOpFailTime=json_data.get("VnicOpFailTime"),
            VsApicScaleoutTimeout=json_data.get("VsApicScaleoutTimeout"),
            VsAwaitingSeTimeout=json_data.get("VsAwaitingSeTimeout"),
            VsKeyRotatePeriod=json_data.get("VsKeyRotatePeriod"),
            VsScaleoutReadyCheckInterval=json_data.get("VsScaleoutReadyCheckInterval"),
            VsSeAttachIpFail=json_data.get("VsSeAttachIpFail"),
            VsSeBootupFail=json_data.get("VsSeBootupFail"),
            VsSeCreateFail=json_data.get("VsSeCreateFail"),
            VsSePingFail=json_data.get("VsSePingFail"),
            VsSeVnicFail=json_data.get("VsSeVnicFail"),
            VsSeVnicIpFail=json_data.get("VsSeVnicIpFail"),
            WarmstartSeReconnectWaitTime=json_data.get("WarmstartSeReconnectWaitTime"),
            WarmstartVsResyncWaitTime=json_data.get("WarmstartVsResyncWaitTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


