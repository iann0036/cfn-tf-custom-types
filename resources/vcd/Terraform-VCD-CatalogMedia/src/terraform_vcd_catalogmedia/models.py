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
    Catalog: Optional[str]
    CreationDate: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IsIso: Optional[bool]
    IsPublished: Optional[bool]
    MediaPath: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    Org: Optional[str]
    OwnerName: Optional[str]
    ShowUploadProgress: Optional[bool]
    Size: Optional[float]
    Status: Optional[str]
    StorageProfileName: Optional[str]
    UploadPieceSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Catalog=json_data.get("Catalog"),
            CreationDate=json_data.get("CreationDate"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IsIso=json_data.get("IsIso"),
            IsPublished=json_data.get("IsPublished"),
            MediaPath=json_data.get("MediaPath"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            OwnerName=json_data.get("OwnerName"),
            ShowUploadProgress=json_data.get("ShowUploadProgress"),
            Size=json_data.get("Size"),
            Status=json_data.get("Status"),
            StorageProfileName=json_data.get("StorageProfileName"),
            UploadPieceSize=json_data.get("UploadPieceSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Metadata:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


