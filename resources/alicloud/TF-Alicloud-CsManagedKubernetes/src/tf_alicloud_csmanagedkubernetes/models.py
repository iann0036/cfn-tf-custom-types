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
    ApiAudiences: Optional[Sequence[str]]
    AvailabilityZone: Optional[str]
    CertificateAuthority: Optional[Sequence["_CertificateAuthorityDefinition"]]
    ClientCert: Optional[str]
    ClientKey: Optional[str]
    ClusterCaCert: Optional[str]
    ClusterDomain: Optional[str]
    ClusterNetworkType: Optional[str]
    ClusterSpec: Optional[str]
    Connections: Optional[Sequence["_ConnectionsDefinition"]]
    CpuPolicy: Optional[str]
    CustomSan: Optional[str]
    DeletionProtection: Optional[bool]
    EnableSsh: Optional[bool]
    EncryptionProviderKey: Optional[str]
    ExcludeAutoscalerNodes: Optional[bool]
    ForceUpdate: Optional[bool]
    Id: Optional[str]
    ImageId: Optional[str]
    InstallCloudMonitor: Optional[bool]
    IsEnterpriseSecurityGroup: Optional[bool]
    KeyName: Optional[str]
    KmsEncryptedPassword: Optional[str]
    KmsEncryptionContext: Optional[Sequence["_KmsEncryptionContextDefinition"]]
    KubeConfig: Optional[str]
    LoadBalancerSpec: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    NatGatewayId: Optional[str]
    NewNatGateway: Optional[bool]
    NodeCidrMask: Optional[float]
    NodeNameMode: Optional[str]
    NodePortRange: Optional[str]
    OsType: Optional[str]
    Password: Optional[str]
    Platform: Optional[str]
    PodCidr: Optional[str]
    PodVswitchIds: Optional[Sequence[str]]
    ProxyMode: Optional[str]
    RdsInstances: Optional[Sequence[str]]
    ResourceGroupId: Optional[str]
    Runtime: Optional[Sequence["_RuntimeDefinition"]]
    SecurityGroupId: Optional[str]
    ServiceAccountIssuer: Optional[str]
    ServiceCidr: Optional[str]
    SlbId: Optional[str]
    SlbInternet: Optional[str]
    SlbInternetEnabled: Optional[bool]
    SlbIntranet: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Timezone: Optional[str]
    UserCa: Optional[str]
    UserData: Optional[str]
    Version: Optional[str]
    VpcId: Optional[str]
    VswitchIds: Optional[Sequence[str]]
    WorkerAutoRenew: Optional[bool]
    WorkerAutoRenewPeriod: Optional[float]
    WorkerDataDiskCategory: Optional[str]
    WorkerDataDiskSize: Optional[float]
    WorkerDiskCategory: Optional[str]
    WorkerDiskPerformanceLevel: Optional[str]
    WorkerDiskSize: Optional[float]
    WorkerDiskSnapshotPolicyId: Optional[str]
    WorkerInstanceChargeType: Optional[str]
    WorkerInstanceType: Optional[str]
    WorkerInstanceTypes: Optional[Sequence[str]]
    WorkerNodes: Optional[Sequence["_WorkerNodesDefinition"]]
    WorkerNumber: Optional[float]
    WorkerNumbers: Optional[Sequence[float]]
    WorkerPeriod: Optional[float]
    WorkerPeriodUnit: Optional[str]
    WorkerRamRoleName: Optional[str]
    WorkerVswitchIds: Optional[Sequence[str]]
    Addons: Optional[Sequence["_AddonsDefinition"]]
    LogConfig: Optional[Sequence["_LogConfigDefinition"]]
    MaintenanceWindow: Optional[Sequence["_MaintenanceWindowDefinition"]]
    Taints: Optional[Sequence["_TaintsDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    WorkerDataDisks: Optional[Sequence["_WorkerDataDisksDefinition"]]

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
            ApiAudiences=json_data.get("ApiAudiences"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            CertificateAuthority=deserialize_list(json_data.get("CertificateAuthority"), CertificateAuthorityDefinition),
            ClientCert=json_data.get("ClientCert"),
            ClientKey=json_data.get("ClientKey"),
            ClusterCaCert=json_data.get("ClusterCaCert"),
            ClusterDomain=json_data.get("ClusterDomain"),
            ClusterNetworkType=json_data.get("ClusterNetworkType"),
            ClusterSpec=json_data.get("ClusterSpec"),
            Connections=deserialize_list(json_data.get("Connections"), ConnectionsDefinition),
            CpuPolicy=json_data.get("CpuPolicy"),
            CustomSan=json_data.get("CustomSan"),
            DeletionProtection=json_data.get("DeletionProtection"),
            EnableSsh=json_data.get("EnableSsh"),
            EncryptionProviderKey=json_data.get("EncryptionProviderKey"),
            ExcludeAutoscalerNodes=json_data.get("ExcludeAutoscalerNodes"),
            ForceUpdate=json_data.get("ForceUpdate"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            InstallCloudMonitor=json_data.get("InstallCloudMonitor"),
            IsEnterpriseSecurityGroup=json_data.get("IsEnterpriseSecurityGroup"),
            KeyName=json_data.get("KeyName"),
            KmsEncryptedPassword=json_data.get("KmsEncryptedPassword"),
            KmsEncryptionContext=deserialize_list(json_data.get("KmsEncryptionContext"), KmsEncryptionContextDefinition),
            KubeConfig=json_data.get("KubeConfig"),
            LoadBalancerSpec=json_data.get("LoadBalancerSpec"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            NatGatewayId=json_data.get("NatGatewayId"),
            NewNatGateway=json_data.get("NewNatGateway"),
            NodeCidrMask=json_data.get("NodeCidrMask"),
            NodeNameMode=json_data.get("NodeNameMode"),
            NodePortRange=json_data.get("NodePortRange"),
            OsType=json_data.get("OsType"),
            Password=json_data.get("Password"),
            Platform=json_data.get("Platform"),
            PodCidr=json_data.get("PodCidr"),
            PodVswitchIds=json_data.get("PodVswitchIds"),
            ProxyMode=json_data.get("ProxyMode"),
            RdsInstances=json_data.get("RdsInstances"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            Runtime=deserialize_list(json_data.get("Runtime"), RuntimeDefinition),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            ServiceAccountIssuer=json_data.get("ServiceAccountIssuer"),
            ServiceCidr=json_data.get("ServiceCidr"),
            SlbId=json_data.get("SlbId"),
            SlbInternet=json_data.get("SlbInternet"),
            SlbInternetEnabled=json_data.get("SlbInternetEnabled"),
            SlbIntranet=json_data.get("SlbIntranet"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Timezone=json_data.get("Timezone"),
            UserCa=json_data.get("UserCa"),
            UserData=json_data.get("UserData"),
            Version=json_data.get("Version"),
            VpcId=json_data.get("VpcId"),
            VswitchIds=json_data.get("VswitchIds"),
            WorkerAutoRenew=json_data.get("WorkerAutoRenew"),
            WorkerAutoRenewPeriod=json_data.get("WorkerAutoRenewPeriod"),
            WorkerDataDiskCategory=json_data.get("WorkerDataDiskCategory"),
            WorkerDataDiskSize=json_data.get("WorkerDataDiskSize"),
            WorkerDiskCategory=json_data.get("WorkerDiskCategory"),
            WorkerDiskPerformanceLevel=json_data.get("WorkerDiskPerformanceLevel"),
            WorkerDiskSize=json_data.get("WorkerDiskSize"),
            WorkerDiskSnapshotPolicyId=json_data.get("WorkerDiskSnapshotPolicyId"),
            WorkerInstanceChargeType=json_data.get("WorkerInstanceChargeType"),
            WorkerInstanceType=json_data.get("WorkerInstanceType"),
            WorkerInstanceTypes=json_data.get("WorkerInstanceTypes"),
            WorkerNodes=deserialize_list(json_data.get("WorkerNodes"), WorkerNodesDefinition),
            WorkerNumber=json_data.get("WorkerNumber"),
            WorkerNumbers=json_data.get("WorkerNumbers"),
            WorkerPeriod=json_data.get("WorkerPeriod"),
            WorkerPeriodUnit=json_data.get("WorkerPeriodUnit"),
            WorkerRamRoleName=json_data.get("WorkerRamRoleName"),
            WorkerVswitchIds=json_data.get("WorkerVswitchIds"),
            Addons=deserialize_list(json_data.get("Addons"), AddonsDefinition),
            LogConfig=deserialize_list(json_data.get("LogConfig"), LogConfigDefinition),
            MaintenanceWindow=deserialize_list(json_data.get("MaintenanceWindow"), MaintenanceWindowDefinition),
            Taints=deserialize_list(json_data.get("Taints"), TaintsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            WorkerDataDisks=deserialize_list(json_data.get("WorkerDataDisks"), WorkerDataDisksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CertificateAuthorityDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateAuthorityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateAuthorityDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateAuthorityDefinition = CertificateAuthorityDefinition


@dataclass
class ConnectionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionsDefinition = ConnectionsDefinition


@dataclass
class KmsEncryptionContextDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KmsEncryptionContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KmsEncryptionContextDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KmsEncryptionContextDefinition = KmsEncryptionContextDefinition


@dataclass
class RuntimeDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuntimeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuntimeDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuntimeDefinition = RuntimeDefinition


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
class WorkerNodesDefinition(BaseModel):
    Id: Optional[str]
    Name: Optional[str]
    PrivateIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerNodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerNodesDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PrivateIp=json_data.get("PrivateIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerNodesDefinition = WorkerNodesDefinition


@dataclass
class AddonsDefinition(BaseModel):
    Config: Optional[str]
    Disabled: Optional[bool]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddonsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddonsDefinition"]:
        if not json_data:
            return None
        return cls(
            Config=json_data.get("Config"),
            Disabled=json_data.get("Disabled"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddonsDefinition = AddonsDefinition


@dataclass
class LogConfigDefinition(BaseModel):
    Project: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Project=json_data.get("Project"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfigDefinition = LogConfigDefinition


@dataclass
class MaintenanceWindowDefinition(BaseModel):
    Duration: Optional[str]
    Enable: Optional[bool]
    MaintenanceTime: Optional[str]
    WeeklyPeriod: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            Enable=json_data.get("Enable"),
            MaintenanceTime=json_data.get("MaintenanceTime"),
            WeeklyPeriod=json_data.get("WeeklyPeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowDefinition = MaintenanceWindowDefinition


@dataclass
class TaintsDefinition(BaseModel):
    Effect: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaintsDefinition"]:
        if not json_data:
            return None
        return cls(
            Effect=json_data.get("Effect"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaintsDefinition = TaintsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class WorkerDataDisksDefinition(BaseModel):
    AutoSnapshotPolicyId: Optional[str]
    Category: Optional[str]
    Device: Optional[str]
    Encrypted: Optional[str]
    KmsKeyId: Optional[str]
    Name: Optional[str]
    PerformanceLevel: Optional[str]
    Size: Optional[str]
    SnapshotId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerDataDisksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerDataDisksDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoSnapshotPolicyId=json_data.get("AutoSnapshotPolicyId"),
            Category=json_data.get("Category"),
            Device=json_data.get("Device"),
            Encrypted=json_data.get("Encrypted"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Name=json_data.get("Name"),
            PerformanceLevel=json_data.get("PerformanceLevel"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerDataDisksDefinition = WorkerDataDisksDefinition


