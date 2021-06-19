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
    Name: Optional[str]
    Compute: Optional[Sequence["_ComputeDefinition"]]
    Filter: Optional[Sequence["_FilterDefinition"]]
    GroupBy: Optional[Sequence["_GroupByDefinition"]]

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
            Name=json_data.get("Name"),
            Compute=deserialize_list(json_data.get("Compute"), ComputeDefinition),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
            GroupBy=deserialize_list(json_data.get("GroupBy"), GroupByDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ComputeDefinition(BaseModel):
    AggregationType: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComputeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComputeDefinition"]:
        if not json_data:
            return None
        return cls(
            AggregationType=json_data.get("AggregationType"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComputeDefinition = ComputeDefinition


@dataclass
class FilterDefinition(BaseModel):
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class GroupByDefinition(BaseModel):
    Path: Optional[str]
    TagName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GroupByDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupByDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            TagName=json_data.get("TagName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupByDefinition = GroupByDefinition


