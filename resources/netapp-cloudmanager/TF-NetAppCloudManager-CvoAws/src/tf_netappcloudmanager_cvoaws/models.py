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
    BackupVolumesToCbs: Optional[bool]
    CapacityTier: Optional[str]
    ClientId: Optional[str]
    CloudProviderAccount: Optional[str]
    ClusterFloatingIp: Optional[str]
    DataEncryptionType: Optional[str]
    DataFloatingIp: Optional[str]
    DataFloatingIp2: Optional[str]
    EbsVolumeSize: Optional[float]
    EbsVolumeSizeUnit: Optional[str]
    EbsVolumeType: Optional[str]
    EnableCompliance: Optional[bool]
    EnableMonitoring: Optional[bool]
    FailoverMode: Optional[str]
    Id: Optional[str]
    InstanceProfileName: Optional[str]
    InstanceTenancy: Optional[str]
    InstanceType: Optional[str]
    Iops: Optional[float]
    IsHa: Optional[bool]
    KmsKeyId: Optional[str]
    LicenseType: Optional[str]
    MediatorAssignPublicIp: Optional[bool]
    MediatorKeyPairName: Optional[str]
    MediatorSubnetId: Optional[str]
    Name: Optional[str]
    Node1SubnetId: Optional[str]
    Node2SubnetId: Optional[str]
    NssAccount: Optional[str]
    OntapVersion: Optional[str]
    OptimizedNetworkUtilization: Optional[bool]
    PlatformSerialNumber: Optional[str]
    PlatformSerialNumberNode1: Optional[str]
    PlatformSerialNumberNode2: Optional[str]
    Region: Optional[str]
    RouteTableIds: Optional[Sequence[str]]
    SecurityGroupId: Optional[str]
    SubnetId: Optional[str]
    SvmFloatingIp: Optional[str]
    SvmPassword: Optional[str]
    Throughput: Optional[float]
    TierLevel: Optional[str]
    UseLatestVersion: Optional[bool]
    VpcId: Optional[str]
    WorkspaceId: Optional[str]
    WritingSpeedState: Optional[str]
    AwsTag: Optional[Sequence["_AwsTagDefinition"]]

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
            BackupVolumesToCbs=json_data.get("BackupVolumesToCbs"),
            CapacityTier=json_data.get("CapacityTier"),
            ClientId=json_data.get("ClientId"),
            CloudProviderAccount=json_data.get("CloudProviderAccount"),
            ClusterFloatingIp=json_data.get("ClusterFloatingIp"),
            DataEncryptionType=json_data.get("DataEncryptionType"),
            DataFloatingIp=json_data.get("DataFloatingIp"),
            DataFloatingIp2=json_data.get("DataFloatingIp2"),
            EbsVolumeSize=json_data.get("EbsVolumeSize"),
            EbsVolumeSizeUnit=json_data.get("EbsVolumeSizeUnit"),
            EbsVolumeType=json_data.get("EbsVolumeType"),
            EnableCompliance=json_data.get("EnableCompliance"),
            EnableMonitoring=json_data.get("EnableMonitoring"),
            FailoverMode=json_data.get("FailoverMode"),
            Id=json_data.get("Id"),
            InstanceProfileName=json_data.get("InstanceProfileName"),
            InstanceTenancy=json_data.get("InstanceTenancy"),
            InstanceType=json_data.get("InstanceType"),
            Iops=json_data.get("Iops"),
            IsHa=json_data.get("IsHa"),
            KmsKeyId=json_data.get("KmsKeyId"),
            LicenseType=json_data.get("LicenseType"),
            MediatorAssignPublicIp=json_data.get("MediatorAssignPublicIp"),
            MediatorKeyPairName=json_data.get("MediatorKeyPairName"),
            MediatorSubnetId=json_data.get("MediatorSubnetId"),
            Name=json_data.get("Name"),
            Node1SubnetId=json_data.get("Node1SubnetId"),
            Node2SubnetId=json_data.get("Node2SubnetId"),
            NssAccount=json_data.get("NssAccount"),
            OntapVersion=json_data.get("OntapVersion"),
            OptimizedNetworkUtilization=json_data.get("OptimizedNetworkUtilization"),
            PlatformSerialNumber=json_data.get("PlatformSerialNumber"),
            PlatformSerialNumberNode1=json_data.get("PlatformSerialNumberNode1"),
            PlatformSerialNumberNode2=json_data.get("PlatformSerialNumberNode2"),
            Region=json_data.get("Region"),
            RouteTableIds=json_data.get("RouteTableIds"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SubnetId=json_data.get("SubnetId"),
            SvmFloatingIp=json_data.get("SvmFloatingIp"),
            SvmPassword=json_data.get("SvmPassword"),
            Throughput=json_data.get("Throughput"),
            TierLevel=json_data.get("TierLevel"),
            UseLatestVersion=json_data.get("UseLatestVersion"),
            VpcId=json_data.get("VpcId"),
            WorkspaceId=json_data.get("WorkspaceId"),
            WritingSpeedState=json_data.get("WritingSpeedState"),
            AwsTag=deserialize_list(json_data.get("AwsTag"), AwsTagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AwsTagDefinition(BaseModel):
    TagKey: Optional[str]
    TagValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsTagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsTagDefinition"]:
        if not json_data:
            return None
        return cls(
            TagKey=json_data.get("TagKey"),
            TagValue=json_data.get("TagValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsTagDefinition = AwsTagDefinition


