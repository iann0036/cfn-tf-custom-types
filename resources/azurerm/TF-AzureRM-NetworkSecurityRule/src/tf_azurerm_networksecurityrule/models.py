# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    Access: Optional[str]
    Description: Optional[str]
    DestinationAddressPrefix: Optional[str]
    DestinationAddressPrefixes: Optional[Sequence[str]]
    DestinationApplicationSecurityGroupIds: Optional[Sequence[str]]
    DestinationPortRange: Optional[str]
    DestinationPortRanges: Optional[Sequence[str]]
    Direction: Optional[str]
    Id: Optional[str]
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
    Timeouts: Optional["_TimeoutsDefinition"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
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
            Id=json_data.get("Id"),
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
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


