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
    Bandwidth: Optional[float]
    CenBandwidthPackageName: Optional[str]
    ChargeType: Optional[str]
    Description: Optional[str]
    ExpiredTime: Optional[str]
    GeographicRegionAId: Optional[str]
    GeographicRegionBId: Optional[str]
    GeographicRegionIds: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    PaymentType: Optional[str]
    Period: Optional[float]
    Status: Optional[str]
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
            Bandwidth=json_data.get("Bandwidth"),
            CenBandwidthPackageName=json_data.get("CenBandwidthPackageName"),
            ChargeType=json_data.get("ChargeType"),
            Description=json_data.get("Description"),
            ExpiredTime=json_data.get("ExpiredTime"),
            GeographicRegionAId=json_data.get("GeographicRegionAId"),
            GeographicRegionBId=json_data.get("GeographicRegionBId"),
            GeographicRegionIds=json_data.get("GeographicRegionIds"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PaymentType=json_data.get("PaymentType"),
            Period=json_data.get("Period"),
            Status=json_data.get("Status"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


