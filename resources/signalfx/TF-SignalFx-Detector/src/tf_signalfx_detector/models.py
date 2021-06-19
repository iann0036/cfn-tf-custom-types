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
    AuthorizedWriterTeams: Optional[Sequence[str]]
    AuthorizedWriterUsers: Optional[Sequence[str]]
    Description: Optional[str]
    DisableSampling: Optional[bool]
    EndTime: Optional[float]
    Id: Optional[str]
    MaxDelay: Optional[float]
    MinDelay: Optional[float]
    Name: Optional[str]
    ProgramText: Optional[str]
    ShowDataMarkers: Optional[bool]
    ShowEventLines: Optional[bool]
    StartTime: Optional[float]
    Tags: Optional[Sequence[str]]
    Teams: Optional[Sequence[str]]
    TimeRange: Optional[float]
    Timezone: Optional[str]
    Url: Optional[str]
    Rule: Optional[Sequence["_RuleDefinition"]]
    VizOptions: Optional[Sequence["_VizOptionsDefinition"]]

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
            AuthorizedWriterTeams=json_data.get("AuthorizedWriterTeams"),
            AuthorizedWriterUsers=json_data.get("AuthorizedWriterUsers"),
            Description=json_data.get("Description"),
            DisableSampling=json_data.get("DisableSampling"),
            EndTime=json_data.get("EndTime"),
            Id=json_data.get("Id"),
            MaxDelay=json_data.get("MaxDelay"),
            MinDelay=json_data.get("MinDelay"),
            Name=json_data.get("Name"),
            ProgramText=json_data.get("ProgramText"),
            ShowDataMarkers=json_data.get("ShowDataMarkers"),
            ShowEventLines=json_data.get("ShowEventLines"),
            StartTime=json_data.get("StartTime"),
            Tags=json_data.get("Tags"),
            Teams=json_data.get("Teams"),
            TimeRange=json_data.get("TimeRange"),
            Timezone=json_data.get("Timezone"),
            Url=json_data.get("Url"),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
            VizOptions=deserialize_list(json_data.get("VizOptions"), VizOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RuleDefinition(BaseModel):
    Description: Optional[str]
    DetectLabel: Optional[str]
    Disabled: Optional[bool]
    Notifications: Optional[Sequence[str]]
    ParameterizedBody: Optional[str]
    ParameterizedSubject: Optional[str]
    RunbookUrl: Optional[str]
    Severity: Optional[str]
    Tip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            DetectLabel=json_data.get("DetectLabel"),
            Disabled=json_data.get("Disabled"),
            Notifications=json_data.get("Notifications"),
            ParameterizedBody=json_data.get("ParameterizedBody"),
            ParameterizedSubject=json_data.get("ParameterizedSubject"),
            RunbookUrl=json_data.get("RunbookUrl"),
            Severity=json_data.get("Severity"),
            Tip=json_data.get("Tip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class VizOptionsDefinition(BaseModel):
    Color: Optional[str]
    DisplayName: Optional[str]
    Label: Optional[str]
    ValuePrefix: Optional[str]
    ValueSuffix: Optional[str]
    ValueUnit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VizOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VizOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
            DisplayName=json_data.get("DisplayName"),
            Label=json_data.get("Label"),
            ValuePrefix=json_data.get("ValuePrefix"),
            ValueSuffix=json_data.get("ValueSuffix"),
            ValueUnit=json_data.get("ValueUnit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VizOptionsDefinition = VizOptionsDefinition


