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
    Checksum: Optional[str]
    ContainerFormat: Optional[str]
    CreatedAt: Optional[str]
    DiskFormat: Optional[str]
    File: Optional[str]
    Id: Optional[str]
    ImageCachePath: Optional[str]
    ImageSourceUrl: Optional[str]
    LocalFilePath: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    MinDiskGb: Optional[float]
    MinRamMb: Optional[float]
    Name: Optional[str]
    Owner: Optional[str]
    Properties: Optional[Sequence["_Properties"]]
    Protected: Optional[bool]
    Region: Optional[str]
    Schema: Optional[str]
    SizeBytes: Optional[float]
    Status: Optional[str]
    Tags: Optional[Sequence[str]]
    UpdateAt: Optional[str]
    UpdatedAt: Optional[str]
    VerifyChecksum: Optional[bool]
    Visibility: Optional[str]
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
            Checksum=json_data.get("Checksum"),
            ContainerFormat=json_data.get("ContainerFormat"),
            CreatedAt=json_data.get("CreatedAt"),
            DiskFormat=json_data.get("DiskFormat"),
            File=json_data.get("File"),
            Id=json_data.get("Id"),
            ImageCachePath=json_data.get("ImageCachePath"),
            ImageSourceUrl=json_data.get("ImageSourceUrl"),
            LocalFilePath=json_data.get("LocalFilePath"),
            Metadata=json_data.get("Metadata"),
            MinDiskGb=json_data.get("MinDiskGb"),
            MinRamMb=json_data.get("MinRamMb"),
            Name=json_data.get("Name"),
            Owner=json_data.get("Owner"),
            Properties=json_data.get("Properties"),
            Protected=json_data.get("Protected"),
            Region=json_data.get("Region"),
            Schema=json_data.get("Schema"),
            SizeBytes=json_data.get("SizeBytes"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            UpdateAt=json_data.get("UpdateAt"),
            UpdatedAt=json_data.get("UpdatedAt"),
            VerifyChecksum=json_data.get("VerifyChecksum"),
            Visibility=json_data.get("Visibility"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
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


@dataclass
class Properties:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Properties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Properties"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Properties = Properties


@dataclass
class Timeouts:
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


