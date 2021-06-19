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
    HttpListenerIds: Optional[Sequence[str]]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PathBasedRuleIds: Optional[Sequence[str]]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    CustomRules: Optional[Sequence["_CustomRulesDefinition"]]
    ManagedRules: Optional[Sequence["_ManagedRulesDefinition"]]
    PolicySettings: Optional[Sequence["_PolicySettingsDefinition"]]
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
            HttpListenerIds=json_data.get("HttpListenerIds"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PathBasedRuleIds=json_data.get("PathBasedRuleIds"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            CustomRules=deserialize_list(json_data.get("CustomRules"), CustomRulesDefinition),
            ManagedRules=deserialize_list(json_data.get("ManagedRules"), ManagedRulesDefinition),
            PolicySettings=deserialize_list(json_data.get("PolicySettings"), PolicySettingsDefinition),
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
class CustomRulesDefinition(BaseModel):
    Action: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    RuleType: Optional[str]
    MatchConditions: Optional[Sequence["_MatchConditionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            RuleType=json_data.get("RuleType"),
            MatchConditions=deserialize_list(json_data.get("MatchConditions"), MatchConditionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomRulesDefinition = CustomRulesDefinition


@dataclass
class MatchConditionsDefinition(BaseModel):
    MatchValues: Optional[Sequence[str]]
    NegationCondition: Optional[bool]
    Operator: Optional[str]
    Transforms: Optional[Sequence[str]]
    MatchVariables: Optional[Sequence["_MatchVariablesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            NegationCondition=json_data.get("NegationCondition"),
            Operator=json_data.get("Operator"),
            Transforms=json_data.get("Transforms"),
            MatchVariables=deserialize_list(json_data.get("MatchVariables"), MatchVariablesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchConditionsDefinition = MatchConditionsDefinition


@dataclass
class MatchVariablesDefinition(BaseModel):
    Selector: Optional[str]
    VariableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchVariablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchVariablesDefinition"]:
        if not json_data:
            return None
        return cls(
            Selector=json_data.get("Selector"),
            VariableName=json_data.get("VariableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchVariablesDefinition = MatchVariablesDefinition


@dataclass
class ManagedRulesDefinition(BaseModel):
    Exclusion: Optional[Sequence["_ExclusionDefinition"]]
    ManagedRuleSet: Optional[Sequence["_ManagedRuleSetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Exclusion=deserialize_list(json_data.get("Exclusion"), ExclusionDefinition),
            ManagedRuleSet=deserialize_list(json_data.get("ManagedRuleSet"), ManagedRuleSetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedRulesDefinition = ManagedRulesDefinition


@dataclass
class ExclusionDefinition(BaseModel):
    MatchVariable: Optional[str]
    Selector: Optional[str]
    SelectorMatchOperator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExclusionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExclusionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchVariable=json_data.get("MatchVariable"),
            Selector=json_data.get("Selector"),
            SelectorMatchOperator=json_data.get("SelectorMatchOperator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExclusionDefinition = ExclusionDefinition


@dataclass
class ManagedRuleSetDefinition(BaseModel):
    Type: Optional[str]
    Version: Optional[str]
    RuleGroupOverride: Optional[Sequence["_RuleGroupOverrideDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedRuleSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedRuleSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Version=json_data.get("Version"),
            RuleGroupOverride=deserialize_list(json_data.get("RuleGroupOverride"), RuleGroupOverrideDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedRuleSetDefinition = ManagedRuleSetDefinition


@dataclass
class RuleGroupOverrideDefinition(BaseModel):
    DisabledRules: Optional[Sequence[str]]
    RuleGroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuleGroupOverrideDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleGroupOverrideDefinition"]:
        if not json_data:
            return None
        return cls(
            DisabledRules=json_data.get("DisabledRules"),
            RuleGroupName=json_data.get("RuleGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleGroupOverrideDefinition = RuleGroupOverrideDefinition


@dataclass
class PolicySettingsDefinition(BaseModel):
    Enabled: Optional[bool]
    FileUploadLimitInMb: Optional[float]
    MaxRequestBodySizeInKb: Optional[float]
    Mode: Optional[str]
    RequestBodyCheck: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PolicySettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicySettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            FileUploadLimitInMb=json_data.get("FileUploadLimitInMb"),
            MaxRequestBodySizeInKb=json_data.get("MaxRequestBodySizeInKb"),
            Mode=json_data.get("Mode"),
            RequestBodyCheck=json_data.get("RequestBodyCheck"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicySettingsDefinition = PolicySettingsDefinition


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


