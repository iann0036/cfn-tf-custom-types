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
    AggregationRule: Optional[Sequence["_AggregationRuleDefinition"]]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Rule: Optional[Sequence["_RuleDefinition"]]

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
            AggregationRule=deserialize_list(json_data.get("AggregationRule"), AggregationRuleDefinition),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AggregationRuleDefinition(BaseModel):
    ClusterRoleSelectors: Optional[Sequence["_ClusterRoleSelectorsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AggregationRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggregationRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterRoleSelectors=deserialize_list(json_data.get("ClusterRoleSelectors"), ClusterRoleSelectorsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggregationRuleDefinition = AggregationRuleDefinition


@dataclass
class ClusterRoleSelectorsDefinition(BaseModel):
    MatchLabels: Optional[Sequence["_MatchLabelsDefinition"]]
    MatchExpressions: Optional[Sequence["_MatchExpressionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterRoleSelectorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterRoleSelectorsDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchLabels=deserialize_list(json_data.get("MatchLabels"), MatchLabelsDefinition),
            MatchExpressions=deserialize_list(json_data.get("MatchExpressions"), MatchExpressionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterRoleSelectorsDefinition = ClusterRoleSelectorsDefinition


@dataclass
class MatchLabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchLabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchLabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchLabelsDefinition = MatchLabelsDefinition


@dataclass
class MatchExpressionsDefinition(BaseModel):
    Key: Optional[str]
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchExpressionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchExpressionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchExpressionsDefinition = MatchExpressionsDefinition


@dataclass
class MetadataDefinition(BaseModel):
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class RuleDefinition(BaseModel):
    ApiGroups: Optional[Sequence[str]]
    NonResourceUrls: Optional[Sequence[str]]
    ResourceNames: Optional[Sequence[str]]
    Resources: Optional[Sequence[str]]
    Verbs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiGroups=json_data.get("ApiGroups"),
            NonResourceUrls=json_data.get("NonResourceUrls"),
            ResourceNames=json_data.get("ResourceNames"),
            Resources=json_data.get("Resources"),
            Verbs=json_data.get("Verbs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


