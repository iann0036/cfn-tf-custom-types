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
    KmsEncryptionContext: Optional[Sequence["_KmsEncryptionContext"]]
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
    SystemDiskSize: Optional[float]
    Tags: Optional[Sequence["_Tags"]]
    UserData: Optional[str]
    VolumeTags: Optional[Sequence["_VolumeTags"]]
    VswitchId: Optional[str]
    DataDisks: Optional[Sequence["_DataDisks"]]
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
            KmsEncryptionContext=json_data.get("KmsEncryptionContext"),
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
            SystemDiskSize=json_data.get("SystemDiskSize"),
            Tags=json_data.get("Tags"),
            UserData=json_data.get("UserData"),
            VolumeTags=json_data.get("VolumeTags"),
            VswitchId=json_data.get("VswitchId"),
            DataDisks=json_data.get("DataDisks"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
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
class VolumeTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeTags = VolumeTags


@dataclass
class DataDisks:
    AutoSnapshotPolicyId: Optional[str]
    Category: Optional[str]
    DeleteWithInstance: Optional[bool]
    Description: Optional[str]
    Encrypted: Optional[bool]
    Name: Optional[str]
    Size: Optional[float]
    SnapshotId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDisks"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDisks"]:
        if not json_data:
            return None
        return cls(
            AutoSnapshotPolicyId=json_data.get("AutoSnapshotPolicyId"),
            Category=json_data.get("Category"),
            DeleteWithInstance=json_data.get("DeleteWithInstance"),
            Description=json_data.get("Description"),
            Encrypted=json_data.get("Encrypted"),
            Name=json_data.get("Name"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDisks = DataDisks


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


