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
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Service: Optional[Sequence["_ServiceDefinition"]]
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
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Service=deserialize_list(json_data.get("Service"), ServiceDefinition),
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
class ServiceDefinition(BaseModel):
    Name: Optional[str]
    OsType: Optional[str]
    CodePackage: Optional[Sequence["_CodePackageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            OsType=json_data.get("OsType"),
            CodePackage=deserialize_list(json_data.get("CodePackage"), CodePackageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceDefinition = ServiceDefinition


@dataclass
class CodePackageDefinition(BaseModel):
    ImageName: Optional[str]
    Name: Optional[str]
    Resources: Optional[Sequence["_ResourcesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CodePackageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CodePackageDefinition"]:
        if not json_data:
            return None
        return cls(
            ImageName=json_data.get("ImageName"),
            Name=json_data.get("Name"),
            Resources=deserialize_list(json_data.get("Resources"), ResourcesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CodePackageDefinition = CodePackageDefinition


@dataclass
class ResourcesDefinition(BaseModel):
    Limits: Optional[Sequence["_LimitsDefinition"]]
    Requests: Optional[Sequence["_RequestsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            Limits=deserialize_list(json_data.get("Limits"), LimitsDefinition),
            Requests=deserialize_list(json_data.get("Requests"), RequestsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcesDefinition = ResourcesDefinition


@dataclass
class LimitsDefinition(BaseModel):
    Cpu: Optional[float]
    Memory: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            Cpu=json_data.get("Cpu"),
            Memory=json_data.get("Memory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LimitsDefinition = LimitsDefinition


@dataclass
class RequestsDefinition(BaseModel):
    Cpu: Optional[float]
    Memory: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RequestsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestsDefinition"]:
        if not json_data:
            return None
        return cls(
            Cpu=json_data.get("Cpu"),
            Memory=json_data.get("Memory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestsDefinition = RequestsDefinition


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


