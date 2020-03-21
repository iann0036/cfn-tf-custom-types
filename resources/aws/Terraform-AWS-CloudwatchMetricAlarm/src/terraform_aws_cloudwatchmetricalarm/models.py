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
    ActionsEnabled: Optional[bool]
    AlarmActions: Optional[Sequence[str]]
    AlarmDescription: Optional[str]
    AlarmName: Optional[str]
    Arn: Optional[str]
    ComparisonOperator: Optional[str]
    DatapointsToAlarm: Optional[float]
    Dimensions: Optional[Sequence["_Dimensions"]]
    EvaluateLowSampleCountPercentiles: Optional[str]
    EvaluationPeriods: Optional[float]
    ExtendedStatistic: Optional[str]
    InsufficientDataActions: Optional[Sequence[str]]
    MetricName: Optional[str]
    Namespace: Optional[str]
    OkActions: Optional[Sequence[str]]
    Period: Optional[float]
    Statistic: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Threshold: Optional[float]
    ThresholdMetricId: Optional[str]
    TreatMissingData: Optional[str]
    Unit: Optional[str]
    MetricQuery: Optional[Sequence["_MetricQuery"]]
    Metric: Optional[Sequence["_Metric"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ActionsEnabled=json_data.get("ActionsEnabled"),
            AlarmActions=json_data.get("AlarmActions"),
            AlarmDescription=json_data.get("AlarmDescription"),
            AlarmName=json_data.get("AlarmName"),
            Arn=json_data.get("Arn"),
            ComparisonOperator=json_data.get("ComparisonOperator"),
            DatapointsToAlarm=json_data.get("DatapointsToAlarm"),
            Dimensions=json_data.get("Dimensions"),
            EvaluateLowSampleCountPercentiles=json_data.get("EvaluateLowSampleCountPercentiles"),
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
            ExtendedStatistic=json_data.get("ExtendedStatistic"),
            InsufficientDataActions=json_data.get("InsufficientDataActions"),
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            OkActions=json_data.get("OkActions"),
            Period=json_data.get("Period"),
            Statistic=json_data.get("Statistic"),
            Tags=json_data.get("Tags"),
            Threshold=json_data.get("Threshold"),
            ThresholdMetricId=json_data.get("ThresholdMetricId"),
            TreatMissingData=json_data.get("TreatMissingData"),
            Unit=json_data.get("Unit"),
            MetricQuery=json_data.get("MetricQuery"),
            Metric=json_data.get("Metric"),
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


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class MetricQuery:
    Expression: Optional[str]
    Id: Optional[str]
    Label: Optional[str]
    ReturnData: Optional[bool]
    Metric: Optional[Sequence["_Metric"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricQuery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricQuery"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Id=json_data.get("Id"),
            Label=json_data.get("Label"),
            ReturnData=json_data.get("ReturnData"),
            Metric=json_data.get("Metric"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricQuery = MetricQuery


@dataclass
class Metric:
    Dimensions: Optional[Sequence["_Dimensions2"]]
    MetricName: Optional[str]
    Namespace: Optional[str]
    Period: Optional[float]
    Stat: Optional[str]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metric"]:
        if not json_data:
            return None
        return cls(
            Dimensions=json_data.get("Dimensions"),
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            Period=json_data.get("Period"),
            Stat=json_data.get("Stat"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metric = Metric


@dataclass
class Dimensions2:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dimensions2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dimensions2"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dimensions2 = Dimensions2


