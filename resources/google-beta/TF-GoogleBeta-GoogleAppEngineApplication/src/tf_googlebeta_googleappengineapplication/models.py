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
    AppId: Optional[str]
    AuthDomain: Optional[str]
    CodeBucket: Optional[str]
    DatabaseType: Optional[str]
    DefaultBucket: Optional[str]
    DefaultHostname: Optional[str]
    GcrDomain: Optional[str]
    Id: Optional[str]
    LocationId: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    ServingStatus: Optional[str]
    UrlDispatchRule: Optional[Sequence["_UrlDispatchRuleDefinition"]]
    FeatureSettings: Optional[Sequence["_FeatureSettingsDefinition"]]
    Iap: Optional[Sequence["_IapDefinition"]]
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
            AppId=json_data.get("AppId"),
            AuthDomain=json_data.get("AuthDomain"),
            CodeBucket=json_data.get("CodeBucket"),
            DatabaseType=json_data.get("DatabaseType"),
            DefaultBucket=json_data.get("DefaultBucket"),
            DefaultHostname=json_data.get("DefaultHostname"),
            GcrDomain=json_data.get("GcrDomain"),
            Id=json_data.get("Id"),
            LocationId=json_data.get("LocationId"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            ServingStatus=json_data.get("ServingStatus"),
            UrlDispatchRule=deserialize_list(json_data.get("UrlDispatchRule"), UrlDispatchRuleDefinition),
            FeatureSettings=deserialize_list(json_data.get("FeatureSettings"), FeatureSettingsDefinition),
            Iap=deserialize_list(json_data.get("Iap"), IapDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class UrlDispatchRuleDefinition(BaseModel):
    Domain: Optional[str]
    Path: Optional[str]
    Service: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UrlDispatchRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlDispatchRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Domain=json_data.get("Domain"),
            Path=json_data.get("Path"),
            Service=json_data.get("Service"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlDispatchRuleDefinition = UrlDispatchRuleDefinition


@dataclass
class FeatureSettingsDefinition(BaseModel):
    SplitHealthChecks: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FeatureSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FeatureSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            SplitHealthChecks=json_data.get("SplitHealthChecks"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FeatureSettingsDefinition = FeatureSettingsDefinition


@dataclass
class IapDefinition(BaseModel):
    Enabled: Optional[bool]
    Oauth2ClientId: Optional[str]
    Oauth2ClientSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IapDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Oauth2ClientId=json_data.get("Oauth2ClientId"),
            Oauth2ClientSecret=json_data.get("Oauth2ClientSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IapDefinition = IapDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


