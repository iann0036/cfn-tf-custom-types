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
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Query: Optional[str]
    Saved: Optional[bool]
    SearchId: Optional[str]
    TimeRange: Optional[Sequence["_TimeRangeDefinition"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Query=json_data.get("Query"),
            Saved=json_data.get("Saved"),
            SearchId=json_data.get("SearchId"),
            TimeRange=deserialize_list(json_data.get("TimeRange"), TimeRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeRangeDefinition(BaseModel):
    Absolute: Optional[Sequence["_AbsoluteDefinition"]]
    Relative: Optional[Sequence["_RelativeDefinition"]]
    ToNow: Optional[Sequence["_ToNowDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TimeRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Absolute=deserialize_list(json_data.get("Absolute"), AbsoluteDefinition),
            Relative=deserialize_list(json_data.get("Relative"), RelativeDefinition),
            ToNow=deserialize_list(json_data.get("ToNow"), ToNowDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeRangeDefinition = TimeRangeDefinition


@dataclass
class AbsoluteDefinition(BaseModel):
    End: Optional[float]
    Start: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AbsoluteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AbsoluteDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AbsoluteDefinition = AbsoluteDefinition


@dataclass
class RelativeDefinition(BaseModel):
    Amount: Optional[float]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelativeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelativeDefinition"]:
        if not json_data:
            return None
        return cls(
            Amount=json_data.get("Amount"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelativeDefinition = RelativeDefinition


@dataclass
class ToNowDefinition(BaseModel):
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ToNowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ToNowDefinition"]:
        if not json_data:
            return None
        return cls(
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ToNowDefinition = ToNowDefinition


