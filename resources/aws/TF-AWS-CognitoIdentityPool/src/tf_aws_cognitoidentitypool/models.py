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
    AllowClassicFlow: Optional[bool]
    AllowUnauthenticatedIdentities: Optional[bool]
    Arn: Optional[str]
    DeveloperProviderName: Optional[str]
    Id: Optional[str]
    IdentityPoolName: Optional[str]
    OpenidConnectProviderArns: Optional[Sequence[str]]
    SamlProviderArns: Optional[Sequence[str]]
    SupportedLoginProviders: Optional[Sequence["_SupportedLoginProvidersDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    CognitoIdentityProviders: Optional[Sequence["_CognitoIdentityProvidersDefinition"]]

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
            AllowClassicFlow=json_data.get("AllowClassicFlow"),
            AllowUnauthenticatedIdentities=json_data.get("AllowUnauthenticatedIdentities"),
            Arn=json_data.get("Arn"),
            DeveloperProviderName=json_data.get("DeveloperProviderName"),
            Id=json_data.get("Id"),
            IdentityPoolName=json_data.get("IdentityPoolName"),
            OpenidConnectProviderArns=json_data.get("OpenidConnectProviderArns"),
            SamlProviderArns=json_data.get("SamlProviderArns"),
            SupportedLoginProviders=deserialize_list(json_data.get("SupportedLoginProviders"), SupportedLoginProvidersDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            CognitoIdentityProviders=deserialize_list(json_data.get("CognitoIdentityProviders"), CognitoIdentityProvidersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SupportedLoginProvidersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SupportedLoginProvidersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SupportedLoginProvidersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SupportedLoginProvidersDefinition = SupportedLoginProvidersDefinition


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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class CognitoIdentityProvidersDefinition(BaseModel):
    ClientId: Optional[str]
    ProviderName: Optional[str]
    ServerSideTokenCheck: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CognitoIdentityProvidersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CognitoIdentityProvidersDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            ProviderName=json_data.get("ProviderName"),
            ServerSideTokenCheck=json_data.get("ServerSideTokenCheck"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CognitoIdentityProvidersDefinition = CognitoIdentityProvidersDefinition


