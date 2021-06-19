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
    Ami: Optional[str]
    Arn: Optional[str]
    AssociatePublicIpAddress: Optional[bool]
    AvailabilityZone: Optional[str]
    CpuCoreCount: Optional[float]
    CpuThreadsPerCore: Optional[float]
    DisableApiTermination: Optional[bool]
    EbsOptimized: Optional[bool]
    GetPasswordData: Optional[bool]
    Hibernation: Optional[bool]
    HostId: Optional[str]
    IamInstanceProfile: Optional[str]
    Id: Optional[str]
    InstanceInitiatedShutdownBehavior: Optional[str]
    InstanceState: Optional[str]
    InstanceType: Optional[str]
    Ipv6AddressCount: Optional[float]
    Ipv6Addresses: Optional[Sequence[str]]
    KeyName: Optional[str]
    Monitoring: Optional[bool]
    OutpostArn: Optional[str]
    PasswordData: Optional[str]
    PlacementGroup: Optional[str]
    PrimaryNetworkInterfaceId: Optional[str]
    PrivateDns: Optional[str]
    PrivateIp: Optional[str]
    PublicDns: Optional[str]
    PublicIp: Optional[str]
    SecondaryPrivateIps: Optional[Sequence[str]]
    SecurityGroups: Optional[Sequence[str]]
    SourceDestCheck: Optional[bool]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Tenancy: Optional[str]
    UserData: Optional[str]
    UserDataBase64: Optional[str]
    VolumeTags: Optional[Sequence["_VolumeTagsDefinition"]]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    CapacityReservationSpecification: Optional[Sequence["_CapacityReservationSpecificationDefinition"]]
    CreditSpecification: Optional[Sequence["_CreditSpecificationDefinition"]]
    EbsBlockDevice: Optional[Sequence["_EbsBlockDeviceDefinition"]]
    EnclaveOptions: Optional[Sequence["_EnclaveOptionsDefinition"]]
    EphemeralBlockDevice: Optional[Sequence["_EphemeralBlockDeviceDefinition"]]
    MetadataOptions: Optional[Sequence["_MetadataOptionsDefinition"]]
    NetworkInterface: Optional[Sequence["_NetworkInterfaceDefinition"]]
    RootBlockDevice: Optional[Sequence["_RootBlockDeviceDefinition"]]
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
            Ami=json_data.get("Ami"),
            Arn=json_data.get("Arn"),
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            CpuCoreCount=json_data.get("CpuCoreCount"),
            CpuThreadsPerCore=json_data.get("CpuThreadsPerCore"),
            DisableApiTermination=json_data.get("DisableApiTermination"),
            EbsOptimized=json_data.get("EbsOptimized"),
            GetPasswordData=json_data.get("GetPasswordData"),
            Hibernation=json_data.get("Hibernation"),
            HostId=json_data.get("HostId"),
            IamInstanceProfile=json_data.get("IamInstanceProfile"),
            Id=json_data.get("Id"),
            InstanceInitiatedShutdownBehavior=json_data.get("InstanceInitiatedShutdownBehavior"),
            InstanceState=json_data.get("InstanceState"),
            InstanceType=json_data.get("InstanceType"),
            Ipv6AddressCount=json_data.get("Ipv6AddressCount"),
            Ipv6Addresses=json_data.get("Ipv6Addresses"),
            KeyName=json_data.get("KeyName"),
            Monitoring=json_data.get("Monitoring"),
            OutpostArn=json_data.get("OutpostArn"),
            PasswordData=json_data.get("PasswordData"),
            PlacementGroup=json_data.get("PlacementGroup"),
            PrimaryNetworkInterfaceId=json_data.get("PrimaryNetworkInterfaceId"),
            PrivateDns=json_data.get("PrivateDns"),
            PrivateIp=json_data.get("PrivateIp"),
            PublicDns=json_data.get("PublicDns"),
            PublicIp=json_data.get("PublicIp"),
            SecondaryPrivateIps=json_data.get("SecondaryPrivateIps"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SourceDestCheck=json_data.get("SourceDestCheck"),
            SubnetId=json_data.get("SubnetId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Tenancy=json_data.get("Tenancy"),
            UserData=json_data.get("UserData"),
            UserDataBase64=json_data.get("UserDataBase64"),
            VolumeTags=deserialize_list(json_data.get("VolumeTags"), VolumeTagsDefinition),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            CapacityReservationSpecification=deserialize_list(json_data.get("CapacityReservationSpecification"), CapacityReservationSpecificationDefinition),
            CreditSpecification=deserialize_list(json_data.get("CreditSpecification"), CreditSpecificationDefinition),
            EbsBlockDevice=deserialize_list(json_data.get("EbsBlockDevice"), EbsBlockDeviceDefinition),
            EnclaveOptions=deserialize_list(json_data.get("EnclaveOptions"), EnclaveOptionsDefinition),
            EphemeralBlockDevice=deserialize_list(json_data.get("EphemeralBlockDevice"), EphemeralBlockDeviceDefinition),
            MetadataOptions=deserialize_list(json_data.get("MetadataOptions"), MetadataOptionsDefinition),
            NetworkInterface=deserialize_list(json_data.get("NetworkInterface"), NetworkInterfaceDefinition),
            RootBlockDevice=deserialize_list(json_data.get("RootBlockDevice"), RootBlockDeviceDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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
class EbsBlockDeviceDefinition(BaseModel):
    DeleteOnTermination: Optional[bool]
    DeviceName: Optional[str]
    Encrypted: Optional[bool]
    Iops: Optional[float]
    KmsKeyId: Optional[str]
    SnapshotId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition2"]]
    Throughput: Optional[float]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsBlockDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsBlockDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            DeviceName=json_data.get("DeviceName"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SnapshotId=json_data.get("SnapshotId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition2),
            Throughput=json_data.get("Throughput"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsBlockDeviceDefinition = EbsBlockDeviceDefinition


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
class EphemeralBlockDeviceDefinition(BaseModel):
    DeviceName: Optional[str]
    NoDevice: Optional[bool]
    VirtualName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EphemeralBlockDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EphemeralBlockDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            NoDevice=json_data.get("NoDevice"),
            VirtualName=json_data.get("VirtualName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EphemeralBlockDeviceDefinition = EphemeralBlockDeviceDefinition


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
class NetworkInterfaceDefinition(BaseModel):
    DeleteOnTermination: Optional[bool]
    DeviceIndex: Optional[float]
    NetworkInterfaceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            DeviceIndex=json_data.get("DeviceIndex"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfaceDefinition = NetworkInterfaceDefinition


@dataclass
class RootBlockDeviceDefinition(BaseModel):
    DeleteOnTermination: Optional[bool]
    Encrypted: Optional[bool]
    Iops: Optional[float]
    KmsKeyId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition3"]]
    Throughput: Optional[float]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RootBlockDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RootBlockDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition3),
            Throughput=json_data.get("Throughput"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RootBlockDeviceDefinition = RootBlockDeviceDefinition


@dataclass
class TagsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition3 = TagsDefinition3


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


