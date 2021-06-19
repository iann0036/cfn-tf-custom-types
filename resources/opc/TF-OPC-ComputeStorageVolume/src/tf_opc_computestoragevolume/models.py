# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
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
    Timeouts: Optional["_TimeoutsDefinition"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
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
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


