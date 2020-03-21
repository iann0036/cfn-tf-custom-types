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
    Attachment: Optional[Sequence["_Attachment"]]
    AvailabilityZone: Optional[str]
    BackupId: Optional[str]
    Cascade: Optional[bool]
    Description: Optional[str]
    DeviceType: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    KmsId: Optional[str]
    Multiattach: Optional[bool]
    Name: Optional[str]
    Size: Optional[float]
    SnapshotId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VolumeType: Optional[str]
    Wwn: Optional[str]
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
            Attachment=json_data.get("Attachment"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            BackupId=json_data.get("BackupId"),
            Cascade=json_data.get("Cascade"),
            Description=json_data.get("Description"),
            DeviceType=json_data.get("DeviceType"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            KmsId=json_data.get("KmsId"),
            Multiattach=json_data.get("Multiattach"),
            Name=json_data.get("Name"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
            Tags=json_data.get("Tags"),
            VolumeType=json_data.get("VolumeType"),
            Wwn=json_data.get("Wwn"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Attachment:
    Device: Optional[str]
    Id: Optional[str]
    InstanceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Attachment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Attachment"]:
        if not json_data:
            return None
        return cls(
            Device=json_data.get("Device"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Attachment = Attachment


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


