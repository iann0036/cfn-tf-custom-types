# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    CreateOption: Optional[str]
    DiskSizeGb: Optional[float]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    SourceResourceId: Optional[str]
    SourceUri: Optional[str]
    StorageAccountId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    EncryptionSettings: Optional[Sequence["_EncryptionSettings"]]
    Timeouts: Optional["_Timeouts"]
    DiskEncryptionKey: Optional[Sequence["_DiskEncryptionKey"]]
    KeyEncryptionKey: Optional[Sequence["_KeyEncryptionKey"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreateOption=json_data.get("CreateOption"),
            DiskSizeGb=json_data.get("DiskSizeGb"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SourceResourceId=json_data.get("SourceResourceId"),
            SourceUri=json_data.get("SourceUri"),
            StorageAccountId=json_data.get("StorageAccountId"),
            Tags=json_data.get("Tags"),
            EncryptionSettings=json_data.get("EncryptionSettings"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            DiskEncryptionKey=json_data.get("DiskEncryptionKey"),
            KeyEncryptionKey=json_data.get("KeyEncryptionKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class EncryptionSettings:
    Enabled: Optional[bool]
    DiskEncryptionKey: Optional[Sequence["_DiskEncryptionKey"]]
    KeyEncryptionKey: Optional[Sequence["_KeyEncryptionKey"]]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionSettings"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            DiskEncryptionKey=json_data.get("DiskEncryptionKey"),
            KeyEncryptionKey=json_data.get("KeyEncryptionKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionSettings = EncryptionSettings


@dataclass
class DiskEncryptionKey:
    SecretUrl: Optional[str]
    SourceVaultId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskEncryptionKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskEncryptionKey"]:
        if not json_data:
            return None
        return cls(
            SecretUrl=json_data.get("SecretUrl"),
            SourceVaultId=json_data.get("SourceVaultId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskEncryptionKey = DiskEncryptionKey


@dataclass
class KeyEncryptionKey:
    KeyUrl: Optional[str]
    SourceVaultId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyEncryptionKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyEncryptionKey"]:
        if not json_data:
            return None
        return cls(
            KeyUrl=json_data.get("KeyUrl"),
            SourceVaultId=json_data.get("SourceVaultId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyEncryptionKey = KeyEncryptionKey


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


