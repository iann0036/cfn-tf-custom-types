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
    SecurityGroupId: Optional[str]
    InboundRule: Optional[Sequence["_InboundRuleDefinition"]]
    OutboundRule: Optional[Sequence["_OutboundRuleDefinition"]]
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
            Id=json_data.get("Id"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            InboundRule=deserialize_list(json_data.get("InboundRule"), InboundRuleDefinition),
            OutboundRule=deserialize_list(json_data.get("OutboundRule"), OutboundRuleDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InboundRuleDefinition(BaseModel):
    Action: Optional[str]
    Ip: Optional[str]
    IpRange: Optional[str]
    Port: Optional[float]
    PortRange: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InboundRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InboundRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Ip=json_data.get("Ip"),
            IpRange=json_data.get("IpRange"),
            Port=json_data.get("Port"),
            PortRange=json_data.get("PortRange"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InboundRuleDefinition = InboundRuleDefinition


@dataclass
class OutboundRuleDefinition(BaseModel):
    Action: Optional[str]
    Ip: Optional[str]
    IpRange: Optional[str]
    Port: Optional[float]
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
            Action=json_data.get("Action"),
            Ip=json_data.get("Ip"),
            IpRange=json_data.get("IpRange"),
            Port=json_data.get("Port"),
            PortRange=json_data.get("PortRange"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutboundRuleDefinition = OutboundRuleDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Default: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


