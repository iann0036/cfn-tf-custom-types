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
    AcceptAllEulas: Optional[bool]
    BootImage: Optional[str]
    CatalogName: Optional[str]
    ComputerName: Optional[str]
    CpuCores: Optional[float]
    CpuHotAddEnabled: Optional[bool]
    Cpus: Optional[float]
    Description: Optional[str]
    ExposeHardwareVirtualization: Optional[bool]
    GuestProperties: Optional[Sequence["_GuestPropertiesDefinition"]]
    HardwareVersion: Optional[str]
    Href: Optional[str]
    Id: Optional[str]
    InternalDisk: Optional[Sequence["_InternalDiskDefinition"]]
    Memory: Optional[float]
    MemoryHotAddEnabled: Optional[bool]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    NetworkDhcpWaitSeconds: Optional[float]
    Org: Optional[str]
    OsType: Optional[str]
    PowerOn: Optional[bool]
    PreventUpdatePowerOff: Optional[bool]
    SizingPolicyId: Optional[str]
    StorageProfile: Optional[str]
    TemplateName: Optional[str]
    VappName: Optional[str]
    Vdc: Optional[str]
    VmNameInTemplate: Optional[str]
    VmType: Optional[str]
    Customization: Optional[Sequence["_CustomizationDefinition"]]
    Disk: Optional[Sequence["_DiskDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
    OverrideTemplateDisk: Optional[Sequence["_OverrideTemplateDiskDefinition"]]

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
            AcceptAllEulas=json_data.get("AcceptAllEulas"),
            BootImage=json_data.get("BootImage"),
            CatalogName=json_data.get("CatalogName"),
            ComputerName=json_data.get("ComputerName"),
            CpuCores=json_data.get("CpuCores"),
            CpuHotAddEnabled=json_data.get("CpuHotAddEnabled"),
            Cpus=json_data.get("Cpus"),
            Description=json_data.get("Description"),
            ExposeHardwareVirtualization=json_data.get("ExposeHardwareVirtualization"),
            GuestProperties=deserialize_list(json_data.get("GuestProperties"), GuestPropertiesDefinition),
            HardwareVersion=json_data.get("HardwareVersion"),
            Href=json_data.get("Href"),
            Id=json_data.get("Id"),
            InternalDisk=deserialize_list(json_data.get("InternalDisk"), InternalDiskDefinition),
            Memory=json_data.get("Memory"),
            MemoryHotAddEnabled=json_data.get("MemoryHotAddEnabled"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            NetworkDhcpWaitSeconds=json_data.get("NetworkDhcpWaitSeconds"),
            Org=json_data.get("Org"),
            OsType=json_data.get("OsType"),
            PowerOn=json_data.get("PowerOn"),
            PreventUpdatePowerOff=json_data.get("PreventUpdatePowerOff"),
            SizingPolicyId=json_data.get("SizingPolicyId"),
            StorageProfile=json_data.get("StorageProfile"),
            TemplateName=json_data.get("TemplateName"),
            VappName=json_data.get("VappName"),
            Vdc=json_data.get("Vdc"),
            VmNameInTemplate=json_data.get("VmNameInTemplate"),
            VmType=json_data.get("VmType"),
            Customization=deserialize_list(json_data.get("Customization"), CustomizationDefinition),
            Disk=deserialize_list(json_data.get("Disk"), DiskDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            OverrideTemplateDisk=deserialize_list(json_data.get("OverrideTemplateDisk"), OverrideTemplateDiskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GuestPropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestPropertiesDefinition = GuestPropertiesDefinition


@dataclass
class InternalDiskDefinition(BaseModel):
    BusNumber: Optional[float]
    BusType: Optional[str]
    DiskId: Optional[str]
    Iops: Optional[float]
    SizeInMb: Optional[float]
    StorageProfile: Optional[str]
    ThinProvisioned: Optional[bool]
    UnitNumber: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InternalDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternalDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            BusNumber=json_data.get("BusNumber"),
            BusType=json_data.get("BusType"),
            DiskId=json_data.get("DiskId"),
            Iops=json_data.get("Iops"),
            SizeInMb=json_data.get("SizeInMb"),
            StorageProfile=json_data.get("StorageProfile"),
            ThinProvisioned=json_data.get("ThinProvisioned"),
            UnitNumber=json_data.get("UnitNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternalDiskDefinition = InternalDiskDefinition


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
class CustomizationDefinition(BaseModel):
    AdminPassword: Optional[str]
    AllowLocalAdminPassword: Optional[bool]
    AutoGeneratePassword: Optional[bool]
    ChangeSid: Optional[bool]
    Enabled: Optional[bool]
    Force: Optional[bool]
    Initscript: Optional[str]
    JoinDomain: Optional[bool]
    JoinDomainAccountOu: Optional[str]
    JoinDomainName: Optional[str]
    JoinDomainPassword: Optional[str]
    JoinDomainUser: Optional[str]
    JoinOrgDomain: Optional[bool]
    MustChangePasswordOnFirstLogin: Optional[bool]
    NumberOfAutoLogons: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CustomizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomizationDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminPassword=json_data.get("AdminPassword"),
            AllowLocalAdminPassword=json_data.get("AllowLocalAdminPassword"),
            AutoGeneratePassword=json_data.get("AutoGeneratePassword"),
            ChangeSid=json_data.get("ChangeSid"),
            Enabled=json_data.get("Enabled"),
            Force=json_data.get("Force"),
            Initscript=json_data.get("Initscript"),
            JoinDomain=json_data.get("JoinDomain"),
            JoinDomainAccountOu=json_data.get("JoinDomainAccountOu"),
            JoinDomainName=json_data.get("JoinDomainName"),
            JoinDomainPassword=json_data.get("JoinDomainPassword"),
            JoinDomainUser=json_data.get("JoinDomainUser"),
            JoinOrgDomain=json_data.get("JoinOrgDomain"),
            MustChangePasswordOnFirstLogin=json_data.get("MustChangePasswordOnFirstLogin"),
            NumberOfAutoLogons=json_data.get("NumberOfAutoLogons"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomizationDefinition = CustomizationDefinition


@dataclass
class DiskDefinition(BaseModel):
    BusNumber: Optional[str]
    Name: Optional[str]
    UnitNumber: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskDefinition"]:
        if not json_data:
            return None
        return cls(
            BusNumber=json_data.get("BusNumber"),
            Name=json_data.get("Name"),
            UnitNumber=json_data.get("UnitNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskDefinition = DiskDefinition


@dataclass
class NetworkDefinition(BaseModel):
    AdapterType: Optional[str]
    Connected: Optional[bool]
    Ip: Optional[str]
    IpAllocationMode: Optional[str]
    IsPrimary: Optional[bool]
    Mac: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            AdapterType=json_data.get("AdapterType"),
            Connected=json_data.get("Connected"),
            Ip=json_data.get("Ip"),
            IpAllocationMode=json_data.get("IpAllocationMode"),
            IsPrimary=json_data.get("IsPrimary"),
            Mac=json_data.get("Mac"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class OverrideTemplateDiskDefinition(BaseModel):
    BusNumber: Optional[float]
    BusType: Optional[str]
    Iops: Optional[float]
    SizeInMb: Optional[float]
    StorageProfile: Optional[str]
    UnitNumber: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OverrideTemplateDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverrideTemplateDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            BusNumber=json_data.get("BusNumber"),
            BusType=json_data.get("BusType"),
            Iops=json_data.get("Iops"),
            SizeInMb=json_data.get("SizeInMb"),
            StorageProfile=json_data.get("StorageProfile"),
            UnitNumber=json_data.get("UnitNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverrideTemplateDiskDefinition = OverrideTemplateDiskDefinition


