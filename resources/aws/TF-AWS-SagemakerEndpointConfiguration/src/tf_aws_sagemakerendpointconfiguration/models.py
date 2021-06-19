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
    Arn: Optional[str]
    Id: Optional[str]
    KmsKeyArn: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    DataCaptureConfig: Optional[Sequence["_DataCaptureConfigDefinition"]]
    ProductionVariants: Optional[Sequence["_ProductionVariantsDefinition"]]

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
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            Name=json_data.get("Name"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            DataCaptureConfig=deserialize_list(json_data.get("DataCaptureConfig"), DataCaptureConfigDefinition),
            ProductionVariants=deserialize_list(json_data.get("ProductionVariants"), ProductionVariantsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class DataCaptureConfigDefinition(BaseModel):
    DestinationS3Uri: Optional[str]
    EnableCapture: Optional[bool]
    InitialSamplingPercentage: Optional[float]
    KmsKeyId: Optional[str]
    CaptureContentTypeHeader: Optional[Sequence["_CaptureContentTypeHeaderDefinition"]]
    CaptureOptions: Optional[Sequence["_CaptureOptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DataCaptureConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataCaptureConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationS3Uri=json_data.get("DestinationS3Uri"),
            EnableCapture=json_data.get("EnableCapture"),
            InitialSamplingPercentage=json_data.get("InitialSamplingPercentage"),
            KmsKeyId=json_data.get("KmsKeyId"),
            CaptureContentTypeHeader=deserialize_list(json_data.get("CaptureContentTypeHeader"), CaptureContentTypeHeaderDefinition),
            CaptureOptions=deserialize_list(json_data.get("CaptureOptions"), CaptureOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataCaptureConfigDefinition = DataCaptureConfigDefinition


@dataclass
class CaptureContentTypeHeaderDefinition(BaseModel):
    CsvContentTypes: Optional[Sequence[str]]
    JsonContentTypes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CaptureContentTypeHeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaptureContentTypeHeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            CsvContentTypes=json_data.get("CsvContentTypes"),
            JsonContentTypes=json_data.get("JsonContentTypes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaptureContentTypeHeaderDefinition = CaptureContentTypeHeaderDefinition


@dataclass
class CaptureOptionsDefinition(BaseModel):
    CaptureMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CaptureOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaptureOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            CaptureMode=json_data.get("CaptureMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaptureOptionsDefinition = CaptureOptionsDefinition


@dataclass
class ProductionVariantsDefinition(BaseModel):
    AcceleratorType: Optional[str]
    InitialInstanceCount: Optional[float]
    InitialVariantWeight: Optional[float]
    InstanceType: Optional[str]
    ModelName: Optional[str]
    VariantName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProductionVariantsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProductionVariantsDefinition"]:
        if not json_data:
            return None
        return cls(
            AcceleratorType=json_data.get("AcceleratorType"),
            InitialInstanceCount=json_data.get("InitialInstanceCount"),
            InitialVariantWeight=json_data.get("InitialVariantWeight"),
            InstanceType=json_data.get("InstanceType"),
            ModelName=json_data.get("ModelName"),
            VariantName=json_data.get("VariantName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProductionVariantsDefinition = ProductionVariantsDefinition


