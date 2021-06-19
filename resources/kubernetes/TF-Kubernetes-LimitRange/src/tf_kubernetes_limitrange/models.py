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
    Limit: Optional[Sequence["_LimitDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecDefinition"]:
        if not json_data:
            return None
        return cls(
            Limit=deserialize_list(json_data.get("Limit"), LimitDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecDefinition = SpecDefinition


@dataclass
class LimitDefinition(BaseModel):
    Default: Optional[Sequence["_DefaultDefinition"]]
    DefaultRequest: Optional[Sequence["_DefaultRequestDefinition"]]
    Max: Optional[Sequence["_MaxDefinition"]]
    MaxLimitRequestRatio: Optional[Sequence["_MaxLimitRequestRatioDefinition"]]
    Min: Optional[Sequence["_MinDefinition"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LimitDefinition"]:
        if not json_data:
            return None
        return cls(
            Default=deserialize_list(json_data.get("Default"), DefaultDefinition),
            DefaultRequest=deserialize_list(json_data.get("DefaultRequest"), DefaultRequestDefinition),
            Max=deserialize_list(json_data.get("Max"), MaxDefinition),
            MaxLimitRequestRatio=deserialize_list(json_data.get("MaxLimitRequestRatio"), MaxLimitRequestRatioDefinition),
            Min=deserialize_list(json_data.get("Min"), MinDefinition),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LimitDefinition = LimitDefinition


@dataclass
class DefaultDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultDefinition = DefaultDefinition


@dataclass
class DefaultRequestDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultRequestDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultRequestDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultRequestDefinition = DefaultRequestDefinition


@dataclass
class MaxDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaxDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaxDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaxDefinition = MaxDefinition


@dataclass
class MaxLimitRequestRatioDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaxLimitRequestRatioDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaxLimitRequestRatioDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaxLimitRequestRatioDefinition = MaxLimitRequestRatioDefinition


@dataclass
class MinDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MinDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MinDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MinDefinition = MinDefinition


