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
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Spec: Optional[Sequence["_SpecDefinition"]]

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
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Spec=deserialize_list(json_data.get("Spec"), SpecDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    GenerateName: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            GenerateName=json_data.get("GenerateName"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
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
class SpecDefinition(BaseModel):
    MaxReplicas: Optional[float]
    MinReplicas: Optional[float]
    TargetCpuUtilizationPercentage: Optional[float]
    Metric: Optional[Sequence["_MetricDefinition"]]
    ScaleTargetRef: Optional[Sequence["_ScaleTargetRefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxReplicas=json_data.get("MaxReplicas"),
            MinReplicas=json_data.get("MinReplicas"),
            TargetCpuUtilizationPercentage=json_data.get("TargetCpuUtilizationPercentage"),
            Metric=deserialize_list(json_data.get("Metric"), MetricDefinition),
            ScaleTargetRef=deserialize_list(json_data.get("ScaleTargetRef"), ScaleTargetRefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecDefinition = SpecDefinition


@dataclass
class MetricDefinition(BaseModel):
    Name: Optional[str]
    Selector: Optional[Sequence["_SelectorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Selector=deserialize_list(json_data.get("Selector"), SelectorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDefinition = MetricDefinition


@dataclass
class SelectorDefinition(BaseModel):
    MatchLabels: Optional[Sequence["_MatchLabelsDefinition"]]
    MatchExpressions: Optional[Sequence["_MatchExpressionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchLabels=deserialize_list(json_data.get("MatchLabels"), MatchLabelsDefinition),
            MatchExpressions=deserialize_list(json_data.get("MatchExpressions"), MatchExpressionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelectorDefinition = SelectorDefinition


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
class ScaleTargetRefDefinition(BaseModel):
    ApiVersion: Optional[str]
    Kind: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScaleTargetRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScaleTargetRefDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiVersion=json_data.get("ApiVersion"),
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScaleTargetRefDefinition = ScaleTargetRefDefinition


