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
    Bandwidth: Optional[float]
    ChargeType: Optional[str]
    CreateTime: Optional[str]
    ExpiredTime: Optional[str]
    Id: Optional[str]
    IsAddressBlocked: Optional[bool]
    Name: Optional[str]
    NewPurchasePlan: Optional[str]
    PrepaidPeriod: Optional[float]
    PrepaidRenewFlag: Optional[str]
    PublicIpAddress: Optional[str]
    RestrictState: Optional[str]
    State: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Type: Optional[str]
    VpcId: Optional[str]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Bandwidth=json_data.get("Bandwidth"),
            ChargeType=json_data.get("ChargeType"),
            CreateTime=json_data.get("CreateTime"),
            ExpiredTime=json_data.get("ExpiredTime"),
            Id=json_data.get("Id"),
            IsAddressBlocked=json_data.get("IsAddressBlocked"),
            Name=json_data.get("Name"),
            NewPurchasePlan=json_data.get("NewPurchasePlan"),
            PrepaidPeriod=json_data.get("PrepaidPeriod"),
            PrepaidRenewFlag=json_data.get("PrepaidRenewFlag"),
            PublicIpAddress=json_data.get("PublicIpAddress"),
            RestrictState=json_data.get("RestrictState"),
            State=json_data.get("State"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            VpcId=json_data.get("VpcId"),
            Zone=json_data.get("Zone"),
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


