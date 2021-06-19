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
    AfterDisable: Optional[float]
    AutoNatNoIpRefresh: Optional[str]
    BuffThresh: Optional[float]
    BuffThreshHwBuff: Optional[float]
    BuffThreshRelieveThresh: Optional[float]
    BuffThreshSysBuffHigh: Optional[float]
    BuffThreshSysBuffLow: Optional[float]
    CompressBlockSize: Optional[float]
    DisableAdaptiveResourceCheck: Optional[float]
    DisableServerAutoReselect: Optional[float]
    DnsCacheAge: Optional[float]
    DnsCacheEnable: Optional[float]
    DnsCacheEntrySize: Optional[float]
    DnsVipStateless: Optional[float]
    DropIcmpToVipWhenVipDown: Optional[float]
    DsrHealthCheckEnable: Optional[float]
    EnableL7ReqAcct: Optional[float]
    Entity: Optional[str]
    ExcludeDestination: Optional[str]
    ExtendedStats: Optional[float]
    FastPathDisable: Optional[float]
    GatewayHealthCheck: Optional[float]
    GracefulShutdown: Optional[float]
    GracefulShutdownEnable: Optional[float]
    HonorServerResponseTtl: Optional[float]
    HwCompression: Optional[float]
    HwSynRr: Optional[float]
    Id: Optional[str]
    Interval: Optional[float]
    L2l3TrunkLbDisable: Optional[float]
    LogForResetUnknownConn: Optional[float]
    LowLatency: Optional[float]
    MaxBuffQueuedPerConn: Optional[float]
    MaxHttpHeaderCount: Optional[float]
    MaxLocalRate: Optional[float]
    MaxRemoteRate: Optional[float]
    MslTime: Optional[float]
    MssTable: Optional[float]
    NoAutoUpOnAflex: Optional[float]
    OverridePort: Optional[float]
    PktRateForResetUnknownConn: Optional[float]
    PlayerIdCheckEnable: Optional[float]
    Range: Optional[float]
    RangeEnd: Optional[float]
    RangeStart: Optional[float]
    RateLimitLogging: Optional[float]
    ResetStaleSession: Optional[float]
    ResolvePortConflict: Optional[float]
    ResponseType: Optional[str]
    ScaleOut: Optional[float]
    SnatGwyForL3: Optional[float]
    SnatOnVip: Optional[float]
    Software: Optional[float]
    SortRes: Optional[float]
    SsliSniHashEnable: Optional[float]
    StatelessSgMultiBinding: Optional[float]
    StatsDataDisable: Optional[float]
    Timeout: Optional[float]
    TtlThreshold: Optional[float]
    UseMssTab: Optional[float]
    Uuid: Optional[str]
    ConnRateLimit: Optional[Sequence["_ConnRateLimitDefinition"]]
    DdosProtection: Optional[Sequence["_DdosProtectionDefinition"]]
    DnsResponseRateLimiting: Optional[Sequence["_DnsResponseRateLimitingDefinition"]]

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
            AfterDisable=json_data.get("AfterDisable"),
            AutoNatNoIpRefresh=json_data.get("AutoNatNoIpRefresh"),
            BuffThresh=json_data.get("BuffThresh"),
            BuffThreshHwBuff=json_data.get("BuffThreshHwBuff"),
            BuffThreshRelieveThresh=json_data.get("BuffThreshRelieveThresh"),
            BuffThreshSysBuffHigh=json_data.get("BuffThreshSysBuffHigh"),
            BuffThreshSysBuffLow=json_data.get("BuffThreshSysBuffLow"),
            CompressBlockSize=json_data.get("CompressBlockSize"),
            DisableAdaptiveResourceCheck=json_data.get("DisableAdaptiveResourceCheck"),
            DisableServerAutoReselect=json_data.get("DisableServerAutoReselect"),
            DnsCacheAge=json_data.get("DnsCacheAge"),
            DnsCacheEnable=json_data.get("DnsCacheEnable"),
            DnsCacheEntrySize=json_data.get("DnsCacheEntrySize"),
            DnsVipStateless=json_data.get("DnsVipStateless"),
            DropIcmpToVipWhenVipDown=json_data.get("DropIcmpToVipWhenVipDown"),
            DsrHealthCheckEnable=json_data.get("DsrHealthCheckEnable"),
            EnableL7ReqAcct=json_data.get("EnableL7ReqAcct"),
            Entity=json_data.get("Entity"),
            ExcludeDestination=json_data.get("ExcludeDestination"),
            ExtendedStats=json_data.get("ExtendedStats"),
            FastPathDisable=json_data.get("FastPathDisable"),
            GatewayHealthCheck=json_data.get("GatewayHealthCheck"),
            GracefulShutdown=json_data.get("GracefulShutdown"),
            GracefulShutdownEnable=json_data.get("GracefulShutdownEnable"),
            HonorServerResponseTtl=json_data.get("HonorServerResponseTtl"),
            HwCompression=json_data.get("HwCompression"),
            HwSynRr=json_data.get("HwSynRr"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            L2l3TrunkLbDisable=json_data.get("L2l3TrunkLbDisable"),
            LogForResetUnknownConn=json_data.get("LogForResetUnknownConn"),
            LowLatency=json_data.get("LowLatency"),
            MaxBuffQueuedPerConn=json_data.get("MaxBuffQueuedPerConn"),
            MaxHttpHeaderCount=json_data.get("MaxHttpHeaderCount"),
            MaxLocalRate=json_data.get("MaxLocalRate"),
            MaxRemoteRate=json_data.get("MaxRemoteRate"),
            MslTime=json_data.get("MslTime"),
            MssTable=json_data.get("MssTable"),
            NoAutoUpOnAflex=json_data.get("NoAutoUpOnAflex"),
            OverridePort=json_data.get("OverridePort"),
            PktRateForResetUnknownConn=json_data.get("PktRateForResetUnknownConn"),
            PlayerIdCheckEnable=json_data.get("PlayerIdCheckEnable"),
            Range=json_data.get("Range"),
            RangeEnd=json_data.get("RangeEnd"),
            RangeStart=json_data.get("RangeStart"),
            RateLimitLogging=json_data.get("RateLimitLogging"),
            ResetStaleSession=json_data.get("ResetStaleSession"),
            ResolvePortConflict=json_data.get("ResolvePortConflict"),
            ResponseType=json_data.get("ResponseType"),
            ScaleOut=json_data.get("ScaleOut"),
            SnatGwyForL3=json_data.get("SnatGwyForL3"),
            SnatOnVip=json_data.get("SnatOnVip"),
            Software=json_data.get("Software"),
            SortRes=json_data.get("SortRes"),
            SsliSniHashEnable=json_data.get("SsliSniHashEnable"),
            StatelessSgMultiBinding=json_data.get("StatelessSgMultiBinding"),
            StatsDataDisable=json_data.get("StatsDataDisable"),
            Timeout=json_data.get("Timeout"),
            TtlThreshold=json_data.get("TtlThreshold"),
            UseMssTab=json_data.get("UseMssTab"),
            Uuid=json_data.get("Uuid"),
            ConnRateLimit=deserialize_list(json_data.get("ConnRateLimit"), ConnRateLimitDefinition),
            DdosProtection=deserialize_list(json_data.get("DdosProtection"), DdosProtectionDefinition),
            DnsResponseRateLimiting=deserialize_list(json_data.get("DnsResponseRateLimiting"), DnsResponseRateLimitingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConnRateLimitDefinition(BaseModel):
    SrcIpList: Optional[Sequence["_SrcIpListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConnRateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnRateLimitDefinition"]:
        if not json_data:
            return None
        return cls(
            SrcIpList=deserialize_list(json_data.get("SrcIpList"), SrcIpListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnRateLimitDefinition = ConnRateLimitDefinition


@dataclass
class SrcIpListDefinition(BaseModel):
    ExceedAction: Optional[float]
    Limit: Optional[float]
    LimitPeriod: Optional[str]
    LockOut: Optional[float]
    Log: Optional[float]
    Protocol: Optional[str]
    Shared: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcIpListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcIpListDefinition"]:
        if not json_data:
            return None
        return cls(
            ExceedAction=json_data.get("ExceedAction"),
            Limit=json_data.get("Limit"),
            LimitPeriod=json_data.get("LimitPeriod"),
            LockOut=json_data.get("LockOut"),
            Log=json_data.get("Log"),
            Protocol=json_data.get("Protocol"),
            Shared=json_data.get("Shared"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcIpListDefinition = SrcIpListDefinition


@dataclass
class DdosProtectionDefinition(BaseModel):
    IpdEnableToggle: Optional[str]
    Logging: Optional[Sequence["_LoggingDefinition"]]
    PacketsPerSecond: Optional[Sequence["_PacketsPerSecondDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DdosProtectionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DdosProtectionDefinition"]:
        if not json_data:
            return None
        return cls(
            IpdEnableToggle=json_data.get("IpdEnableToggle"),
            Logging=deserialize_list(json_data.get("Logging"), LoggingDefinition),
            PacketsPerSecond=deserialize_list(json_data.get("PacketsPerSecond"), PacketsPerSecondDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DdosProtectionDefinition = DdosProtectionDefinition


@dataclass
class LoggingDefinition(BaseModel):
    IpdLoggingToggle: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingDefinition"]:
        if not json_data:
            return None
        return cls(
            IpdLoggingToggle=json_data.get("IpdLoggingToggle"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingDefinition = LoggingDefinition


@dataclass
class PacketsPerSecondDefinition(BaseModel):
    IpdTcp: Optional[float]
    IpdUdp: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PacketsPerSecondDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PacketsPerSecondDefinition"]:
        if not json_data:
            return None
        return cls(
            IpdTcp=json_data.get("IpdTcp"),
            IpdUdp=json_data.get("IpdUdp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PacketsPerSecondDefinition = PacketsPerSecondDefinition


@dataclass
class DnsResponseRateLimitingDefinition(BaseModel):
    MaxTableEntries: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsResponseRateLimitingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsResponseRateLimitingDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxTableEntries=json_data.get("MaxTableEntries"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsResponseRateLimitingDefinition = DnsResponseRateLimitingDefinition


