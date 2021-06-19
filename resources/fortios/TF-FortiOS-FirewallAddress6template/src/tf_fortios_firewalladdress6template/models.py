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
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Ip6: Optional[str]
    Name: Optional[str]
    SubnetSegmentCount: Optional[float]
    Vdomparam: Optional[str]
    SubnetSegment: Optional[Sequence["_SubnetSegmentDefinition"]]

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
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Ip6=json_data.get("Ip6"),
            Name=json_data.get("Name"),
            SubnetSegmentCount=json_data.get("SubnetSegmentCount"),
            Vdomparam=json_data.get("Vdomparam"),
            SubnetSegment=deserialize_list(json_data.get("SubnetSegment"), SubnetSegmentDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SubnetSegmentDefinition(BaseModel):
    Bits: Optional[float]
    Exclusive: Optional[str]
    Id: Optional[float]
    Name: Optional[str]
    Values: Optional[Sequence["_ValuesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetSegmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetSegmentDefinition"]:
        if not json_data:
            return None
        return cls(
            Bits=json_data.get("Bits"),
            Exclusive=json_data.get("Exclusive"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Values=deserialize_list(json_data.get("Values"), ValuesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetSegmentDefinition = SubnetSegmentDefinition


@dataclass
class ValuesDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValuesDefinition = ValuesDefinition


