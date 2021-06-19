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
    Affinity: Optional[str]
    DynamicSortSubtable: Optional[str]
    GroupDownOption: Optional[str]
    Id: Optional[str]
    LdbMethod: Optional[str]
    Name: Optional[str]
    Vdomparam: Optional[str]
    ServerList: Optional[Sequence["_ServerListDefinition"]]

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
            Affinity=json_data.get("Affinity"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            GroupDownOption=json_data.get("GroupDownOption"),
            Id=json_data.get("Id"),
            LdbMethod=json_data.get("LdbMethod"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            ServerList=deserialize_list(json_data.get("ServerList"), ServerListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ServerListDefinition(BaseModel):
    Name: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServerListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerListDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerListDefinition = ServerListDefinition


