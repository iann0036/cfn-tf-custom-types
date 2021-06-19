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
    CloudType: Optional[str]
    ConfigData: Optional[Sequence["_ConfigDataDefinition"]]
    Description: Optional[str]
    EventData: Optional[Sequence["_EventDataDefinition"]]
    GroupBy: Optional[Sequence[str]]
    Id: Optional[str]
    Limit: Optional[float]
    Name: Optional[str]
    Query: Optional[str]
    SearchId: Optional[str]
    SearchType: Optional[str]
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
            CloudType=json_data.get("CloudType"),
            ConfigData=deserialize_list(json_data.get("ConfigData"), ConfigDataDefinition),
            Description=json_data.get("Description"),
            EventData=deserialize_list(json_data.get("EventData"), EventDataDefinition),
            GroupBy=json_data.get("GroupBy"),
            Id=json_data.get("Id"),
            Limit=json_data.get("Limit"),
            Name=json_data.get("Name"),
            Query=json_data.get("Query"),
            SearchId=json_data.get("SearchId"),
            SearchType=json_data.get("SearchType"),
            TimeRange=deserialize_list(json_data.get("TimeRange"), TimeRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConfigDataDefinition(BaseModel):
    Name: Optional[str]
    StateId: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDataDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            StateId=json_data.get("StateId"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDataDefinition = ConfigDataDefinition


@dataclass
class EventDataDefinition(BaseModel):
    Account: Optional[str]
    RegionApiIdentifier: Optional[str]
    RegionId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EventDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventDataDefinition"]:
        if not json_data:
            return None
        return cls(
            Account=json_data.get("Account"),
            RegionApiIdentifier=json_data.get("RegionApiIdentifier"),
            RegionId=json_data.get("RegionId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventDataDefinition = EventDataDefinition


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


