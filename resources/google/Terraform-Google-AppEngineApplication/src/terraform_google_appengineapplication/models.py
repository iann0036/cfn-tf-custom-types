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
    AppId: Optional[str]
    AuthDomain: Optional[str]
    CodeBucket: Optional[str]
    DefaultBucket: Optional[str]
    DefaultHostname: Optional[str]
    GcrDomain: Optional[str]
    LocationId: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    ServingStatus: Optional[str]
    UrlDispatchRule: Optional[Sequence["_UrlDispatchRule"]]
    FeatureSettings: Optional[Sequence["_FeatureSettings"]]
    Iap: Optional[Sequence["_Iap"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AppId=json_data.get("AppId"),
            AuthDomain=json_data.get("AuthDomain"),
            CodeBucket=json_data.get("CodeBucket"),
            DefaultBucket=json_data.get("DefaultBucket"),
            DefaultHostname=json_data.get("DefaultHostname"),
            GcrDomain=json_data.get("GcrDomain"),
            LocationId=json_data.get("LocationId"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            ServingStatus=json_data.get("ServingStatus"),
            UrlDispatchRule=json_data.get("UrlDispatchRule"),
            FeatureSettings=json_data.get("FeatureSettings"),
            Iap=json_data.get("Iap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class UrlDispatchRule:
    Domain: Optional[str]
    Path: Optional[str]
    Service: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UrlDispatchRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlDispatchRule"]:
        if not json_data:
            return None
        return cls(
            Domain=json_data.get("Domain"),
            Path=json_data.get("Path"),
            Service=json_data.get("Service"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlDispatchRule = UrlDispatchRule


@dataclass
class FeatureSettings:
    SplitHealthChecks: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FeatureSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FeatureSettings"]:
        if not json_data:
            return None
        return cls(
            SplitHealthChecks=json_data.get("SplitHealthChecks"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FeatureSettings = FeatureSettings


@dataclass
class Iap:
    Oauth2ClientId: Optional[str]
    Oauth2ClientSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Iap"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Iap"]:
        if not json_data:
            return None
        return cls(
            Oauth2ClientId=json_data.get("Oauth2ClientId"),
            Oauth2ClientSecret=json_data.get("Oauth2ClientSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Iap = Iap


