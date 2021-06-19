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
    CnameCoalescingEnabled: Optional[bool]
    Comment: Optional[str]
    Contract: Optional[str]
    DefaultErrorPenalty: Optional[float]
    DefaultHealthMax: Optional[float]
    DefaultHealthMultiplier: Optional[float]
    DefaultHealthThreshold: Optional[float]
    DefaultMaxUnreachablePenalty: Optional[float]
    DefaultSslClientCertificate: Optional[str]
    DefaultSslClientPrivateKey: Optional[str]
    DefaultTimeoutPenalty: Optional[float]
    DefaultUnreachableThreshold: Optional[float]
    EmailNotificationList: Optional[Sequence[str]]
    EndUserMappingEnabled: Optional[bool]
    Group: Optional[str]
    Id: Optional[str]
    LoadFeedback: Optional[bool]
    LoadImbalancePercentage: Optional[float]
    MapUpdateInterval: Optional[float]
    MaxProperties: Optional[float]
    MaxResources: Optional[float]
    MaxTestTimeout: Optional[float]
    MaxTtl: Optional[float]
    MinPingableRegionFraction: Optional[float]
    MinTestInterval: Optional[float]
    MinTtl: Optional[float]
    Name: Optional[str]
    PingInterval: Optional[float]
    PingPacketSize: Optional[float]
    RoundRobinPrefix: Optional[str]
    ServermonitorLivenessCount: Optional[float]
    ServermonitorLoadCount: Optional[float]
    ServermonitorPool: Optional[str]
    Type: Optional[str]
    WaitOnComplete: Optional[bool]

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
            CnameCoalescingEnabled=json_data.get("CnameCoalescingEnabled"),
            Comment=json_data.get("Comment"),
            Contract=json_data.get("Contract"),
            DefaultErrorPenalty=json_data.get("DefaultErrorPenalty"),
            DefaultHealthMax=json_data.get("DefaultHealthMax"),
            DefaultHealthMultiplier=json_data.get("DefaultHealthMultiplier"),
            DefaultHealthThreshold=json_data.get("DefaultHealthThreshold"),
            DefaultMaxUnreachablePenalty=json_data.get("DefaultMaxUnreachablePenalty"),
            DefaultSslClientCertificate=json_data.get("DefaultSslClientCertificate"),
            DefaultSslClientPrivateKey=json_data.get("DefaultSslClientPrivateKey"),
            DefaultTimeoutPenalty=json_data.get("DefaultTimeoutPenalty"),
            DefaultUnreachableThreshold=json_data.get("DefaultUnreachableThreshold"),
            EmailNotificationList=json_data.get("EmailNotificationList"),
            EndUserMappingEnabled=json_data.get("EndUserMappingEnabled"),
            Group=json_data.get("Group"),
            Id=json_data.get("Id"),
            LoadFeedback=json_data.get("LoadFeedback"),
            LoadImbalancePercentage=json_data.get("LoadImbalancePercentage"),
            MapUpdateInterval=json_data.get("MapUpdateInterval"),
            MaxProperties=json_data.get("MaxProperties"),
            MaxResources=json_data.get("MaxResources"),
            MaxTestTimeout=json_data.get("MaxTestTimeout"),
            MaxTtl=json_data.get("MaxTtl"),
            MinPingableRegionFraction=json_data.get("MinPingableRegionFraction"),
            MinTestInterval=json_data.get("MinTestInterval"),
            MinTtl=json_data.get("MinTtl"),
            Name=json_data.get("Name"),
            PingInterval=json_data.get("PingInterval"),
            PingPacketSize=json_data.get("PingPacketSize"),
            RoundRobinPrefix=json_data.get("RoundRobinPrefix"),
            ServermonitorLivenessCount=json_data.get("ServermonitorLivenessCount"),
            ServermonitorLoadCount=json_data.get("ServermonitorLoadCount"),
            ServermonitorPool=json_data.get("ServermonitorPool"),
            Type=json_data.get("Type"),
            WaitOnComplete=json_data.get("WaitOnComplete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


