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
    EndDate: Optional[str]
    Id: Optional[str]
    Length: Optional[float]
    Name: Optional[str]
    ScheduleId: Optional[str]
    StartDate: Optional[str]
    Type: Optional[str]
    Participant: Optional[Sequence["_Participant"]]
    TimeRestriction: Optional[Sequence["_TimeRestriction"]]
    Restriction: Optional[Sequence["_Restriction"]]
    Restrictions: Optional[Sequence["_Restrictions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EndDate=json_data.get("EndDate"),
            Id=json_data.get("Id"),
            Length=json_data.get("Length"),
            Name=json_data.get("Name"),
            ScheduleId=json_data.get("ScheduleId"),
            StartDate=json_data.get("StartDate"),
            Type=json_data.get("Type"),
            Participant=json_data.get("Participant"),
            TimeRestriction=json_data.get("TimeRestriction"),
            Restriction=json_data.get("Restriction"),
            Restrictions=json_data.get("Restrictions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Participant:
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Participant"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Participant"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Participant = Participant


@dataclass
class TimeRestriction:
    Type: Optional[str]
    Restriction: Optional[Sequence["_Restriction"]]
    Restrictions: Optional[Sequence["_Restrictions"]]

    @classmethod
    def _deserialize(
        cls: Type["_TimeRestriction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeRestriction"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Restriction=json_data.get("Restriction"),
            Restrictions=json_data.get("Restrictions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeRestriction = TimeRestriction


@dataclass
class Restriction:
    EndHour: Optional[float]
    EndMin: Optional[float]
    StartHour: Optional[float]
    StartMin: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Restriction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Restriction"]:
        if not json_data:
            return None
        return cls(
            EndHour=json_data.get("EndHour"),
            EndMin=json_data.get("EndMin"),
            StartHour=json_data.get("StartHour"),
            StartMin=json_data.get("StartMin"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Restriction = Restriction


@dataclass
class Restrictions:
    EndDay: Optional[str]
    EndHour: Optional[float]
    EndMin: Optional[float]
    StartDay: Optional[str]
    StartHour: Optional[float]
    StartMin: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Restrictions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Restrictions"]:
        if not json_data:
            return None
        return cls(
            EndDay=json_data.get("EndDay"),
            EndHour=json_data.get("EndHour"),
            EndMin=json_data.get("EndMin"),
            StartDay=json_data.get("StartDay"),
            StartHour=json_data.get("StartHour"),
            StartMin=json_data.get("StartMin"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Restrictions = Restrictions


