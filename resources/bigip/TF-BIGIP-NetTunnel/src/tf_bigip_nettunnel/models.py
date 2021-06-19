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
    AppService: Optional[str]
    AutoLastHop: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IdleTimeout: Optional[float]
    Key: Optional[float]
    LocalAddress: Optional[str]
    Mode: Optional[str]
    Mtu: Optional[float]
    Name: Optional[str]
    Partition: Optional[str]
    Profile: Optional[str]
    RemoteAddress: Optional[str]
    SecondaryAddress: Optional[str]
    Tos: Optional[str]
    TrafficGroup: Optional[str]
    Transparent: Optional[str]
    UsePmtu: Optional[str]

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
            AppService=json_data.get("AppService"),
            AutoLastHop=json_data.get("AutoLastHop"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IdleTimeout=json_data.get("IdleTimeout"),
            Key=json_data.get("Key"),
            LocalAddress=json_data.get("LocalAddress"),
            Mode=json_data.get("Mode"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            Partition=json_data.get("Partition"),
            Profile=json_data.get("Profile"),
            RemoteAddress=json_data.get("RemoteAddress"),
            SecondaryAddress=json_data.get("SecondaryAddress"),
            Tos=json_data.get("Tos"),
            TrafficGroup=json_data.get("TrafficGroup"),
            Transparent=json_data.get("Transparent"),
            UsePmtu=json_data.get("UsePmtu"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


