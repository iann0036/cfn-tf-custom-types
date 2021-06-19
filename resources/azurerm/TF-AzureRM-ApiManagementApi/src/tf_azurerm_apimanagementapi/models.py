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
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    IsCurrent: Optional[bool]
    IsOnline: Optional[bool]
    Name: Optional[str]
    Path: Optional[str]
    Protocols: Optional[Sequence[str]]
    ResourceGroupName: Optional[str]
    Revision: Optional[str]
    ServiceUrl: Optional[str]
    SoapPassThrough: Optional[bool]
    SubscriptionRequired: Optional[bool]
    Version: Optional[str]
    VersionSetId: Optional[str]
    Import: Optional[Sequence["_ImportDefinition"]]
    Oauth2Authorization: Optional[Sequence["_Oauth2AuthorizationDefinition"]]
    OpenidAuthentication: Optional[Sequence["_OpenidAuthenticationDefinition"]]
    SubscriptionKeyParameterNames: Optional[Sequence["_SubscriptionKeyParameterNamesDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            IsCurrent=json_data.get("IsCurrent"),
            IsOnline=json_data.get("IsOnline"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Protocols=json_data.get("Protocols"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Revision=json_data.get("Revision"),
            ServiceUrl=json_data.get("ServiceUrl"),
            SoapPassThrough=json_data.get("SoapPassThrough"),
            SubscriptionRequired=json_data.get("SubscriptionRequired"),
            Version=json_data.get("Version"),
            VersionSetId=json_data.get("VersionSetId"),
            Import=deserialize_list(json_data.get("Import"), ImportDefinition),
            Oauth2Authorization=deserialize_list(json_data.get("Oauth2Authorization"), Oauth2AuthorizationDefinition),
            OpenidAuthentication=deserialize_list(json_data.get("OpenidAuthentication"), OpenidAuthenticationDefinition),
            SubscriptionKeyParameterNames=deserialize_list(json_data.get("SubscriptionKeyParameterNames"), SubscriptionKeyParameterNamesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ImportDefinition(BaseModel):
    ContentFormat: Optional[str]
    ContentValue: Optional[str]
    WsdlSelector: Optional[Sequence["_WsdlSelectorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ImportDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImportDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentFormat=json_data.get("ContentFormat"),
            ContentValue=json_data.get("ContentValue"),
            WsdlSelector=deserialize_list(json_data.get("WsdlSelector"), WsdlSelectorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImportDefinition = ImportDefinition


@dataclass
class WsdlSelectorDefinition(BaseModel):
    EndpointName: Optional[str]
    ServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WsdlSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WsdlSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            EndpointName=json_data.get("EndpointName"),
            ServiceName=json_data.get("ServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WsdlSelectorDefinition = WsdlSelectorDefinition


@dataclass
class Oauth2AuthorizationDefinition(BaseModel):
    AuthorizationServerName: Optional[str]
    Scope: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Oauth2AuthorizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Oauth2AuthorizationDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthorizationServerName=json_data.get("AuthorizationServerName"),
            Scope=json_data.get("Scope"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Oauth2AuthorizationDefinition = Oauth2AuthorizationDefinition


@dataclass
class OpenidAuthenticationDefinition(BaseModel):
    BearerTokenSendingMethods: Optional[Sequence[str]]
    OpenidProviderName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OpenidAuthenticationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenidAuthenticationDefinition"]:
        if not json_data:
            return None
        return cls(
            BearerTokenSendingMethods=json_data.get("BearerTokenSendingMethods"),
            OpenidProviderName=json_data.get("OpenidProviderName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenidAuthenticationDefinition = OpenidAuthenticationDefinition


@dataclass
class SubscriptionKeyParameterNamesDefinition(BaseModel):
    Header: Optional[str]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubscriptionKeyParameterNamesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubscriptionKeyParameterNamesDefinition"]:
        if not json_data:
            return None
        return cls(
            Header=json_data.get("Header"),
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubscriptionKeyParameterNamesDefinition = SubscriptionKeyParameterNamesDefinition


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


