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
    Filter: Optional[str]
    Id: Optional[str]
    LabelExtractors: Optional[Sequence["_LabelExtractorsDefinition"]]
    Name: Optional[str]
    Project: Optional[str]
    ValueExtractor: Optional[str]
    BucketOptions: Optional[Sequence["_BucketOptionsDefinition"]]
    MetricDescriptor: Optional[Sequence["_MetricDescriptorDefinition"]]
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
            Filter=json_data.get("Filter"),
            Id=json_data.get("Id"),
            LabelExtractors=deserialize_list(json_data.get("LabelExtractors"), LabelExtractorsDefinition),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            ValueExtractor=json_data.get("ValueExtractor"),
            BucketOptions=deserialize_list(json_data.get("BucketOptions"), BucketOptionsDefinition),
            MetricDescriptor=deserialize_list(json_data.get("MetricDescriptor"), MetricDescriptorDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelExtractorsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelExtractorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelExtractorsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelExtractorsDefinition = LabelExtractorsDefinition


@dataclass
class BucketOptionsDefinition(BaseModel):
    ExplicitBuckets: Optional[Sequence["_ExplicitBucketsDefinition"]]
    ExponentialBuckets: Optional[Sequence["_ExponentialBucketsDefinition"]]
    LinearBuckets: Optional[Sequence["_LinearBucketsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BucketOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BucketOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ExplicitBuckets=deserialize_list(json_data.get("ExplicitBuckets"), ExplicitBucketsDefinition),
            ExponentialBuckets=deserialize_list(json_data.get("ExponentialBuckets"), ExponentialBucketsDefinition),
            LinearBuckets=deserialize_list(json_data.get("LinearBuckets"), LinearBucketsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BucketOptionsDefinition = BucketOptionsDefinition


@dataclass
class ExplicitBucketsDefinition(BaseModel):
    Bounds: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_ExplicitBucketsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExplicitBucketsDefinition"]:
        if not json_data:
            return None
        return cls(
            Bounds=json_data.get("Bounds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExplicitBucketsDefinition = ExplicitBucketsDefinition


@dataclass
class ExponentialBucketsDefinition(BaseModel):
    GrowthFactor: Optional[float]
    NumFiniteBuckets: Optional[float]
    Scale: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ExponentialBucketsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExponentialBucketsDefinition"]:
        if not json_data:
            return None
        return cls(
            GrowthFactor=json_data.get("GrowthFactor"),
            NumFiniteBuckets=json_data.get("NumFiniteBuckets"),
            Scale=json_data.get("Scale"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExponentialBucketsDefinition = ExponentialBucketsDefinition


@dataclass
class LinearBucketsDefinition(BaseModel):
    NumFiniteBuckets: Optional[float]
    Offset: Optional[float]
    Width: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LinearBucketsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinearBucketsDefinition"]:
        if not json_data:
            return None
        return cls(
            NumFiniteBuckets=json_data.get("NumFiniteBuckets"),
            Offset=json_data.get("Offset"),
            Width=json_data.get("Width"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinearBucketsDefinition = LinearBucketsDefinition


@dataclass
class MetricDescriptorDefinition(BaseModel):
    DisplayName: Optional[str]
    MetricKind: Optional[str]
    Unit: Optional[str]
    ValueType: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDescriptorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDescriptorDefinition"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            MetricKind=json_data.get("MetricKind"),
            Unit=json_data.get("Unit"),
            ValueType=json_data.get("ValueType"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDescriptorDefinition = MetricDescriptorDefinition


@dataclass
class LabelsDefinition(BaseModel):
    Description: Optional[str]
    Key: Optional[str]
    ValueType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Key=json_data.get("Key"),
            ValueType=json_data.get("ValueType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


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


