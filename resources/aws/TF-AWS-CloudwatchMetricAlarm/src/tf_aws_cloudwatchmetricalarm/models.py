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
    ActionsEnabled: Optional[bool]
    AlarmActions: Optional[Sequence[str]]
    AlarmDescription: Optional[str]
    AlarmName: Optional[str]
    Arn: Optional[str]
    ComparisonOperator: Optional[str]
    DatapointsToAlarm: Optional[float]
    Dimensions: Optional[Sequence["_DimensionsDefinition"]]
    EvaluateLowSampleCountPercentiles: Optional[str]
    EvaluationPeriods: Optional[float]
    ExtendedStatistic: Optional[str]
    Id: Optional[str]
    InsufficientDataActions: Optional[Sequence[str]]
    MetricName: Optional[str]
    Namespace: Optional[str]
    OkActions: Optional[Sequence[str]]
    Period: Optional[float]
    Statistic: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Threshold: Optional[float]
    ThresholdMetricId: Optional[str]
    TreatMissingData: Optional[str]
    Unit: Optional[str]
    MetricQuery: Optional[Sequence["_MetricQueryDefinition"]]

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
            ActionsEnabled=json_data.get("ActionsEnabled"),
            AlarmActions=json_data.get("AlarmActions"),
            AlarmDescription=json_data.get("AlarmDescription"),
            AlarmName=json_data.get("AlarmName"),
            Arn=json_data.get("Arn"),
            ComparisonOperator=json_data.get("ComparisonOperator"),
            DatapointsToAlarm=json_data.get("DatapointsToAlarm"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition),
            EvaluateLowSampleCountPercentiles=json_data.get("EvaluateLowSampleCountPercentiles"),
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
            ExtendedStatistic=json_data.get("ExtendedStatistic"),
            Id=json_data.get("Id"),
            InsufficientDataActions=json_data.get("InsufficientDataActions"),
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            OkActions=json_data.get("OkActions"),
            Period=json_data.get("Period"),
            Statistic=json_data.get("Statistic"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Threshold=json_data.get("Threshold"),
            ThresholdMetricId=json_data.get("ThresholdMetricId"),
            TreatMissingData=json_data.get("TreatMissingData"),
            Unit=json_data.get("Unit"),
            MetricQuery=deserialize_list(json_data.get("MetricQuery"), MetricQueryDefinition),
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


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class MetricQueryDefinition(BaseModel):
    Expression: Optional[str]
    Id: Optional[str]
    Label: Optional[str]
    ReturnData: Optional[bool]
    Metric: Optional[Sequence["_MetricDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricQueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricQueryDefinition"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Id=json_data.get("Id"),
            Label=json_data.get("Label"),
            ReturnData=json_data.get("ReturnData"),
            Metric=deserialize_list(json_data.get("Metric"), MetricDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricQueryDefinition = MetricQueryDefinition


@dataclass
class MetricDefinition(BaseModel):
    Dimensions: Optional[Sequence["_DimensionsDefinition2"]]
    MetricName: Optional[str]
    Namespace: Optional[str]
    Period: Optional[float]
    Stat: Optional[str]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDefinition"]:
        if not json_data:
            return None
        return cls(
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition2),
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            Period=json_data.get("Period"),
            Stat=json_data.get("Stat"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDefinition = MetricDefinition


@dataclass
class DimensionsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionsDefinition2 = DimensionsDefinition2


