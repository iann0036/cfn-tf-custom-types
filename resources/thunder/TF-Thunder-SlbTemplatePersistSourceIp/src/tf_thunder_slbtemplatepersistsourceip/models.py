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
    DontHonorConnRules: Optional[float]
    EnforceHigherPriority: Optional[float]
    HashPersist: Optional[float]
    Id: Optional[str]
    InclDstIp: Optional[float]
    InclSport: Optional[float]
    MatchType: Optional[float]
    Name: Optional[str]
    Netmask: Optional[str]
    Netmask6: Optional[float]
    PrimaryPort: Optional[float]
    ScanAllMembers: Optional[float]
    Server: Optional[float]
    ServiceGroup: Optional[float]
    Timeout: Optional[float]
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
            DontHonorConnRules=json_data.get("DontHonorConnRules"),
            EnforceHigherPriority=json_data.get("EnforceHigherPriority"),
            HashPersist=json_data.get("HashPersist"),
            Id=json_data.get("Id"),
            InclDstIp=json_data.get("InclDstIp"),
            InclSport=json_data.get("InclSport"),
            MatchType=json_data.get("MatchType"),
            Name=json_data.get("Name"),
            Netmask=json_data.get("Netmask"),
            Netmask6=json_data.get("Netmask6"),
            PrimaryPort=json_data.get("PrimaryPort"),
            ScanAllMembers=json_data.get("ScanAllMembers"),
            Server=json_data.get("Server"),
            ServiceGroup=json_data.get("ServiceGroup"),
            Timeout=json_data.get("Timeout"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


