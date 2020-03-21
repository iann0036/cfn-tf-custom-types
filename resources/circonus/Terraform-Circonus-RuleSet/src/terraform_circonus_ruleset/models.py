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
    Check: Optional[str]
    Link: Optional[str]
    MetricFilter: Optional[str]
    MetricName: Optional[str]
    MetricPattern: Optional[str]
    MetricType: Optional[str]
    Notes: Optional[str]
    Parent: Optional[str]
    RuleSetId: Optional[str]
    Tags: Optional[Sequence[str]]
    If: Optional[Sequence["_If"]]
    Then: Optional[Sequence["_Then"]]
    Value: Optional[Sequence["_Value"]]
    Over: Optional[Sequence["_Over"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Check=json_data.get("Check"),
            Link=json_data.get("Link"),
            MetricFilter=json_data.get("MetricFilter"),
            MetricName=json_data.get("MetricName"),
            MetricPattern=json_data.get("MetricPattern"),
            MetricType=json_data.get("MetricType"),
            Notes=json_data.get("Notes"),
            Parent=json_data.get("Parent"),
            RuleSetId=json_data.get("RuleSetId"),
            Tags=json_data.get("Tags"),
            If=json_data.get("If"),
            Then=json_data.get("Then"),
            Value=json_data.get("Value"),
            Over=json_data.get("Over"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class If:
    Then: Optional[Sequence["_Then"]]
    Value: Optional[Sequence["_Value"]]

    @classmethod
    def _deserialize(
        cls: Type["_If"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_If"]:
        if not json_data:
            return None
        return cls(
            Then=json_data.get("Then"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_If = If


@dataclass
class Then:
    After: Optional[str]
    Notify: Optional[Sequence[str]]
    Severity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Then"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Then"]:
        if not json_data:
            return None
        return cls(
            After=json_data.get("After"),
            Notify=json_data.get("Notify"),
            Severity=json_data.get("Severity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Then = Then


@dataclass
class Value:
    Absent: Optional[str]
    Changed: Optional[str]
    Contains: Optional[str]
    Match: Optional[str]
    MaxValue: Optional[str]
    MinValue: Optional[str]
    NotContain: Optional[str]
    NotMatch: Optional[str]
    Over: Optional[Sequence["_Over"]]

    @classmethod
    def _deserialize(
        cls: Type["_Value"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Value"]:
        if not json_data:
            return None
        return cls(
            Absent=json_data.get("Absent"),
            Changed=json_data.get("Changed"),
            Contains=json_data.get("Contains"),
            Match=json_data.get("Match"),
            MaxValue=json_data.get("MaxValue"),
            MinValue=json_data.get("MinValue"),
            NotContain=json_data.get("NotContain"),
            NotMatch=json_data.get("NotMatch"),
            Over=json_data.get("Over"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Value = Value


@dataclass
class Over:
    Last: Optional[str]
    Using: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Over"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Over"]:
        if not json_data:
            return None
        return cls(
            Last=json_data.get("Last"),
            Using=json_data.get("Using"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Over = Over


