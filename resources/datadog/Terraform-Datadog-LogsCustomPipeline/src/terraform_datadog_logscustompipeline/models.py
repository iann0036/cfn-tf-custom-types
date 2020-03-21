# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Filter: Optional[Sequence["_Filter"]]
    Processor: Optional[Sequence["_Processor"]]
    ArithmeticProcessor: Optional[Sequence["_ArithmeticProcessor"]]
    AttributeRemapper: Optional[Sequence["_AttributeRemapper"]]
    CategoryProcessor: Optional[Sequence["_CategoryProcessor"]]
    DateRemapper: Optional[Sequence["_DateRemapper"]]
    GeoIpParser: Optional[Sequence["_GeoIpParser"]]
    GrokParser: Optional[Sequence["_GrokParser"]]
    MessageRemapper: Optional[Sequence["_MessageRemapper"]]
    Pipeline: Optional[Sequence["_Pipeline"]]
    ServiceRemapper: Optional[Sequence["_ServiceRemapper"]]
    StatusRemapper: Optional[Sequence["_StatusRemapper"]]
    StringBuilderProcessor: Optional[Sequence["_StringBuilderProcessor"]]
    TraceIdRemapper: Optional[Sequence["_TraceIdRemapper"]]
    UrlParser: Optional[Sequence["_UrlParser"]]
    UserAgentParser: Optional[Sequence["_UserAgentParser"]]
    Category: Optional[Sequence["_Category"]]
    Grok: Optional[Sequence["_Grok"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Filter=json_data.get("Filter"),
            Processor=json_data.get("Processor"),
            ArithmeticProcessor=json_data.get("ArithmeticProcessor"),
            AttributeRemapper=json_data.get("AttributeRemapper"),
            CategoryProcessor=json_data.get("CategoryProcessor"),
            DateRemapper=json_data.get("DateRemapper"),
            GeoIpParser=json_data.get("GeoIpParser"),
            GrokParser=json_data.get("GrokParser"),
            MessageRemapper=json_data.get("MessageRemapper"),
            Pipeline=json_data.get("Pipeline"),
            ServiceRemapper=json_data.get("ServiceRemapper"),
            StatusRemapper=json_data.get("StatusRemapper"),
            StringBuilderProcessor=json_data.get("StringBuilderProcessor"),
            TraceIdRemapper=json_data.get("TraceIdRemapper"),
            UrlParser=json_data.get("UrlParser"),
            UserAgentParser=json_data.get("UserAgentParser"),
            Category=json_data.get("Category"),
            Grok=json_data.get("Grok"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Filter:
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


@dataclass
class Processor:
    ArithmeticProcessor: Optional[Sequence["_ArithmeticProcessor"]]
    AttributeRemapper: Optional[Sequence["_AttributeRemapper"]]
    CategoryProcessor: Optional[Sequence["_CategoryProcessor"]]
    DateRemapper: Optional[Sequence["_DateRemapper"]]
    GeoIpParser: Optional[Sequence["_GeoIpParser"]]
    GrokParser: Optional[Sequence["_GrokParser"]]
    MessageRemapper: Optional[Sequence["_MessageRemapper"]]
    ServiceRemapper: Optional[Sequence["_ServiceRemapper"]]
    StatusRemapper: Optional[Sequence["_StatusRemapper"]]
    StringBuilderProcessor: Optional[Sequence["_StringBuilderProcessor"]]
    TraceIdRemapper: Optional[Sequence["_TraceIdRemapper"]]
    UrlParser: Optional[Sequence["_UrlParser"]]
    UserAgentParser: Optional[Sequence["_UserAgentParser"]]

    @classmethod
    def _deserialize(
        cls: Type["_Processor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Processor"]:
        if not json_data:
            return None
        return cls(
            ArithmeticProcessor=json_data.get("ArithmeticProcessor"),
            AttributeRemapper=json_data.get("AttributeRemapper"),
            CategoryProcessor=json_data.get("CategoryProcessor"),
            DateRemapper=json_data.get("DateRemapper"),
            GeoIpParser=json_data.get("GeoIpParser"),
            GrokParser=json_data.get("GrokParser"),
            MessageRemapper=json_data.get("MessageRemapper"),
            ServiceRemapper=json_data.get("ServiceRemapper"),
            StatusRemapper=json_data.get("StatusRemapper"),
            StringBuilderProcessor=json_data.get("StringBuilderProcessor"),
            TraceIdRemapper=json_data.get("TraceIdRemapper"),
            UrlParser=json_data.get("UrlParser"),
            UserAgentParser=json_data.get("UserAgentParser"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Processor = Processor


@dataclass
class ArithmeticProcessor:
    Expression: Optional[str]
    IsEnabled: Optional[bool]
    IsReplaceMissing: Optional[bool]
    Name: Optional[str]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ArithmeticProcessor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArithmeticProcessor"]:
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
_ArithmeticProcessor = ArithmeticProcessor


@dataclass
class AttributeRemapper:
    IsEnabled: Optional[bool]
    Name: Optional[str]
    OverrideOnConflict: Optional[bool]
    PreserveSource: Optional[bool]
    SourceType: Optional[str]
    Sources: Optional[Sequence[str]]
    Target: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeRemapper"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeRemapper"]:
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
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeRemapper = AttributeRemapper


@dataclass
class CategoryProcessor:
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Target: Optional[str]
    Category: Optional[Sequence["_Category"]]

    @classmethod
    def _deserialize(
        cls: Type["_CategoryProcessor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoryProcessor"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Target=json_data.get("Target"),
            Category=json_data.get("Category"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoryProcessor = CategoryProcessor


@dataclass
class Category:
    Name: Optional[str]
    Filter: Optional[Sequence["_Filter"]]

    @classmethod
    def _deserialize(
        cls: Type["_Category"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Category"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Filter=json_data.get("Filter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Category = Category


@dataclass
class DateRemapper:
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Sources: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DateRemapper"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateRemapper"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Sources=json_data.get("Sources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateRemapper = DateRemapper


@dataclass
class GeoIpParser:
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Sources: Optional[Sequence[str]]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeoIpParser"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoIpParser"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Sources=json_data.get("Sources"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoIpParser = GeoIpParser


@dataclass
class GrokParser:
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Samples: Optional[Sequence[str]]
    Source: Optional[str]
    Grok: Optional[Sequence["_Grok"]]

    @classmethod
    def _deserialize(
        cls: Type["_GrokParser"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrokParser"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Samples=json_data.get("Samples"),
            Source=json_data.get("Source"),
            Grok=json_data.get("Grok"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrokParser = GrokParser


@dataclass
class Grok:
    MatchRules: Optional[str]
    SupportRules: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Grok"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Grok"]:
        if not json_data:
            return None
        return cls(
            MatchRules=json_data.get("MatchRules"),
            SupportRules=json_data.get("SupportRules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Grok = Grok


@dataclass
class MessageRemapper:
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Sources: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MessageRemapper"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MessageRemapper"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Sources=json_data.get("Sources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MessageRemapper = MessageRemapper


@dataclass
class ServiceRemapper:
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Sources: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceRemapper"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceRemapper"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Sources=json_data.get("Sources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceRemapper = ServiceRemapper


@dataclass
class StatusRemapper:
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Sources: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_StatusRemapper"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusRemapper"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Sources=json_data.get("Sources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusRemapper = StatusRemapper


@dataclass
class StringBuilderProcessor:
    IsEnabled: Optional[bool]
    IsReplaceMissing: Optional[bool]
    Name: Optional[str]
    Target: Optional[str]
    Template: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StringBuilderProcessor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringBuilderProcessor"]:
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
_StringBuilderProcessor = StringBuilderProcessor


@dataclass
class TraceIdRemapper:
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Sources: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TraceIdRemapper"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TraceIdRemapper"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Sources=json_data.get("Sources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TraceIdRemapper = TraceIdRemapper


@dataclass
class UrlParser:
    IsEnabled: Optional[bool]
    Name: Optional[str]
    NormalizeEndingSlashes: Optional[bool]
    Sources: Optional[Sequence[str]]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UrlParser"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlParser"]:
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
_UrlParser = UrlParser


@dataclass
class UserAgentParser:
    IsEnabled: Optional[bool]
    IsEncoded: Optional[bool]
    Name: Optional[str]
    Sources: Optional[Sequence[str]]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserAgentParser"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserAgentParser"]:
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
_UserAgentParser = UserAgentParser


@dataclass
class Pipeline:
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Filter: Optional[Sequence["_Filter"]]
    Processor: Optional[Sequence["_Processor"]]

    @classmethod
    def _deserialize(
        cls: Type["_Pipeline"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Pipeline"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Filter=json_data.get("Filter"),
            Processor=json_data.get("Processor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Pipeline = Pipeline


