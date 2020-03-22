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
    AccessPolicy: Optional[Sequence["_AccessPolicy"]]
    EnabledForDeployment: Optional[bool]
    EnabledForDiskEncryption: Optional[bool]
    EnabledForTemplateDeployment: Optional[bool]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PurgeProtectionEnabled: Optional[bool]
    ResourceGroupName: Optional[str]
    SkuName: Optional[str]
    SoftDeleteEnabled: Optional[bool]
    Tags: Optional[Sequence["_Tags"]]
    TenantId: Optional[str]
    VaultUri: Optional[str]
    NetworkAcls: Optional[Sequence["_NetworkAcls"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccessPolicy=json_data.get("AccessPolicy"),
            EnabledForDeployment=json_data.get("EnabledForDeployment"),
            EnabledForDiskEncryption=json_data.get("EnabledForDiskEncryption"),
            EnabledForTemplateDeployment=json_data.get("EnabledForTemplateDeployment"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PurgeProtectionEnabled=json_data.get("PurgeProtectionEnabled"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SkuName=json_data.get("SkuName"),
            SoftDeleteEnabled=json_data.get("SoftDeleteEnabled"),
            Tags=json_data.get("Tags"),
            TenantId=json_data.get("TenantId"),
            VaultUri=json_data.get("VaultUri"),
            NetworkAcls=json_data.get("NetworkAcls"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccessPolicy:
    ApplicationId: Optional[str]
    CertificatePermissions: Optional[Sequence[str]]
    KeyPermissions: Optional[Sequence[str]]
    ObjectId: Optional[str]
    SecretPermissions: Optional[Sequence[str]]
    StoragePermissions: Optional[Sequence[str]]
    TenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessPolicy"]:
        if not json_data:
            return None
        return cls(
            ApplicationId=json_data.get("ApplicationId"),
            CertificatePermissions=json_data.get("CertificatePermissions"),
            KeyPermissions=json_data.get("KeyPermissions"),
            ObjectId=json_data.get("ObjectId"),
            SecretPermissions=json_data.get("SecretPermissions"),
            StoragePermissions=json_data.get("StoragePermissions"),
            TenantId=json_data.get("TenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessPolicy = AccessPolicy


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
class NetworkAcls:
    Bypass: Optional[str]
    DefaultAction: Optional[str]
    IpRules: Optional[Sequence[str]]
    VirtualNetworkSubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkAcls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkAcls"]:
        if not json_data:
            return None
        return cls(
            Bypass=json_data.get("Bypass"),
            DefaultAction=json_data.get("DefaultAction"),
            IpRules=json_data.get("IpRules"),
            VirtualNetworkSubnetIds=json_data.get("VirtualNetworkSubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkAcls = NetworkAcls


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


