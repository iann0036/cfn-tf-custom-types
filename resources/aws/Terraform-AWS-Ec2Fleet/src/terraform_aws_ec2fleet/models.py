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
    ExcessCapacityTerminationPolicy: Optional[str]
    Id: Optional[str]
    ReplaceUnhealthyInstances: Optional[bool]
    Tags: Optional[Sequence["_Tags"]]
    TerminateInstances: Optional[bool]
    TerminateInstancesWithExpiration: Optional[bool]
    Type: Optional[str]
    LaunchTemplateConfig: Optional[Sequence["_LaunchTemplateConfig"]]
    OnDemandOptions: Optional[Sequence["_OnDemandOptions"]]
    SpotOptions: Optional[Sequence["_SpotOptions"]]
    TargetCapacitySpecification: Optional[Sequence["_TargetCapacitySpecification"]]
    Timeouts: Optional["_Timeouts"]
    LaunchTemplateSpecification: Optional[Sequence["_LaunchTemplateSpecification"]]
    Override: Optional[Sequence["_Override"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ExcessCapacityTerminationPolicy=json_data.get("ExcessCapacityTerminationPolicy"),
            Id=json_data.get("Id"),
            ReplaceUnhealthyInstances=json_data.get("ReplaceUnhealthyInstances"),
            Tags=json_data.get("Tags"),
            TerminateInstances=json_data.get("TerminateInstances"),
            TerminateInstancesWithExpiration=json_data.get("TerminateInstancesWithExpiration"),
            Type=json_data.get("Type"),
            LaunchTemplateConfig=json_data.get("LaunchTemplateConfig"),
            OnDemandOptions=json_data.get("OnDemandOptions"),
            SpotOptions=json_data.get("SpotOptions"),
            TargetCapacitySpecification=json_data.get("TargetCapacitySpecification"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            LaunchTemplateSpecification=json_data.get("LaunchTemplateSpecification"),
            Override=json_data.get("Override"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class LaunchTemplateConfig:
    LaunchTemplateSpecification: Optional[Sequence["_LaunchTemplateSpecification"]]
    Override: Optional[Sequence["_Override"]]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateConfig"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateSpecification=json_data.get("LaunchTemplateSpecification"),
            Override=json_data.get("Override"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateConfig = LaunchTemplateConfig


@dataclass
class LaunchTemplateSpecification:
    LaunchTemplateId: Optional[str]
    LaunchTemplateName: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateSpecification"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateId=json_data.get("LaunchTemplateId"),
            LaunchTemplateName=json_data.get("LaunchTemplateName"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateSpecification = LaunchTemplateSpecification


@dataclass
class Override:
    AvailabilityZone: Optional[str]
    InstanceType: Optional[str]
    MaxPrice: Optional[str]
    Priority: Optional[float]
    SubnetId: Optional[str]
    WeightedCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Override"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Override"]:
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
_Override = Override


@dataclass
class OnDemandOptions:
    AllocationStrategy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnDemandOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnDemandOptions"]:
        if not json_data:
            return None
        return cls(
            AllocationStrategy=json_data.get("AllocationStrategy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnDemandOptions = OnDemandOptions


@dataclass
class SpotOptions:
    AllocationStrategy: Optional[str]
    InstanceInterruptionBehavior: Optional[str]
    InstancePoolsToUseCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SpotOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotOptions"]:
        if not json_data:
            return None
        return cls(
            AllocationStrategy=json_data.get("AllocationStrategy"),
            InstanceInterruptionBehavior=json_data.get("InstanceInterruptionBehavior"),
            InstancePoolsToUseCount=json_data.get("InstancePoolsToUseCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotOptions = SpotOptions


@dataclass
class TargetCapacitySpecification:
    DefaultTargetCapacityType: Optional[str]
    OnDemandTargetCapacity: Optional[float]
    SpotTargetCapacity: Optional[float]
    TotalTargetCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TargetCapacitySpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetCapacitySpecification"]:
        if not json_data:
            return None
        return cls(
            DefaultTargetCapacityType=json_data.get("DefaultTargetCapacityType"),
            OnDemandTargetCapacity=json_data.get("OnDemandTargetCapacity"),
            SpotTargetCapacity=json_data.get("SpotTargetCapacity"),
            TotalTargetCapacity=json_data.get("TotalTargetCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetCapacitySpecification = TargetCapacitySpecification


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


