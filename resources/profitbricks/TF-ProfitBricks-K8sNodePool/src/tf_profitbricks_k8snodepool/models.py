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
    AvailabilityZone: Optional[str]
    CoresCount: Optional[float]
    CpuFamily: Optional[str]
    DatacenterId: Optional[str]
    Id: Optional[str]
    K8sClusterId: Optional[str]
    K8sVersion: Optional[str]
    Lans: Optional[Sequence[float]]
    Name: Optional[str]
    NodeCount: Optional[float]
    PublicIps: Optional[Sequence[str]]
    RamSize: Optional[float]
    StorageSize: Optional[float]
    StorageType: Optional[str]
    AutoScaling: Optional[Sequence["_AutoScalingDefinition"]]
    MaintenanceWindow: Optional[Sequence["_MaintenanceWindowDefinition"]]
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
            AvailabilityZone=json_data.get("AvailabilityZone"),
            CoresCount=json_data.get("CoresCount"),
            CpuFamily=json_data.get("CpuFamily"),
            DatacenterId=json_data.get("DatacenterId"),
            Id=json_data.get("Id"),
            K8sClusterId=json_data.get("K8sClusterId"),
            K8sVersion=json_data.get("K8sVersion"),
            Lans=json_data.get("Lans"),
            Name=json_data.get("Name"),
            NodeCount=json_data.get("NodeCount"),
            PublicIps=json_data.get("PublicIps"),
            RamSize=json_data.get("RamSize"),
            StorageSize=json_data.get("StorageSize"),
            StorageType=json_data.get("StorageType"),
            AutoScaling=deserialize_list(json_data.get("AutoScaling"), AutoScalingDefinition),
            MaintenanceWindow=deserialize_list(json_data.get("MaintenanceWindow"), MaintenanceWindowDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutoScalingDefinition(BaseModel):
    MaxNodeCount: Optional[float]
    MinNodeCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScalingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScalingDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxNodeCount=json_data.get("MaxNodeCount"),
            MinNodeCount=json_data.get("MinNodeCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScalingDefinition = AutoScalingDefinition


@dataclass
class MaintenanceWindowDefinition(BaseModel):
    DayOfTheWeek: Optional[str]
    Time: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowDefinition"]:
        if not json_data:
            return None
        return cls(
            DayOfTheWeek=json_data.get("DayOfTheWeek"),
            Time=json_data.get("Time"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowDefinition = MaintenanceWindowDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Default: Optional[str]
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
            Default=json_data.get("Default"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


