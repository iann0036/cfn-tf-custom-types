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
    Name: Optional[str]
    Vhost: Optional[str]
    Settings: Optional[Sequence["_Settings"]]

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
            Name=json_data.get("Name"),
            Vhost=json_data.get("Vhost"),
            Settings=json_data.get("Settings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Settings:
    Arguments: Optional[Sequence["_Arguments"]]
    ArgumentsJson: Optional[str]
    AutoDelete: Optional[bool]
    Durable: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Settings"]:
        if not json_data:
            return None
        return cls(
            Arguments=json_data.get("Arguments"),
            ArgumentsJson=json_data.get("ArgumentsJson"),
            AutoDelete=json_data.get("AutoDelete"),
            Durable=json_data.get("Durable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Settings = Settings


@dataclass
class Arguments:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Arguments"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Arguments"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Arguments = Arguments


