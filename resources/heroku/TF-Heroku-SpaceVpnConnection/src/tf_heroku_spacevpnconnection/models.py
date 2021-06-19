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
    Id: Optional[str]
    IkeVersion: Optional[float]
    Name: Optional[str]
    PublicIp: Optional[str]
    RoutableCidrs: Optional[Sequence[str]]
    Space: Optional[str]
    SpaceCidrBlock: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]
    Tunnels: Optional[Sequence["_TunnelsDefinition"]]

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
            Id=json_data.get("Id"),
            IkeVersion=json_data.get("IkeVersion"),
            Name=json_data.get("Name"),
            PublicIp=json_data.get("PublicIp"),
            RoutableCidrs=json_data.get("RoutableCidrs"),
            Space=json_data.get("Space"),
            SpaceCidrBlock=json_data.get("SpaceCidrBlock"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            Tunnels=deserialize_list(json_data.get("Tunnels"), TunnelsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class TunnelsDefinition(BaseModel):
    Ip: Optional[str]
    PreSharedKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TunnelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TunnelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            PreSharedKey=json_data.get("PreSharedKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TunnelsDefinition = TunnelsDefinition


