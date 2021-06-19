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
    AvailabilityZone: Optional[str]
    CertificateAuthority: Optional[Sequence["_CertificateAuthorityDefinition"]]
    ClientCert: Optional[str]
    ClientKey: Optional[str]
    ClusterCaCert: Optional[str]
    Connections: Optional[Sequence["_ConnectionsDefinition"]]
    DeletionProtection: Optional[bool]
    ForceUpdate: Optional[bool]
    Id: Optional[str]
    InstallCloudMonitor: Optional[bool]
    IsEnterpriseSecurityGroup: Optional[bool]
    KeyName: Optional[str]
    KubeConfig: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    NatGatewayId: Optional[str]
    NewNatGateway: Optional[bool]
    NodeCidrMask: Optional[float]
    Password: Optional[str]
    PodCidr: Optional[str]
    ProxyMode: Optional[str]
    RdsInstances: Optional[Sequence[str]]
    ResourceGroupId: Optional[str]
    SecurityGroupId: Optional[str]
    ServiceCidr: Optional[str]
    SlbInternet: Optional[str]
    SlbInternetEnabled: Optional[bool]
    SlbIntranet: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    UserData: Optional[str]
    Version: Optional[str]
    VpcId: Optional[str]
    WorkerDiskCategory: Optional[str]
    WorkerDiskPerformanceLevel: Optional[str]
    WorkerDiskSize: Optional[float]
    WorkerDiskSnapshotPolicyId: Optional[str]
    WorkerInstanceChargeType: Optional[str]
    WorkerInstanceTypes: Optional[Sequence[str]]
    WorkerNodes: Optional[Sequence["_WorkerNodesDefinition"]]
    WorkerNumber: Optional[float]
    WorkerVswitchIds: Optional[Sequence[str]]
    Addons: Optional[Sequence["_AddonsDefinition"]]
    LogConfig: Optional[Sequence["_LogConfigDefinition"]]
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
            AvailabilityZone=json_data.get("AvailabilityZone"),
            CertificateAuthority=deserialize_list(json_data.get("CertificateAuthority"), CertificateAuthorityDefinition),
            ClientCert=json_data.get("ClientCert"),
            ClientKey=json_data.get("ClientKey"),
            ClusterCaCert=json_data.get("ClusterCaCert"),
            Connections=deserialize_list(json_data.get("Connections"), ConnectionsDefinition),
            DeletionProtection=json_data.get("DeletionProtection"),
            ForceUpdate=json_data.get("ForceUpdate"),
            Id=json_data.get("Id"),
            InstallCloudMonitor=json_data.get("InstallCloudMonitor"),
            IsEnterpriseSecurityGroup=json_data.get("IsEnterpriseSecurityGroup"),
            KeyName=json_data.get("KeyName"),
            KubeConfig=json_data.get("KubeConfig"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            NatGatewayId=json_data.get("NatGatewayId"),
            NewNatGateway=json_data.get("NewNatGateway"),
            NodeCidrMask=json_data.get("NodeCidrMask"),
            Password=json_data.get("Password"),
            PodCidr=json_data.get("PodCidr"),
            ProxyMode=json_data.get("ProxyMode"),
            RdsInstances=json_data.get("RdsInstances"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            ServiceCidr=json_data.get("ServiceCidr"),
            SlbInternet=json_data.get("SlbInternet"),
            SlbInternetEnabled=json_data.get("SlbInternetEnabled"),
            SlbIntranet=json_data.get("SlbIntranet"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            UserData=json_data.get("UserData"),
            Version=json_data.get("Version"),
            VpcId=json_data.get("VpcId"),
            WorkerDiskCategory=json_data.get("WorkerDiskCategory"),
            WorkerDiskPerformanceLevel=json_data.get("WorkerDiskPerformanceLevel"),
            WorkerDiskSize=json_data.get("WorkerDiskSize"),
            WorkerDiskSnapshotPolicyId=json_data.get("WorkerDiskSnapshotPolicyId"),
            WorkerInstanceChargeType=json_data.get("WorkerInstanceChargeType"),
            WorkerInstanceTypes=json_data.get("WorkerInstanceTypes"),
            WorkerNodes=deserialize_list(json_data.get("WorkerNodes"), WorkerNodesDefinition),
            WorkerNumber=json_data.get("WorkerNumber"),
            WorkerVswitchIds=json_data.get("WorkerVswitchIds"),
            Addons=deserialize_list(json_data.get("Addons"), AddonsDefinition),
            LogConfig=deserialize_list(json_data.get("LogConfig"), LogConfigDefinition),
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


