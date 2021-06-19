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
    AutoRenewFlag: Optional[float]
    AvailableZone: Optional[str]
    ChargeType: Optional[str]
    Charset: Optional[str]
    ClusterName: Optional[str]
    ClusterStatus: Optional[str]
    CreateTime: Optional[str]
    DbType: Optional[str]
    DbVersion: Optional[str]
    ForceDelete: Optional[bool]
    Id: Optional[str]
    InstanceCpuCore: Optional[float]
    InstanceId: Optional[str]
    InstanceMaintainDuration: Optional[float]
    InstanceMaintainStartTime: Optional[float]
    InstanceMaintainWeekdays: Optional[Sequence[str]]
    InstanceMemorySize: Optional[float]
    InstanceName: Optional[str]
    InstanceStatus: Optional[str]
    InstanceStorageSize: Optional[float]
    Password: Optional[str]
    Port: Optional[float]
    PrepaidPeriod: Optional[float]
    ProjectId: Optional[float]
    RoGroupAddr: Optional[Sequence["_RoGroupAddrDefinition"]]
    RoGroupId: Optional[str]
    RoGroupInstances: Optional[Sequence["_RoGroupInstancesDefinition"]]
    RoGroupSg: Optional[Sequence[str]]
    RwGroupAddr: Optional[Sequence["_RwGroupAddrDefinition"]]
    RwGroupId: Optional[str]
    RwGroupInstances: Optional[Sequence["_RwGroupInstancesDefinition"]]
    RwGroupSg: Optional[Sequence[str]]
    StorageLimit: Optional[float]
    StorageUsed: Optional[float]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VpcId: Optional[str]

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
            AutoRenewFlag=json_data.get("AutoRenewFlag"),
            AvailableZone=json_data.get("AvailableZone"),
            ChargeType=json_data.get("ChargeType"),
            Charset=json_data.get("Charset"),
            ClusterName=json_data.get("ClusterName"),
            ClusterStatus=json_data.get("ClusterStatus"),
            CreateTime=json_data.get("CreateTime"),
            DbType=json_data.get("DbType"),
            DbVersion=json_data.get("DbVersion"),
            ForceDelete=json_data.get("ForceDelete"),
            Id=json_data.get("Id"),
            InstanceCpuCore=json_data.get("InstanceCpuCore"),
            InstanceId=json_data.get("InstanceId"),
            InstanceMaintainDuration=json_data.get("InstanceMaintainDuration"),
            InstanceMaintainStartTime=json_data.get("InstanceMaintainStartTime"),
            InstanceMaintainWeekdays=json_data.get("InstanceMaintainWeekdays"),
            InstanceMemorySize=json_data.get("InstanceMemorySize"),
            InstanceName=json_data.get("InstanceName"),
            InstanceStatus=json_data.get("InstanceStatus"),
            InstanceStorageSize=json_data.get("InstanceStorageSize"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            PrepaidPeriod=json_data.get("PrepaidPeriod"),
            ProjectId=json_data.get("ProjectId"),
            RoGroupAddr=deserialize_list(json_data.get("RoGroupAddr"), RoGroupAddrDefinition),
            RoGroupId=json_data.get("RoGroupId"),
            RoGroupInstances=deserialize_list(json_data.get("RoGroupInstances"), RoGroupInstancesDefinition),
            RoGroupSg=json_data.get("RoGroupSg"),
            RwGroupAddr=deserialize_list(json_data.get("RwGroupAddr"), RwGroupAddrDefinition),
            RwGroupId=json_data.get("RwGroupId"),
            RwGroupInstances=deserialize_list(json_data.get("RwGroupInstances"), RwGroupInstancesDefinition),
            RwGroupSg=json_data.get("RwGroupSg"),
            StorageLimit=json_data.get("StorageLimit"),
            StorageUsed=json_data.get("StorageUsed"),
            SubnetId=json_data.get("SubnetId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RoGroupAddrDefinition(BaseModel):
    Ip: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RoGroupAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoGroupAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoGroupAddrDefinition = RoGroupAddrDefinition


@dataclass
class RoGroupInstancesDefinition(BaseModel):
    InstanceId: Optional[str]
    InstanceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RoGroupInstancesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoGroupInstancesDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceId=json_data.get("InstanceId"),
            InstanceName=json_data.get("InstanceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoGroupInstancesDefinition = RoGroupInstancesDefinition


@dataclass
class RwGroupAddrDefinition(BaseModel):
    Ip: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RwGroupAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RwGroupAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RwGroupAddrDefinition = RwGroupAddrDefinition


@dataclass
class RwGroupInstancesDefinition(BaseModel):
    InstanceId: Optional[str]
    InstanceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RwGroupInstancesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RwGroupInstancesDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceId=json_data.get("InstanceId"),
            InstanceName=json_data.get("InstanceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RwGroupInstancesDefinition = RwGroupInstancesDefinition


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


