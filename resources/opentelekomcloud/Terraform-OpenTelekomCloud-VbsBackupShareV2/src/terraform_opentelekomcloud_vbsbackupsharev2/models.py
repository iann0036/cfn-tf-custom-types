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
    AvailabilityZone: Optional[str]
    BackupId: Optional[str]
    BackupName: Optional[str]
    BackupStatus: Optional[str]
    Container: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Region: Optional[str]
    ServiceMetadata: Optional[str]
    ShareIds: Optional[Sequence[str]]
    Size: Optional[float]
    SnapshotId: Optional[str]
    ToProjectIds: Optional[Sequence[str]]
    VolumeId: Optional[str]
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
            AvailabilityZone=json_data.get("AvailabilityZone"),
            BackupId=json_data.get("BackupId"),
            BackupName=json_data.get("BackupName"),
            BackupStatus=json_data.get("BackupStatus"),
            Container=json_data.get("Container"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Region=json_data.get("Region"),
            ServiceMetadata=json_data.get("ServiceMetadata"),
            ShareIds=json_data.get("ShareIds"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
            ToProjectIds=json_data.get("ToProjectIds"),
            VolumeId=json_data.get("VolumeId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


