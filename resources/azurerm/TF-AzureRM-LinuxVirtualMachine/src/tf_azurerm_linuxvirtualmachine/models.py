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
    AllowExtensionOperations: Optional[bool]
    AvailabilitySetId: Optional[str]
    ComputerName: Optional[str]
    CustomData: Optional[str]
    DedicatedHostId: Optional[str]
    DisablePasswordAuthentication: Optional[bool]
    EncryptionAtHostEnabled: Optional[bool]
    EvictionPolicy: Optional[str]
    ExtensionsTimeBudget: Optional[str]
    Id: Optional[str]
    LicenseType: Optional[str]
    Location: Optional[str]
    MaxBidPrice: Optional[float]
    Name: Optional[str]
    NetworkInterfaceIds: Optional[Sequence[str]]
    PlatformFaultDomain: Optional[float]
    Priority: Optional[str]
    PrivateIpAddress: Optional[str]
    PrivateIpAddresses: Optional[Sequence[str]]
    ProvisionVmAgent: Optional[bool]
    ProximityPlacementGroupId: Optional[str]
    PublicIpAddress: Optional[str]
    PublicIpAddresses: Optional[Sequence[str]]
    ResourceGroupName: Optional[str]
    Size: Optional[str]
    SourceImageId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VirtualMachineId: Optional[str]
    VirtualMachineScaleSetId: Optional[str]
    Zone: Optional[str]
    AdditionalCapabilities: Optional[Sequence["_AdditionalCapabilitiesDefinition"]]
    AdminSshKey: Optional[Sequence["_AdminSshKeyDefinition"]]
    BootDiagnostics: Optional[Sequence["_BootDiagnosticsDefinition"]]
    Identity: Optional[Sequence["_IdentityDefinition"]]
    OsDisk: Optional[Sequence["_OsDiskDefinition"]]
    Plan: Optional[Sequence["_PlanDefinition"]]
    Secret: Optional[Sequence["_SecretDefinition"]]
    SourceImageReference: Optional[Sequence["_SourceImageReferenceDefinition"]]
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
            AllowExtensionOperations=json_data.get("AllowExtensionOperations"),
            AvailabilitySetId=json_data.get("AvailabilitySetId"),
            ComputerName=json_data.get("ComputerName"),
            CustomData=json_data.get("CustomData"),
            DedicatedHostId=json_data.get("DedicatedHostId"),
            DisablePasswordAuthentication=json_data.get("DisablePasswordAuthentication"),
            EncryptionAtHostEnabled=json_data.get("EncryptionAtHostEnabled"),
            EvictionPolicy=json_data.get("EvictionPolicy"),
            ExtensionsTimeBudget=json_data.get("ExtensionsTimeBudget"),
            Id=json_data.get("Id"),
            LicenseType=json_data.get("LicenseType"),
            Location=json_data.get("Location"),
            MaxBidPrice=json_data.get("MaxBidPrice"),
            Name=json_data.get("Name"),
            NetworkInterfaceIds=json_data.get("NetworkInterfaceIds"),
            PlatformFaultDomain=json_data.get("PlatformFaultDomain"),
            Priority=json_data.get("Priority"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            PrivateIpAddresses=json_data.get("PrivateIpAddresses"),
            ProvisionVmAgent=json_data.get("ProvisionVmAgent"),
            ProximityPlacementGroupId=json_data.get("ProximityPlacementGroupId"),
            PublicIpAddress=json_data.get("PublicIpAddress"),
            PublicIpAddresses=json_data.get("PublicIpAddresses"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Size=json_data.get("Size"),
            SourceImageId=json_data.get("SourceImageId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VirtualMachineId=json_data.get("VirtualMachineId"),
            VirtualMachineScaleSetId=json_data.get("VirtualMachineScaleSetId"),
            Zone=json_data.get("Zone"),
            AdditionalCapabilities=deserialize_list(json_data.get("AdditionalCapabilities"), AdditionalCapabilitiesDefinition),
            AdminSshKey=deserialize_list(json_data.get("AdminSshKey"), AdminSshKeyDefinition),
            BootDiagnostics=deserialize_list(json_data.get("BootDiagnostics"), BootDiagnosticsDefinition),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            OsDisk=deserialize_list(json_data.get("OsDisk"), OsDiskDefinition),
            Plan=deserialize_list(json_data.get("Plan"), PlanDefinition),
            Secret=deserialize_list(json_data.get("Secret"), SecretDefinition),
            SourceImageReference=deserialize_list(json_data.get("SourceImageReference"), SourceImageReferenceDefinition),
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
class OsDiskDefinition(BaseModel):
    Caching: Optional[str]
    DiskEncryptionSetId: Optional[str]
    DiskSizeGb: Optional[float]
    Name: Optional[str]
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
            Name=json_data.get("Name"),
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


