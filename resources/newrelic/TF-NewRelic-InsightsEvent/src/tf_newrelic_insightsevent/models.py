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
    Id: Optional[str]
    Event: Optional[Sequence["_EventDefinition"]]

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
            Id=json_data.get("Id"),
            Event=deserialize_list(json_data.get("Event"), EventDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EventDefinition(BaseModel):
    Timestamp: Optional[float]
    Type: Optional[str]
    Attribute: Optional[Sequence["_AttributeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EventDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventDefinition"]:
        if not json_data:
            return None
        return cls(
            Timestamp=json_data.get("Timestamp"),
            Type=json_data.get("Type"),
            Attribute=deserialize_list(json_data.get("Attribute"), AttributeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventDefinition = EventDefinition


@dataclass
class AttributeDefinition(BaseModel):
    Key: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeDefinition = AttributeDefinition


