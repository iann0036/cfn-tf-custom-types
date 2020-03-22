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
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    Revision: Optional[float]
    Subnet: Optional[Sequence["_Subnet"]]
    Tag: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            Revision=json_data.get("Revision"),
            Subnet=json_data.get("Subnet"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Subnet:
    AllocationRanges: Optional[Sequence[str]]
    Cidr: Optional[str]
    DnsNameservers: Optional[Sequence[str]]
    DnsSuffix: Optional[str]
    GatewayIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Subnet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subnet"]:
        if not json_data:
            return None
        return cls(
            AllocationRanges=json_data.get("AllocationRanges"),
            Cidr=json_data.get("Cidr"),
            DnsNameservers=json_data.get("DnsNameservers"),
            DnsSuffix=json_data.get("DnsSuffix"),
            GatewayIp=json_data.get("GatewayIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subnet = Subnet


@dataclass
class Tag:
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


