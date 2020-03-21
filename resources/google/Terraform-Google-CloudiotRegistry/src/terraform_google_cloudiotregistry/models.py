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
    EventNotificationConfig: Optional[Sequence["_EventNotificationConfig"]]
    HttpConfig: Optional[Sequence["_HttpConfig"]]
    LogLevel: Optional[str]
    MqttConfig: Optional[Sequence["_MqttConfig"]]
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    StateNotificationConfig: Optional[Sequence["_StateNotificationConfig"]]
    Credentials: Optional[Sequence["_Credentials"]]
    EventNotificationConfigs: Optional[Sequence["_EventNotificationConfigs"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EventNotificationConfig=json_data.get("EventNotificationConfig"),
            HttpConfig=json_data.get("HttpConfig"),
            LogLevel=json_data.get("LogLevel"),
            MqttConfig=json_data.get("MqttConfig"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            StateNotificationConfig=json_data.get("StateNotificationConfig"),
            Credentials=json_data.get("Credentials"),
            EventNotificationConfigs=json_data.get("EventNotificationConfigs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EventNotificationConfig:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventNotificationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventNotificationConfig"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventNotificationConfig = EventNotificationConfig


@dataclass
class HttpConfig:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpConfig"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpConfig = HttpConfig


@dataclass
class MqttConfig:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MqttConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MqttConfig"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MqttConfig = MqttConfig


@dataclass
class StateNotificationConfig:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StateNotificationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StateNotificationConfig"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StateNotificationConfig = StateNotificationConfig


@dataclass
class Credentials:
    PublicKeyCertificate: Optional[Sequence["_PublicKeyCertificate"]]

    @classmethod
    def _deserialize(
        cls: Type["_Credentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Credentials"]:
        if not json_data:
            return None
        return cls(
            PublicKeyCertificate=json_data.get("PublicKeyCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Credentials = Credentials


@dataclass
class PublicKeyCertificate:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicKeyCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicKeyCertificate"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicKeyCertificate = PublicKeyCertificate


@dataclass
class EventNotificationConfigs:
    PubsubTopicName: Optional[str]
    SubfolderMatches: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventNotificationConfigs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventNotificationConfigs"]:
        if not json_data:
            return None
        return cls(
            PubsubTopicName=json_data.get("PubsubTopicName"),
            SubfolderMatches=json_data.get("SubfolderMatches"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventNotificationConfigs = EventNotificationConfigs


