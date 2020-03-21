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
    ClusterId: Optional[str]
    WorkerInstancesList: Optional[Sequence["_WorkerInstancesList"]]
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
            ClusterId=json_data.get("ClusterId"),
            WorkerInstancesList=json_data.get("WorkerInstancesList"),
            WorkerConfig=json_data.get("WorkerConfig"),
            DataDisk=json_data.get("DataDisk"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


