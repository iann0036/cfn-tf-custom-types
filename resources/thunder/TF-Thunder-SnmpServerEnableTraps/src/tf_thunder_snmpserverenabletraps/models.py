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
    All: Optional[float]
    Id: Optional[str]
    Lldp: Optional[float]
    Uuid: Optional[str]
    Gslb: Optional[Sequence["_GslbDefinition"]]
    Lsn: Optional[Sequence["_LsnDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
    Routing: Optional[Sequence["_RoutingDefinition"]]
    Slb: Optional[Sequence["_SlbDefinition"]]
    SlbChange: Optional[Sequence["_SlbChangeDefinition"]]
    Snmp: Optional[Sequence["_SnmpDefinition"]]
    Ssl: Optional[Sequence["_SslDefinition"]]
    System: Optional[Sequence["_SystemDefinition"]]
    Vcs: Optional[Sequence["_VcsDefinition"]]
    VrrpA: Optional[Sequence["_VrrpADefinition"]]

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
            All=json_data.get("All"),
            Id=json_data.get("Id"),
            Lldp=json_data.get("Lldp"),
            Uuid=json_data.get("Uuid"),
            Gslb=deserialize_list(json_data.get("Gslb"), GslbDefinition),
            Lsn=deserialize_list(json_data.get("Lsn"), LsnDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            Routing=deserialize_list(json_data.get("Routing"), RoutingDefinition),
            Slb=deserialize_list(json_data.get("Slb"), SlbDefinition),
            SlbChange=deserialize_list(json_data.get("SlbChange"), SlbChangeDefinition),
            Snmp=deserialize_list(json_data.get("Snmp"), SnmpDefinition),
            Ssl=deserialize_list(json_data.get("Ssl"), SslDefinition),
            System=deserialize_list(json_data.get("System"), SystemDefinition),
            Vcs=deserialize_list(json_data.get("Vcs"), VcsDefinition),
            VrrpA=deserialize_list(json_data.get("VrrpA"), VrrpADefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GslbDefinition(BaseModel):
    All: Optional[float]
    Group: Optional[float]
    ServiceIp: Optional[float]
    Site: Optional[float]
    Uuid: Optional[str]
    Zone: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_GslbDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GslbDefinition"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            Group=json_data.get("Group"),
            ServiceIp=json_data.get("ServiceIp"),
            Site=json_data.get("Site"),
            Uuid=json_data.get("Uuid"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GslbDefinition = GslbDefinition


@dataclass
class LsnDefinition(BaseModel):
    All: Optional[float]
    FixedNatPortMappingFileChange: Optional[float]
    MaxIpportThreshold: Optional[float]
    MaxPortThreshold: Optional[float]
    PerIpPortUsageThreshold: Optional[float]
    TotalPortUsageThreshold: Optional[float]
    TrafficExceeded: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LsnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LsnDefinition"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            FixedNatPortMappingFileChange=json_data.get("FixedNatPortMappingFileChange"),
            MaxIpportThreshold=json_data.get("MaxIpportThreshold"),
            MaxPortThreshold=json_data.get("MaxPortThreshold"),
            PerIpPortUsageThreshold=json_data.get("PerIpPortUsageThreshold"),
            TotalPortUsageThreshold=json_data.get("TotalPortUsageThreshold"),
            TrafficExceeded=json_data.get("TrafficExceeded"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LsnDefinition = LsnDefinition


@dataclass
class NetworkDefinition(BaseModel):
    TrunkPortThreshold: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            TrunkPortThreshold=json_data.get("TrunkPortThreshold"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class RoutingDefinition(BaseModel):
    Bgp: Optional[Sequence["_BgpDefinition"]]
    Isis: Optional[Sequence["_IsisDefinition"]]
    Ospf: Optional[Sequence["_OspfDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingDefinition"]:
        if not json_data:
            return None
        return cls(
            Bgp=deserialize_list(json_data.get("Bgp"), BgpDefinition),
            Isis=deserialize_list(json_data.get("Isis"), IsisDefinition),
            Ospf=deserialize_list(json_data.get("Ospf"), OspfDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingDefinition = RoutingDefinition


@dataclass
class BgpDefinition(BaseModel):
    BgpBackwardTransNotification: Optional[float]
    BgpEstablishedNotification: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BgpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpDefinition"]:
        if not json_data:
            return None
        return cls(
            BgpBackwardTransNotification=json_data.get("BgpBackwardTransNotification"),
            BgpEstablishedNotification=json_data.get("BgpEstablishedNotification"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpDefinition = BgpDefinition


@dataclass
class IsisDefinition(BaseModel):
    IsisAdjacencyChange: Optional[float]
    IsisAreaMismatch: Optional[float]
    IsisAttemptToExceedMaxSequence: Optional[float]
    IsisAuthenticationFailure: Optional[float]
    IsisAuthenticationTypeFailure: Optional[float]
    IsisCorruptedLspDetected: Optional[float]
    IsisDatabaseOverload: Optional[float]
    IsisIdLenMismatch: Optional[float]
    IsisLspTooLargeToPropagate: Optional[float]
    IsisManualAddressDrops: Optional[float]
    IsisMaxAreaAddressesMismatch: Optional[float]
    IsisOriginatingLspBufferSizeMismatch: Optional[float]
    IsisOwnLspPurge: Optional[float]
    IsisProtocolsSupportedMismatch: Optional[float]
    IsisRejectedAdjacency: Optional[float]
    IsisSequenceNumberSkip: Optional[float]
    IsisVersionSkew: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IsisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IsisDefinition"]:
        if not json_data:
            return None
        return cls(
            IsisAdjacencyChange=json_data.get("IsisAdjacencyChange"),
            IsisAreaMismatch=json_data.get("IsisAreaMismatch"),
            IsisAttemptToExceedMaxSequence=json_data.get("IsisAttemptToExceedMaxSequence"),
            IsisAuthenticationFailure=json_data.get("IsisAuthenticationFailure"),
            IsisAuthenticationTypeFailure=json_data.get("IsisAuthenticationTypeFailure"),
            IsisCorruptedLspDetected=json_data.get("IsisCorruptedLspDetected"),
            IsisDatabaseOverload=json_data.get("IsisDatabaseOverload"),
            IsisIdLenMismatch=json_data.get("IsisIdLenMismatch"),
            IsisLspTooLargeToPropagate=json_data.get("IsisLspTooLargeToPropagate"),
            IsisManualAddressDrops=json_data.get("IsisManualAddressDrops"),
            IsisMaxAreaAddressesMismatch=json_data.get("IsisMaxAreaAddressesMismatch"),
            IsisOriginatingLspBufferSizeMismatch=json_data.get("IsisOriginatingLspBufferSizeMismatch"),
            IsisOwnLspPurge=json_data.get("IsisOwnLspPurge"),
            IsisProtocolsSupportedMismatch=json_data.get("IsisProtocolsSupportedMismatch"),
            IsisRejectedAdjacency=json_data.get("IsisRejectedAdjacency"),
            IsisSequenceNumberSkip=json_data.get("IsisSequenceNumberSkip"),
            IsisVersionSkew=json_data.get("IsisVersionSkew"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IsisDefinition = IsisDefinition


@dataclass
class OspfDefinition(BaseModel):
    OspfIfAuthFailure: Optional[float]
    OspfIfConfigError: Optional[float]
    OspfIfRxBadPacket: Optional[float]
    OspfIfStateChange: Optional[float]
    OspfLsdbApproachingOverflow: Optional[float]
    OspfLsdbOverflow: Optional[float]
    OspfMaxAgeLsa: Optional[float]
    OspfNbrStateChange: Optional[float]
    OspfOriginateLsa: Optional[float]
    OspfTxRetransmit: Optional[float]
    OspfVirtIfAuthFailure: Optional[float]
    OspfVirtIfConfigError: Optional[float]
    OspfVirtIfRxBadPacket: Optional[float]
    OspfVirtIfStateChange: Optional[float]
    OspfVirtIfTxRetransmit: Optional[float]
    OspfVirtNbrStateChange: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OspfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OspfDefinition"]:
        if not json_data:
            return None
        return cls(
            OspfIfAuthFailure=json_data.get("OspfIfAuthFailure"),
            OspfIfConfigError=json_data.get("OspfIfConfigError"),
            OspfIfRxBadPacket=json_data.get("OspfIfRxBadPacket"),
            OspfIfStateChange=json_data.get("OspfIfStateChange"),
            OspfLsdbApproachingOverflow=json_data.get("OspfLsdbApproachingOverflow"),
            OspfLsdbOverflow=json_data.get("OspfLsdbOverflow"),
            OspfMaxAgeLsa=json_data.get("OspfMaxAgeLsa"),
            OspfNbrStateChange=json_data.get("OspfNbrStateChange"),
            OspfOriginateLsa=json_data.get("OspfOriginateLsa"),
            OspfTxRetransmit=json_data.get("OspfTxRetransmit"),
            OspfVirtIfAuthFailure=json_data.get("OspfVirtIfAuthFailure"),
            OspfVirtIfConfigError=json_data.get("OspfVirtIfConfigError"),
            OspfVirtIfRxBadPacket=json_data.get("OspfVirtIfRxBadPacket"),
            OspfVirtIfStateChange=json_data.get("OspfVirtIfStateChange"),
            OspfVirtIfTxRetransmit=json_data.get("OspfVirtIfTxRetransmit"),
            OspfVirtNbrStateChange=json_data.get("OspfVirtNbrStateChange"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OspfDefinition = OspfDefinition


@dataclass
class SlbDefinition(BaseModel):
    All: Optional[float]
    ApplicationBufferLimit: Optional[float]
    BwRateLimitExceed: Optional[float]
    BwRateLimitResume: Optional[float]
    GatewayDown: Optional[float]
    GatewayUp: Optional[float]
    ServerConnLimit: Optional[float]
    ServerConnResume: Optional[float]
    ServerDisabled: Optional[float]
    ServerDown: Optional[float]
    ServerSelectionFailure: Optional[float]
    ServerUp: Optional[float]
    ServiceConnLimit: Optional[float]
    ServiceConnResume: Optional[float]
    ServiceDown: Optional[float]
    ServiceGroupDown: Optional[float]
    ServiceGroupMemberDown: Optional[float]
    ServiceGroupMemberUp: Optional[float]
    ServiceGroupUp: Optional[float]
    ServiceUp: Optional[float]
    Uuid: Optional[str]
    VipConnlimit: Optional[float]
    VipConnratelimit: Optional[float]
    VipDown: Optional[float]
    VipPortConnlimit: Optional[float]
    VipPortConnratelimit: Optional[float]
    VipPortDown: Optional[float]
    VipPortUp: Optional[float]
    VipUp: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SlbDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlbDefinition"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            ApplicationBufferLimit=json_data.get("ApplicationBufferLimit"),
            BwRateLimitExceed=json_data.get("BwRateLimitExceed"),
            BwRateLimitResume=json_data.get("BwRateLimitResume"),
            GatewayDown=json_data.get("GatewayDown"),
            GatewayUp=json_data.get("GatewayUp"),
            ServerConnLimit=json_data.get("ServerConnLimit"),
            ServerConnResume=json_data.get("ServerConnResume"),
            ServerDisabled=json_data.get("ServerDisabled"),
            ServerDown=json_data.get("ServerDown"),
            ServerSelectionFailure=json_data.get("ServerSelectionFailure"),
            ServerUp=json_data.get("ServerUp"),
            ServiceConnLimit=json_data.get("ServiceConnLimit"),
            ServiceConnResume=json_data.get("ServiceConnResume"),
            ServiceDown=json_data.get("ServiceDown"),
            ServiceGroupDown=json_data.get("ServiceGroupDown"),
            ServiceGroupMemberDown=json_data.get("ServiceGroupMemberDown"),
            ServiceGroupMemberUp=json_data.get("ServiceGroupMemberUp"),
            ServiceGroupUp=json_data.get("ServiceGroupUp"),
            ServiceUp=json_data.get("ServiceUp"),
            Uuid=json_data.get("Uuid"),
            VipConnlimit=json_data.get("VipConnlimit"),
            VipConnratelimit=json_data.get("VipConnratelimit"),
            VipDown=json_data.get("VipDown"),
            VipPortConnlimit=json_data.get("VipPortConnlimit"),
            VipPortConnratelimit=json_data.get("VipPortConnratelimit"),
            VipPortDown=json_data.get("VipPortDown"),
            VipPortUp=json_data.get("VipPortUp"),
            VipUp=json_data.get("VipUp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlbDefinition = SlbDefinition


@dataclass
class SlbChangeDefinition(BaseModel):
    All: Optional[float]
    ConnectionResourceEvent: Optional[float]
    ResourceUsageWarning: Optional[float]
    Server: Optional[float]
    ServerPort: Optional[float]
    SslCertChange: Optional[float]
    SslCertExpire: Optional[float]
    SystemThreshold: Optional[float]
    Uuid: Optional[str]
    Vip: Optional[float]
    VipPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SlbChangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlbChangeDefinition"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            ConnectionResourceEvent=json_data.get("ConnectionResourceEvent"),
            ResourceUsageWarning=json_data.get("ResourceUsageWarning"),
            Server=json_data.get("Server"),
            ServerPort=json_data.get("ServerPort"),
            SslCertChange=json_data.get("SslCertChange"),
            SslCertExpire=json_data.get("SslCertExpire"),
            SystemThreshold=json_data.get("SystemThreshold"),
            Uuid=json_data.get("Uuid"),
            Vip=json_data.get("Vip"),
            VipPort=json_data.get("VipPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlbChangeDefinition = SlbChangeDefinition


@dataclass
class SnmpDefinition(BaseModel):
    All: Optional[float]
    Linkdown: Optional[float]
    Linkup: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnmpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnmpDefinition"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            Linkdown=json_data.get("Linkdown"),
            Linkup=json_data.get("Linkup"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnmpDefinition = SnmpDefinition


@dataclass
class SslDefinition(BaseModel):
    ServerCertificateError: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslDefinition"]:
        if not json_data:
            return None
        return cls(
            ServerCertificateError=json_data.get("ServerCertificateError"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslDefinition = SslDefinition


@dataclass
class SystemDefinition(BaseModel):
    All: Optional[float]
    ControlCpuHigh: Optional[float]
    DataCpuHigh: Optional[float]
    Fan: Optional[float]
    FileSysReadOnly: Optional[float]
    HighDiskUse: Optional[float]
    HighMemoryUse: Optional[float]
    HighTemp: Optional[float]
    LicenseManagement: Optional[float]
    LowTemp: Optional[float]
    PacketDrop: Optional[float]
    Power: Optional[float]
    PriDisk: Optional[float]
    Restart: Optional[float]
    SecDisk: Optional[float]
    Shutdown: Optional[float]
    SmpResourceEvent: Optional[float]
    Start: Optional[float]
    SyslogSeverityOne: Optional[float]
    TacacsServerUpDown: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemDefinition"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            ControlCpuHigh=json_data.get("ControlCpuHigh"),
            DataCpuHigh=json_data.get("DataCpuHigh"),
            Fan=json_data.get("Fan"),
            FileSysReadOnly=json_data.get("FileSysReadOnly"),
            HighDiskUse=json_data.get("HighDiskUse"),
            HighMemoryUse=json_data.get("HighMemoryUse"),
            HighTemp=json_data.get("HighTemp"),
            LicenseManagement=json_data.get("LicenseManagement"),
            LowTemp=json_data.get("LowTemp"),
            PacketDrop=json_data.get("PacketDrop"),
            Power=json_data.get("Power"),
            PriDisk=json_data.get("PriDisk"),
            Restart=json_data.get("Restart"),
            SecDisk=json_data.get("SecDisk"),
            Shutdown=json_data.get("Shutdown"),
            SmpResourceEvent=json_data.get("SmpResourceEvent"),
            Start=json_data.get("Start"),
            SyslogSeverityOne=json_data.get("SyslogSeverityOne"),
            TacacsServerUpDown=json_data.get("TacacsServerUpDown"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemDefinition = SystemDefinition


@dataclass
class VcsDefinition(BaseModel):
    StateChange: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VcsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VcsDefinition"]:
        if not json_data:
            return None
        return cls(
            StateChange=json_data.get("StateChange"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VcsDefinition = VcsDefinition


@dataclass
class VrrpADefinition(BaseModel):
    Active: Optional[float]
    All: Optional[float]
    Standby: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VrrpADefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VrrpADefinition"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
            All=json_data.get("All"),
            Standby=json_data.get("Standby"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VrrpADefinition = VrrpADefinition


