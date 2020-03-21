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
    DataEncryptionKeyId: Optional[str]
    Description: Optional[str]
    Encrypted: Optional[bool]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    OwnerAlias: Optional[str]
    OwnerId: Optional[str]
    SourceRegion: Optional[str]
    SourceSnapshotId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VolumeId: Optional[str]
    VolumeSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DataEncryptionKeyId=json_data.get("DataEncryptionKeyId"),
            Description=json_data.get("Description"),
            Encrypted=json_data.get("Encrypted"),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            OwnerAlias=json_data.get("OwnerAlias"),
            OwnerId=json_data.get("OwnerId"),
            SourceRegion=json_data.get("SourceRegion"),
            SourceSnapshotId=json_data.get("SourceSnapshotId"),
            Tags=json_data.get("Tags"),
            VolumeId=json_data.get("VolumeId"),
            VolumeSize=json_data.get("VolumeSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


