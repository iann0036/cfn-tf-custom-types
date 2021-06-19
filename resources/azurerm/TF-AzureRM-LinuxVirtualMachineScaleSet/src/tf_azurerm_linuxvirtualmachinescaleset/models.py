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
    AdminPassword: Optional[str]
    AdminUsername: Optional[str]
    ComputerNamePrefix: Optional[str]
    CustomData: Optional[str]
    DisablePasswordAuthentication: Optional[bool]
    DoNotRunExtensionsOnOverprovisionedMachines: Optional[bool]
    EncryptionAtHostEnabled: Optional[bool]
    EvictionPolicy: Optional[str]
    ExtensionsTimeBudget: Optional[str]
    HealthProbeId: Optional[str]
    Id: Optional[str]
    Instances: Optional[float]
    Location: Optional[str]
    MaxBidPrice: Optional[float]
    Name: Optional[str]
    Overprovision: Optional[bool]
    PlatformFaultDomainCount: Optional[float]
    Priority: Optional[str]
    ProvisionVmAgent: Optional[bool]
    ProximityPlacementGroupId: Optional[str]
    ResourceGroupName: Optional[str]
    ScaleInPolicy: Optional[str]
    SinglePlacementGroup: Optional[bool]
    Sku: Optional[str]
    SourceImageId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    UniqueId: Optional[str]
    UpgradeMode: Optional[str]
    ZoneBalance: Optional[bool]
    Zones: Optional[Sequence[str]]
    AdditionalCapabilities: Optional[Sequence["_AdditionalCapabilitiesDefinition"]]
    AdminSshKey: Optional[Sequence["_AdminSshKeyDefinition"]]
    AutomaticInstanceRepair: Optional[Sequence["_AutomaticInstanceRepairDefinition"]]
    AutomaticOsUpgradePolicy: Optional[Sequence["_AutomaticOsUpgradePolicyDefinition"]]
    BootDiagnostics: Optional[Sequence["_BootDiagnosticsDefinition"]]
    DataDisk: Optional[Sequence["_DataDiskDefinition"]]
    Extension: Optional[Sequence["_ExtensionDefinition"]]
    Identity: Optional[Sequence["_IdentityDefinition"]]
    NetworkInterface: Optional[Sequence["_NetworkInterfaceDefinition"]]
    OsDisk: Optional[Sequence["_OsDiskDefinition"]]
    Plan: Optional[Sequence["_PlanDefinition"]]
    RollingUpgradePolicy: Optional[Sequence["_RollingUpgradePolicyDefinition"]]
    Secret: Optional[Sequence["_SecretDefinition"]]
    SourceImageReference: Optional[Sequence["_SourceImageReferenceDefinition"]]
    TerminateNotification: Optional[Sequence["_TerminateNotificationDefinition"]]
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
            AdminPassword=json_data.get("AdminPassword"),
            AdminUsername=json_data.get("AdminUsername"),
            ComputerNamePrefix=json_data.get("ComputerNamePrefix"),
            CustomData=json_data.get("CustomData"),
            DisablePasswordAuthentication=json_data.get("DisablePasswordAuthentication"),
            DoNotRunExtensionsOnOverprovisionedMachines=json_data.get("DoNotRunExtensionsOnOverprovisionedMachines"),
            EncryptionAtHostEnabled=json_data.get("EncryptionAtHostEnabled"),
            EvictionPolicy=json_data.get("EvictionPolicy"),
            ExtensionsTimeBudget=json_data.get("ExtensionsTimeBudget"),
            HealthProbeId=json_data.get("HealthProbeId"),
            Id=json_data.get("Id"),
            Instances=json_data.get("Instances"),
            Location=json_data.get("Location"),
            MaxBidPrice=json_data.get("MaxBidPrice"),
            Name=json_data.get("Name"),
            Overprovision=json_data.get("Overprovision"),
            PlatformFaultDomainCount=json_data.get("PlatformFaultDomainCount"),
            Priority=json_data.get("Priority"),
            ProvisionVmAgent=json_data.get("ProvisionVmAgent"),
            ProximityPlacementGroupId=json_data.get("ProximityPlacementGroupId"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ScaleInPolicy=json_data.get("ScaleInPolicy"),
            SinglePlacementGroup=json_data.get("SinglePlacementGroup"),
            Sku=json_data.get("Sku"),
            SourceImageId=json_data.get("SourceImageId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            UniqueId=json_data.get("UniqueId"),
            UpgradeMode=json_data.get("UpgradeMode"),
            ZoneBalance=json_data.get("ZoneBalance"),
            Zones=json_data.get("Zones"),
            AdditionalCapabilities=deserialize_list(json_data.get("AdditionalCapabilities"), AdditionalCapabilitiesDefinition),
            AdminSshKey=deserialize_list(json_data.get("AdminSshKey"), AdminSshKeyDefinition),
            AutomaticInstanceRepair=deserialize_list(json_data.get("AutomaticInstanceRepair"), AutomaticInstanceRepairDefinition),
            AutomaticOsUpgradePolicy=deserialize_list(json_data.get("AutomaticOsUpgradePolicy"), AutomaticOsUpgradePolicyDefinition),
            BootDiagnostics=deserialize_list(json_data.get("BootDiagnostics"), BootDiagnosticsDefinition),
            DataDisk=deserialize_list(json_data.get("DataDisk"), DataDiskDefinition),
            Extension=deserialize_list(json_data.get("Extension"), ExtensionDefinition),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            NetworkInterface=deserialize_list(json_data.get("NetworkInterface"), NetworkInterfaceDefinition),
            OsDisk=deserialize_list(json_data.get("OsDisk"), OsDiskDefinition),
            Plan=deserialize_list(json_data.get("Plan"), PlanDefinition),
            RollingUpgradePolicy=deserialize_list(json_data.get("RollingUpgradePolicy"), RollingUpgradePolicyDefinition),
            Secret=deserialize_list(json_data.get("Secret"), SecretDefinition),
            SourceImageReference=deserialize_list(json_data.get("SourceImageReference"), SourceImageReferenceDefinition),
            TerminateNotification=deserialize_list(json_data.get("TerminateNotification"), TerminateNotificationDefinition),
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
class AdminSshKeyDefinition(BaseModel):
    PublicKey: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdminSshKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdminSshKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            PublicKey=json_data.get("PublicKey"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdminSshKeyDefinition = AdminSshKeyDefinition


@dataclass
class AutomaticInstanceRepairDefinition(BaseModel):
    Enabled: Optional[bool]
    GracePeriod: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutomaticInstanceRepairDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutomaticInstanceRepairDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            GracePeriod=json_data.get("GracePeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutomaticInstanceRepairDefinition = AutomaticInstanceRepairDefinition


@dataclass
class AutomaticOsUpgradePolicyDefinition(BaseModel):
    DisableAutomaticRollback: Optional[bool]
    EnableAutomaticOsUpgrade: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AutomaticOsUpgradePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutomaticOsUpgradePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableAutomaticRollback=json_data.get("DisableAutomaticRollback"),
            EnableAutomaticOsUpgrade=json_data.get("EnableAutomaticOsUpgrade"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutomaticOsUpgradePolicyDefinition = AutomaticOsUpgradePolicyDefinition


@dataclass
class BootDiagnosticsDefinition(BaseModel):
    StorageAccountUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BootDiagnosticsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BootDiagnosticsDefinition"]:
        if not json_data:
            return None
        return cls(
            StorageAccountUri=json_data.get("StorageAccountUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BootDiagnosticsDefinition = BootDiagnosticsDefinition


@dataclass
class DataDiskDefinition(BaseModel):
    Caching: Optional[str]
    CreateOption: Optional[str]
    DiskEncryptionSetId: Optional[str]
    DiskIopsReadWrite: Optional[float]
    DiskMbpsReadWrite: Optional[float]
    DiskSizeGb: Optional[float]
    Lun: Optional[float]
    StorageAccountType: Optional[str]
    WriteAcceleratorEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DataDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            Caching=json_data.get("Caching"),
            CreateOption=json_data.get("CreateOption"),
            DiskEncryptionSetId=json_data.get("DiskEncryptionSetId"),
            DiskIopsReadWrite=json_data.get("DiskIopsReadWrite"),
            DiskMbpsReadWrite=json_data.get("DiskMbpsReadWrite"),
            DiskSizeGb=json_data.get("DiskSizeGb"),
            Lun=json_data.get("Lun"),
            StorageAccountType=json_data.get("StorageAccountType"),
            WriteAcceleratorEnabled=json_data.get("WriteAcceleratorEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDiskDefinition = DataDiskDefinition


@dataclass
class ExtensionDefinition(BaseModel):
    AutoUpgradeMinorVersion: Optional[bool]
    ForceUpdateTag: Optional[str]
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
            ForceUpdateTag=json_data.get("ForceUpdateTag"),
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
class NetworkInterfaceDefinition(BaseModel):
    DnsServers: Optional[Sequence[str]]
    EnableAcceleratedNetworking: Optional[bool]
    EnableIpForwarding: Optional[bool]
    Name: Optional[str]
    NetworkSecurityGroupId: Optional[str]
    Primary: Optional[bool]
    IpConfiguration: Optional[Sequence["_IpConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsServers=json_data.get("DnsServers"),
            EnableAcceleratedNetworking=json_data.get("EnableAcceleratedNetworking"),
            EnableIpForwarding=json_data.get("EnableIpForwarding"),
            Name=json_data.get("Name"),
            NetworkSecurityGroupId=json_data.get("NetworkSecurityGroupId"),
            Primary=json_data.get("Primary"),
            IpConfiguration=deserialize_list(json_data.get("IpConfiguration"), IpConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfaceDefinition = NetworkInterfaceDefinition


@dataclass
class IpConfigurationDefinition(BaseModel):
    ApplicationGatewayBackendAddressPoolIds: Optional[Sequence[str]]
    ApplicationSecurityGroupIds: Optional[Sequence[str]]
    LoadBalancerBackendAddressPoolIds: Optional[Sequence[str]]
    LoadBalancerInboundNatRulesIds: Optional[Sequence[str]]
    Name: Optional[str]
    Primary: Optional[bool]
    SubnetId: Optional[str]
    Version: Optional[str]
    PublicIpAddress: Optional[Sequence["_PublicIpAddressDefinition"]]

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
            Version=json_data.get("Version"),
            PublicIpAddress=deserialize_list(json_data.get("PublicIpAddress"), PublicIpAddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpConfigurationDefinition = IpConfigurationDefinition


@dataclass
class PublicIpAddressDefinition(BaseModel):
    DomainNameLabel: Optional[str]
    IdleTimeoutInMinutes: Optional[float]
    Name: Optional[str]
    PublicIpPrefixId: Optional[str]
    IpTag: Optional[Sequence["_IpTagDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PublicIpAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicIpAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            DomainNameLabel=json_data.get("DomainNameLabel"),
            IdleTimeoutInMinutes=json_data.get("IdleTimeoutInMinutes"),
            Name=json_data.get("Name"),
            PublicIpPrefixId=json_data.get("PublicIpPrefixId"),
            IpTag=deserialize_list(json_data.get("IpTag"), IpTagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicIpAddressDefinition = PublicIpAddressDefinition


@dataclass
class IpTagDefinition(BaseModel):
    Tag: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpTagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpTagDefinition"]:
        if not json_data:
            return None
        return cls(
            Tag=json_data.get("Tag"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpTagDefinition = IpTagDefinition


@dataclass
class OsDiskDefinition(BaseModel):
    Caching: Optional[str]
    DiskEncryptionSetId: Optional[str]
    DiskSizeGb: Optional[float]
    StorageAccountType: Optional[str]
    WriteAcceleratorEnabled: Optional[bool]
    DiffDiskSettings: Optional[Sequence["_DiffDiskSettingsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OsDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            Caching=json_data.get("Caching"),
            DiskEncryptionSetId=json_data.get("DiskEncryptionSetId"),
            DiskSizeGb=json_data.get("DiskSizeGb"),
            StorageAccountType=json_data.get("StorageAccountType"),
            WriteAcceleratorEnabled=json_data.get("WriteAcceleratorEnabled"),
            DiffDiskSettings=deserialize_list(json_data.get("DiffDiskSettings"), DiffDiskSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsDiskDefinition = OsDiskDefinition


@dataclass
class DiffDiskSettingsDefinition(BaseModel):
    Option: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiffDiskSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiffDiskSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Option=json_data.get("Option"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiffDiskSettingsDefinition = DiffDiskSettingsDefinition


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
class SecretDefinition(BaseModel):
    KeyVaultId: Optional[str]
    Certificate: Optional[Sequence["_CertificateDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecretDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyVaultId=json_data.get("KeyVaultId"),
            Certificate=deserialize_list(json_data.get("Certificate"), CertificateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretDefinition = SecretDefinition


@dataclass
class CertificateDefinition(BaseModel):
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDefinition = CertificateDefinition


@dataclass
class SourceImageReferenceDefinition(BaseModel):
    Offer: Optional[str]
    Publisher: Optional[str]
    Sku: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceImageReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceImageReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Offer=json_data.get("Offer"),
            Publisher=json_data.get("Publisher"),
            Sku=json_data.get("Sku"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceImageReferenceDefinition = SourceImageReferenceDefinition


@dataclass
class TerminateNotificationDefinition(BaseModel):
    Enabled: Optional[bool]
    Timeout: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TerminateNotificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TerminateNotificationDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TerminateNotificationDefinition = TerminateNotificationDefinition


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


