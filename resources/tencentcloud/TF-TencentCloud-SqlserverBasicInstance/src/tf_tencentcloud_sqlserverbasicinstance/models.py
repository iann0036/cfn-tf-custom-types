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
    AutoRenew: Optional[float]
    AutoVoucher: Optional[float]
    AvailabilityZone: Optional[str]
    ChargeType: Optional[str]
    Cpu: Optional[float]
    CreateTime: Optional[str]
    EngineVersion: Optional[str]
    Id: Optional[str]
    MachineType: Optional[str]
    MaintenanceStartTime: Optional[str]
    MaintenanceTimeSpan: Optional[float]
    MaintenanceWeekSet: Optional[Sequence[float]]
    Memory: Optional[float]
    Name: Optional[str]
    Period: Optional[float]
    ProjectId: Optional[float]
    SecurityGroups: Optional[Sequence[str]]
    Status: Optional[float]
    Storage: Optional[float]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Vip: Optional[str]
    VoucherIds: Optional[Sequence[str]]
    VpcId: Optional[str]
    Vport: Optional[float]

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
            AutoVoucher=json_data.get("AutoVoucher"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            ChargeType=json_data.get("ChargeType"),
            Cpu=json_data.get("Cpu"),
            CreateTime=json_data.get("CreateTime"),
            EngineVersion=json_data.get("EngineVersion"),
            Id=json_data.get("Id"),
            MachineType=json_data.get("MachineType"),
            MaintenanceStartTime=json_data.get("MaintenanceStartTime"),
            MaintenanceTimeSpan=json_data.get("MaintenanceTimeSpan"),
            MaintenanceWeekSet=json_data.get("MaintenanceWeekSet"),
            Memory=json_data.get("Memory"),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
            ProjectId=json_data.get("ProjectId"),
            SecurityGroups=json_data.get("SecurityGroups"),
            Status=json_data.get("Status"),
            Storage=json_data.get("Storage"),
            SubnetId=json_data.get("SubnetId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Vip=json_data.get("Vip"),
            VoucherIds=json_data.get("VoucherIds"),
            VpcId=json_data.get("VpcId"),
            Vport=json_data.get("Vport"),
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

