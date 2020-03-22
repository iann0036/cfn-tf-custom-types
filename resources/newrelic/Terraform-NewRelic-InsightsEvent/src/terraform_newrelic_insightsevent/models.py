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
    Id: Optional[str]
    Event: Optional[Sequence["_Event"]]
    Attribute: Optional[Sequence["_Attribute"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            Event=json_data.get("Event"),
            Attribute=json_data.get("Attribute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Event:
    Timestamp: Optional[float]
    Type: Optional[str]
    Attribute: Optional[Sequence["_Attribute"]]

    @classmethod
    def _deserialize(
        cls: Type["_Event"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Event"]:
        if not json_data:
            return None
        return cls(
            Timestamp=json_data.get("Timestamp"),
            Type=json_data.get("Type"),
            Attribute=json_data.get("Attribute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Event = Event


@dataclass
class Attribute:
    Key: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Attribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Attribute"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Attribute = Attribute


