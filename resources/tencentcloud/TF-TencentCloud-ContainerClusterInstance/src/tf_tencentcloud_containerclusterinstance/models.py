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
    AbnormalReason: Optional[str]
    Bandwidth: Optional[float]
    BandwidthType: Optional[str]
    ClusterId: Optional[str]
    Cpu: Optional[float]
    CvmType: Optional[str]
    DockerGraphPath: Optional[str]
    Id: Optional[str]
    InstanceId: Optional[str]
    InstanceName: Optional[str]
    InstanceType: Optional[str]
    IsNormal: Optional[float]
    IsVpcGateway: Optional[float]
    KeyId: Optional[str]
    LanIp: Optional[str]
    Mem: Optional[float]
    MountTarget: Optional[str]
    Password: Optional[str]
    Period: Optional[float]
    RequireWanIp: Optional[float]
    RootSize: Optional[float]
    RootType: Optional[str]
    SgId: Optional[str]
    StorageSize: Optional[float]
    StorageType: Optional[str]
    SubnetId: Optional[str]
    Unschedulable: Optional[float]
    UserScript: Optional[str]
    WanIp: Optional[str]
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
            AbnormalReason=json_data.get("AbnormalReason"),
            Bandwidth=json_data.get("Bandwidth"),
            BandwidthType=json_data.get("BandwidthType"),
            ClusterId=json_data.get("ClusterId"),
            Cpu=json_data.get("Cpu"),
            CvmType=json_data.get("CvmType"),
            DockerGraphPath=json_data.get("DockerGraphPath"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            InstanceName=json_data.get("InstanceName"),
            InstanceType=json_data.get("InstanceType"),
            IsNormal=json_data.get("IsNormal"),
            IsVpcGateway=json_data.get("IsVpcGateway"),
            KeyId=json_data.get("KeyId"),
            LanIp=json_data.get("LanIp"),
            Mem=json_data.get("Mem"),
            MountTarget=json_data.get("MountTarget"),
            Password=json_data.get("Password"),
            Period=json_data.get("Period"),
            RequireWanIp=json_data.get("RequireWanIp"),
            RootSize=json_data.get("RootSize"),
            RootType=json_data.get("RootType"),
            SgId=json_data.get("SgId"),
            StorageSize=json_data.get("StorageSize"),
            StorageType=json_data.get("StorageType"),
            SubnetId=json_data.get("SubnetId"),
            Unschedulable=json_data.get("Unschedulable"),
            UserScript=json_data.get("UserScript"),
            WanIp=json_data.get("WanIp"),
            ZoneId=json_data.get("ZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


