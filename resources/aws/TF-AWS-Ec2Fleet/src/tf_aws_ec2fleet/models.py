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
    ExcessCapacityTerminationPolicy: Optional[str]
    Id: Optional[str]
    ReplaceUnhealthyInstances: Optional[bool]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    TerminateInstances: Optional[bool]
    TerminateInstancesWithExpiration: Optional[bool]
    Type: Optional[str]
    LaunchTemplateConfig: Optional[Sequence["_LaunchTemplateConfigDefinition"]]
    OnDemandOptions: Optional[Sequence["_OnDemandOptionsDefinition"]]
    SpotOptions: Optional[Sequence["_SpotOptionsDefinition"]]
    TargetCapacitySpecification: Optional[Sequence["_TargetCapacitySpecificationDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            ExcessCapacityTerminationPolicy=json_data.get("ExcessCapacityTerminationPolicy"),
            Id=json_data.get("Id"),
            ReplaceUnhealthyInstances=json_data.get("ReplaceUnhealthyInstances"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            TerminateInstances=json_data.get("TerminateInstances"),
            TerminateInstancesWithExpiration=json_data.get("TerminateInstancesWithExpiration"),
            Type=json_data.get("Type"),
            LaunchTemplateConfig=deserialize_list(json_data.get("LaunchTemplateConfig"), LaunchTemplateConfigDefinition),
            OnDemandOptions=deserialize_list(json_data.get("OnDemandOptions"), OnDemandOptionsDefinition),
            SpotOptions=deserialize_list(json_data.get("SpotOptions"), SpotOptionsDefinition),
            TargetCapacitySpecification=deserialize_list(json_data.get("TargetCapacitySpecification"), TargetCapacitySpecificationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class LaunchTemplateConfigDefinition(BaseModel):
    LaunchTemplateSpecification: Optional[Sequence["_LaunchTemplateSpecificationDefinition"]]
    Override: Optional[Sequence["_OverrideDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateSpecification=deserialize_list(json_data.get("LaunchTemplateSpecification"), LaunchTemplateSpecificationDefinition),
            Override=deserialize_list(json_data.get("Override"), OverrideDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateConfigDefinition = LaunchTemplateConfigDefinition


@dataclass
class LaunchTemplateSpecificationDefinition(BaseModel):
    LaunchTemplateId: Optional[str]
    LaunchTemplateName: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateId=json_data.get("LaunchTemplateId"),
            LaunchTemplateName=json_data.get("LaunchTemplateName"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateSpecificationDefinition = LaunchTemplateSpecificationDefinition


@dataclass
class OverrideDefinition(BaseModel):
    AvailabilityZone: Optional[str]
    InstanceType: Optional[str]
    MaxPrice: Optional[str]
    Priority: Optional[float]
    SubnetId: Optional[str]
    WeightedCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OverrideDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverrideDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            InstanceType=json_data.get("InstanceType"),
            MaxPrice=json_data.get("MaxPrice"),
            Priority=json_data.get("Priority"),
            SubnetId=json_data.get("SubnetId"),
            WeightedCapacity=json_data.get("WeightedCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverrideDefinition = OverrideDefinition


@dataclass
class OnDemandOptionsDefinition(BaseModel):
    AllocationStrategy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnDemandOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnDemandOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            AllocationStrategy=json_data.get("AllocationStrategy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnDemandOptionsDefinition = OnDemandOptionsDefinition


@dataclass
class SpotOptionsDefinition(BaseModel):
    AllocationStrategy: Optional[str]
    InstanceInterruptionBehavior: Optional[str]
    InstancePoolsToUseCount: Optional[float]
    MaintenanceStrategies: Optional[Sequence["_MaintenanceStrategiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpotOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            AllocationStrategy=json_data.get("AllocationStrategy"),
            InstanceInterruptionBehavior=json_data.get("InstanceInterruptionBehavior"),
            InstancePoolsToUseCount=json_data.get("InstancePoolsToUseCount"),
            MaintenanceStrategies=deserialize_list(json_data.get("MaintenanceStrategies"), MaintenanceStrategiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotOptionsDefinition = SpotOptionsDefinition


@dataclass
class MaintenanceStrategiesDefinition(BaseModel):
    CapacityRebalance: Optional[Sequence["_CapacityRebalanceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceStrategiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceStrategiesDefinition"]:
        if not json_data:
            return None
        return cls(
            CapacityRebalance=deserialize_list(json_data.get("CapacityRebalance"), CapacityRebalanceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceStrategiesDefinition = MaintenanceStrategiesDefinition


@dataclass
class CapacityRebalanceDefinition(BaseModel):
    ReplacementStrategy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityRebalanceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityRebalanceDefinition"]:
        if not json_data:
            return None
        return cls(
            ReplacementStrategy=json_data.get("ReplacementStrategy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityRebalanceDefinition = CapacityRebalanceDefinition


@dataclass
class TargetCapacitySpecificationDefinition(BaseModel):
    DefaultTargetCapacityType: Optional[str]
    OnDemandTargetCapacity: Optional[float]
    SpotTargetCapacity: Optional[float]
    TotalTargetCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TargetCapacitySpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetCapacitySpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultTargetCapacityType=json_data.get("DefaultTargetCapacityType"),
            OnDemandTargetCapacity=json_data.get("OnDemandTargetCapacity"),
            SpotTargetCapacity=json_data.get("SpotTargetCapacity"),
            TotalTargetCapacity=json_data.get("TotalTargetCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetCapacitySpecificationDefinition = TargetCapacitySpecificationDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


