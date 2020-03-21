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
    AllowUnauthenticatedIdentities: Optional[bool]
    Arn: Optional[str]
    DeveloperProviderName: Optional[str]
    Id: Optional[str]
    IdentityPoolName: Optional[str]
    OpenidConnectProviderArns: Optional[Sequence[str]]
    SamlProviderArns: Optional[Sequence[str]]
    SupportedLoginProviders: Optional[Sequence["_SupportedLoginProviders"]]
    Tags: Optional[Sequence["_Tags"]]
    CognitoIdentityProviders: Optional[Sequence["_CognitoIdentityProviders"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowUnauthenticatedIdentities=json_data.get("AllowUnauthenticatedIdentities"),
            Arn=json_data.get("Arn"),
            DeveloperProviderName=json_data.get("DeveloperProviderName"),
            Id=json_data.get("Id"),
            IdentityPoolName=json_data.get("IdentityPoolName"),
            OpenidConnectProviderArns=json_data.get("OpenidConnectProviderArns"),
            SamlProviderArns=json_data.get("SamlProviderArns"),
            SupportedLoginProviders=json_data.get("SupportedLoginProviders"),
            Tags=json_data.get("Tags"),
            CognitoIdentityProviders=json_data.get("CognitoIdentityProviders"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SupportedLoginProviders:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SupportedLoginProviders"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SupportedLoginProviders"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SupportedLoginProviders = SupportedLoginProviders


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
class CognitoIdentityProviders:
    ClientId: Optional[str]
    ProviderName: Optional[str]
    ServerSideTokenCheck: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CognitoIdentityProviders"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CognitoIdentityProviders"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            ProviderName=json_data.get("ProviderName"),
            ServerSideTokenCheck=json_data.get("ServerSideTokenCheck"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CognitoIdentityProviders = CognitoIdentityProviders


