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
    Timeouts: Optional["_TimeoutsDefinition"]
    TokenBodyParameter: Optional[Sequence["_TokenBodyParameterDefinition"]]

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
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            TokenBodyParameter=deserialize_list(json_data.get("TokenBodyParameter"), TokenBodyParameterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class TokenBodyParameterDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TokenBodyParameterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TokenBodyParameterDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TokenBodyParameterDefinition = TokenBodyParameterDefinition


