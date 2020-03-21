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
    DestinationAddressPrefixes: Optional[Sequence[str]]
    DestinationApplicationSecurityGroupIds: Optional[Sequence[str]]
    DestinationPortRange: Optional[str]
    DestinationPortRanges: Optional[Sequence[str]]
    Direction: Optional[str]
    Name: Optional[str]
    NetworkSecurityGroupName: Optional[str]
    Priority: Optional[float]
    Protocol: Optional[str]
    ResourceGroupName: Optional[str]
    SourceAddressPrefix: Optional[str]
    SourceAddressPrefixes: Optional[Sequence[str]]
    SourceApplicationSecurityGroupIds: Optional[Sequence[str]]
    SourcePortRange: Optional[str]
    SourcePortRanges: Optional[Sequence[str]]
    Timeouts: Optional["_Timeouts"]

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
            DestinationAddressPrefixes=json_data.get("DestinationAddressPrefixes"),
            DestinationApplicationSecurityGroupIds=json_data.get("DestinationApplicationSecurityGroupIds"),
            DestinationPortRange=json_data.get("DestinationPortRange"),
            DestinationPortRanges=json_data.get("DestinationPortRanges"),
            Direction=json_data.get("Direction"),
            Name=json_data.get("Name"),
            NetworkSecurityGroupName=json_data.get("NetworkSecurityGroupName"),
            Priority=json_data.get("Priority"),
            Protocol=json_data.get("Protocol"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SourceAddressPrefix=json_data.get("SourceAddressPrefix"),
            SourceAddressPrefixes=json_data.get("SourceAddressPrefixes"),
            SourceApplicationSecurityGroupIds=json_data.get("SourceApplicationSecurityGroupIds"),
            SourcePortRange=json_data.get("SourcePortRange"),
            SourcePortRanges=json_data.get("SourcePortRanges"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


