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
    AuthorizedKeys: Optional[Sequence[str]]
    AuthorizedUsers: Optional[Sequence[str]]
    BackupId: Optional[float]
    Backups: Optional[Sequence["_BackupsDefinition2"]]
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
    Specs: Optional[Sequence["_SpecsDefinition"]]
    StackscriptData: Optional[Sequence["_StackscriptDataDefinition"]]
    StackscriptId: Optional[float]
    Status: Optional[str]
    SwapSize: Optional[float]
    Tags: Optional[Sequence[str]]
    Type: Optional[str]
    WatchdogEnabled: Optional[bool]
    Alerts: Optional[Sequence["_AlertsDefinition"]]
    Config: Optional[Sequence["_ConfigDefinition"]]
    Disk: Optional[Sequence["_DiskDefinition"]]
    Interface: Optional[Sequence["_InterfaceDefinition"]]
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
            AuthorizedKeys=json_data.get("AuthorizedKeys"),
            AuthorizedUsers=json_data.get("AuthorizedUsers"),
            BackupId=json_data.get("BackupId"),
            Backups=deserialize_list(json_data.get("Backups"), BackupsDefinition2),
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
            Specs=deserialize_list(json_data.get("Specs"), SpecsDefinition),
            StackscriptData=deserialize_list(json_data.get("StackscriptData"), StackscriptDataDefinition),
            StackscriptId=json_data.get("StackscriptId"),
            Status=json_data.get("Status"),
            SwapSize=json_data.get("SwapSize"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            WatchdogEnabled=json_data.get("WatchdogEnabled"),
            Alerts=deserialize_list(json_data.get("Alerts"), AlertsDefinition),
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
            Disk=deserialize_list(json_data.get("Disk"), DiskDefinition),
            Interface=deserialize_list(json_data.get("Interface"), InterfaceDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackupsDefinition2(BaseModel):
    Enabled: Optional[bool]
    Schedule: Optional[Sequence["_BackupsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BackupsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupsDefinition2"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Schedule=deserialize_list(json_data.get("Schedule"), BackupsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupsDefinition2 = BackupsDefinition2


@dataclass
class BackupsDefinition(BaseModel):
    Day: Optional[str]
    Window: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            Window=json_data.get("Window"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupsDefinition = BackupsDefinition


@dataclass
class SpecsDefinition(BaseModel):
    Disk: Optional[float]
    Memory: Optional[float]
    Transfer: Optional[float]
    Vcpus: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SpecsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecsDefinition"]:
        if not json_data:
            return None
        return cls(
            Disk=json_data.get("Disk"),
            Memory=json_data.get("Memory"),
            Transfer=json_data.get("Transfer"),
            Vcpus=json_data.get("Vcpus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecsDefinition = SpecsDefinition


@dataclass
class StackscriptDataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StackscriptDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StackscriptDataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StackscriptDataDefinition = StackscriptDataDefinition


@dataclass
class AlertsDefinition(BaseModel):
    Cpu: Optional[float]
    Io: Optional[float]
    NetworkIn: Optional[float]
    NetworkOut: Optional[float]
    TransferQuota: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AlertsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlertsDefinition"]:
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
_AlertsDefinition = AlertsDefinition


@dataclass
class ConfigDefinition(BaseModel):
    Comments: Optional[str]
    Kernel: Optional[str]
    Label: Optional[str]
    MemoryLimit: Optional[float]
    RootDevice: Optional[str]
    RunLevel: Optional[str]
    VirtMode: Optional[str]
    Devices: Optional[Sequence["_DevicesDefinition"]]
    Helpers: Optional[Sequence["_HelpersDefinition"]]
    Interface: Optional[Sequence["_InterfaceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
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
            Devices=deserialize_list(json_data.get("Devices"), DevicesDefinition),
            Helpers=deserialize_list(json_data.get("Helpers"), HelpersDefinition),
            Interface=deserialize_list(json_data.get("Interface"), InterfaceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


@dataclass
class DevicesDefinition(BaseModel):
    Sda: Optional[Sequence["_SdaDefinition"]]
    Sdb: Optional[Sequence["_SdbDefinition"]]
    Sdc: Optional[Sequence["_SdcDefinition"]]
    Sdd: Optional[Sequence["_SddDefinition"]]
    Sde: Optional[Sequence["_SdeDefinition"]]
    Sdf: Optional[Sequence["_SdfDefinition"]]
    Sdg: Optional[Sequence["_SdgDefinition"]]
    Sdh: Optional[Sequence["_SdhDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DevicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DevicesDefinition"]:
        if not json_data:
            return None
        return cls(
            Sda=deserialize_list(json_data.get("Sda"), SdaDefinition),
            Sdb=deserialize_list(json_data.get("Sdb"), SdbDefinition),
            Sdc=deserialize_list(json_data.get("Sdc"), SdcDefinition),
            Sdd=deserialize_list(json_data.get("Sdd"), SddDefinition),
            Sde=deserialize_list(json_data.get("Sde"), SdeDefinition),
            Sdf=deserialize_list(json_data.get("Sdf"), SdfDefinition),
            Sdg=deserialize_list(json_data.get("Sdg"), SdgDefinition),
            Sdh=deserialize_list(json_data.get("Sdh"), SdhDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DevicesDefinition = DevicesDefinition


@dataclass
class SdaDefinition(BaseModel):
    DiskId: Optional[float]
    DiskLabel: Optional[str]
    VolumeId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SdaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SdaDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskId=json_data.get("DiskId"),
            DiskLabel=json_data.get("DiskLabel"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SdaDefinition = SdaDefinition


@dataclass
class SdbDefinition(BaseModel):
    DiskId: Optional[float]
    DiskLabel: Optional[str]
    VolumeId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SdbDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SdbDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskId=json_data.get("DiskId"),
            DiskLabel=json_data.get("DiskLabel"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SdbDefinition = SdbDefinition


@dataclass
class SdcDefinition(BaseModel):
    DiskId: Optional[float]
    DiskLabel: Optional[str]
    VolumeId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SdcDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SdcDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskId=json_data.get("DiskId"),
            DiskLabel=json_data.get("DiskLabel"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SdcDefinition = SdcDefinition


@dataclass
class SddDefinition(BaseModel):
    DiskId: Optional[float]
    DiskLabel: Optional[str]
    VolumeId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SddDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SddDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskId=json_data.get("DiskId"),
            DiskLabel=json_data.get("DiskLabel"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SddDefinition = SddDefinition


@dataclass
class SdeDefinition(BaseModel):
    DiskId: Optional[float]
    DiskLabel: Optional[str]
    VolumeId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SdeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SdeDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskId=json_data.get("DiskId"),
            DiskLabel=json_data.get("DiskLabel"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SdeDefinition = SdeDefinition


@dataclass
class SdfDefinition(BaseModel):
    DiskId: Optional[float]
    DiskLabel: Optional[str]
    VolumeId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SdfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SdfDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskId=json_data.get("DiskId"),
            DiskLabel=json_data.get("DiskLabel"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SdfDefinition = SdfDefinition


@dataclass
class SdgDefinition(BaseModel):
    DiskId: Optional[float]
    DiskLabel: Optional[str]
    VolumeId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SdgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SdgDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskId=json_data.get("DiskId"),
            DiskLabel=json_data.get("DiskLabel"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SdgDefinition = SdgDefinition


@dataclass
class SdhDefinition(BaseModel):
    DiskId: Optional[float]
    DiskLabel: Optional[str]
    VolumeId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SdhDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SdhDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskId=json_data.get("DiskId"),
            DiskLabel=json_data.get("DiskLabel"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SdhDefinition = SdhDefinition


@dataclass
class HelpersDefinition(BaseModel):
    DevtmpfsAutomount: Optional[bool]
    Distro: Optional[bool]
    ModulesDep: Optional[bool]
    Network: Optional[bool]
    UpdatedbDisabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_HelpersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HelpersDefinition"]:
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
_HelpersDefinition = HelpersDefinition


@dataclass
class InterfaceDefinition(BaseModel):
    IpamAddress: Optional[str]
    Label: Optional[str]
    Purpose: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            IpamAddress=json_data.get("IpamAddress"),
            Label=json_data.get("Label"),
            Purpose=json_data.get("Purpose"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfaceDefinition = InterfaceDefinition


@dataclass
class DiskDefinition(BaseModel):
    AuthorizedKeys: Optional[Sequence[str]]
    AuthorizedUsers: Optional[Sequence[str]]
    Filesystem: Optional[str]
    Image: Optional[str]
    Label: Optional[str]
    ReadOnly: Optional[bool]
    RootPass: Optional[str]
    Size: Optional[float]
    StackscriptData: Optional[Sequence["_StackscriptDataDefinition2"]]
    StackscriptId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskDefinition"]:
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
            StackscriptData=deserialize_list(json_data.get("StackscriptData"), StackscriptDataDefinition2),
            StackscriptId=json_data.get("StackscriptId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskDefinition = DiskDefinition


@dataclass
class StackscriptDataDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StackscriptDataDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StackscriptDataDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StackscriptDataDefinition2 = StackscriptDataDefinition2


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


