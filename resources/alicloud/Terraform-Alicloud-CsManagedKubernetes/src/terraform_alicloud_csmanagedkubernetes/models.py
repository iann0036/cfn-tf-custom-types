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
    AvailabilityZone: Optional[str]
    ClientCert: Optional[str]
    ClientKey: Optional[str]
    ClusterCaCert: Optional[str]
    ClusterNetworkType: Optional[str]
    Connections: Optional[Sequence["_Connections"]]
    CpuPolicy: Optional[str]
    EnableSsh: Optional[bool]
    ForceUpdate: Optional[bool]
    ImageId: Optional[str]
    InstallCloudMonitor: Optional[bool]
    KeyName: Optional[str]
    KmsEncryptedPassword: Optional[str]
    KmsEncryptionContext: Optional[Sequence["_KmsEncryptionContext"]]
    KubeConfig: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    NatGatewayId: Optional[str]
    NewNatGateway: Optional[bool]
    NodeCidrMask: Optional[float]
    Password: Optional[str]
    PodCidr: Optional[str]
    PodVswitchIds: Optional[Sequence[str]]
    ProxyMode: Optional[str]
    SecurityGroupId: Optional[str]
    ServiceCidr: Optional[str]
    SlbId: Optional[str]
    SlbInternet: Optional[str]
    SlbInternetEnabled: Optional[bool]
    SlbIntranet: Optional[str]
    UserCa: Optional[str]
    Version: Optional[str]
    VpcId: Optional[str]
    VswitchIds: Optional[Sequence[str]]
    WorkerAutoRenew: Optional[bool]
    WorkerAutoRenewPeriod: Optional[float]
    WorkerDataDiskCategory: Optional[str]
    WorkerDataDiskSize: Optional[float]
    WorkerDiskCategory: Optional[str]
    WorkerDiskSize: Optional[float]
    WorkerInstanceChargeType: Optional[str]
    WorkerInstanceType: Optional[str]
    WorkerInstanceTypes: Optional[Sequence[str]]
    WorkerNodes: Optional[Sequence["_WorkerNodes"]]
    WorkerNumber: Optional[float]
    WorkerNumbers: Optional[Sequence[float]]
    WorkerPeriod: Optional[float]
    WorkerPeriodUnit: Optional[str]
    WorkerVswitchIds: Optional[Sequence[str]]
    Addons: Optional[Sequence["_Addons"]]
    LogConfig: Optional[Sequence["_LogConfig"]]
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
            AvailabilityZone=json_data.get("AvailabilityZone"),
            ClientCert=json_data.get("ClientCert"),
            ClientKey=json_data.get("ClientKey"),
            ClusterCaCert=json_data.get("ClusterCaCert"),
            ClusterNetworkType=json_data.get("ClusterNetworkType"),
            Connections=json_data.get("Connections"),
            CpuPolicy=json_data.get("CpuPolicy"),
            EnableSsh=json_data.get("EnableSsh"),
            ForceUpdate=json_data.get("ForceUpdate"),
            ImageId=json_data.get("ImageId"),
            InstallCloudMonitor=json_data.get("InstallCloudMonitor"),
            KeyName=json_data.get("KeyName"),
            KmsEncryptedPassword=json_data.get("KmsEncryptedPassword"),
            KmsEncryptionContext=json_data.get("KmsEncryptionContext"),
            KubeConfig=json_data.get("KubeConfig"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            NatGatewayId=json_data.get("NatGatewayId"),
            NewNatGateway=json_data.get("NewNatGateway"),
            NodeCidrMask=json_data.get("NodeCidrMask"),
            Password=json_data.get("Password"),
            PodCidr=json_data.get("PodCidr"),
            PodVswitchIds=json_data.get("PodVswitchIds"),
            ProxyMode=json_data.get("ProxyMode"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            ServiceCidr=json_data.get("ServiceCidr"),
            SlbId=json_data.get("SlbId"),
            SlbInternet=json_data.get("SlbInternet"),
            SlbInternetEnabled=json_data.get("SlbInternetEnabled"),
            SlbIntranet=json_data.get("SlbIntranet"),
            UserCa=json_data.get("UserCa"),
            Version=json_data.get("Version"),
            VpcId=json_data.get("VpcId"),
            VswitchIds=json_data.get("VswitchIds"),
            WorkerAutoRenew=json_data.get("WorkerAutoRenew"),
            WorkerAutoRenewPeriod=json_data.get("WorkerAutoRenewPeriod"),
            WorkerDataDiskCategory=json_data.get("WorkerDataDiskCategory"),
            WorkerDataDiskSize=json_data.get("WorkerDataDiskSize"),
            WorkerDiskCategory=json_data.get("WorkerDiskCategory"),
            WorkerDiskSize=json_data.get("WorkerDiskSize"),
            WorkerInstanceChargeType=json_data.get("WorkerInstanceChargeType"),
            WorkerInstanceType=json_data.get("WorkerInstanceType"),
            WorkerInstanceTypes=json_data.get("WorkerInstanceTypes"),
            WorkerNodes=json_data.get("WorkerNodes"),
            WorkerNumber=json_data.get("WorkerNumber"),
            WorkerNumbers=json_data.get("WorkerNumbers"),
            WorkerPeriod=json_data.get("WorkerPeriod"),
            WorkerPeriodUnit=json_data.get("WorkerPeriodUnit"),
            WorkerVswitchIds=json_data.get("WorkerVswitchIds"),
            Addons=json_data.get("Addons"),
            LogConfig=json_data.get("LogConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Connections:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Connections"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Connections"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Connections = Connections


@dataclass
class KmsEncryptionContext:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KmsEncryptionContext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KmsEncryptionContext"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KmsEncryptionContext = KmsEncryptionContext


@dataclass
class WorkerNodes:
    Id: Optional[str]
    Name: Optional[str]
    PrivateIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerNodes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerNodes"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PrivateIp=json_data.get("PrivateIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerNodes = WorkerNodes


@dataclass
class Addons:
    Config: Optional[str]
    Disabled: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Addons"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Addons"]:
        if not json_data:
            return None
        return cls(
            Config=json_data.get("Config"),
            Disabled=json_data.get("Disabled"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Addons = Addons


@dataclass
class LogConfig:
    Project: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfig"]:
        if not json_data:
            return None
        return cls(
            Project=json_data.get("Project"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfig = LogConfig


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


