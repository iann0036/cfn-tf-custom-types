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
    Category: Optional[str]
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    RequestCacheControl: Optional[str]
    ResponseCacheControl: Optional[str]
    ResponseExpires: Optional[str]
    Status: Optional[str]
    TextResponseVcache: Optional[str]
    Updateserver: Optional[str]
    Vdomparam: Optional[str]
    HostDomainNameSuffix: Optional[Sequence["_HostDomainNameSuffixDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]

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
            Category=json_data.get("Category"),
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RequestCacheControl=json_data.get("RequestCacheControl"),
            ResponseCacheControl=json_data.get("ResponseCacheControl"),
            ResponseExpires=json_data.get("ResponseExpires"),
            Status=json_data.get("Status"),
            TextResponseVcache=json_data.get("TextResponseVcache"),
            Updateserver=json_data.get("Updateserver"),
            Vdomparam=json_data.get("Vdomparam"),
            HostDomainNameSuffix=deserialize_list(json_data.get("HostDomainNameSuffix"), HostDomainNameSuffixDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HostDomainNameSuffixDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostDomainNameSuffixDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostDomainNameSuffixDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostDomainNameSuffixDefinition = HostDomainNameSuffixDefinition


@dataclass
class RulesDefinition(BaseModel):
    MatchMode: Optional[str]
    Name: Optional[str]
    SkipRuleMode: Optional[str]
    ContentId: Optional[Sequence["_ContentIdDefinition"]]
    MatchEntries: Optional[Sequence["_MatchEntriesDefinition"]]
    SkipEntries: Optional[Sequence["_SkipEntriesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchMode=json_data.get("MatchMode"),
            Name=json_data.get("Name"),
            SkipRuleMode=json_data.get("SkipRuleMode"),
            ContentId=deserialize_list(json_data.get("ContentId"), ContentIdDefinition),
            MatchEntries=deserialize_list(json_data.get("MatchEntries"), MatchEntriesDefinition),
            SkipEntries=deserialize_list(json_data.get("SkipEntries"), SkipEntriesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class ContentIdDefinition(BaseModel):
    EndDirection: Optional[str]
    EndSkip: Optional[float]
    EndStr: Optional[str]
    RangeStr: Optional[str]
    StartDirection: Optional[str]
    StartSkip: Optional[float]
    StartStr: Optional[str]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContentIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContentIdDefinition"]:
        if not json_data:
            return None
        return cls(
            EndDirection=json_data.get("EndDirection"),
            EndSkip=json_data.get("EndSkip"),
            EndStr=json_data.get("EndStr"),
            RangeStr=json_data.get("RangeStr"),
            StartDirection=json_data.get("StartDirection"),
            StartSkip=json_data.get("StartSkip"),
            StartStr=json_data.get("StartStr"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContentIdDefinition = ContentIdDefinition


@dataclass
class MatchEntriesDefinition(BaseModel):
    Id: Optional[float]
    Target: Optional[str]
    Pattern: Optional[Sequence["_PatternDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchEntriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchEntriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Target=json_data.get("Target"),
            Pattern=deserialize_list(json_data.get("Pattern"), PatternDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchEntriesDefinition = MatchEntriesDefinition


@dataclass
class PatternDefinition(BaseModel):
    String: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PatternDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PatternDefinition"]:
        if not json_data:
            return None
        return cls(
            String=json_data.get("String"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PatternDefinition = PatternDefinition


@dataclass
class SkipEntriesDefinition(BaseModel):
    Id: Optional[float]
    Target: Optional[str]
    Pattern: Optional[Sequence["_PatternDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SkipEntriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SkipEntriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Target=json_data.get("Target"),
            Pattern=deserialize_list(json_data.get("Pattern"), PatternDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SkipEntriesDefinition = SkipEntriesDefinition


