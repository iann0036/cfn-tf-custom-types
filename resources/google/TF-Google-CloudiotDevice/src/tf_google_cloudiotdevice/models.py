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
    Blocked: Optional[bool]
    Config: Optional[Sequence["_ConfigDefinition"]]
    Id: Optional[str]
    LastConfigAckTime: Optional[str]
    LastConfigSendTime: Optional[str]
    LastErrorStatus: Optional[Sequence["_LastErrorStatusDefinition2"]]
    LastErrorTime: Optional[str]
    LastEventTime: Optional[str]
    LastHeartbeatTime: Optional[str]
    LastStateTime: Optional[str]
    LogLevel: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    NumId: Optional[str]
    Registry: Optional[str]
    State: Optional[Sequence["_StateDefinition"]]
    Credentials: Optional[Sequence["_CredentialsDefinition"]]
    GatewayConfig: Optional[Sequence["_GatewayConfigDefinition"]]
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
            Blocked=json_data.get("Blocked"),
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
            Id=json_data.get("Id"),
            LastConfigAckTime=json_data.get("LastConfigAckTime"),
            LastConfigSendTime=json_data.get("LastConfigSendTime"),
            LastErrorStatus=deserialize_list(json_data.get("LastErrorStatus"), LastErrorStatusDefinition2),
            LastErrorTime=json_data.get("LastErrorTime"),
            LastEventTime=json_data.get("LastEventTime"),
            LastHeartbeatTime=json_data.get("LastHeartbeatTime"),
            LastStateTime=json_data.get("LastStateTime"),
            LogLevel=json_data.get("LogLevel"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            NumId=json_data.get("NumId"),
            Registry=json_data.get("Registry"),
            State=deserialize_list(json_data.get("State"), StateDefinition),
            Credentials=deserialize_list(json_data.get("Credentials"), CredentialsDefinition),
            GatewayConfig=deserialize_list(json_data.get("GatewayConfig"), GatewayConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConfigDefinition(BaseModel):
    BinaryData: Optional[str]
    CloudUpdateTime: Optional[str]
    DeviceAckTime: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BinaryData=json_data.get("BinaryData"),
            CloudUpdateTime=json_data.get("CloudUpdateTime"),
            DeviceAckTime=json_data.get("DeviceAckTime"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


@dataclass
class LastErrorStatusDefinition2(BaseModel):
    Details: Optional[Sequence[Sequence["_LastErrorStatusDefinition"]]]
    Message: Optional[str]
    Number: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LastErrorStatusDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LastErrorStatusDefinition2"]:
        if not json_data:
            return None
        return cls(
            Details=deserialize_list(json_data.get("Details"), <ResolvedType(ContainerType.MODEL, LastErrorStatusDefinition)>),
            Message=json_data.get("Message"),
            Number=json_data.get("Number"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LastErrorStatusDefinition2 = LastErrorStatusDefinition2


@dataclass
class LastErrorStatusDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LastErrorStatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LastErrorStatusDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LastErrorStatusDefinition = LastErrorStatusDefinition


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class StateDefinition(BaseModel):
    BinaryData: Optional[str]
    UpdateTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StateDefinition"]:
        if not json_data:
            return None
        return cls(
            BinaryData=json_data.get("BinaryData"),
            UpdateTime=json_data.get("UpdateTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StateDefinition = StateDefinition


@dataclass
class CredentialsDefinition(BaseModel):
    ExpirationTime: Optional[str]
    PublicKey: Optional[Sequence["_PublicKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CredentialsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CredentialsDefinition"]:
        if not json_data:
            return None
        return cls(
            ExpirationTime=json_data.get("ExpirationTime"),
            PublicKey=deserialize_list(json_data.get("PublicKey"), PublicKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CredentialsDefinition = CredentialsDefinition


@dataclass
class PublicKeyDefinition(BaseModel):
    Format: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Format=json_data.get("Format"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicKeyDefinition = PublicKeyDefinition


@dataclass
class GatewayConfigDefinition(BaseModel):
    GatewayAuthMethod: Optional[str]
    GatewayType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            GatewayAuthMethod=json_data.get("GatewayAuthMethod"),
            GatewayType=json_data.get("GatewayType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayConfigDefinition = GatewayConfigDefinition


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


