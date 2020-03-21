# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    ClusterId: Optional[str]
    AutoScalingConfig: Optional[Sequence["_AutoScalingConfig"]]
    AutoScalingGroup: Optional[Sequence["_AutoScalingGroup"]]
    DataDisk: Optional[Sequence["_DataDisk"]]
    ForwardBalancerIds: Optional[Sequence["_ForwardBalancerIds"]]
    TargetAttribute: Optional[Sequence["_TargetAttribute"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ClusterId=json_data.get("ClusterId"),
            AutoScalingConfig=json_data.get("AutoScalingConfig"),
            AutoScalingGroup=json_data.get("AutoScalingGroup"),
            DataDisk=json_data.get("DataDisk"),
            ForwardBalancerIds=json_data.get("ForwardBalancerIds"),
            TargetAttribute=json_data.get("TargetAttribute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutoScalingConfig:
    ConfigurationName: Optional[str]
    EnhancedMonitorService: Optional[bool]
    EnhancedSecurityService: Optional[bool]
    InstanceTags: Optional[Sequence["_InstanceTags"]]
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
    DataDisk: Optional[Sequence["_DataDisk"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScalingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScalingConfig"]:
        if not json_data:
            return None
        return cls(
            ConfigurationName=json_data.get("ConfigurationName"),
            EnhancedMonitorService=json_data.get("EnhancedMonitorService"),
            EnhancedSecurityService=json_data.get("EnhancedSecurityService"),
            InstanceTags=json_data.get("InstanceTags"),
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
            DataDisk=json_data.get("DataDisk"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScalingConfig = AutoScalingConfig


@dataclass
class InstanceTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceTags = InstanceTags


@dataclass
class DataDisk:
    DiskSize: Optional[float]
    DiskType: Optional[str]
    SnapshotId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDisk"]:
        if not json_data:
            return None
        return cls(
            DiskSize=json_data.get("DiskSize"),
            DiskType=json_data.get("DiskType"),
            SnapshotId=json_data.get("SnapshotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDisk = DataDisk


@dataclass
class AutoScalingGroup:
    DefaultCooldown: Optional[float]
    DesiredCapacity: Optional[float]
    LoadBalancerIds: Optional[Sequence[str]]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    ProjectId: Optional[float]
    RetryPolicy: Optional[str]
    ScalingGroupName: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    TerminationPolicies: Optional[Sequence[str]]
    VpcId: Optional[str]
    Zones: Optional[Sequence[str]]
    ForwardBalancerIds: Optional[Sequence["_ForwardBalancerIds"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScalingGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScalingGroup"]:
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
            Tags=json_data.get("Tags"),
            TerminationPolicies=json_data.get("TerminationPolicies"),
            VpcId=json_data.get("VpcId"),
            Zones=json_data.get("Zones"),
            ForwardBalancerIds=json_data.get("ForwardBalancerIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScalingGroup = AutoScalingGroup


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class ForwardBalancerIds:
    ListenerId: Optional[str]
    LoadBalancerId: Optional[str]
    RuleId: Optional[str]
    TargetAttribute: Optional[Sequence["_TargetAttribute"]]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardBalancerIds"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardBalancerIds"]:
        if not json_data:
            return None
        return cls(
            ListenerId=json_data.get("ListenerId"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            RuleId=json_data.get("RuleId"),
            TargetAttribute=json_data.get("TargetAttribute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardBalancerIds = ForwardBalancerIds


@dataclass
class TargetAttribute:
    Port: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TargetAttribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetAttribute"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetAttribute = TargetAttribute


