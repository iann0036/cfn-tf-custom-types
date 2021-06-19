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
    CustomAttributes: Optional[Sequence["_CustomAttributesDefinition"]]
    DatacenterId: Optional[str]
    DatastoreClusterId: Optional[str]
    DatastoreId: Optional[str]
    DefaultIpAddress: Optional[str]
    EfiSecureBootEnabled: Optional[bool]
    EnableDiskUuid: Optional[bool]
    EnableLogging: Optional[bool]
    EptRviMode: Optional[str]
    ExtraConfig: Optional[Sequence["_ExtraConfigDefinition"]]
    Firmware: Optional[str]
    Folder: Optional[str]
    ForcePowerOff: Optional[bool]
    GuestId: Optional[str]
    GuestIpAddresses: Optional[Sequence[str]]
    HardwareVersion: Optional[float]
    HostSystemId: Optional[str]
    HvMode: Optional[str]
    Id: Optional[str]
    IdeControllerCount: Optional[float]
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
    PciDeviceId: Optional[Sequence[str]]
    PoweronTimeout: Optional[float]
    RebootRequired: Optional[bool]
    ReplaceTrigger: Optional[str]
    ResourcePoolId: Optional[str]
    RunToolsScriptsAfterPowerOn: Optional[bool]
    RunToolsScriptsAfterResume: Optional[bool]
    RunToolsScriptsBeforeGuestReboot: Optional[bool]
    RunToolsScriptsBeforeGuestShutdown: Optional[bool]
    RunToolsScriptsBeforeGuestStandby: Optional[bool]
    SataControllerCount: Optional[float]
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
    VbsEnabled: Optional[bool]
    VmwareToolsStatus: Optional[str]
    VmxPath: Optional[str]
    VvtdEnabled: Optional[bool]
    WaitForGuestIpTimeout: Optional[float]
    WaitForGuestNetRoutable: Optional[bool]
    WaitForGuestNetTimeout: Optional[float]
    Cdrom: Optional[Sequence["_CdromDefinition"]]
    Clone: Optional[Sequence["_CloneDefinition"]]
    Disk: Optional[Sequence["_DiskDefinition"]]
    NetworkInterface: Optional[Sequence["_NetworkInterfaceDefinition"]]
    OvfDeploy: Optional[Sequence["_OvfDeployDefinition"]]
    Vapp: Optional[Sequence["_VappDefinition"]]

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
            CustomAttributes=deserialize_list(json_data.get("CustomAttributes"), CustomAttributesDefinition),
            DatacenterId=json_data.get("DatacenterId"),
            DatastoreClusterId=json_data.get("DatastoreClusterId"),
            DatastoreId=json_data.get("DatastoreId"),
            DefaultIpAddress=json_data.get("DefaultIpAddress"),
            EfiSecureBootEnabled=json_data.get("EfiSecureBootEnabled"),
            EnableDiskUuid=json_data.get("EnableDiskUuid"),
            EnableLogging=json_data.get("EnableLogging"),
            EptRviMode=json_data.get("EptRviMode"),
            ExtraConfig=deserialize_list(json_data.get("ExtraConfig"), ExtraConfigDefinition),
            Firmware=json_data.get("Firmware"),
            Folder=json_data.get("Folder"),
            ForcePowerOff=json_data.get("ForcePowerOff"),
            GuestId=json_data.get("GuestId"),
            GuestIpAddresses=json_data.get("GuestIpAddresses"),
            HardwareVersion=json_data.get("HardwareVersion"),
            HostSystemId=json_data.get("HostSystemId"),
            HvMode=json_data.get("HvMode"),
            Id=json_data.get("Id"),
            IdeControllerCount=json_data.get("IdeControllerCount"),
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
            PciDeviceId=json_data.get("PciDeviceId"),
            PoweronTimeout=json_data.get("PoweronTimeout"),
            RebootRequired=json_data.get("RebootRequired"),
            ReplaceTrigger=json_data.get("ReplaceTrigger"),
            ResourcePoolId=json_data.get("ResourcePoolId"),
            RunToolsScriptsAfterPowerOn=json_data.get("RunToolsScriptsAfterPowerOn"),
            RunToolsScriptsAfterResume=json_data.get("RunToolsScriptsAfterResume"),
            RunToolsScriptsBeforeGuestReboot=json_data.get("RunToolsScriptsBeforeGuestReboot"),
            RunToolsScriptsBeforeGuestShutdown=json_data.get("RunToolsScriptsBeforeGuestShutdown"),
            RunToolsScriptsBeforeGuestStandby=json_data.get("RunToolsScriptsBeforeGuestStandby"),
            SataControllerCount=json_data.get("SataControllerCount"),
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
            VbsEnabled=json_data.get("VbsEnabled"),
            VmwareToolsStatus=json_data.get("VmwareToolsStatus"),
            VmxPath=json_data.get("VmxPath"),
            VvtdEnabled=json_data.get("VvtdEnabled"),
            WaitForGuestIpTimeout=json_data.get("WaitForGuestIpTimeout"),
            WaitForGuestNetRoutable=json_data.get("WaitForGuestNetRoutable"),
            WaitForGuestNetTimeout=json_data.get("WaitForGuestNetTimeout"),
            Cdrom=deserialize_list(json_data.get("Cdrom"), CdromDefinition),
            Clone=deserialize_list(json_data.get("Clone"), CloneDefinition),
            Disk=deserialize_list(json_data.get("Disk"), DiskDefinition),
            NetworkInterface=deserialize_list(json_data.get("NetworkInterface"), NetworkInterfaceDefinition),
            OvfDeploy=deserialize_list(json_data.get("OvfDeploy"), OvfDeployDefinition),
            Vapp=deserialize_list(json_data.get("Vapp"), VappDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomAttributesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomAttributesDefinition = CustomAttributesDefinition


@dataclass
class ExtraConfigDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraConfigDefinition = ExtraConfigDefinition


@dataclass
class CdromDefinition(BaseModel):
    ClientDevice: Optional[bool]
    DatastoreId: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CdromDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CdromDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientDevice=json_data.get("ClientDevice"),
            DatastoreId=json_data.get("DatastoreId"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CdromDefinition = CdromDefinition


@dataclass
class CloneDefinition(BaseModel):
    LinkedClone: Optional[bool]
    OvfNetworkMap: Optional[Sequence["_OvfNetworkMapDefinition"]]
    OvfStorageMap: Optional[Sequence["_OvfStorageMapDefinition"]]
    TemplateUuid: Optional[str]
    Timeout: Optional[float]
    Customize: Optional[Sequence["_CustomizeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CloneDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloneDefinition"]:
        if not json_data:
            return None
        return cls(
            LinkedClone=json_data.get("LinkedClone"),
            OvfNetworkMap=deserialize_list(json_data.get("OvfNetworkMap"), OvfNetworkMapDefinition),
            OvfStorageMap=deserialize_list(json_data.get("OvfStorageMap"), OvfStorageMapDefinition),
            TemplateUuid=json_data.get("TemplateUuid"),
            Timeout=json_data.get("Timeout"),
            Customize=deserialize_list(json_data.get("Customize"), CustomizeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloneDefinition = CloneDefinition


@dataclass
class OvfNetworkMapDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OvfNetworkMapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OvfNetworkMapDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OvfNetworkMapDefinition = OvfNetworkMapDefinition


@dataclass
class OvfStorageMapDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OvfStorageMapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OvfStorageMapDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OvfStorageMapDefinition = OvfStorageMapDefinition


@dataclass
class CustomizeDefinition(BaseModel):
    DnsServerList: Optional[Sequence[str]]
    DnsSuffixList: Optional[Sequence[str]]
    Ipv4Gateway: Optional[str]
    Ipv6Gateway: Optional[str]
    Timeout: Optional[float]
    WindowsSysprepText: Optional[str]
    LinuxOptions: Optional[Sequence["_LinuxOptionsDefinition"]]
    NetworkInterface: Optional[Sequence["_NetworkInterfaceDefinition"]]
    WindowsOptions: Optional[Sequence["_WindowsOptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomizeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomizeDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsServerList=json_data.get("DnsServerList"),
            DnsSuffixList=json_data.get("DnsSuffixList"),
            Ipv4Gateway=json_data.get("Ipv4Gateway"),
            Ipv6Gateway=json_data.get("Ipv6Gateway"),
            Timeout=json_data.get("Timeout"),
            WindowsSysprepText=json_data.get("WindowsSysprepText"),
            LinuxOptions=deserialize_list(json_data.get("LinuxOptions"), LinuxOptionsDefinition),
            NetworkInterface=deserialize_list(json_data.get("NetworkInterface"), NetworkInterfaceDefinition),
            WindowsOptions=deserialize_list(json_data.get("WindowsOptions"), WindowsOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomizeDefinition = CustomizeDefinition


@dataclass
class LinuxOptionsDefinition(BaseModel):
    Domain: Optional[str]
    HostName: Optional[str]
    HwClockUtc: Optional[bool]
    TimeZone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LinuxOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinuxOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Domain=json_data.get("Domain"),
            HostName=json_data.get("HostName"),
            HwClockUtc=json_data.get("HwClockUtc"),
            TimeZone=json_data.get("TimeZone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinuxOptionsDefinition = LinuxOptionsDefinition


@dataclass
class NetworkInterfaceDefinition(BaseModel):
    DnsDomain: Optional[str]
    DnsServerList: Optional[Sequence[str]]
    Ipv4Address: Optional[str]
    Ipv4Netmask: Optional[float]
    Ipv6Address: Optional[str]
    Ipv6Netmask: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaceDefinition"]:
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
_NetworkInterfaceDefinition = NetworkInterfaceDefinition


@dataclass
class WindowsOptionsDefinition(BaseModel):
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
        cls: Type["_WindowsOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WindowsOptionsDefinition"]:
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
_WindowsOptionsDefinition = WindowsOptionsDefinition


@dataclass
class DiskDefinition(BaseModel):
    Attach: Optional[bool]
    ControllerType: Optional[str]
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
    Path: Optional[str]
    Size: Optional[float]
    StoragePolicyId: Optional[str]
    ThinProvisioned: Optional[bool]
    UnitNumber: Optional[float]
    WriteThrough: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskDefinition"]:
        if not json_data:
            return None
        return cls(
            Attach=json_data.get("Attach"),
            ControllerType=json_data.get("ControllerType"),
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
            Path=json_data.get("Path"),
            Size=json_data.get("Size"),
            StoragePolicyId=json_data.get("StoragePolicyId"),
            ThinProvisioned=json_data.get("ThinProvisioned"),
            UnitNumber=json_data.get("UnitNumber"),
            WriteThrough=json_data.get("WriteThrough"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskDefinition = DiskDefinition


@dataclass
class OvfDeployDefinition(BaseModel):
    AllowUnverifiedSslCert: Optional[bool]
    DeploymentOption: Optional[str]
    DiskProvisioning: Optional[str]
    EnableHiddenProperties: Optional[bool]
    IpAllocationPolicy: Optional[str]
    IpProtocol: Optional[str]
    LocalOvfPath: Optional[str]
    OvfNetworkMap: Optional[Sequence["_OvfNetworkMapDefinition2"]]
    RemoteOvfUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OvfDeployDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OvfDeployDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowUnverifiedSslCert=json_data.get("AllowUnverifiedSslCert"),
            DeploymentOption=json_data.get("DeploymentOption"),
            DiskProvisioning=json_data.get("DiskProvisioning"),
            EnableHiddenProperties=json_data.get("EnableHiddenProperties"),
            IpAllocationPolicy=json_data.get("IpAllocationPolicy"),
            IpProtocol=json_data.get("IpProtocol"),
            LocalOvfPath=json_data.get("LocalOvfPath"),
            OvfNetworkMap=deserialize_list(json_data.get("OvfNetworkMap"), OvfNetworkMapDefinition2),
            RemoteOvfUrl=json_data.get("RemoteOvfUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OvfDeployDefinition = OvfDeployDefinition


@dataclass
class OvfNetworkMapDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OvfNetworkMapDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OvfNetworkMapDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OvfNetworkMapDefinition2 = OvfNetworkMapDefinition2


@dataclass
class VappDefinition(BaseModel):
    Properties: Optional[Sequence["_PropertiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VappDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VappDefinition"]:
        if not json_data:
            return None
        return cls(
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VappDefinition = VappDefinition


@dataclass
class PropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition = PropertiesDefinition


