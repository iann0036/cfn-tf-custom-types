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
    ActionType: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    NotificationTime: Optional[Sequence[str]]
    Order: Optional[float]
    Username: Optional[str]
    Criteria: Optional[Sequence["_CriteriaDefinition"]]
    Repeat: Optional[Sequence["_RepeatDefinition"]]
    Schedules: Optional[Sequence["_SchedulesDefinition"]]
    Steps: Optional[Sequence["_StepsDefinition"]]
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
            ActionType=json_data.get("ActionType"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NotificationTime=json_data.get("NotificationTime"),
            Order=json_data.get("Order"),
            Username=json_data.get("Username"),
            Criteria=deserialize_list(json_data.get("Criteria"), CriteriaDefinition),
            Repeat=deserialize_list(json_data.get("Repeat"), RepeatDefinition),
            Schedules=deserialize_list(json_data.get("Schedules"), SchedulesDefinition),
            Steps=deserialize_list(json_data.get("Steps"), StepsDefinition),
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
class RepeatDefinition(BaseModel):
    Enabled: Optional[bool]
    LoopAfter: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RepeatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RepeatDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            LoopAfter=json_data.get("LoopAfter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RepeatDefinition = RepeatDefinition


@dataclass
class SchedulesDefinition(BaseModel):
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchedulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchedulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchedulesDefinition = SchedulesDefinition


@dataclass
class StepsDefinition(BaseModel):
    Enabled: Optional[bool]
    SendAfter: Optional[float]
    Contact: Optional[Sequence["_ContactDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StepsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            SendAfter=json_data.get("SendAfter"),
            Contact=deserialize_list(json_data.get("Contact"), ContactDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepsDefinition = StepsDefinition


@dataclass
class ContactDefinition(BaseModel):
    Method: Optional[str]
    To: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContactDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContactDefinition"]:
        if not json_data:
            return None
        return cls(
            Method=json_data.get("Method"),
            To=json_data.get("To"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContactDefinition = ContactDefinition


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


