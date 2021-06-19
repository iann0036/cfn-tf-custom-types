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
    Id: Optional[str]
    Uuid: Optional[str]
    SeAgentProperties: Optional[Sequence["_SeAgentPropertiesDefinition"]]
    SeBootupProperties: Optional[Sequence["_SeBootupPropertiesDefinition"]]
    SeRuntimeProperties: Optional[Sequence["_SeRuntimePropertiesDefinition"]]

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
            Id=json_data.get("Id"),
            Uuid=json_data.get("Uuid"),
            SeAgentProperties=deserialize_list(json_data.get("SeAgentProperties"), SeAgentPropertiesDefinition),
            SeBootupProperties=deserialize_list(json_data.get("SeBootupProperties"), SeBootupPropertiesDefinition),
            SeRuntimeProperties=deserialize_list(json_data.get("SeRuntimeProperties"), SeRuntimePropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SeAgentPropertiesDefinition(BaseModel):
    ControllerEchoMissAggressiveLimit: Optional[float]
    ControllerEchoMissLimit: Optional[float]
    ControllerEchoRpcAggressiveTimeout: Optional[float]
    ControllerEchoRpcTimeout: Optional[float]
    ControllerHeartbeatMissLimit: Optional[float]
    ControllerHeartbeatTimeoutSec: Optional[float]
    ControllerRegistrationTimeoutSec: Optional[float]
    ControllerRpcTimeout: Optional[float]
    CpustatsInterval: Optional[float]
    CtrlRegPendingMaxWaitTime: Optional[float]
    DebugMode: Optional[bool]
    DpAggressiveDeqIntervalMsec: Optional[float]
    DpAggressiveEnqIntervalMsec: Optional[float]
    DpBatchSize: Optional[float]
    DpDeqIntervalMsec: Optional[float]
    DpEnqIntervalMsec: Optional[float]
    DpMaxWaitRspTimeSec: Optional[float]
    DpRegPendingMaxWaitTime: Optional[float]
    HeadlessTimeoutSec: Optional[float]
    IgnoreDockerMacChange: Optional[bool]
    NsHelperDeqIntervalMsec: Optional[float]
    SdbFlushInterval: Optional[float]
    SdbPipelineSize: Optional[float]
    SdbScanCount: Optional[float]
    SeGrpChangeDisruptive: Optional[bool]
    SendSeReadyTimeout: Optional[float]
    StatesFlushInterval: Optional[float]
    VnicDhcpIpCheckInterval: Optional[float]
    VnicDhcpIpMaxRetries: Optional[float]
    VnicIpDeleteInterval: Optional[float]
    VnicProbeInterval: Optional[float]
    VnicRpcRetryInterval: Optional[float]
    VnicdbCmdHistorySize: Optional[float]
    SeagentStatecacheProperties: Optional[Sequence["_SeagentStatecachePropertiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SeAgentPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeAgentPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            ControllerEchoMissAggressiveLimit=json_data.get("ControllerEchoMissAggressiveLimit"),
            ControllerEchoMissLimit=json_data.get("ControllerEchoMissLimit"),
            ControllerEchoRpcAggressiveTimeout=json_data.get("ControllerEchoRpcAggressiveTimeout"),
            ControllerEchoRpcTimeout=json_data.get("ControllerEchoRpcTimeout"),
            ControllerHeartbeatMissLimit=json_data.get("ControllerHeartbeatMissLimit"),
            ControllerHeartbeatTimeoutSec=json_data.get("ControllerHeartbeatTimeoutSec"),
            ControllerRegistrationTimeoutSec=json_data.get("ControllerRegistrationTimeoutSec"),
            ControllerRpcTimeout=json_data.get("ControllerRpcTimeout"),
            CpustatsInterval=json_data.get("CpustatsInterval"),
            CtrlRegPendingMaxWaitTime=json_data.get("CtrlRegPendingMaxWaitTime"),
            DebugMode=json_data.get("DebugMode"),
            DpAggressiveDeqIntervalMsec=json_data.get("DpAggressiveDeqIntervalMsec"),
            DpAggressiveEnqIntervalMsec=json_data.get("DpAggressiveEnqIntervalMsec"),
            DpBatchSize=json_data.get("DpBatchSize"),
            DpDeqIntervalMsec=json_data.get("DpDeqIntervalMsec"),
            DpEnqIntervalMsec=json_data.get("DpEnqIntervalMsec"),
            DpMaxWaitRspTimeSec=json_data.get("DpMaxWaitRspTimeSec"),
            DpRegPendingMaxWaitTime=json_data.get("DpRegPendingMaxWaitTime"),
            HeadlessTimeoutSec=json_data.get("HeadlessTimeoutSec"),
            IgnoreDockerMacChange=json_data.get("IgnoreDockerMacChange"),
            NsHelperDeqIntervalMsec=json_data.get("NsHelperDeqIntervalMsec"),
            SdbFlushInterval=json_data.get("SdbFlushInterval"),
            SdbPipelineSize=json_data.get("SdbPipelineSize"),
            SdbScanCount=json_data.get("SdbScanCount"),
            SeGrpChangeDisruptive=json_data.get("SeGrpChangeDisruptive"),
            SendSeReadyTimeout=json_data.get("SendSeReadyTimeout"),
            StatesFlushInterval=json_data.get("StatesFlushInterval"),
            VnicDhcpIpCheckInterval=json_data.get("VnicDhcpIpCheckInterval"),
            VnicDhcpIpMaxRetries=json_data.get("VnicDhcpIpMaxRetries"),
            VnicIpDeleteInterval=json_data.get("VnicIpDeleteInterval"),
            VnicProbeInterval=json_data.get("VnicProbeInterval"),
            VnicRpcRetryInterval=json_data.get("VnicRpcRetryInterval"),
            VnicdbCmdHistorySize=json_data.get("VnicdbCmdHistorySize"),
            SeagentStatecacheProperties=deserialize_list(json_data.get("SeagentStatecacheProperties"), SeagentStatecachePropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeAgentPropertiesDefinition = SeAgentPropertiesDefinition


@dataclass
class SeagentStatecachePropertiesDefinition(BaseModel):
    ScBatchBufferFlushLimit: Optional[float]
    ScDnsQBatchDequeueLimit: Optional[float]
    ScDnsQMaxSize: Optional[float]
    ScShardCleanupMaxTime: Optional[float]
    ScStateRingBatchDequeueLimit: Optional[float]
    ScStatesFlushInterval: Optional[float]
    ScStreamCheckInterval: Optional[float]
    ScThreadQBatchDequeueLimit: Optional[float]
    ScThreadQMaxSize: Optional[float]
    ScThreadSleepInterval: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SeagentStatecachePropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeagentStatecachePropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            ScBatchBufferFlushLimit=json_data.get("ScBatchBufferFlushLimit"),
            ScDnsQBatchDequeueLimit=json_data.get("ScDnsQBatchDequeueLimit"),
            ScDnsQMaxSize=json_data.get("ScDnsQMaxSize"),
            ScShardCleanupMaxTime=json_data.get("ScShardCleanupMaxTime"),
            ScStateRingBatchDequeueLimit=json_data.get("ScStateRingBatchDequeueLimit"),
            ScStatesFlushInterval=json_data.get("ScStatesFlushInterval"),
            ScStreamCheckInterval=json_data.get("ScStreamCheckInterval"),
            ScThreadQBatchDequeueLimit=json_data.get("ScThreadQBatchDequeueLimit"),
            ScThreadQMaxSize=json_data.get("ScThreadQMaxSize"),
            ScThreadSleepInterval=json_data.get("ScThreadSleepInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeagentStatecachePropertiesDefinition = SeagentStatecachePropertiesDefinition


@dataclass
class SeBootupPropertiesDefinition(BaseModel):
    DockerBackendPortend: Optional[float]
    DockerBackendPortstart: Optional[float]
    FairQueueingEnabled: Optional[bool]
    GeoDbGranularity: Optional[float]
    L7ConnsPerCore: Optional[float]
    L7ResvdListenConnsPerCore: Optional[float]
    LogAgentDebugEnabled: Optional[bool]
    LogAgentTraceEnabled: Optional[bool]
    SeEmulatedCores: Optional[float]
    SeIpEncapIpc: Optional[float]
    SeL3EncapIpc: Optional[float]
    SeLogBufferAppBlockingDequeue: Optional[bool]
    SeLogBufferApplogSize: Optional[float]
    SeLogBufferChunkCount: Optional[float]
    SeLogBufferConnBlockingDequeue: Optional[bool]
    SeLogBufferConnlogSize: Optional[float]
    SeLogBufferEventsBlockingDequeue: Optional[bool]
    SeLogBufferEventsSize: Optional[float]
    SslSessCachePerVs: Optional[float]
    SslSessCacheTimeout: Optional[float]
    TcpSyncacheHashsize: Optional[float]
    SeDpCompression: Optional[Sequence["_SeDpCompressionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SeBootupPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeBootupPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            DockerBackendPortend=json_data.get("DockerBackendPortend"),
            DockerBackendPortstart=json_data.get("DockerBackendPortstart"),
            FairQueueingEnabled=json_data.get("FairQueueingEnabled"),
            GeoDbGranularity=json_data.get("GeoDbGranularity"),
            L7ConnsPerCore=json_data.get("L7ConnsPerCore"),
            L7ResvdListenConnsPerCore=json_data.get("L7ResvdListenConnsPerCore"),
            LogAgentDebugEnabled=json_data.get("LogAgentDebugEnabled"),
            LogAgentTraceEnabled=json_data.get("LogAgentTraceEnabled"),
            SeEmulatedCores=json_data.get("SeEmulatedCores"),
            SeIpEncapIpc=json_data.get("SeIpEncapIpc"),
            SeL3EncapIpc=json_data.get("SeL3EncapIpc"),
            SeLogBufferAppBlockingDequeue=json_data.get("SeLogBufferAppBlockingDequeue"),
            SeLogBufferApplogSize=json_data.get("SeLogBufferApplogSize"),
            SeLogBufferChunkCount=json_data.get("SeLogBufferChunkCount"),
            SeLogBufferConnBlockingDequeue=json_data.get("SeLogBufferConnBlockingDequeue"),
            SeLogBufferConnlogSize=json_data.get("SeLogBufferConnlogSize"),
            SeLogBufferEventsBlockingDequeue=json_data.get("SeLogBufferEventsBlockingDequeue"),
            SeLogBufferEventsSize=json_data.get("SeLogBufferEventsSize"),
            SslSessCachePerVs=json_data.get("SslSessCachePerVs"),
            SslSessCacheTimeout=json_data.get("SslSessCacheTimeout"),
            TcpSyncacheHashsize=json_data.get("TcpSyncacheHashsize"),
            SeDpCompression=deserialize_list(json_data.get("SeDpCompression"), SeDpCompressionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeBootupPropertiesDefinition = SeBootupPropertiesDefinition


@dataclass
class SeDpCompressionDefinition(BaseModel):
    MaxLowRtt: Optional[float]
    MinHighRtt: Optional[float]
    MinLength: Optional[float]
    MobileStr: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SeDpCompressionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeDpCompressionDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxLowRtt=json_data.get("MaxLowRtt"),
            MinHighRtt=json_data.get("MinHighRtt"),
            MinLength=json_data.get("MinLength"),
            MobileStr=json_data.get("MobileStr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeDpCompressionDefinition = SeDpCompressionDefinition


@dataclass
class SeRuntimePropertiesDefinition(BaseModel):
    AdminSshEnabled: Optional[bool]
    BaremetalDispatcherHandlesFlows: Optional[bool]
    ConnectionsLossyLogRateLimiterThreshold: Optional[float]
    ConnectionsUdfnfLogRateLimiterThreshold: Optional[float]
    DisableFlowProbes: Optional[bool]
    DownstreamSendTimeout: Optional[float]
    DpAggressiveHbFrequency: Optional[float]
    DpAggressiveHbTimeoutCount: Optional[float]
    DpHbFrequency: Optional[float]
    DpHbTimeoutCount: Optional[float]
    DupipFrequency: Optional[float]
    DupipTimeoutCount: Optional[float]
    EnableHsmLog: Optional[bool]
    FeproxyVipsEnableProxyArp: Optional[bool]
    FlowTableBatchPushFrequency: Optional[float]
    GlobalMtu: Optional[float]
    HttpRumConsoleLog: Optional[bool]
    HttpRumMinContentLength: Optional[float]
    LbactionNumRequestsToDispatch: Optional[float]
    LbactionRqPerRequestMaxRetries: Optional[float]
    LogAgentCompressLogs: Optional[bool]
    LogAgentConnSendBufferSize: Optional[float]
    LogAgentExportMsgBufferSize: Optional[float]
    LogAgentExportWaitTime: Optional[float]
    LogAgentFileSzAppl: Optional[float]
    LogAgentFileSzConn: Optional[float]
    LogAgentFileSzDebug: Optional[float]
    LogAgentFileSzEvent: Optional[float]
    LogAgentLogStorageMinSz: Optional[float]
    LogAgentMaxActiveAdfFilesPerVs: Optional[float]
    LogAgentMaxConcurrentRsync: Optional[float]
    LogAgentMaxLogmessageProtoSz: Optional[float]
    LogAgentMaxStorageExcessPercent: Optional[float]
    LogAgentMaxStorageIgnorePercent: Optional[float]
    LogAgentMinStoragePerVs: Optional[float]
    LogAgentPauseInterval: Optional[float]
    LogAgentSleepInterval: Optional[float]
    LogAgentUnknownVsTimer: Optional[float]
    LogMessageMaxFileListSize: Optional[float]
    McacheEnabled: Optional[bool]
    McacheFetchEnabled: Optional[bool]
    McacheStoreInEnabled: Optional[bool]
    McacheStoreInMaxSize: Optional[float]
    McacheStoreInMinSize: Optional[float]
    McacheStoreOutEnabled: Optional[bool]
    NgxFreeConnectionStack: Optional[bool]
    PersistenceMemMax: Optional[float]
    ScaleoutUdpPerPkt: Optional[bool]
    SeAuthLdapBindTimeout: Optional[float]
    SeAuthLdapCacheSize: Optional[float]
    SeAuthLdapConnectTimeout: Optional[float]
    SeAuthLdapConnsPerServer: Optional[float]
    SeAuthLdapReconnectTimeout: Optional[float]
    SeAuthLdapRequestTimeout: Optional[float]
    SeAuthLdapServersFailoverOnly: Optional[bool]
    SeDpHmDrops: Optional[float]
    SeDpIfStatePollInterval: Optional[float]
    SeDpLogNfEnqueuePercent: Optional[float]
    SeDpLogUdfEnqueuePercent: Optional[float]
    SeDumpCoreOnAssert: Optional[bool]
    SeHandleInterfaceRoutes: Optional[bool]
    SeHbPersistFudgeBits: Optional[float]
    SeMacErrorThresholdToDisablePromiscious: Optional[float]
    SeMemoryPoison: Optional[bool]
    SeMetricsInterval: Optional[float]
    SeMetricsRtEnabled: Optional[bool]
    SeMetricsRtInterval: Optional[float]
    SePacketBufferMax: Optional[float]
    SeRandomTcpDrops: Optional[bool]
    ServicesAccessibleAllInterfaces: Optional[bool]
    SpdyFwdProxyParseEnable: Optional[bool]
    TcpSyncacheMaxRetransmitDefault: Optional[float]
    UpstreamConnectTimeout: Optional[float]
    UpstreamConnpoolCacheThresh: Optional[float]
    UpstreamConnpoolConnIdleThreshTmo: Optional[float]
    UpstreamConnpoolCoreMaxCache: Optional[float]
    UpstreamConnpoolEnable: Optional[bool]
    UpstreamConnpoolStrategy: Optional[float]
    UpstreamKeepalive: Optional[bool]
    UpstreamReadTimeout: Optional[float]
    UpstreamSendTimeout: Optional[float]
    UserDefinedMetricAge: Optional[float]
    AppHeaders: Optional[Sequence["_AppHeadersDefinition"]]
    DosProfile: Optional[Sequence["_DosProfileDefinition"]]
    SeDpCompression: Optional[Sequence["_SeDpCompressionDefinition"]]
    SeRateLimiters: Optional[Sequence["_SeRateLimitersDefinition"]]
    ServiceIpSubnets: Optional[Sequence["_ServiceIpSubnetsDefinition"]]
    ServicePortRanges: Optional[Sequence["_ServicePortRangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SeRuntimePropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeRuntimePropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminSshEnabled=json_data.get("AdminSshEnabled"),
            BaremetalDispatcherHandlesFlows=json_data.get("BaremetalDispatcherHandlesFlows"),
            ConnectionsLossyLogRateLimiterThreshold=json_data.get("ConnectionsLossyLogRateLimiterThreshold"),
            ConnectionsUdfnfLogRateLimiterThreshold=json_data.get("ConnectionsUdfnfLogRateLimiterThreshold"),
            DisableFlowProbes=json_data.get("DisableFlowProbes"),
            DownstreamSendTimeout=json_data.get("DownstreamSendTimeout"),
            DpAggressiveHbFrequency=json_data.get("DpAggressiveHbFrequency"),
            DpAggressiveHbTimeoutCount=json_data.get("DpAggressiveHbTimeoutCount"),
            DpHbFrequency=json_data.get("DpHbFrequency"),
            DpHbTimeoutCount=json_data.get("DpHbTimeoutCount"),
            DupipFrequency=json_data.get("DupipFrequency"),
            DupipTimeoutCount=json_data.get("DupipTimeoutCount"),
            EnableHsmLog=json_data.get("EnableHsmLog"),
            FeproxyVipsEnableProxyArp=json_data.get("FeproxyVipsEnableProxyArp"),
            FlowTableBatchPushFrequency=json_data.get("FlowTableBatchPushFrequency"),
            GlobalMtu=json_data.get("GlobalMtu"),
            HttpRumConsoleLog=json_data.get("HttpRumConsoleLog"),
            HttpRumMinContentLength=json_data.get("HttpRumMinContentLength"),
            LbactionNumRequestsToDispatch=json_data.get("LbactionNumRequestsToDispatch"),
            LbactionRqPerRequestMaxRetries=json_data.get("LbactionRqPerRequestMaxRetries"),
            LogAgentCompressLogs=json_data.get("LogAgentCompressLogs"),
            LogAgentConnSendBufferSize=json_data.get("LogAgentConnSendBufferSize"),
            LogAgentExportMsgBufferSize=json_data.get("LogAgentExportMsgBufferSize"),
            LogAgentExportWaitTime=json_data.get("LogAgentExportWaitTime"),
            LogAgentFileSzAppl=json_data.get("LogAgentFileSzAppl"),
            LogAgentFileSzConn=json_data.get("LogAgentFileSzConn"),
            LogAgentFileSzDebug=json_data.get("LogAgentFileSzDebug"),
            LogAgentFileSzEvent=json_data.get("LogAgentFileSzEvent"),
            LogAgentLogStorageMinSz=json_data.get("LogAgentLogStorageMinSz"),
            LogAgentMaxActiveAdfFilesPerVs=json_data.get("LogAgentMaxActiveAdfFilesPerVs"),
            LogAgentMaxConcurrentRsync=json_data.get("LogAgentMaxConcurrentRsync"),
            LogAgentMaxLogmessageProtoSz=json_data.get("LogAgentMaxLogmessageProtoSz"),
            LogAgentMaxStorageExcessPercent=json_data.get("LogAgentMaxStorageExcessPercent"),
            LogAgentMaxStorageIgnorePercent=json_data.get("LogAgentMaxStorageIgnorePercent"),
            LogAgentMinStoragePerVs=json_data.get("LogAgentMinStoragePerVs"),
            LogAgentPauseInterval=json_data.get("LogAgentPauseInterval"),
            LogAgentSleepInterval=json_data.get("LogAgentSleepInterval"),
            LogAgentUnknownVsTimer=json_data.get("LogAgentUnknownVsTimer"),
            LogMessageMaxFileListSize=json_data.get("LogMessageMaxFileListSize"),
            McacheEnabled=json_data.get("McacheEnabled"),
            McacheFetchEnabled=json_data.get("McacheFetchEnabled"),
            McacheStoreInEnabled=json_data.get("McacheStoreInEnabled"),
            McacheStoreInMaxSize=json_data.get("McacheStoreInMaxSize"),
            McacheStoreInMinSize=json_data.get("McacheStoreInMinSize"),
            McacheStoreOutEnabled=json_data.get("McacheStoreOutEnabled"),
            NgxFreeConnectionStack=json_data.get("NgxFreeConnectionStack"),
            PersistenceMemMax=json_data.get("PersistenceMemMax"),
            ScaleoutUdpPerPkt=json_data.get("ScaleoutUdpPerPkt"),
            SeAuthLdapBindTimeout=json_data.get("SeAuthLdapBindTimeout"),
            SeAuthLdapCacheSize=json_data.get("SeAuthLdapCacheSize"),
            SeAuthLdapConnectTimeout=json_data.get("SeAuthLdapConnectTimeout"),
            SeAuthLdapConnsPerServer=json_data.get("SeAuthLdapConnsPerServer"),
            SeAuthLdapReconnectTimeout=json_data.get("SeAuthLdapReconnectTimeout"),
            SeAuthLdapRequestTimeout=json_data.get("SeAuthLdapRequestTimeout"),
            SeAuthLdapServersFailoverOnly=json_data.get("SeAuthLdapServersFailoverOnly"),
            SeDpHmDrops=json_data.get("SeDpHmDrops"),
            SeDpIfStatePollInterval=json_data.get("SeDpIfStatePollInterval"),
            SeDpLogNfEnqueuePercent=json_data.get("SeDpLogNfEnqueuePercent"),
            SeDpLogUdfEnqueuePercent=json_data.get("SeDpLogUdfEnqueuePercent"),
            SeDumpCoreOnAssert=json_data.get("SeDumpCoreOnAssert"),
            SeHandleInterfaceRoutes=json_data.get("SeHandleInterfaceRoutes"),
            SeHbPersistFudgeBits=json_data.get("SeHbPersistFudgeBits"),
            SeMacErrorThresholdToDisablePromiscious=json_data.get("SeMacErrorThresholdToDisablePromiscious"),
            SeMemoryPoison=json_data.get("SeMemoryPoison"),
            SeMetricsInterval=json_data.get("SeMetricsInterval"),
            SeMetricsRtEnabled=json_data.get("SeMetricsRtEnabled"),
            SeMetricsRtInterval=json_data.get("SeMetricsRtInterval"),
            SePacketBufferMax=json_data.get("SePacketBufferMax"),
            SeRandomTcpDrops=json_data.get("SeRandomTcpDrops"),
            ServicesAccessibleAllInterfaces=json_data.get("ServicesAccessibleAllInterfaces"),
            SpdyFwdProxyParseEnable=json_data.get("SpdyFwdProxyParseEnable"),
            TcpSyncacheMaxRetransmitDefault=json_data.get("TcpSyncacheMaxRetransmitDefault"),
            UpstreamConnectTimeout=json_data.get("UpstreamConnectTimeout"),
            UpstreamConnpoolCacheThresh=json_data.get("UpstreamConnpoolCacheThresh"),
            UpstreamConnpoolConnIdleThreshTmo=json_data.get("UpstreamConnpoolConnIdleThreshTmo"),
            UpstreamConnpoolCoreMaxCache=json_data.get("UpstreamConnpoolCoreMaxCache"),
            UpstreamConnpoolEnable=json_data.get("UpstreamConnpoolEnable"),
            UpstreamConnpoolStrategy=json_data.get("UpstreamConnpoolStrategy"),
            UpstreamKeepalive=json_data.get("UpstreamKeepalive"),
            UpstreamReadTimeout=json_data.get("UpstreamReadTimeout"),
            UpstreamSendTimeout=json_data.get("UpstreamSendTimeout"),
            UserDefinedMetricAge=json_data.get("UserDefinedMetricAge"),
            AppHeaders=deserialize_list(json_data.get("AppHeaders"), AppHeadersDefinition),
            DosProfile=deserialize_list(json_data.get("DosProfile"), DosProfileDefinition),
            SeDpCompression=deserialize_list(json_data.get("SeDpCompression"), SeDpCompressionDefinition),
            SeRateLimiters=deserialize_list(json_data.get("SeRateLimiters"), SeRateLimitersDefinition),
            ServiceIpSubnets=deserialize_list(json_data.get("ServiceIpSubnets"), ServiceIpSubnetsDefinition),
            ServicePortRanges=deserialize_list(json_data.get("ServicePortRanges"), ServicePortRangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeRuntimePropertiesDefinition = SeRuntimePropertiesDefinition


@dataclass
class AppHeadersDefinition(BaseModel):
    HdrMatchCase: Optional[str]
    HdrName: Optional[str]
    HdrStringOp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppHeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppHeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            HdrMatchCase=json_data.get("HdrMatchCase"),
            HdrName=json_data.get("HdrName"),
            HdrStringOp=json_data.get("HdrStringOp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppHeadersDefinition = AppHeadersDefinition


@dataclass
class DosProfileDefinition(BaseModel):
    ThreshPeriod: Optional[float]
    ThreshInfo: Optional[Sequence["_ThreshInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DosProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DosProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            ThreshPeriod=json_data.get("ThreshPeriod"),
            ThreshInfo=deserialize_list(json_data.get("ThreshInfo"), ThreshInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DosProfileDefinition = DosProfileDefinition


@dataclass
class ThreshInfoDefinition(BaseModel):
    Attack: Optional[str]
    MaxValue: Optional[float]
    MinValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ThreshInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThreshInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Attack=json_data.get("Attack"),
            MaxValue=json_data.get("MaxValue"),
            MinValue=json_data.get("MinValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThreshInfoDefinition = ThreshInfoDefinition


@dataclass
class SeRateLimitersDefinition(BaseModel):
    ArpRl: Optional[float]
    DefaultRl: Optional[float]
    FlowProbeRl: Optional[float]
    IcmpRl: Optional[float]
    IcmpRspRl: Optional[float]
    RstRl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SeRateLimitersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeRateLimitersDefinition"]:
        if not json_data:
            return None
        return cls(
            ArpRl=json_data.get("ArpRl"),
            DefaultRl=json_data.get("DefaultRl"),
            FlowProbeRl=json_data.get("FlowProbeRl"),
            IcmpRl=json_data.get("IcmpRl"),
            IcmpRspRl=json_data.get("IcmpRspRl"),
            RstRl=json_data.get("RstRl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeRateLimitersDefinition = SeRateLimitersDefinition


@dataclass
class ServiceIpSubnetsDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceIpSubnetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceIpSubnetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceIpSubnetsDefinition = ServiceIpSubnetsDefinition


@dataclass
class IpAddrDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddrDefinition = IpAddrDefinition


@dataclass
class ServicePortRangesDefinition(BaseModel):
    End: Optional[float]
    Start: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServicePortRangesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicePortRangesDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicePortRangesDefinition = ServicePortRangesDefinition


