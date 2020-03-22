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
    Datacenter: Optional[str]
    Id: Optional[str]
    Node: Optional[str]
    Token: Optional[str]
    Service: Optional[Sequence["_Service"]]

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
            Datacenter=json_data.get("Datacenter"),
            Id=json_data.get("Id"),
            Node=json_data.get("Node"),
            Token=json_data.get("Token"),
            Service=json_data.get("Service"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Service:
    Address: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    Tags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Service"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Service"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Service = Service


