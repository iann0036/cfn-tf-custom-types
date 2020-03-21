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
    Id: Optional[str]
    Name: Optional[str]
    Order: Optional[float]
    TeamId: Optional[str]
    Timezone: Optional[str]
    Criteria: Optional[Sequence["_Criteria"]]
    Notify: Optional[Sequence["_Notify"]]
    TimeRestriction: Optional[Sequence["_TimeRestriction"]]
    Conditions: Optional[Sequence["_Conditions"]]
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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Order=json_data.get("Order"),
            TeamId=json_data.get("TeamId"),
            Timezone=json_data.get("Timezone"),
            Criteria=json_data.get("Criteria"),
            Notify=json_data.get("Notify"),
            TimeRestriction=json_data.get("TimeRestriction"),
            Conditions=json_data.get("Conditions"),
            Restriction=json_data.get("Restriction"),
            Restrictions=json_data.get("Restrictions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Criteria:
    Type: Optional[str]
    Conditions: Optional[Sequence["_Conditions"]]

    @classmethod
    def _deserialize(
        cls: Type["_Criteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Criteria"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Conditions=json_data.get("Conditions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Criteria = Criteria


@dataclass
class Conditions:
    ExpectedValue: Optional[str]
    Field: Optional[str]
    Key: Optional[str]
    Not: Optional[bool]
    Operation: Optional[str]
    Order: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Conditions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Conditions"]:
        if not json_data:
            return None
        return cls(
            ExpectedValue=json_data.get("ExpectedValue"),
            Field=json_data.get("Field"),
            Key=json_data.get("Key"),
            Not=json_data.get("Not"),
            Operation=json_data.get("Operation"),
            Order=json_data.get("Order"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Conditions = Conditions


@dataclass
class Notify:
    Id: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Notify"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Notify"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Notify = Notify


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


