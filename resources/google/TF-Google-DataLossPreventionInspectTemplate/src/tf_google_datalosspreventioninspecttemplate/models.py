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
    DisplayName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Parent: Optional[str]
    InspectConfig: Optional[Sequence["_InspectConfigDefinition"]]
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
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Parent=json_data.get("Parent"),
            InspectConfig=deserialize_list(json_data.get("InspectConfig"), InspectConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InspectConfigDefinition(BaseModel):
    ContentOptions: Optional[Sequence[str]]
    ExcludeInfoTypes: Optional[bool]
    IncludeQuote: Optional[bool]
    MinLikelihood: Optional[str]
    CustomInfoTypes: Optional[Sequence["_CustomInfoTypesDefinition"]]
    InfoTypes: Optional[Sequence["_InfoTypesDefinition"]]
    Limits: Optional[Sequence["_LimitsDefinition"]]
    RuleSet: Optional[Sequence["_RuleSetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InspectConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InspectConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentOptions=json_data.get("ContentOptions"),
            ExcludeInfoTypes=json_data.get("ExcludeInfoTypes"),
            IncludeQuote=json_data.get("IncludeQuote"),
            MinLikelihood=json_data.get("MinLikelihood"),
            CustomInfoTypes=deserialize_list(json_data.get("CustomInfoTypes"), CustomInfoTypesDefinition),
            InfoTypes=deserialize_list(json_data.get("InfoTypes"), InfoTypesDefinition),
            Limits=deserialize_list(json_data.get("Limits"), LimitsDefinition),
            RuleSet=deserialize_list(json_data.get("RuleSet"), RuleSetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InspectConfigDefinition = InspectConfigDefinition


@dataclass
class CustomInfoTypesDefinition(BaseModel):
    ExclusionType: Optional[str]
    Likelihood: Optional[str]
    Dictionary: Optional[Sequence["_DictionaryDefinition"]]
    InfoType: Optional[Sequence["_InfoTypeDefinition"]]
    Regex: Optional[Sequence["_RegexDefinition"]]
    StoredType: Optional[Sequence["_StoredTypeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomInfoTypesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomInfoTypesDefinition"]:
        if not json_data:
            return None
        return cls(
            ExclusionType=json_data.get("ExclusionType"),
            Likelihood=json_data.get("Likelihood"),
            Dictionary=deserialize_list(json_data.get("Dictionary"), DictionaryDefinition),
            InfoType=deserialize_list(json_data.get("InfoType"), InfoTypeDefinition),
            Regex=deserialize_list(json_data.get("Regex"), RegexDefinition),
            StoredType=deserialize_list(json_data.get("StoredType"), StoredTypeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomInfoTypesDefinition = CustomInfoTypesDefinition


@dataclass
class DictionaryDefinition(BaseModel):
    CloudStoragePath: Optional[Sequence["_CloudStoragePathDefinition"]]
    WordList: Optional[Sequence["_WordListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DictionaryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DictionaryDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudStoragePath=deserialize_list(json_data.get("CloudStoragePath"), CloudStoragePathDefinition),
            WordList=deserialize_list(json_data.get("WordList"), WordListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DictionaryDefinition = DictionaryDefinition


@dataclass
class CloudStoragePathDefinition(BaseModel):
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudStoragePathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudStoragePathDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudStoragePathDefinition = CloudStoragePathDefinition


@dataclass
class WordListDefinition(BaseModel):
    Words: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_WordListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WordListDefinition"]:
        if not json_data:
            return None
        return cls(
            Words=json_data.get("Words"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WordListDefinition = WordListDefinition


@dataclass
class InfoTypeDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InfoTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InfoTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InfoTypeDefinition = InfoTypeDefinition


@dataclass
class RegexDefinition(BaseModel):
    GroupIndexes: Optional[Sequence[float]]
    Pattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegexDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegexDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupIndexes=json_data.get("GroupIndexes"),
            Pattern=json_data.get("Pattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegexDefinition = RegexDefinition


@dataclass
class StoredTypeDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StoredTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StoredTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StoredTypeDefinition = StoredTypeDefinition


@dataclass
class InfoTypesDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InfoTypesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InfoTypesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InfoTypesDefinition = InfoTypesDefinition


@dataclass
class LimitsDefinition(BaseModel):
    MaxFindingsPerItem: Optional[float]
    MaxFindingsPerRequest: Optional[float]
    MaxFindingsPerInfoType: Optional[Sequence["_MaxFindingsPerInfoTypeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxFindingsPerItem=json_data.get("MaxFindingsPerItem"),
            MaxFindingsPerRequest=json_data.get("MaxFindingsPerRequest"),
            MaxFindingsPerInfoType=deserialize_list(json_data.get("MaxFindingsPerInfoType"), MaxFindingsPerInfoTypeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LimitsDefinition = LimitsDefinition


@dataclass
class MaxFindingsPerInfoTypeDefinition(BaseModel):
    MaxFindings: Optional[float]
    InfoType: Optional[Sequence["_InfoTypeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MaxFindingsPerInfoTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaxFindingsPerInfoTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxFindings=json_data.get("MaxFindings"),
            InfoType=deserialize_list(json_data.get("InfoType"), InfoTypeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaxFindingsPerInfoTypeDefinition = MaxFindingsPerInfoTypeDefinition


@dataclass
class RuleSetDefinition(BaseModel):
    InfoTypes: Optional[Sequence["_InfoTypesDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleSetDefinition"]:
        if not json_data:
            return None
        return cls(
            InfoTypes=deserialize_list(json_data.get("InfoTypes"), InfoTypesDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleSetDefinition = RuleSetDefinition


@dataclass
class RulesDefinition(BaseModel):
    ExclusionRule: Optional[Sequence["_ExclusionRuleDefinition"]]
    HotwordRule: Optional[Sequence["_HotwordRuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            ExclusionRule=deserialize_list(json_data.get("ExclusionRule"), ExclusionRuleDefinition),
            HotwordRule=deserialize_list(json_data.get("HotwordRule"), HotwordRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class ExclusionRuleDefinition(BaseModel):
    MatchingType: Optional[str]
    Dictionary: Optional[Sequence["_DictionaryDefinition"]]
    ExcludeInfoTypes: Optional[Sequence["_ExcludeInfoTypesDefinition"]]
    Regex: Optional[Sequence["_RegexDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExclusionRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExclusionRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchingType=json_data.get("MatchingType"),
            Dictionary=deserialize_list(json_data.get("Dictionary"), DictionaryDefinition),
            ExcludeInfoTypes=deserialize_list(json_data.get("ExcludeInfoTypes"), ExcludeInfoTypesDefinition),
            Regex=deserialize_list(json_data.get("Regex"), RegexDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExclusionRuleDefinition = ExclusionRuleDefinition


@dataclass
class ExcludeInfoTypesDefinition(BaseModel):
    InfoTypes: Optional[Sequence["_InfoTypesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExcludeInfoTypesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExcludeInfoTypesDefinition"]:
        if not json_data:
            return None
        return cls(
            InfoTypes=deserialize_list(json_data.get("InfoTypes"), InfoTypesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExcludeInfoTypesDefinition = ExcludeInfoTypesDefinition


@dataclass
class HotwordRuleDefinition(BaseModel):
    HotwordRegex: Optional[Sequence["_HotwordRegexDefinition"]]
    LikelihoodAdjustment: Optional[Sequence["_LikelihoodAdjustmentDefinition"]]
    Proximity: Optional[Sequence["_ProximityDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HotwordRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HotwordRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            HotwordRegex=deserialize_list(json_data.get("HotwordRegex"), HotwordRegexDefinition),
            LikelihoodAdjustment=deserialize_list(json_data.get("LikelihoodAdjustment"), LikelihoodAdjustmentDefinition),
            Proximity=deserialize_list(json_data.get("Proximity"), ProximityDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HotwordRuleDefinition = HotwordRuleDefinition


@dataclass
class HotwordRegexDefinition(BaseModel):
    GroupIndexes: Optional[Sequence[float]]
    Pattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HotwordRegexDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HotwordRegexDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupIndexes=json_data.get("GroupIndexes"),
            Pattern=json_data.get("Pattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HotwordRegexDefinition = HotwordRegexDefinition


@dataclass
class LikelihoodAdjustmentDefinition(BaseModel):
    FixedLikelihood: Optional[str]
    RelativeLikelihood: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LikelihoodAdjustmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LikelihoodAdjustmentDefinition"]:
        if not json_data:
            return None
        return cls(
            FixedLikelihood=json_data.get("FixedLikelihood"),
            RelativeLikelihood=json_data.get("RelativeLikelihood"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LikelihoodAdjustmentDefinition = LikelihoodAdjustmentDefinition


@dataclass
class ProximityDefinition(BaseModel):
    WindowAfter: Optional[float]
    WindowBefore: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ProximityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProximityDefinition"]:
        if not json_data:
            return None
        return cls(
            WindowAfter=json_data.get("WindowAfter"),
            WindowBefore=json_data.get("WindowBefore"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProximityDefinition = ProximityDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


