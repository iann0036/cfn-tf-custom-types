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
    ClusterId: Optional[str]
    DesiredPodNum: Optional[float]
    DockerGraphPath: Optional[str]
    ExtraArgs: Optional[Sequence[str]]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    MountTarget: Optional[str]
    Unschedulable: Optional[float]
    WorkerInstancesList: Optional[Sequence["_WorkerInstancesListDefinition"]]
    DataDisk: Optional[Sequence["_DataDiskDefinition"]]
    WorkerConfig: Optional[Sequence["_WorkerConfigDefinition"]]

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
            ClusterId=json_data.get("ClusterId"),
            DesiredPodNum=json_data.get("DesiredPodNum"),
            DockerGraphPath=json_data.get("DockerGraphPath"),
            ExtraArgs=json_data.get("ExtraArgs"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            MountTarget=json_data.get("MountTarget"),
            Unschedulable=json_data.get("Unschedulable"),
            WorkerInstancesList=deserialize_list(json_data.get("WorkerInstancesList"), WorkerInstancesListDefinition),
            DataDisk=deserialize_list(json_data.get("DataDisk"), DataDiskDefinition),
            WorkerConfig=deserialize_list(json_data.get("WorkerConfig"), WorkerConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class WorkerInstancesListDefinition(BaseModel):
    FailedReason: Optional[str]
    InstanceId: Optional[str]
    InstanceRole: Optional[str]
    InstanceState: Optional[str]
    LanIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerInstancesListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerInstancesListDefinition"]:
        if not json_data:
            return None
        return cls(
            FailedReason=json_data.get("FailedReason"),
            InstanceId=json_data.get("InstanceId"),
            InstanceRole=json_data.get("InstanceRole"),
            InstanceState=json_data.get("InstanceState"),
            LanIp=json_data.get("LanIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerInstancesListDefinition = WorkerInstancesListDefinition


@dataclass
class DataDiskDefinition(BaseModel):
    DiskSize: Optional[float]
    DiskType: Optional[str]
    SnapshotId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskSize=json_data.get("DiskSize"),
            DiskType=json_data.get("DiskType"),
            SnapshotId=json_data.get("SnapshotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDiskDefinition = DataDiskDefinition


@dataclass
class WorkerConfigDefinition(BaseModel):
    AvailabilityZone: Optional[str]
    CamRoleName: Optional[str]
    Count: Optional[float]
    DesiredPodNum: Optional[float]
    DisasterRecoverGroupIds: Optional[Sequence[str]]
    EnhancedMonitorService: Optional[bool]
    EnhancedSecurityService: Optional[bool]
    Hostname: Optional[str]
    ImgId: Optional[str]
    InstanceChargeType: Optional[str]
    InstanceChargeTypePrepaidPeriod: Optional[float]
    InstanceChargeTypePrepaidRenewFlag: Optional[str]
    InstanceName: Optional[str]
    InstanceType: Optional[str]
    InternetChargeType: Optional[str]
    InternetMaxBandwidthOut: Optional[float]
    KeyIds: Optional[Sequence[str]]
    Password: Optional[str]
    PublicIpAssigned: Optional[bool]
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetId: Optional[str]
    SystemDiskSize: Optional[float]
    SystemDiskType: Optional[str]
    UserData: Optional[str]
    DataDisk: Optional[Sequence["_DataDiskDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            CamRoleName=json_data.get("CamRoleName"),
            Count=json_data.get("Count"),
            DesiredPodNum=json_data.get("DesiredPodNum"),
            DisasterRecoverGroupIds=json_data.get("DisasterRecoverGroupIds"),
            EnhancedMonitorService=json_data.get("EnhancedMonitorService"),
            EnhancedSecurityService=json_data.get("EnhancedSecurityService"),
            Hostname=json_data.get("Hostname"),
            ImgId=json_data.get("ImgId"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            InstanceChargeTypePrepaidPeriod=json_data.get("InstanceChargeTypePrepaidPeriod"),
            InstanceChargeTypePrepaidRenewFlag=json_data.get("InstanceChargeTypePrepaidRenewFlag"),
            InstanceName=json_data.get("InstanceName"),
            InstanceType=json_data.get("InstanceType"),
            InternetChargeType=json_data.get("InternetChargeType"),
            InternetMaxBandwidthOut=json_data.get("InternetMaxBandwidthOut"),
            KeyIds=json_data.get("KeyIds"),
            Password=json_data.get("Password"),
            PublicIpAssigned=json_data.get("PublicIpAssigned"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetId=json_data.get("SubnetId"),
            SystemDiskSize=json_data.get("SystemDiskSize"),
            SystemDiskType=json_data.get("SystemDiskType"),
            UserData=json_data.get("UserData"),
            DataDisk=deserialize_list(json_data.get("DataDisk"), DataDiskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerConfigDefinition = WorkerConfigDefinition


