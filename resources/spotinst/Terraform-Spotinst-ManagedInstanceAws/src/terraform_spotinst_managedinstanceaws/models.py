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
    ImageId: Optional[str]
    InstanceTypes: Optional[Sequence[str]]
    KeyPair: Optional[str]
    LifeCycle: Optional[str]
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
    IntegrationRoute53: Optional[Sequence["_IntegrationRoute53"]]
    LoadBalancers: Optional[Sequence["_LoadBalancers"]]
    NetworkInterface: Optional[Sequence["_NetworkInterface"]]
    RevertToSpot: Optional[Sequence["_RevertToSpot"]]
    ScheduledTask: Optional[Sequence["_ScheduledTask"]]
    Tags: Optional[Sequence["_Tags"]]
    Domains: Optional[Sequence["_Domains"]]
    RecordSets: Optional[Sequence["_RecordSets"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            ImageId=json_data.get("ImageId"),
            InstanceTypes=json_data.get("InstanceTypes"),
            KeyPair=json_data.get("KeyPair"),
            LifeCycle=json_data.get("LifeCycle"),
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
            IntegrationRoute53=json_data.get("IntegrationRoute53"),
            LoadBalancers=json_data.get("LoadBalancers"),
            NetworkInterface=json_data.get("NetworkInterface"),
            RevertToSpot=json_data.get("RevertToSpot"),
            ScheduledTask=json_data.get("ScheduledTask"),
            Tags=json_data.get("Tags"),
            Domains=json_data.get("Domains"),
            RecordSets=json_data.get("RecordSets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IntegrationRoute53:
    Domains: Optional[Sequence["_Domains"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationRoute53"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationRoute53"]:
        if not json_data:
            return None
        return cls(
            Domains=json_data.get("Domains"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationRoute53 = IntegrationRoute53


@dataclass
class Domains:
    HostedZoneId: Optional[str]
    SpotinstAcctId: Optional[str]
    RecordSets: Optional[Sequence["_RecordSets"]]

    @classmethod
    def _deserialize(
        cls: Type["_Domains"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Domains"]:
        if not json_data:
            return None
        return cls(
            HostedZoneId=json_data.get("HostedZoneId"),
            SpotinstAcctId=json_data.get("SpotinstAcctId"),
            RecordSets=json_data.get("RecordSets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Domains = Domains


@dataclass
class RecordSets:
    Name: Optional[str]
    UsePublicIp: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RecordSets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordSets"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            UsePublicIp=json_data.get("UsePublicIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordSets = RecordSets


@dataclass
class LoadBalancers:
    Arn: Optional[str]
    AutoWeight: Optional[bool]
    AzAwareness: Optional[bool]
    BalancerId: Optional[str]
    Name: Optional[str]
    TargetSetId: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancers"]:
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
_LoadBalancers = LoadBalancers


@dataclass
class NetworkInterface:
    AssociateIpv6Address: Optional[bool]
    AssociatePublicIpAddress: Optional[bool]
    DeviceIndex: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterface"]:
        if not json_data:
            return None
        return cls(
            AssociateIpv6Address=json_data.get("AssociateIpv6Address"),
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            DeviceIndex=json_data.get("DeviceIndex"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterface = NetworkInterface


@dataclass
class RevertToSpot:
    PerformAt: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RevertToSpot"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RevertToSpot"]:
        if not json_data:
            return None
        return cls(
            PerformAt=json_data.get("PerformAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RevertToSpot = RevertToSpot


@dataclass
class ScheduledTask:
    CronExpression: Optional[str]
    Frequency: Optional[str]
    IsEnabled: Optional[bool]
    StartTime: Optional[str]
    TaskType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduledTask"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledTask"]:
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
_ScheduledTask = ScheduledTask


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


