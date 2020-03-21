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
    AlarmActions: Optional[Sequence[str]]
    CloudMonitorGroupId: Optional[float]
    ComparisonOperator: Optional[str]
    Description: Optional[str]
    Dimensions: Optional[Sequence["_Dimensions"]]
    Enable: Optional[bool]
    EvaluationCount: Optional[float]
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
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AlarmActions=json_data.get("AlarmActions"),
            CloudMonitorGroupId=json_data.get("CloudMonitorGroupId"),
            ComparisonOperator=json_data.get("ComparisonOperator"),
            Description=json_data.get("Description"),
            Dimensions=json_data.get("Dimensions"),
            Enable=json_data.get("Enable"),
            EvaluationCount=json_data.get("EvaluationCount"),
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
class Dimensions:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dimensions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dimensions"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dimensions = Dimensions


