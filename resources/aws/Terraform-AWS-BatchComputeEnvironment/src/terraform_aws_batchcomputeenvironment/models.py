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
    Arn: Optional[str]
    ComputeEnvironmentName: Optional[str]
    ComputeEnvironmentNamePrefix: Optional[str]
    EccClusterArn: Optional[str]
    EcsClusterArn: Optional[str]
    Id: Optional[str]
    ServiceRole: Optional[str]
    State: Optional[str]
    Status: Optional[str]
    StatusReason: Optional[str]
    Type: Optional[str]
    ComputeResources: Optional[Sequence["_ComputeResources"]]
    LaunchTemplate: Optional[Sequence["_LaunchTemplate"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            ComputeEnvironmentName=json_data.get("ComputeEnvironmentName"),
            ComputeEnvironmentNamePrefix=json_data.get("ComputeEnvironmentNamePrefix"),
            EccClusterArn=json_data.get("EccClusterArn"),
            EcsClusterArn=json_data.get("EcsClusterArn"),
            Id=json_data.get("Id"),
            ServiceRole=json_data.get("ServiceRole"),
            State=json_data.get("State"),
            Status=json_data.get("Status"),
            StatusReason=json_data.get("StatusReason"),
            Type=json_data.get("Type"),
            ComputeResources=json_data.get("ComputeResources"),
            LaunchTemplate=json_data.get("LaunchTemplate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ComputeResources:
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
    Tags: Optional[Sequence["_Tags"]]
    Type: Optional[str]
    LaunchTemplate: Optional[Sequence["_LaunchTemplate"]]

    @classmethod
    def _deserialize(
        cls: Type["_ComputeResources"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComputeResources"]:
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
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            LaunchTemplate=json_data.get("LaunchTemplate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComputeResources = ComputeResources


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
class LaunchTemplate:
    LaunchTemplateId: Optional[str]
    LaunchTemplateName: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplate"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateId=json_data.get("LaunchTemplateId"),
            LaunchTemplateName=json_data.get("LaunchTemplateName"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplate = LaunchTemplate


