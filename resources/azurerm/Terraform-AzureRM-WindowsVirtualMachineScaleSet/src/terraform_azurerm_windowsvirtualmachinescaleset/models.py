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
    AdminPassword: Optional[str]
    AdminUsername: Optional[str]
    ComputerNamePrefix: Optional[str]
    CustomData: Optional[str]
    DoNotRunExtensionsOnOverprovisionedMachines: Optional[bool]
    EnableAutomaticUpdates: Optional[bool]
    EvictionPolicy: Optional[str]
    HealthProbeId: Optional[str]
    Id: Optional[str]
    Instances: Optional[float]
    LicenseType: Optional[str]
    Location: Optional[str]
    MaxBidPrice: Optional[float]
    Name: Optional[str]
    Overprovision: Optional[bool]
    Priority: Optional[str]
    ProvisionVmAgent: Optional[bool]
    ProximityPlacementGroupId: Optional[str]
    ResourceGroupName: Optional[str]
    ScaleInPolicy: Optional[str]
    SinglePlacementGroup: Optional[bool]
    Sku: Optional[str]
    SourceImageId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Timezone: Optional[str]
    UniqueId: Optional[str]
    UpgradeMode: Optional[str]
    ZoneBalance: Optional[bool]
    Zones: Optional[Sequence[str]]
    AdditionalCapabilities: Optional[Sequence["_AdditionalCapabilities"]]
    AdditionalUnattendContent: Optional[Sequence["_AdditionalUnattendContent"]]
    AutomaticOsUpgradePolicy: Optional[Sequence["_AutomaticOsUpgradePolicy"]]
    BootDiagnostics: Optional[Sequence["_BootDiagnostics"]]
    DataDisk: Optional[Sequence["_DataDisk"]]
    Identity: Optional[Sequence["_Identity"]]
    NetworkInterface: Optional[Sequence["_NetworkInterface"]]
    OsDisk: Optional[Sequence["_OsDisk"]]
    Plan: Optional[Sequence["_Plan"]]
    RollingUpgradePolicy: Optional[Sequence["_RollingUpgradePolicy"]]
    Secret: Optional[Sequence["_Secret"]]
    SourceImageReference: Optional[Sequence["_SourceImageReference"]]
    TerminateNotification: Optional[Sequence["_TerminateNotification"]]
    Timeouts: Optional["_Timeouts"]
    WinrmListener: Optional[Sequence["_WinrmListener"]]
    IpConfiguration: Optional[Sequence["_IpConfiguration"]]
    DiffDiskSettings: Optional[Sequence["_DiffDiskSettings"]]
    Certificate: Optional[Sequence["_Certificate"]]
    PublicIpAddress: Optional[Sequence["_PublicIpAddress"]]
    IpTag: Optional[Sequence["_IpTag"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdminPassword=json_data.get("AdminPassword"),
            AdminUsername=json_data.get("AdminUsername"),
            ComputerNamePrefix=json_data.get("ComputerNamePrefix"),
            CustomData=json_data.get("CustomData"),
            DoNotRunExtensionsOnOverprovisionedMachines=json_data.get("DoNotRunExtensionsOnOverprovisionedMachines"),
            EnableAutomaticUpdates=json_data.get("EnableAutomaticUpdates"),
            EvictionPolicy=json_data.get("EvictionPolicy"),
            HealthProbeId=json_data.get("HealthProbeId"),
            Id=json_data.get("Id"),
            Instances=json_data.get("Instances"),
            LicenseType=json_data.get("LicenseType"),
            Location=json_data.get("Location"),
            MaxBidPrice=json_data.get("MaxBidPrice"),
            Name=json_data.get("Name"),
            Overprovision=json_data.get("Overprovision"),
            Priority=json_data.get("Priority"),
            ProvisionVmAgent=json_data.get("ProvisionVmAgent"),
            ProximityPlacementGroupId=json_data.get("ProximityPlacementGroupId"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ScaleInPolicy=json_data.get("ScaleInPolicy"),
            SinglePlacementGroup=json_data.get("SinglePlacementGroup"),
            Sku=json_data.get("Sku"),
            SourceImageId=json_data.get("SourceImageId"),
            Tags=json_data.get("Tags"),
            Timezone=json_data.get("Timezone"),
            UniqueId=json_data.get("UniqueId"),
            UpgradeMode=json_data.get("UpgradeMode"),
            ZoneBalance=json_data.get("ZoneBalance"),
            Zones=json_data.get("Zones"),
            AdditionalCapabilities=json_data.get("AdditionalCapabilities"),
            AdditionalUnattendContent=json_data.get("AdditionalUnattendContent"),
            AutomaticOsUpgradePolicy=json_data.get("AutomaticOsUpgradePolicy"),
            BootDiagnostics=json_data.get("BootDiagnostics"),
            DataDisk=json_data.get("DataDisk"),
            Identity=json_data.get("Identity"),
            NetworkInterface=json_data.get("NetworkInterface"),
            OsDisk=json_data.get("OsDisk"),
            Plan=json_data.get("Plan"),
            RollingUpgradePolicy=json_data.get("RollingUpgradePolicy"),
            Secret=json_data.get("Secret"),
            SourceImageReference=json_data.get("SourceImageReference"),
            TerminateNotification=json_data.get("TerminateNotification"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            WinrmListener=json_data.get("WinrmListener"),
            IpConfiguration=json_data.get("IpConfiguration"),
            DiffDiskSettings=json_data.get("DiffDiskSettings"),
            Certificate=json_data.get("Certificate"),
            PublicIpAddress=json_data.get("PublicIpAddress"),
            IpTag=json_data.get("IpTag"),
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
class AdditionalUnattendContent:
    Content: Optional[str]
    Setting: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalUnattendContent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalUnattendContent"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Setting=json_data.get("Setting"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalUnattendContent = AdditionalUnattendContent


@dataclass
class AutomaticOsUpgradePolicy:
    DisableAutomaticRollback: Optional[bool]
    EnableAutomaticOsUpgrade: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AutomaticOsUpgradePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutomaticOsUpgradePolicy"]:
        if not json_data:
            return None
        return cls(
            DisableAutomaticRollback=json_data.get("DisableAutomaticRollback"),
            EnableAutomaticOsUpgrade=json_data.get("EnableAutomaticOsUpgrade"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutomaticOsUpgradePolicy = AutomaticOsUpgradePolicy


@dataclass
class BootDiagnostics:
    StorageAccountUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BootDiagnostics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BootDiagnostics"]:
        if not json_data:
            return None
        return cls(
            StorageAccountUri=json_data.get("StorageAccountUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BootDiagnostics = BootDiagnostics


@dataclass
class DataDisk:
    Caching: Optional[str]
    DiskEncryptionSetId: Optional[str]
    DiskSizeGb: Optional[float]
    Lun: Optional[float]
    StorageAccountType: Optional[str]
    WriteAcceleratorEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DataDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDisk"]:
        if not json_data:
            return None
        return cls(
            Caching=json_data.get("Caching"),
            DiskEncryptionSetId=json_data.get("DiskEncryptionSetId"),
            DiskSizeGb=json_data.get("DiskSizeGb"),
            Lun=json_data.get("Lun"),
            StorageAccountType=json_data.get("StorageAccountType"),
            WriteAcceleratorEnabled=json_data.get("WriteAcceleratorEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDisk = DataDisk


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
class NetworkInterface:
    DnsServers: Optional[Sequence[str]]
    EnableAcceleratedNetworking: Optional[bool]
    EnableIpForwarding: Optional[bool]
    Name: Optional[str]
    NetworkSecurityGroupId: Optional[str]
    Primary: Optional[bool]
    IpConfiguration: Optional[Sequence["_IpConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterface"]:
        if not json_data:
            return None
        return cls(
            DnsServers=json_data.get("DnsServers"),
            EnableAcceleratedNetworking=json_data.get("EnableAcceleratedNetworking"),
            EnableIpForwarding=json_data.get("EnableIpForwarding"),
            Name=json_data.get("Name"),
            NetworkSecurityGroupId=json_data.get("NetworkSecurityGroupId"),
            Primary=json_data.get("Primary"),
            IpConfiguration=json_data.get("IpConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterface = NetworkInterface


@dataclass
class IpConfiguration:
    ApplicationGatewayBackendAddressPoolIds: Optional[Sequence[str]]
    ApplicationSecurityGroupIds: Optional[Sequence[str]]
    LoadBalancerBackendAddressPoolIds: Optional[Sequence[str]]
    LoadBalancerInboundNatRulesIds: Optional[Sequence[str]]
    Name: Optional[str]
    Primary: Optional[bool]
    SubnetId: Optional[str]
    Version: Optional[str]
    PublicIpAddress: Optional[Sequence["_PublicIpAddress"]]

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
            Version=json_data.get("Version"),
            PublicIpAddress=json_data.get("PublicIpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpConfiguration = IpConfiguration


@dataclass
class PublicIpAddress:
    DomainNameLabel: Optional[str]
    IdleTimeoutInMinutes: Optional[float]
    Name: Optional[str]
    PublicIpPrefixId: Optional[str]
    IpTag: Optional[Sequence["_IpTag"]]

    @classmethod
    def _deserialize(
        cls: Type["_PublicIpAddress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicIpAddress"]:
        if not json_data:
            return None
        return cls(
            DomainNameLabel=json_data.get("DomainNameLabel"),
            IdleTimeoutInMinutes=json_data.get("IdleTimeoutInMinutes"),
            Name=json_data.get("Name"),
            PublicIpPrefixId=json_data.get("PublicIpPrefixId"),
            IpTag=json_data.get("IpTag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicIpAddress = PublicIpAddress


@dataclass
class IpTag:
    Tag: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpTag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpTag"]:
        if not json_data:
            return None
        return cls(
            Tag=json_data.get("Tag"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpTag = IpTag


@dataclass
class OsDisk:
    Caching: Optional[str]
    DiskEncryptionSetId: Optional[str]
    DiskSizeGb: Optional[float]
    StorageAccountType: Optional[str]
    WriteAcceleratorEnabled: Optional[bool]
    DiffDiskSettings: Optional[Sequence["_DiffDiskSettings"]]

    @classmethod
    def _deserialize(
        cls: Type["_OsDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsDisk"]:
        if not json_data:
            return None
        return cls(
            Caching=json_data.get("Caching"),
            DiskEncryptionSetId=json_data.get("DiskEncryptionSetId"),
            DiskSizeGb=json_data.get("DiskSizeGb"),
            StorageAccountType=json_data.get("StorageAccountType"),
            WriteAcceleratorEnabled=json_data.get("WriteAcceleratorEnabled"),
            DiffDiskSettings=json_data.get("DiffDiskSettings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsDisk = OsDisk


@dataclass
class DiffDiskSettings:
    Option: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiffDiskSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiffDiskSettings"]:
        if not json_data:
            return None
        return cls(
            Option=json_data.get("Option"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiffDiskSettings = DiffDiskSettings


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
class Secret:
    KeyVaultId: Optional[str]
    Certificate: Optional[Sequence["_Certificate"]]

    @classmethod
    def _deserialize(
        cls: Type["_Secret"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Secret"]:
        if not json_data:
            return None
        return cls(
            KeyVaultId=json_data.get("KeyVaultId"),
            Certificate=json_data.get("Certificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Secret = Secret


@dataclass
class Certificate:
    Store: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Certificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Certificate"]:
        if not json_data:
            return None
        return cls(
            Store=json_data.get("Store"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Certificate = Certificate


@dataclass
class SourceImageReference:
    Offer: Optional[str]
    Publisher: Optional[str]
    Sku: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceImageReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceImageReference"]:
        if not json_data:
            return None
        return cls(
            Offer=json_data.get("Offer"),
            Publisher=json_data.get("Publisher"),
            Sku=json_data.get("Sku"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceImageReference = SourceImageReference


@dataclass
class TerminateNotification:
    Enabled: Optional[bool]
    Timeout: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TerminateNotification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TerminateNotification"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TerminateNotification = TerminateNotification


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


@dataclass
class WinrmListener:
    CertificateUrl: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WinrmListener"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WinrmListener"]:
        if not json_data:
            return None
        return cls(
            CertificateUrl=json_data.get("CertificateUrl"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WinrmListener = WinrmListener


