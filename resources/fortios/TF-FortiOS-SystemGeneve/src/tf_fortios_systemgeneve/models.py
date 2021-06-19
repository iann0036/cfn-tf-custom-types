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
    Id: Optional[str]
    Interface: Optional[str]
    IpVersion: Optional[str]
    Name: Optional[str]
    RemoteIp: Optional[str]
    RemoteIp6: Optional[str]
    Vdomparam: Optional[str]
    Vni: Optional[float]

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
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            IpVersion=json_data.get("IpVersion"),
            Name=json_data.get("Name"),
            RemoteIp=json_data.get("RemoteIp"),
            RemoteIp6=json_data.get("RemoteIp6"),
            Vdomparam=json_data.get("Vdomparam"),
            Vni=json_data.get("Vni"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


