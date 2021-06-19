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
    AcknowledgementTimeout: Optional[str]
    AlertCreation: Optional[str]
    AlertGrouping: Optional[str]
    AlertGroupingTimeout: Optional[float]
    AutoResolveTimeout: Optional[str]
    CreatedAt: Optional[str]
    Description: Optional[str]
    EscalationPolicy: Optional[str]
    HtmlUrl: Optional[str]
    Id: Optional[str]
    LastIncidentTimestamp: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    IncidentUrgencyRule: Optional[Sequence["_IncidentUrgencyRuleDefinition"]]
    ScheduledActions: Optional[Sequence["_ScheduledActionsDefinition"]]
    SupportHours: Optional[Sequence["_SupportHoursDefinition"]]

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
            AcknowledgementTimeout=json_data.get("AcknowledgementTimeout"),
            AlertCreation=json_data.get("AlertCreation"),
            AlertGrouping=json_data.get("AlertGrouping"),
            AlertGroupingTimeout=json_data.get("AlertGroupingTimeout"),
            AutoResolveTimeout=json_data.get("AutoResolveTimeout"),
            CreatedAt=json_data.get("CreatedAt"),
            Description=json_data.get("Description"),
            EscalationPolicy=json_data.get("EscalationPolicy"),
            HtmlUrl=json_data.get("HtmlUrl"),
            Id=json_data.get("Id"),
            LastIncidentTimestamp=json_data.get("LastIncidentTimestamp"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            IncidentUrgencyRule=deserialize_list(json_data.get("IncidentUrgencyRule"), IncidentUrgencyRuleDefinition),
            ScheduledActions=deserialize_list(json_data.get("ScheduledActions"), ScheduledActionsDefinition),
            SupportHours=deserialize_list(json_data.get("SupportHours"), SupportHoursDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IncidentUrgencyRuleDefinition(BaseModel):
    Type: Optional[str]
    Urgency: Optional[str]
    DuringSupportHours: Optional[Sequence["_DuringSupportHoursDefinition"]]
    OutsideSupportHours: Optional[Sequence["_OutsideSupportHoursDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IncidentUrgencyRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IncidentUrgencyRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Urgency=json_data.get("Urgency"),
            DuringSupportHours=deserialize_list(json_data.get("DuringSupportHours"), DuringSupportHoursDefinition),
            OutsideSupportHours=deserialize_list(json_data.get("OutsideSupportHours"), OutsideSupportHoursDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IncidentUrgencyRuleDefinition = IncidentUrgencyRuleDefinition


@dataclass
class DuringSupportHoursDefinition(BaseModel):
    Type: Optional[str]
    Urgency: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DuringSupportHoursDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DuringSupportHoursDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Urgency=json_data.get("Urgency"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DuringSupportHoursDefinition = DuringSupportHoursDefinition


@dataclass
class OutsideSupportHoursDefinition(BaseModel):
    Type: Optional[str]
    Urgency: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutsideSupportHoursDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutsideSupportHoursDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Urgency=json_data.get("Urgency"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutsideSupportHoursDefinition = OutsideSupportHoursDefinition


@dataclass
class ScheduledActionsDefinition(BaseModel):
    ToUrgency: Optional[str]
    Type: Optional[str]
    At: Optional[Sequence["_AtDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduledActionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledActionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ToUrgency=json_data.get("ToUrgency"),
            Type=json_data.get("Type"),
            At=deserialize_list(json_data.get("At"), AtDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledActionsDefinition = ScheduledActionsDefinition


@dataclass
class AtDefinition(BaseModel):
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AtDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AtDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AtDefinition = AtDefinition


@dataclass
class SupportHoursDefinition(BaseModel):
    DaysOfWeek: Optional[Sequence[float]]
    EndTime: Optional[str]
    StartTime: Optional[str]
    TimeZone: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SupportHoursDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SupportHoursDefinition"]:
        if not json_data:
            return None
        return cls(
            DaysOfWeek=json_data.get("DaysOfWeek"),
            EndTime=json_data.get("EndTime"),
            StartTime=json_data.get("StartTime"),
            TimeZone=json_data.get("TimeZone"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SupportHoursDefinition = SupportHoursDefinition


