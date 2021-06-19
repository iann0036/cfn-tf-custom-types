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
    Name: Optional[str]
    PolicyDescription: Optional[str]
    Suppress: Optional[bool]
    TeamId: Optional[str]
    AutoCloseAction: Optional[Sequence["_AutoCloseActionDefinition"]]
    AutoRestartAction: Optional[Sequence["_AutoRestartActionDefinition"]]
    DeDuplicationAction: Optional[Sequence["_DeDuplicationActionDefinition"]]
    DelayAction: Optional[Sequence["_DelayActionDefinition"]]
    Filter: Optional[Sequence["_FilterDefinition"]]
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
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PolicyDescription=json_data.get("PolicyDescription"),
            Suppress=json_data.get("Suppress"),
            TeamId=json_data.get("TeamId"),
            AutoCloseAction=deserialize_list(json_data.get("AutoCloseAction"), AutoCloseActionDefinition),
            AutoRestartAction=deserialize_list(json_data.get("AutoRestartAction"), AutoRestartActionDefinition),
            DeDuplicationAction=deserialize_list(json_data.get("DeDuplicationAction"), DeDuplicationActionDefinition),
            DelayAction=deserialize_list(json_data.get("DelayAction"), DelayActionDefinition),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
            TimeRestriction=deserialize_list(json_data.get("TimeRestriction"), TimeRestrictionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutoCloseActionDefinition(BaseModel):
    Duration: Optional[Sequence["_DurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoCloseActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoCloseActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=deserialize_list(json_data.get("Duration"), DurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoCloseActionDefinition = AutoCloseActionDefinition


@dataclass
class DurationDefinition(BaseModel):
    TimeAmount: Optional[float]
    TimeUnit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DurationDefinition"]:
        if not json_data:
            return None
        return cls(
            TimeAmount=json_data.get("TimeAmount"),
            TimeUnit=json_data.get("TimeUnit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DurationDefinition = DurationDefinition


@dataclass
class AutoRestartActionDefinition(BaseModel):
    MaxRepeatCount: Optional[float]
    Duration: Optional[Sequence["_DurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoRestartActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoRestartActionDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxRepeatCount=json_data.get("MaxRepeatCount"),
            Duration=deserialize_list(json_data.get("Duration"), DurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoRestartActionDefinition = AutoRestartActionDefinition


@dataclass
class DeDuplicationActionDefinition(BaseModel):
    Count: Optional[float]
    DeDuplicationActionType: Optional[str]
    Duration: Optional[Sequence["_DurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DeDuplicationActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeDuplicationActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            DeDuplicationActionType=json_data.get("DeDuplicationActionType"),
            Duration=deserialize_list(json_data.get("Duration"), DurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeDuplicationActionDefinition = DeDuplicationActionDefinition


@dataclass
class DelayActionDefinition(BaseModel):
    DelayOption: Optional[str]
    UntilHour: Optional[float]
    UntilMinute: Optional[float]
    Duration: Optional[Sequence["_DurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DelayActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DelayActionDefinition"]:
        if not json_data:
            return None
        return cls(
            DelayOption=json_data.get("DelayOption"),
            UntilHour=json_data.get("UntilHour"),
            UntilMinute=json_data.get("UntilMinute"),
            Duration=deserialize_list(json_data.get("Duration"), DurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DelayActionDefinition = DelayActionDefinition


@dataclass
class FilterDefinition(BaseModel):
    Type: Optional[str]
    Conditions: Optional[Sequence["_ConditionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Conditions=deserialize_list(json_data.get("Conditions"), ConditionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


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


