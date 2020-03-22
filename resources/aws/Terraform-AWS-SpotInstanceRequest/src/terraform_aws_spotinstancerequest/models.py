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
    Ami: Optional[str]
    Arn: Optional[str]
    AssociatePublicIpAddress: Optional[bool]
    AvailabilityZone: Optional[str]
    BlockDurationMinutes: Optional[float]
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
    InstanceInterruptionBehaviour: Optional[str]
    InstanceState: Optional[str]
    InstanceType: Optional[str]
    Ipv6AddressCount: Optional[float]
    Ipv6Addresses: Optional[Sequence[str]]
    KeyName: Optional[str]
    LaunchGroup: Optional[str]
    Monitoring: Optional[bool]
    NetworkInterfaceId: Optional[str]
    PasswordData: Optional[str]
    PlacementGroup: Optional[str]
    PrimaryNetworkInterfaceId: Optional[str]
    PrivateDns: Optional[str]
    PrivateIp: Optional[str]
    PublicDns: Optional[str]
    PublicIp: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    SourceDestCheck: Optional[bool]
    SpotBidStatus: Optional[str]
    SpotInstanceId: Optional[str]
    SpotPrice: Optional[str]
    SpotRequestState: Optional[str]
    SpotType: Optional[str]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Tenancy: Optional[str]
    UserData: Optional[str]
    UserDataBase64: Optional[str]
    ValidFrom: Optional[str]
    ValidUntil: Optional[str]
    VolumeTags: Optional[Sequence["_VolumeTags"]]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    WaitForFulfillment: Optional[bool]
    CreditSpecification: Optional[Sequence["_CreditSpecification"]]
    EbsBlockDevice: Optional[Sequence["_EbsBlockDevice"]]
    EphemeralBlockDevice: Optional[Sequence["_EphemeralBlockDevice"]]
    NetworkInterface: Optional[Sequence["_NetworkInterface"]]
    RootBlockDevice: Optional[Sequence["_RootBlockDevice"]]
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
            Ami=json_data.get("Ami"),
            Arn=json_data.get("Arn"),
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            BlockDurationMinutes=json_data.get("BlockDurationMinutes"),
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
            InstanceInterruptionBehaviour=json_data.get("InstanceInterruptionBehaviour"),
            InstanceState=json_data.get("InstanceState"),
            InstanceType=json_data.get("InstanceType"),
            Ipv6AddressCount=json_data.get("Ipv6AddressCount"),
            Ipv6Addresses=json_data.get("Ipv6Addresses"),
            KeyName=json_data.get("KeyName"),
            LaunchGroup=json_data.get("LaunchGroup"),
            Monitoring=json_data.get("Monitoring"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            PasswordData=json_data.get("PasswordData"),
            PlacementGroup=json_data.get("PlacementGroup"),
            PrimaryNetworkInterfaceId=json_data.get("PrimaryNetworkInterfaceId"),
            PrivateDns=json_data.get("PrivateDns"),
            PrivateIp=json_data.get("PrivateIp"),
            PublicDns=json_data.get("PublicDns"),
            PublicIp=json_data.get("PublicIp"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SourceDestCheck=json_data.get("SourceDestCheck"),
            SpotBidStatus=json_data.get("SpotBidStatus"),
            SpotInstanceId=json_data.get("SpotInstanceId"),
            SpotPrice=json_data.get("SpotPrice"),
            SpotRequestState=json_data.get("SpotRequestState"),
            SpotType=json_data.get("SpotType"),
            SubnetId=json_data.get("SubnetId"),
            Tags=json_data.get("Tags"),
            Tenancy=json_data.get("Tenancy"),
            UserData=json_data.get("UserData"),
            UserDataBase64=json_data.get("UserDataBase64"),
            ValidFrom=json_data.get("ValidFrom"),
            ValidUntil=json_data.get("ValidUntil"),
            VolumeTags=json_data.get("VolumeTags"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            WaitForFulfillment=json_data.get("WaitForFulfillment"),
            CreditSpecification=json_data.get("CreditSpecification"),
            EbsBlockDevice=json_data.get("EbsBlockDevice"),
            EphemeralBlockDevice=json_data.get("EphemeralBlockDevice"),
            NetworkInterface=json_data.get("NetworkInterface"),
            RootBlockDevice=json_data.get("RootBlockDevice"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class VolumeTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeTags = VolumeTags


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
class EbsBlockDevice:
    DeleteOnTermination: Optional[bool]
    DeviceName: Optional[str]
    Encrypted: Optional[bool]
    Iops: Optional[float]
    KmsKeyId: Optional[str]
    SnapshotId: Optional[str]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsBlockDevice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsBlockDevice"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            DeviceName=json_data.get("DeviceName"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SnapshotId=json_data.get("SnapshotId"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsBlockDevice = EbsBlockDevice


@dataclass
class EphemeralBlockDevice:
    DeviceName: Optional[str]
    NoDevice: Optional[bool]
    VirtualName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EphemeralBlockDevice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EphemeralBlockDevice"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            NoDevice=json_data.get("NoDevice"),
            VirtualName=json_data.get("VirtualName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EphemeralBlockDevice = EphemeralBlockDevice


@dataclass
class NetworkInterface:
    DeleteOnTermination: Optional[bool]
    DeviceIndex: Optional[float]
    NetworkInterfaceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterface"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            DeviceIndex=json_data.get("DeviceIndex"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterface = NetworkInterface


@dataclass
class RootBlockDevice:
    DeleteOnTermination: Optional[bool]
    Encrypted: Optional[bool]
    Iops: Optional[float]
    KmsKeyId: Optional[str]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RootBlockDevice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RootBlockDevice"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RootBlockDevice = RootBlockDevice


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


