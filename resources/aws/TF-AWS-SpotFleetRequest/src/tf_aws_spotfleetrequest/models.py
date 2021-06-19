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
    AllocationStrategy: Optional[str]
    ClientToken: Optional[str]
    ExcessCapacityTerminationPolicy: Optional[str]
    FleetType: Optional[str]
    IamFleetRole: Optional[str]
    Id: Optional[str]
    InstanceInterruptionBehaviour: Optional[str]
    InstancePoolsToUseCount: Optional[float]
    LoadBalancers: Optional[Sequence[str]]
    OnDemandAllocationStrategy: Optional[str]
    OnDemandMaxTotalPrice: Optional[str]
    OnDemandTargetCapacity: Optional[float]
    ReplaceUnhealthyInstances: Optional[bool]
    SpotPrice: Optional[str]
    SpotRequestState: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    TargetCapacity: Optional[float]
    TargetGroupArns: Optional[Sequence[str]]
    TerminateInstancesWithExpiration: Optional[bool]
    ValidFrom: Optional[str]
    ValidUntil: Optional[str]
    WaitForFulfillment: Optional[bool]
    LaunchSpecification: Optional[Sequence["_LaunchSpecificationDefinition"]]
    LaunchTemplateConfig: Optional[Sequence["_LaunchTemplateConfigDefinition"]]
    SpotMaintenanceStrategies: Optional[Sequence["_SpotMaintenanceStrategiesDefinition"]]
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
            AllocationStrategy=json_data.get("AllocationStrategy"),
            ClientToken=json_data.get("ClientToken"),
            ExcessCapacityTerminationPolicy=json_data.get("ExcessCapacityTerminationPolicy"),
            FleetType=json_data.get("FleetType"),
            IamFleetRole=json_data.get("IamFleetRole"),
            Id=json_data.get("Id"),
            InstanceInterruptionBehaviour=json_data.get("InstanceInterruptionBehaviour"),
            InstancePoolsToUseCount=json_data.get("InstancePoolsToUseCount"),
            LoadBalancers=json_data.get("LoadBalancers"),
            OnDemandAllocationStrategy=json_data.get("OnDemandAllocationStrategy"),
            OnDemandMaxTotalPrice=json_data.get("OnDemandMaxTotalPrice"),
            OnDemandTargetCapacity=json_data.get("OnDemandTargetCapacity"),
            ReplaceUnhealthyInstances=json_data.get("ReplaceUnhealthyInstances"),
            SpotPrice=json_data.get("SpotPrice"),
            SpotRequestState=json_data.get("SpotRequestState"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            TargetCapacity=json_data.get("TargetCapacity"),
            TargetGroupArns=json_data.get("TargetGroupArns"),
            TerminateInstancesWithExpiration=json_data.get("TerminateInstancesWithExpiration"),
            ValidFrom=json_data.get("ValidFrom"),
            ValidUntil=json_data.get("ValidUntil"),
            WaitForFulfillment=json_data.get("WaitForFulfillment"),
            LaunchSpecification=deserialize_list(json_data.get("LaunchSpecification"), LaunchSpecificationDefinition),
            LaunchTemplateConfig=deserialize_list(json_data.get("LaunchTemplateConfig"), LaunchTemplateConfigDefinition),
            SpotMaintenanceStrategies=deserialize_list(json_data.get("SpotMaintenanceStrategies"), SpotMaintenanceStrategiesDefinition),
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
class LaunchSpecificationDefinition(BaseModel):
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
    Tags: Optional[Sequence["_TagsDefinition2"]]
    UserData: Optional[str]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    WeightedCapacity: Optional[str]
    EbsBlockDevice: Optional[Sequence["_EbsBlockDeviceDefinition"]]
    EphemeralBlockDevice: Optional[Sequence["_EphemeralBlockDeviceDefinition"]]
    RootBlockDevice: Optional[Sequence["_RootBlockDeviceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchSpecificationDefinition"]:
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
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition2),
            UserData=json_data.get("UserData"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            WeightedCapacity=json_data.get("WeightedCapacity"),
            EbsBlockDevice=deserialize_list(json_data.get("EbsBlockDevice"), EbsBlockDeviceDefinition),
            EphemeralBlockDevice=deserialize_list(json_data.get("EphemeralBlockDevice"), EphemeralBlockDeviceDefinition),
            RootBlockDevice=deserialize_list(json_data.get("RootBlockDevice"), RootBlockDeviceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchSpecificationDefinition = LaunchSpecificationDefinition


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
class EbsBlockDeviceDefinition(BaseModel):
    DeleteOnTermination: Optional[bool]
    DeviceName: Optional[str]
    Encrypted: Optional[bool]
    Iops: Optional[float]
    KmsKeyId: Optional[str]
    SnapshotId: Optional[str]
    Throughput: Optional[float]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsBlockDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsBlockDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            DeviceName=json_data.get("DeviceName"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SnapshotId=json_data.get("SnapshotId"),
            Throughput=json_data.get("Throughput"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsBlockDeviceDefinition = EbsBlockDeviceDefinition


@dataclass
class EphemeralBlockDeviceDefinition(BaseModel):
    DeviceName: Optional[str]
    VirtualName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EphemeralBlockDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EphemeralBlockDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            VirtualName=json_data.get("VirtualName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EphemeralBlockDeviceDefinition = EphemeralBlockDeviceDefinition


@dataclass
class RootBlockDeviceDefinition(BaseModel):
    DeleteOnTermination: Optional[bool]
    Encrypted: Optional[bool]
    Iops: Optional[float]
    KmsKeyId: Optional[str]
    Throughput: Optional[float]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RootBlockDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RootBlockDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Throughput=json_data.get("Throughput"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RootBlockDeviceDefinition = RootBlockDeviceDefinition


@dataclass
class LaunchTemplateConfigDefinition(BaseModel):
    LaunchTemplateSpecification: Optional[Sequence["_LaunchTemplateSpecificationDefinition"]]
    Overrides: Optional[Sequence["_OverridesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateSpecification=deserialize_list(json_data.get("LaunchTemplateSpecification"), LaunchTemplateSpecificationDefinition),
            Overrides=deserialize_list(json_data.get("Overrides"), OverridesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateConfigDefinition = LaunchTemplateConfigDefinition


@dataclass
class LaunchTemplateSpecificationDefinition(BaseModel):
    Id: Optional[str]
    Name: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateSpecificationDefinition = LaunchTemplateSpecificationDefinition


@dataclass
class OverridesDefinition(BaseModel):
    AvailabilityZone: Optional[str]
    InstanceType: Optional[str]
    Priority: Optional[float]
    SpotPrice: Optional[str]
    SubnetId: Optional[str]
    WeightedCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OverridesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverridesDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            InstanceType=json_data.get("InstanceType"),
            Priority=json_data.get("Priority"),
            SpotPrice=json_data.get("SpotPrice"),
            SubnetId=json_data.get("SubnetId"),
            WeightedCapacity=json_data.get("WeightedCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverridesDefinition = OverridesDefinition


@dataclass
class SpotMaintenanceStrategiesDefinition(BaseModel):
    CapacityRebalance: Optional[Sequence["_CapacityRebalanceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpotMaintenanceStrategiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotMaintenanceStrategiesDefinition"]:
        if not json_data:
            return None
        return cls(
            CapacityRebalance=deserialize_list(json_data.get("CapacityRebalance"), CapacityRebalanceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotMaintenanceStrategiesDefinition = SpotMaintenanceStrategiesDefinition


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
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


