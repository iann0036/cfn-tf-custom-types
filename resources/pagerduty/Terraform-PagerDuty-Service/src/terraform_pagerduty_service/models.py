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
    AcknowledgementTimeout: Optional[str]
    AlertCreation: Optional[str]
    AlertGrouping: Optional[str]
    AlertGroupingTimeout: Optional[float]
    AutoResolveTimeout: Optional[str]
    CreatedAt: Optional[str]
    Description: Optional[str]
    EscalationPolicy: Optional[str]
    HtmlUrl: Optional[str]
    LastIncidentTimestamp: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    IncidentUrgencyRule: Optional[Sequence["_IncidentUrgencyRule"]]
    ScheduledActions: Optional[Sequence["_ScheduledActions"]]
    SupportHours: Optional[Sequence["_SupportHours"]]
    DuringSupportHours: Optional[Sequence["_DuringSupportHours"]]
    OutsideSupportHours: Optional[Sequence["_OutsideSupportHours"]]
    At: Optional[Sequence["_At"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            LastIncidentTimestamp=json_data.get("LastIncidentTimestamp"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            IncidentUrgencyRule=json_data.get("IncidentUrgencyRule"),
            ScheduledActions=json_data.get("ScheduledActions"),
            SupportHours=json_data.get("SupportHours"),
            DuringSupportHours=json_data.get("DuringSupportHours"),
            OutsideSupportHours=json_data.get("OutsideSupportHours"),
            At=json_data.get("At"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IncidentUrgencyRule:
    Type: Optional[str]
    Urgency: Optional[str]
    DuringSupportHours: Optional[Sequence["_DuringSupportHours"]]
    OutsideSupportHours: Optional[Sequence["_OutsideSupportHours"]]

    @classmethod
    def _deserialize(
        cls: Type["_IncidentUrgencyRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IncidentUrgencyRule"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Urgency=json_data.get("Urgency"),
            DuringSupportHours=json_data.get("DuringSupportHours"),
            OutsideSupportHours=json_data.get("OutsideSupportHours"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IncidentUrgencyRule = IncidentUrgencyRule


@dataclass
class DuringSupportHours:
    Type: Optional[str]
    Urgency: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DuringSupportHours"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DuringSupportHours"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Urgency=json_data.get("Urgency"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DuringSupportHours = DuringSupportHours


@dataclass
class OutsideSupportHours:
    Type: Optional[str]
    Urgency: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutsideSupportHours"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutsideSupportHours"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Urgency=json_data.get("Urgency"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutsideSupportHours = OutsideSupportHours


@dataclass
class ScheduledActions:
    ToUrgency: Optional[str]
    Type: Optional[str]
    At: Optional[Sequence["_At"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduledActions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledActions"]:
        if not json_data:
            return None
        return cls(
            ToUrgency=json_data.get("ToUrgency"),
            Type=json_data.get("Type"),
            At=json_data.get("At"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledActions = ScheduledActions


@dataclass
class At:
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_At"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_At"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_At = At


@dataclass
class SupportHours:
    DaysOfWeek: Optional[Sequence[float]]
    EndTime: Optional[str]
    StartTime: Optional[str]
    TimeZone: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SupportHours"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SupportHours"]:
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
_SupportHours = SupportHours


