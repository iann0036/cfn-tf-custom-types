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
    AssociatePublicIpAddress: Optional[bool]
    Blacklist: Optional[Sequence[str]]
    ControllerId: Optional[str]
    DesiredCapacity: Optional[float]
    DrainingTimeout: Optional[float]
    EbsOptimized: Optional[bool]
    FallbackToOndemand: Optional[bool]
    IamInstanceProfile: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    KeyName: Optional[str]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Monitoring: Optional[bool]
    Name: Optional[str]
    Region: Optional[str]
    RootVolumeSize: Optional[float]
    SecurityGroups: Optional[Sequence[str]]
    SpotPercentage: Optional[float]
    SubnetIds: Optional[Sequence[str]]
    UserData: Optional[str]
    UtilizeReservedInstances: Optional[bool]
    Whitelist: Optional[Sequence[str]]
    Autoscaler: Optional[Sequence["_Autoscaler"]]
    LoadBalancers: Optional[Sequence["_LoadBalancers"]]
    Tags: Optional[Sequence["_Tags"]]
    UpdatePolicy: Optional[Sequence["_UpdatePolicy"]]
    AutoscaleDown: Optional[Sequence["_AutoscaleDown"]]
    AutoscaleHeadroom: Optional[Sequence["_AutoscaleHeadroom"]]
    ResourceLimits: Optional[Sequence["_ResourceLimits"]]
    RollConfig: Optional[Sequence["_RollConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            Blacklist=json_data.get("Blacklist"),
            ControllerId=json_data.get("ControllerId"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            DrainingTimeout=json_data.get("DrainingTimeout"),
            EbsOptimized=json_data.get("EbsOptimized"),
            FallbackToOndemand=json_data.get("FallbackToOndemand"),
            IamInstanceProfile=json_data.get("IamInstanceProfile"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            KeyName=json_data.get("KeyName"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Monitoring=json_data.get("Monitoring"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            RootVolumeSize=json_data.get("RootVolumeSize"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SpotPercentage=json_data.get("SpotPercentage"),
            SubnetIds=json_data.get("SubnetIds"),
            UserData=json_data.get("UserData"),
            UtilizeReservedInstances=json_data.get("UtilizeReservedInstances"),
            Whitelist=json_data.get("Whitelist"),
            Autoscaler=json_data.get("Autoscaler"),
            LoadBalancers=json_data.get("LoadBalancers"),
            Tags=json_data.get("Tags"),
            UpdatePolicy=json_data.get("UpdatePolicy"),
            AutoscaleDown=json_data.get("AutoscaleDown"),
            AutoscaleHeadroom=json_data.get("AutoscaleHeadroom"),
            ResourceLimits=json_data.get("ResourceLimits"),
            RollConfig=json_data.get("RollConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Autoscaler:
    AutoscaleCooldown: Optional[float]
    AutoscaleIsAutoConfig: Optional[bool]
    AutoscaleIsEnabled: Optional[bool]
    AutoscaleDown: Optional[Sequence["_AutoscaleDown"]]
    AutoscaleHeadroom: Optional[Sequence["_AutoscaleHeadroom"]]
    ResourceLimits: Optional[Sequence["_ResourceLimits"]]

    @classmethod
    def _deserialize(
        cls: Type["_Autoscaler"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Autoscaler"]:
        if not json_data:
            return None
        return cls(
            AutoscaleCooldown=json_data.get("AutoscaleCooldown"),
            AutoscaleIsAutoConfig=json_data.get("AutoscaleIsAutoConfig"),
            AutoscaleIsEnabled=json_data.get("AutoscaleIsEnabled"),
            AutoscaleDown=json_data.get("AutoscaleDown"),
            AutoscaleHeadroom=json_data.get("AutoscaleHeadroom"),
            ResourceLimits=json_data.get("ResourceLimits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Autoscaler = Autoscaler


@dataclass
class AutoscaleDown:
    EvaluationPeriods: Optional[float]
    MaxScaleDownPercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleDown"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleDown"]:
        if not json_data:
            return None
        return cls(
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
            MaxScaleDownPercentage=json_data.get("MaxScaleDownPercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleDown = AutoscaleDown


@dataclass
class AutoscaleHeadroom:
    CpuPerUnit: Optional[float]
    GpuPerUnit: Optional[float]
    MemoryPerUnit: Optional[float]
    NumOfUnits: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleHeadroom"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleHeadroom"]:
        if not json_data:
            return None
        return cls(
            CpuPerUnit=json_data.get("CpuPerUnit"),
            GpuPerUnit=json_data.get("GpuPerUnit"),
            MemoryPerUnit=json_data.get("MemoryPerUnit"),
            NumOfUnits=json_data.get("NumOfUnits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleHeadroom = AutoscaleHeadroom


@dataclass
class ResourceLimits:
    MaxMemoryGib: Optional[float]
    MaxVcpu: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceLimits"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceLimits"]:
        if not json_data:
            return None
        return cls(
            MaxMemoryGib=json_data.get("MaxMemoryGib"),
            MaxVcpu=json_data.get("MaxVcpu"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceLimits = ResourceLimits


@dataclass
class LoadBalancers:
    Arn: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancers"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancers = LoadBalancers


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
class UpdatePolicy:
    ShouldRoll: Optional[bool]
    RollConfig: Optional[Sequence["_RollConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_UpdatePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpdatePolicy"]:
        if not json_data:
            return None
        return cls(
            ShouldRoll=json_data.get("ShouldRoll"),
            RollConfig=json_data.get("RollConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpdatePolicy = UpdatePolicy


@dataclass
class RollConfig:
    BatchSizePercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RollConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RollConfig"]:
        if not json_data:
            return None
        return cls(
            BatchSizePercentage=json_data.get("BatchSizePercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RollConfig = RollConfig


