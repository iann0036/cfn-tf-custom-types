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
    DomainNameLabel: Optional[str]
    Fqdn: Optional[str]
    Id: Optional[str]
    IdleTimeoutInMinutes: Optional[float]
    IpAddress: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PublicIpAddressAllocation: Optional[str]
    ResourceGroupName: Optional[str]
    ReverseFqdn: Optional[str]
    Tags: Optional[Sequence["_Tags"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DomainNameLabel=json_data.get("DomainNameLabel"),
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            IdleTimeoutInMinutes=json_data.get("IdleTimeoutInMinutes"),
            IpAddress=json_data.get("IpAddress"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PublicIpAddressAllocation=json_data.get("PublicIpAddressAllocation"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ReverseFqdn=json_data.get("ReverseFqdn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


