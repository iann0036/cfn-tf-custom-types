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
    AutoProvisioningGroupName: Optional[str]
    AutoProvisioningGroupType: Optional[str]
    DefaultTargetCapacityType: Optional[str]
    Description: Optional[str]
    ExcessCapacityTerminationPolicy: Optional[str]
    Id: Optional[str]
    LaunchTemplateId: Optional[str]
    LaunchTemplateVersion: Optional[str]
    MaxSpotPrice: Optional[float]
    PayAsYouGoAllocationStrategy: Optional[str]
    PayAsYouGoTargetCapacity: Optional[str]
    SpotAllocationStrategy: Optional[str]
    SpotInstanceInterruptionBehavior: Optional[str]
    SpotInstancePoolsToUseCount: Optional[float]
    SpotTargetCapacity: Optional[str]
    TerminateInstances: Optional[bool]
    TerminateInstancesWithExpiration: Optional[bool]
    TotalTargetCapacity: Optional[str]
    ValidFrom: Optional[str]
    ValidUntil: Optional[str]
    LaunchTemplateConfig: Optional[Sequence["_LaunchTemplateConfigDefinition"]]

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
            AutoProvisioningGroupName=json_data.get("AutoProvisioningGroupName"),
            AutoProvisioningGroupType=json_data.get("AutoProvisioningGroupType"),
            DefaultTargetCapacityType=json_data.get("DefaultTargetCapacityType"),
            Description=json_data.get("Description"),
            ExcessCapacityTerminationPolicy=json_data.get("ExcessCapacityTerminationPolicy"),
            Id=json_data.get("Id"),
            LaunchTemplateId=json_data.get("LaunchTemplateId"),
            LaunchTemplateVersion=json_data.get("LaunchTemplateVersion"),
            MaxSpotPrice=json_data.get("MaxSpotPrice"),
            PayAsYouGoAllocationStrategy=json_data.get("PayAsYouGoAllocationStrategy"),
            PayAsYouGoTargetCapacity=json_data.get("PayAsYouGoTargetCapacity"),
            SpotAllocationStrategy=json_data.get("SpotAllocationStrategy"),
            SpotInstanceInterruptionBehavior=json_data.get("SpotInstanceInterruptionBehavior"),
            SpotInstancePoolsToUseCount=json_data.get("SpotInstancePoolsToUseCount"),
            SpotTargetCapacity=json_data.get("SpotTargetCapacity"),
            TerminateInstances=json_data.get("TerminateInstances"),
            TerminateInstancesWithExpiration=json_data.get("TerminateInstancesWithExpiration"),
            TotalTargetCapacity=json_data.get("TotalTargetCapacity"),
            ValidFrom=json_data.get("ValidFrom"),
            ValidUntil=json_data.get("ValidUntil"),
            LaunchTemplateConfig=deserialize_list(json_data.get("LaunchTemplateConfig"), LaunchTemplateConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LaunchTemplateConfigDefinition(BaseModel):
    InstanceType: Optional[str]
    MaxPrice: Optional[str]
    Priority: Optional[str]
    VswitchId: Optional[str]
    WeightedCapacity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceType=json_data.get("InstanceType"),
            MaxPrice=json_data.get("MaxPrice"),
            Priority=json_data.get("Priority"),
            VswitchId=json_data.get("VswitchId"),
            WeightedCapacity=json_data.get("WeightedCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateConfigDefinition = LaunchTemplateConfigDefinition


