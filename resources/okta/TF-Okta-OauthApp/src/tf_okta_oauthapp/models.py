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
    AutoKeyRotation: Optional[bool]
    AutoSubmitToolbar: Optional[bool]
    ClientBasicSecret: Optional[str]
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    ClientUri: Optional[str]
    ConsentMethod: Optional[str]
    CustomClientId: Optional[str]
    GrantTypes: Optional[Sequence[str]]
    Groups: Optional[Sequence[str]]
    HideIos: Optional[bool]
    HideWeb: Optional[bool]
    Id: Optional[str]
    ImplicitAssignment: Optional[bool]
    IssuerMode: Optional[str]
    Label: Optional[str]
    LoginMode: Optional[str]
    LoginScopes: Optional[Sequence[str]]
    LoginUri: Optional[str]
    LogoUri: Optional[str]
    Name: Optional[str]
    OmitSecret: Optional[bool]
    PolicyUri: Optional[str]
    PostLogoutRedirectUris: Optional[Sequence[str]]
    Profile: Optional[str]
    RedirectUris: Optional[Sequence[str]]
    ResponseTypes: Optional[Sequence[str]]
    SignOnMode: Optional[str]
    Status: Optional[str]
    TokenEndpointAuthMethod: Optional[str]
    TosUri: Optional[str]
    Type: Optional[str]
    Jwks: Optional[Sequence["_JwksDefinition"]]
    Users: Optional[Sequence["_UsersDefinition"]]

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
            AutoKeyRotation=json_data.get("AutoKeyRotation"),
            AutoSubmitToolbar=json_data.get("AutoSubmitToolbar"),
            ClientBasicSecret=json_data.get("ClientBasicSecret"),
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            ClientUri=json_data.get("ClientUri"),
            ConsentMethod=json_data.get("ConsentMethod"),
            CustomClientId=json_data.get("CustomClientId"),
            GrantTypes=json_data.get("GrantTypes"),
            Groups=json_data.get("Groups"),
            HideIos=json_data.get("HideIos"),
            HideWeb=json_data.get("HideWeb"),
            Id=json_data.get("Id"),
            ImplicitAssignment=json_data.get("ImplicitAssignment"),
            IssuerMode=json_data.get("IssuerMode"),
            Label=json_data.get("Label"),
            LoginMode=json_data.get("LoginMode"),
            LoginScopes=json_data.get("LoginScopes"),
            LoginUri=json_data.get("LoginUri"),
            LogoUri=json_data.get("LogoUri"),
            Name=json_data.get("Name"),
            OmitSecret=json_data.get("OmitSecret"),
            PolicyUri=json_data.get("PolicyUri"),
            PostLogoutRedirectUris=json_data.get("PostLogoutRedirectUris"),
            Profile=json_data.get("Profile"),
            RedirectUris=json_data.get("RedirectUris"),
            ResponseTypes=json_data.get("ResponseTypes"),
            SignOnMode=json_data.get("SignOnMode"),
            Status=json_data.get("Status"),
            TokenEndpointAuthMethod=json_data.get("TokenEndpointAuthMethod"),
            TosUri=json_data.get("TosUri"),
            Type=json_data.get("Type"),
            Jwks=deserialize_list(json_data.get("Jwks"), JwksDefinition),
            Users=deserialize_list(json_data.get("Users"), UsersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class JwksDefinition(BaseModel):
    E: Optional[str]
    Kid: Optional[str]
    Kty: Optional[str]
    N: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JwksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JwksDefinition"]:
        if not json_data:
            return None
        return cls(
            E=json_data.get("E"),
            Kid=json_data.get("Kid"),
            Kty=json_data.get("Kty"),
            N=json_data.get("N"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JwksDefinition = JwksDefinition


@dataclass
class UsersDefinition(BaseModel):
    Id: Optional[str]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UsersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsersDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsersDefinition = UsersDefinition


