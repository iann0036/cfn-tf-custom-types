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
    CreatedAt: Optional[str]
    DropletIds: Optional[Sequence[float]]
    Id: Optional[str]
    Name: Optional[str]
    PendingChanges: Optional[Sequence["_PendingChangesDefinition"]]
    Status: Optional[str]
    Tags: Optional[Sequence[str]]
    InboundRule: Optional[Sequence["_InboundRuleDefinition"]]
    OutboundRule: Optional[Sequence["_OutboundRuleDefinition"]]

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
            CreatedAt=json_data.get("CreatedAt"),
            DropletIds=json_data.get("DropletIds"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PendingChanges=deserialize_list(json_data.get("PendingChanges"), PendingChangesDefinition),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            InboundRule=deserialize_list(json_data.get("InboundRule"), InboundRuleDefinition),
            OutboundRule=deserialize_list(json_data.get("OutboundRule"), OutboundRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PendingChangesDefinition(BaseModel):
    DropletId: Optional[float]
    Removing: Optional[bool]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PendingChangesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PendingChangesDefinition"]:
        if not json_data:
            return None
        return cls(
            DropletId=json_data.get("DropletId"),
            Removing=json_data.get("Removing"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PendingChangesDefinition = PendingChangesDefinition


@dataclass
class InboundRuleDefinition(BaseModel):
    PortRange: Optional[str]
    Protocol: Optional[str]
    SourceAddresses: Optional[Sequence[str]]
    SourceDropletIds: Optional[Sequence[float]]
    SourceLoadBalancerUids: Optional[Sequence[str]]
    SourceTags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_InboundRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InboundRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            PortRange=json_data.get("PortRange"),
            Protocol=json_data.get("Protocol"),
            SourceAddresses=json_data.get("SourceAddresses"),
            SourceDropletIds=json_data.get("SourceDropletIds"),
            SourceLoadBalancerUids=json_data.get("SourceLoadBalancerUids"),
            SourceTags=json_data.get("SourceTags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InboundRuleDefinition = InboundRuleDefinition


@dataclass
class OutboundRuleDefinition(BaseModel):
    DestinationAddresses: Optional[Sequence[str]]
    DestinationDropletIds: Optional[Sequence[float]]
    DestinationLoadBalancerUids: Optional[Sequence[str]]
    DestinationTags: Optional[Sequence[str]]
    PortRange: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutboundRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutboundRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationAddresses=json_data.get("DestinationAddresses"),
            DestinationDropletIds=json_data.get("DestinationDropletIds"),
            DestinationLoadBalancerUids=json_data.get("DestinationLoadBalancerUids"),
            DestinationTags=json_data.get("DestinationTags"),
            PortRange=json_data.get("PortRange"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutboundRuleDefinition = OutboundRuleDefinition


