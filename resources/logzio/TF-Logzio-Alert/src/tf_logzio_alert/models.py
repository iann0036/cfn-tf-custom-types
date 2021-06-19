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
    Description: Optional[str]
    Filter: Optional[str]
    GroupByAggregationFields: Optional[Sequence[str]]
    Id: Optional[str]
    IsEnabled: Optional[bool]
    NotificationEmails: Optional[Sequence[str]]
    Operation: Optional[str]
    QueryString: Optional[str]
    SearchTimeframeMinutes: Optional[float]
    SuppressNotificationsMinutes: Optional[float]
    Tags: Optional[Sequence[str]]
    Title: Optional[str]
    ValueAggregationField: Optional[str]
    ValueAggregationType: Optional[str]
    SeverityThresholdTiers: Optional[Sequence["_SeverityThresholdTiersDefinition"]]

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
            Description=json_data.get("Description"),
            Filter=json_data.get("Filter"),
            GroupByAggregationFields=json_data.get("GroupByAggregationFields"),
            Id=json_data.get("Id"),
            IsEnabled=json_data.get("IsEnabled"),
            NotificationEmails=json_data.get("NotificationEmails"),
            Operation=json_data.get("Operation"),
            QueryString=json_data.get("QueryString"),
            SearchTimeframeMinutes=json_data.get("SearchTimeframeMinutes"),
            SuppressNotificationsMinutes=json_data.get("SuppressNotificationsMinutes"),
            Tags=json_data.get("Tags"),
            Title=json_data.get("Title"),
            ValueAggregationField=json_data.get("ValueAggregationField"),
            ValueAggregationType=json_data.get("ValueAggregationType"),
            SeverityThresholdTiers=deserialize_list(json_data.get("SeverityThresholdTiers"), SeverityThresholdTiersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


