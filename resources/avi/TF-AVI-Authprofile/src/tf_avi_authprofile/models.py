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
    Description: Optional[str]
    Id: Optional[str]
    JwtProfileRef: Optional[str]
    Name: Optional[str]
    PaAgentRef: Optional[str]
    TenantRef: Optional[str]
    Type: Optional[str]
    Uuid: Optional[str]
    Http: Optional[Sequence["_HttpDefinition"]]
    Ldap: Optional[Sequence["_LdapDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    Saml: Optional[Sequence["_SamlDefinition"]]
    TacacsPlus: Optional[Sequence["_TacacsPlusDefinition"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            JwtProfileRef=json_data.get("JwtProfileRef"),
            Name=json_data.get("Name"),
            PaAgentRef=json_data.get("PaAgentRef"),
            TenantRef=json_data.get("TenantRef"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
            Http=deserialize_list(json_data.get("Http"), HttpDefinition),
            Ldap=deserialize_list(json_data.get("Ldap"), LdapDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            Saml=deserialize_list(json_data.get("Saml"), SamlDefinition),
            TacacsPlus=deserialize_list(json_data.get("TacacsPlus"), TacacsPlusDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HttpDefinition(BaseModel):
    CacheExpirationTime: Optional[float]
    RequestHeader: Optional[str]
    RequireUserGroups: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpDefinition"]:
        if not json_data:
            return None
        return cls(
            CacheExpirationTime=json_data.get("CacheExpirationTime"),
            RequestHeader=json_data.get("RequestHeader"),
            RequireUserGroups=json_data.get("RequireUserGroups"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpDefinition = HttpDefinition


@dataclass
class LdapDefinition(BaseModel):
    BaseDn: Optional[str]
    BindAsAdministrator: Optional[bool]
    EmailAttribute: Optional[str]
    FullNameAttribute: Optional[str]
    Port: Optional[float]
    SecurityMode: Optional[str]
    Server: Optional[Sequence[str]]
    Settings: Optional[Sequence["_SettingsDefinition"]]
    UserBind: Optional[Sequence["_UserBindDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LdapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LdapDefinition"]:
        if not json_data:
            return None
        return cls(
            BaseDn=json_data.get("BaseDn"),
            BindAsAdministrator=json_data.get("BindAsAdministrator"),
            EmailAttribute=json_data.get("EmailAttribute"),
            FullNameAttribute=json_data.get("FullNameAttribute"),
            Port=json_data.get("Port"),
            SecurityMode=json_data.get("SecurityMode"),
            Server=json_data.get("Server"),
            Settings=deserialize_list(json_data.get("Settings"), SettingsDefinition),
            UserBind=deserialize_list(json_data.get("UserBind"), UserBindDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LdapDefinition = LdapDefinition


@dataclass
class SettingsDefinition(BaseModel):
    AdminBindDn: Optional[str]
    GroupFilter: Optional[str]
    GroupMemberAttribute: Optional[str]
    GroupMemberIsFullDn: Optional[bool]
    GroupSearchDn: Optional[str]
    GroupSearchScope: Optional[str]
    IgnoreReferrals: Optional[bool]
    Password: Optional[str]
    UserAttributes: Optional[Sequence[str]]
    UserIdAttribute: Optional[str]
    UserSearchDn: Optional[str]
    UserSearchScope: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminBindDn=json_data.get("AdminBindDn"),
            GroupFilter=json_data.get("GroupFilter"),
            GroupMemberAttribute=json_data.get("GroupMemberAttribute"),
            GroupMemberIsFullDn=json_data.get("GroupMemberIsFullDn"),
            GroupSearchDn=json_data.get("GroupSearchDn"),
            GroupSearchScope=json_data.get("GroupSearchScope"),
            IgnoreReferrals=json_data.get("IgnoreReferrals"),
            Password=json_data.get("Password"),
            UserAttributes=json_data.get("UserAttributes"),
            UserIdAttribute=json_data.get("UserIdAttribute"),
            UserSearchDn=json_data.get("UserSearchDn"),
            UserSearchScope=json_data.get("UserSearchScope"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SettingsDefinition = SettingsDefinition


@dataclass
class UserBindDefinition(BaseModel):
    DnTemplate: Optional[str]
    Token: Optional[str]
    UserAttributes: Optional[Sequence[str]]
    UserIdAttribute: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserBindDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserBindDefinition"]:
        if not json_data:
            return None
        return cls(
            DnTemplate=json_data.get("DnTemplate"),
            Token=json_data.get("Token"),
            UserAttributes=json_data.get("UserAttributes"),
            UserIdAttribute=json_data.get("UserIdAttribute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserBindDefinition = UserBindDefinition


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


@dataclass
class SamlDefinition(BaseModel):
    Idp: Optional[Sequence["_IdpDefinition"]]
    Sp: Optional[Sequence["_SpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SamlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SamlDefinition"]:
        if not json_data:
            return None
        return cls(
            Idp=deserialize_list(json_data.get("Idp"), IdpDefinition),
            Sp=deserialize_list(json_data.get("Sp"), SpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SamlDefinition = SamlDefinition


@dataclass
class IdpDefinition(BaseModel):
    Metadata: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdpDefinition"]:
        if not json_data:
            return None
        return cls(
            Metadata=json_data.get("Metadata"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdpDefinition = IdpDefinition


@dataclass
class SpDefinition(BaseModel):
    Fqdn: Optional[str]
    OrgDisplayName: Optional[str]
    OrgName: Optional[str]
    OrgUrl: Optional[str]
    SamlEntityType: Optional[str]
    TechContactEmail: Optional[str]
    TechContactName: Optional[str]
    SpNodes: Optional[Sequence["_SpNodesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpDefinition"]:
        if not json_data:
            return None
        return cls(
            Fqdn=json_data.get("Fqdn"),
            OrgDisplayName=json_data.get("OrgDisplayName"),
            OrgName=json_data.get("OrgName"),
            OrgUrl=json_data.get("OrgUrl"),
            SamlEntityType=json_data.get("SamlEntityType"),
            TechContactEmail=json_data.get("TechContactEmail"),
            TechContactName=json_data.get("TechContactName"),
            SpNodes=deserialize_list(json_data.get("SpNodes"), SpNodesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpDefinition = SpDefinition


@dataclass
class SpNodesDefinition(BaseModel):
    EntityId: Optional[str]
    Name: Optional[str]
    SigningSslKeyAndCertificateRef: Optional[str]
    SingleSignonUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SpNodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpNodesDefinition"]:
        if not json_data:
            return None
        return cls(
            EntityId=json_data.get("EntityId"),
            Name=json_data.get("Name"),
            SigningSslKeyAndCertificateRef=json_data.get("SigningSslKeyAndCertificateRef"),
            SingleSignonUrl=json_data.get("SingleSignonUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpNodesDefinition = SpNodesDefinition


@dataclass
class TacacsPlusDefinition(BaseModel):
    Password: Optional[str]
    Port: Optional[float]
    Server: Optional[Sequence[str]]
    Service: Optional[str]
    AuthorizationAttrs: Optional[Sequence["_AuthorizationAttrsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TacacsPlusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TacacsPlusDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Server=json_data.get("Server"),
            Service=json_data.get("Service"),
            AuthorizationAttrs=deserialize_list(json_data.get("AuthorizationAttrs"), AuthorizationAttrsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TacacsPlusDefinition = TacacsPlusDefinition


@dataclass
class AuthorizationAttrsDefinition(BaseModel):
    Mandatory: Optional[bool]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthorizationAttrsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthorizationAttrsDefinition"]:
        if not json_data:
            return None
        return cls(
            Mandatory=json_data.get("Mandatory"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthorizationAttrsDefinition = AuthorizationAttrsDefinition


