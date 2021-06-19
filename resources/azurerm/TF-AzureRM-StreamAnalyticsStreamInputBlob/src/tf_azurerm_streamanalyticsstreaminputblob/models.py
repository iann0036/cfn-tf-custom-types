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
    DateFormat: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PathPattern: Optional[str]
    ResourceGroupName: Optional[str]
    StorageAccountKey: Optional[str]
    StorageAccountName: Optional[str]
    StorageContainerName: Optional[str]
    StreamAnalyticsJobName: Optional[str]
    TimeFormat: Optional[str]
    Serialization: Optional[Sequence["_SerializationDefinition"]]
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
            DateFormat=json_data.get("DateFormat"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PathPattern=json_data.get("PathPattern"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            StorageAccountKey=json_data.get("StorageAccountKey"),
            StorageAccountName=json_data.get("StorageAccountName"),
            StorageContainerName=json_data.get("StorageContainerName"),
            StreamAnalyticsJobName=json_data.get("StreamAnalyticsJobName"),
            TimeFormat=json_data.get("TimeFormat"),
            Serialization=deserialize_list(json_data.get("Serialization"), SerializationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SerializationDefinition(BaseModel):
    Encoding: Optional[str]
    FieldDelimiter: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SerializationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SerializationDefinition"]:
        if not json_data:
            return None
        return cls(
            Encoding=json_data.get("Encoding"),
            FieldDelimiter=json_data.get("FieldDelimiter"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SerializationDefinition = SerializationDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


