# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Arn: Optional[str]
    EndTime: Optional[str]
    Name: Optional[str]
    ResourceId: Optional[str]
    ScalableDimension: Optional[str]
    Schedule: Optional[str]
    ServiceNamespace: Optional[str]
    StartTime: Optional[str]
    ScalableTargetAction: Optional[Sequence["_ScalableTargetAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            EndTime=json_data.get("EndTime"),
            Name=json_data.get("Name"),
            ResourceId=json_data.get("ResourceId"),
            ScalableDimension=json_data.get("ScalableDimension"),
            Schedule=json_data.get("Schedule"),
            ServiceNamespace=json_data.get("ServiceNamespace"),
            StartTime=json_data.get("StartTime"),
            ScalableTargetAction=json_data.get("ScalableTargetAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ScalableTargetAction:
    MaxCapacity: Optional[float]
    MinCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ScalableTargetAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalableTargetAction"]:
        if not json_data:
            return None
        return cls(
            MaxCapacity=json_data.get("MaxCapacity"),
            MinCapacity=json_data.get("MinCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalableTargetAction = ScalableTargetAction


