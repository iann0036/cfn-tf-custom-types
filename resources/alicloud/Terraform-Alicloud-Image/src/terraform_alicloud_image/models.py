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
    Architecture: Optional[str]
    Description: Optional[str]
    Force: Optional[bool]
    ImageName: Optional[str]
    InstanceId: Optional[str]
    Name: Optional[str]
    Platform: Optional[str]
    ResourceGroupId: Optional[str]
    SnapshotId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    DiskDeviceMapping: Optional[Sequence["_DiskDeviceMapping"]]
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
            Architecture=json_data.get("Architecture"),
            Description=json_data.get("Description"),
            Force=json_data.get("Force"),
            ImageName=json_data.get("ImageName"),
            InstanceId=json_data.get("InstanceId"),
            Name=json_data.get("Name"),
            Platform=json_data.get("Platform"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            SnapshotId=json_data.get("SnapshotId"),
            Tags=json_data.get("Tags"),
            DiskDeviceMapping=json_data.get("DiskDeviceMapping"),
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
class DiskDeviceMapping:
    Device: Optional[str]
    DiskType: Optional[str]
    Size: Optional[float]
    SnapshotId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskDeviceMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskDeviceMapping"]:
        if not json_data:
            return None
        return cls(
            Device=json_data.get("Device"),
            DiskType=json_data.get("DiskType"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskDeviceMapping = DiskDeviceMapping


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


