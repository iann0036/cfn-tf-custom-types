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
    AvailabilityZone: Optional[str]
    BackupUnitId: Optional[str]
    Bus: Optional[str]
    CpuHotPlug: Optional[bool]
    DatacenterId: Optional[str]
    DiscVirtioHotPlug: Optional[bool]
    DiscVirtioHotUnplug: Optional[bool]
    DiskType: Optional[str]
    Id: Optional[str]
    ImageName: Optional[str]
    ImagePassword: Optional[str]
    LicenceType: Optional[str]
    Name: Optional[str]
    NicHotPlug: Optional[bool]
    NicHotUnplug: Optional[bool]
    RamHotPlug: Optional[bool]
    ServerId: Optional[str]
    Size: Optional[float]
    SshKeyPath: Optional[Sequence[str]]
    Sshkey: Optional[str]
    UserData: Optional[str]
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
            AvailabilityZone=json_data.get("AvailabilityZone"),
            BackupUnitId=json_data.get("BackupUnitId"),
            Bus=json_data.get("Bus"),
            CpuHotPlug=json_data.get("CpuHotPlug"),
            DatacenterId=json_data.get("DatacenterId"),
            DiscVirtioHotPlug=json_data.get("DiscVirtioHotPlug"),
            DiscVirtioHotUnplug=json_data.get("DiscVirtioHotUnplug"),
            DiskType=json_data.get("DiskType"),
            Id=json_data.get("Id"),
            ImageName=json_data.get("ImageName"),
            ImagePassword=json_data.get("ImagePassword"),
            LicenceType=json_data.get("LicenceType"),
            Name=json_data.get("Name"),
            NicHotPlug=json_data.get("NicHotPlug"),
            NicHotUnplug=json_data.get("NicHotUnplug"),
            RamHotPlug=json_data.get("RamHotPlug"),
            ServerId=json_data.get("ServerId"),
            Size=json_data.get("Size"),
            SshKeyPath=json_data.get("SshKeyPath"),
            Sshkey=json_data.get("Sshkey"),
            UserData=json_data.get("UserData"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Default: Optional[str]
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
            Default=json_data.get("Default"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


