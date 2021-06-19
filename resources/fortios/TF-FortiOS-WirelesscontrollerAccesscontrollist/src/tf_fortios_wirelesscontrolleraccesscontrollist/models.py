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
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Vdomparam: Optional[str]
    Layer3Ipv4Rules: Optional[Sequence["_Layer3Ipv4RulesDefinition"]]
    Layer3Ipv6Rules: Optional[Sequence["_Layer3Ipv6RulesDefinition"]]

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
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            Layer3Ipv4Rules=deserialize_list(json_data.get("Layer3Ipv4Rules"), Layer3Ipv4RulesDefinition),
            Layer3Ipv6Rules=deserialize_list(json_data.get("Layer3Ipv6Rules"), Layer3Ipv6RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Layer3Ipv4RulesDefinition(BaseModel):
    Action: Optional[str]
    Comment: Optional[str]
    Dstaddr: Optional[str]
    Dstport: Optional[float]
    Protocol: Optional[float]
    RuleId: Optional[float]
    Srcaddr: Optional[str]
    Srcport: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Layer3Ipv4RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Layer3Ipv4RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Comment=json_data.get("Comment"),
            Dstaddr=json_data.get("Dstaddr"),
            Dstport=json_data.get("Dstport"),
            Protocol=json_data.get("Protocol"),
            RuleId=json_data.get("RuleId"),
            Srcaddr=json_data.get("Srcaddr"),
            Srcport=json_data.get("Srcport"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Layer3Ipv4RulesDefinition = Layer3Ipv4RulesDefinition


@dataclass
class Layer3Ipv6RulesDefinition(BaseModel):
    Action: Optional[str]
    Comment: Optional[str]
    Dstaddr: Optional[str]
    Dstport: Optional[float]
    Protocol: Optional[float]
    RuleId: Optional[float]
    Srcaddr: Optional[str]
    Srcport: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Layer3Ipv6RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Layer3Ipv6RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Comment=json_data.get("Comment"),
            Dstaddr=json_data.get("Dstaddr"),
            Dstport=json_data.get("Dstport"),
            Protocol=json_data.get("Protocol"),
            RuleId=json_data.get("RuleId"),
            Srcaddr=json_data.get("Srcaddr"),
            Srcport=json_data.get("Srcport"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Layer3Ipv6RulesDefinition = Layer3Ipv6RulesDefinition


