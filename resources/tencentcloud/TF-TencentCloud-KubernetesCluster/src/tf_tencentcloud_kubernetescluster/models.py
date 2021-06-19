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
    BasePodNum: Optional[float]
    CertificationAuthority: Optional[str]
    ClaimExpiredSeconds: Optional[float]
    ClusterAsEnabled: Optional[bool]
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
    DeletionProtection: Optional[bool]
    DockerGraphPath: Optional[str]
    Domain: Optional[str]
    EnableCustomizedPodCidr: Optional[bool]
    EniSubnetIds: Optional[Sequence[str]]
    ExtraArgs: Optional[Sequence[str]]
    GlobeDesiredPodNum: Optional[float]
    Id: Optional[str]
    IgnoreClusterCidrConflict: Optional[bool]
    IsNonStaticIpMode: Optional[bool]
    KubeConfig: Optional[str]
    KubeProxyMode: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    ManagedClusterInternetSecurityPolicies: Optional[Sequence[str]]
    MountTarget: Optional[str]
    NetworkType: Optional[str]
    NodeNameType: Optional[str]
    Password: Optional[str]
    PgwEndpoint: Optional[str]
    ProjectId: Optional[float]
    SecurityPolicy: Optional[Sequence[str]]
    ServiceCidr: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Unschedulable: Optional[float]
    UpgradeInstancesFollowCluster: Optional[bool]
    UserName: Optional[str]
    VpcId: Optional[str]
    WorkerInstancesList: Optional[Sequence["_WorkerInstancesListDefinition"]]
    ClusterExtraArgs: Optional[Sequence["_ClusterExtraArgsDefinition"]]
    ExistInstance: Optional[Sequence["_ExistInstanceDefinition"]]
    MasterConfig: Optional[Sequence["_MasterConfigDefinition"]]
    NodePoolGlobalConfig: Optional[Sequence["_NodePoolGlobalConfigDefinition"]]
    WorkerConfig: Optional[Sequence["_WorkerConfigDefinition"]]

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
            BasePodNum=json_data.get("BasePodNum"),
            CertificationAuthority=json_data.get("CertificationAuthority"),
            ClaimExpiredSeconds=json_data.get("ClaimExpiredSeconds"),
            ClusterAsEnabled=json_data.get("ClusterAsEnabled"),
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
            DeletionProtection=json_data.get("DeletionProtection"),
            DockerGraphPath=json_data.get("DockerGraphPath"),
            Domain=json_data.get("Domain"),
            EnableCustomizedPodCidr=json_data.get("EnableCustomizedPodCidr"),
            EniSubnetIds=json_data.get("EniSubnetIds"),
            ExtraArgs=json_data.get("ExtraArgs"),
            GlobeDesiredPodNum=json_data.get("GlobeDesiredPodNum"),
            Id=json_data.get("Id"),
            IgnoreClusterCidrConflict=json_data.get("IgnoreClusterCidrConflict"),
            IsNonStaticIpMode=json_data.get("IsNonStaticIpMode"),
            KubeConfig=json_data.get("KubeConfig"),
            KubeProxyMode=json_data.get("KubeProxyMode"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            ManagedClusterInternetSecurityPolicies=json_data.get("ManagedClusterInternetSecurityPolicies"),
            MountTarget=json_data.get("MountTarget"),
            NetworkType=json_data.get("NetworkType"),
            NodeNameType=json_data.get("NodeNameType"),
            Password=json_data.get("Password"),
            PgwEndpoint=json_data.get("PgwEndpoint"),
            ProjectId=json_data.get("ProjectId"),
            SecurityPolicy=json_data.get("SecurityPolicy"),
            ServiceCidr=json_data.get("ServiceCidr"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Unschedulable=json_data.get("Unschedulable"),
            UpgradeInstancesFollowCluster=json_data.get("UpgradeInstancesFollowCluster"),
            UserName=json_data.get("UserName"),
            VpcId=json_data.get("VpcId"),
            WorkerInstancesList=deserialize_list(json_data.get("WorkerInstancesList"), WorkerInstancesListDefinition),
            ClusterExtraArgs=deserialize_list(json_data.get("ClusterExtraArgs"), ClusterExtraArgsDefinition),
            ExistInstance=deserialize_list(json_data.get("ExistInstance"), ExistInstanceDefinition),
            MasterConfig=deserialize_list(json_data.get("MasterConfig"), MasterConfigDefinition),
            NodePoolGlobalConfig=deserialize_list(json_data.get("NodePoolGlobalConfig"), NodePoolGlobalConfigDefinition),
            WorkerConfig=deserialize_list(json_data.get("WorkerConfig"), WorkerConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


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
class WorkerInstancesListDefinition(BaseModel):
    FailedReason: Optional[str]
    InstanceId: Optional[str]
    InstanceRole: Optional[str]
    InstanceState: Optional[str]
    LanIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerInstancesListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerInstancesListDefinition"]:
        if not json_data:
            return None
        return cls(
            FailedReason=json_data.get("FailedReason"),
            InstanceId=json_data.get("InstanceId"),
            InstanceRole=json_data.get("InstanceRole"),
            InstanceState=json_data.get("InstanceState"),
            LanIp=json_data.get("LanIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerInstancesListDefinition = WorkerInstancesListDefinition


@dataclass
class ClusterExtraArgsDefinition(BaseModel):
    KubeApiserver: Optional[Sequence[str]]
    KubeControllerManager: Optional[Sequence[str]]
    KubeScheduler: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterExtraArgsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterExtraArgsDefinition"]:
        if not json_data:
            return None
        return cls(
            KubeApiserver=json_data.get("KubeApiserver"),
            KubeControllerManager=json_data.get("KubeControllerManager"),
            KubeScheduler=json_data.get("KubeScheduler"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterExtraArgsDefinition = ClusterExtraArgsDefinition


@dataclass
class ExistInstanceDefinition(BaseModel):
    DesiredPodNumbers: Optional[Sequence[float]]
    NodeRole: Optional[str]
    InstancesPara: Optional[Sequence["_InstancesParaDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExistInstanceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExistInstanceDefinition"]:
        if not json_data:
            return None
        return cls(
            DesiredPodNumbers=json_data.get("DesiredPodNumbers"),
            NodeRole=json_data.get("NodeRole"),
            InstancesPara=deserialize_list(json_data.get("InstancesPara"), InstancesParaDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExistInstanceDefinition = ExistInstanceDefinition


@dataclass
class InstancesParaDefinition(BaseModel):
    InstanceIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_InstancesParaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstancesParaDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceIds=json_data.get("InstanceIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstancesParaDefinition = InstancesParaDefinition


@dataclass
class MasterConfigDefinition(BaseModel):
    AvailabilityZone: Optional[str]
    CamRoleName: Optional[str]
    Count: Optional[float]
    DesiredPodNum: Optional[float]
    DisasterRecoverGroupIds: Optional[Sequence[str]]
    EnhancedMonitorService: Optional[bool]
    EnhancedSecurityService: Optional[bool]
    Hostname: Optional[str]
    ImgId: Optional[str]
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
    DataDisk: Optional[Sequence["_DataDiskDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MasterConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            CamRoleName=json_data.get("CamRoleName"),
            Count=json_data.get("Count"),
            DesiredPodNum=json_data.get("DesiredPodNum"),
            DisasterRecoverGroupIds=json_data.get("DisasterRecoverGroupIds"),
            EnhancedMonitorService=json_data.get("EnhancedMonitorService"),
            EnhancedSecurityService=json_data.get("EnhancedSecurityService"),
            Hostname=json_data.get("Hostname"),
            ImgId=json_data.get("ImgId"),
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
            DataDisk=deserialize_list(json_data.get("DataDisk"), DataDiskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterConfigDefinition = MasterConfigDefinition


@dataclass
class DataDiskDefinition(BaseModel):
    DiskSize: Optional[float]
    DiskType: Optional[str]
    SnapshotId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskSize=json_data.get("DiskSize"),
            DiskType=json_data.get("DiskType"),
            SnapshotId=json_data.get("SnapshotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDiskDefinition = DataDiskDefinition


@dataclass
class NodePoolGlobalConfigDefinition(BaseModel):
    Expander: Optional[str]
    IgnoreDaemonSetsUtilization: Optional[bool]
    IsScaleInEnabled: Optional[bool]
    MaxConcurrentScaleIn: Optional[float]
    ScaleInDelay: Optional[float]
    ScaleInUnneededTime: Optional[float]
    ScaleInUtilizationThreshold: Optional[float]
    SkipNodesWithLocalStorage: Optional[bool]
    SkipNodesWithSystemPods: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NodePoolGlobalConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodePoolGlobalConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Expander=json_data.get("Expander"),
            IgnoreDaemonSetsUtilization=json_data.get("IgnoreDaemonSetsUtilization"),
            IsScaleInEnabled=json_data.get("IsScaleInEnabled"),
            MaxConcurrentScaleIn=json_data.get("MaxConcurrentScaleIn"),
            ScaleInDelay=json_data.get("ScaleInDelay"),
            ScaleInUnneededTime=json_data.get("ScaleInUnneededTime"),
            ScaleInUtilizationThreshold=json_data.get("ScaleInUtilizationThreshold"),
            SkipNodesWithLocalStorage=json_data.get("SkipNodesWithLocalStorage"),
            SkipNodesWithSystemPods=json_data.get("SkipNodesWithSystemPods"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodePoolGlobalConfigDefinition = NodePoolGlobalConfigDefinition


@dataclass
class WorkerConfigDefinition(BaseModel):
    AvailabilityZone: Optional[str]
    CamRoleName: Optional[str]
    Count: Optional[float]
    DesiredPodNum: Optional[float]
    DisasterRecoverGroupIds: Optional[Sequence[str]]
    EnhancedMonitorService: Optional[bool]
    EnhancedSecurityService: Optional[bool]
    Hostname: Optional[str]
    ImgId: Optional[str]
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
    DataDisk: Optional[Sequence["_DataDiskDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            CamRoleName=json_data.get("CamRoleName"),
            Count=json_data.get("Count"),
            DesiredPodNum=json_data.get("DesiredPodNum"),
            DisasterRecoverGroupIds=json_data.get("DisasterRecoverGroupIds"),
            EnhancedMonitorService=json_data.get("EnhancedMonitorService"),
            EnhancedSecurityService=json_data.get("EnhancedSecurityService"),
            Hostname=json_data.get("Hostname"),
            ImgId=json_data.get("ImgId"),
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
            DataDisk=deserialize_list(json_data.get("DataDisk"), DataDiskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerConfigDefinition = WorkerConfigDefinition


