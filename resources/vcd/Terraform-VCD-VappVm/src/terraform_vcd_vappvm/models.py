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
    AcceptAllEulas: Optional[bool]
    CatalogName: Optional[str]
    ComputerName: Optional[str]
    CpuCores: Optional[float]
    Cpus: Optional[float]
    Description: Optional[str]
    ExposeHardwareVirtualization: Optional[bool]
    GuestProperties: Optional[Sequence["_GuestProperties"]]
    Href: Optional[str]
    Id: Optional[str]
    Initscript: Optional[str]
    InternalDisk: Optional[Sequence["_InternalDisk"]]
    Ip: Optional[str]
    Mac: Optional[str]
    Memory: Optional[float]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    NetworkDhcpWaitSeconds: Optional[float]
    NetworkHref: Optional[str]
    NetworkName: Optional[str]
    Org: Optional[str]
    PowerOn: Optional[bool]
    StorageProfile: Optional[str]
    TemplateName: Optional[str]
    VappName: Optional[str]
    VappNetworkName: Optional[str]
    Vdc: Optional[str]
    Customization: Optional[Sequence["_Customization"]]
    Disk: Optional[Sequence["_Disk"]]
    Network: Optional[Sequence["_Network"]]
    OverrideTemplateDisk: Optional[Sequence["_OverrideTemplateDisk"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AcceptAllEulas=json_data.get("AcceptAllEulas"),
            CatalogName=json_data.get("CatalogName"),
            ComputerName=json_data.get("ComputerName"),
            CpuCores=json_data.get("CpuCores"),
            Cpus=json_data.get("Cpus"),
            Description=json_data.get("Description"),
            ExposeHardwareVirtualization=json_data.get("ExposeHardwareVirtualization"),
            GuestProperties=json_data.get("GuestProperties"),
            Href=json_data.get("Href"),
            Id=json_data.get("Id"),
            Initscript=json_data.get("Initscript"),
            InternalDisk=json_data.get("InternalDisk"),
            Ip=json_data.get("Ip"),
            Mac=json_data.get("Mac"),
            Memory=json_data.get("Memory"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            NetworkDhcpWaitSeconds=json_data.get("NetworkDhcpWaitSeconds"),
            NetworkHref=json_data.get("NetworkHref"),
            NetworkName=json_data.get("NetworkName"),
            Org=json_data.get("Org"),
            PowerOn=json_data.get("PowerOn"),
            StorageProfile=json_data.get("StorageProfile"),
            TemplateName=json_data.get("TemplateName"),
            VappName=json_data.get("VappName"),
            VappNetworkName=json_data.get("VappNetworkName"),
            Vdc=json_data.get("Vdc"),
            Customization=json_data.get("Customization"),
            Disk=json_data.get("Disk"),
            Network=json_data.get("Network"),
            OverrideTemplateDisk=json_data.get("OverrideTemplateDisk"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GuestProperties:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestProperties"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestProperties = GuestProperties


@dataclass
class InternalDisk:
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
        cls: Type["_InternalDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternalDisk"]:
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
_InternalDisk = InternalDisk


@dataclass
class Metadata:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class Customization:
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
        cls: Type["_Customization"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Customization"]:
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
_Customization = Customization


@dataclass
class Disk:
    BusNumber: Optional[str]
    Name: Optional[str]
    UnitNumber: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Disk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Disk"]:
        if not json_data:
            return None
        return cls(
            BusNumber=json_data.get("BusNumber"),
            Name=json_data.get("Name"),
            UnitNumber=json_data.get("UnitNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Disk = Disk


@dataclass
class Network:
    AdapterType: Optional[str]
    Ip: Optional[str]
    IpAllocationMode: Optional[str]
    IsPrimary: Optional[bool]
    Mac: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Network"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Network"]:
        if not json_data:
            return None
        return cls(
            AdapterType=json_data.get("AdapterType"),
            Ip=json_data.get("Ip"),
            IpAllocationMode=json_data.get("IpAllocationMode"),
            IsPrimary=json_data.get("IsPrimary"),
            Mac=json_data.get("Mac"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Network = Network


@dataclass
class OverrideTemplateDisk:
    BusNumber: Optional[float]
    BusType: Optional[str]
    Iops: Optional[float]
    SizeInMb: Optional[float]
    StorageProfile: Optional[str]
    UnitNumber: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OverrideTemplateDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverrideTemplateDisk"]:
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
_OverrideTemplateDisk = OverrideTemplateDisk


