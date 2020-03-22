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
    Tags: Optional[Sequence["_Tags"]]
    UpgradePolicyMode: Optional[str]
    Zones: Optional[Sequence[str]]
    BootDiagnostics: Optional[Sequence["_BootDiagnostics"]]
    Extension: Optional[Sequence["_Extension"]]
    Identity: Optional[Sequence["_Identity"]]
    NetworkProfile: Optional[Sequence["_NetworkProfile"]]
    OsProfile: Optional[Sequence["_OsProfile"]]
    OsProfileLinuxConfig: Optional[Sequence["_OsProfileLinuxConfig"]]
    OsProfileSecrets: Optional[Sequence["_OsProfileSecrets"]]
    OsProfileWindowsConfig: Optional[Sequence["_OsProfileWindowsConfig"]]
    Plan: Optional[Sequence["_Plan"]]
    RollingUpgradePolicy: Optional[Sequence["_RollingUpgradePolicy"]]
    Sku: Optional[Sequence["_Sku"]]
    StorageProfileDataDisk: Optional[Sequence["_StorageProfileDataDisk"]]
    StorageProfileImageReference: Optional[Sequence["_StorageProfileImageReference"]]
    StorageProfileOsDisk: Optional[Sequence["_StorageProfileOsDisk"]]
    Timeouts: Optional["_Timeouts"]
    DnsSettings: Optional[Sequence["_DnsSettings"]]
    IpConfiguration: Optional[Sequence["_IpConfiguration"]]
    SshKeys: Optional[Sequence["_SshKeys"]]
    VaultCertificates: Optional[Sequence["_VaultCertificates"]]
    AdditionalUnattendConfig: Optional[Sequence["_AdditionalUnattendConfig"]]
    Winrm: Optional[Sequence["_Winrm"]]
    PublicIpAddressConfiguration: Optional[Sequence["_PublicIpAddressConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            Tags=json_data.get("Tags"),
            UpgradePolicyMode=json_data.get("UpgradePolicyMode"),
            Zones=json_data.get("Zones"),
            BootDiagnostics=json_data.get("BootDiagnostics"),
            Extension=json_data.get("Extension"),
            Identity=json_data.get("Identity"),
            NetworkProfile=json_data.get("NetworkProfile"),
            OsProfile=json_data.get("OsProfile"),
            OsProfileLinuxConfig=json_data.get("OsProfileLinuxConfig"),
            OsProfileSecrets=json_data.get("OsProfileSecrets"),
            OsProfileWindowsConfig=json_data.get("OsProfileWindowsConfig"),
            Plan=json_data.get("Plan"),
            RollingUpgradePolicy=json_data.get("RollingUpgradePolicy"),
            Sku=json_data.get("Sku"),
            StorageProfileDataDisk=json_data.get("StorageProfileDataDisk"),
            StorageProfileImageReference=json_data.get("StorageProfileImageReference"),
            StorageProfileOsDisk=json_data.get("StorageProfileOsDisk"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            DnsSettings=json_data.get("DnsSettings"),
            IpConfiguration=json_data.get("IpConfiguration"),
            SshKeys=json_data.get("SshKeys"),
            VaultCertificates=json_data.get("VaultCertificates"),
            AdditionalUnattendConfig=json_data.get("AdditionalUnattendConfig"),
            Winrm=json_data.get("Winrm"),
            PublicIpAddressConfiguration=json_data.get("PublicIpAddressConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


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
class Extension:
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
        cls: Type["_Extension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Extension"]:
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
_Extension = Extension


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
class NetworkProfile:
    AcceleratedNetworking: Optional[bool]
    IpForwarding: Optional[bool]
    Name: Optional[str]
    NetworkSecurityGroupId: Optional[str]
    Primary: Optional[bool]
    DnsSettings: Optional[Sequence["_DnsSettings"]]
    IpConfiguration: Optional[Sequence["_IpConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkProfile"]:
        if not json_data:
            return None
        return cls(
            AcceleratedNetworking=json_data.get("AcceleratedNetworking"),
            IpForwarding=json_data.get("IpForwarding"),
            Name=json_data.get("Name"),
            NetworkSecurityGroupId=json_data.get("NetworkSecurityGroupId"),
            Primary=json_data.get("Primary"),
            DnsSettings=json_data.get("DnsSettings"),
            IpConfiguration=json_data.get("IpConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkProfile = NetworkProfile


@dataclass
class DnsSettings:
    DnsServers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsSettings"]:
        if not json_data:
            return None
        return cls(
            DnsServers=json_data.get("DnsServers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsSettings = DnsSettings


@dataclass
class IpConfiguration:
    ApplicationGatewayBackendAddressPoolIds: Optional[Sequence[str]]
    ApplicationSecurityGroupIds: Optional[Sequence[str]]
    LoadBalancerBackendAddressPoolIds: Optional[Sequence[str]]
    LoadBalancerInboundNatRulesIds: Optional[Sequence[str]]
    Name: Optional[str]
    Primary: Optional[bool]
    SubnetId: Optional[str]
    PublicIpAddressConfiguration: Optional[Sequence["_PublicIpAddressConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpConfiguration"]:
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
            PublicIpAddressConfiguration=json_data.get("PublicIpAddressConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpConfiguration = IpConfiguration


@dataclass
class PublicIpAddressConfiguration:
    DomainNameLabel: Optional[str]
    IdleTimeout: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicIpAddressConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicIpAddressConfiguration"]:
        if not json_data:
            return None
        return cls(
            DomainNameLabel=json_data.get("DomainNameLabel"),
            IdleTimeout=json_data.get("IdleTimeout"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicIpAddressConfiguration = PublicIpAddressConfiguration


@dataclass
class OsProfile:
    AdminPassword: Optional[str]
    AdminUsername: Optional[str]
    ComputerNamePrefix: Optional[str]
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
            ComputerNamePrefix=json_data.get("ComputerNamePrefix"),
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
class RollingUpgradePolicy:
    MaxBatchInstancePercent: Optional[float]
    MaxUnhealthyInstancePercent: Optional[float]
    MaxUnhealthyUpgradedInstancePercent: Optional[float]
    PauseTimeBetweenBatches: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RollingUpgradePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RollingUpgradePolicy"]:
        if not json_data:
            return None
        return cls(
            MaxBatchInstancePercent=json_data.get("MaxBatchInstancePercent"),
            MaxUnhealthyInstancePercent=json_data.get("MaxUnhealthyInstancePercent"),
            MaxUnhealthyUpgradedInstancePercent=json_data.get("MaxUnhealthyUpgradedInstancePercent"),
            PauseTimeBetweenBatches=json_data.get("PauseTimeBetweenBatches"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RollingUpgradePolicy = RollingUpgradePolicy


@dataclass
class Sku:
    Capacity: Optional[float]
    Name: Optional[str]
    Tier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Sku"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sku"]:
        if not json_data:
            return None
        return cls(
            Capacity=json_data.get("Capacity"),
            Name=json_data.get("Name"),
            Tier=json_data.get("Tier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sku = Sku


@dataclass
class StorageProfileDataDisk:
    Caching: Optional[str]
    CreateOption: Optional[str]
    DiskSizeGb: Optional[float]
    Lun: Optional[float]
    ManagedDiskType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageProfileDataDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageProfileDataDisk"]:
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
_StorageProfileDataDisk = StorageProfileDataDisk


@dataclass
class StorageProfileImageReference:
    Id: Optional[str]
    Offer: Optional[str]
    Publisher: Optional[str]
    Sku: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageProfileImageReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageProfileImageReference"]:
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
_StorageProfileImageReference = StorageProfileImageReference


@dataclass
class StorageProfileOsDisk:
    Caching: Optional[str]
    CreateOption: Optional[str]
    Image: Optional[str]
    ManagedDiskType: Optional[str]
    Name: Optional[str]
    OsType: Optional[str]
    VhdContainers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_StorageProfileOsDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageProfileOsDisk"]:
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
_StorageProfileOsDisk = StorageProfileOsDisk


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


