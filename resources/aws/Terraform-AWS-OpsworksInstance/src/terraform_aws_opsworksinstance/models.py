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
    AgentVersion: Optional[str]
    AmiId: Optional[str]
    Architecture: Optional[str]
    AutoScalingType: Optional[str]
    AvailabilityZone: Optional[str]
    CreatedAt: Optional[str]
    DeleteEbs: Optional[bool]
    DeleteEip: Optional[bool]
    EbsOptimized: Optional[bool]
    Ec2InstanceId: Optional[str]
    EcsClusterArn: Optional[str]
    ElasticIp: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    InfrastructureClass: Optional[str]
    InstallUpdatesOnBoot: Optional[bool]
    InstanceProfileArn: Optional[str]
    InstanceType: Optional[str]
    LastServiceErrorId: Optional[str]
    LayerIds: Optional[Sequence[str]]
    Os: Optional[str]
    Platform: Optional[str]
    PrivateDns: Optional[str]
    PrivateIp: Optional[str]
    PublicDns: Optional[str]
    PublicIp: Optional[str]
    RegisteredBy: Optional[str]
    ReportedAgentVersion: Optional[str]
    ReportedOsFamily: Optional[str]
    ReportedOsName: Optional[str]
    ReportedOsVersion: Optional[str]
    RootDeviceType: Optional[str]
    RootDeviceVolumeId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SshHostDsaKeyFingerprint: Optional[str]
    SshHostRsaKeyFingerprint: Optional[str]
    SshKeyName: Optional[str]
    StackId: Optional[str]
    State: Optional[str]
    Status: Optional[str]
    SubnetId: Optional[str]
    Tenancy: Optional[str]
    VirtualizationType: Optional[str]
    EbsBlockDevice: Optional[Sequence["_EbsBlockDevice"]]
    EphemeralBlockDevice: Optional[Sequence["_EphemeralBlockDevice"]]
    RootBlockDevice: Optional[Sequence["_RootBlockDevice"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AgentVersion=json_data.get("AgentVersion"),
            AmiId=json_data.get("AmiId"),
            Architecture=json_data.get("Architecture"),
            AutoScalingType=json_data.get("AutoScalingType"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            CreatedAt=json_data.get("CreatedAt"),
            DeleteEbs=json_data.get("DeleteEbs"),
            DeleteEip=json_data.get("DeleteEip"),
            EbsOptimized=json_data.get("EbsOptimized"),
            Ec2InstanceId=json_data.get("Ec2InstanceId"),
            EcsClusterArn=json_data.get("EcsClusterArn"),
            ElasticIp=json_data.get("ElasticIp"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            InfrastructureClass=json_data.get("InfrastructureClass"),
            InstallUpdatesOnBoot=json_data.get("InstallUpdatesOnBoot"),
            InstanceProfileArn=json_data.get("InstanceProfileArn"),
            InstanceType=json_data.get("InstanceType"),
            LastServiceErrorId=json_data.get("LastServiceErrorId"),
            LayerIds=json_data.get("LayerIds"),
            Os=json_data.get("Os"),
            Platform=json_data.get("Platform"),
            PrivateDns=json_data.get("PrivateDns"),
            PrivateIp=json_data.get("PrivateIp"),
            PublicDns=json_data.get("PublicDns"),
            PublicIp=json_data.get("PublicIp"),
            RegisteredBy=json_data.get("RegisteredBy"),
            ReportedAgentVersion=json_data.get("ReportedAgentVersion"),
            ReportedOsFamily=json_data.get("ReportedOsFamily"),
            ReportedOsName=json_data.get("ReportedOsName"),
            ReportedOsVersion=json_data.get("ReportedOsVersion"),
            RootDeviceType=json_data.get("RootDeviceType"),
            RootDeviceVolumeId=json_data.get("RootDeviceVolumeId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SshHostDsaKeyFingerprint=json_data.get("SshHostDsaKeyFingerprint"),
            SshHostRsaKeyFingerprint=json_data.get("SshHostRsaKeyFingerprint"),
            SshKeyName=json_data.get("SshKeyName"),
            StackId=json_data.get("StackId"),
            State=json_data.get("State"),
            Status=json_data.get("Status"),
            SubnetId=json_data.get("SubnetId"),
            Tenancy=json_data.get("Tenancy"),
            VirtualizationType=json_data.get("VirtualizationType"),
            EbsBlockDevice=json_data.get("EbsBlockDevice"),
            EphemeralBlockDevice=json_data.get("EphemeralBlockDevice"),
            RootBlockDevice=json_data.get("RootBlockDevice"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EbsBlockDevice:
    DeleteOnTermination: Optional[bool]
    DeviceName: Optional[str]
    Iops: Optional[float]
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
            Iops=json_data.get("Iops"),
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
    Iops: Optional[float]
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
            Iops=json_data.get("Iops"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RootBlockDevice = RootBlockDevice


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


