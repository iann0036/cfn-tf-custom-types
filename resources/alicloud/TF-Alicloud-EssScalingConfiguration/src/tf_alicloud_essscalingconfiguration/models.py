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
    Active: Optional[bool]
    CreditSpecification: Optional[str]
    Enable: Optional[bool]
    ForceDelete: Optional[bool]
    Id: Optional[str]
    ImageId: Optional[str]
    ImageName: Optional[str]
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
    KmsEncryptionContext: Optional[Sequence["_KmsEncryptionContextDefinition"]]
    Override: Optional[bool]
    Password: Optional[str]
    PasswordInherit: Optional[bool]
    RoleName: Optional[str]
    ScalingConfigurationName: Optional[str]
    ScalingGroupId: Optional[str]
    SecurityGroupId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    Substitute: Optional[str]
    SystemDiskAutoSnapshotPolicyId: Optional[str]
    SystemDiskCategory: Optional[str]
    SystemDiskDescription: Optional[str]
    SystemDiskName: Optional[str]
    SystemDiskSize: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    UserData: Optional[str]
    DataDisk: Optional[Sequence["_DataDiskDefinition"]]

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
            Active=json_data.get("Active"),
            CreditSpecification=json_data.get("CreditSpecification"),
            Enable=json_data.get("Enable"),
            ForceDelete=json_data.get("ForceDelete"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            ImageName=json_data.get("ImageName"),
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
            KmsEncryptionContext=deserialize_list(json_data.get("KmsEncryptionContext"), KmsEncryptionContextDefinition),
            Override=json_data.get("Override"),
            Password=json_data.get("Password"),
            PasswordInherit=json_data.get("PasswordInherit"),
            RoleName=json_data.get("RoleName"),
            ScalingConfigurationName=json_data.get("ScalingConfigurationName"),
            ScalingGroupId=json_data.get("ScalingGroupId"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            Substitute=json_data.get("Substitute"),
            SystemDiskAutoSnapshotPolicyId=json_data.get("SystemDiskAutoSnapshotPolicyId"),
            SystemDiskCategory=json_data.get("SystemDiskCategory"),
            SystemDiskDescription=json_data.get("SystemDiskDescription"),
            SystemDiskName=json_data.get("SystemDiskName"),
            SystemDiskSize=json_data.get("SystemDiskSize"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            UserData=json_data.get("UserData"),
            DataDisk=deserialize_list(json_data.get("DataDisk"), DataDiskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class DataDiskDefinition(BaseModel):
    AutoSnapshotPolicyId: Optional[str]
    Category: Optional[str]
    DeleteWithInstance: Optional[bool]
    Description: Optional[str]
    Device: Optional[str]
    Encrypted: Optional[bool]
    KmsKeyId: Optional[str]
    Name: Optional[str]
    Size: Optional[float]
    SnapshotId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoSnapshotPolicyId=json_data.get("AutoSnapshotPolicyId"),
            Category=json_data.get("Category"),
            DeleteWithInstance=json_data.get("DeleteWithInstance"),
            Description=json_data.get("Description"),
            Device=json_data.get("Device"),
            Encrypted=json_data.get("Encrypted"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Name=json_data.get("Name"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDiskDefinition = DataDiskDefinition


