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
    AvailableZoneId: Optional[str]
    AvailableZoneName: Optional[str]
    BillingType: Optional[float]
    ChargingStartTime: Optional[str]
    ClusterAdminSecret: Optional[str]
    ClusterId: Optional[str]
    ClusterName: Optional[str]
    ClusterState: Optional[str]
    ClusterType: Optional[float]
    ClusterVersion: Optional[str]
    CoreDataVolumeCount: Optional[float]
    CoreDataVolumeSize: Optional[float]
    CoreDataVolumeType: Optional[str]
    CoreNodeNum: Optional[float]
    CoreNodeProductId: Optional[str]
    CoreNodeSize: Optional[str]
    CoreNodeSpecId: Optional[str]
    CreateAt: Optional[str]
    DeploymentId: Optional[str]
    Duration: Optional[str]
    ErrorInfo: Optional[str]
    ExternalAlternateIp: Optional[str]
    ExternalIp: Optional[str]
    Fee: Optional[str]
    HadoopVersion: Optional[str]
    Id: Optional[str]
    InstanceId: Optional[str]
    InternalIp: Optional[str]
    LogCollection: Optional[float]
    MasterDataVolumeCount: Optional[float]
    MasterDataVolumeSize: Optional[float]
    MasterDataVolumeType: Optional[str]
    MasterNodeIp: Optional[str]
    MasterNodeNum: Optional[float]
    MasterNodeProductId: Optional[str]
    MasterNodeSize: Optional[str]
    MasterNodeSpecId: Optional[str]
    NodePublicCertName: Optional[str]
    OrderId: Optional[str]
    PrivateIpFirst: Optional[str]
    Region: Optional[str]
    Remark: Optional[str]
    SafeMode: Optional[float]
    SecurityGroupsId: Optional[str]
    SlaveSecurityGroupsId: Optional[str]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TenantId: Optional[str]
    UpdateAt: Optional[str]
    Vnc: Optional[str]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]
    VpcId: Optional[str]
    AddJobs: Optional[Sequence["_AddJobs"]]
    BootstrapScripts: Optional[Sequence["_BootstrapScripts"]]
    ComponentList: Optional[Sequence["_ComponentList"]]
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
            AvailableZoneId=json_data.get("AvailableZoneId"),
            AvailableZoneName=json_data.get("AvailableZoneName"),
            BillingType=json_data.get("BillingType"),
            ChargingStartTime=json_data.get("ChargingStartTime"),
            ClusterAdminSecret=json_data.get("ClusterAdminSecret"),
            ClusterId=json_data.get("ClusterId"),
            ClusterName=json_data.get("ClusterName"),
            ClusterState=json_data.get("ClusterState"),
            ClusterType=json_data.get("ClusterType"),
            ClusterVersion=json_data.get("ClusterVersion"),
            CoreDataVolumeCount=json_data.get("CoreDataVolumeCount"),
            CoreDataVolumeSize=json_data.get("CoreDataVolumeSize"),
            CoreDataVolumeType=json_data.get("CoreDataVolumeType"),
            CoreNodeNum=json_data.get("CoreNodeNum"),
            CoreNodeProductId=json_data.get("CoreNodeProductId"),
            CoreNodeSize=json_data.get("CoreNodeSize"),
            CoreNodeSpecId=json_data.get("CoreNodeSpecId"),
            CreateAt=json_data.get("CreateAt"),
            DeploymentId=json_data.get("DeploymentId"),
            Duration=json_data.get("Duration"),
            ErrorInfo=json_data.get("ErrorInfo"),
            ExternalAlternateIp=json_data.get("ExternalAlternateIp"),
            ExternalIp=json_data.get("ExternalIp"),
            Fee=json_data.get("Fee"),
            HadoopVersion=json_data.get("HadoopVersion"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            InternalIp=json_data.get("InternalIp"),
            LogCollection=json_data.get("LogCollection"),
            MasterDataVolumeCount=json_data.get("MasterDataVolumeCount"),
            MasterDataVolumeSize=json_data.get("MasterDataVolumeSize"),
            MasterDataVolumeType=json_data.get("MasterDataVolumeType"),
            MasterNodeIp=json_data.get("MasterNodeIp"),
            MasterNodeNum=json_data.get("MasterNodeNum"),
            MasterNodeProductId=json_data.get("MasterNodeProductId"),
            MasterNodeSize=json_data.get("MasterNodeSize"),
            MasterNodeSpecId=json_data.get("MasterNodeSpecId"),
            NodePublicCertName=json_data.get("NodePublicCertName"),
            OrderId=json_data.get("OrderId"),
            PrivateIpFirst=json_data.get("PrivateIpFirst"),
            Region=json_data.get("Region"),
            Remark=json_data.get("Remark"),
            SafeMode=json_data.get("SafeMode"),
            SecurityGroupsId=json_data.get("SecurityGroupsId"),
            SlaveSecurityGroupsId=json_data.get("SlaveSecurityGroupsId"),
            SubnetId=json_data.get("SubnetId"),
            Tags=json_data.get("Tags"),
            TenantId=json_data.get("TenantId"),
            UpdateAt=json_data.get("UpdateAt"),
            Vnc=json_data.get("Vnc"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
            VpcId=json_data.get("VpcId"),
            AddJobs=json_data.get("AddJobs"),
            BootstrapScripts=json_data.get("BootstrapScripts"),
            ComponentList=json_data.get("ComponentList"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class AddJobs:
    Arguments: Optional[str]
    FileAction: Optional[str]
    HiveScriptPath: Optional[str]
    Hql: Optional[str]
    Input: Optional[str]
    JarPath: Optional[str]
    JobLog: Optional[str]
    JobName: Optional[str]
    JobType: Optional[float]
    Output: Optional[str]
    ShutdownCluster: Optional[bool]
    SubmitJobOnceClusterRun: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AddJobs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddJobs"]:
        if not json_data:
            return None
        return cls(
            Arguments=json_data.get("Arguments"),
            FileAction=json_data.get("FileAction"),
            HiveScriptPath=json_data.get("HiveScriptPath"),
            Hql=json_data.get("Hql"),
            Input=json_data.get("Input"),
            JarPath=json_data.get("JarPath"),
            JobLog=json_data.get("JobLog"),
            JobName=json_data.get("JobName"),
            JobType=json_data.get("JobType"),
            Output=json_data.get("Output"),
            ShutdownCluster=json_data.get("ShutdownCluster"),
            SubmitJobOnceClusterRun=json_data.get("SubmitJobOnceClusterRun"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddJobs = AddJobs


@dataclass
class BootstrapScripts:
    ActiveMaster: Optional[bool]
    BeforeComponentStart: Optional[bool]
    FailAction: Optional[str]
    Name: Optional[str]
    Nodes: Optional[Sequence[str]]
    Parameters: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BootstrapScripts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BootstrapScripts"]:
        if not json_data:
            return None
        return cls(
            ActiveMaster=json_data.get("ActiveMaster"),
            BeforeComponentStart=json_data.get("BeforeComponentStart"),
            FailAction=json_data.get("FailAction"),
            Name=json_data.get("Name"),
            Nodes=json_data.get("Nodes"),
            Parameters=json_data.get("Parameters"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BootstrapScripts = BootstrapScripts


@dataclass
class ComponentList:
    ComponentName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentList"]:
        if not json_data:
            return None
        return cls(
            ComponentName=json_data.get("ComponentName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentList = ComponentList


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


