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
    AvailabilitySetId: Optional[str]
    DeleteDataDisksOnTermination: Optional[bool]
    DeleteOsDiskOnTermination: Optional[bool]
    Id: Optional[str]
    LicenseType: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    NetworkInterfaceIds: Optional[Sequence[str]]
    PrimaryNetworkInterfaceId: Optional[str]
    ProximityPlacementGroupId: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VmSize: Optional[str]
    Zones: Optional[Sequence[str]]
    AdditionalCapabilities: Optional[Sequence["_AdditionalCapabilitiesDefinition"]]
    BootDiagnostics: Optional[Sequence["_BootDiagnosticsDefinition"]]
    Identity: Optional[Sequence["_IdentityDefinition"]]
    OsProfile: Optional[Sequence["_OsProfileDefinition"]]
    OsProfileLinuxConfig: Optional[Sequence["_OsProfileLinuxConfigDefinition"]]
    OsProfileSecrets: Optional[Sequence["_OsProfileSecretsDefinition"]]
    OsProfileWindowsConfig: Optional[Sequence["_OsProfileWindowsConfigDefinition"]]
    Plan: Optional[Sequence["_PlanDefinition"]]
    StorageDataDisk: Optional[Sequence["_StorageDataDiskDefinition"]]
    StorageImageReference: Optional[Sequence["_StorageImageReferenceDefinition"]]
    StorageOsDisk: Optional[Sequence["_StorageOsDiskDefinition"]]
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
            AvailabilitySetId=json_data.get("AvailabilitySetId"),
            DeleteDataDisksOnTermination=json_data.get("DeleteDataDisksOnTermination"),
            DeleteOsDiskOnTermination=json_data.get("DeleteOsDiskOnTermination"),
            Id=json_data.get("Id"),
            LicenseType=json_data.get("LicenseType"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NetworkInterfaceIds=json_data.get("NetworkInterfaceIds"),
            PrimaryNetworkInterfaceId=json_data.get("PrimaryNetworkInterfaceId"),
            ProximityPlacementGroupId=json_data.get("ProximityPlacementGroupId"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VmSize=json_data.get("VmSize"),
            Zones=json_data.get("Zones"),
            AdditionalCapabilities=deserialize_list(json_data.get("AdditionalCapabilities"), AdditionalCapabilitiesDefinition),
            BootDiagnostics=deserialize_list(json_data.get("BootDiagnostics"), BootDiagnosticsDefinition),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            OsProfile=deserialize_list(json_data.get("OsProfile"), OsProfileDefinition),
            OsProfileLinuxConfig=deserialize_list(json_data.get("OsProfileLinuxConfig"), OsProfileLinuxConfigDefinition),
            OsProfileSecrets=deserialize_list(json_data.get("OsProfileSecrets"), OsProfileSecretsDefinition),
            OsProfileWindowsConfig=deserialize_list(json_data.get("OsProfileWindowsConfig"), OsProfileWindowsConfigDefinition),
            Plan=deserialize_list(json_data.get("Plan"), PlanDefinition),
            StorageDataDisk=deserialize_list(json_data.get("StorageDataDisk"), StorageDataDiskDefinition),
            StorageImageReference=deserialize_list(json_data.get("StorageImageReference"), StorageImageReferenceDefinition),
            StorageOsDisk=deserialize_list(json_data.get("StorageOsDisk"), StorageOsDiskDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class AdditionalCapabilitiesDefinition(BaseModel):
    UltraSsdEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalCapabilitiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalCapabilitiesDefinition"]:
        if not json_data:
            return None
        return cls(
            UltraSsdEnabled=json_data.get("UltraSsdEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalCapabilitiesDefinition = AdditionalCapabilitiesDefinition


@dataclass
class BootDiagnosticsDefinition(BaseModel):
    Enabled: Optional[bool]
    StorageUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BootDiagnosticsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BootDiagnosticsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            StorageUri=json_data.get("StorageUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BootDiagnosticsDefinition = BootDiagnosticsDefinition


@dataclass
class IdentityDefinition(BaseModel):
    IdentityIds: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityDefinition"]:
        if not json_data:
            return None
        return cls(
            IdentityIds=json_data.get("IdentityIds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityDefinition = IdentityDefinition


@dataclass
class OsProfileDefinition(BaseModel):
    AdminPassword: Optional[str]
    AdminUsername: Optional[str]
    ComputerName: Optional[str]
    CustomData: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OsProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminPassword=json_data.get("AdminPassword"),
            AdminUsername=json_data.get("AdminUsername"),
            ComputerName=json_data.get("ComputerName"),
            CustomData=json_data.get("CustomData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsProfileDefinition = OsProfileDefinition


@dataclass
class OsProfileLinuxConfigDefinition(BaseModel):
    DisablePasswordAuthentication: Optional[bool]
    SshKeys: Optional[Sequence["_SshKeysDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OsProfileLinuxConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsProfileLinuxConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DisablePasswordAuthentication=json_data.get("DisablePasswordAuthentication"),
            SshKeys=deserialize_list(json_data.get("SshKeys"), SshKeysDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsProfileLinuxConfigDefinition = OsProfileLinuxConfigDefinition


@dataclass
class SshKeysDefinition(BaseModel):
    KeyData: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SshKeysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SshKeysDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyData=json_data.get("KeyData"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SshKeysDefinition = SshKeysDefinition


@dataclass
class OsProfileSecretsDefinition(BaseModel):
    SourceVaultId: Optional[str]
    VaultCertificates: Optional[Sequence["_VaultCertificatesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OsProfileSecretsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsProfileSecretsDefinition"]:
        if not json_data:
            return None
        return cls(
            SourceVaultId=json_data.get("SourceVaultId"),
            VaultCertificates=deserialize_list(json_data.get("VaultCertificates"), VaultCertificatesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsProfileSecretsDefinition = OsProfileSecretsDefinition


@dataclass
class VaultCertificatesDefinition(BaseModel):
    CertificateStore: Optional[str]
    CertificateUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VaultCertificatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VaultCertificatesDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateStore=json_data.get("CertificateStore"),
            CertificateUrl=json_data.get("CertificateUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VaultCertificatesDefinition = VaultCertificatesDefinition


@dataclass
class OsProfileWindowsConfigDefinition(BaseModel):
    EnableAutomaticUpgrades: Optional[bool]
    ProvisionVmAgent: Optional[bool]
    Timezone: Optional[str]
    AdditionalUnattendConfig: Optional[Sequence["_AdditionalUnattendConfigDefinition"]]
    Winrm: Optional[Sequence["_WinrmDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OsProfileWindowsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsProfileWindowsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableAutomaticUpgrades=json_data.get("EnableAutomaticUpgrades"),
            ProvisionVmAgent=json_data.get("ProvisionVmAgent"),
            Timezone=json_data.get("Timezone"),
            AdditionalUnattendConfig=deserialize_list(json_data.get("AdditionalUnattendConfig"), AdditionalUnattendConfigDefinition),
            Winrm=deserialize_list(json_data.get("Winrm"), WinrmDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsProfileWindowsConfigDefinition = OsProfileWindowsConfigDefinition


@dataclass
class AdditionalUnattendConfigDefinition(BaseModel):
    Component: Optional[str]
    Content: Optional[str]
    Pass: Optional[str]
    SettingName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalUnattendConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalUnattendConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Component=json_data.get("Component"),
            Content=json_data.get("Content"),
            Pass=json_data.get("Pass"),
            SettingName=json_data.get("SettingName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalUnattendConfigDefinition = AdditionalUnattendConfigDefinition


@dataclass
class WinrmDefinition(BaseModel):
    CertificateUrl: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WinrmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WinrmDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateUrl=json_data.get("CertificateUrl"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WinrmDefinition = WinrmDefinition


@dataclass
class PlanDefinition(BaseModel):
    Name: Optional[str]
    Product: Optional[str]
    Publisher: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlanDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlanDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Product=json_data.get("Product"),
            Publisher=json_data.get("Publisher"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlanDefinition = PlanDefinition


@dataclass
class StorageDataDiskDefinition(BaseModel):
    Caching: Optional[str]
    CreateOption: Optional[str]
    DiskSizeGb: Optional[float]
    Lun: Optional[float]
    ManagedDiskId: Optional[str]
    ManagedDiskType: Optional[str]
    Name: Optional[str]
    VhdUri: Optional[str]
    WriteAcceleratorEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_StorageDataDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageDataDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            Caching=json_data.get("Caching"),
            CreateOption=json_data.get("CreateOption"),
            DiskSizeGb=json_data.get("DiskSizeGb"),
            Lun=json_data.get("Lun"),
            ManagedDiskId=json_data.get("ManagedDiskId"),
            ManagedDiskType=json_data.get("ManagedDiskType"),
            Name=json_data.get("Name"),
            VhdUri=json_data.get("VhdUri"),
            WriteAcceleratorEnabled=json_data.get("WriteAcceleratorEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageDataDiskDefinition = StorageDataDiskDefinition


@dataclass
class StorageImageReferenceDefinition(BaseModel):
    Id: Optional[str]
    Offer: Optional[str]
    Publisher: Optional[str]
    Sku: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageImageReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageImageReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Offer=json_data.get("Offer"),
            Publisher=json_data.get("Publisher"),
            Sku=json_data.get("Sku"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageImageReferenceDefinition = StorageImageReferenceDefinition


@dataclass
class StorageOsDiskDefinition(BaseModel):
    Caching: Optional[str]
    CreateOption: Optional[str]
    DiskSizeGb: Optional[float]
    ImageUri: Optional[str]
    ManagedDiskId: Optional[str]
    ManagedDiskType: Optional[str]
    Name: Optional[str]
    OsType: Optional[str]
    VhdUri: Optional[str]
    WriteAcceleratorEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_StorageOsDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageOsDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            Caching=json_data.get("Caching"),
            CreateOption=json_data.get("CreateOption"),
            DiskSizeGb=json_data.get("DiskSizeGb"),
            ImageUri=json_data.get("ImageUri"),
            ManagedDiskId=json_data.get("ManagedDiskId"),
            ManagedDiskType=json_data.get("ManagedDiskType"),
            Name=json_data.get("Name"),
            OsType=json_data.get("OsType"),
            VhdUri=json_data.get("VhdUri"),
            WriteAcceleratorEnabled=json_data.get("WriteAcceleratorEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageOsDiskDefinition = StorageOsDiskDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


