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
    AccessPolicy: Optional[Sequence["_AccessPolicyDefinition"]]
    EnableRbacAuthorization: Optional[bool]
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
    SoftDeleteRetentionDays: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TenantId: Optional[str]
    VaultUri: Optional[str]
    Contact: Optional[Sequence["_ContactDefinition"]]
    NetworkAcls: Optional[Sequence["_NetworkAclsDefinition"]]
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
            AccessPolicy=deserialize_list(json_data.get("AccessPolicy"), AccessPolicyDefinition),
            EnableRbacAuthorization=json_data.get("EnableRbacAuthorization"),
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
            SoftDeleteRetentionDays=json_data.get("SoftDeleteRetentionDays"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TenantId=json_data.get("TenantId"),
            VaultUri=json_data.get("VaultUri"),
            Contact=deserialize_list(json_data.get("Contact"), ContactDefinition),
            NetworkAcls=deserialize_list(json_data.get("NetworkAcls"), NetworkAclsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccessPolicyDefinition(BaseModel):
    ApplicationId: Optional[str]
    CertificatePermissions: Optional[Sequence[str]]
    KeyPermissions: Optional[Sequence[str]]
    ObjectId: Optional[str]
    SecretPermissions: Optional[Sequence[str]]
    StoragePermissions: Optional[Sequence[str]]
    TenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessPolicyDefinition"]:
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
_AccessPolicyDefinition = AccessPolicyDefinition


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
class ContactDefinition(BaseModel):
    Email: Optional[str]
    Name: Optional[str]
    Phone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContactDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContactDefinition"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            Name=json_data.get("Name"),
            Phone=json_data.get("Phone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContactDefinition = ContactDefinition


@dataclass
class NetworkAclsDefinition(BaseModel):
    Bypass: Optional[str]
    DefaultAction: Optional[str]
    IpRules: Optional[Sequence[str]]
    VirtualNetworkSubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkAclsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkAclsDefinition"]:
        if not json_data:
            return None
        return cls(
            Bypass=json_data.get("Bypass"),
            DefaultAction=json_data.get("DefaultAction"),
            IpRules=json_data.get("IpRules"),
            VirtualNetworkSubnetIds=json_data.get("VirtualNetworkSubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkAclsDefinition = NetworkAclsDefinition


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


