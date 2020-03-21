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
    Destination: Optional[str]
    DestinationPort: Optional[str]
    FirewallPolicy: Optional[str]
    IcmpTypeName: Optional[str]
    Id: Optional[str]
    Protocol: Optional[str]
    Source: Optional[str]
    SourcePort: Optional[str]

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
            Destination=json_data.get("Destination"),
            DestinationPort=json_data.get("DestinationPort"),
            FirewallPolicy=json_data.get("FirewallPolicy"),
            IcmpTypeName=json_data.get("IcmpTypeName"),
            Id=json_data.get("Id"),
            Protocol=json_data.get("Protocol"),
            Source=json_data.get("Source"),
            SourcePort=json_data.get("SourcePort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


