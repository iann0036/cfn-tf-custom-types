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
    AuthorizedKeys: Optional[Sequence[str]]
    AuthorizedUsers: Optional[Sequence[str]]
    BackupId: Optional[float]
    Backups: Optional[Sequence["_Backups"]]
    BackupsEnabled: Optional[bool]
    BootConfigLabel: Optional[str]
    Group: Optional[str]
    Id: Optional[str]
    Image: Optional[str]
    IpAddress: Optional[str]
    Ipv4: Optional[Sequence[str]]
    Ipv6: Optional[str]
    Label: Optional[str]
    PrivateIp: Optional[bool]
    PrivateIpAddress: Optional[str]
    Region: Optional[str]
    RootPass: Optional[str]
    Specs: Optional[Sequence["_Specs"]]
    StackscriptData: Optional[Sequence["_StackscriptData"]]
    StackscriptId: Optional[float]
    Status: Optional[str]
    SwapSize: Optional[float]
    Tags: Optional[Sequence[str]]
    Type: Optional[str]
    WatchdogEnabled: Optional[bool]
    Alerts: Optional[Sequence["_Alerts"]]
    Config: Optional[Sequence["_Config"]]
    Disk: Optional[Sequence["_Disk"]]
    Timeouts: Optional["_Timeouts"]
    Devices: Optional[Sequence["_Devices"]]
    Helpers: Optional[Sequence["_Helpers"]]
    Sda: Optional[Sequence["_Sda"]]
    Sdb: Optional[Sequence["_Sdb"]]
    Sdc: Optional[Sequence["_Sdc"]]
    Sdd: Optional[Sequence["_Sdd"]]
    Sde: Optional[Sequence["_Sde"]]
    Sdf: Optional[Sequence["_Sdf"]]
    Sdg: Optional[Sequence["_Sdg"]]
    Sdh: Optional[Sequence["_Sdh"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AuthorizedKeys=json_data.get("AuthorizedKeys"),
            AuthorizedUsers=json_data.get("AuthorizedUsers"),
            BackupId=json_data.get("BackupId"),
            Backups=json_data.get("Backups"),
            BackupsEnabled=json_data.get("BackupsEnabled"),
            BootConfigLabel=json_data.get("BootConfigLabel"),
            Group=json_data.get("Group"),
            Id=json_data.get("Id"),
            Image=json_data.get("Image"),
            IpAddress=json_data.get("IpAddress"),
            Ipv4=json_data.get("Ipv4"),
            Ipv6=json_data.get("Ipv6"),
            Label=json_data.get("Label"),
            PrivateIp=json_data.get("PrivateIp"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            Region=json_data.get("Region"),
            RootPass=json_data.get("RootPass"),
            Specs=json_data.get("Specs"),
            StackscriptData=json_data.get("StackscriptData"),
            StackscriptId=json_data.get("StackscriptId"),
            Status=json_data.get("Status"),
            SwapSize=json_data.get("SwapSize"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            WatchdogEnabled=json_data.get("WatchdogEnabled"),
            Alerts=json_data.get("Alerts"),
            Config=json_data.get("Config"),
            Disk=json_data.get("Disk"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Devices=json_data.get("Devices"),
            Helpers=json_data.get("Helpers"),
            Sda=json_data.get("Sda"),
            Sdb=json_data.get("Sdb"),
            Sdc=json_data.get("Sdc"),
            Sdd=json_data.get("Sdd"),
            Sde=json_data.get("Sde"),
            Sdf=json_data.get("Sdf"),
            Sdg=json_data.get("Sdg"),
            Sdh=json_data.get("Sdh"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Backups:
    Enabled: Optional[bool]
    Schedule: Optional[Sequence["_Schedule"]]

    @classmethod
    def _deserialize(
        cls: Type["_Backups"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Backups"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Schedule=json_data.get("Schedule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Backups = Backups


@dataclass
class Schedule:
    Day: Optional[str]
    Window: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Schedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Schedule"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            Window=json_data.get("Window"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Schedule = Schedule


@dataclass
class Specs:
    Disk: Optional[float]
    Memory: Optional[float]
    Transfer: Optional[float]
    Vcpus: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Specs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Specs"]:
        if not json_data:
            return None
        return cls(
            Disk=json_data.get("Disk"),
            Memory=json_data.get("Memory"),
            Transfer=json_data.get("Transfer"),
            Vcpus=json_data.get("Vcpus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Specs = Specs


@dataclass
class StackscriptData:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StackscriptData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StackscriptData"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StackscriptData = StackscriptData


@dataclass
class Alerts:
    Cpu: Optional[float]
    Io: Optional[float]
    NetworkIn: Optional[float]
    NetworkOut: Optional[float]
    TransferQuota: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Alerts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Alerts"]:
        if not json_data:
            return None
        return cls(
            Cpu=json_data.get("Cpu"),
            Io=json_data.get("Io"),
            NetworkIn=json_data.get("NetworkIn"),
            NetworkOut=json_data.get("NetworkOut"),
            TransferQuota=json_data.get("TransferQuota"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Alerts = Alerts


@dataclass
class Config:
    Comments: Optional[str]
    Kernel: Optional[str]
    Label: Optional[str]
    MemoryLimit: Optional[float]
    RootDevice: Optional[str]
    RunLevel: Optional[str]
    VirtMode: Optional[str]
    Devices: Optional[Sequence["_Devices"]]
    Helpers: Optional[Sequence["_Helpers"]]

    @classmethod
    def _deserialize(
        cls: Type["_Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Config"]:
        if not json_data:
            return None
        return cls(
            Comments=json_data.get("Comments"),
            Kernel=json_data.get("Kernel"),
            Label=json_data.get("Label"),
            MemoryLimit=json_data.get("MemoryLimit"),
            RootDevice=json_data.get("RootDevice"),
            RunLevel=json_data.get("RunLevel"),
            VirtMode=json_data.get("VirtMode"),
            Devices=json_data.get("Devices"),
            Helpers=json_data.get("Helpers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Config = Config


@dataclass
class Devices:
    Sda: Optional[Sequence["_Sda"]]
    Sdb: Optional[Sequence["_Sdb"]]
    Sdc: Optional[Sequence["_Sdc"]]
    Sdd: Optional[Sequence["_Sdd"]]
    Sde: Optional[Sequence["_Sde"]]
    Sdf: Optional[Sequence["_Sdf"]]
    Sdg: Optional[Sequence["_Sdg"]]
    Sdh: Optional[Sequence["_Sdh"]]

    @classmethod
    def _deserialize(
        cls: Type["_Devices"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Devices"]:
        if not json_data:
            return None
        return cls(
            Sda=json_data.get("Sda"),
            Sdb=json_data.get("Sdb"),
            Sdc=json_data.get("Sdc"),
            Sdd=json_data.get("Sdd"),
            Sde=json_data.get("Sde"),
            Sdf=json_data.get("Sdf"),
            Sdg=json_data.get("Sdg"),
            Sdh=json_data.get("Sdh"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Devices = Devices


@dataclass
class Sda:
    DiskId: Optional[float]
    DiskLabel: Optional[str]
    VolumeId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Sda"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sda"]:
        if not json_data:
            return None
        return cls(
            DiskId=json_data.get("DiskId"),
            DiskLabel=json_data.get("DiskLabel"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sda = Sda


@dataclass
class Sdb:
    DiskId: Optional[float]
    DiskLabel: Optional[str]
    VolumeId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Sdb"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sdb"]:
        if not json_data:
            return None
        return cls(
            DiskId=json_data.get("DiskId"),
            DiskLabel=json_data.get("DiskLabel"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sdb = Sdb


@dataclass
class Sdc:
    DiskId: Optional[float]
    DiskLabel: Optional[str]
    VolumeId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Sdc"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sdc"]:
        if not json_data:
            return None
        return cls(
            DiskId=json_data.get("DiskId"),
            DiskLabel=json_data.get("DiskLabel"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sdc = Sdc


@dataclass
class Sdd:
    DiskId: Optional[float]
    DiskLabel: Optional[str]
    VolumeId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Sdd"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sdd"]:
        if not json_data:
            return None
        return cls(
            DiskId=json_data.get("DiskId"),
            DiskLabel=json_data.get("DiskLabel"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sdd = Sdd


@dataclass
class Sde:
    DiskId: Optional[float]
    DiskLabel: Optional[str]
    VolumeId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Sde"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sde"]:
        if not json_data:
            return None
        return cls(
            DiskId=json_data.get("DiskId"),
            DiskLabel=json_data.get("DiskLabel"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sde = Sde


@dataclass
class Sdf:
    DiskId: Optional[float]
    DiskLabel: Optional[str]
    VolumeId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Sdf"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sdf"]:
        if not json_data:
            return None
        return cls(
            DiskId=json_data.get("DiskId"),
            DiskLabel=json_data.get("DiskLabel"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sdf = Sdf


@dataclass
class Sdg:
    DiskId: Optional[float]
    DiskLabel: Optional[str]
    VolumeId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Sdg"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sdg"]:
        if not json_data:
            return None
        return cls(
            DiskId=json_data.get("DiskId"),
            DiskLabel=json_data.get("DiskLabel"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sdg = Sdg


@dataclass
class Sdh:
    DiskId: Optional[float]
    DiskLabel: Optional[str]
    VolumeId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Sdh"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sdh"]:
        if not json_data:
            return None
        return cls(
            DiskId=json_data.get("DiskId"),
            DiskLabel=json_data.get("DiskLabel"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sdh = Sdh


@dataclass
class Helpers:
    DevtmpfsAutomount: Optional[bool]
    Distro: Optional[bool]
    ModulesDep: Optional[bool]
    Network: Optional[bool]
    UpdatedbDisabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Helpers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Helpers"]:
        if not json_data:
            return None
        return cls(
            DevtmpfsAutomount=json_data.get("DevtmpfsAutomount"),
            Distro=json_data.get("Distro"),
            ModulesDep=json_data.get("ModulesDep"),
            Network=json_data.get("Network"),
            UpdatedbDisabled=json_data.get("UpdatedbDisabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Helpers = Helpers


@dataclass
class Disk:
    AuthorizedKeys: Optional[Sequence[str]]
    AuthorizedUsers: Optional[Sequence[str]]
    Filesystem: Optional[str]
    Image: Optional[str]
    Label: Optional[str]
    ReadOnly: Optional[bool]
    RootPass: Optional[str]
    Size: Optional[float]
    StackscriptData: Optional[Sequence["_StackscriptData2"]]
    StackscriptId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Disk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Disk"]:
        if not json_data:
            return None
        return cls(
            AuthorizedKeys=json_data.get("AuthorizedKeys"),
            AuthorizedUsers=json_data.get("AuthorizedUsers"),
            Filesystem=json_data.get("Filesystem"),
            Image=json_data.get("Image"),
            Label=json_data.get("Label"),
            ReadOnly=json_data.get("ReadOnly"),
            RootPass=json_data.get("RootPass"),
            Size=json_data.get("Size"),
            StackscriptData=json_data.get("StackscriptData"),
            StackscriptId=json_data.get("StackscriptId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Disk = Disk


@dataclass
class StackscriptData2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StackscriptData2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StackscriptData2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StackscriptData2 = StackscriptData2


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


