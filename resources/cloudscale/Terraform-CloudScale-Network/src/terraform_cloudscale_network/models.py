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
    Href: Optional[str]
    Id: Optional[str]
    Mtu: Optional[float]
    Name: Optional[str]
    Subnets: Optional[Sequence["_Subnets"]]
    ZoneSlug: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Href=json_data.get("Href"),
            Id=json_data.get("Id"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            Subnets=json_data.get("Subnets"),
            ZoneSlug=json_data.get("ZoneSlug"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Subnets:
    Cidr: Optional[str]
    Href: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Subnets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subnets"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
            Href=json_data.get("Href"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subnets = Subnets


