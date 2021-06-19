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
    AgentAnonMode: Optional[str]
    AgentLevel: Optional[str]
    BlockDurationSeconds: Optional[float]
    BlockHttpCode: Optional[float]
    DisplayName: Optional[str]
    Id: Optional[str]
    PrimaryAgentKey: Optional[Sequence["_PrimaryAgentKeyDefinition"]]
    ShortName: Optional[str]

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
            AgentAnonMode=json_data.get("AgentAnonMode"),
            AgentLevel=json_data.get("AgentLevel"),
            BlockDurationSeconds=json_data.get("BlockDurationSeconds"),
            BlockHttpCode=json_data.get("BlockHttpCode"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            PrimaryAgentKey=deserialize_list(json_data.get("PrimaryAgentKey"), PrimaryAgentKeyDefinition),
            ShortName=json_data.get("ShortName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PrimaryAgentKeyDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrimaryAgentKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrimaryAgentKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrimaryAgentKeyDefinition = PrimaryAgentKeyDefinition


