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
    Active: Optional[bool]
    AutoResolutionTimeout: Optional[str]
    Email: Optional[str]
    EmailFiltered: Optional[bool]
    EmailResolveFiltered: Optional[bool]
    EscalationPolicy: Optional[str]
    FilterOperator: Optional[str]
    Id: Optional[str]
    IncidentCreation: Optional[str]
    IncidentPriorityRule: Optional[str]
    IntegrationKey: Optional[str]
    IntegrationType: Optional[str]
    IntegrationUrl: Optional[str]
    Name: Optional[str]
    ResolveFilterOperator: Optional[str]
    Status: Optional[str]
    Teams: Optional[Sequence[float]]
    AutotaskMetadata: Optional[Sequence["_AutotaskMetadataDefinition"]]
    EmailPredicate: Optional[Sequence["_EmailPredicateDefinition"]]
    EmailResolvePredicate: Optional[Sequence["_EmailResolvePredicateDefinition"]]
    Heartbeat: Optional[Sequence["_HeartbeatDefinition"]]
    ResolveKeyExtractor: Optional[Sequence["_ResolveKeyExtractorDefinition"]]
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
            Active=json_data.get("Active"),
            AutoResolutionTimeout=json_data.get("AutoResolutionTimeout"),
            Email=json_data.get("Email"),
            EmailFiltered=json_data.get("EmailFiltered"),
            EmailResolveFiltered=json_data.get("EmailResolveFiltered"),
            EscalationPolicy=json_data.get("EscalationPolicy"),
            FilterOperator=json_data.get("FilterOperator"),
            Id=json_data.get("Id"),
            IncidentCreation=json_data.get("IncidentCreation"),
            IncidentPriorityRule=json_data.get("IncidentPriorityRule"),
            IntegrationKey=json_data.get("IntegrationKey"),
            IntegrationType=json_data.get("IntegrationType"),
            IntegrationUrl=json_data.get("IntegrationUrl"),
            Name=json_data.get("Name"),
            ResolveFilterOperator=json_data.get("ResolveFilterOperator"),
            Status=json_data.get("Status"),
            Teams=json_data.get("Teams"),
            AutotaskMetadata=deserialize_list(json_data.get("AutotaskMetadata"), AutotaskMetadataDefinition),
            EmailPredicate=deserialize_list(json_data.get("EmailPredicate"), EmailPredicateDefinition),
            EmailResolvePredicate=deserialize_list(json_data.get("EmailResolvePredicate"), EmailResolvePredicateDefinition),
            Heartbeat=deserialize_list(json_data.get("Heartbeat"), HeartbeatDefinition),
            ResolveKeyExtractor=deserialize_list(json_data.get("ResolveKeyExtractor"), ResolveKeyExtractorDefinition),
            SupportHours=deserialize_list(json_data.get("SupportHours"), SupportHoursDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutotaskMetadataDefinition(BaseModel):
    Secret: Optional[str]
    Username: Optional[str]
    WebServer: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutotaskMetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutotaskMetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Secret=json_data.get("Secret"),
            Username=json_data.get("Username"),
            WebServer=json_data.get("WebServer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutotaskMetadataDefinition = AutotaskMetadataDefinition


@dataclass
class EmailPredicateDefinition(BaseModel):
    Criteria: Optional[str]
    Field: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmailPredicateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailPredicateDefinition"]:
        if not json_data:
            return None
        return cls(
            Criteria=json_data.get("Criteria"),
            Field=json_data.get("Field"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailPredicateDefinition = EmailPredicateDefinition


@dataclass
class EmailResolvePredicateDefinition(BaseModel):
    Criteria: Optional[str]
    Field: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmailResolvePredicateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailResolvePredicateDefinition"]:
        if not json_data:
            return None
        return cls(
            Criteria=json_data.get("Criteria"),
            Field=json_data.get("Field"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailResolvePredicateDefinition = EmailResolvePredicateDefinition


@dataclass
class HeartbeatDefinition(BaseModel):
    IntervalSec: Optional[float]
    Summary: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeartbeatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeartbeatDefinition"]:
        if not json_data:
            return None
        return cls(
            IntervalSec=json_data.get("IntervalSec"),
            Summary=json_data.get("Summary"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeartbeatDefinition = HeartbeatDefinition


@dataclass
class ResolveKeyExtractorDefinition(BaseModel):
    Criteria: Optional[str]
    Field: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResolveKeyExtractorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResolveKeyExtractorDefinition"]:
        if not json_data:
            return None
        return cls(
            Criteria=json_data.get("Criteria"),
            Field=json_data.get("Field"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResolveKeyExtractorDefinition = ResolveKeyExtractorDefinition


@dataclass
class SupportHoursDefinition(BaseModel):
    AutoRaiseIncidents: Optional[bool]
    Timezone: Optional[str]
    SupportDays: Optional[Sequence["_SupportDaysDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SupportHoursDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SupportHoursDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoRaiseIncidents=json_data.get("AutoRaiseIncidents"),
            Timezone=json_data.get("Timezone"),
            SupportDays=deserialize_list(json_data.get("SupportDays"), SupportDaysDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SupportHoursDefinition = SupportHoursDefinition


@dataclass
class SupportDaysDefinition(BaseModel):
    Friday: Optional[Sequence["_FridayDefinition"]]
    Monday: Optional[Sequence["_MondayDefinition"]]
    Saturday: Optional[Sequence["_SaturdayDefinition"]]
    Sunday: Optional[Sequence["_SundayDefinition"]]
    Thursday: Optional[Sequence["_ThursdayDefinition"]]
    Tuesday: Optional[Sequence["_TuesdayDefinition"]]
    Wednesday: Optional[Sequence["_WednesdayDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SupportDaysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SupportDaysDefinition"]:
        if not json_data:
            return None
        return cls(
            Friday=deserialize_list(json_data.get("Friday"), FridayDefinition),
            Monday=deserialize_list(json_data.get("Monday"), MondayDefinition),
            Saturday=deserialize_list(json_data.get("Saturday"), SaturdayDefinition),
            Sunday=deserialize_list(json_data.get("Sunday"), SundayDefinition),
            Thursday=deserialize_list(json_data.get("Thursday"), ThursdayDefinition),
            Tuesday=deserialize_list(json_data.get("Tuesday"), TuesdayDefinition),
            Wednesday=deserialize_list(json_data.get("Wednesday"), WednesdayDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SupportDaysDefinition = SupportDaysDefinition


@dataclass
class FridayDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FridayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FridayDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FridayDefinition = FridayDefinition


@dataclass
class MondayDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MondayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MondayDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MondayDefinition = MondayDefinition


@dataclass
class SaturdayDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SaturdayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SaturdayDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SaturdayDefinition = SaturdayDefinition


@dataclass
class SundayDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SundayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SundayDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SundayDefinition = SundayDefinition


@dataclass
class ThursdayDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThursdayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThursdayDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThursdayDefinition = ThursdayDefinition


@dataclass
class TuesdayDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TuesdayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TuesdayDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TuesdayDefinition = TuesdayDefinition


@dataclass
class WednesdayDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WednesdayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WednesdayDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WednesdayDefinition = WednesdayDefinition


