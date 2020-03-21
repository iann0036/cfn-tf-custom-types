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
    CertificationAuthority: Optional[str]
    ClusterCidr: Optional[str]
    ClusterDeployType: Optional[str]
    ClusterDesc: Optional[str]
    ClusterExternalEndpoint: Optional[str]
    ClusterInternet: Optional[bool]
    ClusterIntranet: Optional[bool]
    ClusterIntranetSubnetId: Optional[str]
    ClusterIpvs: Optional[bool]
    ClusterMaxPodNum: Optional[float]
    ClusterMaxServiceNum: Optional[float]
    ClusterName: Optional[str]
    ClusterNodeNum: Optional[float]
    ClusterOs: Optional[str]
    ClusterOsType: Optional[str]
    ClusterVersion: Optional[str]
    ContainerRuntime: Optional[str]
    Domain: Optional[str]
    Id: Optional[str]
    IgnoreClusterCidrConflict: Optional[bool]
    ManagedClusterInternetSecurityPolicies: Optional[Sequence[str]]
    Password: Optional[str]
    PgwEndpoint: Optional[str]
    ProjectId: Optional[float]
    SecurityPolicy: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    UserName: Optional[str]
    VpcId: Optional[str]
    WorkerInstancesList: Optional[Sequence["_WorkerInstancesList"]]
    MasterConfig: Optional[Sequence["_MasterConfig"]]
    WorkerConfig: Optional[Sequence["_WorkerConfig"]]
    DataDisk: Optional[Sequence["_DataDisk"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CertificationAuthority=json_data.get("CertificationAuthority"),
            ClusterCidr=json_data.get("ClusterCidr"),
            ClusterDeployType=json_data.get("ClusterDeployType"),
            ClusterDesc=json_data.get("ClusterDesc"),
            ClusterExternalEndpoint=json_data.get("ClusterExternalEndpoint"),
            ClusterInternet=json_data.get("ClusterInternet"),
            ClusterIntranet=json_data.get("ClusterIntranet"),
            ClusterIntranetSubnetId=json_data.get("ClusterIntranetSubnetId"),
            ClusterIpvs=json_data.get("ClusterIpvs"),
            ClusterMaxPodNum=json_data.get("ClusterMaxPodNum"),
            ClusterMaxServiceNum=json_data.get("ClusterMaxServiceNum"),
            ClusterName=json_data.get("ClusterName"),
            ClusterNodeNum=json_data.get("ClusterNodeNum"),
            ClusterOs=json_data.get("ClusterOs"),
            ClusterOsType=json_data.get("ClusterOsType"),
            ClusterVersion=json_data.get("ClusterVersion"),
            ContainerRuntime=json_data.get("ContainerRuntime"),
            Domain=json_data.get("Domain"),
            Id=json_data.get("Id"),
            IgnoreClusterCidrConflict=json_data.get("IgnoreClusterCidrConflict"),
            ManagedClusterInternetSecurityPolicies=json_data.get("ManagedClusterInternetSecurityPolicies"),
            Password=json_data.get("Password"),
            PgwEndpoint=json_data.get("PgwEndpoint"),
            ProjectId=json_data.get("ProjectId"),
            SecurityPolicy=json_data.get("SecurityPolicy"),
            Tags=json_data.get("Tags"),
            UserName=json_data.get("UserName"),
            VpcId=json_data.get("VpcId"),
            WorkerInstancesList=json_data.get("WorkerInstancesList"),
            MasterConfig=json_data.get("MasterConfig"),
            WorkerConfig=json_data.get("WorkerConfig"),
            DataDisk=json_data.get("DataDisk"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class WorkerInstancesList:
    FailedReason: Optional[str]
    InstanceId: Optional[str]
    InstanceRole: Optional[str]
    InstanceState: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerInstancesList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerInstancesList"]:
        if not json_data:
            return None
        return cls(
            FailedReason=json_data.get("FailedReason"),
            InstanceId=json_data.get("InstanceId"),
            InstanceRole=json_data.get("InstanceRole"),
            InstanceState=json_data.get("InstanceState"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerInstancesList = WorkerInstancesList


@dataclass
class MasterConfig:
    AvailabilityZone: Optional[str]
    Count: Optional[float]
    EnhancedMonitorService: Optional[bool]
    EnhancedSecurityService: Optional[bool]
    InstanceChargeType: Optional[str]
    InstanceChargeTypePrepaidPeriod: Optional[float]
    InstanceChargeTypePrepaidRenewFlag: Optional[str]
    InstanceName: Optional[str]
    InstanceType: Optional[str]
    InternetChargeType: Optional[str]
    InternetMaxBandwidthOut: Optional[float]
    KeyIds: Optional[Sequence[str]]
    Password: Optional[str]
    PublicIpAssigned: Optional[bool]
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetId: Optional[str]
    SystemDiskSize: Optional[float]
    SystemDiskType: Optional[str]
    UserData: Optional[str]
    DataDisk: Optional[Sequence["_DataDisk"]]

    @classmethod
    def _deserialize(
        cls: Type["_MasterConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterConfig"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Count=json_data.get("Count"),
            EnhancedMonitorService=json_data.get("EnhancedMonitorService"),
            EnhancedSecurityService=json_data.get("EnhancedSecurityService"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            InstanceChargeTypePrepaidPeriod=json_data.get("InstanceChargeTypePrepaidPeriod"),
            InstanceChargeTypePrepaidRenewFlag=json_data.get("InstanceChargeTypePrepaidRenewFlag"),
            InstanceName=json_data.get("InstanceName"),
            InstanceType=json_data.get("InstanceType"),
            InternetChargeType=json_data.get("InternetChargeType"),
            InternetMaxBandwidthOut=json_data.get("InternetMaxBandwidthOut"),
            KeyIds=json_data.get("KeyIds"),
            Password=json_data.get("Password"),
            PublicIpAssigned=json_data.get("PublicIpAssigned"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetId=json_data.get("SubnetId"),
            SystemDiskSize=json_data.get("SystemDiskSize"),
            SystemDiskType=json_data.get("SystemDiskType"),
            UserData=json_data.get("UserData"),
            DataDisk=json_data.get("DataDisk"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterConfig = MasterConfig


@dataclass
class DataDisk:
    DiskSize: Optional[float]
    DiskType: Optional[str]
    SnapshotId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDisk"]:
        if not json_data:
            return None
        return cls(
            DiskSize=json_data.get("DiskSize"),
            DiskType=json_data.get("DiskType"),
            SnapshotId=json_data.get("SnapshotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDisk = DataDisk


@dataclass
class WorkerConfig:
    AvailabilityZone: Optional[str]
    Count: Optional[float]
    EnhancedMonitorService: Optional[bool]
    EnhancedSecurityService: Optional[bool]
    InstanceChargeType: Optional[str]
    InstanceChargeTypePrepaidPeriod: Optional[float]
    InstanceChargeTypePrepaidRenewFlag: Optional[str]
    InstanceName: Optional[str]
    InstanceType: Optional[str]
    InternetChargeType: Optional[str]
    InternetMaxBandwidthOut: Optional[float]
    KeyIds: Optional[Sequence[str]]
    Password: Optional[str]
    PublicIpAssigned: Optional[bool]
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetId: Optional[str]
    SystemDiskSize: Optional[float]
    SystemDiskType: Optional[str]
    UserData: Optional[str]
    DataDisk: Optional[Sequence["_DataDisk"]]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerConfig"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Count=json_data.get("Count"),
            EnhancedMonitorService=json_data.get("EnhancedMonitorService"),
            EnhancedSecurityService=json_data.get("EnhancedSecurityService"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            InstanceChargeTypePrepaidPeriod=json_data.get("InstanceChargeTypePrepaidPeriod"),
            InstanceChargeTypePrepaidRenewFlag=json_data.get("InstanceChargeTypePrepaidRenewFlag"),
            InstanceName=json_data.get("InstanceName"),
            InstanceType=json_data.get("InstanceType"),
            InternetChargeType=json_data.get("InternetChargeType"),
            InternetMaxBandwidthOut=json_data.get("InternetMaxBandwidthOut"),
            KeyIds=json_data.get("KeyIds"),
            Password=json_data.get("Password"),
            PublicIpAssigned=json_data.get("PublicIpAssigned"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetId=json_data.get("SubnetId"),
            SystemDiskSize=json_data.get("SystemDiskSize"),
            SystemDiskType=json_data.get("SystemDiskType"),
            UserData=json_data.get("UserData"),
            DataDisk=json_data.get("DataDisk"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerConfig = WorkerConfig


