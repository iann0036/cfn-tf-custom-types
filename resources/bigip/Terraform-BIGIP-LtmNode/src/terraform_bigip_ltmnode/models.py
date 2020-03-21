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
    Address: Optional[str]
    ConnectionLimit: Optional[float]
    Description: Optional[str]
    DynamicRatio: Optional[float]
    Monitor: Optional[str]
    Name: Optional[str]
    RateLimit: Optional[str]
    Ratio: Optional[float]
    State: Optional[str]
    Fqdn: Optional[Sequence["_Fqdn"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Address=json_data.get("Address"),
            ConnectionLimit=json_data.get("ConnectionLimit"),
            Description=json_data.get("Description"),
            DynamicRatio=json_data.get("DynamicRatio"),
            Monitor=json_data.get("Monitor"),
            Name=json_data.get("Name"),
            RateLimit=json_data.get("RateLimit"),
            Ratio=json_data.get("Ratio"),
            State=json_data.get("State"),
            Fqdn=json_data.get("Fqdn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Fqdn:
    AddressFamily: Optional[str]
    Autopopulate: Optional[str]
    Downinterval: Optional[float]
    Interval: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Fqdn"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Fqdn"]:
        if not json_data:
            return None
        return cls(
            AddressFamily=json_data.get("AddressFamily"),
            Autopopulate=json_data.get("Autopopulate"),
            Downinterval=json_data.get("Downinterval"),
            Interval=json_data.get("Interval"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Fqdn = Fqdn


