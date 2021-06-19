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
    Id: Optional[str]
    Name: Optional[str]
    Order: Optional[float]
    TeamId: Optional[str]
    Timezone: Optional[str]
    Criteria: Optional[Sequence["_CriteriaDefinition"]]
    Notify: Optional[Sequence["_NotifyDefinition"]]
    TimeRestriction: Optional[Sequence["_TimeRestrictionDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Order=json_data.get("Order"),
            TeamId=json_data.get("TeamId"),
            Timezone=json_data.get("Timezone"),
            Criteria=deserialize_list(json_data.get("Criteria"), CriteriaDefinition),
            Notify=deserialize_list(json_data.get("Notify"), NotifyDefinition),
            TimeRestriction=deserialize_list(json_data.get("TimeRestriction"), TimeRestrictionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CriteriaDefinition(BaseModel):
    Type: Optional[str]
    Conditions: Optional[Sequence["_ConditionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Conditions=deserialize_list(json_data.get("Conditions"), ConditionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CriteriaDefinition = CriteriaDefinition


@dataclass
class ConditionsDefinition(BaseModel):
    ExpectedValue: Optional[str]
    Field: Optional[str]
    Key: Optional[str]
    Not: Optional[bool]
    Operation: Optional[str]
    Order: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionsDefinition"]:
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
_ConditionsDefinition = ConditionsDefinition


@dataclass
class NotifyDefinition(BaseModel):
    Id: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotifyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotifyDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotifyDefinition = NotifyDefinition


@dataclass
class TimeRestrictionDefinition(BaseModel):
    Type: Optional[str]
    Restriction: Optional[Sequence["_RestrictionDefinition"]]
    Restrictions: Optional[Sequence["_RestrictionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TimeRestrictionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeRestrictionDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Restriction=deserialize_list(json_data.get("Restriction"), RestrictionDefinition),
            Restrictions=deserialize_list(json_data.get("Restrictions"), RestrictionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeRestrictionDefinition = TimeRestrictionDefinition


@dataclass
class RestrictionDefinition(BaseModel):
    EndHour: Optional[float]
    EndMin: Optional[float]
    StartHour: Optional[float]
    StartMin: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RestrictionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestrictionDefinition"]:
        if not json_data:
            return None
        return cls(
            EndHour=json_data.get("EndHour"),
            EndMin=json_data.get("EndMin"),
            StartHour=json_data.get("StartHour"),
            StartMin=json_data.get("StartMin"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestrictionDefinition = RestrictionDefinition


@dataclass
class RestrictionsDefinition(BaseModel):
    EndDay: Optional[str]
    EndHour: Optional[float]
    EndMin: Optional[float]
    StartDay: Optional[str]
    StartHour: Optional[float]
    StartMin: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RestrictionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestrictionsDefinition"]:
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
_RestrictionsDefinition = RestrictionsDefinition


