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
    ConfigurationName: Optional[str]
    CreateTime: Optional[str]
    EnhancedMonitorService: Optional[bool]
    EnhancedSecurityService: Optional[bool]
    Id: Optional[str]
    ImageId: Optional[str]
    InstanceTags: Optional[Sequence["_InstanceTags"]]
    InstanceTypes: Optional[Sequence[str]]
    InternetChargeType: Optional[str]
    InternetMaxBandwidthOut: Optional[float]
    KeepImageLogin: Optional[bool]
    KeyIds: Optional[Sequence[str]]
    Password: Optional[str]
    ProjectId: Optional[float]
    PublicIpAssigned: Optional[bool]
    SecurityGroupIds: Optional[Sequence[str]]
    Status: Optional[str]
    SystemDiskSize: Optional[float]
    SystemDiskType: Optional[str]
    UserData: Optional[str]
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
            ConfigurationName=json_data.get("ConfigurationName"),
            CreateTime=json_data.get("CreateTime"),
            EnhancedMonitorService=json_data.get("EnhancedMonitorService"),
            EnhancedSecurityService=json_data.get("EnhancedSecurityService"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            InstanceTags=json_data.get("InstanceTags"),
            InstanceTypes=json_data.get("InstanceTypes"),
            InternetChargeType=json_data.get("InternetChargeType"),
            InternetMaxBandwidthOut=json_data.get("InternetMaxBandwidthOut"),
            KeepImageLogin=json_data.get("KeepImageLogin"),
            KeyIds=json_data.get("KeyIds"),
            Password=json_data.get("Password"),
            ProjectId=json_data.get("ProjectId"),
            PublicIpAssigned=json_data.get("PublicIpAssigned"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            Status=json_data.get("Status"),
            SystemDiskSize=json_data.get("SystemDiskSize"),
            SystemDiskType=json_data.get("SystemDiskType"),
            UserData=json_data.get("UserData"),
            DataDisk=json_data.get("DataDisk"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InstanceTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceTags = InstanceTags


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


