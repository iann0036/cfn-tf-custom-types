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
    Arn: Optional[str]
    DefaultVersion: Optional[float]
    Description: Optional[str]
    DisableApiTermination: Optional[bool]
    EbsOptimized: Optional[str]
    Id: Optional[str]
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
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    UpdateDefaultVersion: Optional[bool]
    UserData: Optional[str]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    BlockDeviceMappings: Optional[Sequence["_BlockDeviceMappingsDefinition"]]
    CapacityReservationSpecification: Optional[Sequence["_CapacityReservationSpecificationDefinition"]]
    CpuOptions: Optional[Sequence["_CpuOptionsDefinition"]]
    CreditSpecification: Optional[Sequence["_CreditSpecificationDefinition"]]
    ElasticGpuSpecifications: Optional[Sequence["_ElasticGpuSpecificationsDefinition"]]
    ElasticInferenceAccelerator: Optional[Sequence["_ElasticInferenceAcceleratorDefinition"]]
    EnclaveOptions: Optional[Sequence["_EnclaveOptionsDefinition"]]
    HibernationOptions: Optional[Sequence["_HibernationOptionsDefinition"]]
    IamInstanceProfile: Optional[Sequence["_IamInstanceProfileDefinition"]]
    InstanceMarketOptions: Optional[Sequence["_InstanceMarketOptionsDefinition"]]
    LicenseSpecification: Optional[Sequence["_LicenseSpecificationDefinition"]]
    MetadataOptions: Optional[Sequence["_MetadataOptionsDefinition"]]
    Monitoring: Optional[Sequence["_MonitoringDefinition"]]
    NetworkInterfaces: Optional[Sequence["_NetworkInterfacesDefinition"]]
    Placement: Optional[Sequence["_PlacementDefinition"]]
    TagSpecifications: Optional[Sequence["_TagSpecificationsDefinition"]]

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
            Arn=json_data.get("Arn"),
            DefaultVersion=json_data.get("DefaultVersion"),
            Description=json_data.get("Description"),
            DisableApiTermination=json_data.get("DisableApiTermination"),
            EbsOptimized=json_data.get("EbsOptimized"),
            Id=json_data.get("Id"),
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
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            UpdateDefaultVersion=json_data.get("UpdateDefaultVersion"),
            UserData=json_data.get("UserData"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            BlockDeviceMappings=deserialize_list(json_data.get("BlockDeviceMappings"), BlockDeviceMappingsDefinition),
            CapacityReservationSpecification=deserialize_list(json_data.get("CapacityReservationSpecification"), CapacityReservationSpecificationDefinition),
            CpuOptions=deserialize_list(json_data.get("CpuOptions"), CpuOptionsDefinition),
            CreditSpecification=deserialize_list(json_data.get("CreditSpecification"), CreditSpecificationDefinition),
            ElasticGpuSpecifications=deserialize_list(json_data.get("ElasticGpuSpecifications"), ElasticGpuSpecificationsDefinition),
            ElasticInferenceAccelerator=deserialize_list(json_data.get("ElasticInferenceAccelerator"), ElasticInferenceAcceleratorDefinition),
            EnclaveOptions=deserialize_list(json_data.get("EnclaveOptions"), EnclaveOptionsDefinition),
            HibernationOptions=deserialize_list(json_data.get("HibernationOptions"), HibernationOptionsDefinition),
            IamInstanceProfile=deserialize_list(json_data.get("IamInstanceProfile"), IamInstanceProfileDefinition),
            InstanceMarketOptions=deserialize_list(json_data.get("InstanceMarketOptions"), InstanceMarketOptionsDefinition),
            LicenseSpecification=deserialize_list(json_data.get("LicenseSpecification"), LicenseSpecificationDefinition),
            MetadataOptions=deserialize_list(json_data.get("MetadataOptions"), MetadataOptionsDefinition),
            Monitoring=deserialize_list(json_data.get("Monitoring"), MonitoringDefinition),
            NetworkInterfaces=deserialize_list(json_data.get("NetworkInterfaces"), NetworkInterfacesDefinition),
            Placement=deserialize_list(json_data.get("Placement"), PlacementDefinition),
            TagSpecifications=deserialize_list(json_data.get("TagSpecifications"), TagSpecificationsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class BlockDeviceMappingsDefinition(BaseModel):
    DeviceName: Optional[str]
    NoDevice: Optional[str]
    VirtualName: Optional[str]
    Ebs: Optional[Sequence["_EbsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BlockDeviceMappingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockDeviceMappingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            NoDevice=json_data.get("NoDevice"),
            VirtualName=json_data.get("VirtualName"),
            Ebs=deserialize_list(json_data.get("Ebs"), EbsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockDeviceMappingsDefinition = BlockDeviceMappingsDefinition


@dataclass
class EbsDefinition(BaseModel):
    DeleteOnTermination: Optional[str]
    Encrypted: Optional[str]
    Iops: Optional[float]
    KmsKeyId: Optional[str]
    SnapshotId: Optional[str]
    Throughput: Optional[float]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SnapshotId=json_data.get("SnapshotId"),
            Throughput=json_data.get("Throughput"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsDefinition = EbsDefinition


@dataclass
class CapacityReservationSpecificationDefinition(BaseModel):
    CapacityReservationPreference: Optional[str]
    CapacityReservationTarget: Optional[Sequence["_CapacityReservationTargetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityReservationSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityReservationSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            CapacityReservationPreference=json_data.get("CapacityReservationPreference"),
            CapacityReservationTarget=deserialize_list(json_data.get("CapacityReservationTarget"), CapacityReservationTargetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityReservationSpecificationDefinition = CapacityReservationSpecificationDefinition


@dataclass
class CapacityReservationTargetDefinition(BaseModel):
    CapacityReservationId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityReservationTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityReservationTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            CapacityReservationId=json_data.get("CapacityReservationId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityReservationTargetDefinition = CapacityReservationTargetDefinition


@dataclass
class CpuOptionsDefinition(BaseModel):
    CoreCount: Optional[float]
    ThreadsPerCore: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CpuOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CpuOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            CoreCount=json_data.get("CoreCount"),
            ThreadsPerCore=json_data.get("ThreadsPerCore"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CpuOptionsDefinition = CpuOptionsDefinition


@dataclass
class CreditSpecificationDefinition(BaseModel):
    CpuCredits: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CreditSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreditSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            CpuCredits=json_data.get("CpuCredits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreditSpecificationDefinition = CreditSpecificationDefinition


@dataclass
class ElasticGpuSpecificationsDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticGpuSpecificationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticGpuSpecificationsDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticGpuSpecificationsDefinition = ElasticGpuSpecificationsDefinition


@dataclass
class ElasticInferenceAcceleratorDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticInferenceAcceleratorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticInferenceAcceleratorDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticInferenceAcceleratorDefinition = ElasticInferenceAcceleratorDefinition


@dataclass
class EnclaveOptionsDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EnclaveOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnclaveOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnclaveOptionsDefinition = EnclaveOptionsDefinition


@dataclass
class HibernationOptionsDefinition(BaseModel):
    Configured: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_HibernationOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HibernationOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Configured=json_data.get("Configured"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HibernationOptionsDefinition = HibernationOptionsDefinition


@dataclass
class IamInstanceProfileDefinition(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IamInstanceProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IamInstanceProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IamInstanceProfileDefinition = IamInstanceProfileDefinition


@dataclass
class InstanceMarketOptionsDefinition(BaseModel):
    MarketType: Optional[str]
    SpotOptions: Optional[Sequence["_SpotOptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceMarketOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceMarketOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MarketType=json_data.get("MarketType"),
            SpotOptions=deserialize_list(json_data.get("SpotOptions"), SpotOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceMarketOptionsDefinition = InstanceMarketOptionsDefinition


@dataclass
class SpotOptionsDefinition(BaseModel):
    BlockDurationMinutes: Optional[float]
    InstanceInterruptionBehavior: Optional[str]
    MaxPrice: Optional[str]
    SpotInstanceType: Optional[str]
    ValidUntil: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SpotOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotOptionsDefinition"]:
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
_SpotOptionsDefinition = SpotOptionsDefinition


@dataclass
class LicenseSpecificationDefinition(BaseModel):
    LicenseConfigurationArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LicenseSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LicenseSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            LicenseConfigurationArn=json_data.get("LicenseConfigurationArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LicenseSpecificationDefinition = LicenseSpecificationDefinition


@dataclass
class MetadataOptionsDefinition(BaseModel):
    HttpEndpoint: Optional[str]
    HttpPutResponseHopLimit: Optional[float]
    HttpTokens: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            HttpEndpoint=json_data.get("HttpEndpoint"),
            HttpPutResponseHopLimit=json_data.get("HttpPutResponseHopLimit"),
            HttpTokens=json_data.get("HttpTokens"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataOptionsDefinition = MetadataOptionsDefinition


@dataclass
class MonitoringDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_MonitoringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitoringDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitoringDefinition = MonitoringDefinition


@dataclass
class NetworkInterfacesDefinition(BaseModel):
    AssociateCarrierIpAddress: Optional[str]
    AssociatePublicIpAddress: Optional[str]
    DeleteOnTermination: Optional[str]
    Description: Optional[str]
    DeviceIndex: Optional[float]
    InterfaceType: Optional[str]
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
        cls: Type["_NetworkInterfacesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfacesDefinition"]:
        if not json_data:
            return None
        return cls(
            AssociateCarrierIpAddress=json_data.get("AssociateCarrierIpAddress"),
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Description=json_data.get("Description"),
            DeviceIndex=json_data.get("DeviceIndex"),
            InterfaceType=json_data.get("InterfaceType"),
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
_NetworkInterfacesDefinition = NetworkInterfacesDefinition


@dataclass
class PlacementDefinition(BaseModel):
    Affinity: Optional[str]
    AvailabilityZone: Optional[str]
    GroupName: Optional[str]
    HostId: Optional[str]
    HostResourceGroupArn: Optional[str]
    PartitionNumber: Optional[float]
    SpreadDomain: Optional[str]
    Tenancy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementDefinition"]:
        if not json_data:
            return None
        return cls(
            Affinity=json_data.get("Affinity"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            GroupName=json_data.get("GroupName"),
            HostId=json_data.get("HostId"),
            HostResourceGroupArn=json_data.get("HostResourceGroupArn"),
            PartitionNumber=json_data.get("PartitionNumber"),
            SpreadDomain=json_data.get("SpreadDomain"),
            Tenancy=json_data.get("Tenancy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementDefinition = PlacementDefinition


@dataclass
class TagSpecificationsDefinition(BaseModel):
    ResourceType: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_TagSpecificationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagSpecificationsDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceType=json_data.get("ResourceType"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagSpecificationsDefinition = TagSpecificationsDefinition


@dataclass
class TagsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition2 = TagsDefinition2


