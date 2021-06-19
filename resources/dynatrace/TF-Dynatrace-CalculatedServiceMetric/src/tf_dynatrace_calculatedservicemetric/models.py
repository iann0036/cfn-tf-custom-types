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
    Enabled: Optional[bool]
    EntityId: Optional[str]
    Id: Optional[str]
    ManagementZones: Optional[Sequence[str]]
    MetricKey: Optional[str]
    Name: Optional[str]
    Unit: Optional[str]
    UnitDisplayName: Optional[str]
    Unknowns: Optional[str]
    Conditions: Optional[Sequence["_ConditionsDefinition"]]
    DimensionDefinition: Optional[Sequence["_DimensionDefinitionDefinition"]]
    MetricDefinition: Optional[Sequence["_MetricDefinitionDefinition"]]

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
            Enabled=json_data.get("Enabled"),
            EntityId=json_data.get("EntityId"),
            Id=json_data.get("Id"),
            ManagementZones=json_data.get("ManagementZones"),
            MetricKey=json_data.get("MetricKey"),
            Name=json_data.get("Name"),
            Unit=json_data.get("Unit"),
            UnitDisplayName=json_data.get("UnitDisplayName"),
            Unknowns=json_data.get("Unknowns"),
            Conditions=deserialize_list(json_data.get("Conditions"), ConditionsDefinition),
            DimensionDefinition=deserialize_list(json_data.get("DimensionDefinition"), DimensionDefinitionDefinition),
            MetricDefinition=deserialize_list(json_data.get("MetricDefinition"), MetricDefinitionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConditionsDefinition(BaseModel):
    Condition: Optional[Sequence["_ConditionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Condition=deserialize_list(json_data.get("Condition"), ConditionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionsDefinition = ConditionsDefinition


@dataclass
class ConditionDefinition(BaseModel):
    Attribute: Optional[str]
    Comparison: Optional[Sequence["_ComparisonDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            Comparison=deserialize_list(json_data.get("Comparison"), ComparisonDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionDefinition = ConditionDefinition


@dataclass
class ComparisonDefinition(BaseModel):
    Negate: Optional[bool]
    Boolean: Optional[Sequence["_BooleanDefinition"]]
    EsbInputNodeType: Optional[Sequence["_EsbInputNodeTypeDefinition"]]
    FailedState: Optional[Sequence["_FailedStateDefinition"]]
    FailureReason: Optional[Sequence["_FailureReasonDefinition"]]
    FastString: Optional[Sequence["_FastStringDefinition"]]
    FlawState: Optional[Sequence["_FlawStateDefinition"]]
    Generic: Optional[Sequence["_GenericDefinition"]]
    HttpMethod: Optional[Sequence["_HttpMethodDefinition"]]
    HttpStatusClass: Optional[Sequence["_HttpStatusClassDefinition"]]
    IibInputNodeType: Optional[Sequence["_IibInputNodeTypeDefinition"]]
    Number: Optional[Sequence["_NumberDefinition"]]
    NumberRequestAttribute: Optional[Sequence["_NumberRequestAttributeDefinition"]]
    ServiceType: Optional[Sequence["_ServiceTypeDefinition"]]
    String: Optional[Sequence["_StringDefinition"]]
    StringRequestAttribute: Optional[Sequence["_StringRequestAttributeDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]
    ZosCallType: Optional[Sequence["_ZosCallTypeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ComparisonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComparisonDefinition"]:
        if not json_data:
            return None
        return cls(
            Negate=json_data.get("Negate"),
            Boolean=deserialize_list(json_data.get("Boolean"), BooleanDefinition),
            EsbInputNodeType=deserialize_list(json_data.get("EsbInputNodeType"), EsbInputNodeTypeDefinition),
            FailedState=deserialize_list(json_data.get("FailedState"), FailedStateDefinition),
            FailureReason=deserialize_list(json_data.get("FailureReason"), FailureReasonDefinition),
            FastString=deserialize_list(json_data.get("FastString"), FastStringDefinition),
            FlawState=deserialize_list(json_data.get("FlawState"), FlawStateDefinition),
            Generic=deserialize_list(json_data.get("Generic"), GenericDefinition),
            HttpMethod=deserialize_list(json_data.get("HttpMethod"), HttpMethodDefinition),
            HttpStatusClass=deserialize_list(json_data.get("HttpStatusClass"), HttpStatusClassDefinition),
            IibInputNodeType=deserialize_list(json_data.get("IibInputNodeType"), IibInputNodeTypeDefinition),
            Number=deserialize_list(json_data.get("Number"), NumberDefinition),
            NumberRequestAttribute=deserialize_list(json_data.get("NumberRequestAttribute"), NumberRequestAttributeDefinition),
            ServiceType=deserialize_list(json_data.get("ServiceType"), ServiceTypeDefinition),
            String=deserialize_list(json_data.get("String"), StringDefinition),
            StringRequestAttribute=deserialize_list(json_data.get("StringRequestAttribute"), StringRequestAttributeDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
            ZosCallType=deserialize_list(json_data.get("ZosCallType"), ZosCallTypeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComparisonDefinition = ComparisonDefinition


@dataclass
class BooleanDefinition(BaseModel):
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[bool]
    Values: Optional[Sequence[bool]]

    @classmethod
    def _deserialize(
        cls: Type["_BooleanDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BooleanDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BooleanDefinition = BooleanDefinition


@dataclass
class EsbInputNodeTypeDefinition(BaseModel):
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_EsbInputNodeTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EsbInputNodeTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EsbInputNodeTypeDefinition = EsbInputNodeTypeDefinition


@dataclass
class FailedStateDefinition(BaseModel):
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FailedStateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailedStateDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailedStateDefinition = FailedStateDefinition


@dataclass
class FailureReasonDefinition(BaseModel):
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FailureReasonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailureReasonDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailureReasonDefinition = FailureReasonDefinition


@dataclass
class FastStringDefinition(BaseModel):
    CaseSensitive: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FastStringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FastStringDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FastStringDefinition = FastStringDefinition


@dataclass
class FlawStateDefinition(BaseModel):
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FlawStateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlawStateDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlawStateDefinition = FlawStateDefinition


@dataclass
class GenericDefinition(BaseModel):
    Type: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GenericDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GenericDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GenericDefinition = GenericDefinition


@dataclass
class HttpMethodDefinition(BaseModel):
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpMethodDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpMethodDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpMethodDefinition = HttpMethodDefinition


@dataclass
class HttpStatusClassDefinition(BaseModel):
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpStatusClassDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpStatusClassDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpStatusClassDefinition = HttpStatusClassDefinition


@dataclass
class IibInputNodeTypeDefinition(BaseModel):
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IibInputNodeTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IibInputNodeTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IibInputNodeTypeDefinition = IibInputNodeTypeDefinition


@dataclass
class NumberDefinition(BaseModel):
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[float]
    Values: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_NumberDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumberDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumberDefinition = NumberDefinition


@dataclass
class NumberRequestAttributeDefinition(BaseModel):
    MatchOnChildCalls: Optional[bool]
    Operator: Optional[str]
    RequestAttribute: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[float]
    Values: Optional[Sequence[float]]
    Source: Optional[Sequence["_SourceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NumberRequestAttributeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumberRequestAttributeDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchOnChildCalls=json_data.get("MatchOnChildCalls"),
            Operator=json_data.get("Operator"),
            RequestAttribute=json_data.get("RequestAttribute"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumberRequestAttributeDefinition = NumberRequestAttributeDefinition


@dataclass
class SourceDefinition(BaseModel):
    ManagementZone: Optional[str]
    Unknowns: Optional[str]
    ServiceTag: Optional[Sequence["_ServiceTagDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            ManagementZone=json_data.get("ManagementZone"),
            Unknowns=json_data.get("Unknowns"),
            ServiceTag=deserialize_list(json_data.get("ServiceTag"), ServiceTagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


@dataclass
class ServiceTagDefinition(BaseModel):
    Context: Optional[str]
    Key: Optional[str]
    Value: Optional[str]
    TagKey: Optional[Sequence["_TagKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceTagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceTagDefinition"]:
        if not json_data:
            return None
        return cls(
            Context=json_data.get("Context"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
            TagKey=deserialize_list(json_data.get("TagKey"), TagKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceTagDefinition = ServiceTagDefinition


@dataclass
class TagKeyDefinition(BaseModel):
    Context: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Context=json_data.get("Context"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagKeyDefinition = TagKeyDefinition


@dataclass
class ServiceTypeDefinition(BaseModel):
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceTypeDefinition = ServiceTypeDefinition


@dataclass
class StringDefinition(BaseModel):
    CaseSensitive: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_StringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringDefinition = StringDefinition


@dataclass
class StringRequestAttributeDefinition(BaseModel):
    CaseSensitive: Optional[bool]
    MatchOnChildCalls: Optional[bool]
    Operator: Optional[str]
    RequestAttribute: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]
    Values: Optional[Sequence[str]]
    Source: Optional[Sequence["_SourceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StringRequestAttributeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringRequestAttributeDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            MatchOnChildCalls=json_data.get("MatchOnChildCalls"),
            Operator=json_data.get("Operator"),
            RequestAttribute=json_data.get("RequestAttribute"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringRequestAttributeDefinition = StringRequestAttributeDefinition


@dataclass
class TagDefinition(BaseModel):
    Operator: Optional[str]
    Unknowns: Optional[str]
    Values: Optional[Sequence["_ValuesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Values=deserialize_list(json_data.get("Values"), ValuesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


@dataclass
class ValuesDefinition(BaseModel):
    Value: Optional[Sequence["_ValueDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=deserialize_list(json_data.get("Value"), ValueDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValuesDefinition = ValuesDefinition


@dataclass
class ValueDefinition(BaseModel):
    Context: Optional[str]
    Key: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValueDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueDefinition"]:
        if not json_data:
            return None
        return cls(
            Context=json_data.get("Context"),
            Key=json_data.get("Key"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueDefinition = ValueDefinition


@dataclass
class ZosCallTypeDefinition(BaseModel):
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ZosCallTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZosCallTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZosCallTypeDefinition = ZosCallTypeDefinition


@dataclass
class DimensionDefinitionDefinition(BaseModel):
    Dimension: Optional[str]
    Name: Optional[str]
    TopX: Optional[float]
    TopXAggregation: Optional[str]
    TopXDirection: Optional[str]
    Unknowns: Optional[str]
    Placeholders: Optional[Sequence["_PlaceholdersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Dimension=json_data.get("Dimension"),
            Name=json_data.get("Name"),
            TopX=json_data.get("TopX"),
            TopXAggregation=json_data.get("TopXAggregation"),
            TopXDirection=json_data.get("TopXDirection"),
            Unknowns=json_data.get("Unknowns"),
            Placeholders=deserialize_list(json_data.get("Placeholders"), PlaceholdersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionDefinitionDefinition = DimensionDefinitionDefinition


@dataclass
class PlaceholdersDefinition(BaseModel):
    Placeholder: Optional[Sequence["_PlaceholderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PlaceholdersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlaceholdersDefinition"]:
        if not json_data:
            return None
        return cls(
            Placeholder=deserialize_list(json_data.get("Placeholder"), PlaceholderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlaceholdersDefinition = PlaceholdersDefinition


@dataclass
class PlaceholderDefinition(BaseModel):
    Aggregation: Optional[str]
    Attribute: Optional[str]
    DelimiterOrRegex: Optional[str]
    EndDelimiter: Optional[str]
    Kind: Optional[str]
    Name: Optional[str]
    Normalization: Optional[str]
    RequestAttribute: Optional[str]
    Unknowns: Optional[str]
    UseFromChildCalls: Optional[bool]
    Source: Optional[Sequence["_SourceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PlaceholderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlaceholderDefinition"]:
        if not json_data:
            return None
        return cls(
            Aggregation=json_data.get("Aggregation"),
            Attribute=json_data.get("Attribute"),
            DelimiterOrRegex=json_data.get("DelimiterOrRegex"),
            EndDelimiter=json_data.get("EndDelimiter"),
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Normalization=json_data.get("Normalization"),
            RequestAttribute=json_data.get("RequestAttribute"),
            Unknowns=json_data.get("Unknowns"),
            UseFromChildCalls=json_data.get("UseFromChildCalls"),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlaceholderDefinition = PlaceholderDefinition


@dataclass
class MetricDefinitionDefinition(BaseModel):
    Metric: Optional[str]
    RequestAttribute: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Metric=json_data.get("Metric"),
            RequestAttribute=json_data.get("RequestAttribute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDefinitionDefinition = MetricDefinitionDefinition


