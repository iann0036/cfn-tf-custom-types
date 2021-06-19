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
    ExtraArgs: Optional[Sequence[str]]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Unschedulable: Optional[float]
    AutoScalingConfig: Optional[Sequence["_AutoScalingConfigDefinition"]]
    AutoScalingGroup: Optional[Sequence["_AutoScalingGroupDefinition"]]

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
            ExtraArgs=json_data.get("ExtraArgs"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Unschedulable=json_data.get("Unschedulable"),
            AutoScalingConfig=deserialize_list(json_data.get("AutoScalingConfig"), AutoScalingConfigDefinition),
            AutoScalingGroup=deserialize_list(json_data.get("AutoScalingGroup"), AutoScalingGroupDefinition),
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
    ConfigurationName: Optional[str]
    EnhancedMonitorService: Optional[bool]
    EnhancedSecurityService: Optional[bool]
    InstanceTags: Optional[Sequence["_InstanceTagsDefinition"]]
    InstanceType: Optional[str]
    InternetChargeType: Optional[str]
    InternetMaxBandwidthOut: Optional[float]
    KeyIds: Optional[Sequence[str]]
    Password: Optional[str]
    ProjectId: Optional[float]
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
            ConfigurationName=json_data.get("ConfigurationName"),
            EnhancedMonitorService=json_data.get("EnhancedMonitorService"),
            EnhancedSecurityService=json_data.get("EnhancedSecurityService"),
            InstanceTags=deserialize_list(json_data.get("InstanceTags"), InstanceTagsDefinition),
            InstanceType=json_data.get("InstanceType"),
            InternetChargeType=json_data.get("InternetChargeType"),
            InternetMaxBandwidthOut=json_data.get("InternetMaxBandwidthOut"),
            KeyIds=json_data.get("KeyIds"),
            Password=json_data.get("Password"),
            ProjectId=json_data.get("ProjectId"),
            PublicIpAssigned=json_data.get("PublicIpAssigned"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SystemDiskSize=json_data.get("SystemDiskSize"),
            SystemDiskType=json_data.get("SystemDiskType"),
            DataDisk=deserialize_list(json_data.get("DataDisk"), DataDiskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScalingConfigDefinition = AutoScalingConfigDefinition


@dataclass
class InstanceTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceTagsDefinition = InstanceTagsDefinition


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
class AutoScalingGroupDefinition(BaseModel):
    DefaultCooldown: Optional[float]
    DesiredCapacity: Optional[float]
    LoadBalancerIds: Optional[Sequence[str]]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    ProjectId: Optional[float]
    RetryPolicy: Optional[str]
    ScalingGroupName: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TerminationPolicies: Optional[Sequence[str]]
    VpcId: Optional[str]
    Zones: Optional[Sequence[str]]
    ForwardBalancerIds: Optional[Sequence["_ForwardBalancerIdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScalingGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScalingGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultCooldown=json_data.get("DefaultCooldown"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            LoadBalancerIds=json_data.get("LoadBalancerIds"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            ProjectId=json_data.get("ProjectId"),
            RetryPolicy=json_data.get("RetryPolicy"),
            ScalingGroupName=json_data.get("ScalingGroupName"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TerminationPolicies=json_data.get("TerminationPolicies"),
            VpcId=json_data.get("VpcId"),
            Zones=json_data.get("Zones"),
            ForwardBalancerIds=deserialize_list(json_data.get("ForwardBalancerIds"), ForwardBalancerIdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScalingGroupDefinition = AutoScalingGroupDefinition


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
class ForwardBalancerIdsDefinition(BaseModel):
    ListenerId: Optional[str]
    LoadBalancerId: Optional[str]
    RuleId: Optional[str]
    TargetAttribute: Optional[Sequence["_TargetAttributeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardBalancerIdsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardBalancerIdsDefinition"]:
        if not json_data:
            return None
        return cls(
            ListenerId=json_data.get("ListenerId"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            RuleId=json_data.get("RuleId"),
            TargetAttribute=deserialize_list(json_data.get("TargetAttribute"), TargetAttributeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardBalancerIdsDefinition = ForwardBalancerIdsDefinition


@dataclass
class TargetAttributeDefinition(BaseModel):
    Port: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TargetAttributeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetAttributeDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetAttributeDefinition = TargetAttributeDefinition


