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
    Components: Optional[Sequence["_Components"]]
    CouponId: Optional[str]
    Duration: Optional[float]
    PackageVersion: Optional[str]
    PayType: Optional[str]
    PricingCycle: Optional[str]
    ProductCode: Optional[str]
    Quantity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Components=json_data.get("Components"),
            CouponId=json_data.get("CouponId"),
            Duration=json_data.get("Duration"),
            PackageVersion=json_data.get("PackageVersion"),
            PayType=json_data.get("PayType"),
            PricingCycle=json_data.get("PricingCycle"),
            ProductCode=json_data.get("ProductCode"),
            Quantity=json_data.get("Quantity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Components:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Components"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Components"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Components = Components


