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
    ClientConnThrottle: Optional[float]
    Created: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    Ipv4: Optional[str]
    Ipv6: Optional[str]
    Label: Optional[str]
    Region: Optional[str]
    Tags: Optional[Sequence[str]]
    Transfer: Optional[Sequence["_Transfer"]]
    Updated: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ClientConnThrottle=json_data.get("ClientConnThrottle"),
            Created=json_data.get("Created"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Ipv4=json_data.get("Ipv4"),
            Ipv6=json_data.get("Ipv6"),
            Label=json_data.get("Label"),
            Region=json_data.get("Region"),
            Tags=json_data.get("Tags"),
            Transfer=json_data.get("Transfer"),
            Updated=json_data.get("Updated"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Transfer:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Transfer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Transfer"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Transfer = Transfer


