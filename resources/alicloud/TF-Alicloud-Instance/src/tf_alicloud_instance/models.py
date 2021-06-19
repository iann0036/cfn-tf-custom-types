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
    AllocatePublicIp: Optional[bool]
    AutoReleaseTime: Optional[str]
    AutoRenewPeriod: Optional[float]
    AvailabilityZone: Optional[str]
    CreditSpecification: Optional[str]
    DeletionProtection: Optional[bool]
    Description: Optional[str]
    DryRun: Optional[bool]
    ForceDelete: Optional[bool]
    HostName: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    IncludeDataDisks: Optional[bool]
    InstanceChargeType: Optional[str]
    InstanceName: Optional[str]
    InstanceType: Optional[str]
    InternetChargeType: Optional[str]
    InternetMaxBandwidthIn: Optional[float]
    InternetMaxBandwidthOut: Optional[float]
    IoOptimized: Optional[str]
    IsOutdated: Optional[bool]
    KeyName: Optional[str]
    KmsEncryptedPassword: Optional[str]
    KmsEncryptionContext: Optional[Sequence["_KmsEncryptionContextDefinition"]]
    Password: Optional[str]
    Period: Optional[float]
    PeriodUnit: Optional[str]
    PrivateIp: Optional[str]
    PublicIp: Optional[str]
    RenewalStatus: Optional[str]
    ResourceGroupId: Optional[str]
    RoleName: Optional[str]
    SecurityEnhancementStrategy: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    SpotPriceLimit: Optional[float]
    SpotStrategy: Optional[str]
    Status: Optional[str]
    SubnetId: Optional[str]
    SystemDiskAutoSnapshotPolicyId: Optional[str]
    SystemDiskCategory: Optional[str]
    SystemDiskDescription: Optional[str]
    SystemDiskName: Optional[str]
    SystemDiskPerformanceLevel: Optional[str]
    SystemDiskSize: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    UserData: Optional[str]
    VolumeTags: Optional[Sequence["_VolumeTagsDefinition"]]
    VswitchId: Optional[str]
    DataDisks: Optional[Sequence["_DataDisksDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AllocatePublicIp=json_data.get("AllocatePublicIp"),
            AutoReleaseTime=json_data.get("AutoReleaseTime"),
            AutoRenewPeriod=json_data.get("AutoRenewPeriod"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            CreditSpecification=json_data.get("CreditSpecification"),
            DeletionProtection=json_data.get("DeletionProtection"),
            Description=json_data.get("Description"),
            DryRun=json_data.get("DryRun"),
            ForceDelete=json_data.get("ForceDelete"),
            HostName=json_data.get("HostName"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            IncludeDataDisks=json_data.get("IncludeDataDisks"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            InstanceName=json_data.get("InstanceName"),
            InstanceType=json_data.get("InstanceType"),
            InternetChargeType=json_data.get("InternetChargeType"),
            InternetMaxBandwidthIn=json_data.get("InternetMaxBandwidthIn"),
            InternetMaxBandwidthOut=json_data.get("InternetMaxBandwidthOut"),
            IoOptimized=json_data.get("IoOptimized"),
            IsOutdated=json_data.get("IsOutdated"),
            KeyName=json_data.get("KeyName"),
            KmsEncryptedPassword=json_data.get("KmsEncryptedPassword"),
            KmsEncryptionContext=deserialize_list(json_data.get("KmsEncryptionContext"), KmsEncryptionContextDefinition),
            Password=json_data.get("Password"),
            Period=json_data.get("Period"),
            PeriodUnit=json_data.get("PeriodUnit"),
            PrivateIp=json_data.get("PrivateIp"),
            PublicIp=json_data.get("PublicIp"),
            RenewalStatus=json_data.get("RenewalStatus"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            RoleName=json_data.get("RoleName"),
            SecurityEnhancementStrategy=json_data.get("SecurityEnhancementStrategy"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SpotPriceLimit=json_data.get("SpotPriceLimit"),
            SpotStrategy=json_data.get("SpotStrategy"),
            Status=json_data.get("Status"),
            SubnetId=json_data.get("SubnetId"),
            SystemDiskAutoSnapshotPolicyId=json_data.get("SystemDiskAutoSnapshotPolicyId"),
            SystemDiskCategory=json_data.get("SystemDiskCategory"),
            SystemDiskDescription=json_data.get("SystemDiskDescription"),
            SystemDiskName=json_data.get("SystemDiskName"),
            SystemDiskPerformanceLevel=json_data.get("SystemDiskPerformanceLevel"),
            SystemDiskSize=json_data.get("SystemDiskSize"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            UserData=json_data.get("UserData"),
            VolumeTags=deserialize_list(json_data.get("VolumeTags"), VolumeTagsDefinition),
            VswitchId=json_data.get("VswitchId"),
            DataDisks=deserialize_list(json_data.get("DataDisks"), DataDisksDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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
class VolumeTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeTagsDefinition = VolumeTagsDefinition


@dataclass
class DataDisksDefinition(BaseModel):
    AutoSnapshotPolicyId: Optional[str]
    Category: Optional[str]
    DeleteWithInstance: Optional[bool]
    Description: Optional[str]
    Encrypted: Optional[bool]
    KmsKeyId: Optional[str]
    Name: Optional[str]
    PerformanceLevel: Optional[str]
    Size: Optional[float]
    SnapshotId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDisksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDisksDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoSnapshotPolicyId=json_data.get("AutoSnapshotPolicyId"),
            Category=json_data.get("Category"),
            DeleteWithInstance=json_data.get("DeleteWithInstance"),
            Description=json_data.get("Description"),
            Encrypted=json_data.get("Encrypted"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Name=json_data.get("Name"),
            PerformanceLevel=json_data.get("PerformanceLevel"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDisksDefinition = DataDisksDefinition


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


