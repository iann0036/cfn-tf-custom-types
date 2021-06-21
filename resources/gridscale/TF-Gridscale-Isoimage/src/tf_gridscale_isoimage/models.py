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
    Capacity: Optional[float]
    ChangeTime: Optional[str]
    CreateTime: Optional[str]
    CurrentPrice: Optional[float]
    Description: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence[str]]
    LocationCountry: Optional[str]
    LocationIata: Optional[str]
    LocationName: Optional[str]
    LocationUuid: Optional[str]
    Name: Optional[str]
    Private: Optional[bool]
    Server: Optional[Sequence["_ServerDefinition"]]
    SourceUrl: Optional[str]
    Status: Optional[str]
    UsageInMinutes: Optional[float]
    Version: Optional[str]
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
            Capacity=json_data.get("Capacity"),
            ChangeTime=json_data.get("ChangeTime"),
            CreateTime=json_data.get("CreateTime"),
            CurrentPrice=json_data.get("CurrentPrice"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            LocationCountry=json_data.get("LocationCountry"),
            LocationIata=json_data.get("LocationIata"),
            LocationName=json_data.get("LocationName"),
            LocationUuid=json_data.get("LocationUuid"),
            Name=json_data.get("Name"),
            Private=json_data.get("Private"),
            Server=deserialize_list(json_data.get("Server"), ServerDefinition),
            SourceUrl=json_data.get("SourceUrl"),
            Status=json_data.get("Status"),
            UsageInMinutes=json_data.get("UsageInMinutes"),
            Version=json_data.get("Version"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ServerDefinition(BaseModel):
    Bootdevice: Optional[bool]
    CreateTime: Optional[str]
    ObjectName: Optional[str]
    ObjectUuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerDefinition"]:
        if not json_data:
            return None
        return cls(
            Bootdevice=json_data.get("Bootdevice"),
            CreateTime=json_data.get("CreateTime"),
            ObjectName=json_data.get("ObjectName"),
            ObjectUuid=json_data.get("ObjectUuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerDefinition = ServerDefinition


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

