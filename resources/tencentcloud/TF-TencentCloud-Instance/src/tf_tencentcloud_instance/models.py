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
    AllocatePublicIp: Optional[bool]
    AvailabilityZone: Optional[str]
    CamRoleName: Optional[str]
    CdhHostId: Optional[str]
    CdhInstanceType: Optional[str]
    CreateTime: Optional[str]
    DisableMonitorService: Optional[bool]
    DisableSecurityService: Optional[bool]
    ExpiredTime: Optional[str]
    ForceDelete: Optional[bool]
    Hostname: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    InstanceChargeType: Optional[str]
    InstanceChargeTypePrepaidPeriod: Optional[float]
    InstanceChargeTypePrepaidRenewFlag: Optional[str]
    InstanceName: Optional[str]
    InstanceStatus: Optional[str]
    InstanceType: Optional[str]
    InternetChargeType: Optional[str]
    InternetMaxBandwidthOut: Optional[float]
    KeepImageLogin: Optional[bool]
    KeyName: Optional[str]
    Password: Optional[str]
    PlacementGroupId: Optional[str]
    PrivateIp: Optional[str]
    ProjectId: Optional[float]
    PublicIp: Optional[str]
    RunningFlag: Optional[bool]
    SecurityGroups: Optional[Sequence[str]]
    SpotInstanceType: Optional[str]
    SpotMaxPrice: Optional[str]
    SubnetId: Optional[str]
    SystemDiskId: Optional[str]
    SystemDiskSize: Optional[float]
    SystemDiskType: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    UserData: Optional[str]
    UserDataRaw: Optional[str]
    VpcId: Optional[str]
    DataDisks: Optional[Sequence["_DataDisksDefinition"]]

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
            AllocatePublicIp=json_data.get("AllocatePublicIp"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            CamRoleName=json_data.get("CamRoleName"),
            CdhHostId=json_data.get("CdhHostId"),
            CdhInstanceType=json_data.get("CdhInstanceType"),
            CreateTime=json_data.get("CreateTime"),
            DisableMonitorService=json_data.get("DisableMonitorService"),
            DisableSecurityService=json_data.get("DisableSecurityService"),
            ExpiredTime=json_data.get("ExpiredTime"),
            ForceDelete=json_data.get("ForceDelete"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            InstanceChargeTypePrepaidPeriod=json_data.get("InstanceChargeTypePrepaidPeriod"),
            InstanceChargeTypePrepaidRenewFlag=json_data.get("InstanceChargeTypePrepaidRenewFlag"),
            InstanceName=json_data.get("InstanceName"),
            InstanceStatus=json_data.get("InstanceStatus"),
            InstanceType=json_data.get("InstanceType"),
            InternetChargeType=json_data.get("InternetChargeType"),
            InternetMaxBandwidthOut=json_data.get("InternetMaxBandwidthOut"),
            KeepImageLogin=json_data.get("KeepImageLogin"),
            KeyName=json_data.get("KeyName"),
            Password=json_data.get("Password"),
            PlacementGroupId=json_data.get("PlacementGroupId"),
            PrivateIp=json_data.get("PrivateIp"),
            ProjectId=json_data.get("ProjectId"),
            PublicIp=json_data.get("PublicIp"),
            RunningFlag=json_data.get("RunningFlag"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SpotInstanceType=json_data.get("SpotInstanceType"),
            SpotMaxPrice=json_data.get("SpotMaxPrice"),
            SubnetId=json_data.get("SubnetId"),
            SystemDiskId=json_data.get("SystemDiskId"),
            SystemDiskSize=json_data.get("SystemDiskSize"),
            SystemDiskType=json_data.get("SystemDiskType"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            UserData=json_data.get("UserData"),
            UserDataRaw=json_data.get("UserDataRaw"),
            VpcId=json_data.get("VpcId"),
            DataDisks=deserialize_list(json_data.get("DataDisks"), DataDisksDefinition),
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
class DataDisksDefinition(BaseModel):
    DataDiskId: Optional[str]
    DataDiskSize: Optional[float]
    DataDiskSnapshotId: Optional[str]
    DataDiskType: Optional[str]
    DeleteWithInstance: Optional[bool]
    Encrypt: Optional[bool]
    ThroughputPerformance: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DataDisksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDisksDefinition"]:
        if not json_data:
            return None
        return cls(
            DataDiskId=json_data.get("DataDiskId"),
            DataDiskSize=json_data.get("DataDiskSize"),
            DataDiskSnapshotId=json_data.get("DataDiskSnapshotId"),
            DataDiskType=json_data.get("DataDiskType"),
            DeleteWithInstance=json_data.get("DeleteWithInstance"),
            Encrypt=json_data.get("Encrypt"),
            ThroughputPerformance=json_data.get("ThroughputPerformance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDisksDefinition = DataDisksDefinition


