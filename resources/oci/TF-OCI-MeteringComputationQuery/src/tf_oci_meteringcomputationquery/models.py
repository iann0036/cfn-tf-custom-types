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
    CompartmentId: Optional[str]
    Id: Optional[str]
    QueryDefinition: Optional[Sequence["_QueryDefinitionDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            CompartmentId=json_data.get("CompartmentId"),
            Id=json_data.get("Id"),
            QueryDefinition=deserialize_list(json_data.get("QueryDefinition"), QueryDefinitionDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class QueryDefinitionDefinition(BaseModel):
    DisplayName: Optional[str]
    Version: Optional[float]
    CostAnalysisUi: Optional[Sequence["_CostAnalysisUiDefinition"]]
    ReportQuery: Optional[Sequence["_ReportQueryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            Version=json_data.get("Version"),
            CostAnalysisUi=deserialize_list(json_data.get("CostAnalysisUi"), CostAnalysisUiDefinition),
            ReportQuery=deserialize_list(json_data.get("ReportQuery"), ReportQueryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryDefinitionDefinition = QueryDefinitionDefinition


@dataclass
class CostAnalysisUiDefinition(BaseModel):
    Graph: Optional[str]
    IsCumulativeGraph: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CostAnalysisUiDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CostAnalysisUiDefinition"]:
        if not json_data:
            return None
        return cls(
            Graph=json_data.get("Graph"),
            IsCumulativeGraph=json_data.get("IsCumulativeGraph"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CostAnalysisUiDefinition = CostAnalysisUiDefinition


@dataclass
class ReportQueryDefinition(BaseModel):
    CompartmentDepth: Optional[float]
    DateRangeName: Optional[str]
    Filter: Optional[str]
    Granularity: Optional[str]
    GroupBy: Optional[Sequence[str]]
    IsAggregateByTime: Optional[bool]
    QueryType: Optional[str]
    TenantId: Optional[str]
    TimeUsageEnded: Optional[str]
    TimeUsageStarted: Optional[str]
    Forecast: Optional[Sequence["_ForecastDefinition"]]
    GroupByTag: Optional[Sequence["_GroupByTagDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReportQueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReportQueryDefinition"]:
        if not json_data:
            return None
        return cls(
            CompartmentDepth=json_data.get("CompartmentDepth"),
            DateRangeName=json_data.get("DateRangeName"),
            Filter=json_data.get("Filter"),
            Granularity=json_data.get("Granularity"),
            GroupBy=json_data.get("GroupBy"),
            IsAggregateByTime=json_data.get("IsAggregateByTime"),
            QueryType=json_data.get("QueryType"),
            TenantId=json_data.get("TenantId"),
            TimeUsageEnded=json_data.get("TimeUsageEnded"),
            TimeUsageStarted=json_data.get("TimeUsageStarted"),
            Forecast=deserialize_list(json_data.get("Forecast"), ForecastDefinition),
            GroupByTag=deserialize_list(json_data.get("GroupByTag"), GroupByTagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReportQueryDefinition = ReportQueryDefinition


@dataclass
class ForecastDefinition(BaseModel):
    ForecastType: Optional[str]
    TimeForecastEnded: Optional[str]
    TimeForecastStarted: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForecastDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForecastDefinition"]:
        if not json_data:
            return None
        return cls(
            ForecastType=json_data.get("ForecastType"),
            TimeForecastEnded=json_data.get("TimeForecastEnded"),
            TimeForecastStarted=json_data.get("TimeForecastStarted"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForecastDefinition = ForecastDefinition


@dataclass
class GroupByTagDefinition(BaseModel):
    Key: Optional[str]
    Namespace: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GroupByTagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupByTagDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Namespace=json_data.get("Namespace"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupByTagDefinition = GroupByTagDefinition


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


