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
    ExcludeFromLatest: Optional[bool]
    GalleryName: Optional[str]
    Id: Optional[str]
    ImageName: Optional[str]
    Location: Optional[str]
    ManagedImageId: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TargetRegion: Optional[Sequence["_TargetRegion"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ExcludeFromLatest=json_data.get("ExcludeFromLatest"),
            GalleryName=json_data.get("GalleryName"),
            Id=json_data.get("Id"),
            ImageName=json_data.get("ImageName"),
            Location=json_data.get("Location"),
            ManagedImageId=json_data.get("ManagedImageId"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=json_data.get("Tags"),
            TargetRegion=json_data.get("TargetRegion"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
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


@dataclass
class TargetRegion:
    Name: Optional[str]
    RegionalReplicaCount: Optional[float]
    StorageAccountType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetRegion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetRegion"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            RegionalReplicaCount=json_data.get("RegionalReplicaCount"),
            StorageAccountType=json_data.get("StorageAccountType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetRegion = TargetRegion


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


