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
    Bootable: Optional[bool]
    Description: Optional[str]
    Hypervisor: Optional[str]
    Id: Optional[str]
    ImageList: Optional[str]
    ImageListEntry: Optional[float]
    MachineImage: Optional[str]
    Managed: Optional[bool]
    Name: Optional[str]
    Platform: Optional[str]
    Readonly: Optional[bool]
    Size: Optional[float]
    Snapshot: Optional[str]
    SnapshotAccount: Optional[str]
    SnapshotId: Optional[str]
    Status: Optional[str]
    StoragePool: Optional[str]
    StorageType: Optional[str]
    Tags: Optional[Sequence[str]]
    Uri: Optional[str]
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
            Bootable=json_data.get("Bootable"),
            Description=json_data.get("Description"),
            Hypervisor=json_data.get("Hypervisor"),
            Id=json_data.get("Id"),
            ImageList=json_data.get("ImageList"),
            ImageListEntry=json_data.get("ImageListEntry"),
            MachineImage=json_data.get("MachineImage"),
            Managed=json_data.get("Managed"),
            Name=json_data.get("Name"),
            Platform=json_data.get("Platform"),
            Readonly=json_data.get("Readonly"),
            Size=json_data.get("Size"),
            Snapshot=json_data.get("Snapshot"),
            SnapshotAccount=json_data.get("SnapshotAccount"),
            SnapshotId=json_data.get("SnapshotId"),
            Status=json_data.get("Status"),
            StoragePool=json_data.get("StoragePool"),
            StorageType=json_data.get("StorageType"),
            Tags=json_data.get("Tags"),
            Uri=json_data.get("Uri"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


