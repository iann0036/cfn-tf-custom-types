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
    HomeDirectory: Optional[str]
    HomeDirectoryType: Optional[str]
    Id: Optional[str]
    Policy: Optional[str]
    Role: Optional[str]
    ServerId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    UserName: Optional[str]
    HomeDirectoryMappings: Optional[Sequence["_HomeDirectoryMappingsDefinition"]]
    PosixProfile: Optional[Sequence["_PosixProfileDefinition"]]

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
            HomeDirectory=json_data.get("HomeDirectory"),
            HomeDirectoryType=json_data.get("HomeDirectoryType"),
            Id=json_data.get("Id"),
            Policy=json_data.get("Policy"),
            Role=json_data.get("Role"),
            ServerId=json_data.get("ServerId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            UserName=json_data.get("UserName"),
            HomeDirectoryMappings=deserialize_list(json_data.get("HomeDirectoryMappings"), HomeDirectoryMappingsDefinition),
            PosixProfile=deserialize_list(json_data.get("PosixProfile"), PosixProfileDefinition),
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
class HomeDirectoryMappingsDefinition(BaseModel):
    Entry: Optional[str]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HomeDirectoryMappingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HomeDirectoryMappingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Entry=json_data.get("Entry"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HomeDirectoryMappingsDefinition = HomeDirectoryMappingsDefinition


@dataclass
class PosixProfileDefinition(BaseModel):
    Gid: Optional[float]
    SecondaryGids: Optional[Sequence[float]]
    Uid: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PosixProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PosixProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            Gid=json_data.get("Gid"),
            SecondaryGids=json_data.get("SecondaryGids"),
            Uid=json_data.get("Uid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PosixProfileDefinition = PosixProfileDefinition


