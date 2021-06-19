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
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    SecurityRule: Optional[Sequence["_SecurityRuleDefinition"]]

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
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            SecurityRule=deserialize_list(json_data.get("SecurityRule"), SecurityRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class SecurityRuleDefinition(BaseModel):
    Access: Optional[str]
    Description: Optional[str]
    DestinationAddressPrefix: Optional[str]
    DestinationPortRange: Optional[str]
    Direction: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    Protocol: Optional[str]
    SourceAddressPrefix: Optional[str]
    SourcePortRange: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Access=json_data.get("Access"),
            Description=json_data.get("Description"),
            DestinationAddressPrefix=json_data.get("DestinationAddressPrefix"),
            DestinationPortRange=json_data.get("DestinationPortRange"),
            Direction=json_data.get("Direction"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Protocol=json_data.get("Protocol"),
            SourceAddressPrefix=json_data.get("SourceAddressPrefix"),
            SourcePortRange=json_data.get("SourcePortRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityRuleDefinition = SecurityRuleDefinition


