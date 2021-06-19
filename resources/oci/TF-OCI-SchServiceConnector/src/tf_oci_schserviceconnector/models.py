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
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    Description: Optional[str]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    LifecyleDetails: Optional[str]
    State: Optional[str]
    SystemTags: Optional[Sequence["_SystemTagsDefinition"]]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    Source: Optional[Sequence["_SourceDefinition"]]
    Target: Optional[Sequence["_TargetDefinition"]]
    Tasks: Optional[Sequence["_TasksDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            LifecyleDetails=json_data.get("LifecyleDetails"),
            State=json_data.get("State"),
            SystemTags=deserialize_list(json_data.get("SystemTags"), SystemTagsDefinition),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
            Target=deserialize_list(json_data.get("Target"), TargetDefinition),
            Tasks=deserialize_list(json_data.get("Tasks"), TasksDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class SystemTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemTagsDefinition = SystemTagsDefinition


@dataclass
class SourceDefinition(BaseModel):
    Kind: Optional[str]
    StreamId: Optional[str]
    Cursor: Optional[Sequence["_CursorDefinition"]]
    LogSources: Optional[Sequence["_LogSourcesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            StreamId=json_data.get("StreamId"),
            Cursor=deserialize_list(json_data.get("Cursor"), CursorDefinition),
            LogSources=deserialize_list(json_data.get("LogSources"), LogSourcesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


@dataclass
class CursorDefinition(BaseModel):
    Kind: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CursorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CursorDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CursorDefinition = CursorDefinition


@dataclass
class LogSourcesDefinition(BaseModel):
    CompartmentId: Optional[str]
    LogGroupId: Optional[str]
    LogId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogSourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogSourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            CompartmentId=json_data.get("CompartmentId"),
            LogGroupId=json_data.get("LogGroupId"),
            LogId=json_data.get("LogId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogSourcesDefinition = LogSourcesDefinition


@dataclass
class TargetDefinition(BaseModel):
    BatchRolloverSizeInMbs: Optional[float]
    BatchRolloverTimeInMs: Optional[float]
    Bucket: Optional[str]
    CompartmentId: Optional[str]
    EnableFormattedMessaging: Optional[bool]
    FunctionId: Optional[str]
    Kind: Optional[str]
    LogGroupId: Optional[str]
    Metric: Optional[str]
    MetricNamespace: Optional[str]
    Namespace: Optional[str]
    ObjectNamePrefix: Optional[str]
    StreamId: Optional[str]
    TopicId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetDefinition"]:
        if not json_data:
            return None
        return cls(
            BatchRolloverSizeInMbs=json_data.get("BatchRolloverSizeInMbs"),
            BatchRolloverTimeInMs=json_data.get("BatchRolloverTimeInMs"),
            Bucket=json_data.get("Bucket"),
            CompartmentId=json_data.get("CompartmentId"),
            EnableFormattedMessaging=json_data.get("EnableFormattedMessaging"),
            FunctionId=json_data.get("FunctionId"),
            Kind=json_data.get("Kind"),
            LogGroupId=json_data.get("LogGroupId"),
            Metric=json_data.get("Metric"),
            MetricNamespace=json_data.get("MetricNamespace"),
            Namespace=json_data.get("Namespace"),
            ObjectNamePrefix=json_data.get("ObjectNamePrefix"),
            StreamId=json_data.get("StreamId"),
            TopicId=json_data.get("TopicId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetDefinition = TargetDefinition


@dataclass
class TasksDefinition(BaseModel):
    BatchSizeInKbs: Optional[float]
    BatchTimeInSec: Optional[float]
    Condition: Optional[str]
    FunctionId: Optional[str]
    Kind: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TasksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TasksDefinition"]:
        if not json_data:
            return None
        return cls(
            BatchSizeInKbs=json_data.get("BatchSizeInKbs"),
            BatchTimeInSec=json_data.get("BatchTimeInSec"),
            Condition=json_data.get("Condition"),
            FunctionId=json_data.get("FunctionId"),
            Kind=json_data.get("Kind"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TasksDefinition = TasksDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


