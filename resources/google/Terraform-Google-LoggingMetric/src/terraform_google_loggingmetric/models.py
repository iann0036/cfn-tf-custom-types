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
    Description: Optional[str]
    Filter: Optional[str]
    LabelExtractors: Optional[Sequence["_LabelExtractors"]]
    Name: Optional[str]
    Project: Optional[str]
    ValueExtractor: Optional[str]
    BucketOptions: Optional[Sequence["_BucketOptions"]]
    MetricDescriptor: Optional[Sequence["_MetricDescriptor"]]
    Timeouts: Optional["_Timeouts"]
    ExplicitBuckets: Optional[Sequence["_ExplicitBuckets"]]
    ExponentialBuckets: Optional[Sequence["_ExponentialBuckets"]]
    LinearBuckets: Optional[Sequence["_LinearBuckets"]]
    Labels: Optional[Sequence["_Labels"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Filter=json_data.get("Filter"),
            LabelExtractors=json_data.get("LabelExtractors"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            ValueExtractor=json_data.get("ValueExtractor"),
            BucketOptions=json_data.get("BucketOptions"),
            MetricDescriptor=json_data.get("MetricDescriptor"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            ExplicitBuckets=json_data.get("ExplicitBuckets"),
            ExponentialBuckets=json_data.get("ExponentialBuckets"),
            LinearBuckets=json_data.get("LinearBuckets"),
            Labels=json_data.get("Labels"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelExtractors:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelExtractors"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelExtractors"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelExtractors = LabelExtractors


@dataclass
class BucketOptions:
    ExplicitBuckets: Optional[Sequence["_ExplicitBuckets"]]
    ExponentialBuckets: Optional[Sequence["_ExponentialBuckets"]]
    LinearBuckets: Optional[Sequence["_LinearBuckets"]]

    @classmethod
    def _deserialize(
        cls: Type["_BucketOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BucketOptions"]:
        if not json_data:
            return None
        return cls(
            ExplicitBuckets=json_data.get("ExplicitBuckets"),
            ExponentialBuckets=json_data.get("ExponentialBuckets"),
            LinearBuckets=json_data.get("LinearBuckets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BucketOptions = BucketOptions


@dataclass
class ExplicitBuckets:
    Bounds: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_ExplicitBuckets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExplicitBuckets"]:
        if not json_data:
            return None
        return cls(
            Bounds=json_data.get("Bounds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExplicitBuckets = ExplicitBuckets


@dataclass
class ExponentialBuckets:
    GrowthFactor: Optional[float]
    NumFiniteBuckets: Optional[float]
    Scale: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ExponentialBuckets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExponentialBuckets"]:
        if not json_data:
            return None
        return cls(
            GrowthFactor=json_data.get("GrowthFactor"),
            NumFiniteBuckets=json_data.get("NumFiniteBuckets"),
            Scale=json_data.get("Scale"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExponentialBuckets = ExponentialBuckets


@dataclass
class LinearBuckets:
    NumFiniteBuckets: Optional[float]
    Offset: Optional[float]
    Width: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LinearBuckets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinearBuckets"]:
        if not json_data:
            return None
        return cls(
            NumFiniteBuckets=json_data.get("NumFiniteBuckets"),
            Offset=json_data.get("Offset"),
            Width=json_data.get("Width"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinearBuckets = LinearBuckets


@dataclass
class MetricDescriptor:
    DisplayName: Optional[str]
    MetricKind: Optional[str]
    Unit: Optional[str]
    ValueType: Optional[str]
    Labels: Optional[Sequence["_Labels"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDescriptor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDescriptor"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            MetricKind=json_data.get("MetricKind"),
            Unit=json_data.get("Unit"),
            ValueType=json_data.get("ValueType"),
            Labels=json_data.get("Labels"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDescriptor = MetricDescriptor


@dataclass
class Labels:
    Description: Optional[str]
    Key: Optional[str]
    ValueType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Key=json_data.get("Key"),
            ValueType=json_data.get("ValueType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


