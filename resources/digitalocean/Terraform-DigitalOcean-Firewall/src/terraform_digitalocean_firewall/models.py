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
    CreatedAt: Optional[str]
    DropletIds: Optional[Sequence[float]]
    Name: Optional[str]
    PendingChanges: Optional[Sequence["_PendingChanges"]]
    Status: Optional[str]
    Tags: Optional[Sequence[str]]
    InboundRule: Optional[Sequence["_InboundRule"]]
    OutboundRule: Optional[Sequence["_OutboundRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreatedAt=json_data.get("CreatedAt"),
            DropletIds=json_data.get("DropletIds"),
            Name=json_data.get("Name"),
            PendingChanges=json_data.get("PendingChanges"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            InboundRule=json_data.get("InboundRule"),
            OutboundRule=json_data.get("OutboundRule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PendingChanges:
    DropletId: Optional[float]
    Removing: Optional[bool]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PendingChanges"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PendingChanges"]:
        if not json_data:
            return None
        return cls(
            DropletId=json_data.get("DropletId"),
            Removing=json_data.get("Removing"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PendingChanges = PendingChanges


@dataclass
class InboundRule:
    PortRange: Optional[str]
    Protocol: Optional[str]
    SourceAddresses: Optional[Sequence[str]]
    SourceDropletIds: Optional[Sequence[float]]
    SourceLoadBalancerUids: Optional[Sequence[str]]
    SourceTags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_InboundRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InboundRule"]:
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
_InboundRule = InboundRule


@dataclass
class OutboundRule:
    DestinationAddresses: Optional[Sequence[str]]
    DestinationDropletIds: Optional[Sequence[float]]
    DestinationLoadBalancerUids: Optional[Sequence[str]]
    DestinationTags: Optional[Sequence[str]]
    PortRange: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutboundRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutboundRule"]:
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
_OutboundRule = OutboundRule


