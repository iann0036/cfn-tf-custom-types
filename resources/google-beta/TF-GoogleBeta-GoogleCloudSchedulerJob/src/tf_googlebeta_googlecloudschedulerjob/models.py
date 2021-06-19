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
    AttemptDeadline: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    Schedule: Optional[str]
    TimeZone: Optional[str]
    AppEngineHttpTarget: Optional[Sequence["_AppEngineHttpTargetDefinition"]]
    HttpTarget: Optional[Sequence["_HttpTargetDefinition"]]
    PubsubTarget: Optional[Sequence["_PubsubTargetDefinition"]]
    RetryConfig: Optional[Sequence["_RetryConfigDefinition"]]
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
            AttemptDeadline=json_data.get("AttemptDeadline"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            Schedule=json_data.get("Schedule"),
            TimeZone=json_data.get("TimeZone"),
            AppEngineHttpTarget=deserialize_list(json_data.get("AppEngineHttpTarget"), AppEngineHttpTargetDefinition),
            HttpTarget=deserialize_list(json_data.get("HttpTarget"), HttpTargetDefinition),
            PubsubTarget=deserialize_list(json_data.get("PubsubTarget"), PubsubTargetDefinition),
            RetryConfig=deserialize_list(json_data.get("RetryConfig"), RetryConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppEngineHttpTargetDefinition(BaseModel):
    Body: Optional[str]
    Headers: Optional[Sequence["_HeadersDefinition"]]
    HttpMethod: Optional[str]
    RelativeUri: Optional[str]
    AppEngineRouting: Optional[Sequence["_AppEngineRoutingDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AppEngineHttpTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppEngineHttpTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            Body=json_data.get("Body"),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
            HttpMethod=json_data.get("HttpMethod"),
            RelativeUri=json_data.get("RelativeUri"),
            AppEngineRouting=deserialize_list(json_data.get("AppEngineRouting"), AppEngineRoutingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppEngineHttpTargetDefinition = AppEngineHttpTargetDefinition


@dataclass
class HeadersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


@dataclass
class AppEngineRoutingDefinition(BaseModel):
    Instance: Optional[str]
    Service: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppEngineRoutingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppEngineRoutingDefinition"]:
        if not json_data:
            return None
        return cls(
            Instance=json_data.get("Instance"),
            Service=json_data.get("Service"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppEngineRoutingDefinition = AppEngineRoutingDefinition


@dataclass
class HttpTargetDefinition(BaseModel):
    Body: Optional[str]
    Headers: Optional[Sequence["_HeadersDefinition2"]]
    HttpMethod: Optional[str]
    Uri: Optional[str]
    OauthToken: Optional[Sequence["_OauthTokenDefinition"]]
    OidcToken: Optional[Sequence["_OidcTokenDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            Body=json_data.get("Body"),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition2),
            HttpMethod=json_data.get("HttpMethod"),
            Uri=json_data.get("Uri"),
            OauthToken=deserialize_list(json_data.get("OauthToken"), OauthTokenDefinition),
            OidcToken=deserialize_list(json_data.get("OidcToken"), OidcTokenDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpTargetDefinition = HttpTargetDefinition


@dataclass
class HeadersDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition2 = HeadersDefinition2


@dataclass
class OauthTokenDefinition(BaseModel):
    Scope: Optional[str]
    ServiceAccountEmail: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OauthTokenDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OauthTokenDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            ServiceAccountEmail=json_data.get("ServiceAccountEmail"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OauthTokenDefinition = OauthTokenDefinition


@dataclass
class OidcTokenDefinition(BaseModel):
    Audience: Optional[str]
    ServiceAccountEmail: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OidcTokenDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OidcTokenDefinition"]:
        if not json_data:
            return None
        return cls(
            Audience=json_data.get("Audience"),
            ServiceAccountEmail=json_data.get("ServiceAccountEmail"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OidcTokenDefinition = OidcTokenDefinition


@dataclass
class PubsubTargetDefinition(BaseModel):
    Attributes: Optional[Sequence["_AttributesDefinition"]]
    Data: Optional[str]
    TopicName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PubsubTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PubsubTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            Attributes=deserialize_list(json_data.get("Attributes"), AttributesDefinition),
            Data=json_data.get("Data"),
            TopicName=json_data.get("TopicName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PubsubTargetDefinition = PubsubTargetDefinition


@dataclass
class AttributesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributesDefinition = AttributesDefinition


@dataclass
class RetryConfigDefinition(BaseModel):
    MaxBackoffDuration: Optional[str]
    MaxDoublings: Optional[float]
    MaxRetryDuration: Optional[str]
    MinBackoffDuration: Optional[str]
    RetryCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RetryConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxBackoffDuration=json_data.get("MaxBackoffDuration"),
            MaxDoublings=json_data.get("MaxDoublings"),
            MaxRetryDuration=json_data.get("MaxRetryDuration"),
            MinBackoffDuration=json_data.get("MinBackoffDuration"),
            RetryCount=json_data.get("RetryCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryConfigDefinition = RetryConfigDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


