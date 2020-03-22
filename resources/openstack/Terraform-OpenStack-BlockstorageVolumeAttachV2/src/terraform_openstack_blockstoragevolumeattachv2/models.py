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
    AttachMode: Optional[str]
    Data: Optional[Sequence["_Data"]]
    Device: Optional[str]
    DriverVolumeType: Optional[str]
    HostName: Optional[str]
    Id: Optional[str]
    Initiator: Optional[str]
    InstanceId: Optional[str]
    IpAddress: Optional[str]
    MountPointBase: Optional[str]
    Multipath: Optional[bool]
    OsType: Optional[str]
    Platform: Optional[str]
    Region: Optional[str]
    VolumeId: Optional[str]
    Wwnn: Optional[str]
    Wwpn: Optional[Sequence[str]]
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
            AttachMode=json_data.get("AttachMode"),
            Data=json_data.get("Data"),
            Device=json_data.get("Device"),
            DriverVolumeType=json_data.get("DriverVolumeType"),
            HostName=json_data.get("HostName"),
            Id=json_data.get("Id"),
            Initiator=json_data.get("Initiator"),
            InstanceId=json_data.get("InstanceId"),
            IpAddress=json_data.get("IpAddress"),
            MountPointBase=json_data.get("MountPointBase"),
            Multipath=json_data.get("Multipath"),
            OsType=json_data.get("OsType"),
            Platform=json_data.get("Platform"),
            Region=json_data.get("Region"),
            VolumeId=json_data.get("VolumeId"),
            Wwnn=json_data.get("Wwnn"),
            Wwpn=json_data.get("Wwpn"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Data:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Data"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Data"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Data = Data


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


