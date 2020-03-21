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
    Access: Optional[str]
    Description: Optional[str]
    DestinationAddressPrefix: Optional[str]
    DestinationPortRange: Optional[str]
    Direction: Optional[str]
    Name: Optional[str]
    NetworkSecurityGroupName: Optional[str]
    Priority: Optional[float]
    Protocol: Optional[str]
    ResourceGroupName: Optional[str]
    SourceAddressPrefix: Optional[str]
    SourceApplicationSecurityGroupIds: Optional[Sequence[str]]
    SourcePortRange: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Access=json_data.get("Access"),
            Description=json_data.get("Description"),
            DestinationAddressPrefix=json_data.get("DestinationAddressPrefix"),
            DestinationPortRange=json_data.get("DestinationPortRange"),
            Direction=json_data.get("Direction"),
            Name=json_data.get("Name"),
            NetworkSecurityGroupName=json_data.get("NetworkSecurityGroupName"),
            Priority=json_data.get("Priority"),
            Protocol=json_data.get("Protocol"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SourceAddressPrefix=json_data.get("SourceAddressPrefix"),
            SourceApplicationSecurityGroupIds=json_data.get("SourceApplicationSecurityGroupIds"),
            SourcePortRange=json_data.get("SourcePortRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


