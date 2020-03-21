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
    AllowExtensionOperations: Optional[bool]
    AvailabilitySetId: Optional[str]
    ComputerName: Optional[str]
    CustomData: Optional[str]
    DedicatedHostId: Optional[str]
    DisablePasswordAuthentication: Optional[bool]
    EvictionPolicy: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    MaxBidPrice: Optional[float]
    Name: Optional[str]
    NetworkInterfaceIds: Optional[Sequence[str]]
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
    Tags: Optional[Sequence["_Tags"]]
    VirtualMachineId: Optional[str]
    Zone: Optional[str]
    AdditionalCapabilities: Optional[Sequence["_AdditionalCapabilities"]]
    AdminSshKey: Optional[Sequence["_AdminSshKey"]]
    BootDiagnostics: Optional[Sequence["_BootDiagnostics"]]
    Identity: Optional[Sequence["_Identity"]]
    OsDisk: Optional[Sequence["_OsDisk"]]
    Plan: Optional[Sequence["_Plan"]]
    Secret: Optional[Sequence["_Secret"]]
    SourceImageReference: Optional[Sequence["_SourceImageReference"]]
    Timeouts: Optional["_Timeouts"]
    DiffDiskSettings: Optional[Sequence["_DiffDiskSettings"]]
    Certificate: Optional[Sequence["_Certificate"]]

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
            AllowExtensionOperations=json_data.get("AllowExtensionOperations"),
            AvailabilitySetId=json_data.get("AvailabilitySetId"),
            ComputerName=json_data.get("ComputerName"),
            CustomData=json_data.get("CustomData"),
            DedicatedHostId=json_data.get("DedicatedHostId"),
            DisablePasswordAuthentication=json_data.get("DisablePasswordAuthentication"),
            EvictionPolicy=json_data.get("EvictionPolicy"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            MaxBidPrice=json_data.get("MaxBidPrice"),
            Name=json_data.get("Name"),
            NetworkInterfaceIds=json_data.get("NetworkInterfaceIds"),
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
            Tags=json_data.get("Tags"),
            VirtualMachineId=json_data.get("VirtualMachineId"),
            Zone=json_data.get("Zone"),
            AdditionalCapabilities=json_data.get("AdditionalCapabilities"),
            AdminSshKey=json_data.get("AdminSshKey"),
            BootDiagnostics=json_data.get("BootDiagnostics"),
            Identity=json_data.get("Identity"),
            OsDisk=json_data.get("OsDisk"),
            Plan=json_data.get("Plan"),
            Secret=json_data.get("Secret"),
            SourceImageReference=json_data.get("SourceImageReference"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            DiffDiskSettings=json_data.get("DiffDiskSettings"),
            Certificate=json_data.get("Certificate"),
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
class AdminSshKey:
    PublicKey: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdminSshKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdminSshKey"]:
        if not json_data:
            return None
        return cls(
            PublicKey=json_data.get("PublicKey"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdminSshKey = AdminSshKey


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
class OsDisk:
    Caching: Optional[str]
    DiskEncryptionSetId: Optional[str]
    DiskSizeGb: Optional[float]
    Name: Optional[str]
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
            Name=json_data.get("Name"),
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
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Certificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Certificate"]:
        if not json_data:
            return None
        return cls(
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


