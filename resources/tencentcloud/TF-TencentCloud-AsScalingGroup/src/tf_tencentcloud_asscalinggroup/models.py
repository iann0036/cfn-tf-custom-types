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
    ConfigurationId: Optional[str]
    CreateTime: Optional[str]
    DefaultCooldown: Optional[float]
    DesiredCapacity: Optional[float]
    Id: Optional[str]
    InstanceCount: Optional[float]
    LoadBalancerIds: Optional[Sequence[str]]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    MultiZoneSubnetPolicy: Optional[str]
    ProjectId: Optional[float]
    RetryPolicy: Optional[str]
    ScalingGroupName: Optional[str]
    Status: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TerminationPolicies: Optional[Sequence[str]]
    VpcId: Optional[str]
    Zones: Optional[Sequence[str]]
    ForwardBalancerIds: Optional[Sequence["_ForwardBalancerIdsDefinition"]]

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
            ConfigurationId=json_data.get("ConfigurationId"),
            CreateTime=json_data.get("CreateTime"),
            DefaultCooldown=json_data.get("DefaultCooldown"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            Id=json_data.get("Id"),
            InstanceCount=json_data.get("InstanceCount"),
            LoadBalancerIds=json_data.get("LoadBalancerIds"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            MultiZoneSubnetPolicy=json_data.get("MultiZoneSubnetPolicy"),
            ProjectId=json_data.get("ProjectId"),
            RetryPolicy=json_data.get("RetryPolicy"),
            ScalingGroupName=json_data.get("ScalingGroupName"),
            Status=json_data.get("Status"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TerminationPolicies=json_data.get("TerminationPolicies"),
            VpcId=json_data.get("VpcId"),
            Zones=json_data.get("Zones"),
            ForwardBalancerIds=deserialize_list(json_data.get("ForwardBalancerIds"), ForwardBalancerIdsDefinition),
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


