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
    AutoHealing: Optional[bool]
    BlockDevicesMode: Optional[str]
    CpuCredits: Optional[str]
    Description: Optional[str]
    DrainingTimeout: Optional[float]
    EbsOptimized: Optional[bool]
    ElasticIp: Optional[str]
    EnableMonitoring: Optional[bool]
    FallBackToOd: Optional[bool]
    GracePeriod: Optional[float]
    HealthCheckType: Optional[str]
    IamInstanceProfile: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    InstanceTypes: Optional[Sequence[str]]
    KeyPair: Optional[str]
    LifeCycle: Optional[str]
    MinimumInstanceLifetime: Optional[float]
    Name: Optional[str]
    OptimizationWindows: Optional[Sequence[str]]
    Orientation: Optional[str]
    PersistBlockDevices: Optional[bool]
    PersistPrivateIp: Optional[bool]
    PersistRootDevice: Optional[bool]
    PlacementTenancy: Optional[str]
    PreferredType: Optional[str]
    PrivateIp: Optional[str]
    Product: Optional[str]
    Region: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    ShutdownScript: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    UnhealthyDuration: Optional[float]
    UserData: Optional[str]
    UtilizeReservedInstances: Optional[bool]
    VpcId: Optional[str]
    BlockDeviceMappings: Optional[Sequence["_BlockDeviceMappingsDefinition"]]
    IntegrationRoute53: Optional[Sequence["_IntegrationRoute53Definition"]]
    LoadBalancers: Optional[Sequence["_LoadBalancersDefinition"]]
    ManagedInstanceAction: Optional[Sequence["_ManagedInstanceActionDefinition"]]
    NetworkInterface: Optional[Sequence["_NetworkInterfaceDefinition"]]
    RevertToSpot: Optional[Sequence["_RevertToSpotDefinition"]]
    ScheduledTask: Optional[Sequence["_ScheduledTaskDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]

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
            AutoHealing=json_data.get("AutoHealing"),
            BlockDevicesMode=json_data.get("BlockDevicesMode"),
            CpuCredits=json_data.get("CpuCredits"),
            Description=json_data.get("Description"),
            DrainingTimeout=json_data.get("DrainingTimeout"),
            EbsOptimized=json_data.get("EbsOptimized"),
            ElasticIp=json_data.get("ElasticIp"),
            EnableMonitoring=json_data.get("EnableMonitoring"),
            FallBackToOd=json_data.get("FallBackToOd"),
            GracePeriod=json_data.get("GracePeriod"),
            HealthCheckType=json_data.get("HealthCheckType"),
            IamInstanceProfile=json_data.get("IamInstanceProfile"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            InstanceTypes=json_data.get("InstanceTypes"),
            KeyPair=json_data.get("KeyPair"),
            LifeCycle=json_data.get("LifeCycle"),
            MinimumInstanceLifetime=json_data.get("MinimumInstanceLifetime"),
            Name=json_data.get("Name"),
            OptimizationWindows=json_data.get("OptimizationWindows"),
            Orientation=json_data.get("Orientation"),
            PersistBlockDevices=json_data.get("PersistBlockDevices"),
            PersistPrivateIp=json_data.get("PersistPrivateIp"),
            PersistRootDevice=json_data.get("PersistRootDevice"),
            PlacementTenancy=json_data.get("PlacementTenancy"),
            PreferredType=json_data.get("PreferredType"),
            PrivateIp=json_data.get("PrivateIp"),
            Product=json_data.get("Product"),
            Region=json_data.get("Region"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            ShutdownScript=json_data.get("ShutdownScript"),
            SubnetIds=json_data.get("SubnetIds"),
            UnhealthyDuration=json_data.get("UnhealthyDuration"),
            UserData=json_data.get("UserData"),
            UtilizeReservedInstances=json_data.get("UtilizeReservedInstances"),
            VpcId=json_data.get("VpcId"),
            BlockDeviceMappings=deserialize_list(json_data.get("BlockDeviceMappings"), BlockDeviceMappingsDefinition),
            IntegrationRoute53=deserialize_list(json_data.get("IntegrationRoute53"), IntegrationRoute53Definition),
            LoadBalancers=deserialize_list(json_data.get("LoadBalancers"), LoadBalancersDefinition),
            ManagedInstanceAction=deserialize_list(json_data.get("ManagedInstanceAction"), ManagedInstanceActionDefinition),
            NetworkInterface=deserialize_list(json_data.get("NetworkInterface"), NetworkInterfaceDefinition),
            RevertToSpot=deserialize_list(json_data.get("RevertToSpot"), RevertToSpotDefinition),
            ScheduledTask=deserialize_list(json_data.get("ScheduledTask"), ScheduledTaskDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BlockDeviceMappingsDefinition(BaseModel):
    DeviceName: Optional[str]
    Ebs: Optional[Sequence["_EbsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BlockDeviceMappingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockDeviceMappingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            Ebs=deserialize_list(json_data.get("Ebs"), EbsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockDeviceMappingsDefinition = BlockDeviceMappingsDefinition


@dataclass
class EbsDefinition(BaseModel):
    DeleteOnTermination: Optional[bool]
    Iops: Optional[float]
    Throughput: Optional[float]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Iops=json_data.get("Iops"),
            Throughput=json_data.get("Throughput"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsDefinition = EbsDefinition


@dataclass
class IntegrationRoute53Definition(BaseModel):
    Domains: Optional[Sequence["_DomainsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationRoute53Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationRoute53Definition"]:
        if not json_data:
            return None
        return cls(
            Domains=deserialize_list(json_data.get("Domains"), DomainsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationRoute53Definition = IntegrationRoute53Definition


@dataclass
class DomainsDefinition(BaseModel):
    HostedZoneId: Optional[str]
    RecordSetType: Optional[str]
    SpotinstAcctId: Optional[str]
    RecordSets: Optional[Sequence["_RecordSetsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DomainsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainsDefinition"]:
        if not json_data:
            return None
        return cls(
            HostedZoneId=json_data.get("HostedZoneId"),
            RecordSetType=json_data.get("RecordSetType"),
            SpotinstAcctId=json_data.get("SpotinstAcctId"),
            RecordSets=deserialize_list(json_data.get("RecordSets"), RecordSetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainsDefinition = DomainsDefinition


@dataclass
class RecordSetsDefinition(BaseModel):
    Name: Optional[str]
    UsePublicDns: Optional[bool]
    UsePublicIp: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RecordSetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordSetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            UsePublicDns=json_data.get("UsePublicDns"),
            UsePublicIp=json_data.get("UsePublicIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordSetsDefinition = RecordSetsDefinition


@dataclass
class LoadBalancersDefinition(BaseModel):
    Arn: Optional[str]
    AutoWeight: Optional[bool]
    AzAwareness: Optional[bool]
    BalancerId: Optional[str]
    Name: Optional[str]
    TargetSetId: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancersDefinition"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            AutoWeight=json_data.get("AutoWeight"),
            AzAwareness=json_data.get("AzAwareness"),
            BalancerId=json_data.get("BalancerId"),
            Name=json_data.get("Name"),
            TargetSetId=json_data.get("TargetSetId"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancersDefinition = LoadBalancersDefinition


@dataclass
class ManagedInstanceActionDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedInstanceActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedInstanceActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedInstanceActionDefinition = ManagedInstanceActionDefinition


@dataclass
class NetworkInterfaceDefinition(BaseModel):
    AssociateIpv6Address: Optional[bool]
    AssociatePublicIpAddress: Optional[bool]
    DeviceIndex: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            AssociateIpv6Address=json_data.get("AssociateIpv6Address"),
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            DeviceIndex=json_data.get("DeviceIndex"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfaceDefinition = NetworkInterfaceDefinition


@dataclass
class RevertToSpotDefinition(BaseModel):
    PerformAt: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RevertToSpotDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RevertToSpotDefinition"]:
        if not json_data:
            return None
        return cls(
            PerformAt=json_data.get("PerformAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RevertToSpotDefinition = RevertToSpotDefinition


@dataclass
class ScheduledTaskDefinition(BaseModel):
    CronExpression: Optional[str]
    Frequency: Optional[str]
    IsEnabled: Optional[bool]
    StartTime: Optional[str]
    TaskType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduledTaskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledTaskDefinition"]:
        if not json_data:
            return None
        return cls(
            CronExpression=json_data.get("CronExpression"),
            Frequency=json_data.get("Frequency"),
            IsEnabled=json_data.get("IsEnabled"),
            StartTime=json_data.get("StartTime"),
            TaskType=json_data.get("TaskType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledTaskDefinition = ScheduledTaskDefinition


@dataclass
class TagsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


