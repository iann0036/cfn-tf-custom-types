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
    AlternateGuestName: Optional[str]
    Annotation: Optional[str]
    BootDelay: Optional[float]
    BootRetryDelay: Optional[float]
    BootRetryEnabled: Optional[bool]
    ChangeVersion: Optional[str]
    CpuHotAddEnabled: Optional[bool]
    CpuHotRemoveEnabled: Optional[bool]
    CpuLimit: Optional[float]
    CpuPerformanceCountersEnabled: Optional[bool]
    CpuReservation: Optional[float]
    CpuShareCount: Optional[float]
    CpuShareLevel: Optional[str]
    CustomAttributes: Optional[Sequence["_CustomAttributes"]]
    DatastoreClusterId: Optional[str]
    DatastoreId: Optional[str]
    DefaultIpAddress: Optional[str]
    EfiSecureBootEnabled: Optional[bool]
    EnableDiskUuid: Optional[bool]
    EnableLogging: Optional[bool]
    EptRviMode: Optional[str]
    ExtraConfig: Optional[Sequence["_ExtraConfig"]]
    Firmware: Optional[str]
    Folder: Optional[str]
    ForcePowerOff: Optional[bool]
    GuestId: Optional[str]
    GuestIpAddresses: Optional[Sequence[str]]
    HostSystemId: Optional[str]
    HvMode: Optional[str]
    Id: Optional[str]
    IgnoredGuestIps: Optional[Sequence[str]]
    Imported: Optional[bool]
    LatencySensitivity: Optional[str]
    Memory: Optional[float]
    MemoryHotAddEnabled: Optional[bool]
    MemoryLimit: Optional[float]
    MemoryReservation: Optional[float]
    MemoryShareCount: Optional[float]
    MemoryShareLevel: Optional[str]
    MigrateWaitTimeout: Optional[float]
    Moid: Optional[str]
    Name: Optional[str]
    NestedHvEnabled: Optional[bool]
    NumCoresPerSocket: Optional[float]
    NumCpus: Optional[float]
    RebootRequired: Optional[bool]
    ResourcePoolId: Optional[str]
    RunToolsScriptsAfterPowerOn: Optional[bool]
    RunToolsScriptsAfterResume: Optional[bool]
    RunToolsScriptsBeforeGuestReboot: Optional[bool]
    RunToolsScriptsBeforeGuestShutdown: Optional[bool]
    RunToolsScriptsBeforeGuestStandby: Optional[bool]
    ScsiBusSharing: Optional[str]
    ScsiControllerCount: Optional[float]
    ScsiType: Optional[str]
    ShutdownWaitTimeout: Optional[float]
    StoragePolicyId: Optional[str]
    SwapPlacementPolicy: Optional[str]
    SyncTimeWithHost: Optional[bool]
    Tags: Optional[Sequence[str]]
    Uuid: Optional[str]
    VappTransport: Optional[Sequence[str]]
    VmwareToolsStatus: Optional[str]
    VmxPath: Optional[str]
    WaitForGuestIpTimeout: Optional[float]
    WaitForGuestNetRoutable: Optional[bool]
    WaitForGuestNetTimeout: Optional[float]
    Cdrom: Optional[Sequence["_Cdrom"]]
    Clone: Optional[Sequence["_Clone"]]
    Disk: Optional[Sequence["_Disk"]]
    NetworkInterface: Optional[Sequence["_NetworkInterface"]]
    Vapp: Optional[Sequence["_Vapp"]]
    Customize: Optional[Sequence["_Customize"]]
    LinuxOptions: Optional[Sequence["_LinuxOptions"]]
    WindowsOptions: Optional[Sequence["_WindowsOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AlternateGuestName=json_data.get("AlternateGuestName"),
            Annotation=json_data.get("Annotation"),
            BootDelay=json_data.get("BootDelay"),
            BootRetryDelay=json_data.get("BootRetryDelay"),
            BootRetryEnabled=json_data.get("BootRetryEnabled"),
            ChangeVersion=json_data.get("ChangeVersion"),
            CpuHotAddEnabled=json_data.get("CpuHotAddEnabled"),
            CpuHotRemoveEnabled=json_data.get("CpuHotRemoveEnabled"),
            CpuLimit=json_data.get("CpuLimit"),
            CpuPerformanceCountersEnabled=json_data.get("CpuPerformanceCountersEnabled"),
            CpuReservation=json_data.get("CpuReservation"),
            CpuShareCount=json_data.get("CpuShareCount"),
            CpuShareLevel=json_data.get("CpuShareLevel"),
            CustomAttributes=json_data.get("CustomAttributes"),
            DatastoreClusterId=json_data.get("DatastoreClusterId"),
            DatastoreId=json_data.get("DatastoreId"),
            DefaultIpAddress=json_data.get("DefaultIpAddress"),
            EfiSecureBootEnabled=json_data.get("EfiSecureBootEnabled"),
            EnableDiskUuid=json_data.get("EnableDiskUuid"),
            EnableLogging=json_data.get("EnableLogging"),
            EptRviMode=json_data.get("EptRviMode"),
            ExtraConfig=json_data.get("ExtraConfig"),
            Firmware=json_data.get("Firmware"),
            Folder=json_data.get("Folder"),
            ForcePowerOff=json_data.get("ForcePowerOff"),
            GuestId=json_data.get("GuestId"),
            GuestIpAddresses=json_data.get("GuestIpAddresses"),
            HostSystemId=json_data.get("HostSystemId"),
            HvMode=json_data.get("HvMode"),
            Id=json_data.get("Id"),
            IgnoredGuestIps=json_data.get("IgnoredGuestIps"),
            Imported=json_data.get("Imported"),
            LatencySensitivity=json_data.get("LatencySensitivity"),
            Memory=json_data.get("Memory"),
            MemoryHotAddEnabled=json_data.get("MemoryHotAddEnabled"),
            MemoryLimit=json_data.get("MemoryLimit"),
            MemoryReservation=json_data.get("MemoryReservation"),
            MemoryShareCount=json_data.get("MemoryShareCount"),
            MemoryShareLevel=json_data.get("MemoryShareLevel"),
            MigrateWaitTimeout=json_data.get("MigrateWaitTimeout"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            NestedHvEnabled=json_data.get("NestedHvEnabled"),
            NumCoresPerSocket=json_data.get("NumCoresPerSocket"),
            NumCpus=json_data.get("NumCpus"),
            RebootRequired=json_data.get("RebootRequired"),
            ResourcePoolId=json_data.get("ResourcePoolId"),
            RunToolsScriptsAfterPowerOn=json_data.get("RunToolsScriptsAfterPowerOn"),
            RunToolsScriptsAfterResume=json_data.get("RunToolsScriptsAfterResume"),
            RunToolsScriptsBeforeGuestReboot=json_data.get("RunToolsScriptsBeforeGuestReboot"),
            RunToolsScriptsBeforeGuestShutdown=json_data.get("RunToolsScriptsBeforeGuestShutdown"),
            RunToolsScriptsBeforeGuestStandby=json_data.get("RunToolsScriptsBeforeGuestStandby"),
            ScsiBusSharing=json_data.get("ScsiBusSharing"),
            ScsiControllerCount=json_data.get("ScsiControllerCount"),
            ScsiType=json_data.get("ScsiType"),
            ShutdownWaitTimeout=json_data.get("ShutdownWaitTimeout"),
            StoragePolicyId=json_data.get("StoragePolicyId"),
            SwapPlacementPolicy=json_data.get("SwapPlacementPolicy"),
            SyncTimeWithHost=json_data.get("SyncTimeWithHost"),
            Tags=json_data.get("Tags"),
            Uuid=json_data.get("Uuid"),
            VappTransport=json_data.get("VappTransport"),
            VmwareToolsStatus=json_data.get("VmwareToolsStatus"),
            VmxPath=json_data.get("VmxPath"),
            WaitForGuestIpTimeout=json_data.get("WaitForGuestIpTimeout"),
            WaitForGuestNetRoutable=json_data.get("WaitForGuestNetRoutable"),
            WaitForGuestNetTimeout=json_data.get("WaitForGuestNetTimeout"),
            Cdrom=json_data.get("Cdrom"),
            Clone=json_data.get("Clone"),
            Disk=json_data.get("Disk"),
            NetworkInterface=json_data.get("NetworkInterface"),
            Vapp=json_data.get("Vapp"),
            Customize=json_data.get("Customize"),
            LinuxOptions=json_data.get("LinuxOptions"),
            WindowsOptions=json_data.get("WindowsOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomAttributes:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomAttributes"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomAttributes = CustomAttributes


@dataclass
class ExtraConfig:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraConfig"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraConfig = ExtraConfig


@dataclass
class Cdrom:
    ClientDevice: Optional[bool]
    DatastoreId: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Cdrom"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cdrom"]:
        if not json_data:
            return None
        return cls(
            ClientDevice=json_data.get("ClientDevice"),
            DatastoreId=json_data.get("DatastoreId"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cdrom = Cdrom


@dataclass
class Clone:
    LinkedClone: Optional[bool]
    TemplateUuid: Optional[str]
    Timeout: Optional[float]
    Customize: Optional[Sequence["_Customize"]]

    @classmethod
    def _deserialize(
        cls: Type["_Clone"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Clone"]:
        if not json_data:
            return None
        return cls(
            LinkedClone=json_data.get("LinkedClone"),
            TemplateUuid=json_data.get("TemplateUuid"),
            Timeout=json_data.get("Timeout"),
            Customize=json_data.get("Customize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Clone = Clone


@dataclass
class Customize:
    DnsServerList: Optional[Sequence[str]]
    DnsSuffixList: Optional[Sequence[str]]
    Ipv4Gateway: Optional[str]
    Ipv6Gateway: Optional[str]
    Timeout: Optional[float]
    WindowsSysprepText: Optional[str]
    LinuxOptions: Optional[Sequence["_LinuxOptions"]]
    NetworkInterface: Optional[Sequence["_NetworkInterface"]]
    WindowsOptions: Optional[Sequence["_WindowsOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_Customize"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Customize"]:
        if not json_data:
            return None
        return cls(
            DnsServerList=json_data.get("DnsServerList"),
            DnsSuffixList=json_data.get("DnsSuffixList"),
            Ipv4Gateway=json_data.get("Ipv4Gateway"),
            Ipv6Gateway=json_data.get("Ipv6Gateway"),
            Timeout=json_data.get("Timeout"),
            WindowsSysprepText=json_data.get("WindowsSysprepText"),
            LinuxOptions=json_data.get("LinuxOptions"),
            NetworkInterface=json_data.get("NetworkInterface"),
            WindowsOptions=json_data.get("WindowsOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Customize = Customize


@dataclass
class LinuxOptions:
    Domain: Optional[str]
    HostName: Optional[str]
    HwClockUtc: Optional[bool]
    TimeZone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LinuxOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinuxOptions"]:
        if not json_data:
            return None
        return cls(
            Domain=json_data.get("Domain"),
            HostName=json_data.get("HostName"),
            HwClockUtc=json_data.get("HwClockUtc"),
            TimeZone=json_data.get("TimeZone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinuxOptions = LinuxOptions


@dataclass
class NetworkInterface:
    DnsDomain: Optional[str]
    DnsServerList: Optional[Sequence[str]]
    Ipv4Address: Optional[str]
    Ipv4Netmask: Optional[float]
    Ipv6Address: Optional[str]
    Ipv6Netmask: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterface"]:
        if not json_data:
            return None
        return cls(
            DnsDomain=json_data.get("DnsDomain"),
            DnsServerList=json_data.get("DnsServerList"),
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv4Netmask=json_data.get("Ipv4Netmask"),
            Ipv6Address=json_data.get("Ipv6Address"),
            Ipv6Netmask=json_data.get("Ipv6Netmask"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterface = NetworkInterface


@dataclass
class WindowsOptions:
    AdminPassword: Optional[str]
    AutoLogon: Optional[bool]
    AutoLogonCount: Optional[float]
    ComputerName: Optional[str]
    DomainAdminPassword: Optional[str]
    DomainAdminUser: Optional[str]
    FullName: Optional[str]
    JoinDomain: Optional[str]
    OrganizationName: Optional[str]
    ProductKey: Optional[str]
    RunOnceCommandList: Optional[Sequence[str]]
    TimeZone: Optional[float]
    Workgroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WindowsOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WindowsOptions"]:
        if not json_data:
            return None
        return cls(
            AdminPassword=json_data.get("AdminPassword"),
            AutoLogon=json_data.get("AutoLogon"),
            AutoLogonCount=json_data.get("AutoLogonCount"),
            ComputerName=json_data.get("ComputerName"),
            DomainAdminPassword=json_data.get("DomainAdminPassword"),
            DomainAdminUser=json_data.get("DomainAdminUser"),
            FullName=json_data.get("FullName"),
            JoinDomain=json_data.get("JoinDomain"),
            OrganizationName=json_data.get("OrganizationName"),
            ProductKey=json_data.get("ProductKey"),
            RunOnceCommandList=json_data.get("RunOnceCommandList"),
            TimeZone=json_data.get("TimeZone"),
            Workgroup=json_data.get("Workgroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WindowsOptions = WindowsOptions


@dataclass
class Disk:
    Attach: Optional[bool]
    DatastoreId: Optional[str]
    DiskMode: Optional[str]
    DiskSharing: Optional[str]
    EagerlyScrub: Optional[bool]
    IoLimit: Optional[float]
    IoReservation: Optional[float]
    IoShareCount: Optional[float]
    IoShareLevel: Optional[str]
    KeepOnRemove: Optional[bool]
    Label: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Size: Optional[float]
    StoragePolicyId: Optional[str]
    ThinProvisioned: Optional[bool]
    UnitNumber: Optional[float]
    WriteThrough: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Disk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Disk"]:
        if not json_data:
            return None
        return cls(
            Attach=json_data.get("Attach"),
            DatastoreId=json_data.get("DatastoreId"),
            DiskMode=json_data.get("DiskMode"),
            DiskSharing=json_data.get("DiskSharing"),
            EagerlyScrub=json_data.get("EagerlyScrub"),
            IoLimit=json_data.get("IoLimit"),
            IoReservation=json_data.get("IoReservation"),
            IoShareCount=json_data.get("IoShareCount"),
            IoShareLevel=json_data.get("IoShareLevel"),
            KeepOnRemove=json_data.get("KeepOnRemove"),
            Label=json_data.get("Label"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Size=json_data.get("Size"),
            StoragePolicyId=json_data.get("StoragePolicyId"),
            ThinProvisioned=json_data.get("ThinProvisioned"),
            UnitNumber=json_data.get("UnitNumber"),
            WriteThrough=json_data.get("WriteThrough"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Disk = Disk


@dataclass
class Vapp:
    Properties: Optional[Sequence["_Properties"]]

    @classmethod
    def _deserialize(
        cls: Type["_Vapp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Vapp"]:
        if not json_data:
            return None
        return cls(
            Properties=json_data.get("Properties"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Vapp = Vapp


@dataclass
class Properties:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Properties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Properties"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Properties = Properties


