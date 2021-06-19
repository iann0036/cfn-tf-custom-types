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
    ServerId: Optional[str]
    FirewallRule: Optional[Sequence["_FirewallRuleDefinition"]]

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
            ServerId=json_data.get("ServerId"),
            FirewallRule=deserialize_list(json_data.get("FirewallRule"), FirewallRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FirewallRuleDefinition(BaseModel):
    Action: Optional[str]
    Comment: Optional[str]
    DestinationAddressEnd: Optional[str]
    DestinationAddressStart: Optional[str]
    DestinationPortEnd: Optional[float]
    DestinationPortStart: Optional[float]
    Direction: Optional[str]
    Family: Optional[str]
    IcmpType: Optional[str]
    Protocol: Optional[str]
    SourceAddressEnd: Optional[str]
    SourceAddressStart: Optional[str]
    SourcePortEnd: Optional[float]
    SourcePortStart: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FirewallRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirewallRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Comment=json_data.get("Comment"),
            DestinationAddressEnd=json_data.get("DestinationAddressEnd"),
            DestinationAddressStart=json_data.get("DestinationAddressStart"),
            DestinationPortEnd=json_data.get("DestinationPortEnd"),
            DestinationPortStart=json_data.get("DestinationPortStart"),
            Direction=json_data.get("Direction"),
            Family=json_data.get("Family"),
            IcmpType=json_data.get("IcmpType"),
            Protocol=json_data.get("Protocol"),
            SourceAddressEnd=json_data.get("SourceAddressEnd"),
            SourceAddressStart=json_data.get("SourceAddressStart"),
            SourcePortEnd=json_data.get("SourcePortEnd"),
            SourcePortStart=json_data.get("SourcePortStart"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirewallRuleDefinition = FirewallRuleDefinition


