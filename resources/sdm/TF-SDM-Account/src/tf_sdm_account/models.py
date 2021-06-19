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
    Service: Optional[Sequence["_ServiceDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    User: Optional[Sequence["_UserDefinition"]]

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
            Service=deserialize_list(json_data.get("Service"), ServiceDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            User=deserialize_list(json_data.get("User"), UserDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ServiceDefinition(BaseModel):
    Name: Optional[str]
    Suspended: Optional[bool]
    Tags: Optional[Sequence["_TagsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Suspended=json_data.get("Suspended"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceDefinition = ServiceDefinition


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
class TimeoutsDefinition(BaseModel):
    Default: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class UserDefinition(BaseModel):
    Email: Optional[str]
    FirstName: Optional[str]
    LastName: Optional[str]
    Suspended: Optional[bool]
    Tags: Optional[Sequence["_TagsDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_UserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserDefinition"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            FirstName=json_data.get("FirstName"),
            LastName=json_data.get("LastName"),
            Suspended=json_data.get("Suspended"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserDefinition = UserDefinition


@dataclass
class TagsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition2 = TagsDefinition2


