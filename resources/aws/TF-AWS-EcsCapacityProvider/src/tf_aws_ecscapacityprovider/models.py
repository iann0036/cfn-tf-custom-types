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
    Arn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    AutoScalingGroupProvider: Optional[Sequence["_AutoScalingGroupProviderDefinition"]]

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
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            AutoScalingGroupProvider=deserialize_list(json_data.get("AutoScalingGroupProvider"), AutoScalingGroupProviderDefinition),
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
class AutoScalingGroupProviderDefinition(BaseModel):
    AutoScalingGroupArn: Optional[str]
    ManagedTerminationProtection: Optional[str]
    ManagedScaling: Optional[Sequence["_ManagedScalingDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScalingGroupProviderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScalingGroupProviderDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoScalingGroupArn=json_data.get("AutoScalingGroupArn"),
            ManagedTerminationProtection=json_data.get("ManagedTerminationProtection"),
            ManagedScaling=deserialize_list(json_data.get("ManagedScaling"), ManagedScalingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScalingGroupProviderDefinition = AutoScalingGroupProviderDefinition


@dataclass
class ManagedScalingDefinition(BaseModel):
    InstanceWarmupPeriod: Optional[float]
    MaximumScalingStepSize: Optional[float]
    MinimumScalingStepSize: Optional[float]
    Status: Optional[str]
    TargetCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedScalingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedScalingDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceWarmupPeriod=json_data.get("InstanceWarmupPeriod"),
            MaximumScalingStepSize=json_data.get("MaximumScalingStepSize"),
            MinimumScalingStepSize=json_data.get("MinimumScalingStepSize"),
            Status=json_data.get("Status"),
            TargetCapacity=json_data.get("TargetCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedScalingDefinition = ManagedScalingDefinition


