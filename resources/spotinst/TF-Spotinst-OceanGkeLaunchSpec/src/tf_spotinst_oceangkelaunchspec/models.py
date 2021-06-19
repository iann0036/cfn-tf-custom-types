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
    OceanId: Optional[str]
    RestrictScaleDown: Optional[bool]
    SourceImage: Optional[str]
    AutoscaleHeadrooms: Optional[Sequence["_AutoscaleHeadroomsDefinition"]]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Strategy: Optional[Sequence["_StrategyDefinition"]]
    Taints: Optional[Sequence["_TaintsDefinition"]]

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
            OceanId=json_data.get("OceanId"),
            RestrictScaleDown=json_data.get("RestrictScaleDown"),
            SourceImage=json_data.get("SourceImage"),
            AutoscaleHeadrooms=deserialize_list(json_data.get("AutoscaleHeadrooms"), AutoscaleHeadroomsDefinition),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Strategy=deserialize_list(json_data.get("Strategy"), StrategyDefinition),
            Taints=deserialize_list(json_data.get("Taints"), TaintsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutoscaleHeadroomsDefinition(BaseModel):
    CpuPerUnit: Optional[float]
    GpuPerUnit: Optional[float]
    MemoryPerUnit: Optional[float]
    NumOfUnits: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleHeadroomsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleHeadroomsDefinition"]:
        if not json_data:
            return None
        return cls(
            CpuPerUnit=json_data.get("CpuPerUnit"),
            GpuPerUnit=json_data.get("GpuPerUnit"),
            MemoryPerUnit=json_data.get("MemoryPerUnit"),
            NumOfUnits=json_data.get("NumOfUnits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleHeadroomsDefinition = AutoscaleHeadroomsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class MetadataDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class StrategyDefinition(BaseModel):
    PreemptiblePercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StrategyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StrategyDefinition"]:
        if not json_data:
            return None
        return cls(
            PreemptiblePercentage=json_data.get("PreemptiblePercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StrategyDefinition = StrategyDefinition


@dataclass
class TaintsDefinition(BaseModel):
    Effect: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaintsDefinition"]:
        if not json_data:
            return None
        return cls(
            Effect=json_data.get("Effect"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaintsDefinition = TaintsDefinition


