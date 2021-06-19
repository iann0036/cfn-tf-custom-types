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
    Bandwidth: Optional[float]
    BandwidthType: Optional[str]
    ClusterCidr: Optional[str]
    ClusterDesc: Optional[str]
    ClusterName: Optional[str]
    ClusterVersion: Optional[str]
    Cpu: Optional[float]
    CvmType: Optional[str]
    DockerGraphPath: Optional[str]
    GoodsNum: Optional[float]
    Id: Optional[str]
    InstanceName: Optional[str]
    InstanceType: Optional[str]
    IsVpcGateway: Optional[float]
    KeyId: Optional[str]
    KubernetesVersion: Optional[str]
    Mem: Optional[float]
    MountTarget: Optional[str]
    NodesNum: Optional[float]
    NodesStatus: Optional[str]
    OsName: Optional[str]
    Password: Optional[str]
    Period: Optional[float]
    RequireWanIp: Optional[float]
    RootSize: Optional[float]
    RootType: Optional[str]
    SgId: Optional[str]
    StorageSize: Optional[float]
    StorageType: Optional[str]
    SubnetId: Optional[str]
    TotalCpu: Optional[float]
    TotalMem: Optional[float]
    Unschedulable: Optional[float]
    UserScript: Optional[str]
    VpcId: Optional[str]
    ZoneId: Optional[str]

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
            Bandwidth=json_data.get("Bandwidth"),
            BandwidthType=json_data.get("BandwidthType"),
            ClusterCidr=json_data.get("ClusterCidr"),
            ClusterDesc=json_data.get("ClusterDesc"),
            ClusterName=json_data.get("ClusterName"),
            ClusterVersion=json_data.get("ClusterVersion"),
            Cpu=json_data.get("Cpu"),
            CvmType=json_data.get("CvmType"),
            DockerGraphPath=json_data.get("DockerGraphPath"),
            GoodsNum=json_data.get("GoodsNum"),
            Id=json_data.get("Id"),
            InstanceName=json_data.get("InstanceName"),
            InstanceType=json_data.get("InstanceType"),
            IsVpcGateway=json_data.get("IsVpcGateway"),
            KeyId=json_data.get("KeyId"),
            KubernetesVersion=json_data.get("KubernetesVersion"),
            Mem=json_data.get("Mem"),
            MountTarget=json_data.get("MountTarget"),
            NodesNum=json_data.get("NodesNum"),
            NodesStatus=json_data.get("NodesStatus"),
            OsName=json_data.get("OsName"),
            Password=json_data.get("Password"),
            Period=json_data.get("Period"),
            RequireWanIp=json_data.get("RequireWanIp"),
            RootSize=json_data.get("RootSize"),
            RootType=json_data.get("RootType"),
            SgId=json_data.get("SgId"),
            StorageSize=json_data.get("StorageSize"),
            StorageType=json_data.get("StorageType"),
            SubnetId=json_data.get("SubnetId"),
            TotalCpu=json_data.get("TotalCpu"),
            TotalMem=json_data.get("TotalMem"),
            Unschedulable=json_data.get("Unschedulable"),
            UserScript=json_data.get("UserScript"),
            VpcId=json_data.get("VpcId"),
            ZoneId=json_data.get("ZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


