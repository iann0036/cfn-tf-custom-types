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
    Arn: Optional[str]
    EndTime: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ResourceId: Optional[str]
    ScalableDimension: Optional[str]
    Schedule: Optional[str]
    ServiceNamespace: Optional[str]
    StartTime: Optional[str]
    Timezone: Optional[str]
    ScalableTargetAction: Optional[Sequence["_ScalableTargetActionDefinition"]]

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
            Arn=json_data.get("Arn"),
            EndTime=json_data.get("EndTime"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResourceId=json_data.get("ResourceId"),
            ScalableDimension=json_data.get("ScalableDimension"),
            Schedule=json_data.get("Schedule"),
            ServiceNamespace=json_data.get("ServiceNamespace"),
            StartTime=json_data.get("StartTime"),
            Timezone=json_data.get("Timezone"),
            ScalableTargetAction=deserialize_list(json_data.get("ScalableTargetAction"), ScalableTargetActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ScalableTargetActionDefinition(BaseModel):
    MaxCapacity: Optional[str]
    MinCapacity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScalableTargetActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalableTargetActionDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxCapacity=json_data.get("MaxCapacity"),
            MinCapacity=json_data.get("MinCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalableTargetActionDefinition = ScalableTargetActionDefinition


