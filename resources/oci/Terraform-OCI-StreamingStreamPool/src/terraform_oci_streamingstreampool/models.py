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
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Id: Optional[str]
    LifecycleStateDetails: Optional[str]
    Name: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    KafkaSettings: Optional[Sequence["_KafkaSettings"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            FreeformTags=json_data.get("FreeformTags"),
            Id=json_data.get("Id"),
            LifecycleStateDetails=json_data.get("LifecycleStateDetails"),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            KafkaSettings=json_data.get("KafkaSettings"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class KafkaSettings:
    AutoCreateTopicsEnable: Optional[bool]
    LogRetentionHours: Optional[float]
    NumPartitions: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_KafkaSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KafkaSettings"]:
        if not json_data:
            return None
        return cls(
            AutoCreateTopicsEnable=json_data.get("AutoCreateTopicsEnable"),
            LogRetentionHours=json_data.get("LogRetentionHours"),
            NumPartitions=json_data.get("NumPartitions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KafkaSettings = KafkaSettings


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts

