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
    ClientList: Optional[Sequence[str]]
    DefaultStorageClass: Optional[str]
    FileShareName: Optional[str]
    FileshareId: Optional[str]
    GatewayArn: Optional[str]
    GuessMimeTypeEnabled: Optional[bool]
    Id: Optional[str]
    KmsEncrypted: Optional[bool]
    KmsKeyArn: Optional[str]
    LocationArn: Optional[str]
    NotificationPolicy: Optional[str]
    ObjectAcl: Optional[str]
    Path: Optional[str]
    ReadOnly: Optional[bool]
    RequesterPays: Optional[bool]
    RoleArn: Optional[str]
    Squash: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    CacheAttributes: Optional[Sequence["_CacheAttributesDefinition"]]
    NfsFileShareDefaults: Optional[Sequence["_NfsFileShareDefaultsDefinition"]]
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
            ClientList=json_data.get("ClientList"),
            DefaultStorageClass=json_data.get("DefaultStorageClass"),
            FileShareName=json_data.get("FileShareName"),
            FileshareId=json_data.get("FileshareId"),
            GatewayArn=json_data.get("GatewayArn"),
            GuessMimeTypeEnabled=json_data.get("GuessMimeTypeEnabled"),
            Id=json_data.get("Id"),
            KmsEncrypted=json_data.get("KmsEncrypted"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            LocationArn=json_data.get("LocationArn"),
            NotificationPolicy=json_data.get("NotificationPolicy"),
            ObjectAcl=json_data.get("ObjectAcl"),
            Path=json_data.get("Path"),
            ReadOnly=json_data.get("ReadOnly"),
            RequesterPays=json_data.get("RequesterPays"),
            RoleArn=json_data.get("RoleArn"),
            Squash=json_data.get("Squash"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            CacheAttributes=deserialize_list(json_data.get("CacheAttributes"), CacheAttributesDefinition),
            NfsFileShareDefaults=deserialize_list(json_data.get("NfsFileShareDefaults"), NfsFileShareDefaultsDefinition),
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
class CacheAttributesDefinition(BaseModel):
    CacheStaleTimeoutInSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CacheAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            CacheStaleTimeoutInSeconds=json_data.get("CacheStaleTimeoutInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheAttributesDefinition = CacheAttributesDefinition


@dataclass
class NfsFileShareDefaultsDefinition(BaseModel):
    DirectoryMode: Optional[str]
    FileMode: Optional[str]
    GroupId: Optional[str]
    OwnerId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NfsFileShareDefaultsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NfsFileShareDefaultsDefinition"]:
        if not json_data:
            return None
        return cls(
            DirectoryMode=json_data.get("DirectoryMode"),
            FileMode=json_data.get("FileMode"),
            GroupId=json_data.get("GroupId"),
            OwnerId=json_data.get("OwnerId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NfsFileShareDefaultsDefinition = NfsFileShareDefaultsDefinition


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


