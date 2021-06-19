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
    AdminPass: Optional[str]
    AvailabilityZone: Optional[str]
    FlavorId: Optional[str]
    FlavorName: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    ImageName: Optional[str]
    KeyPair: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    NicPhysicalPorts: Optional[Sequence["_NicPhysicalPortsDefinition3"]]
    UserData: Optional[str]
    Filesystems: Optional[Sequence["_FilesystemsDefinition"]]
    LvmVolumeGroups: Optional[Sequence["_LvmVolumeGroupsDefinition"]]
    Networks: Optional[Sequence["_NetworksDefinition"]]
    Personality: Optional[Sequence["_PersonalityDefinition"]]
    RaidArrays: Optional[Sequence["_RaidArraysDefinition"]]
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
            AdminPass=json_data.get("AdminPass"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            FlavorId=json_data.get("FlavorId"),
            FlavorName=json_data.get("FlavorName"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            ImageName=json_data.get("ImageName"),
            KeyPair=json_data.get("KeyPair"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            NicPhysicalPorts=deserialize_list(json_data.get("NicPhysicalPorts"), NicPhysicalPortsDefinition3),
            UserData=json_data.get("UserData"),
            Filesystems=deserialize_list(json_data.get("Filesystems"), FilesystemsDefinition),
            LvmVolumeGroups=deserialize_list(json_data.get("LvmVolumeGroups"), LvmVolumeGroupsDefinition),
            Networks=deserialize_list(json_data.get("Networks"), NetworksDefinition),
            Personality=deserialize_list(json_data.get("Personality"), PersonalityDefinition),
            RaidArrays=deserialize_list(json_data.get("RaidArrays"), RaidArraysDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class NicPhysicalPortsDefinition3(BaseModel):
    AttachedPorts: Optional[Sequence["_NicPhysicalPortsDefinition2"]]
    HardwareId: Optional[str]
    Id: Optional[str]
    MacAddr: Optional[str]
    NetworkPhysicalPortId: Optional[str]
    Plane: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NicPhysicalPortsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NicPhysicalPortsDefinition3"]:
        if not json_data:
            return None
        return cls(
            AttachedPorts=deserialize_list(json_data.get("AttachedPorts"), NicPhysicalPortsDefinition2),
            HardwareId=json_data.get("HardwareId"),
            Id=json_data.get("Id"),
            MacAddr=json_data.get("MacAddr"),
            NetworkPhysicalPortId=json_data.get("NetworkPhysicalPortId"),
            Plane=json_data.get("Plane"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NicPhysicalPortsDefinition3 = NicPhysicalPortsDefinition3


@dataclass
class NicPhysicalPortsDefinition2(BaseModel):
    FixedIps: Optional[Sequence["_NicPhysicalPortsDefinition"]]
    NetworkId: Optional[str]
    PortId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NicPhysicalPortsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NicPhysicalPortsDefinition2"]:
        if not json_data:
            return None
        return cls(
            FixedIps=deserialize_list(json_data.get("FixedIps"), NicPhysicalPortsDefinition),
            NetworkId=json_data.get("NetworkId"),
            PortId=json_data.get("PortId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NicPhysicalPortsDefinition2 = NicPhysicalPortsDefinition2


@dataclass
class NicPhysicalPortsDefinition(BaseModel):
    IpAddress: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NicPhysicalPortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NicPhysicalPortsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NicPhysicalPortsDefinition = NicPhysicalPortsDefinition


@dataclass
class FilesystemsDefinition(BaseModel):
    FsType: Optional[str]
    Label: Optional[str]
    MountPoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilesystemsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilesystemsDefinition"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            Label=json_data.get("Label"),
            MountPoint=json_data.get("MountPoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilesystemsDefinition = FilesystemsDefinition


@dataclass
class LvmVolumeGroupsDefinition(BaseModel):
    PhysicalVolumePartitionLabels: Optional[Sequence[str]]
    VgLabel: Optional[str]
    LogicalVolumes: Optional[Sequence["_LogicalVolumesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LvmVolumeGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LvmVolumeGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            PhysicalVolumePartitionLabels=json_data.get("PhysicalVolumePartitionLabels"),
            VgLabel=json_data.get("VgLabel"),
            LogicalVolumes=deserialize_list(json_data.get("LogicalVolumes"), LogicalVolumesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LvmVolumeGroupsDefinition = LvmVolumeGroupsDefinition


@dataclass
class LogicalVolumesDefinition(BaseModel):
    LvLabel: Optional[str]
    Size: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogicalVolumesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogicalVolumesDefinition"]:
        if not json_data:
            return None
        return cls(
            LvLabel=json_data.get("LvLabel"),
            Size=json_data.get("Size"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogicalVolumesDefinition = LogicalVolumesDefinition


@dataclass
class NetworksDefinition(BaseModel):
    FixedIp: Optional[str]
    Plane: Optional[str]
    Port: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworksDefinition"]:
        if not json_data:
            return None
        return cls(
            FixedIp=json_data.get("FixedIp"),
            Plane=json_data.get("Plane"),
            Port=json_data.get("Port"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworksDefinition = NetworksDefinition


@dataclass
class PersonalityDefinition(BaseModel):
    Contents: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PersonalityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PersonalityDefinition"]:
        if not json_data:
            return None
        return cls(
            Contents=json_data.get("Contents"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PersonalityDefinition = PersonalityDefinition


@dataclass
class RaidArraysDefinition(BaseModel):
    DiskHardwareIds: Optional[Sequence[str]]
    PrimaryStorage: Optional[bool]
    RaidCardHardwareId: Optional[str]
    RaidLevel: Optional[float]
    Partitions: Optional[Sequence["_PartitionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RaidArraysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RaidArraysDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskHardwareIds=json_data.get("DiskHardwareIds"),
            PrimaryStorage=json_data.get("PrimaryStorage"),
            RaidCardHardwareId=json_data.get("RaidCardHardwareId"),
            RaidLevel=json_data.get("RaidLevel"),
            Partitions=deserialize_list(json_data.get("Partitions"), PartitionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RaidArraysDefinition = RaidArraysDefinition


@dataclass
class PartitionsDefinition(BaseModel):
    Lvm: Optional[bool]
    PartitionLabel: Optional[str]
    Size: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PartitionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PartitionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Lvm=json_data.get("Lvm"),
            PartitionLabel=json_data.get("PartitionLabel"),
            Size=json_data.get("Size"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PartitionsDefinition = PartitionsDefinition


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


