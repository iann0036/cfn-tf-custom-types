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
    AvailabilitySetId: Optional[str]
    DeleteDataDisksOnTermination: Optional[bool]
    DeleteOsDiskOnTermination: Optional[bool]
    LicenseType: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    NetworkInterfaceIds: Optional[Sequence[str]]
    PrimaryNetworkInterfaceId: Optional[str]
    ProximityPlacementGroupId: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VmSize: Optional[str]
    Zones: Optional[Sequence[str]]
    AdditionalCapabilities: Optional[Sequence["_AdditionalCapabilities"]]
    BootDiagnostics: Optional[Sequence["_BootDiagnostics"]]
    Identity: Optional[Sequence["_Identity"]]
    OsProfile: Optional[Sequence["_OsProfile"]]
    OsProfileLinuxConfig: Optional[Sequence["_OsProfileLinuxConfig"]]
    OsProfileSecrets: Optional[Sequence["_OsProfileSecrets"]]
    OsProfileWindowsConfig: Optional[Sequence["_OsProfileWindowsConfig"]]
    Plan: Optional[Sequence["_Plan"]]
    StorageDataDisk: Optional[Sequence["_StorageDataDisk"]]
    StorageImageReference: Optional[Sequence["_StorageImageReference"]]
    StorageOsDisk: Optional[Sequence["_StorageOsDisk"]]
    Timeouts: Optional["_Timeouts"]
    SshKeys: Optional[Sequence["_SshKeys"]]
    VaultCertificates: Optional[Sequence["_VaultCertificates"]]
    AdditionalUnattendConfig: Optional[Sequence["_AdditionalUnattendConfig"]]
    Winrm: Optional[Sequence["_Winrm"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AvailabilitySetId=json_data.get("AvailabilitySetId"),
            DeleteDataDisksOnTermination=json_data.get("DeleteDataDisksOnTermination"),
            DeleteOsDiskOnTermination=json_data.get("DeleteOsDiskOnTermination"),
            LicenseType=json_data.get("LicenseType"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NetworkInterfaceIds=json_data.get("NetworkInterfaceIds"),
            PrimaryNetworkInterfaceId=json_data.get("PrimaryNetworkInterfaceId"),
            ProximityPlacementGroupId=json_data.get("ProximityPlacementGroupId"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=json_data.get("Tags"),
            VmSize=json_data.get("VmSize"),
            Zones=json_data.get("Zones"),
            AdditionalCapabilities=json_data.get("AdditionalCapabilities"),
            BootDiagnostics=json_data.get("BootDiagnostics"),
            Identity=json_data.get("Identity"),
            OsProfile=json_data.get("OsProfile"),
            OsProfileLinuxConfig=json_data.get("OsProfileLinuxConfig"),
            OsProfileSecrets=json_data.get("OsProfileSecrets"),
            OsProfileWindowsConfig=json_data.get("OsProfileWindowsConfig"),
            Plan=json_data.get("Plan"),
            StorageDataDisk=json_data.get("StorageDataDisk"),
            StorageImageReference=json_data.get("StorageImageReference"),
            StorageOsDisk=json_data.get("StorageOsDisk"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            SshKeys=json_data.get("SshKeys"),
            VaultCertificates=json_data.get("VaultCertificates"),
            AdditionalUnattendConfig=json_data.get("AdditionalUnattendConfig"),
            Winrm=json_data.get("Winrm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class AdditionalCapabilities:
    UltraSsdEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalCapabilities"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalCapabilities"]:
        if not json_data:
            return None
        return cls(
            UltraSsdEnabled=json_data.get("UltraSsdEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalCapabilities = AdditionalCapabilities


@dataclass
class BootDiagnostics:
    Enabled: Optional[bool]
    StorageUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BootDiagnostics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BootDiagnostics"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            StorageUri=json_data.get("StorageUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BootDiagnostics = BootDiagnostics


@dataclass
class Identity:
    IdentityIds: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Identity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Identity"]:
        if not json_data:
            return None
        return cls(
            IdentityIds=json_data.get("IdentityIds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Identity = Identity


@dataclass
class OsProfile:
    AdminPassword: Optional[str]
    AdminUsername: Optional[str]
    ComputerName: Optional[str]
    CustomData: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OsProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsProfile"]:
        if not json_data:
            return None
        return cls(
            AdminPassword=json_data.get("AdminPassword"),
            AdminUsername=json_data.get("AdminUsername"),
            ComputerName=json_data.get("ComputerName"),
            CustomData=json_data.get("CustomData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsProfile = OsProfile


@dataclass
class OsProfileLinuxConfig:
    DisablePasswordAuthentication: Optional[bool]
    SshKeys: Optional[Sequence["_SshKeys"]]

    @classmethod
    def _deserialize(
        cls: Type["_OsProfileLinuxConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsProfileLinuxConfig"]:
        if not json_data:
            return None
        return cls(
            DisablePasswordAuthentication=json_data.get("DisablePasswordAuthentication"),
            SshKeys=json_data.get("SshKeys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsProfileLinuxConfig = OsProfileLinuxConfig


@dataclass
class SshKeys:
    KeyData: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SshKeys"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SshKeys"]:
        if not json_data:
            return None
        return cls(
            KeyData=json_data.get("KeyData"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SshKeys = SshKeys


@dataclass
class OsProfileSecrets:
    SourceVaultId: Optional[str]
    VaultCertificates: Optional[Sequence["_VaultCertificates"]]

    @classmethod
    def _deserialize(
        cls: Type["_OsProfileSecrets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsProfileSecrets"]:
        if not json_data:
            return None
        return cls(
            SourceVaultId=json_data.get("SourceVaultId"),
            VaultCertificates=json_data.get("VaultCertificates"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsProfileSecrets = OsProfileSecrets


@dataclass
class VaultCertificates:
    CertificateStore: Optional[str]
    CertificateUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VaultCertificates"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VaultCertificates"]:
        if not json_data:
            return None
        return cls(
            CertificateStore=json_data.get("CertificateStore"),
            CertificateUrl=json_data.get("CertificateUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VaultCertificates = VaultCertificates


@dataclass
class OsProfileWindowsConfig:
    EnableAutomaticUpgrades: Optional[bool]
    ProvisionVmAgent: Optional[bool]
    Timezone: Optional[str]
    AdditionalUnattendConfig: Optional[Sequence["_AdditionalUnattendConfig"]]
    Winrm: Optional[Sequence["_Winrm"]]

    @classmethod
    def _deserialize(
        cls: Type["_OsProfileWindowsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsProfileWindowsConfig"]:
        if not json_data:
            return None
        return cls(
            EnableAutomaticUpgrades=json_data.get("EnableAutomaticUpgrades"),
            ProvisionVmAgent=json_data.get("ProvisionVmAgent"),
            Timezone=json_data.get("Timezone"),
            AdditionalUnattendConfig=json_data.get("AdditionalUnattendConfig"),
            Winrm=json_data.get("Winrm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsProfileWindowsConfig = OsProfileWindowsConfig


@dataclass
class AdditionalUnattendConfig:
    Component: Optional[str]
    Content: Optional[str]
    Pass: Optional[str]
    SettingName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalUnattendConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalUnattendConfig"]:
        if not json_data:
            return None
        return cls(
            Component=json_data.get("Component"),
            Content=json_data.get("Content"),
            Pass=json_data.get("Pass"),
            SettingName=json_data.get("SettingName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalUnattendConfig = AdditionalUnattendConfig


@dataclass
class Winrm:
    CertificateUrl: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Winrm"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Winrm"]:
        if not json_data:
            return None
        return cls(
            CertificateUrl=json_data.get("CertificateUrl"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Winrm = Winrm


@dataclass
class Plan:
    Name: Optional[str]
    Product: Optional[str]
    Publisher: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Plan"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Plan"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Product=json_data.get("Product"),
            Publisher=json_data.get("Publisher"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Plan = Plan


@dataclass
class StorageDataDisk:
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
        cls: Type["_StorageDataDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageDataDisk"]:
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
_StorageDataDisk = StorageDataDisk


@dataclass
class StorageImageReference:
    Id: Optional[str]
    Offer: Optional[str]
    Publisher: Optional[str]
    Sku: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageImageReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageImageReference"]:
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
_StorageImageReference = StorageImageReference


@dataclass
class StorageOsDisk:
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
        cls: Type["_StorageOsDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageOsDisk"]:
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
_StorageOsDisk = StorageOsDisk


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


