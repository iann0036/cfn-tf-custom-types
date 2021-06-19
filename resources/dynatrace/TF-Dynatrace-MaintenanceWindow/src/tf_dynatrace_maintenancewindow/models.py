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
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    SuppressSynthMonExec: Optional[bool]
    Suppression: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Schedule: Optional[Sequence["_ScheduleDefinition"]]
    Scope: Optional[Sequence["_ScopeDefinition"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SuppressSynthMonExec=json_data.get("SuppressSynthMonExec"),
            Suppression=json_data.get("Suppression"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Schedule=deserialize_list(json_data.get("Schedule"), ScheduleDefinition),
            Scope=deserialize_list(json_data.get("Scope"), ScopeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    ClusterVersion: Optional[str]
    ConfigurationVersions: Optional[Sequence[float]]
    CurrentConfigurationVersions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterVersion=json_data.get("ClusterVersion"),
            ConfigurationVersions=json_data.get("ConfigurationVersions"),
            CurrentConfigurationVersions=json_data.get("CurrentConfigurationVersions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class ScheduleDefinition(BaseModel):
    End: Optional[str]
    RecurrenceType: Optional[str]
    Start: Optional[str]
    Unknowns: Optional[str]
    ZoneId: Optional[str]
    Recurrence: Optional[Sequence["_RecurrenceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            RecurrenceType=json_data.get("RecurrenceType"),
            Start=json_data.get("Start"),
            Unknowns=json_data.get("Unknowns"),
            ZoneId=json_data.get("ZoneId"),
            Recurrence=deserialize_list(json_data.get("Recurrence"), RecurrenceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleDefinition = ScheduleDefinition


@dataclass
class RecurrenceDefinition(BaseModel):
    DayOfMonth: Optional[float]
    DayOfWeek: Optional[str]
    DurationMinutes: Optional[float]
    StartTime: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecurrenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecurrenceDefinition"]:
        if not json_data:
            return None
        return cls(
            DayOfMonth=json_data.get("DayOfMonth"),
            DayOfWeek=json_data.get("DayOfWeek"),
            DurationMinutes=json_data.get("DurationMinutes"),
            StartTime=json_data.get("StartTime"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecurrenceDefinition = RecurrenceDefinition


@dataclass
class ScopeDefinition(BaseModel):
    Entities: Optional[Sequence[str]]
    Unknowns: Optional[str]
    Matches: Optional[Sequence["_MatchesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScopeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScopeDefinition"]:
        if not json_data:
            return None
        return cls(
            Entities=json_data.get("Entities"),
            Unknowns=json_data.get("Unknowns"),
            Matches=deserialize_list(json_data.get("Matches"), MatchesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScopeDefinition = ScopeDefinition


@dataclass
class MatchesDefinition(BaseModel):
    MzId: Optional[str]
    TagCombination: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchesDefinition"]:
        if not json_data:
            return None
        return cls(
            MzId=json_data.get("MzId"),
            TagCombination=json_data.get("TagCombination"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchesDefinition = MatchesDefinition


@dataclass
class TagsDefinition(BaseModel):
    Context: Optional[str]
    Key: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Context=json_data.get("Context"),
            Key=json_data.get("Key"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


