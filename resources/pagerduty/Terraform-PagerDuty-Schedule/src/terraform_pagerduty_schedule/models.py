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
    Id: Optional[str]
    Name: Optional[str]
    Overflow: Optional[bool]
    TimeZone: Optional[str]
    Layer: Optional[Sequence["_Layer"]]
    Restriction: Optional[Sequence["_Restriction"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Overflow=json_data.get("Overflow"),
            TimeZone=json_data.get("TimeZone"),
            Layer=json_data.get("Layer"),
            Restriction=json_data.get("Restriction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Layer:
    End: Optional[str]
    Name: Optional[str]
    RotationTurnLengthSeconds: Optional[float]
    RotationVirtualStart: Optional[str]
    Start: Optional[str]
    Users: Optional[Sequence[str]]
    Restriction: Optional[Sequence["_Restriction"]]

    @classmethod
    def _deserialize(
        cls: Type["_Layer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Layer"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Name=json_data.get("Name"),
            RotationTurnLengthSeconds=json_data.get("RotationTurnLengthSeconds"),
            RotationVirtualStart=json_data.get("RotationVirtualStart"),
            Start=json_data.get("Start"),
            Users=json_data.get("Users"),
            Restriction=json_data.get("Restriction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Layer = Layer


@dataclass
class Restriction:
    DurationSeconds: Optional[float]
    StartDayOfWeek: Optional[float]
    StartTimeOfDay: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Restriction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Restriction"]:
        if not json_data:
            return None
        return cls(
            DurationSeconds=json_data.get("DurationSeconds"),
            StartDayOfWeek=json_data.get("StartDayOfWeek"),
            StartTimeOfDay=json_data.get("StartTimeOfDay"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Restriction = Restriction


