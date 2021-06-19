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
    CustomBlockResponseBody: Optional[str]
    CustomBlockResponseStatusCode: Optional[float]
    Enabled: Optional[bool]
    FrontendEndpointIds: Optional[Sequence[str]]
    Id: Optional[str]
    Location: Optional[str]
    Mode: Optional[str]
    Name: Optional[str]
    RedirectUrl: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    CustomRule: Optional[Sequence["_CustomRuleDefinition"]]
    ManagedRule: Optional[Sequence["_ManagedRuleDefinition"]]
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
            CustomBlockResponseBody=json_data.get("CustomBlockResponseBody"),
            CustomBlockResponseStatusCode=json_data.get("CustomBlockResponseStatusCode"),
            Enabled=json_data.get("Enabled"),
            FrontendEndpointIds=json_data.get("FrontendEndpointIds"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            RedirectUrl=json_data.get("RedirectUrl"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            CustomRule=deserialize_list(json_data.get("CustomRule"), CustomRuleDefinition),
            ManagedRule=deserialize_list(json_data.get("ManagedRule"), ManagedRuleDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class CustomRuleDefinition(BaseModel):
    Action: Optional[str]
    Enabled: Optional[bool]
    Name: Optional[str]
    Priority: Optional[float]
    RateLimitDurationInMinutes: Optional[float]
    RateLimitThreshold: Optional[float]
    Type: Optional[str]
    MatchCondition: Optional[Sequence["_MatchConditionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Enabled=json_data.get("Enabled"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            RateLimitDurationInMinutes=json_data.get("RateLimitDurationInMinutes"),
            RateLimitThreshold=json_data.get("RateLimitThreshold"),
            Type=json_data.get("Type"),
            MatchCondition=deserialize_list(json_data.get("MatchCondition"), MatchConditionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomRuleDefinition = CustomRuleDefinition


@dataclass
class MatchConditionDefinition(BaseModel):
    MatchValues: Optional[Sequence[str]]
    MatchVariable: Optional[str]
    NegationCondition: Optional[bool]
    Operator: Optional[str]
    Selector: Optional[str]
    Transforms: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            MatchVariable=json_data.get("MatchVariable"),
            NegationCondition=json_data.get("NegationCondition"),
            Operator=json_data.get("Operator"),
            Selector=json_data.get("Selector"),
            Transforms=json_data.get("Transforms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchConditionDefinition = MatchConditionDefinition


@dataclass
class ManagedRuleDefinition(BaseModel):
    Type: Optional[str]
    Version: Optional[str]
    Exclusion: Optional[Sequence["_ExclusionDefinition"]]
    Override: Optional[Sequence["_OverrideDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Version=json_data.get("Version"),
            Exclusion=deserialize_list(json_data.get("Exclusion"), ExclusionDefinition),
            Override=deserialize_list(json_data.get("Override"), OverrideDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedRuleDefinition = ManagedRuleDefinition


@dataclass
class ExclusionDefinition(BaseModel):
    MatchVariable: Optional[str]
    Operator: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExclusionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExclusionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchVariable=json_data.get("MatchVariable"),
            Operator=json_data.get("Operator"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExclusionDefinition = ExclusionDefinition


@dataclass
class OverrideDefinition(BaseModel):
    RuleGroupName: Optional[str]
    Exclusion: Optional[Sequence["_ExclusionDefinition"]]
    Rule: Optional[Sequence["_RuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OverrideDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverrideDefinition"]:
        if not json_data:
            return None
        return cls(
            RuleGroupName=json_data.get("RuleGroupName"),
            Exclusion=deserialize_list(json_data.get("Exclusion"), ExclusionDefinition),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverrideDefinition = OverrideDefinition


@dataclass
class RuleDefinition(BaseModel):
    Action: Optional[str]
    Enabled: Optional[bool]
    RuleId: Optional[str]
    Exclusion: Optional[Sequence["_ExclusionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Enabled=json_data.get("Enabled"),
            RuleId=json_data.get("RuleId"),
            Exclusion=deserialize_list(json_data.get("Exclusion"), ExclusionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


