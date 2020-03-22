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
    ApiManagementName: Optional[str]
    AuthorizationEndpoint: Optional[str]
    AuthorizationMethods: Optional[Sequence[str]]
    BearerTokenSendingMethods: Optional[Sequence[str]]
    ClientAuthenticationMethod: Optional[Sequence[str]]
    ClientId: Optional[str]
    ClientRegistrationEndpoint: Optional[str]
    ClientSecret: Optional[str]
    DefaultScope: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    GrantTypes: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    ResourceOwnerPassword: Optional[str]
    ResourceOwnerUsername: Optional[str]
    SupportState: Optional[bool]
    TokenEndpoint: Optional[str]
    Timeouts: Optional["_Timeouts"]
    TokenBodyParameter: Optional[Sequence["_TokenBodyParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApiManagementName=json_data.get("ApiManagementName"),
            AuthorizationEndpoint=json_data.get("AuthorizationEndpoint"),
            AuthorizationMethods=json_data.get("AuthorizationMethods"),
            BearerTokenSendingMethods=json_data.get("BearerTokenSendingMethods"),
            ClientAuthenticationMethod=json_data.get("ClientAuthenticationMethod"),
            ClientId=json_data.get("ClientId"),
            ClientRegistrationEndpoint=json_data.get("ClientRegistrationEndpoint"),
            ClientSecret=json_data.get("ClientSecret"),
            DefaultScope=json_data.get("DefaultScope"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            GrantTypes=json_data.get("GrantTypes"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ResourceOwnerPassword=json_data.get("ResourceOwnerPassword"),
            ResourceOwnerUsername=json_data.get("ResourceOwnerUsername"),
            SupportState=json_data.get("SupportState"),
            TokenEndpoint=json_data.get("TokenEndpoint"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            TokenBodyParameter=json_data.get("TokenBodyParameter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


@dataclass
class TokenBodyParameter:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TokenBodyParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TokenBodyParameter"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TokenBodyParameter = TokenBodyParameter


