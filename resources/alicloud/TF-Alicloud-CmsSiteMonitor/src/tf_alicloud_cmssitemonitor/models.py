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
    Address: Optional[str]
    AlertIds: Optional[Sequence[str]]
    CreateTime: Optional[str]
    Id: Optional[str]
    Interval: Optional[float]
    OptionsJson: Optional[str]
    TaskName: Optional[str]
    TaskState: Optional[str]
    TaskType: Optional[str]
    UpdateTime: Optional[str]
    IspCities: Optional[Sequence["_IspCitiesDefinition"]]

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
            Address=json_data.get("Address"),
            AlertIds=json_data.get("AlertIds"),
            CreateTime=json_data.get("CreateTime"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            OptionsJson=json_data.get("OptionsJson"),
            TaskName=json_data.get("TaskName"),
            TaskState=json_data.get("TaskState"),
            TaskType=json_data.get("TaskType"),
            UpdateTime=json_data.get("UpdateTime"),
            IspCities=deserialize_list(json_data.get("IspCities"), IspCitiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IspCitiesDefinition(BaseModel):
    City: Optional[str]
    Isp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IspCitiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IspCitiesDefinition"]:
        if not json_data:
            return None
        return cls(
            City=json_data.get("City"),
            Isp=json_data.get("Isp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IspCitiesDefinition = IspCitiesDefinition


