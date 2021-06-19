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
    IncludeTags: Optional[bool]
    Name: Optional[str]
    Query: Optional[str]
    RehydrationTags: Optional[Sequence[str]]
    AzureArchive: Optional[Sequence["_AzureArchiveDefinition"]]
    GcsArchive: Optional[Sequence["_GcsArchiveDefinition"]]
    S3Archive: Optional[Sequence["_S3ArchiveDefinition"]]

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
            IncludeTags=json_data.get("IncludeTags"),
            Name=json_data.get("Name"),
            Query=json_data.get("Query"),
            RehydrationTags=json_data.get("RehydrationTags"),
            AzureArchive=deserialize_list(json_data.get("AzureArchive"), AzureArchiveDefinition),
            GcsArchive=deserialize_list(json_data.get("GcsArchive"), GcsArchiveDefinition),
            S3Archive=deserialize_list(json_data.get("S3Archive"), S3ArchiveDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AzureArchiveDefinition(BaseModel):
    ClientId: Optional[str]
    Container: Optional[str]
    Path: Optional[str]
    StorageAccount: Optional[str]
    TenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureArchiveDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureArchiveDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            Container=json_data.get("Container"),
            Path=json_data.get("Path"),
            StorageAccount=json_data.get("StorageAccount"),
            TenantId=json_data.get("TenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureArchiveDefinition = AzureArchiveDefinition


@dataclass
class GcsArchiveDefinition(BaseModel):
    Bucket: Optional[str]
    ClientEmail: Optional[str]
    Path: Optional[str]
    ProjectId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GcsArchiveDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcsArchiveDefinition"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            ClientEmail=json_data.get("ClientEmail"),
            Path=json_data.get("Path"),
            ProjectId=json_data.get("ProjectId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcsArchiveDefinition = GcsArchiveDefinition


@dataclass
class S3ArchiveDefinition(BaseModel):
    AccountId: Optional[str]
    Bucket: Optional[str]
    Path: Optional[str]
    RoleName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3ArchiveDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3ArchiveDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            Bucket=json_data.get("Bucket"),
            Path=json_data.get("Path"),
            RoleName=json_data.get("RoleName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3ArchiveDefinition = S3ArchiveDefinition


