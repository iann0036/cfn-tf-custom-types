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
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    PolicyDescription: Optional[str]
    Suppress: Optional[bool]
    TeamId: Optional[str]
    AutoCloseAction: Optional[Sequence["_AutoCloseAction"]]
    AutoRestartAction: Optional[Sequence["_AutoRestartAction"]]
    DeDuplicationAction: Optional[Sequence["_DeDuplicationAction"]]
    DelayAction: Optional[Sequence["_DelayAction"]]
    Filter: Optional[Sequence["_Filter"]]
    TimeRestriction: Optional[Sequence["_TimeRestriction"]]
    Duration: Optional[Sequence["_Duration"]]
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
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PolicyDescription=json_data.get("PolicyDescription"),
            Suppress=json_data.get("Suppress"),
            TeamId=json_data.get("TeamId"),
            AutoCloseAction=json_data.get("AutoCloseAction"),
            AutoRestartAction=json_data.get("AutoRestartAction"),
            DeDuplicationAction=json_data.get("DeDuplicationAction"),
            DelayAction=json_data.get("DelayAction"),
            Filter=json_data.get("Filter"),
            TimeRestriction=json_data.get("TimeRestriction"),
            Duration=json_data.get("Duration"),
            Conditions=json_data.get("Conditions"),
            Restriction=json_data.get("Restriction"),
            Restrictions=json_data.get("Restrictions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutoCloseAction:
    Duration: Optional[Sequence["_Duration"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoCloseAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoCloseAction"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoCloseAction = AutoCloseAction


@dataclass
class Duration:
    TimeAmount: Optional[float]
    TimeUnit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Duration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Duration"]:
        if not json_data:
            return None
        return cls(
            TimeAmount=json_data.get("TimeAmount"),
            TimeUnit=json_data.get("TimeUnit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Duration = Duration


@dataclass
class AutoRestartAction:
    MaxRepeatCount: Optional[float]
    Duration: Optional[Sequence["_Duration"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoRestartAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoRestartAction"]:
        if not json_data:
            return None
        return cls(
            MaxRepeatCount=json_data.get("MaxRepeatCount"),
            Duration=json_data.get("Duration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoRestartAction = AutoRestartAction


@dataclass
class DeDuplicationAction:
    Count: Optional[float]
    DeDuplicationActionType: Optional[str]
    Duration: Optional[Sequence["_Duration"]]

    @classmethod
    def _deserialize(
        cls: Type["_DeDuplicationAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeDuplicationAction"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            DeDuplicationActionType=json_data.get("DeDuplicationActionType"),
            Duration=json_data.get("Duration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeDuplicationAction = DeDuplicationAction


@dataclass
class DelayAction:
    DelayOption: Optional[str]
    UntilHour: Optional[float]
    UntilMinute: Optional[float]
    Duration: Optional[Sequence["_Duration"]]

    @classmethod
    def _deserialize(
        cls: Type["_DelayAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DelayAction"]:
        if not json_data:
            return None
        return cls(
            DelayOption=json_data.get("DelayOption"),
            UntilHour=json_data.get("UntilHour"),
            UntilMinute=json_data.get("UntilMinute"),
            Duration=json_data.get("Duration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DelayAction = DelayAction


@dataclass
class Filter:
    Type: Optional[str]
    Conditions: Optional[Sequence["_Conditions"]]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Conditions=json_data.get("Conditions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


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


