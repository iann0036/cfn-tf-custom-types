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
    ActualNodeCount: Optional[float]
    AutoScale: Optional[bool]
    ClusterId: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    MaxNodes: Optional[float]
    MinNodes: Optional[float]
    Name: Optional[str]
    NodeCount: Optional[float]
    Nodes: Optional[Sequence["_NodesDefinition"]]
    Size: Optional[str]
    Tags: Optional[Sequence[str]]
    Taint: Optional[Sequence["_TaintDefinition"]]

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
            ActualNodeCount=json_data.get("ActualNodeCount"),
            AutoScale=json_data.get("AutoScale"),
            ClusterId=json_data.get("ClusterId"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            MaxNodes=json_data.get("MaxNodes"),
            MinNodes=json_data.get("MinNodes"),
            Name=json_data.get("Name"),
            NodeCount=json_data.get("NodeCount"),
            Nodes=deserialize_list(json_data.get("Nodes"), NodesDefinition),
            Size=json_data.get("Size"),
            Tags=json_data.get("Tags"),
            Taint=deserialize_list(json_data.get("Taint"), TaintDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class NodesDefinition(BaseModel):
    CreatedAt: Optional[str]
    DropletId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    UpdatedAt: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodesDefinition"]:
        if not json_data:
            return None
        return cls(
            CreatedAt=json_data.get("CreatedAt"),
            DropletId=json_data.get("DropletId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            UpdatedAt=json_data.get("UpdatedAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodesDefinition = NodesDefinition


@dataclass
class TaintDefinition(BaseModel):
    Effect: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaintDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaintDefinition"]:
        if not json_data:
            return None
        return cls(
            Effect=json_data.get("Effect"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaintDefinition = TaintDefinition


