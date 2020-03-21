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
    ClusterName: Optional[str]
    DesiredCapacity: Optional[float]
    DrainingTimeout: Optional[float]
    EbsOptimized: Optional[bool]
    IamInstanceProfile: Optional[str]
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
    UtilizeReservedInstances: Optional[bool]
    Whitelist: Optional[Sequence[str]]
    Autoscaler: Optional[Sequence["_Autoscaler"]]
    Tags: Optional[Sequence["_Tags"]]
    UpdatePolicy: Optional[Sequence["_UpdatePolicy"]]
    Down: Optional[Sequence["_Down"]]
    Headroom: Optional[Sequence["_Headroom"]]
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
            ClusterName=json_data.get("ClusterName"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            DrainingTimeout=json_data.get("DrainingTimeout"),
            EbsOptimized=json_data.get("EbsOptimized"),
            IamInstanceProfile=json_data.get("IamInstanceProfile"),
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
            UtilizeReservedInstances=json_data.get("UtilizeReservedInstances"),
            Whitelist=json_data.get("Whitelist"),
            Autoscaler=json_data.get("Autoscaler"),
            Tags=json_data.get("Tags"),
            UpdatePolicy=json_data.get("UpdatePolicy"),
            Down=json_data.get("Down"),
            Headroom=json_data.get("Headroom"),
            ResourceLimits=json_data.get("ResourceLimits"),
            RollConfig=json_data.get("RollConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Autoscaler:
    Cooldown: Optional[float]
    IsAutoConfig: Optional[bool]
    IsEnabled: Optional[bool]
    Down: Optional[Sequence["_Down"]]
    Headroom: Optional[Sequence["_Headroom"]]
    ResourceLimits: Optional[Sequence["_ResourceLimits"]]

    @classmethod
    def _deserialize(
        cls: Type["_Autoscaler"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Autoscaler"]:
        if not json_data:
            return None
        return cls(
            Cooldown=json_data.get("Cooldown"),
            IsAutoConfig=json_data.get("IsAutoConfig"),
            IsEnabled=json_data.get("IsEnabled"),
            Down=json_data.get("Down"),
            Headroom=json_data.get("Headroom"),
            ResourceLimits=json_data.get("ResourceLimits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Autoscaler = Autoscaler


@dataclass
class Down:
    MaxScaleDownPercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Down"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Down"]:
        if not json_data:
            return None
        return cls(
            MaxScaleDownPercentage=json_data.get("MaxScaleDownPercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Down = Down


@dataclass
class Headroom:
    CpuPerUnit: Optional[float]
    MemoryPerUnit: Optional[float]
    NumOfUnits: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Headroom"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headroom"]:
        if not json_data:
            return None
        return cls(
            CpuPerUnit=json_data.get("CpuPerUnit"),
            MemoryPerUnit=json_data.get("MemoryPerUnit"),
            NumOfUnits=json_data.get("NumOfUnits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headroom = Headroom


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


