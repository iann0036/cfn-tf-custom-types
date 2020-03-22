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
    AllowedOauthFlows: Optional[Sequence[str]]
    AllowedOauthFlowsUserPoolClient: Optional[bool]
    AllowedOauthScopes: Optional[Sequence[str]]
    CallbackUrls: Optional[Sequence[str]]
    ClientSecret: Optional[str]
    DefaultRedirectUri: Optional[str]
    ExplicitAuthFlows: Optional[Sequence[str]]
    GenerateSecret: Optional[bool]
    Id: Optional[str]
    LogoutUrls: Optional[Sequence[str]]
    Name: Optional[str]
    PreventUserExistenceErrors: Optional[str]
    ReadAttributes: Optional[Sequence[str]]
    RefreshTokenValidity: Optional[float]
    SupportedIdentityProviders: Optional[Sequence[str]]
    UserPoolId: Optional[str]
    WriteAttributes: Optional[Sequence[str]]
    AnalyticsConfiguration: Optional[Sequence["_AnalyticsConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowedOauthFlows=json_data.get("AllowedOauthFlows"),
            AllowedOauthFlowsUserPoolClient=json_data.get("AllowedOauthFlowsUserPoolClient"),
            AllowedOauthScopes=json_data.get("AllowedOauthScopes"),
            CallbackUrls=json_data.get("CallbackUrls"),
            ClientSecret=json_data.get("ClientSecret"),
            DefaultRedirectUri=json_data.get("DefaultRedirectUri"),
            ExplicitAuthFlows=json_data.get("ExplicitAuthFlows"),
            GenerateSecret=json_data.get("GenerateSecret"),
            Id=json_data.get("Id"),
            LogoutUrls=json_data.get("LogoutUrls"),
            Name=json_data.get("Name"),
            PreventUserExistenceErrors=json_data.get("PreventUserExistenceErrors"),
            ReadAttributes=json_data.get("ReadAttributes"),
            RefreshTokenValidity=json_data.get("RefreshTokenValidity"),
            SupportedIdentityProviders=json_data.get("SupportedIdentityProviders"),
            UserPoolId=json_data.get("UserPoolId"),
            WriteAttributes=json_data.get("WriteAttributes"),
            AnalyticsConfiguration=json_data.get("AnalyticsConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnalyticsConfiguration:
    ApplicationId: Optional[str]
    ExternalId: Optional[str]
    RoleArn: Optional[str]
    UserDataShared: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AnalyticsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalyticsConfiguration"]:
        if not json_data:
            return None
        return cls(
            ApplicationId=json_data.get("ApplicationId"),
            ExternalId=json_data.get("ExternalId"),
            RoleArn=json_data.get("RoleArn"),
            UserDataShared=json_data.get("UserDataShared"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalyticsConfiguration = AnalyticsConfiguration


