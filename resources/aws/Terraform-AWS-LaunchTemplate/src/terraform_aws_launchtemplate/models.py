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
    Arn: Optional[str]
    DefaultVersion: Optional[float]
    Description: Optional[str]
    DisableApiTermination: Optional[bool]
    EbsOptimized: Optional[str]
    ImageId: Optional[str]
    InstanceInitiatedShutdownBehavior: Optional[str]
    InstanceType: Optional[str]
    KernelId: Optional[str]
    KeyName: Optional[str]
    LatestVersion: Optional[float]
    Name: Optional[str]
    NamePrefix: Optional[str]
    RamDiskId: Optional[str]
    SecurityGroupNames: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    UserData: Optional[str]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    BlockDeviceMappings: Optional[Sequence["_BlockDeviceMappings"]]
    CapacityReservationSpecification: Optional[Sequence["_CapacityReservationSpecification"]]
    CpuOptions: Optional[Sequence["_CpuOptions"]]
    CreditSpecification: Optional[Sequence["_CreditSpecification"]]
    ElasticGpuSpecifications: Optional[Sequence["_ElasticGpuSpecifications"]]
    ElasticInferenceAccelerator: Optional[Sequence["_ElasticInferenceAccelerator"]]
    IamInstanceProfile: Optional[Sequence["_IamInstanceProfile"]]
    InstanceMarketOptions: Optional[Sequence["_InstanceMarketOptions"]]
    LicenseSpecification: Optional[Sequence["_LicenseSpecification"]]
    Monitoring: Optional[Sequence["_Monitoring"]]
    NetworkInterfaces: Optional[Sequence["_NetworkInterfaces"]]
    Placement: Optional[Sequence["_Placement"]]
    TagSpecifications: Optional[Sequence["_TagSpecifications"]]
    Ebs: Optional[Sequence["_Ebs"]]
    CapacityReservationTarget: Optional[Sequence["_CapacityReservationTarget"]]
    SpotOptions: Optional[Sequence["_SpotOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            DefaultVersion=json_data.get("DefaultVersion"),
            Description=json_data.get("Description"),
            DisableApiTermination=json_data.get("DisableApiTermination"),
            EbsOptimized=json_data.get("EbsOptimized"),
            ImageId=json_data.get("ImageId"),
            InstanceInitiatedShutdownBehavior=json_data.get("InstanceInitiatedShutdownBehavior"),
            InstanceType=json_data.get("InstanceType"),
            KernelId=json_data.get("KernelId"),
            KeyName=json_data.get("KeyName"),
            LatestVersion=json_data.get("LatestVersion"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            RamDiskId=json_data.get("RamDiskId"),
            SecurityGroupNames=json_data.get("SecurityGroupNames"),
            Tags=json_data.get("Tags"),
            UserData=json_data.get("UserData"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            BlockDeviceMappings=json_data.get("BlockDeviceMappings"),
            CapacityReservationSpecification=json_data.get("CapacityReservationSpecification"),
            CpuOptions=json_data.get("CpuOptions"),
            CreditSpecification=json_data.get("CreditSpecification"),
            ElasticGpuSpecifications=json_data.get("ElasticGpuSpecifications"),
            ElasticInferenceAccelerator=json_data.get("ElasticInferenceAccelerator"),
            IamInstanceProfile=json_data.get("IamInstanceProfile"),
            InstanceMarketOptions=json_data.get("InstanceMarketOptions"),
            LicenseSpecification=json_data.get("LicenseSpecification"),
            Monitoring=json_data.get("Monitoring"),
            NetworkInterfaces=json_data.get("NetworkInterfaces"),
            Placement=json_data.get("Placement"),
            TagSpecifications=json_data.get("TagSpecifications"),
            Ebs=json_data.get("Ebs"),
            CapacityReservationTarget=json_data.get("CapacityReservationTarget"),
            SpotOptions=json_data.get("SpotOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class BlockDeviceMappings:
    DeviceName: Optional[str]
    NoDevice: Optional[str]
    VirtualName: Optional[str]
    Ebs: Optional[Sequence["_Ebs"]]

    @classmethod
    def _deserialize(
        cls: Type["_BlockDeviceMappings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockDeviceMappings"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            NoDevice=json_data.get("NoDevice"),
            VirtualName=json_data.get("VirtualName"),
            Ebs=json_data.get("Ebs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockDeviceMappings = BlockDeviceMappings


@dataclass
class Ebs:
    DeleteOnTermination: Optional[str]
    Encrypted: Optional[str]
    Iops: Optional[float]
    KmsKeyId: Optional[str]
    SnapshotId: Optional[str]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ebs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ebs"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SnapshotId=json_data.get("SnapshotId"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ebs = Ebs


@dataclass
class CapacityReservationSpecification:
    CapacityReservationPreference: Optional[str]
    CapacityReservationTarget: Optional[Sequence["_CapacityReservationTarget"]]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityReservationSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityReservationSpecification"]:
        if not json_data:
            return None
        return cls(
            CapacityReservationPreference=json_data.get("CapacityReservationPreference"),
            CapacityReservationTarget=json_data.get("CapacityReservationTarget"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityReservationSpecification = CapacityReservationSpecification


@dataclass
class CapacityReservationTarget:
    CapacityReservationId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityReservationTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityReservationTarget"]:
        if not json_data:
            return None
        return cls(
            CapacityReservationId=json_data.get("CapacityReservationId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityReservationTarget = CapacityReservationTarget


@dataclass
class CpuOptions:
    CoreCount: Optional[float]
    ThreadsPerCore: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CpuOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CpuOptions"]:
        if not json_data:
            return None
        return cls(
            CoreCount=json_data.get("CoreCount"),
            ThreadsPerCore=json_data.get("ThreadsPerCore"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CpuOptions = CpuOptions


@dataclass
class CreditSpecification:
    CpuCredits: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CreditSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreditSpecification"]:
        if not json_data:
            return None
        return cls(
            CpuCredits=json_data.get("CpuCredits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreditSpecification = CreditSpecification


@dataclass
class ElasticGpuSpecifications:
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticGpuSpecifications"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticGpuSpecifications"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticGpuSpecifications = ElasticGpuSpecifications


@dataclass
class ElasticInferenceAccelerator:
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticInferenceAccelerator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticInferenceAccelerator"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticInferenceAccelerator = ElasticInferenceAccelerator


@dataclass
class IamInstanceProfile:
    Arn: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IamInstanceProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IamInstanceProfile"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IamInstanceProfile = IamInstanceProfile


@dataclass
class InstanceMarketOptions:
    MarketType: Optional[str]
    SpotOptions: Optional[Sequence["_SpotOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceMarketOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceMarketOptions"]:
        if not json_data:
            return None
        return cls(
            MarketType=json_data.get("MarketType"),
            SpotOptions=json_data.get("SpotOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceMarketOptions = InstanceMarketOptions


@dataclass
class SpotOptions:
    BlockDurationMinutes: Optional[float]
    InstanceInterruptionBehavior: Optional[str]
    MaxPrice: Optional[str]
    SpotInstanceType: Optional[str]
    ValidUntil: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SpotOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotOptions"]:
        if not json_data:
            return None
        return cls(
            BlockDurationMinutes=json_data.get("BlockDurationMinutes"),
            InstanceInterruptionBehavior=json_data.get("InstanceInterruptionBehavior"),
            MaxPrice=json_data.get("MaxPrice"),
            SpotInstanceType=json_data.get("SpotInstanceType"),
            ValidUntil=json_data.get("ValidUntil"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotOptions = SpotOptions


@dataclass
class LicenseSpecification:
    LicenseConfigurationArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LicenseSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LicenseSpecification"]:
        if not json_data:
            return None
        return cls(
            LicenseConfigurationArn=json_data.get("LicenseConfigurationArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LicenseSpecification = LicenseSpecification


@dataclass
class Monitoring:
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Monitoring"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Monitoring"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Monitoring = Monitoring


@dataclass
class NetworkInterfaces:
    AssociatePublicIpAddress: Optional[str]
    DeleteOnTermination: Optional[bool]
    Description: Optional[str]
    DeviceIndex: Optional[float]
    Ipv4AddressCount: Optional[float]
    Ipv4Addresses: Optional[Sequence[str]]
    Ipv6AddressCount: Optional[float]
    Ipv6Addresses: Optional[Sequence[str]]
    NetworkInterfaceId: Optional[str]
    PrivateIpAddress: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaces"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaces"]:
        if not json_data:
            return None
        return cls(
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Description=json_data.get("Description"),
            DeviceIndex=json_data.get("DeviceIndex"),
            Ipv4AddressCount=json_data.get("Ipv4AddressCount"),
            Ipv4Addresses=json_data.get("Ipv4Addresses"),
            Ipv6AddressCount=json_data.get("Ipv6AddressCount"),
            Ipv6Addresses=json_data.get("Ipv6Addresses"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfaces = NetworkInterfaces


@dataclass
class Placement:
    Affinity: Optional[str]
    AvailabilityZone: Optional[str]
    GroupName: Optional[str]
    HostId: Optional[str]
    SpreadDomain: Optional[str]
    Tenancy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Placement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Placement"]:
        if not json_data:
            return None
        return cls(
            Affinity=json_data.get("Affinity"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            GroupName=json_data.get("GroupName"),
            HostId=json_data.get("HostId"),
            SpreadDomain=json_data.get("SpreadDomain"),
            Tenancy=json_data.get("Tenancy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Placement = Placement


@dataclass
class TagSpecifications:
    ResourceType: Optional[str]
    Tags: Optional[Sequence["_Tags2"]]

    @classmethod
    def _deserialize(
        cls: Type["_TagSpecifications"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagSpecifications"]:
        if not json_data:
            return None
        return cls(
            ResourceType=json_data.get("ResourceType"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagSpecifications = TagSpecifications


@dataclass
class Tags2:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags2"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags2 = Tags2


