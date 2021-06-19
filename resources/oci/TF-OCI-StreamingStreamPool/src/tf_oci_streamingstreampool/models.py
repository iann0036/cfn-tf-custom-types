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
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    EndpointFqdn: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    IsPrivate: Optional[bool]
    LifecycleStateDetails: Optional[str]
    Name: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    CustomEncryptionKey: Optional[Sequence["_CustomEncryptionKeyDefinition"]]
    KafkaSettings: Optional[Sequence["_KafkaSettingsDefinition"]]
    PrivateEndpointSettings: Optional[Sequence["_PrivateEndpointSettingsDefinition"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            EndpointFqdn=json_data.get("EndpointFqdn"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            IsPrivate=json_data.get("IsPrivate"),
            LifecycleStateDetails=json_data.get("LifecycleStateDetails"),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            CustomEncryptionKey=deserialize_list(json_data.get("CustomEncryptionKey"), CustomEncryptionKeyDefinition),
            KafkaSettings=deserialize_list(json_data.get("KafkaSettings"), KafkaSettingsDefinition),
            PrivateEndpointSettings=deserialize_list(json_data.get("PrivateEndpointSettings"), PrivateEndpointSettingsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class CustomEncryptionKeyDefinition(BaseModel):
    KmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomEncryptionKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomEncryptionKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomEncryptionKeyDefinition = CustomEncryptionKeyDefinition


@dataclass
class KafkaSettingsDefinition(BaseModel):
    AutoCreateTopicsEnable: Optional[bool]
    LogRetentionHours: Optional[float]
    NumPartitions: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_KafkaSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KafkaSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoCreateTopicsEnable=json_data.get("AutoCreateTopicsEnable"),
            LogRetentionHours=json_data.get("LogRetentionHours"),
            NumPartitions=json_data.get("NumPartitions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KafkaSettingsDefinition = KafkaSettingsDefinition


@dataclass
class PrivateEndpointSettingsDefinition(BaseModel):
    NsgIds: Optional[Sequence[str]]
    PrivateEndpointIp: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateEndpointSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateEndpointSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            NsgIds=json_data.get("NsgIds"),
            PrivateEndpointIp=json_data.get("PrivateEndpointIp"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateEndpointSettingsDefinition = PrivateEndpointSettingsDefinition


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


