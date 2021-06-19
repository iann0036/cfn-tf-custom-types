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
    AccessTokenValidity: Optional[float]
    AllowedOauthFlows: Optional[Sequence[str]]
    AllowedOauthFlowsUserPoolClient: Optional[bool]
    AllowedOauthScopes: Optional[Sequence[str]]
    CallbackUrls: Optional[Sequence[str]]
    ClientSecret: Optional[str]
    DefaultRedirectUri: Optional[str]
    ExplicitAuthFlows: Optional[Sequence[str]]
    GenerateSecret: Optional[bool]
    Id: Optional[str]
    IdTokenValidity: Optional[float]
    LogoutUrls: Optional[Sequence[str]]
    Name: Optional[str]
    PreventUserExistenceErrors: Optional[str]
    ReadAttributes: Optional[Sequence[str]]
    RefreshTokenValidity: Optional[float]
    SupportedIdentityProviders: Optional[Sequence[str]]
    UserPoolId: Optional[str]
    WriteAttributes: Optional[Sequence[str]]
    AnalyticsConfiguration: Optional[Sequence["_AnalyticsConfigurationDefinition"]]
    TokenValidityUnits: Optional[Sequence["_TokenValidityUnitsDefinition"]]

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
            AccessTokenValidity=json_data.get("AccessTokenValidity"),
            AllowedOauthFlows=json_data.get("AllowedOauthFlows"),
            AllowedOauthFlowsUserPoolClient=json_data.get("AllowedOauthFlowsUserPoolClient"),
            AllowedOauthScopes=json_data.get("AllowedOauthScopes"),
            CallbackUrls=json_data.get("CallbackUrls"),
            ClientSecret=json_data.get("ClientSecret"),
            DefaultRedirectUri=json_data.get("DefaultRedirectUri"),
            ExplicitAuthFlows=json_data.get("ExplicitAuthFlows"),
            GenerateSecret=json_data.get("GenerateSecret"),
            Id=json_data.get("Id"),
            IdTokenValidity=json_data.get("IdTokenValidity"),
            LogoutUrls=json_data.get("LogoutUrls"),
            Name=json_data.get("Name"),
            PreventUserExistenceErrors=json_data.get("PreventUserExistenceErrors"),
            ReadAttributes=json_data.get("ReadAttributes"),
            RefreshTokenValidity=json_data.get("RefreshTokenValidity"),
            SupportedIdentityProviders=json_data.get("SupportedIdentityProviders"),
            UserPoolId=json_data.get("UserPoolId"),
            WriteAttributes=json_data.get("WriteAttributes"),
            AnalyticsConfiguration=deserialize_list(json_data.get("AnalyticsConfiguration"), AnalyticsConfigurationDefinition),
            TokenValidityUnits=deserialize_list(json_data.get("TokenValidityUnits"), TokenValidityUnitsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnalyticsConfigurationDefinition(BaseModel):
    ApplicationArn: Optional[str]
    ApplicationId: Optional[str]
    ExternalId: Optional[str]
    RoleArn: Optional[str]
    UserDataShared: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AnalyticsConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalyticsConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ApplicationArn=json_data.get("ApplicationArn"),
            ApplicationId=json_data.get("ApplicationId"),
            ExternalId=json_data.get("ExternalId"),
            RoleArn=json_data.get("RoleArn"),
            UserDataShared=json_data.get("UserDataShared"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalyticsConfigurationDefinition = AnalyticsConfigurationDefinition


@dataclass
class TokenValidityUnitsDefinition(BaseModel):
    AccessToken: Optional[str]
    IdToken: Optional[str]
    RefreshToken: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TokenValidityUnitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TokenValidityUnitsDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessToken=json_data.get("AccessToken"),
            IdToken=json_data.get("IdToken"),
            RefreshToken=json_data.get("RefreshToken"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TokenValidityUnitsDefinition = TokenValidityUnitsDefinition


