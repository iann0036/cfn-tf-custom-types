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
    CalendarPeriod: Optional[str]
    DisplayName: Optional[str]
    Goal: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    RollingPeriodDays: Optional[float]
    Service: Optional[str]
    SloId: Optional[str]
    BasicSli: Optional[Sequence["_BasicSliDefinition"]]
    RequestBasedSli: Optional[Sequence["_RequestBasedSliDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    WindowsBasedSli: Optional[Sequence["_WindowsBasedSliDefinition"]]

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
            CalendarPeriod=json_data.get("CalendarPeriod"),
            DisplayName=json_data.get("DisplayName"),
            Goal=json_data.get("Goal"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            RollingPeriodDays=json_data.get("RollingPeriodDays"),
            Service=json_data.get("Service"),
            SloId=json_data.get("SloId"),
            BasicSli=deserialize_list(json_data.get("BasicSli"), BasicSliDefinition),
            RequestBasedSli=deserialize_list(json_data.get("RequestBasedSli"), RequestBasedSliDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            WindowsBasedSli=deserialize_list(json_data.get("WindowsBasedSli"), WindowsBasedSliDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BasicSliDefinition(BaseModel):
    Location: Optional[Sequence[str]]
    Method: Optional[Sequence[str]]
    Version: Optional[Sequence[str]]
    Availability: Optional[Sequence["_AvailabilityDefinition"]]
    Latency: Optional[Sequence["_LatencyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BasicSliDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BasicSliDefinition"]:
        if not json_data:
            return None
        return cls(
            Location=json_data.get("Location"),
            Method=json_data.get("Method"),
            Version=json_data.get("Version"),
            Availability=deserialize_list(json_data.get("Availability"), AvailabilityDefinition),
            Latency=deserialize_list(json_data.get("Latency"), LatencyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BasicSliDefinition = BasicSliDefinition


@dataclass
class AvailabilityDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AvailabilityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AvailabilityDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AvailabilityDefinition = AvailabilityDefinition


@dataclass
class LatencyDefinition(BaseModel):
    Threshold: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LatencyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LatencyDefinition"]:
        if not json_data:
            return None
        return cls(
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LatencyDefinition = LatencyDefinition


@dataclass
class RequestBasedSliDefinition(BaseModel):
    DistributionCut: Optional[Sequence["_DistributionCutDefinition"]]
    GoodTotalRatio: Optional[Sequence["_GoodTotalRatioDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RequestBasedSliDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestBasedSliDefinition"]:
        if not json_data:
            return None
        return cls(
            DistributionCut=deserialize_list(json_data.get("DistributionCut"), DistributionCutDefinition),
            GoodTotalRatio=deserialize_list(json_data.get("GoodTotalRatio"), GoodTotalRatioDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestBasedSliDefinition = RequestBasedSliDefinition


@dataclass
class DistributionCutDefinition(BaseModel):
    DistributionFilter: Optional[str]
    Range: Optional[Sequence["_RangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DistributionCutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DistributionCutDefinition"]:
        if not json_data:
            return None
        return cls(
            DistributionFilter=json_data.get("DistributionFilter"),
            Range=deserialize_list(json_data.get("Range"), RangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DistributionCutDefinition = DistributionCutDefinition


@dataclass
class RangeDefinition(BaseModel):
    Max: Optional[float]
    Min: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangeDefinition = RangeDefinition


@dataclass
class GoodTotalRatioDefinition(BaseModel):
    BadServiceFilter: Optional[str]
    GoodServiceFilter: Optional[str]
    TotalServiceFilter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GoodTotalRatioDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GoodTotalRatioDefinition"]:
        if not json_data:
            return None
        return cls(
            BadServiceFilter=json_data.get("BadServiceFilter"),
            GoodServiceFilter=json_data.get("GoodServiceFilter"),
            TotalServiceFilter=json_data.get("TotalServiceFilter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GoodTotalRatioDefinition = GoodTotalRatioDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class WindowsBasedSliDefinition(BaseModel):
    GoodBadMetricFilter: Optional[str]
    WindowPeriod: Optional[str]
    GoodTotalRatioThreshold: Optional[Sequence["_GoodTotalRatioThresholdDefinition"]]
    MetricMeanInRange: Optional[Sequence["_MetricMeanInRangeDefinition"]]
    MetricSumInRange: Optional[Sequence["_MetricSumInRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WindowsBasedSliDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WindowsBasedSliDefinition"]:
        if not json_data:
            return None
        return cls(
            GoodBadMetricFilter=json_data.get("GoodBadMetricFilter"),
            WindowPeriod=json_data.get("WindowPeriod"),
            GoodTotalRatioThreshold=deserialize_list(json_data.get("GoodTotalRatioThreshold"), GoodTotalRatioThresholdDefinition),
            MetricMeanInRange=deserialize_list(json_data.get("MetricMeanInRange"), MetricMeanInRangeDefinition),
            MetricSumInRange=deserialize_list(json_data.get("MetricSumInRange"), MetricSumInRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WindowsBasedSliDefinition = WindowsBasedSliDefinition


@dataclass
class GoodTotalRatioThresholdDefinition(BaseModel):
    Threshold: Optional[float]
    BasicSliPerformance: Optional[Sequence["_BasicSliPerformanceDefinition"]]
    Performance: Optional[Sequence["_PerformanceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GoodTotalRatioThresholdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GoodTotalRatioThresholdDefinition"]:
        if not json_data:
            return None
        return cls(
            Threshold=json_data.get("Threshold"),
            BasicSliPerformance=deserialize_list(json_data.get("BasicSliPerformance"), BasicSliPerformanceDefinition),
            Performance=deserialize_list(json_data.get("Performance"), PerformanceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GoodTotalRatioThresholdDefinition = GoodTotalRatioThresholdDefinition


@dataclass
class BasicSliPerformanceDefinition(BaseModel):
    Location: Optional[Sequence[str]]
    Method: Optional[Sequence[str]]
    Version: Optional[Sequence[str]]
    Availability: Optional[Sequence["_AvailabilityDefinition"]]
    Latency: Optional[Sequence["_LatencyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BasicSliPerformanceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BasicSliPerformanceDefinition"]:
        if not json_data:
            return None
        return cls(
            Location=json_data.get("Location"),
            Method=json_data.get("Method"),
            Version=json_data.get("Version"),
            Availability=deserialize_list(json_data.get("Availability"), AvailabilityDefinition),
            Latency=deserialize_list(json_data.get("Latency"), LatencyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BasicSliPerformanceDefinition = BasicSliPerformanceDefinition


@dataclass
class PerformanceDefinition(BaseModel):
    DistributionCut: Optional[Sequence["_DistributionCutDefinition"]]
    GoodTotalRatio: Optional[Sequence["_GoodTotalRatioDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PerformanceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PerformanceDefinition"]:
        if not json_data:
            return None
        return cls(
            DistributionCut=deserialize_list(json_data.get("DistributionCut"), DistributionCutDefinition),
            GoodTotalRatio=deserialize_list(json_data.get("GoodTotalRatio"), GoodTotalRatioDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PerformanceDefinition = PerformanceDefinition


@dataclass
class MetricMeanInRangeDefinition(BaseModel):
    TimeSeries: Optional[str]
    Range: Optional[Sequence["_RangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricMeanInRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricMeanInRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            TimeSeries=json_data.get("TimeSeries"),
            Range=deserialize_list(json_data.get("Range"), RangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricMeanInRangeDefinition = MetricMeanInRangeDefinition


@dataclass
class MetricSumInRangeDefinition(BaseModel):
    TimeSeries: Optional[str]
    Range: Optional[Sequence["_RangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricSumInRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricSumInRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            TimeSeries=json_data.get("TimeSeries"),
            Range=deserialize_list(json_data.get("Range"), RangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricSumInRangeDefinition = MetricSumInRangeDefinition


