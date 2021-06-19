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
    Arn: Optional[str]
    CloudwatchLogGroupArn: Optional[str]
    DestinationLocationArn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    SourceLocationArn: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Excludes: Optional[Sequence["_ExcludesDefinition"]]
    Options: Optional[Sequence["_OptionsDefinition"]]
    Schedule: Optional[Sequence["_ScheduleDefinition"]]
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
            Arn=json_data.get("Arn"),
            CloudwatchLogGroupArn=json_data.get("CloudwatchLogGroupArn"),
            DestinationLocationArn=json_data.get("DestinationLocationArn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SourceLocationArn=json_data.get("SourceLocationArn"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Excludes=deserialize_list(json_data.get("Excludes"), ExcludesDefinition),
            Options=deserialize_list(json_data.get("Options"), OptionsDefinition),
            Schedule=deserialize_list(json_data.get("Schedule"), ScheduleDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class ExcludesDefinition(BaseModel):
    FilterType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExcludesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExcludesDefinition"]:
        if not json_data:
            return None
        return cls(
            FilterType=json_data.get("FilterType"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExcludesDefinition = ExcludesDefinition


@dataclass
class OptionsDefinition(BaseModel):
    Atime: Optional[str]
    BytesPerSecond: Optional[float]
    Gid: Optional[str]
    LogLevel: Optional[str]
    Mtime: Optional[str]
    OverwriteMode: Optional[str]
    PosixPermissions: Optional[str]
    PreserveDeletedFiles: Optional[str]
    PreserveDevices: Optional[str]
    TaskQueueing: Optional[str]
    TransferMode: Optional[str]
    Uid: Optional[str]
    VerifyMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Atime=json_data.get("Atime"),
            BytesPerSecond=json_data.get("BytesPerSecond"),
            Gid=json_data.get("Gid"),
            LogLevel=json_data.get("LogLevel"),
            Mtime=json_data.get("Mtime"),
            OverwriteMode=json_data.get("OverwriteMode"),
            PosixPermissions=json_data.get("PosixPermissions"),
            PreserveDeletedFiles=json_data.get("PreserveDeletedFiles"),
            PreserveDevices=json_data.get("PreserveDevices"),
            TaskQueueing=json_data.get("TaskQueueing"),
            TransferMode=json_data.get("TransferMode"),
            Uid=json_data.get("Uid"),
            VerifyMode=json_data.get("VerifyMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionsDefinition = OptionsDefinition


@dataclass
class ScheduleDefinition(BaseModel):
    ScheduleExpression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            ScheduleExpression=json_data.get("ScheduleExpression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleDefinition = ScheduleDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


