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
    AutoScalingGroupId: Optional[str]
    ClusterId: Optional[str]
    DeleteKeepInstance: Optional[bool]
    DesiredCapacity: Optional[float]
    EnableAutoScale: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    LaunchConfigId: Optional[str]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Name: Optional[str]
    NodeCount: Optional[float]
    NodeOs: Optional[str]
    NodeOsType: Optional[str]
    RetryPolicy: Optional[str]
    ScalingMode: Optional[str]
    Status: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Unschedulable: Optional[float]
    VpcId: Optional[str]
    AutoScalingConfig: Optional[Sequence["_AutoScalingConfigDefinition"]]
    NodeConfig: Optional[Sequence["_NodeConfigDefinition"]]
    Taints: Optional[Sequence["_TaintsDefinition"]]

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
            AutoScalingGroupId=json_data.get("AutoScalingGroupId"),
            ClusterId=json_data.get("ClusterId"),
            DeleteKeepInstance=json_data.get("DeleteKeepInstance"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            EnableAutoScale=json_data.get("EnableAutoScale"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            LaunchConfigId=json_data.get("LaunchConfigId"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Name=json_data.get("Name"),
            NodeCount=json_data.get("NodeCount"),
            NodeOs=json_data.get("NodeOs"),
            NodeOsType=json_data.get("NodeOsType"),
            RetryPolicy=json_data.get("RetryPolicy"),
            ScalingMode=json_data.get("ScalingMode"),
            Status=json_data.get("Status"),
            SubnetIds=json_data.get("SubnetIds"),
            Unschedulable=json_data.get("Unschedulable"),
            VpcId=json_data.get("VpcId"),
            AutoScalingConfig=deserialize_list(json_data.get("AutoScalingConfig"), AutoScalingConfigDefinition),
            NodeConfig=deserialize_list(json_data.get("NodeConfig"), NodeConfigDefinition),
            Taints=deserialize_list(json_data.get("Taints"), TaintsDefinition),
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
class AutoScalingConfigDefinition(BaseModel):
    EnhancedMonitorService: Optional[bool]
    EnhancedSecurityService: Optional[bool]
    InstanceType: Optional[str]
    InternetChargeType: Optional[str]
    InternetMaxBandwidthOut: Optional[float]
    KeyIds: Optional[Sequence[str]]
    Password: Optional[str]
    PublicIpAssigned: Optional[bool]
    SecurityGroupIds: Optional[Sequence[str]]
    SystemDiskSize: Optional[float]
    SystemDiskType: Optional[str]
    DataDisk: Optional[Sequence["_DataDiskDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScalingConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScalingConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            EnhancedMonitorService=json_data.get("EnhancedMonitorService"),
            EnhancedSecurityService=json_data.get("EnhancedSecurityService"),
            InstanceType=json_data.get("InstanceType"),
            InternetChargeType=json_data.get("InternetChargeType"),
            InternetMaxBandwidthOut=json_data.get("InternetMaxBandwidthOut"),
            KeyIds=json_data.get("KeyIds"),
            Password=json_data.get("Password"),
            PublicIpAssigned=json_data.get("PublicIpAssigned"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SystemDiskSize=json_data.get("SystemDiskSize"),
            SystemDiskType=json_data.get("SystemDiskType"),
            DataDisk=deserialize_list(json_data.get("DataDisk"), DataDiskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScalingConfigDefinition = AutoScalingConfigDefinition


@dataclass
class DataDiskDefinition(BaseModel):
    AutoFormatAndMount: Optional[bool]
    DiskSize: Optional[float]
    DiskType: Optional[str]
    FileSystem: Optional[str]
    MountTarget: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoFormatAndMount=json_data.get("AutoFormatAndMount"),
            DiskSize=json_data.get("DiskSize"),
            DiskType=json_data.get("DiskType"),
            FileSystem=json_data.get("FileSystem"),
            MountTarget=json_data.get("MountTarget"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDiskDefinition = DataDiskDefinition


@dataclass
class NodeConfigDefinition(BaseModel):
    DesiredPodNum: Optional[float]
    DockerGraphPath: Optional[str]
    ExtraArgs: Optional[Sequence[str]]
    IsSchedule: Optional[bool]
    MountTarget: Optional[str]
    UserData: Optional[str]
    DataDisk: Optional[Sequence["_DataDiskDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DesiredPodNum=json_data.get("DesiredPodNum"),
            DockerGraphPath=json_data.get("DockerGraphPath"),
            ExtraArgs=json_data.get("ExtraArgs"),
            IsSchedule=json_data.get("IsSchedule"),
            MountTarget=json_data.get("MountTarget"),
            UserData=json_data.get("UserData"),
            DataDisk=deserialize_list(json_data.get("DataDisk"), DataDiskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeConfigDefinition = NodeConfigDefinition


@dataclass
class TaintsDefinition(BaseModel):
    Effect: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaintsDefinition"]:
        if not json_data:
            return None
        return cls(
            Effect=json_data.get("Effect"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaintsDefinition = TaintsDefinition


