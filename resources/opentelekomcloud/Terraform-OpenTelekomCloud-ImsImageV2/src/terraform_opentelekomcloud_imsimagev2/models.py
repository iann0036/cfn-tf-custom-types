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
    CmkId: Optional[str]
    DataOrigin: Optional[str]
    Description: Optional[str]
    DiskFormat: Optional[str]
    ImageSize: Optional[str]
    ImageUrl: Optional[str]
    InstanceId: Optional[str]
    IsConfig: Optional[bool]
    MaxRam: Optional[float]
    MinDisk: Optional[float]
    MinRam: Optional[float]
    Name: Optional[str]
    OsVersion: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Type: Optional[str]
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
            CmkId=json_data.get("CmkId"),
            DataOrigin=json_data.get("DataOrigin"),
            Description=json_data.get("Description"),
            DiskFormat=json_data.get("DiskFormat"),
            ImageSize=json_data.get("ImageSize"),
            ImageUrl=json_data.get("ImageUrl"),
            InstanceId=json_data.get("InstanceId"),
            IsConfig=json_data.get("IsConfig"),
            MaxRam=json_data.get("MaxRam"),
            MinDisk=json_data.get("MinDisk"),
            MinRam=json_data.get("MinRam"),
            Name=json_data.get("Name"),
            OsVersion=json_data.get("OsVersion"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            Visibility=json_data.get("Visibility"),
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
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


