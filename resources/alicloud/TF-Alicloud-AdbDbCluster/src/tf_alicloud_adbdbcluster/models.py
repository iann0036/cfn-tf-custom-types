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
    AutoRenewPeriod: Optional[float]
    ComputeResource: Optional[str]
    ConnectionString: Optional[str]
    DbClusterCategory: Optional[str]
    DbClusterClass: Optional[str]
    DbClusterVersion: Optional[str]
    DbNodeClass: Optional[str]
    DbNodeCount: Optional[float]
    DbNodeStorage: Optional[float]
    Description: Optional[str]
    ElasticIoResource: Optional[float]
    Id: Optional[str]
    MaintainTime: Optional[str]
    Mode: Optional[str]
    ModifyType: Optional[str]
    PayType: Optional[str]
    PaymentType: Optional[str]
    Period: Optional[float]
    RenewalStatus: Optional[str]
    ResourceGroupId: Optional[str]
    SecurityIps: Optional[Sequence[str]]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
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
            AutoRenewPeriod=json_data.get("AutoRenewPeriod"),
            ComputeResource=json_data.get("ComputeResource"),
            ConnectionString=json_data.get("ConnectionString"),
            DbClusterCategory=json_data.get("DbClusterCategory"),
            DbClusterClass=json_data.get("DbClusterClass"),
            DbClusterVersion=json_data.get("DbClusterVersion"),
            DbNodeClass=json_data.get("DbNodeClass"),
            DbNodeCount=json_data.get("DbNodeCount"),
            DbNodeStorage=json_data.get("DbNodeStorage"),
            Description=json_data.get("Description"),
            ElasticIoResource=json_data.get("ElasticIoResource"),
            Id=json_data.get("Id"),
            MaintainTime=json_data.get("MaintainTime"),
            Mode=json_data.get("Mode"),
            ModifyType=json_data.get("ModifyType"),
            PayType=json_data.get("PayType"),
            PaymentType=json_data.get("PaymentType"),
            Period=json_data.get("Period"),
            RenewalStatus=json_data.get("RenewalStatus"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            SecurityIps=json_data.get("SecurityIps"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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


