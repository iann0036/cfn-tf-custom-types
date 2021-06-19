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
    Devices: Optional[Sequence["_DevicesDefinition"]]
    Disabled: Optional[bool]
    Id: Optional[str]
    InboundPolicy: Optional[str]
    Label: Optional[str]
    Linodes: Optional[Sequence[float]]
    OutboundPolicy: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence[str]]
    Inbound: Optional[Sequence["_InboundDefinition"]]
    Outbound: Optional[Sequence["_OutboundDefinition"]]

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
            Devices=deserialize_list(json_data.get("Devices"), DevicesDefinition),
            Disabled=json_data.get("Disabled"),
            Id=json_data.get("Id"),
            InboundPolicy=json_data.get("InboundPolicy"),
            Label=json_data.get("Label"),
            Linodes=json_data.get("Linodes"),
            OutboundPolicy=json_data.get("OutboundPolicy"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            Inbound=deserialize_list(json_data.get("Inbound"), InboundDefinition),
            Outbound=deserialize_list(json_data.get("Outbound"), OutboundDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DevicesDefinition(BaseModel):
    EntityId: Optional[float]
    Id: Optional[float]
    Label: Optional[str]
    Type: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DevicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DevicesDefinition"]:
        if not json_data:
            return None
        return cls(
            EntityId=json_data.get("EntityId"),
            Id=json_data.get("Id"),
            Label=json_data.get("Label"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DevicesDefinition = DevicesDefinition


@dataclass
class InboundDefinition(BaseModel):
    Action: Optional[str]
    Ipv4: Optional[Sequence[str]]
    Ipv6: Optional[Sequence[str]]
    Label: Optional[str]
    Ports: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InboundDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InboundDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Ipv4=json_data.get("Ipv4"),
            Ipv6=json_data.get("Ipv6"),
            Label=json_data.get("Label"),
            Ports=json_data.get("Ports"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InboundDefinition = InboundDefinition


@dataclass
class OutboundDefinition(BaseModel):
    Action: Optional[str]
    Ipv4: Optional[Sequence[str]]
    Ipv6: Optional[Sequence[str]]
    Label: Optional[str]
    Ports: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutboundDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutboundDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Ipv4=json_data.get("Ipv4"),
            Ipv6=json_data.get("Ipv6"),
            Label=json_data.get("Label"),
            Ports=json_data.get("Ports"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutboundDefinition = OutboundDefinition


