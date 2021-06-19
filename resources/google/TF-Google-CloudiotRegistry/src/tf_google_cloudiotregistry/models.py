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
    HttpConfig: Optional[Sequence["_HttpConfigDefinition"]]
    Id: Optional[str]
    LogLevel: Optional[str]
    MqttConfig: Optional[Sequence["_MqttConfigDefinition"]]
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    StateNotificationConfig: Optional[Sequence["_StateNotificationConfigDefinition"]]
    Credentials: Optional[Sequence["_CredentialsDefinition"]]
    EventNotificationConfigs: Optional[Sequence["_EventNotificationConfigsDefinition"]]
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
            HttpConfig=deserialize_list(json_data.get("HttpConfig"), HttpConfigDefinition),
            Id=json_data.get("Id"),
            LogLevel=json_data.get("LogLevel"),
            MqttConfig=deserialize_list(json_data.get("MqttConfig"), MqttConfigDefinition),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            StateNotificationConfig=deserialize_list(json_data.get("StateNotificationConfig"), StateNotificationConfigDefinition),
            Credentials=deserialize_list(json_data.get("Credentials"), CredentialsDefinition),
            EventNotificationConfigs=deserialize_list(json_data.get("EventNotificationConfigs"), EventNotificationConfigsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HttpConfigDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpConfigDefinition = HttpConfigDefinition


@dataclass
class MqttConfigDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MqttConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MqttConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MqttConfigDefinition = MqttConfigDefinition


@dataclass
class StateNotificationConfigDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StateNotificationConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StateNotificationConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StateNotificationConfigDefinition = StateNotificationConfigDefinition


@dataclass
class CredentialsDefinition(BaseModel):
    PublicKeyCertificate: Optional[Sequence["_PublicKeyCertificateDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CredentialsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CredentialsDefinition"]:
        if not json_data:
            return None
        return cls(
            PublicKeyCertificate=deserialize_list(json_data.get("PublicKeyCertificate"), PublicKeyCertificateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CredentialsDefinition = CredentialsDefinition


@dataclass
class PublicKeyCertificateDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicKeyCertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicKeyCertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicKeyCertificateDefinition = PublicKeyCertificateDefinition


@dataclass
class EventNotificationConfigsDefinition(BaseModel):
    PubsubTopicName: Optional[str]
    SubfolderMatches: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventNotificationConfigsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventNotificationConfigsDefinition"]:
        if not json_data:
            return None
        return cls(
            PubsubTopicName=json_data.get("PubsubTopicName"),
            SubfolderMatches=json_data.get("SubfolderMatches"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventNotificationConfigsDefinition = EventNotificationConfigsDefinition


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


