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
    FirewallPolicyId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    ApplicationRuleCollection: Optional[Sequence["_ApplicationRuleCollectionDefinition"]]
    NatRuleCollection: Optional[Sequence["_NatRuleCollectionDefinition"]]
    NetworkRuleCollection: Optional[Sequence["_NetworkRuleCollectionDefinition"]]
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
            FirewallPolicyId=json_data.get("FirewallPolicyId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            ApplicationRuleCollection=deserialize_list(json_data.get("ApplicationRuleCollection"), ApplicationRuleCollectionDefinition),
            NatRuleCollection=deserialize_list(json_data.get("NatRuleCollection"), NatRuleCollectionDefinition),
            NetworkRuleCollection=deserialize_list(json_data.get("NetworkRuleCollection"), NetworkRuleCollectionDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ApplicationRuleCollectionDefinition(BaseModel):
    Action: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    Rule: Optional[Sequence["_RuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationRuleCollectionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationRuleCollectionDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationRuleCollectionDefinition = ApplicationRuleCollectionDefinition


@dataclass
class RuleDefinition(BaseModel):
    DestinationAddresses: Optional[Sequence[str]]
    DestinationFqdns: Optional[Sequence[str]]
    DestinationIpGroups: Optional[Sequence[str]]
    DestinationPorts: Optional[Sequence[str]]
    Name: Optional[str]
    Protocols: Optional[Sequence[str]]
    SourceAddresses: Optional[Sequence[str]]
    SourceIpGroups: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationAddresses=json_data.get("DestinationAddresses"),
            DestinationFqdns=json_data.get("DestinationFqdns"),
            DestinationIpGroups=json_data.get("DestinationIpGroups"),
            DestinationPorts=json_data.get("DestinationPorts"),
            Name=json_data.get("Name"),
            Protocols=json_data.get("Protocols"),
            SourceAddresses=json_data.get("SourceAddresses"),
            SourceIpGroups=json_data.get("SourceIpGroups"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class NatRuleCollectionDefinition(BaseModel):
    Action: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    Rule: Optional[Sequence["_RuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NatRuleCollectionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NatRuleCollectionDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NatRuleCollectionDefinition = NatRuleCollectionDefinition


@dataclass
class NetworkRuleCollectionDefinition(BaseModel):
    Action: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    Rule: Optional[Sequence["_RuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkRuleCollectionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkRuleCollectionDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkRuleCollectionDefinition = NetworkRuleCollectionDefinition


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

