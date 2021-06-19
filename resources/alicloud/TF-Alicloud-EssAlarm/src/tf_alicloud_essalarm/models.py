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
    AlarmActions: Optional[Sequence[str]]
    CloudMonitorGroupId: Optional[float]
    ComparisonOperator: Optional[str]
    Description: Optional[str]
    Dimensions: Optional[Sequence["_DimensionsDefinition"]]
    Enable: Optional[bool]
    EvaluationCount: Optional[float]
    Id: Optional[str]
    MetricName: Optional[str]
    MetricType: Optional[str]
    Name: Optional[str]
    Period: Optional[float]
    ScalingGroupId: Optional[str]
    State: Optional[str]
    Statistics: Optional[str]
    Threshold: Optional[str]

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
            AlarmActions=json_data.get("AlarmActions"),
            CloudMonitorGroupId=json_data.get("CloudMonitorGroupId"),
            ComparisonOperator=json_data.get("ComparisonOperator"),
            Description=json_data.get("Description"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition),
            Enable=json_data.get("Enable"),
            EvaluationCount=json_data.get("EvaluationCount"),
            Id=json_data.get("Id"),
            MetricName=json_data.get("MetricName"),
            MetricType=json_data.get("MetricType"),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
            ScalingGroupId=json_data.get("ScalingGroupId"),
            State=json_data.get("State"),
            Statistics=json_data.get("Statistics"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DimensionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionsDefinition = DimensionsDefinition


