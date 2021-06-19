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
    Path: Optional[str]
    Revision: Optional[float]
    DefaultRule: Optional[Sequence["_DefaultRuleDefinition"]]
    Rule: Optional[Sequence["_RuleDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

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
            Path=json_data.get("Path"),
            Revision=json_data.get("Revision"),
            DefaultRule=deserialize_list(json_data.get("DefaultRule"), DefaultRuleDefinition),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefaultRuleDefinition(BaseModel):
    Action: Optional[str]
    Description: Optional[str]
    LogLabel: Optional[str]
    Logged: Optional[bool]
    Tag: Optional[Sequence["_TagDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Description=json_data.get("Description"),
            LogLabel=json_data.get("LogLabel"),
            Logged=json_data.get("Logged"),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultRuleDefinition = DefaultRuleDefinition


@dataclass
class TagDefinition(BaseModel):
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


@dataclass
class RuleDefinition(BaseModel):
    Action: Optional[str]
    Description: Optional[str]
    DestinationGroups: Optional[Sequence[str]]
    DestinationsExcluded: Optional[bool]
    Direction: Optional[str]
    Disabled: Optional[bool]
    DisplayName: Optional[str]
    IpVersion: Optional[str]
    LogLabel: Optional[str]
    Logged: Optional[bool]
    Notes: Optional[str]
    NsxId: Optional[str]
    Profiles: Optional[Sequence[str]]
    Scope: Optional[Sequence[str]]
    SequenceNumber: Optional[float]
    Services: Optional[Sequence[str]]
    SourceGroups: Optional[Sequence[str]]
    SourcesExcluded: Optional[bool]
    Tag: Optional[Sequence["_TagDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Description=json_data.get("Description"),
            DestinationGroups=json_data.get("DestinationGroups"),
            DestinationsExcluded=json_data.get("DestinationsExcluded"),
            Direction=json_data.get("Direction"),
            Disabled=json_data.get("Disabled"),
            DisplayName=json_data.get("DisplayName"),
            IpVersion=json_data.get("IpVersion"),
            LogLabel=json_data.get("LogLabel"),
            Logged=json_data.get("Logged"),
            Notes=json_data.get("Notes"),
            NsxId=json_data.get("NsxId"),
            Profiles=json_data.get("Profiles"),
            Scope=json_data.get("Scope"),
            SequenceNumber=json_data.get("SequenceNumber"),
            Services=json_data.get("Services"),
            SourceGroups=json_data.get("SourceGroups"),
            SourcesExcluded=json_data.get("SourcesExcluded"),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


