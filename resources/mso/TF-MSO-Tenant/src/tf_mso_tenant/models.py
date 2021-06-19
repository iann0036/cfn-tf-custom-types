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
    DisplayName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    SiteAssociations: Optional[Sequence["_SiteAssociationsDefinition"]]
    UserAssociations: Optional[Sequence["_UserAssociationsDefinition"]]

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
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SiteAssociations=deserialize_list(json_data.get("SiteAssociations"), SiteAssociationsDefinition),
            UserAssociations=deserialize_list(json_data.get("UserAssociations"), UserAssociationsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SiteAssociationsDefinition(BaseModel):
    AwsAccessKeyId: Optional[str]
    AwsAccountId: Optional[str]
    AwsSecretKey: Optional[str]
    AzureAccessType: Optional[str]
    AzureActiveDirectoryId: Optional[str]
    AzureApplicationId: Optional[str]
    AzureClientSecret: Optional[str]
    AzureSharedAccountId: Optional[str]
    AzureSubscriptionId: Optional[str]
    IsAwsAccountTrusted: Optional[bool]
    SecurityDomains: Optional[Sequence[str]]
    SiteId: Optional[str]
    Vendor: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SiteAssociationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SiteAssociationsDefinition"]:
        if not json_data:
            return None
        return cls(
            AwsAccessKeyId=json_data.get("AwsAccessKeyId"),
            AwsAccountId=json_data.get("AwsAccountId"),
            AwsSecretKey=json_data.get("AwsSecretKey"),
            AzureAccessType=json_data.get("AzureAccessType"),
            AzureActiveDirectoryId=json_data.get("AzureActiveDirectoryId"),
            AzureApplicationId=json_data.get("AzureApplicationId"),
            AzureClientSecret=json_data.get("AzureClientSecret"),
            AzureSharedAccountId=json_data.get("AzureSharedAccountId"),
            AzureSubscriptionId=json_data.get("AzureSubscriptionId"),
            IsAwsAccountTrusted=json_data.get("IsAwsAccountTrusted"),
            SecurityDomains=json_data.get("SecurityDomains"),
            SiteId=json_data.get("SiteId"),
            Vendor=json_data.get("Vendor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SiteAssociationsDefinition = SiteAssociationsDefinition


@dataclass
class UserAssociationsDefinition(BaseModel):
    UserId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserAssociationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserAssociationsDefinition"]:
        if not json_data:
            return None
        return cls(
            UserId=json_data.get("UserId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserAssociationsDefinition = UserAssociationsDefinition


