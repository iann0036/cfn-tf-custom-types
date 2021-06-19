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
    AutoRenew: Optional[bool]
    AutoRenewPeriod: Optional[float]
    ClusterId: Optional[str]
    DataCenterId: Optional[str]
    DataCenterName: Optional[str]
    DiskSize: Optional[float]
    DiskType: Optional[str]
    EnablePublic: Optional[bool]
    Id: Optional[str]
    InstanceType: Optional[str]
    NodeCount: Optional[float]
    PayType: Optional[str]
    Period: Optional[float]
    PeriodUnit: Optional[str]
    PublicPoints: Optional[Sequence[str]]
    Status: Optional[str]
    VswitchId: Optional[str]
    ZoneId: Optional[str]
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
            AutoRenew=json_data.get("AutoRenew"),
            AutoRenewPeriod=json_data.get("AutoRenewPeriod"),
            ClusterId=json_data.get("ClusterId"),
            DataCenterId=json_data.get("DataCenterId"),
            DataCenterName=json_data.get("DataCenterName"),
            DiskSize=json_data.get("DiskSize"),
            DiskType=json_data.get("DiskType"),
            EnablePublic=json_data.get("EnablePublic"),
            Id=json_data.get("Id"),
            InstanceType=json_data.get("InstanceType"),
            NodeCount=json_data.get("NodeCount"),
            PayType=json_data.get("PayType"),
            Period=json_data.get("Period"),
            PeriodUnit=json_data.get("PeriodUnit"),
            PublicPoints=json_data.get("PublicPoints"),
            Status=json_data.get("Status"),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
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


