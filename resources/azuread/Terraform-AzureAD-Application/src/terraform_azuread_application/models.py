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
    ApplicationId: Optional[str]
    AvailableToOtherTenants: Optional[bool]
    GroupMembershipClaims: Optional[str]
    Homepage: Optional[str]
    Id: Optional[str]
    IdentifierUris: Optional[Sequence[str]]
    LogoutUrl: Optional[str]
    Name: Optional[str]
    Oauth2AllowImplicitFlow: Optional[bool]
    ObjectId: Optional[str]
    Owners: Optional[Sequence[str]]
    PublicClient: Optional[bool]
    ReplyUrls: Optional[Sequence[str]]
    Type: Optional[str]
    AppRole: Optional[Sequence["_AppRole"]]
    RequiredResourceAccess: Optional[Sequence["_RequiredResourceAccess"]]
    ResourceAccess: Optional[Sequence["_ResourceAccess"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApplicationId=json_data.get("ApplicationId"),
            AvailableToOtherTenants=json_data.get("AvailableToOtherTenants"),
            GroupMembershipClaims=json_data.get("GroupMembershipClaims"),
            Homepage=json_data.get("Homepage"),
            Id=json_data.get("Id"),
            IdentifierUris=json_data.get("IdentifierUris"),
            LogoutUrl=json_data.get("LogoutUrl"),
            Name=json_data.get("Name"),
            Oauth2AllowImplicitFlow=json_data.get("Oauth2AllowImplicitFlow"),
            ObjectId=json_data.get("ObjectId"),
            Owners=json_data.get("Owners"),
            PublicClient=json_data.get("PublicClient"),
            ReplyUrls=json_data.get("ReplyUrls"),
            Type=json_data.get("Type"),
            AppRole=json_data.get("AppRole"),
            RequiredResourceAccess=json_data.get("RequiredResourceAccess"),
            ResourceAccess=json_data.get("ResourceAccess"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppRole:
    AllowedMemberTypes: Optional[Sequence[str]]
    Description: Optional[str]
    DisplayName: Optional[str]
    IsEnabled: Optional[bool]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppRole"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppRole"]:
        if not json_data:
            return None
        return cls(
            AllowedMemberTypes=json_data.get("AllowedMemberTypes"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            IsEnabled=json_data.get("IsEnabled"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppRole = AppRole


@dataclass
class RequiredResourceAccess:
    ResourceAppId: Optional[str]
    ResourceAccess: Optional[Sequence["_ResourceAccess"]]

    @classmethod
    def _deserialize(
        cls: Type["_RequiredResourceAccess"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequiredResourceAccess"]:
        if not json_data:
            return None
        return cls(
            ResourceAppId=json_data.get("ResourceAppId"),
            ResourceAccess=json_data.get("ResourceAccess"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequiredResourceAccess = RequiredResourceAccess


@dataclass
class ResourceAccess:
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAccess"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAccess"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAccess = ResourceAccess


