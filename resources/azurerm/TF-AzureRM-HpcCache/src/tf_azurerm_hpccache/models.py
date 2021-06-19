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
    CacheSizeInGb: Optional[float]
    Id: Optional[str]
    Location: Optional[str]
    MountAddresses: Optional[Sequence[str]]
    Mtu: Optional[float]
    Name: Optional[str]
    NtpServer: Optional[str]
    ResourceGroupName: Optional[str]
    RootSquashEnabled: Optional[bool]
    SkuName: Optional[str]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    DefaultAccessPolicy: Optional[Sequence["_DefaultAccessPolicyDefinition"]]
    DirectoryActiveDirectory: Optional[Sequence["_DirectoryActiveDirectoryDefinition"]]
    DirectoryFlatFile: Optional[Sequence["_DirectoryFlatFileDefinition"]]
    DirectoryLdap: Optional[Sequence["_DirectoryLdapDefinition"]]
    Dns: Optional[Sequence["_DnsDefinition"]]
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
            CacheSizeInGb=json_data.get("CacheSizeInGb"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            MountAddresses=json_data.get("MountAddresses"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            NtpServer=json_data.get("NtpServer"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RootSquashEnabled=json_data.get("RootSquashEnabled"),
            SkuName=json_data.get("SkuName"),
            SubnetId=json_data.get("SubnetId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            DefaultAccessPolicy=deserialize_list(json_data.get("DefaultAccessPolicy"), DefaultAccessPolicyDefinition),
            DirectoryActiveDirectory=deserialize_list(json_data.get("DirectoryActiveDirectory"), DirectoryActiveDirectoryDefinition),
            DirectoryFlatFile=deserialize_list(json_data.get("DirectoryFlatFile"), DirectoryFlatFileDefinition),
            DirectoryLdap=deserialize_list(json_data.get("DirectoryLdap"), DirectoryLdapDefinition),
            Dns=deserialize_list(json_data.get("Dns"), DnsDefinition),
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
class DefaultAccessPolicyDefinition(BaseModel):
    AccessRule: Optional[Sequence["_AccessRuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultAccessPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultAccessPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessRule=deserialize_list(json_data.get("AccessRule"), AccessRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultAccessPolicyDefinition = DefaultAccessPolicyDefinition


@dataclass
class AccessRuleDefinition(BaseModel):
    Access: Optional[str]
    AnonymousGid: Optional[float]
    AnonymousUid: Optional[float]
    Filter: Optional[str]
    RootSquashEnabled: Optional[bool]
    Scope: Optional[str]
    SubmountAccessEnabled: Optional[bool]
    SuidEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AccessRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Access=json_data.get("Access"),
            AnonymousGid=json_data.get("AnonymousGid"),
            AnonymousUid=json_data.get("AnonymousUid"),
            Filter=json_data.get("Filter"),
            RootSquashEnabled=json_data.get("RootSquashEnabled"),
            Scope=json_data.get("Scope"),
            SubmountAccessEnabled=json_data.get("SubmountAccessEnabled"),
            SuidEnabled=json_data.get("SuidEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessRuleDefinition = AccessRuleDefinition


@dataclass
class DirectoryActiveDirectoryDefinition(BaseModel):
    CacheNetbiosName: Optional[str]
    DnsPrimaryIp: Optional[str]
    DnsSecondaryIp: Optional[str]
    DomainName: Optional[str]
    DomainNetbiosName: Optional[str]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DirectoryActiveDirectoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DirectoryActiveDirectoryDefinition"]:
        if not json_data:
            return None
        return cls(
            CacheNetbiosName=json_data.get("CacheNetbiosName"),
            DnsPrimaryIp=json_data.get("DnsPrimaryIp"),
            DnsSecondaryIp=json_data.get("DnsSecondaryIp"),
            DomainName=json_data.get("DomainName"),
            DomainNetbiosName=json_data.get("DomainNetbiosName"),
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DirectoryActiveDirectoryDefinition = DirectoryActiveDirectoryDefinition


@dataclass
class DirectoryFlatFileDefinition(BaseModel):
    GroupFileUri: Optional[str]
    PasswordFileUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DirectoryFlatFileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DirectoryFlatFileDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupFileUri=json_data.get("GroupFileUri"),
            PasswordFileUri=json_data.get("PasswordFileUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DirectoryFlatFileDefinition = DirectoryFlatFileDefinition


@dataclass
class DirectoryLdapDefinition(BaseModel):
    BaseDn: Optional[str]
    CertificateValidationUri: Optional[str]
    DownloadCertificateAutomatically: Optional[bool]
    Encrypted: Optional[bool]
    Server: Optional[str]
    Bind: Optional[Sequence["_BindDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DirectoryLdapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DirectoryLdapDefinition"]:
        if not json_data:
            return None
        return cls(
            BaseDn=json_data.get("BaseDn"),
            CertificateValidationUri=json_data.get("CertificateValidationUri"),
            DownloadCertificateAutomatically=json_data.get("DownloadCertificateAutomatically"),
            Encrypted=json_data.get("Encrypted"),
            Server=json_data.get("Server"),
            Bind=deserialize_list(json_data.get("Bind"), BindDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DirectoryLdapDefinition = DirectoryLdapDefinition


@dataclass
class BindDefinition(BaseModel):
    Dn: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BindDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BindDefinition"]:
        if not json_data:
            return None
        return cls(
            Dn=json_data.get("Dn"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BindDefinition = BindDefinition


@dataclass
class DnsDefinition(BaseModel):
    SearchDomain: Optional[str]
    Servers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsDefinition"]:
        if not json_data:
            return None
        return cls(
            SearchDomain=json_data.get("SearchDomain"),
            Servers=json_data.get("Servers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsDefinition = DnsDefinition


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


