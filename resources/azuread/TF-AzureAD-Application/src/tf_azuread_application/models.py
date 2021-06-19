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
    AppRole: Optional[Sequence["_AppRoleDefinition"]]
    ApplicationId: Optional[str]
    AvailableToOtherTenants: Optional[bool]
    DisplayName: Optional[str]
    FallbackPublicClientEnabled: Optional[bool]
    GroupMembershipClaims: Optional[str]
    Homepage: Optional[str]
    Id: Optional[str]
    IdentifierUris: Optional[Sequence[str]]
    LogoutUrl: Optional[str]
    Name: Optional[str]
    Oauth2AllowImplicitFlow: Optional[bool]
    Oauth2Permissions: Optional[Sequence["_Oauth2PermissionsDefinition"]]
    ObjectId: Optional[str]
    Owners: Optional[Sequence[str]]
    PreventDuplicateNames: Optional[bool]
    PublicClient: Optional[bool]
    ReplyUrls: Optional[Sequence[str]]
    SignInAudience: Optional[str]
    Type: Optional[str]
    Api: Optional[Sequence["_ApiDefinition"]]
    OptionalClaims: Optional[Sequence["_OptionalClaimsDefinition"]]
    RequiredResourceAccess: Optional[Sequence["_RequiredResourceAccessDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    Web: Optional[Sequence["_WebDefinition"]]

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
            AppRole=deserialize_list(json_data.get("AppRole"), AppRoleDefinition),
            ApplicationId=json_data.get("ApplicationId"),
            AvailableToOtherTenants=json_data.get("AvailableToOtherTenants"),
            DisplayName=json_data.get("DisplayName"),
            FallbackPublicClientEnabled=json_data.get("FallbackPublicClientEnabled"),
            GroupMembershipClaims=json_data.get("GroupMembershipClaims"),
            Homepage=json_data.get("Homepage"),
            Id=json_data.get("Id"),
            IdentifierUris=json_data.get("IdentifierUris"),
            LogoutUrl=json_data.get("LogoutUrl"),
            Name=json_data.get("Name"),
            Oauth2AllowImplicitFlow=json_data.get("Oauth2AllowImplicitFlow"),
            Oauth2Permissions=deserialize_list(json_data.get("Oauth2Permissions"), Oauth2PermissionsDefinition),
            ObjectId=json_data.get("ObjectId"),
            Owners=json_data.get("Owners"),
            PreventDuplicateNames=json_data.get("PreventDuplicateNames"),
            PublicClient=json_data.get("PublicClient"),
            ReplyUrls=json_data.get("ReplyUrls"),
            SignInAudience=json_data.get("SignInAudience"),
            Type=json_data.get("Type"),
            Api=deserialize_list(json_data.get("Api"), ApiDefinition),
            OptionalClaims=deserialize_list(json_data.get("OptionalClaims"), OptionalClaimsDefinition),
            RequiredResourceAccess=deserialize_list(json_data.get("RequiredResourceAccess"), RequiredResourceAccessDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            Web=deserialize_list(json_data.get("Web"), WebDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppRoleDefinition(BaseModel):
    AllowedMemberTypes: Optional[Sequence[str]]
    Description: Optional[str]
    DisplayName: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    IsEnabled: Optional[bool]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppRoleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppRoleDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedMemberTypes=json_data.get("AllowedMemberTypes"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            IsEnabled=json_data.get("IsEnabled"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppRoleDefinition = AppRoleDefinition


@dataclass
class Oauth2PermissionsDefinition(BaseModel):
    AdminConsentDescription: Optional[str]
    AdminConsentDisplayName: Optional[str]
    Id: Optional[str]
    IsEnabled: Optional[bool]
    Type: Optional[str]
    UserConsentDescription: Optional[str]
    UserConsentDisplayName: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Oauth2PermissionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Oauth2PermissionsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminConsentDescription=json_data.get("AdminConsentDescription"),
            AdminConsentDisplayName=json_data.get("AdminConsentDisplayName"),
            Id=json_data.get("Id"),
            IsEnabled=json_data.get("IsEnabled"),
            Type=json_data.get("Type"),
            UserConsentDescription=json_data.get("UserConsentDescription"),
            UserConsentDisplayName=json_data.get("UserConsentDisplayName"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Oauth2PermissionsDefinition = Oauth2PermissionsDefinition


@dataclass
class ApiDefinition(BaseModel):
    Oauth2PermissionScope: Optional[Sequence["_Oauth2PermissionScopeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApiDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApiDefinition"]:
        if not json_data:
            return None
        return cls(
            Oauth2PermissionScope=deserialize_list(json_data.get("Oauth2PermissionScope"), Oauth2PermissionScopeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApiDefinition = ApiDefinition


@dataclass
class Oauth2PermissionScopeDefinition(BaseModel):
    AdminConsentDescription: Optional[str]
    AdminConsentDisplayName: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Type: Optional[str]
    UserConsentDescription: Optional[str]
    UserConsentDisplayName: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Oauth2PermissionScopeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Oauth2PermissionScopeDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminConsentDescription=json_data.get("AdminConsentDescription"),
            AdminConsentDisplayName=json_data.get("AdminConsentDisplayName"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
            UserConsentDescription=json_data.get("UserConsentDescription"),
            UserConsentDisplayName=json_data.get("UserConsentDisplayName"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Oauth2PermissionScopeDefinition = Oauth2PermissionScopeDefinition


@dataclass
class OptionalClaimsDefinition(BaseModel):
    AccessToken: Optional[Sequence["_AccessTokenDefinition"]]
    IdToken: Optional[Sequence["_IdTokenDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OptionalClaimsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionalClaimsDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessToken=deserialize_list(json_data.get("AccessToken"), AccessTokenDefinition),
            IdToken=deserialize_list(json_data.get("IdToken"), IdTokenDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionalClaimsDefinition = OptionalClaimsDefinition


@dataclass
class AccessTokenDefinition(BaseModel):
    AdditionalProperties: Optional[Sequence[str]]
    Essential: Optional[bool]
    Name: Optional[str]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessTokenDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessTokenDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Essential=json_data.get("Essential"),
            Name=json_data.get("Name"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessTokenDefinition = AccessTokenDefinition


@dataclass
class IdTokenDefinition(BaseModel):
    AdditionalProperties: Optional[Sequence[str]]
    Essential: Optional[bool]
    Name: Optional[str]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdTokenDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdTokenDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Essential=json_data.get("Essential"),
            Name=json_data.get("Name"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdTokenDefinition = IdTokenDefinition


@dataclass
class RequiredResourceAccessDefinition(BaseModel):
    ResourceAppId: Optional[str]
    ResourceAccess: Optional[Sequence["_ResourceAccessDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RequiredResourceAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequiredResourceAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceAppId=json_data.get("ResourceAppId"),
            ResourceAccess=deserialize_list(json_data.get("ResourceAccess"), ResourceAccessDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequiredResourceAccessDefinition = RequiredResourceAccessDefinition


@dataclass
class ResourceAccessDefinition(BaseModel):
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAccessDefinition = ResourceAccessDefinition


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


@dataclass
class WebDefinition(BaseModel):
    HomepageUrl: Optional[str]
    LogoutUrl: Optional[str]
    RedirectUris: Optional[Sequence[str]]
    ImplicitGrant: Optional[Sequence["_ImplicitGrantDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WebDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebDefinition"]:
        if not json_data:
            return None
        return cls(
            HomepageUrl=json_data.get("HomepageUrl"),
            LogoutUrl=json_data.get("LogoutUrl"),
            RedirectUris=json_data.get("RedirectUris"),
            ImplicitGrant=deserialize_list(json_data.get("ImplicitGrant"), ImplicitGrantDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebDefinition = WebDefinition


@dataclass
class ImplicitGrantDefinition(BaseModel):
    AccessTokenIssuanceEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ImplicitGrantDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImplicitGrantDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessTokenIssuanceEnabled=json_data.get("AccessTokenIssuanceEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImplicitGrantDefinition = ImplicitGrantDefinition


