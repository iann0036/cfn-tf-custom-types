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
    Arn: Optional[str]
    Id: Optional[str]
    KmsKeyArn: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    ProductionVariants: Optional[Sequence["_ProductionVariants"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            ProductionVariants=json_data.get("ProductionVariants"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class ProductionVariants:
    AcceleratorType: Optional[str]
    InitialInstanceCount: Optional[float]
    InitialVariantWeight: Optional[float]
    InstanceType: Optional[str]
    ModelName: Optional[str]
    VariantName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProductionVariants"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProductionVariants"]:
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
_ProductionVariants = ProductionVariants


