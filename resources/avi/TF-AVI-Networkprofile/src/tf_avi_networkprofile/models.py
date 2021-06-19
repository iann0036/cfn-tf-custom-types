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
    ConnectionMirror: Optional[bool]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    Profile: Optional[Sequence["_ProfileDefinition"]]

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
            ConnectionMirror=json_data.get("ConnectionMirror"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            Profile=deserialize_list(json_data.get("Profile"), ProfileDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


@dataclass
class ProfileDefinition(BaseModel):
    Type: Optional[str]
    TcpFastPathProfile: Optional[Sequence["_TcpFastPathProfileDefinition"]]
    TcpProxyProfile: Optional[Sequence["_TcpProxyProfileDefinition"]]
    UdpFastPathProfile: Optional[Sequence["_UdpFastPathProfileDefinition"]]
    UdpProxyProfile: Optional[Sequence["_UdpProxyProfileDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            TcpFastPathProfile=deserialize_list(json_data.get("TcpFastPathProfile"), TcpFastPathProfileDefinition),
            TcpProxyProfile=deserialize_list(json_data.get("TcpProxyProfile"), TcpProxyProfileDefinition),
            UdpFastPathProfile=deserialize_list(json_data.get("UdpFastPathProfile"), UdpFastPathProfileDefinition),
            UdpProxyProfile=deserialize_list(json_data.get("UdpProxyProfile"), UdpProxyProfileDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProfileDefinition = ProfileDefinition


@dataclass
class TcpFastPathProfileDefinition(BaseModel):
    EnableSynProtection: Optional[bool]
    SessionIdleTimeout: Optional[float]
    DsrProfile: Optional[Sequence["_DsrProfileDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TcpFastPathProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpFastPathProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableSynProtection=json_data.get("EnableSynProtection"),
            SessionIdleTimeout=json_data.get("SessionIdleTimeout"),
            DsrProfile=deserialize_list(json_data.get("DsrProfile"), DsrProfileDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpFastPathProfileDefinition = TcpFastPathProfileDefinition


@dataclass
class DsrProfileDefinition(BaseModel):
    DsrEncapType: Optional[str]
    DsrType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DsrProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DsrProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            DsrEncapType=json_data.get("DsrEncapType"),
            DsrType=json_data.get("DsrType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DsrProfileDefinition = DsrProfileDefinition


@dataclass
class TcpProxyProfileDefinition(BaseModel):
    AggressiveCongestionAvoidance: Optional[bool]
    AutoWindowGrowth: Optional[bool]
    Automatic: Optional[bool]
    CcAlgo: Optional[str]
    CongestionRecoveryScalingFactor: Optional[float]
    IdleConnectionTimeout: Optional[float]
    IdleConnectionType: Optional[str]
    IgnoreTimeWait: Optional[bool]
    IpDscp: Optional[float]
    KeepaliveInHalfcloseState: Optional[bool]
    MaxRetransmissions: Optional[float]
    MaxSegmentSize: Optional[float]
    MaxSynRetransmissions: Optional[float]
    MinRexmtTimeout: Optional[float]
    NaglesAlgorithm: Optional[bool]
    ReassemblyQueueSize: Optional[float]
    ReceiveWindow: Optional[float]
    ReorderThreshold: Optional[float]
    SlowStartScalingFactor: Optional[float]
    TimeWaitDelay: Optional[float]
    UseInterfaceMtu: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TcpProxyProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpProxyProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            AggressiveCongestionAvoidance=json_data.get("AggressiveCongestionAvoidance"),
            AutoWindowGrowth=json_data.get("AutoWindowGrowth"),
            Automatic=json_data.get("Automatic"),
            CcAlgo=json_data.get("CcAlgo"),
            CongestionRecoveryScalingFactor=json_data.get("CongestionRecoveryScalingFactor"),
            IdleConnectionTimeout=json_data.get("IdleConnectionTimeout"),
            IdleConnectionType=json_data.get("IdleConnectionType"),
            IgnoreTimeWait=json_data.get("IgnoreTimeWait"),
            IpDscp=json_data.get("IpDscp"),
            KeepaliveInHalfcloseState=json_data.get("KeepaliveInHalfcloseState"),
            MaxRetransmissions=json_data.get("MaxRetransmissions"),
            MaxSegmentSize=json_data.get("MaxSegmentSize"),
            MaxSynRetransmissions=json_data.get("MaxSynRetransmissions"),
            MinRexmtTimeout=json_data.get("MinRexmtTimeout"),
            NaglesAlgorithm=json_data.get("NaglesAlgorithm"),
            ReassemblyQueueSize=json_data.get("ReassemblyQueueSize"),
            ReceiveWindow=json_data.get("ReceiveWindow"),
            ReorderThreshold=json_data.get("ReorderThreshold"),
            SlowStartScalingFactor=json_data.get("SlowStartScalingFactor"),
            TimeWaitDelay=json_data.get("TimeWaitDelay"),
            UseInterfaceMtu=json_data.get("UseInterfaceMtu"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpProxyProfileDefinition = TcpProxyProfileDefinition


@dataclass
class UdpFastPathProfileDefinition(BaseModel):
    PerPktLoadbalance: Optional[bool]
    SessionIdleTimeout: Optional[float]
    Snat: Optional[bool]
    DsrProfile: Optional[Sequence["_DsrProfileDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UdpFastPathProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UdpFastPathProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            PerPktLoadbalance=json_data.get("PerPktLoadbalance"),
            SessionIdleTimeout=json_data.get("SessionIdleTimeout"),
            Snat=json_data.get("Snat"),
            DsrProfile=deserialize_list(json_data.get("DsrProfile"), DsrProfileDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UdpFastPathProfileDefinition = UdpFastPathProfileDefinition


@dataclass
class UdpProxyProfileDefinition(BaseModel):
    SessionIdleTimeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_UdpProxyProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UdpProxyProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            SessionIdleTimeout=json_data.get("SessionIdleTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UdpProxyProfileDefinition = UdpProxyProfileDefinition


