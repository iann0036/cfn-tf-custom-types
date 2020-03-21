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
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PricingPlan: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    ReservationPlanSettings: Optional[Sequence["_ReservationPlanSettings"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PricingPlan=json_data.get("PricingPlan"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            ReservationPlanSettings=json_data.get("ReservationPlanSettings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class ReservationPlanSettings:
    Commitment: Optional[str]
    RenewalType: Optional[str]
    ReservedSlots: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ReservationPlanSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReservationPlanSettings"]:
        if not json_data:
            return None
        return cls(
            Commitment=json_data.get("Commitment"),
            RenewalType=json_data.get("RenewalType"),
            ReservedSlots=json_data.get("ReservedSlots"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReservationPlanSettings = ReservationPlanSettings


