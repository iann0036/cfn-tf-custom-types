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
    CreateOption: Optional[str]
    DiskAccessId: Optional[str]
    DiskEncryptionSetId: Optional[str]
    DiskIopsReadWrite: Optional[float]
    DiskMbpsReadWrite: Optional[float]
    DiskSizeGb: Optional[float]
    Id: Optional[str]
    ImageReferenceId: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    NetworkAccessPolicy: Optional[str]
    OsType: Optional[str]
    ResourceGroupName: Optional[str]
    SourceResourceId: Optional[str]
    SourceUri: Optional[str]
    StorageAccountId: Optional[str]
    StorageAccountType: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Tier: Optional[str]
    Zones: Optional[Sequence[str]]
    EncryptionSettings: Optional[Sequence["_EncryptionSettingsDefinition"]]
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
            CreateOption=json_data.get("CreateOption"),
            DiskAccessId=json_data.get("DiskAccessId"),
            DiskEncryptionSetId=json_data.get("DiskEncryptionSetId"),
            DiskIopsReadWrite=json_data.get("DiskIopsReadWrite"),
            DiskMbpsReadWrite=json_data.get("DiskMbpsReadWrite"),
            DiskSizeGb=json_data.get("DiskSizeGb"),
            Id=json_data.get("Id"),
            ImageReferenceId=json_data.get("ImageReferenceId"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NetworkAccessPolicy=json_data.get("NetworkAccessPolicy"),
            OsType=json_data.get("OsType"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SourceResourceId=json_data.get("SourceResourceId"),
            SourceUri=json_data.get("SourceUri"),
            StorageAccountId=json_data.get("StorageAccountId"),
            StorageAccountType=json_data.get("StorageAccountType"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Tier=json_data.get("Tier"),
            Zones=json_data.get("Zones"),
            EncryptionSettings=deserialize_list(json_data.get("EncryptionSettings"), EncryptionSettingsDefinition),
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
class EncryptionSettingsDefinition(BaseModel):
    Enabled: Optional[bool]
    DiskEncryptionKey: Optional[Sequence["_DiskEncryptionKeyDefinition"]]
    KeyEncryptionKey: Optional[Sequence["_KeyEncryptionKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            DiskEncryptionKey=deserialize_list(json_data.get("DiskEncryptionKey"), DiskEncryptionKeyDefinition),
            KeyEncryptionKey=deserialize_list(json_data.get("KeyEncryptionKey"), KeyEncryptionKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionSettingsDefinition = EncryptionSettingsDefinition


@dataclass
class DiskEncryptionKeyDefinition(BaseModel):
    SecretUrl: Optional[str]
    SourceVaultId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskEncryptionKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskEncryptionKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            SecretUrl=json_data.get("SecretUrl"),
            SourceVaultId=json_data.get("SourceVaultId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskEncryptionKeyDefinition = DiskEncryptionKeyDefinition


@dataclass
class KeyEncryptionKeyDefinition(BaseModel):
    KeyUrl: Optional[str]
    SourceVaultId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyEncryptionKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyEncryptionKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyUrl=json_data.get("KeyUrl"),
            SourceVaultId=json_data.get("SourceVaultId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyEncryptionKeyDefinition = KeyEncryptionKeyDefinition


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


