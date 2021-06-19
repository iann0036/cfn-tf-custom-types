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
    Id: Optional[str]
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]
    Processor: Optional[Sequence["_ProcessorDefinition"]]

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
            Id=json_data.get("Id"),
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
            Processor=deserialize_list(json_data.get("Processor"), ProcessorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FilterDefinition(BaseModel):
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class ProcessorDefinition(BaseModel):
    ArithmeticProcessor: Optional[Sequence["_ArithmeticProcessorDefinition"]]
    AttributeRemapper: Optional[Sequence["_AttributeRemapperDefinition"]]
    CategoryProcessor: Optional[Sequence["_CategoryProcessorDefinition"]]
    DateRemapper: Optional[Sequence["_DateRemapperDefinition"]]
    GeoIpParser: Optional[Sequence["_GeoIpParserDefinition"]]
    GrokParser: Optional[Sequence["_GrokParserDefinition"]]
    LookupProcessor: Optional[Sequence["_LookupProcessorDefinition"]]
    MessageRemapper: Optional[Sequence["_MessageRemapperDefinition"]]
    ServiceRemapper: Optional[Sequence["_ServiceRemapperDefinition"]]
    StatusRemapper: Optional[Sequence["_StatusRemapperDefinition"]]
    StringBuilderProcessor: Optional[Sequence["_StringBuilderProcessorDefinition"]]
    TraceIdRemapper: Optional[Sequence["_TraceIdRemapperDefinition"]]
    UrlParser: Optional[Sequence["_UrlParserDefinition"]]
    UserAgentParser: Optional[Sequence["_UserAgentParserDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessorDefinition"]:
        if not json_data:
            return None
        return cls(
            ArithmeticProcessor=deserialize_list(json_data.get("ArithmeticProcessor"), ArithmeticProcessorDefinition),
            AttributeRemapper=deserialize_list(json_data.get("AttributeRemapper"), AttributeRemapperDefinition),
            CategoryProcessor=deserialize_list(json_data.get("CategoryProcessor"), CategoryProcessorDefinition),
            DateRemapper=deserialize_list(json_data.get("DateRemapper"), DateRemapperDefinition),
            GeoIpParser=deserialize_list(json_data.get("GeoIpParser"), GeoIpParserDefinition),
            GrokParser=deserialize_list(json_data.get("GrokParser"), GrokParserDefinition),
            LookupProcessor=deserialize_list(json_data.get("LookupProcessor"), LookupProcessorDefinition),
            MessageRemapper=deserialize_list(json_data.get("MessageRemapper"), MessageRemapperDefinition),
            ServiceRemapper=deserialize_list(json_data.get("ServiceRemapper"), ServiceRemapperDefinition),
            StatusRemapper=deserialize_list(json_data.get("StatusRemapper"), StatusRemapperDefinition),
            StringBuilderProcessor=deserialize_list(json_data.get("StringBuilderProcessor"), StringBuilderProcessorDefinition),
            TraceIdRemapper=deserialize_list(json_data.get("TraceIdRemapper"), TraceIdRemapperDefinition),
            UrlParser=deserialize_list(json_data.get("UrlParser"), UrlParserDefinition),
            UserAgentParser=deserialize_list(json_data.get("UserAgentParser"), UserAgentParserDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessorDefinition = ProcessorDefinition


@dataclass
class ArithmeticProcessorDefinition(BaseModel):
    Expression: Optional[str]
    IsEnabled: Optional[bool]
    IsReplaceMissing: Optional[bool]
    Name: Optional[str]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ArithmeticProcessorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArithmeticProcessorDefinition"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            IsEnabled=json_data.get("IsEnabled"),
            IsReplaceMissing=json_data.get("IsReplaceMissing"),
            Name=json_data.get("Name"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArithmeticProcessorDefinition = ArithmeticProcessorDefinition


@dataclass
class AttributeRemapperDefinition(BaseModel):
    IsEnabled: Optional[bool]
    Name: Optional[str]
    OverrideOnConflict: Optional[bool]
    PreserveSource: Optional[bool]
    SourceType: Optional[str]
    Sources: Optional[Sequence[str]]
    Target: Optional[str]
    TargetFormat: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeRemapperDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeRemapperDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            OverrideOnConflict=json_data.get("OverrideOnConflict"),
            PreserveSource=json_data.get("PreserveSource"),
            SourceType=json_data.get("SourceType"),
            Sources=json_data.get("Sources"),
            Target=json_data.get("Target"),
            TargetFormat=json_data.get("TargetFormat"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeRemapperDefinition = AttributeRemapperDefinition


@dataclass
class CategoryProcessorDefinition(BaseModel):
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Target: Optional[str]
    Category: Optional[Sequence["_CategoryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CategoryProcessorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoryProcessorDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Target=json_data.get("Target"),
            Category=deserialize_list(json_data.get("Category"), CategoryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoryProcessorDefinition = CategoryProcessorDefinition


@dataclass
class CategoryDefinition(BaseModel):
    Name: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CategoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoryDefinition = CategoryDefinition


@dataclass
class DateRemapperDefinition(BaseModel):
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Sources: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DateRemapperDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateRemapperDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Sources=json_data.get("Sources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateRemapperDefinition = DateRemapperDefinition


@dataclass
class GeoIpParserDefinition(BaseModel):
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Sources: Optional[Sequence[str]]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeoIpParserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoIpParserDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Sources=json_data.get("Sources"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoIpParserDefinition = GeoIpParserDefinition


@dataclass
class GrokParserDefinition(BaseModel):
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Samples: Optional[Sequence[str]]
    Source: Optional[str]
    Grok: Optional[Sequence["_GrokDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GrokParserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrokParserDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Samples=json_data.get("Samples"),
            Source=json_data.get("Source"),
            Grok=deserialize_list(json_data.get("Grok"), GrokDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrokParserDefinition = GrokParserDefinition


@dataclass
class GrokDefinition(BaseModel):
    MatchRules: Optional[str]
    SupportRules: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GrokDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrokDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchRules=json_data.get("MatchRules"),
            SupportRules=json_data.get("SupportRules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrokDefinition = GrokDefinition


@dataclass
class LookupProcessorDefinition(BaseModel):
    DefaultLookup: Optional[str]
    IsEnabled: Optional[bool]
    LookupTable: Optional[Sequence[str]]
    Name: Optional[str]
    Source: Optional[str]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LookupProcessorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LookupProcessorDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultLookup=json_data.get("DefaultLookup"),
            IsEnabled=json_data.get("IsEnabled"),
            LookupTable=json_data.get("LookupTable"),
            Name=json_data.get("Name"),
            Source=json_data.get("Source"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LookupProcessorDefinition = LookupProcessorDefinition


@dataclass
class MessageRemapperDefinition(BaseModel):
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Sources: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MessageRemapperDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MessageRemapperDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Sources=json_data.get("Sources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MessageRemapperDefinition = MessageRemapperDefinition


@dataclass
class ServiceRemapperDefinition(BaseModel):
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Sources: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceRemapperDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceRemapperDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Sources=json_data.get("Sources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceRemapperDefinition = ServiceRemapperDefinition


@dataclass
class StatusRemapperDefinition(BaseModel):
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Sources: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_StatusRemapperDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusRemapperDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Sources=json_data.get("Sources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusRemapperDefinition = StatusRemapperDefinition


@dataclass
class StringBuilderProcessorDefinition(BaseModel):
    IsEnabled: Optional[bool]
    IsReplaceMissing: Optional[bool]
    Name: Optional[str]
    Target: Optional[str]
    Template: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StringBuilderProcessorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringBuilderProcessorDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            IsReplaceMissing=json_data.get("IsReplaceMissing"),
            Name=json_data.get("Name"),
            Target=json_data.get("Target"),
            Template=json_data.get("Template"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringBuilderProcessorDefinition = StringBuilderProcessorDefinition


@dataclass
class TraceIdRemapperDefinition(BaseModel):
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Sources: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TraceIdRemapperDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TraceIdRemapperDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Sources=json_data.get("Sources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TraceIdRemapperDefinition = TraceIdRemapperDefinition


@dataclass
class UrlParserDefinition(BaseModel):
    IsEnabled: Optional[bool]
    Name: Optional[str]
    NormalizeEndingSlashes: Optional[bool]
    Sources: Optional[Sequence[str]]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UrlParserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlParserDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            NormalizeEndingSlashes=json_data.get("NormalizeEndingSlashes"),
            Sources=json_data.get("Sources"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlParserDefinition = UrlParserDefinition


@dataclass
class UserAgentParserDefinition(BaseModel):
    IsEnabled: Optional[bool]
    IsEncoded: Optional[bool]
    Name: Optional[str]
    Sources: Optional[Sequence[str]]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserAgentParserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserAgentParserDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            IsEncoded=json_data.get("IsEncoded"),
            Name=json_data.get("Name"),
            Sources=json_data.get("Sources"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserAgentParserDefinition = UserAgentParserDefinition


