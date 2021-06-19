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
    AutomaticOsUpgrade: Optional[bool]
    EvictionPolicy: Optional[str]
    HealthProbeId: Optional[str]
    Id: Optional[str]
    LicenseType: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    Overprovision: Optional[bool]
    Priority: Optional[str]
    ProximityPlacementGroupId: Optional[str]
    ResourceGroupName: Optional[str]
    SinglePlacementGroup: Optional[bool]
    Tags: Optional[Sequence["_TagsDefinition"]]
    UpgradePolicyMode: Optional[str]
    Zones: Optional[Sequence[str]]
    BootDiagnostics: Optional[Sequence["_BootDiagnosticsDefinition"]]
    Extension: Optional[Sequence["_ExtensionDefinition"]]
    Identity: Optional[Sequence["_IdentityDefinition"]]
    NetworkProfile: Optional[Sequence["_NetworkProfileDefinition"]]
    OsProfile: Optional[Sequence["_OsProfileDefinition"]]
    OsProfileLinuxConfig: Optional[Sequence["_OsProfileLinuxConfigDefinition"]]
    OsProfileSecrets: Optional[Sequence["_OsProfileSecretsDefinition"]]
    OsProfileWindowsConfig: Optional[Sequence["_OsProfileWindowsConfigDefinition"]]
    Plan: Optional[Sequence["_PlanDefinition"]]
    RollingUpgradePolicy: Optional[Sequence["_RollingUpgradePolicyDefinition"]]
    Sku: Optional[Sequence["_SkuDefinition"]]
    StorageProfileDataDisk: Optional[Sequence["_StorageProfileDataDiskDefinition"]]
    StorageProfileImageReference: Optional[Sequence["_StorageProfileImageReferenceDefinition"]]
    StorageProfileOsDisk: Optional[Sequence["_StorageProfileOsDiskDefinition"]]
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
            AutomaticOsUpgrade=json_data.get("AutomaticOsUpgrade"),
            EvictionPolicy=json_data.get("EvictionPolicy"),
            HealthProbeId=json_data.get("HealthProbeId"),
            Id=json_data.get("Id"),
            LicenseType=json_data.get("LicenseType"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Overprovision=json_data.get("Overprovision"),
            Priority=json_data.get("Priority"),
            ProximityPlacementGroupId=json_data.get("ProximityPlacementGroupId"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SinglePlacementGroup=json_data.get("SinglePlacementGroup"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            UpgradePolicyMode=json_data.get("UpgradePolicyMode"),
            Zones=json_data.get("Zones"),
            BootDiagnostics=deserialize_list(json_data.get("BootDiagnostics"), BootDiagnosticsDefinition),
            Extension=deserialize_list(json_data.get("Extension"), ExtensionDefinition),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            NetworkProfile=deserialize_list(json_data.get("NetworkProfile"), NetworkProfileDefinition),
            OsProfile=deserialize_list(json_data.get("OsProfile"), OsProfileDefinition),
            OsProfileLinuxConfig=deserialize_list(json_data.get("OsProfileLinuxConfig"), OsProfileLinuxConfigDefinition),
            OsProfileSecrets=deserialize_list(json_data.get("OsProfileSecrets"), OsProfileSecretsDefinition),
            OsProfileWindowsConfig=deserialize_list(json_data.get("OsProfileWindowsConfig"), OsProfileWindowsConfigDefinition),
            Plan=deserialize_list(json_data.get("Plan"), PlanDefinition),
            RollingUpgradePolicy=deserialize_list(json_data.get("RollingUpgradePolicy"), RollingUpgradePolicyDefinition),
            Sku=deserialize_list(json_data.get("Sku"), SkuDefinition),
            StorageProfileDataDisk=deserialize_list(json_data.get("StorageProfileDataDisk"), StorageProfileDataDiskDefinition),
            StorageProfileImageReference=deserialize_list(json_data.get("StorageProfileImageReference"), StorageProfileImageReferenceDefinition),
            StorageProfileOsDisk=deserialize_list(json_data.get("StorageProfileOsDisk"), StorageProfileOsDiskDefinition),
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
class ExtensionDefinition(BaseModel):
    AutoUpgradeMinorVersion: Optional[bool]
    Name: Optional[str]
    ProtectedSettings: Optional[str]
    ProvisionAfterExtensions: Optional[Sequence[str]]
    Publisher: Optional[str]
    Settings: Optional[str]
    Type: Optional[str]
    TypeHandlerVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtensionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtensionDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoUpgradeMinorVersion=json_data.get("AutoUpgradeMinorVersion"),
            Name=json_data.get("Name"),
            ProtectedSettings=json_data.get("ProtectedSettings"),
            ProvisionAfterExtensions=json_data.get("ProvisionAfterExtensions"),
            Publisher=json_data.get("Publisher"),
            Settings=json_data.get("Settings"),
            Type=json_data.get("Type"),
            TypeHandlerVersion=json_data.get("TypeHandlerVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtensionDefinition = ExtensionDefinition


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
class NetworkProfileDefinition(BaseModel):
    AcceleratedNetworking: Optional[bool]
    IpForwarding: Optional[bool]
    Name: Optional[str]
    NetworkSecurityGroupId: Optional[str]
    Primary: Optional[bool]
    DnsSettings: Optional[Sequence["_DnsSettingsDefinition"]]
    IpConfiguration: Optional[Sequence["_IpConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            AcceleratedNetworking=json_data.get("AcceleratedNetworking"),
            IpForwarding=json_data.get("IpForwarding"),
            Name=json_data.get("Name"),
            NetworkSecurityGroupId=json_data.get("NetworkSecurityGroupId"),
            Primary=json_data.get("Primary"),
            DnsSettings=deserialize_list(json_data.get("DnsSettings"), DnsSettingsDefinition),
            IpConfiguration=deserialize_list(json_data.get("IpConfiguration"), IpConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkProfileDefinition = NetworkProfileDefinition


@dataclass
class DnsSettingsDefinition(BaseModel):
    DnsServers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsServers=json_data.get("DnsServers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsSettingsDefinition = DnsSettingsDefinition


@dataclass
class IpConfigurationDefinition(BaseModel):
    ApplicationGatewayBackendAddressPoolIds: Optional[Sequence[str]]
    ApplicationSecurityGroupIds: Optional[Sequence[str]]
    LoadBalancerBackendAddressPoolIds: Optional[Sequence[str]]
    LoadBalancerInboundNatRulesIds: Optional[Sequence[str]]
    Name: Optional[str]
    Primary: Optional[bool]
    SubnetId: Optional[str]
    PublicIpAddressConfiguration: Optional[Sequence["_PublicIpAddressConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ApplicationGatewayBackendAddressPoolIds=json_data.get("ApplicationGatewayBackendAddressPoolIds"),
            ApplicationSecurityGroupIds=json_data.get("ApplicationSecurityGroupIds"),
            LoadBalancerBackendAddressPoolIds=json_data.get("LoadBalancerBackendAddressPoolIds"),
            LoadBalancerInboundNatRulesIds=json_data.get("LoadBalancerInboundNatRulesIds"),
            Name=json_data.get("Name"),
            Primary=json_data.get("Primary"),
            SubnetId=json_data.get("SubnetId"),
            PublicIpAddressConfiguration=deserialize_list(json_data.get("PublicIpAddressConfiguration"), PublicIpAddressConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpConfigurationDefinition = IpConfigurationDefinition


@dataclass
class PublicIpAddressConfigurationDefinition(BaseModel):
    DomainNameLabel: Optional[str]
    IdleTimeout: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicIpAddressConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicIpAddressConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            DomainNameLabel=json_data.get("DomainNameLabel"),
            IdleTimeout=json_data.get("IdleTimeout"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicIpAddressConfigurationDefinition = PublicIpAddressConfigurationDefinition


@dataclass
class OsProfileDefinition(BaseModel):
    AdminPassword: Optional[str]
    AdminUsername: Optional[str]
    ComputerNamePrefix: Optional[str]
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
            ComputerNamePrefix=json_data.get("ComputerNamePrefix"),
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
class RollingUpgradePolicyDefinition(BaseModel):
    MaxBatchInstancePercent: Optional[float]
    MaxUnhealthyInstancePercent: Optional[float]
    MaxUnhealthyUpgradedInstancePercent: Optional[float]
    PauseTimeBetweenBatches: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RollingUpgradePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RollingUpgradePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxBatchInstancePercent=json_data.get("MaxBatchInstancePercent"),
            MaxUnhealthyInstancePercent=json_data.get("MaxUnhealthyInstancePercent"),
            MaxUnhealthyUpgradedInstancePercent=json_data.get("MaxUnhealthyUpgradedInstancePercent"),
            PauseTimeBetweenBatches=json_data.get("PauseTimeBetweenBatches"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RollingUpgradePolicyDefinition = RollingUpgradePolicyDefinition


@dataclass
class SkuDefinition(BaseModel):
    Capacity: Optional[float]
    Name: Optional[str]
    Tier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SkuDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SkuDefinition"]:
        if not json_data:
            return None
        return cls(
            Capacity=json_data.get("Capacity"),
            Name=json_data.get("Name"),
            Tier=json_data.get("Tier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SkuDefinition = SkuDefinition


@dataclass
class StorageProfileDataDiskDefinition(BaseModel):
    Caching: Optional[str]
    CreateOption: Optional[str]
    DiskSizeGb: Optional[float]
    Lun: Optional[float]
    ManagedDiskType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageProfileDataDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageProfileDataDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            Caching=json_data.get("Caching"),
            CreateOption=json_data.get("CreateOption"),
            DiskSizeGb=json_data.get("DiskSizeGb"),
            Lun=json_data.get("Lun"),
            ManagedDiskType=json_data.get("ManagedDiskType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageProfileDataDiskDefinition = StorageProfileDataDiskDefinition


@dataclass
class StorageProfileImageReferenceDefinition(BaseModel):
    Id: Optional[str]
    Offer: Optional[str]
    Publisher: Optional[str]
    Sku: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageProfileImageReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageProfileImageReferenceDefinition"]:
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
_StorageProfileImageReferenceDefinition = StorageProfileImageReferenceDefinition


@dataclass
class StorageProfileOsDiskDefinition(BaseModel):
    Caching: Optional[str]
    CreateOption: Optional[str]
    Image: Optional[str]
    ManagedDiskType: Optional[str]
    Name: Optional[str]
    OsType: Optional[str]
    VhdContainers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_StorageProfileOsDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageProfileOsDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            Caching=json_data.get("Caching"),
            CreateOption=json_data.get("CreateOption"),
            Image=json_data.get("Image"),
            ManagedDiskType=json_data.get("ManagedDiskType"),
            Name=json_data.get("Name"),
            OsType=json_data.get("OsType"),
            VhdContainers=json_data.get("VhdContainers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageProfileOsDiskDefinition = StorageProfileOsDiskDefinition


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


