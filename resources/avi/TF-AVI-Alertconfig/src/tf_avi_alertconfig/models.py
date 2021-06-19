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
    ActionGroupRef: Optional[str]
    AutoscaleAlert: Optional[bool]
    Category: Optional[str]
    Description: Optional[str]
    Enabled: Optional[bool]
    ExpiryTime: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    ObjUuid: Optional[str]
    ObjectType: Optional[str]
    Recommendation: Optional[str]
    RollingWindow: Optional[float]
    Source: Optional[str]
    Summary: Optional[str]
    TenantRef: Optional[str]
    Threshold: Optional[float]
    Throttle: Optional[float]
    Uuid: Optional[str]
    AlertRule: Optional[Sequence["_AlertRuleDefinition"]]

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
            ActionGroupRef=json_data.get("ActionGroupRef"),
            AutoscaleAlert=json_data.get("AutoscaleAlert"),
            Category=json_data.get("Category"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            ExpiryTime=json_data.get("ExpiryTime"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ObjUuid=json_data.get("ObjUuid"),
            ObjectType=json_data.get("ObjectType"),
            Recommendation=json_data.get("Recommendation"),
            RollingWindow=json_data.get("RollingWindow"),
            Source=json_data.get("Source"),
            Summary=json_data.get("Summary"),
            TenantRef=json_data.get("TenantRef"),
            Threshold=json_data.get("Threshold"),
            Throttle=json_data.get("Throttle"),
            Uuid=json_data.get("Uuid"),
            AlertRule=deserialize_list(json_data.get("AlertRule"), AlertRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AlertRuleDefinition(BaseModel):
    EventMatchFilter: Optional[str]
    Operator: Optional[str]
    ConnAppLogRule: Optional[Sequence["_ConnAppLogRuleDefinition"]]
    MetricsRule: Optional[Sequence["_MetricsRuleDefinition"]]
    SysEventRule: Optional[Sequence["_SysEventRuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AlertRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlertRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            EventMatchFilter=json_data.get("EventMatchFilter"),
            Operator=json_data.get("Operator"),
            ConnAppLogRule=deserialize_list(json_data.get("ConnAppLogRule"), ConnAppLogRuleDefinition),
            MetricsRule=deserialize_list(json_data.get("MetricsRule"), MetricsRuleDefinition),
            SysEventRule=deserialize_list(json_data.get("SysEventRule"), SysEventRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlertRuleDefinition = AlertRuleDefinition


@dataclass
class ConnAppLogRuleDefinition(BaseModel):
    FilterAction: Optional[str]
    FilterString: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnAppLogRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnAppLogRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            FilterAction=json_data.get("FilterAction"),
            FilterString=json_data.get("FilterString"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnAppLogRuleDefinition = ConnAppLogRuleDefinition


@dataclass
class MetricsRuleDefinition(BaseModel):
    Duration: Optional[float]
    MetricId: Optional[str]
    MetricThreshold: Optional[Sequence["_MetricThresholdDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricsRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricsRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            MetricId=json_data.get("MetricId"),
            MetricThreshold=deserialize_list(json_data.get("MetricThreshold"), MetricThresholdDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricsRuleDefinition = MetricsRuleDefinition


@dataclass
class MetricThresholdDefinition(BaseModel):
    Comparator: Optional[str]
    Threshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MetricThresholdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricThresholdDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparator=json_data.get("Comparator"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricThresholdDefinition = MetricThresholdDefinition


@dataclass
class SysEventRuleDefinition(BaseModel):
    EventId: Optional[str]
    NotCond: Optional[bool]
    EventDetails: Optional[Sequence["_EventDetailsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SysEventRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SysEventRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            EventId=json_data.get("EventId"),
            NotCond=json_data.get("NotCond"),
            EventDetails=deserialize_list(json_data.get("EventDetails"), EventDetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SysEventRuleDefinition = SysEventRuleDefinition


@dataclass
class EventDetailsDefinition(BaseModel):
    Comparator: Optional[str]
    EventDetailsKey: Optional[str]
    EventDetailsValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparator=json_data.get("Comparator"),
            EventDetailsKey=json_data.get("EventDetailsKey"),
            EventDetailsValue=json_data.get("EventDetailsValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventDetailsDefinition = EventDetailsDefinition


