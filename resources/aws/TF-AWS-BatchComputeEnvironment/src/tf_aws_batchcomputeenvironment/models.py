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
    ComputeEnvironmentName: Optional[str]
    ComputeEnvironmentNamePrefix: Optional[str]
    EcsClusterArn: Optional[str]
    Id: Optional[str]
    ServiceRole: Optional[str]
    State: Optional[str]
    Status: Optional[str]
    StatusReason: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Type: Optional[str]
    ComputeResources: Optional[Sequence["_ComputeResourcesDefinition"]]

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
            ComputeEnvironmentName=json_data.get("ComputeEnvironmentName"),
            ComputeEnvironmentNamePrefix=json_data.get("ComputeEnvironmentNamePrefix"),
            EcsClusterArn=json_data.get("EcsClusterArn"),
            Id=json_data.get("Id"),
            ServiceRole=json_data.get("ServiceRole"),
            State=json_data.get("State"),
            Status=json_data.get("Status"),
            StatusReason=json_data.get("StatusReason"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Type=json_data.get("Type"),
            ComputeResources=deserialize_list(json_data.get("ComputeResources"), ComputeResourcesDefinition),
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
class ComputeResourcesDefinition(BaseModel):
    AllocationStrategy: Optional[str]
    BidPercentage: Optional[float]
    DesiredVcpus: Optional[float]
    Ec2KeyPair: Optional[str]
    ImageId: Optional[str]
    InstanceRole: Optional[str]
    InstanceType: Optional[Sequence[str]]
    MaxVcpus: Optional[float]
    MinVcpus: Optional[float]
    SecurityGroupIds: Optional[Sequence[str]]
    SpotIamFleetRole: Optional[str]
    Subnets: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition2"]]
    Type: Optional[str]
    LaunchTemplate: Optional[Sequence["_LaunchTemplateDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ComputeResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComputeResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            AllocationStrategy=json_data.get("AllocationStrategy"),
            BidPercentage=json_data.get("BidPercentage"),
            DesiredVcpus=json_data.get("DesiredVcpus"),
            Ec2KeyPair=json_data.get("Ec2KeyPair"),
            ImageId=json_data.get("ImageId"),
            InstanceRole=json_data.get("InstanceRole"),
            InstanceType=json_data.get("InstanceType"),
            MaxVcpus=json_data.get("MaxVcpus"),
            MinVcpus=json_data.get("MinVcpus"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SpotIamFleetRole=json_data.get("SpotIamFleetRole"),
            Subnets=json_data.get("Subnets"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition2),
            Type=json_data.get("Type"),
            LaunchTemplate=deserialize_list(json_data.get("LaunchTemplate"), LaunchTemplateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComputeResourcesDefinition = ComputeResourcesDefinition


@dataclass
class TagsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition2 = TagsDefinition2


@dataclass
class LaunchTemplateDefinition(BaseModel):
    LaunchTemplateId: Optional[str]
    LaunchTemplateName: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateId=json_data.get("LaunchTemplateId"),
            LaunchTemplateName=json_data.get("LaunchTemplateName"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateDefinition = LaunchTemplateDefinition


