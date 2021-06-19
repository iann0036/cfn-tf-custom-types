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
    AckAggressiveness: Optional[str]
    AliveIfActive: Optional[float]
    BackendWscale: Optional[float]
    DelSessionOnServerDown: Optional[float]
    Disable: Optional[float]
    DisableAbc: Optional[float]
    DisableSack: Optional[float]
    DisableTcpTimestamps: Optional[float]
    DisableWindowScale: Optional[float]
    Down: Optional[float]
    DynamicBufferAllocation: Optional[float]
    EarlyRetransmit: Optional[float]
    FinTimeout: Optional[float]
    ForceDeleteTimeout: Optional[float]
    ForceDeleteTimeout100ms: Optional[float]
    HalfCloseIdleTimeout: Optional[float]
    HalfOpenIdleTimeout: Optional[float]
    Id: Optional[str]
    IdleTimeout: Optional[float]
    InitCwnd: Optional[float]
    InitialWindowSize: Optional[float]
    InsertClientIp: Optional[float]
    InvalidRateLimit: Optional[float]
    KeepaliveInterval: Optional[float]
    KeepaliveProbes: Optional[float]
    LimitedSlowstart: Optional[float]
    Maxburst: Optional[float]
    MinRto: Optional[float]
    Mss: Optional[float]
    Nagle: Optional[float]
    Name: Optional[str]
    PshFlagOptimization: Optional[float]
    Qos: Optional[float]
    ReassemblyLimit: Optional[float]
    ReassemblyTimeout: Optional[float]
    ReceiveBuffer: Optional[float]
    Reno: Optional[float]
    ResetFwd: Optional[float]
    ResetRev: Optional[float]
    RetransmitRetries: Optional[float]
    ServerDownAction: Optional[str]
    SynRetries: Optional[float]
    Timewait: Optional[float]
    TransmitBuffer: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]

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
            AckAggressiveness=json_data.get("AckAggressiveness"),
            AliveIfActive=json_data.get("AliveIfActive"),
            BackendWscale=json_data.get("BackendWscale"),
            DelSessionOnServerDown=json_data.get("DelSessionOnServerDown"),
            Disable=json_data.get("Disable"),
            DisableAbc=json_data.get("DisableAbc"),
            DisableSack=json_data.get("DisableSack"),
            DisableTcpTimestamps=json_data.get("DisableTcpTimestamps"),
            DisableWindowScale=json_data.get("DisableWindowScale"),
            Down=json_data.get("Down"),
            DynamicBufferAllocation=json_data.get("DynamicBufferAllocation"),
            EarlyRetransmit=json_data.get("EarlyRetransmit"),
            FinTimeout=json_data.get("FinTimeout"),
            ForceDeleteTimeout=json_data.get("ForceDeleteTimeout"),
            ForceDeleteTimeout100ms=json_data.get("ForceDeleteTimeout100ms"),
            HalfCloseIdleTimeout=json_data.get("HalfCloseIdleTimeout"),
            HalfOpenIdleTimeout=json_data.get("HalfOpenIdleTimeout"),
            Id=json_data.get("Id"),
            IdleTimeout=json_data.get("IdleTimeout"),
            InitCwnd=json_data.get("InitCwnd"),
            InitialWindowSize=json_data.get("InitialWindowSize"),
            InsertClientIp=json_data.get("InsertClientIp"),
            InvalidRateLimit=json_data.get("InvalidRateLimit"),
            KeepaliveInterval=json_data.get("KeepaliveInterval"),
            KeepaliveProbes=json_data.get("KeepaliveProbes"),
            LimitedSlowstart=json_data.get("LimitedSlowstart"),
            Maxburst=json_data.get("Maxburst"),
            MinRto=json_data.get("MinRto"),
            Mss=json_data.get("Mss"),
            Nagle=json_data.get("Nagle"),
            Name=json_data.get("Name"),
            PshFlagOptimization=json_data.get("PshFlagOptimization"),
            Qos=json_data.get("Qos"),
            ReassemblyLimit=json_data.get("ReassemblyLimit"),
            ReassemblyTimeout=json_data.get("ReassemblyTimeout"),
            ReceiveBuffer=json_data.get("ReceiveBuffer"),
            Reno=json_data.get("Reno"),
            ResetFwd=json_data.get("ResetFwd"),
            ResetRev=json_data.get("ResetRev"),
            RetransmitRetries=json_data.get("RetransmitRetries"),
            ServerDownAction=json_data.get("ServerDownAction"),
            SynRetries=json_data.get("SynRetries"),
            Timewait=json_data.get("Timewait"),
            TransmitBuffer=json_data.get("TransmitBuffer"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


