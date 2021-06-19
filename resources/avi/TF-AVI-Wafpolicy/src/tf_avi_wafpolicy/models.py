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
    AllowModeDelegation: Optional[bool]
    CreatedBy: Optional[str]
    Description: Optional[str]
    EnableAppLearning: Optional[bool]
    EnableAutoRuleUpdates: Optional[bool]
    EnableRegexLearning: Optional[bool]
    FailureMode: Optional[str]
    Id: Optional[str]
    MinConfidence: Optional[str]
    Mode: Optional[str]
    Name: Optional[str]
    ParanoiaLevel: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    WafCrsRef: Optional[str]
    WafProfileRef: Optional[str]
    Allowlist: Optional[Sequence["_AllowlistDefinition"]]
    ApplicationSignatures: Optional[Sequence["_ApplicationSignaturesDefinition"]]
    ConfidenceOverride: Optional[Sequence["_ConfidenceOverrideDefinition"]]
    CrsOverrides: Optional[Sequence["_CrsOverridesDefinition"]]
    LearningParams: Optional[Sequence["_LearningParamsDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    PositiveSecurityModel: Optional[Sequence["_PositiveSecurityModelDefinition"]]
    PostCrsGroups: Optional[Sequence["_PostCrsGroupsDefinition"]]
    PreCrsGroups: Optional[Sequence["_PreCrsGroupsDefinition"]]
    ResolvedCrsGroups: Optional[Sequence["_ResolvedCrsGroupsDefinition"]]

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
            AllowModeDelegation=json_data.get("AllowModeDelegation"),
            CreatedBy=json_data.get("CreatedBy"),
            Description=json_data.get("Description"),
            EnableAppLearning=json_data.get("EnableAppLearning"),
            EnableAutoRuleUpdates=json_data.get("EnableAutoRuleUpdates"),
            EnableRegexLearning=json_data.get("EnableRegexLearning"),
            FailureMode=json_data.get("FailureMode"),
            Id=json_data.get("Id"),
            MinConfidence=json_data.get("MinConfidence"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            ParanoiaLevel=json_data.get("ParanoiaLevel"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            WafCrsRef=json_data.get("WafCrsRef"),
            WafProfileRef=json_data.get("WafProfileRef"),
            Allowlist=deserialize_list(json_data.get("Allowlist"), AllowlistDefinition),
            ApplicationSignatures=deserialize_list(json_data.get("ApplicationSignatures"), ApplicationSignaturesDefinition),
            ConfidenceOverride=deserialize_list(json_data.get("ConfidenceOverride"), ConfidenceOverrideDefinition),
            CrsOverrides=deserialize_list(json_data.get("CrsOverrides"), CrsOverridesDefinition),
            LearningParams=deserialize_list(json_data.get("LearningParams"), LearningParamsDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            PositiveSecurityModel=deserialize_list(json_data.get("PositiveSecurityModel"), PositiveSecurityModelDefinition),
            PostCrsGroups=deserialize_list(json_data.get("PostCrsGroups"), PostCrsGroupsDefinition),
            PreCrsGroups=deserialize_list(json_data.get("PreCrsGroups"), PreCrsGroupsDefinition),
            ResolvedCrsGroups=deserialize_list(json_data.get("ResolvedCrsGroups"), ResolvedCrsGroupsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AllowlistDefinition(BaseModel):
    Rules: Optional[Sequence["_RulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AllowlistDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowlistDefinition"]:
        if not json_data:
            return None
        return cls(
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowlistDefinition = AllowlistDefinition


@dataclass
class RulesDefinition(BaseModel):
    Enable: Optional[bool]
    Index: Optional[float]
    IsSensitive: Optional[bool]
    Mode: Optional[str]
    Name: Optional[str]
    Rule: Optional[str]
    RuleId: Optional[str]
    Tags: Optional[Sequence[str]]
    ExcludeList: Optional[Sequence["_ExcludeListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Index=json_data.get("Index"),
            IsSensitive=json_data.get("IsSensitive"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            Rule=json_data.get("Rule"),
            RuleId=json_data.get("RuleId"),
            Tags=json_data.get("Tags"),
            ExcludeList=deserialize_list(json_data.get("ExcludeList"), ExcludeListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class ExcludeListDefinition(BaseModel):
    Description: Optional[str]
    MatchElement: Optional[str]
    UriPath: Optional[str]
    ClientSubnet: Optional[Sequence["_ClientSubnetDefinition"]]
    MatchElementCriteria: Optional[Sequence["_MatchElementCriteriaDefinition"]]
    UriMatchCriteria: Optional[Sequence["_UriMatchCriteriaDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExcludeListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExcludeListDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            MatchElement=json_data.get("MatchElement"),
            UriPath=json_data.get("UriPath"),
            ClientSubnet=deserialize_list(json_data.get("ClientSubnet"), ClientSubnetDefinition),
            MatchElementCriteria=deserialize_list(json_data.get("MatchElementCriteria"), MatchElementCriteriaDefinition),
            UriMatchCriteria=deserialize_list(json_data.get("UriMatchCriteria"), UriMatchCriteriaDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExcludeListDefinition = ExcludeListDefinition


@dataclass
class ClientSubnetDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientSubnetDefinition = ClientSubnetDefinition


@dataclass
class IpAddrDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddrDefinition = IpAddrDefinition


@dataclass
class MatchElementCriteriaDefinition(BaseModel):
    MatchCase: Optional[str]
    MatchOp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchElementCriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchElementCriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCase=json_data.get("MatchCase"),
            MatchOp=json_data.get("MatchOp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchElementCriteriaDefinition = MatchElementCriteriaDefinition


@dataclass
class UriMatchCriteriaDefinition(BaseModel):
    MatchCase: Optional[str]
    MatchOp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UriMatchCriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UriMatchCriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCase=json_data.get("MatchCase"),
            MatchOp=json_data.get("MatchOp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UriMatchCriteriaDefinition = UriMatchCriteriaDefinition


@dataclass
class ApplicationSignaturesDefinition(BaseModel):
    ProviderRef: Optional[str]
    SelectedApplications: Optional[Sequence[str]]
    ResolvedRules: Optional[Sequence["_ResolvedRulesDefinition"]]
    RuleOverrides: Optional[Sequence["_RuleOverridesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationSignaturesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationSignaturesDefinition"]:
        if not json_data:
            return None
        return cls(
            ProviderRef=json_data.get("ProviderRef"),
            SelectedApplications=json_data.get("SelectedApplications"),
            ResolvedRules=deserialize_list(json_data.get("ResolvedRules"), ResolvedRulesDefinition),
            RuleOverrides=deserialize_list(json_data.get("RuleOverrides"), RuleOverridesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationSignaturesDefinition = ApplicationSignaturesDefinition


@dataclass
class ResolvedRulesDefinition(BaseModel):
    Enable: Optional[bool]
    Index: Optional[float]
    IsSensitive: Optional[bool]
    Mode: Optional[str]
    Name: Optional[str]
    Rule: Optional[str]
    RuleId: Optional[str]
    Tags: Optional[Sequence[str]]
    ExcludeList: Optional[Sequence["_ExcludeListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResolvedRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResolvedRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Index=json_data.get("Index"),
            IsSensitive=json_data.get("IsSensitive"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            Rule=json_data.get("Rule"),
            RuleId=json_data.get("RuleId"),
            Tags=json_data.get("Tags"),
            ExcludeList=deserialize_list(json_data.get("ExcludeList"), ExcludeListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResolvedRulesDefinition = ResolvedRulesDefinition


@dataclass
class RuleOverridesDefinition(BaseModel):
    Enable: Optional[bool]
    Mode: Optional[str]
    RuleId: Optional[str]
    ExcludeList: Optional[Sequence["_ExcludeListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleOverridesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleOverridesDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Mode=json_data.get("Mode"),
            RuleId=json_data.get("RuleId"),
            ExcludeList=deserialize_list(json_data.get("ExcludeList"), ExcludeListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleOverridesDefinition = RuleOverridesDefinition


@dataclass
class ConfidenceOverrideDefinition(BaseModel):
    ConfidHighValue: Optional[float]
    ConfidLowValue: Optional[float]
    ConfidProbableValue: Optional[float]
    ConfidVeryHighValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConfidenceOverrideDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfidenceOverrideDefinition"]:
        if not json_data:
            return None
        return cls(
            ConfidHighValue=json_data.get("ConfidHighValue"),
            ConfidLowValue=json_data.get("ConfidLowValue"),
            ConfidProbableValue=json_data.get("ConfidProbableValue"),
            ConfidVeryHighValue=json_data.get("ConfidVeryHighValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfidenceOverrideDefinition = ConfidenceOverrideDefinition


@dataclass
class CrsOverridesDefinition(BaseModel):
    Enable: Optional[bool]
    Mode: Optional[str]
    Name: Optional[str]
    ExcludeList: Optional[Sequence["_ExcludeListDefinition"]]
    RuleOverrides: Optional[Sequence["_RuleOverridesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CrsOverridesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CrsOverridesDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            ExcludeList=deserialize_list(json_data.get("ExcludeList"), ExcludeListDefinition),
            RuleOverrides=deserialize_list(json_data.get("RuleOverrides"), RuleOverridesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CrsOverridesDefinition = CrsOverridesDefinition


@dataclass
class LearningParamsDefinition(BaseModel):
    EnablePerUriLearning: Optional[bool]
    MaxParams: Optional[float]
    MaxUris: Optional[float]
    MinHitsToLearn: Optional[float]
    SamplingPercent: Optional[float]
    UpdateInterval: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LearningParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LearningParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            EnablePerUriLearning=json_data.get("EnablePerUriLearning"),
            MaxParams=json_data.get("MaxParams"),
            MaxUris=json_data.get("MaxUris"),
            MinHitsToLearn=json_data.get("MinHitsToLearn"),
            SamplingPercent=json_data.get("SamplingPercent"),
            UpdateInterval=json_data.get("UpdateInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LearningParamsDefinition = LearningParamsDefinition


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


@dataclass
class PositiveSecurityModelDefinition(BaseModel):
    GroupRefs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PositiveSecurityModelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PositiveSecurityModelDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupRefs=json_data.get("GroupRefs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PositiveSecurityModelDefinition = PositiveSecurityModelDefinition


@dataclass
class PostCrsGroupsDefinition(BaseModel):
    Enable: Optional[bool]
    Index: Optional[float]
    Name: Optional[str]
    ExcludeList: Optional[Sequence["_ExcludeListDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PostCrsGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PostCrsGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Index=json_data.get("Index"),
            Name=json_data.get("Name"),
            ExcludeList=deserialize_list(json_data.get("ExcludeList"), ExcludeListDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PostCrsGroupsDefinition = PostCrsGroupsDefinition


@dataclass
class PreCrsGroupsDefinition(BaseModel):
    Enable: Optional[bool]
    Index: Optional[float]
    Name: Optional[str]
    ExcludeList: Optional[Sequence["_ExcludeListDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PreCrsGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PreCrsGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Index=json_data.get("Index"),
            Name=json_data.get("Name"),
            ExcludeList=deserialize_list(json_data.get("ExcludeList"), ExcludeListDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PreCrsGroupsDefinition = PreCrsGroupsDefinition


@dataclass
class ResolvedCrsGroupsDefinition(BaseModel):
    Enable: Optional[bool]
    Index: Optional[float]
    Name: Optional[str]
    ExcludeList: Optional[Sequence["_ExcludeListDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResolvedCrsGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResolvedCrsGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Index=json_data.get("Index"),
            Name=json_data.get("Name"),
            ExcludeList=deserialize_list(json_data.get("ExcludeList"), ExcludeListDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResolvedCrsGroupsDefinition = ResolvedCrsGroupsDefinition


