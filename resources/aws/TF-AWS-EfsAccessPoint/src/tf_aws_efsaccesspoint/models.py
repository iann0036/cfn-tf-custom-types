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
    FileSystemArn: Optional[str]
    FileSystemId: Optional[str]
    Id: Optional[str]
    OwnerId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    PosixUser: Optional[Sequence["_PosixUserDefinition"]]
    RootDirectory: Optional[Sequence["_RootDirectoryDefinition"]]

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
            FileSystemArn=json_data.get("FileSystemArn"),
            FileSystemId=json_data.get("FileSystemId"),
            Id=json_data.get("Id"),
            OwnerId=json_data.get("OwnerId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            PosixUser=deserialize_list(json_data.get("PosixUser"), PosixUserDefinition),
            RootDirectory=deserialize_list(json_data.get("RootDirectory"), RootDirectoryDefinition),
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
class PosixUserDefinition(BaseModel):
    Gid: Optional[float]
    SecondaryGids: Optional[Sequence[float]]
    Uid: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PosixUserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PosixUserDefinition"]:
        if not json_data:
            return None
        return cls(
            Gid=json_data.get("Gid"),
            SecondaryGids=json_data.get("SecondaryGids"),
            Uid=json_data.get("Uid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PosixUserDefinition = PosixUserDefinition


@dataclass
class RootDirectoryDefinition(BaseModel):
    Path: Optional[str]
    CreationInfo: Optional[Sequence["_CreationInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RootDirectoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RootDirectoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            CreationInfo=deserialize_list(json_data.get("CreationInfo"), CreationInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RootDirectoryDefinition = RootDirectoryDefinition


@dataclass
class CreationInfoDefinition(BaseModel):
    OwnerGid: Optional[float]
    OwnerUid: Optional[float]
    Permissions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CreationInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreationInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            OwnerGid=json_data.get("OwnerGid"),
            OwnerUid=json_data.get("OwnerUid"),
            Permissions=json_data.get("Permissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreationInfoDefinition = CreationInfoDefinition


