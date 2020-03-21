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
    Active: Optional[bool]
    Enable: Optional[bool]
    ForceDelete: Optional[bool]
    ImageId: Optional[str]
    InstanceIds: Optional[Sequence[str]]
    InstanceName: Optional[str]
    InstanceType: Optional[str]
    InstanceTypes: Optional[Sequence[str]]
    InternetChargeType: Optional[str]
    InternetMaxBandwidthIn: Optional[float]
    InternetMaxBandwidthOut: Optional[float]
    IoOptimized: Optional[str]
    IsOutdated: Optional[bool]
    KeyName: Optional[str]
    KmsEncryptedPassword: Optional[str]
    KmsEncryptionContext: Optional[Sequence["_KmsEncryptionContext"]]
    Override: Optional[bool]
    Password: Optional[str]
    PasswordInherit: Optional[bool]
    RoleName: Optional[str]
    ScalingConfigurationName: Optional[str]
    ScalingGroupId: Optional[str]
    SecurityGroupId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    Substitute: Optional[str]
    SystemDiskCategory: Optional[str]
    SystemDiskSize: Optional[float]
    Tags: Optional[Sequence["_Tags"]]
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
            Active=json_data.get("Active"),
            Enable=json_data.get("Enable"),
            ForceDelete=json_data.get("ForceDelete"),
            ImageId=json_data.get("ImageId"),
            InstanceIds=json_data.get("InstanceIds"),
            InstanceName=json_data.get("InstanceName"),
            InstanceType=json_data.get("InstanceType"),
            InstanceTypes=json_data.get("InstanceTypes"),
            InternetChargeType=json_data.get("InternetChargeType"),
            InternetMaxBandwidthIn=json_data.get("InternetMaxBandwidthIn"),
            InternetMaxBandwidthOut=json_data.get("InternetMaxBandwidthOut"),
            IoOptimized=json_data.get("IoOptimized"),
            IsOutdated=json_data.get("IsOutdated"),
            KeyName=json_data.get("KeyName"),
            KmsEncryptedPassword=json_data.get("KmsEncryptedPassword"),
            KmsEncryptionContext=json_data.get("KmsEncryptionContext"),
            Override=json_data.get("Override"),
            Password=json_data.get("Password"),
            PasswordInherit=json_data.get("PasswordInherit"),
            RoleName=json_data.get("RoleName"),
            ScalingConfigurationName=json_data.get("ScalingConfigurationName"),
            ScalingGroupId=json_data.get("ScalingGroupId"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            Substitute=json_data.get("Substitute"),
            SystemDiskCategory=json_data.get("SystemDiskCategory"),
            SystemDiskSize=json_data.get("SystemDiskSize"),
            Tags=json_data.get("Tags"),
            UserData=json_data.get("UserData"),
            DataDisk=json_data.get("DataDisk"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class DataDisk:
    Category: Optional[str]
    DeleteWithInstance: Optional[bool]
    Device: Optional[str]
    Size: Optional[float]
    SnapshotId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDisk"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            DeleteWithInstance=json_data.get("DeleteWithInstance"),
            Device=json_data.get("Device"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDisk = DataDisk


