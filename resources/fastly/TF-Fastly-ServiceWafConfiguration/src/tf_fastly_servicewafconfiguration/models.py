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
    AllowedHttpVersions: Optional[str]
    AllowedMethods: Optional[str]
    AllowedRequestContentType: Optional[str]
    AllowedRequestContentTypeCharset: Optional[str]
    ArgLength: Optional[float]
    ArgNameLength: Optional[float]
    CombinedFileSizes: Optional[float]
    CriticalAnomalyScore: Optional[float]
    CrsValidateUtf8Encoding: Optional[bool]
    ErrorAnomalyScore: Optional[float]
    HighRiskCountryCodes: Optional[str]
    HttpViolationScoreThreshold: Optional[float]
    Id: Optional[str]
    InboundAnomalyScoreThreshold: Optional[float]
    LfiScoreThreshold: Optional[float]
    MaxFileSize: Optional[float]
    MaxNumArgs: Optional[float]
    NoticeAnomalyScore: Optional[float]
    ParanoiaLevel: Optional[float]
    PhpInjectionScoreThreshold: Optional[float]
    RceScoreThreshold: Optional[float]
    RestrictedExtensions: Optional[str]
    RestrictedHeaders: Optional[str]
    RfiScoreThreshold: Optional[float]
    SessionFixationScoreThreshold: Optional[float]
    SqlInjectionScoreThreshold: Optional[float]
    TotalArgLength: Optional[float]
    WafId: Optional[str]
    WarningAnomalyScore: Optional[float]
    XssScoreThreshold: Optional[float]
    Rule: Optional[Sequence["_RuleDefinition"]]
    RuleExclusion: Optional[Sequence["_RuleExclusionDefinition"]]

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
            AllowedHttpVersions=json_data.get("AllowedHttpVersions"),
            AllowedMethods=json_data.get("AllowedMethods"),
            AllowedRequestContentType=json_data.get("AllowedRequestContentType"),
            AllowedRequestContentTypeCharset=json_data.get("AllowedRequestContentTypeCharset"),
            ArgLength=json_data.get("ArgLength"),
            ArgNameLength=json_data.get("ArgNameLength"),
            CombinedFileSizes=json_data.get("CombinedFileSizes"),
            CriticalAnomalyScore=json_data.get("CriticalAnomalyScore"),
            CrsValidateUtf8Encoding=json_data.get("CrsValidateUtf8Encoding"),
            ErrorAnomalyScore=json_data.get("ErrorAnomalyScore"),
            HighRiskCountryCodes=json_data.get("HighRiskCountryCodes"),
            HttpViolationScoreThreshold=json_data.get("HttpViolationScoreThreshold"),
            Id=json_data.get("Id"),
            InboundAnomalyScoreThreshold=json_data.get("InboundAnomalyScoreThreshold"),
            LfiScoreThreshold=json_data.get("LfiScoreThreshold"),
            MaxFileSize=json_data.get("MaxFileSize"),
            MaxNumArgs=json_data.get("MaxNumArgs"),
            NoticeAnomalyScore=json_data.get("NoticeAnomalyScore"),
            ParanoiaLevel=json_data.get("ParanoiaLevel"),
            PhpInjectionScoreThreshold=json_data.get("PhpInjectionScoreThreshold"),
            RceScoreThreshold=json_data.get("RceScoreThreshold"),
            RestrictedExtensions=json_data.get("RestrictedExtensions"),
            RestrictedHeaders=json_data.get("RestrictedHeaders"),
            RfiScoreThreshold=json_data.get("RfiScoreThreshold"),
            SessionFixationScoreThreshold=json_data.get("SessionFixationScoreThreshold"),
            SqlInjectionScoreThreshold=json_data.get("SqlInjectionScoreThreshold"),
            TotalArgLength=json_data.get("TotalArgLength"),
            WafId=json_data.get("WafId"),
            WarningAnomalyScore=json_data.get("WarningAnomalyScore"),
            XssScoreThreshold=json_data.get("XssScoreThreshold"),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
            RuleExclusion=deserialize_list(json_data.get("RuleExclusion"), RuleExclusionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RuleDefinition(BaseModel):
    ModsecRuleId: Optional[float]
    Revision: Optional[float]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            ModsecRuleId=json_data.get("ModsecRuleId"),
            Revision=json_data.get("Revision"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class RuleExclusionDefinition(BaseModel):
    Condition: Optional[str]
    ExclusionType: Optional[str]
    ModsecRuleIds: Optional[Sequence[float]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuleExclusionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleExclusionDefinition"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            ExclusionType=json_data.get("ExclusionType"),
            ModsecRuleIds=json_data.get("ModsecRuleIds"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleExclusionDefinition = RuleExclusionDefinition


