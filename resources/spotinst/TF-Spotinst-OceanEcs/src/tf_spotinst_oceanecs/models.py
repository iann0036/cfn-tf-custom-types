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
    AssociatePublicIpAddress: Optional[bool]
    ClusterName: Optional[str]
    DesiredCapacity: Optional[float]
    DrainingTimeout: Optional[float]
    EbsOptimized: Optional[bool]
    IamInstanceProfile: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    KeyPair: Optional[str]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Monitoring: Optional[bool]
    Name: Optional[str]
    Region: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]
    UserData: Optional[str]
    UtilizeCommitments: Optional[bool]
    UtilizeReservedInstances: Optional[bool]
    Whitelist: Optional[Sequence[str]]
    Autoscaler: Optional[Sequence["_AutoscalerDefinition"]]
    BlockDeviceMappings: Optional[Sequence["_BlockDeviceMappingsDefinition"]]
    OptimizeImages: Optional[Sequence["_OptimizeImagesDefinition"]]
    ScheduledTask: Optional[Sequence["_ScheduledTaskDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    UpdatePolicy: Optional[Sequence["_UpdatePolicyDefinition"]]

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
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            ClusterName=json_data.get("ClusterName"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            DrainingTimeout=json_data.get("DrainingTimeout"),
            EbsOptimized=json_data.get("EbsOptimized"),
            IamInstanceProfile=json_data.get("IamInstanceProfile"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            KeyPair=json_data.get("KeyPair"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Monitoring=json_data.get("Monitoring"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
            UserData=json_data.get("UserData"),
            UtilizeCommitments=json_data.get("UtilizeCommitments"),
            UtilizeReservedInstances=json_data.get("UtilizeReservedInstances"),
            Whitelist=json_data.get("Whitelist"),
            Autoscaler=deserialize_list(json_data.get("Autoscaler"), AutoscalerDefinition),
            BlockDeviceMappings=deserialize_list(json_data.get("BlockDeviceMappings"), BlockDeviceMappingsDefinition),
            OptimizeImages=deserialize_list(json_data.get("OptimizeImages"), OptimizeImagesDefinition),
            ScheduledTask=deserialize_list(json_data.get("ScheduledTask"), ScheduledTaskDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            UpdatePolicy=deserialize_list(json_data.get("UpdatePolicy"), UpdatePolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutoscalerDefinition(BaseModel):
    Cooldown: Optional[float]
    IsAutoConfig: Optional[bool]
    IsEnabled: Optional[bool]
    Down: Optional[Sequence["_DownDefinition"]]
    Headroom: Optional[Sequence["_HeadroomDefinition"]]
    ResourceLimits: Optional[Sequence["_ResourceLimitsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscalerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscalerDefinition"]:
        if not json_data:
            return None
        return cls(
            Cooldown=json_data.get("Cooldown"),
            IsAutoConfig=json_data.get("IsAutoConfig"),
            IsEnabled=json_data.get("IsEnabled"),
            Down=deserialize_list(json_data.get("Down"), DownDefinition),
            Headroom=deserialize_list(json_data.get("Headroom"), HeadroomDefinition),
            ResourceLimits=deserialize_list(json_data.get("ResourceLimits"), ResourceLimitsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscalerDefinition = AutoscalerDefinition


@dataclass
class DownDefinition(BaseModel):
    MaxScaleDownPercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DownDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DownDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxScaleDownPercentage=json_data.get("MaxScaleDownPercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DownDefinition = DownDefinition


@dataclass
class HeadroomDefinition(BaseModel):
    CpuPerUnit: Optional[float]
    MemoryPerUnit: Optional[float]
    NumOfUnits: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HeadroomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadroomDefinition"]:
        if not json_data:
            return None
        return cls(
            CpuPerUnit=json_data.get("CpuPerUnit"),
            MemoryPerUnit=json_data.get("MemoryPerUnit"),
            NumOfUnits=json_data.get("NumOfUnits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadroomDefinition = HeadroomDefinition


@dataclass
class ResourceLimitsDefinition(BaseModel):
    MaxMemoryGib: Optional[float]
    MaxVcpu: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxMemoryGib=json_data.get("MaxMemoryGib"),
            MaxVcpu=json_data.get("MaxVcpu"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceLimitsDefinition = ResourceLimitsDefinition


@dataclass
class BlockDeviceMappingsDefinition(BaseModel):
    DeviceName: Optional[str]
    NoDevice: Optional[str]
    VirtualName: Optional[str]
    Ebs: Optional[Sequence["_EbsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BlockDeviceMappingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockDeviceMappingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            NoDevice=json_data.get("NoDevice"),
            VirtualName=json_data.get("VirtualName"),
            Ebs=deserialize_list(json_data.get("Ebs"), EbsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockDeviceMappingsDefinition = BlockDeviceMappingsDefinition


@dataclass
class EbsDefinition(BaseModel):
    DeleteOnTermination: Optional[bool]
    Encrypted: Optional[bool]
    Iops: Optional[float]
    KmsKeyId: Optional[str]
    SnapshotId: Optional[str]
    Throughput: Optional[float]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]
    DynamicVolumeSize: Optional[Sequence["_DynamicVolumeSizeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EbsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SnapshotId=json_data.get("SnapshotId"),
            Throughput=json_data.get("Throughput"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
            DynamicVolumeSize=deserialize_list(json_data.get("DynamicVolumeSize"), DynamicVolumeSizeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsDefinition = EbsDefinition


@dataclass
class DynamicVolumeSizeDefinition(BaseModel):
    BaseSize: Optional[float]
    Resource: Optional[str]
    SizePerResourceUnit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicVolumeSizeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicVolumeSizeDefinition"]:
        if not json_data:
            return None
        return cls(
            BaseSize=json_data.get("BaseSize"),
            Resource=json_data.get("Resource"),
            SizePerResourceUnit=json_data.get("SizePerResourceUnit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicVolumeSizeDefinition = DynamicVolumeSizeDefinition


@dataclass
class OptimizeImagesDefinition(BaseModel):
    PerformAt: Optional[str]
    ShouldOptimizeEcsAmi: Optional[bool]
    TimeWindows: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_OptimizeImagesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptimizeImagesDefinition"]:
        if not json_data:
            return None
        return cls(
            PerformAt=json_data.get("PerformAt"),
            ShouldOptimizeEcsAmi=json_data.get("ShouldOptimizeEcsAmi"),
            TimeWindows=json_data.get("TimeWindows"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptimizeImagesDefinition = OptimizeImagesDefinition


@dataclass
class ScheduledTaskDefinition(BaseModel):
    ShutdownHours: Optional[Sequence["_ShutdownHoursDefinition"]]
    Tasks: Optional[Sequence["_TasksDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduledTaskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledTaskDefinition"]:
        if not json_data:
            return None
        return cls(
            ShutdownHours=deserialize_list(json_data.get("ShutdownHours"), ShutdownHoursDefinition),
            Tasks=deserialize_list(json_data.get("Tasks"), TasksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledTaskDefinition = ScheduledTaskDefinition


@dataclass
class ShutdownHoursDefinition(BaseModel):
    IsEnabled: Optional[bool]
    TimeWindows: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ShutdownHoursDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShutdownHoursDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            TimeWindows=json_data.get("TimeWindows"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShutdownHoursDefinition = ShutdownHoursDefinition


@dataclass
class TasksDefinition(BaseModel):
    CronExpression: Optional[str]
    IsEnabled: Optional[bool]
    TaskType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TasksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TasksDefinition"]:
        if not json_data:
            return None
        return cls(
            CronExpression=json_data.get("CronExpression"),
            IsEnabled=json_data.get("IsEnabled"),
            TaskType=json_data.get("TaskType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TasksDefinition = TasksDefinition


@dataclass
class TagsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class UpdatePolicyDefinition(BaseModel):
    ShouldRoll: Optional[bool]
    RollConfig: Optional[Sequence["_RollConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UpdatePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpdatePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            ShouldRoll=json_data.get("ShouldRoll"),
            RollConfig=deserialize_list(json_data.get("RollConfig"), RollConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpdatePolicyDefinition = UpdatePolicyDefinition


@dataclass
class RollConfigDefinition(BaseModel):
    BatchSizePercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RollConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RollConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BatchSizePercentage=json_data.get("BatchSizePercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RollConfigDefinition = RollConfigDefinition


