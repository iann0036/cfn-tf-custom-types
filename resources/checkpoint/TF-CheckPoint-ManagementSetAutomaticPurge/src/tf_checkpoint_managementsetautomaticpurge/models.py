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
    Enabled: Optional[bool]
    Id: Optional[str]
    KeepSessionsByCount: Optional[bool]
    KeepSessionsByDays: Optional[bool]
    NumberOfDaysToKeep: Optional[float]
    NumberOfSessionsToKeep: Optional[float]
    Scheduling: Optional[Sequence["_SchedulingDefinition"]]

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
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            KeepSessionsByCount=json_data.get("KeepSessionsByCount"),
            KeepSessionsByDays=json_data.get("KeepSessionsByDays"),
            NumberOfDaysToKeep=json_data.get("NumberOfDaysToKeep"),
            NumberOfSessionsToKeep=json_data.get("NumberOfSessionsToKeep"),
            Scheduling=deserialize_list(json_data.get("Scheduling"), SchedulingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SchedulingDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchedulingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchedulingDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchedulingDefinition = SchedulingDefinition


