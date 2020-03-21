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
    ConfigurationId: Optional[str]
    CreateTime: Optional[str]
    DefaultCooldown: Optional[float]
    DesiredCapacity: Optional[float]
    InstanceCount: Optional[float]
    LoadBalancerIds: Optional[Sequence[str]]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    ProjectId: Optional[float]
    RetryPolicy: Optional[str]
    ScalingGroupName: Optional[str]
    Status: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    TerminationPolicies: Optional[Sequence[str]]
    VpcId: Optional[str]
    Zones: Optional[Sequence[str]]
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
            ConfigurationId=json_data.get("ConfigurationId"),
            CreateTime=json_data.get("CreateTime"),
            DefaultCooldown=json_data.get("DefaultCooldown"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            InstanceCount=json_data.get("InstanceCount"),
            LoadBalancerIds=json_data.get("LoadBalancerIds"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            ProjectId=json_data.get("ProjectId"),
            RetryPolicy=json_data.get("RetryPolicy"),
            ScalingGroupName=json_data.get("ScalingGroupName"),
            Status=json_data.get("Status"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=json_data.get("Tags"),
            TerminationPolicies=json_data.get("TerminationPolicies"),
            VpcId=json_data.get("VpcId"),
            Zones=json_data.get("Zones"),
            ForwardBalancerIds=json_data.get("ForwardBalancerIds"),
            TargetAttribute=json_data.get("TargetAttribute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


