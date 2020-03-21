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
    Description: Optional[str]
    Rules: Optional[Sequence["_Rules"]]
    Time: Optional[Sequence["_Time"]]
    Entity: Optional[Sequence["_Entity"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Rules=json_data.get("Rules"),
            Time=json_data.get("Time"),
            Entity=json_data.get("Entity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Rules:
    State: Optional[str]
    Entity: Optional[Sequence["_Entity"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rules"]:
        if not json_data:
            return None
        return cls(
            State=json_data.get("State"),
            Entity=json_data.get("Entity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rules = Rules


@dataclass
class Entity:
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Entity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Entity"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Entity = Entity


@dataclass
class Time:
    EndDate: Optional[str]
    StartDate: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Time"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Time"]:
        if not json_data:
            return None
        return cls(
            EndDate=json_data.get("EndDate"),
            StartDate=json_data.get("StartDate"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Time = Time


