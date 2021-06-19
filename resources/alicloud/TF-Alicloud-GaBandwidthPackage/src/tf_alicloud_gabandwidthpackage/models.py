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
    AutoPay: Optional[bool]
    AutoUseCoupon: Optional[bool]
    Bandwidth: Optional[float]
    BandwidthPackageName: Optional[str]
    BandwidthType: Optional[str]
    BillingType: Optional[str]
    CbnGeographicRegionIda: Optional[str]
    CbnGeographicRegionIdb: Optional[str]
    Description: Optional[str]
    Duration: Optional[str]
    Id: Optional[str]
    PaymentType: Optional[str]
    Ratio: Optional[float]
    Status: Optional[str]
    Type: Optional[str]
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
            AutoPay=json_data.get("AutoPay"),
            AutoUseCoupon=json_data.get("AutoUseCoupon"),
            Bandwidth=json_data.get("Bandwidth"),
            BandwidthPackageName=json_data.get("BandwidthPackageName"),
            BandwidthType=json_data.get("BandwidthType"),
            BillingType=json_data.get("BillingType"),
            CbnGeographicRegionIda=json_data.get("CbnGeographicRegionIda"),
            CbnGeographicRegionIdb=json_data.get("CbnGeographicRegionIdb"),
            Description=json_data.get("Description"),
            Duration=json_data.get("Duration"),
            Id=json_data.get("Id"),
            PaymentType=json_data.get("PaymentType"),
            Ratio=json_data.get("Ratio"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


