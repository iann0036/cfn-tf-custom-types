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
    AlertNotificationEndpoints: Optional[Sequence[float]]
    CorrelationOperator: Optional[str]
    CreatedAt: Optional[str]
    CreatedBy: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IsEnabled: Optional[bool]
    Joins: Optional[Sequence[Sequence["_JoinsDefinition"]]]
    NotificationEmails: Optional[Sequence[str]]
    OutputType: Optional[str]
    SearchTimeframeMinutes: Optional[float]
    SuppressNotificationsMinutes: Optional[float]
    Tags: Optional[Sequence[str]]
    Title: Optional[str]
    UpdatedAt: Optional[str]
    UpdatedBy: Optional[str]
    SubComponents: Optional[Sequence["_SubComponentsDefinition"]]

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
            AlertNotificationEndpoints=json_data.get("AlertNotificationEndpoints"),
            CorrelationOperator=json_data.get("CorrelationOperator"),
            CreatedAt=json_data.get("CreatedAt"),
            CreatedBy=json_data.get("CreatedBy"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IsEnabled=json_data.get("IsEnabled"),
            Joins=deserialize_list(json_data.get("Joins"), <ResolvedType(ContainerType.MODEL, JoinsDefinition)>),
            NotificationEmails=json_data.get("NotificationEmails"),
            OutputType=json_data.get("OutputType"),
            SearchTimeframeMinutes=json_data.get("SearchTimeframeMinutes"),
            SuppressNotificationsMinutes=json_data.get("SuppressNotificationsMinutes"),
            Tags=json_data.get("Tags"),
            Title=json_data.get("Title"),
            UpdatedAt=json_data.get("UpdatedAt"),
            UpdatedBy=json_data.get("UpdatedBy"),
            SubComponents=deserialize_list(json_data.get("SubComponents"), SubComponentsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class JoinsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JoinsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JoinsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JoinsDefinition = JoinsDefinition


@dataclass
class SubComponentsDefinition(BaseModel):
    AccountIdsToQueryOn: Optional[Sequence[float]]
    FilterMust: Optional[Sequence[Sequence["_FilterMustDefinition"]]]
    FilterMustNot: Optional[Sequence[Sequence["_FilterMustNotDefinition"]]]
    GroupByAggregationFields: Optional[Sequence[str]]
    Operation: Optional[str]
    QueryString: Optional[str]
    ShouldQueryOnAllAccounts: Optional[bool]
    ValueAggregationField: Optional[str]
    ValueAggregationType: Optional[str]
    Columns: Optional[Sequence["_ColumnsDefinition"]]
    SeverityThresholdTiers: Optional[Sequence["_SeverityThresholdTiersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubComponentsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubComponentsDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountIdsToQueryOn=json_data.get("AccountIdsToQueryOn"),
            FilterMust=deserialize_list(json_data.get("FilterMust"), <ResolvedType(ContainerType.MODEL, FilterMustDefinition)>),
            FilterMustNot=deserialize_list(json_data.get("FilterMustNot"), <ResolvedType(ContainerType.MODEL, FilterMustNotDefinition)>),
            GroupByAggregationFields=json_data.get("GroupByAggregationFields"),
            Operation=json_data.get("Operation"),
            QueryString=json_data.get("QueryString"),
            ShouldQueryOnAllAccounts=json_data.get("ShouldQueryOnAllAccounts"),
            ValueAggregationField=json_data.get("ValueAggregationField"),
            ValueAggregationType=json_data.get("ValueAggregationType"),
            Columns=deserialize_list(json_data.get("Columns"), ColumnsDefinition),
            SeverityThresholdTiers=deserialize_list(json_data.get("SeverityThresholdTiers"), SeverityThresholdTiersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubComponentsDefinition = SubComponentsDefinition


@dataclass
class FilterMustDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterMustDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterMustDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterMustDefinition = FilterMustDefinition


@dataclass
class FilterMustNotDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterMustNotDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterMustNotDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterMustNotDefinition = FilterMustNotDefinition


@dataclass
class ColumnsDefinition(BaseModel):
    FieldName: Optional[str]
    Regex: Optional[str]
    Sort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnsDefinition"]:
        if not json_data:
            return None
        return cls(
            FieldName=json_data.get("FieldName"),
            Regex=json_data.get("Regex"),
            Sort=json_data.get("Sort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnsDefinition = ColumnsDefinition


@dataclass
class SeverityThresholdTiersDefinition(BaseModel):
    Severity: Optional[str]
    Threshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SeverityThresholdTiersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeverityThresholdTiersDefinition"]:
        if not json_data:
            return None
        return cls(
            Severity=json_data.get("Severity"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeverityThresholdTiersDefinition = SeverityThresholdTiersDefinition


