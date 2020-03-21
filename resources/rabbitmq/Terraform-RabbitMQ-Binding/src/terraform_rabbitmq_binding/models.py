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
    Arguments: Optional[Sequence["_Arguments"]]
    Destination: Optional[str]
    DestinationType: Optional[str]
    Id: Optional[str]
    PropertiesKey: Optional[str]
    RoutingKey: Optional[str]
    Source: Optional[str]
    Vhost: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arguments=json_data.get("Arguments"),
            Destination=json_data.get("Destination"),
            DestinationType=json_data.get("DestinationType"),
            Id=json_data.get("Id"),
            PropertiesKey=json_data.get("PropertiesKey"),
            RoutingKey=json_data.get("RoutingKey"),
            Source=json_data.get("Source"),
            Vhost=json_data.get("Vhost"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Arguments:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Arguments"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Arguments"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Arguments = Arguments


