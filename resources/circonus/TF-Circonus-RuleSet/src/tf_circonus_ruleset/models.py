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
    Check: Optional[str]
    Id: Optional[str]
    Link: Optional[str]
    MetricFilter: Optional[str]
    MetricName: Optional[str]
    MetricPattern: Optional[str]
    MetricType: Optional[str]
    Name: Optional[str]
    Notes: Optional[str]
    Parent: Optional[str]
    RuleSetId: Optional[str]
    Tags: Optional[Sequence[str]]
    UserJson: Optional[str]
    If: Optional[Sequence["_IfDefinition"]]

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
            Check=json_data.get("Check"),
            Id=json_data.get("Id"),
            Link=json_data.get("Link"),
            MetricFilter=json_data.get("MetricFilter"),
            MetricName=json_data.get("MetricName"),
            MetricPattern=json_data.get("MetricPattern"),
            MetricType=json_data.get("MetricType"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Parent=json_data.get("Parent"),
            RuleSetId=json_data.get("RuleSetId"),
            Tags=json_data.get("Tags"),
            UserJson=json_data.get("UserJson"),
            If=deserialize_list(json_data.get("If"), IfDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IfDefinition(BaseModel):
    Then: Optional[Sequence["_ThenDefinition"]]
    Value: Optional[Sequence["_ValueDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IfDefinition"]:
        if not json_data:
            return None
        return cls(
            Then=deserialize_list(json_data.get("Then"), ThenDefinition),
            Value=deserialize_list(json_data.get("Value"), ValueDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IfDefinition = IfDefinition


@dataclass
class ThenDefinition(BaseModel):
    After: Optional[str]
    Notify: Optional[Sequence[str]]
    Severity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ThenDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThenDefinition"]:
        if not json_data:
            return None
        return cls(
            After=json_data.get("After"),
            Notify=json_data.get("Notify"),
            Severity=json_data.get("Severity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThenDefinition = ThenDefinition


@dataclass
class ValueDefinition(BaseModel):
    Absent: Optional[str]
    Changed: Optional[str]
    Contains: Optional[str]
    EqValue: Optional[str]
    Match: Optional[str]
    MaxValue: Optional[str]
    MinValue: Optional[str]
    NeqValue: Optional[str]
    NotContain: Optional[str]
    NotMatch: Optional[str]
    Over: Optional[Sequence["_OverDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ValueDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueDefinition"]:
        if not json_data:
            return None
        return cls(
            Absent=json_data.get("Absent"),
            Changed=json_data.get("Changed"),
            Contains=json_data.get("Contains"),
            EqValue=json_data.get("EqValue"),
            Match=json_data.get("Match"),
            MaxValue=json_data.get("MaxValue"),
            MinValue=json_data.get("MinValue"),
            NeqValue=json_data.get("NeqValue"),
            NotContain=json_data.get("NotContain"),
            NotMatch=json_data.get("NotMatch"),
            Over=deserialize_list(json_data.get("Over"), OverDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueDefinition = ValueDefinition


@dataclass
class OverDefinition(BaseModel):
    Atleast: Optional[str]
    Last: Optional[str]
    Using: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OverDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverDefinition"]:
        if not json_data:
            return None
        return cls(
            Atleast=json_data.get("Atleast"),
            Last=json_data.get("Last"),
            Using=json_data.get("Using"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverDefinition = OverDefinition


