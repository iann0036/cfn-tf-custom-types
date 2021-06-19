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
    Action: Optional[str]
    AzureFirewallName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    ResourceGroupName: Optional[str]
    Rule: Optional[Sequence["_RuleDefinition"]]
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
            Action=json_data.get("Action"),
            AzureFirewallName=json_data.get("AzureFirewallName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RuleDefinition(BaseModel):
    Description: Optional[str]
    FqdnTags: Optional[Sequence[str]]
    Name: Optional[str]
    SourceAddresses: Optional[Sequence[str]]
    SourceIpGroups: Optional[Sequence[str]]
    TargetFqdns: Optional[Sequence[str]]
    Protocol: Optional[Sequence["_ProtocolDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            FqdnTags=json_data.get("FqdnTags"),
            Name=json_data.get("Name"),
            SourceAddresses=json_data.get("SourceAddresses"),
            SourceIpGroups=json_data.get("SourceIpGroups"),
            TargetFqdns=json_data.get("TargetFqdns"),
            Protocol=deserialize_list(json_data.get("Protocol"), ProtocolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class ProtocolDefinition(BaseModel):
    Port: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProtocolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProtocolDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProtocolDefinition = ProtocolDefinition


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


