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
    Account: Optional[str]
    Collocated: Optional[bool]
    Description: Optional[str]
    MachineImageName: Optional[str]
    Name: Optional[str]
    ParentVolumeBootable: Optional[bool]
    Platform: Optional[str]
    Property: Optional[str]
    Size: Optional[str]
    SnapshotId: Optional[str]
    SnapshotTimestamp: Optional[str]
    StartTimestamp: Optional[str]
    Status: Optional[str]
    StatusDetail: Optional[str]
    StatusTimestamp: Optional[str]
    Tags: Optional[Sequence[str]]
    Uri: Optional[str]
    VolumeName: Optional[str]
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
            Account=json_data.get("Account"),
            Collocated=json_data.get("Collocated"),
            Description=json_data.get("Description"),
            MachineImageName=json_data.get("MachineImageName"),
            Name=json_data.get("Name"),
            ParentVolumeBootable=json_data.get("ParentVolumeBootable"),
            Platform=json_data.get("Platform"),
            Property=json_data.get("Property"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
            SnapshotTimestamp=json_data.get("SnapshotTimestamp"),
            StartTimestamp=json_data.get("StartTimestamp"),
            Status=json_data.get("Status"),
            StatusDetail=json_data.get("StatusDetail"),
            StatusTimestamp=json_data.get("StatusTimestamp"),
            Tags=json_data.get("Tags"),
            Uri=json_data.get("Uri"),
            VolumeName=json_data.get("VolumeName"),
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


