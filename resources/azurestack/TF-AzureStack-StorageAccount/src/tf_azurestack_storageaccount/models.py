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
    AccountEncryptionSource: Optional[str]
    AccountKind: Optional[str]
    AccountReplicationType: Optional[str]
    AccountTier: Optional[str]
    AccountType: Optional[str]
    EnableBlobEncryption: Optional[bool]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PrimaryAccessKey: Optional[str]
    PrimaryBlobConnectionString: Optional[str]
    PrimaryBlobEndpoint: Optional[str]
    PrimaryConnectionString: Optional[str]
    PrimaryFileEndpoint: Optional[str]
    PrimaryLocation: Optional[str]
    PrimaryQueueEndpoint: Optional[str]
    PrimaryTableEndpoint: Optional[str]
    ResourceGroupName: Optional[str]
    SecondaryAccessKey: Optional[str]
    SecondaryBlobConnectionString: Optional[str]
    SecondaryBlobEndpoint: Optional[str]
    SecondaryConnectionString: Optional[str]
    SecondaryLocation: Optional[str]
    SecondaryQueueEndpoint: Optional[str]
    SecondaryTableEndpoint: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    CustomDomain: Optional[Sequence["_CustomDomainDefinition"]]

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
            AccountEncryptionSource=json_data.get("AccountEncryptionSource"),
            AccountKind=json_data.get("AccountKind"),
            AccountReplicationType=json_data.get("AccountReplicationType"),
            AccountTier=json_data.get("AccountTier"),
            AccountType=json_data.get("AccountType"),
            EnableBlobEncryption=json_data.get("EnableBlobEncryption"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PrimaryAccessKey=json_data.get("PrimaryAccessKey"),
            PrimaryBlobConnectionString=json_data.get("PrimaryBlobConnectionString"),
            PrimaryBlobEndpoint=json_data.get("PrimaryBlobEndpoint"),
            PrimaryConnectionString=json_data.get("PrimaryConnectionString"),
            PrimaryFileEndpoint=json_data.get("PrimaryFileEndpoint"),
            PrimaryLocation=json_data.get("PrimaryLocation"),
            PrimaryQueueEndpoint=json_data.get("PrimaryQueueEndpoint"),
            PrimaryTableEndpoint=json_data.get("PrimaryTableEndpoint"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SecondaryAccessKey=json_data.get("SecondaryAccessKey"),
            SecondaryBlobConnectionString=json_data.get("SecondaryBlobConnectionString"),
            SecondaryBlobEndpoint=json_data.get("SecondaryBlobEndpoint"),
            SecondaryConnectionString=json_data.get("SecondaryConnectionString"),
            SecondaryLocation=json_data.get("SecondaryLocation"),
            SecondaryQueueEndpoint=json_data.get("SecondaryQueueEndpoint"),
            SecondaryTableEndpoint=json_data.get("SecondaryTableEndpoint"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            CustomDomain=deserialize_list(json_data.get("CustomDomain"), CustomDomainDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class CustomDomainDefinition(BaseModel):
    Name: Optional[str]
    UseSubdomain: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CustomDomainDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomDomainDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            UseSubdomain=json_data.get("UseSubdomain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomDomainDefinition = CustomDomainDefinition


