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
    AllocationStrategy: Optional[str]
    ClientToken: Optional[str]
    ExcessCapacityTerminationPolicy: Optional[str]
    FleetType: Optional[str]
    IamFleetRole: Optional[str]
    Id: Optional[str]
    InstanceInterruptionBehaviour: Optional[str]
    InstancePoolsToUseCount: Optional[float]
    LoadBalancers: Optional[Sequence[str]]
    ReplaceUnhealthyInstances: Optional[bool]
    SpotPrice: Optional[str]
    SpotRequestState: Optional[str]
    TargetCapacity: Optional[float]
    TargetGroupArns: Optional[Sequence[str]]
    TerminateInstancesWithExpiration: Optional[bool]
    ValidFrom: Optional[str]
    ValidUntil: Optional[str]
    WaitForFulfillment: Optional[bool]
    LaunchSpecification: Optional[Sequence["_LaunchSpecification"]]
    Timeouts: Optional["_Timeouts"]
    EbsBlockDevice: Optional[Sequence["_EbsBlockDevice"]]
    EphemeralBlockDevice: Optional[Sequence["_EphemeralBlockDevice"]]
    RootBlockDevice: Optional[Sequence["_RootBlockDevice"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllocationStrategy=json_data.get("AllocationStrategy"),
            ClientToken=json_data.get("ClientToken"),
            ExcessCapacityTerminationPolicy=json_data.get("ExcessCapacityTerminationPolicy"),
            FleetType=json_data.get("FleetType"),
            IamFleetRole=json_data.get("IamFleetRole"),
            Id=json_data.get("Id"),
            InstanceInterruptionBehaviour=json_data.get("InstanceInterruptionBehaviour"),
            InstancePoolsToUseCount=json_data.get("InstancePoolsToUseCount"),
            LoadBalancers=json_data.get("LoadBalancers"),
            ReplaceUnhealthyInstances=json_data.get("ReplaceUnhealthyInstances"),
            SpotPrice=json_data.get("SpotPrice"),
            SpotRequestState=json_data.get("SpotRequestState"),
            TargetCapacity=json_data.get("TargetCapacity"),
            TargetGroupArns=json_data.get("TargetGroupArns"),
            TerminateInstancesWithExpiration=json_data.get("TerminateInstancesWithExpiration"),
            ValidFrom=json_data.get("ValidFrom"),
            ValidUntil=json_data.get("ValidUntil"),
            WaitForFulfillment=json_data.get("WaitForFulfillment"),
            LaunchSpecification=json_data.get("LaunchSpecification"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            EbsBlockDevice=json_data.get("EbsBlockDevice"),
            EphemeralBlockDevice=json_data.get("EphemeralBlockDevice"),
            RootBlockDevice=json_data.get("RootBlockDevice"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LaunchSpecification:
    Ami: Optional[str]
    AssociatePublicIpAddress: Optional[bool]
    AvailabilityZone: Optional[str]
    EbsOptimized: Optional[bool]
    IamInstanceProfile: Optional[str]
    IamInstanceProfileArn: Optional[str]
    InstanceType: Optional[str]
    KeyName: Optional[str]
    Monitoring: Optional[bool]
    PlacementGroup: Optional[str]
    PlacementTenancy: Optional[str]
    SpotPrice: Optional[str]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    UserData: Optional[str]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    WeightedCapacity: Optional[str]
    EbsBlockDevice: Optional[Sequence["_EbsBlockDevice"]]
    EphemeralBlockDevice: Optional[Sequence["_EphemeralBlockDevice"]]
    RootBlockDevice: Optional[Sequence["_RootBlockDevice"]]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchSpecification"]:
        if not json_data:
            return None
        return cls(
            Ami=json_data.get("Ami"),
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            EbsOptimized=json_data.get("EbsOptimized"),
            IamInstanceProfile=json_data.get("IamInstanceProfile"),
            IamInstanceProfileArn=json_data.get("IamInstanceProfileArn"),
            InstanceType=json_data.get("InstanceType"),
            KeyName=json_data.get("KeyName"),
            Monitoring=json_data.get("Monitoring"),
            PlacementGroup=json_data.get("PlacementGroup"),
            PlacementTenancy=json_data.get("PlacementTenancy"),
            SpotPrice=json_data.get("SpotPrice"),
            SubnetId=json_data.get("SubnetId"),
            Tags=json_data.get("Tags"),
            UserData=json_data.get("UserData"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            WeightedCapacity=json_data.get("WeightedCapacity"),
            EbsBlockDevice=json_data.get("EbsBlockDevice"),
            EphemeralBlockDevice=json_data.get("EphemeralBlockDevice"),
            RootBlockDevice=json_data.get("RootBlockDevice"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchSpecification = LaunchSpecification


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
class EbsBlockDevice:
    DeleteOnTermination: Optional[bool]
    DeviceName: Optional[str]
    Encrypted: Optional[bool]
    Iops: Optional[float]
    KmsKeyId: Optional[str]
    SnapshotId: Optional[str]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsBlockDevice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsBlockDevice"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            DeviceName=json_data.get("DeviceName"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SnapshotId=json_data.get("SnapshotId"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsBlockDevice = EbsBlockDevice


@dataclass
class EphemeralBlockDevice:
    DeviceName: Optional[str]
    VirtualName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EphemeralBlockDevice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EphemeralBlockDevice"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            VirtualName=json_data.get("VirtualName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EphemeralBlockDevice = EphemeralBlockDevice


@dataclass
class RootBlockDevice:
    DeleteOnTermination: Optional[bool]
    Encrypted: Optional[bool]
    Iops: Optional[float]
    KmsKeyId: Optional[str]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RootBlockDevice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RootBlockDevice"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RootBlockDevice = RootBlockDevice


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


