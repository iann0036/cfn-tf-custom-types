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
    Account: Optional[str]
    Collocated: Optional[bool]
    Description: Optional[str]
    Id: Optional[str]
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
            Account=json_data.get("Account"),
            Collocated=json_data.get("Collocated"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
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
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


