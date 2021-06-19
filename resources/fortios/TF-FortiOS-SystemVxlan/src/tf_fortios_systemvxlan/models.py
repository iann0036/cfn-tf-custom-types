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
    Dstport: Optional[float]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    IpVersion: Optional[str]
    MulticastTtl: Optional[float]
    Name: Optional[str]
    Vdomparam: Optional[str]
    Vni: Optional[float]
    RemoteIp: Optional[Sequence["_RemoteIpDefinition"]]
    RemoteIp6: Optional[Sequence["_RemoteIp6Definition"]]

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
            Dstport=json_data.get("Dstport"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            IpVersion=json_data.get("IpVersion"),
            MulticastTtl=json_data.get("MulticastTtl"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            Vni=json_data.get("Vni"),
            RemoteIp=deserialize_list(json_data.get("RemoteIp"), RemoteIpDefinition),
            RemoteIp6=deserialize_list(json_data.get("RemoteIp6"), RemoteIp6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RemoteIpDefinition(BaseModel):
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RemoteIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoteIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoteIpDefinition = RemoteIpDefinition


@dataclass
class RemoteIp6Definition(BaseModel):
    Ip6: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RemoteIp6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoteIp6Definition"]:
        if not json_data:
            return None
        return cls(
            Ip6=json_data.get("Ip6"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoteIp6Definition = RemoteIp6Definition


