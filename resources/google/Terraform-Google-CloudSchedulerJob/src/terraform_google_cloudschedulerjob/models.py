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
    AttemptDeadline: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    Schedule: Optional[str]
    TimeZone: Optional[str]
    AppEngineHttpTarget: Optional[Sequence["_AppEngineHttpTarget"]]
    HttpTarget: Optional[Sequence["_HttpTarget"]]
    PubsubTarget: Optional[Sequence["_PubsubTarget"]]
    RetryConfig: Optional[Sequence["_RetryConfig"]]
    Timeouts: Optional["_Timeouts"]
    AppEngineRouting: Optional[Sequence["_AppEngineRouting"]]
    OauthToken: Optional[Sequence["_OauthToken"]]
    OidcToken: Optional[Sequence["_OidcToken"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AttemptDeadline=json_data.get("AttemptDeadline"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            Schedule=json_data.get("Schedule"),
            TimeZone=json_data.get("TimeZone"),
            AppEngineHttpTarget=json_data.get("AppEngineHttpTarget"),
            HttpTarget=json_data.get("HttpTarget"),
            PubsubTarget=json_data.get("PubsubTarget"),
            RetryConfig=json_data.get("RetryConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            AppEngineRouting=json_data.get("AppEngineRouting"),
            OauthToken=json_data.get("OauthToken"),
            OidcToken=json_data.get("OidcToken"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppEngineHttpTarget:
    Body: Optional[str]
    Headers: Optional[Sequence["_Headers"]]
    HttpMethod: Optional[str]
    RelativeUri: Optional[str]
    AppEngineRouting: Optional[Sequence["_AppEngineRouting"]]

    @classmethod
    def _deserialize(
        cls: Type["_AppEngineHttpTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppEngineHttpTarget"]:
        if not json_data:
            return None
        return cls(
            Body=json_data.get("Body"),
            Headers=json_data.get("Headers"),
            HttpMethod=json_data.get("HttpMethod"),
            RelativeUri=json_data.get("RelativeUri"),
            AppEngineRouting=json_data.get("AppEngineRouting"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppEngineHttpTarget = AppEngineHttpTarget


@dataclass
class Headers:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers = Headers


@dataclass
class AppEngineRouting:
    Instance: Optional[str]
    Service: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppEngineRouting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppEngineRouting"]:
        if not json_data:
            return None
        return cls(
            Instance=json_data.get("Instance"),
            Service=json_data.get("Service"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppEngineRouting = AppEngineRouting


@dataclass
class HttpTarget:
    Body: Optional[str]
    Headers: Optional[Sequence["_Headers2"]]
    HttpMethod: Optional[str]
    Uri: Optional[str]
    OauthToken: Optional[Sequence["_OauthToken"]]
    OidcToken: Optional[Sequence["_OidcToken"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpTarget"]:
        if not json_data:
            return None
        return cls(
            Body=json_data.get("Body"),
            Headers=json_data.get("Headers"),
            HttpMethod=json_data.get("HttpMethod"),
            Uri=json_data.get("Uri"),
            OauthToken=json_data.get("OauthToken"),
            OidcToken=json_data.get("OidcToken"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpTarget = HttpTarget


@dataclass
class Headers2:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers2"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers2 = Headers2


@dataclass
class OauthToken:
    Scope: Optional[str]
    ServiceAccountEmail: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OauthToken"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OauthToken"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            ServiceAccountEmail=json_data.get("ServiceAccountEmail"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OauthToken = OauthToken


@dataclass
class OidcToken:
    Audience: Optional[str]
    ServiceAccountEmail: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OidcToken"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OidcToken"]:
        if not json_data:
            return None
        return cls(
            Audience=json_data.get("Audience"),
            ServiceAccountEmail=json_data.get("ServiceAccountEmail"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OidcToken = OidcToken


@dataclass
class PubsubTarget:
    Attributes: Optional[Sequence["_Attributes"]]
    Data: Optional[str]
    TopicName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PubsubTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PubsubTarget"]:
        if not json_data:
            return None
        return cls(
            Attributes=json_data.get("Attributes"),
            Data=json_data.get("Data"),
            TopicName=json_data.get("TopicName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PubsubTarget = PubsubTarget


@dataclass
class Attributes:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Attributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Attributes"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Attributes = Attributes


@dataclass
class RetryConfig:
    MaxBackoffDuration: Optional[str]
    MaxDoublings: Optional[float]
    MaxRetryDuration: Optional[str]
    MinBackoffDuration: Optional[str]
    RetryCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RetryConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryConfig"]:
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
_RetryConfig = RetryConfig


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


