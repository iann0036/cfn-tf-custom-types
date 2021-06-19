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
    City: Optional[str]
    CloneOf: Optional[float]
    CloudServerHostHeaderOverride: Optional[bool]
    CloudServerTargeting: Optional[bool]
    Continent: Optional[str]
    Country: Optional[str]
    DatacenterId: Optional[float]
    Domain: Optional[str]
    Id: Optional[str]
    Latitude: Optional[float]
    Longitude: Optional[float]
    Nickname: Optional[str]
    PingInterval: Optional[float]
    PingPacketSize: Optional[float]
    ScorePenalty: Optional[float]
    ServermonitorLivenessCount: Optional[float]
    ServermonitorLoadCount: Optional[float]
    ServermonitorPool: Optional[str]
    StateOrProvince: Optional[str]
    Virtual: Optional[bool]
    WaitOnComplete: Optional[bool]
    DefaultLoadObject: Optional[Sequence["_DefaultLoadObjectDefinition"]]

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
            City=json_data.get("City"),
            CloneOf=json_data.get("CloneOf"),
            CloudServerHostHeaderOverride=json_data.get("CloudServerHostHeaderOverride"),
            CloudServerTargeting=json_data.get("CloudServerTargeting"),
            Continent=json_data.get("Continent"),
            Country=json_data.get("Country"),
            DatacenterId=json_data.get("DatacenterId"),
            Domain=json_data.get("Domain"),
            Id=json_data.get("Id"),
            Latitude=json_data.get("Latitude"),
            Longitude=json_data.get("Longitude"),
            Nickname=json_data.get("Nickname"),
            PingInterval=json_data.get("PingInterval"),
            PingPacketSize=json_data.get("PingPacketSize"),
            ScorePenalty=json_data.get("ScorePenalty"),
            ServermonitorLivenessCount=json_data.get("ServermonitorLivenessCount"),
            ServermonitorLoadCount=json_data.get("ServermonitorLoadCount"),
            ServermonitorPool=json_data.get("ServermonitorPool"),
            StateOrProvince=json_data.get("StateOrProvince"),
            Virtual=json_data.get("Virtual"),
            WaitOnComplete=json_data.get("WaitOnComplete"),
            DefaultLoadObject=deserialize_list(json_data.get("DefaultLoadObject"), DefaultLoadObjectDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefaultLoadObjectDefinition(BaseModel):
    LoadObject: Optional[str]
    LoadObjectPort: Optional[float]
    LoadServers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultLoadObjectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultLoadObjectDefinition"]:
        if not json_data:
            return None
        return cls(
            LoadObject=json_data.get("LoadObject"),
            LoadObjectPort=json_data.get("LoadObjectPort"),
            LoadServers=json_data.get("LoadServers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultLoadObjectDefinition = DefaultLoadObjectDefinition


